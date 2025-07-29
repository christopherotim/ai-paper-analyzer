"""
AI分析器模块
负责使用AI分析论文内容并生成结构化摘要
"""
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Any, Optional
from pathlib import Path

from ..utils.console import ConsoleOutput
from ..utils.logger import get_logger
from ..utils.file_utils import FileManager
from ..utils.progress import ProgressManager
from ..utils.ai_client import create_retryable_client
from ..models.paper import Paper
from ..models.report import AnalysisResult, DailyReport
from .parser import ContentParser


class PaperAnalyzer:
    """
    论文AI分析器
    
    负责使用AI分析论文内容，生成结构化的分析结果
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        初始化分析器
        
        Args:
            config: 配置字典
        """
        self.config = config
        self.console = ConsoleOutput()
        self.logger = get_logger('analyzer')
        self.file_manager = FileManager('analyzer')
        self.parser = ContentParser()
        
        # 设置默认配置
        self.output_dir = config.get('output_dir', 'data/daily_reports')
        self.ai_model = config.get('ai_model', 'zhipu')
        self.use_ai = config.get('use_ai', True)
        self.max_retries = config.get('max_retries', 3)
        self.retry_delay = config.get('retry_delay', 2)
        
        # 初始化AI客户端
        self.ai_client = None
        if self.use_ai:
            try:
                self.ai_client = create_retryable_client(
                    self.ai_model,
                    max_retries=self.max_retries
                )
            except Exception as e:
                self.logger.warning(f"AI客户端初始化失败: {e}")
                self.use_ai = False
    
    def analyze_batch(self, papers: List[Paper], date: str = None, silent: bool = False) -> List[AnalysisResult]:
        """
        批量分析论文
        
        Args:
            papers: 论文列表
            date: 日期字符串（用于保存结果）
            silent: 是否静默模式
            
        Returns:
            分析结果列表
        """
        if not papers:
            if not silent:
                self.console.print_warning("没有论文需要分析")
            return []
        
        if not silent:
            self.console.print_header("AI分析生成摘要", 3)
            self.console.print_info(f"开始顺序处理 {len(papers)} 篇论文")
        
        self.logger.info(f"开始批量分析 {len(papers)} 篇论文")
        
        # 初始化进度管理器
        progress = ProgressManager(len(papers), "AI分析论文") if not silent else None
        results = []
        
        # 准备输出文件（如果提供了日期）
        final_file = None
        if date:
            final_dir = Path(self.output_dir) / 'reports'
            self.file_manager.ensure_dir(final_dir)
            final_file = final_dir / f"{date}_report.json"
            
            # 加载已存在的结果
            existing_results = self._load_existing_results(final_file)
            existing_ids = {self._extract_paper_id_from_result(r) for r in existing_results}
        else:
            existing_ids = set()
        
        # 统计变量
        processed_count = 0
        success_count = 0
        fail_count = 0
        skip_count = 0

        # 顺序处理每篇论文
        for i, paper in enumerate(papers):
            # 检查是否已经处理过
            if date and paper.id in existing_ids:
                skip_count += 1
                if not silent:
                    self.console.print_skip(f"已处理的论文: {paper.id}")
                continue

            processed_count += 1

            if not silent:
                # 显示当前处理的论文信息
                self.console.print_info(f"🔍 处理第 {i+1}/{len(papers)} 项: {paper.translation}")

                # 显示整体进度条
                progress_bar = self._create_progress_bar(i, len(papers))
                remaining_papers = len(papers) - i - 1
                estimated_remaining = remaining_papers * 15  # 假设每篇15秒
                print(f"📊 进度: {progress_bar} {i}/{len(papers)} (成功:{success_count}, 失败:{fail_count}, 跳过:{skip_count}) 预计剩余: {estimated_remaining}秒")
            
            self.logger.info(f"开始分析论文: {paper.id} - {paper.title}")
            
            try:
                # 分析单篇论文（保持与批量分析相同的静默状态）
                result = self.analyze_single(paper, silent=silent)
                
                if result:
                    # 立即保存结果（如果提供了文件路径）
                    if final_file:
                        self._save_single_result(result, final_file)

                    results.append(result)
                    success_count += 1

                    if progress:
                        progress.update(True, f"{paper.id}")

                    if not silent:
                        self.console.print_success(f"✅ 完成: {paper.id} ({i+1}/{len(papers)})")

                    self.logger.info(f"论文分析完成: {paper.id}")
                else:
                    fail_count += 1

                    if progress:
                        progress.update(False, f"{paper.id}")

                    if not silent:
                        self.console.print_error(f"❌ 失败: {paper.id} ({i+1}/{len(papers)})")

                    self.logger.error(f"论文分析失败: {paper.id}")
                    
            except Exception as e:
                fail_count += 1

                if progress:
                    progress.update(False, f"{paper.id} - {e}")

                if not silent:
                    self.console.print_error(f"❌ 异常: {paper.id} - {e}")

                self.logger.error(f"论文分析异常: {paper.id} - {e}")
        
        # 显示最终统计
        if progress:
            progress.finish()
        
        if not silent:
            # 计算实际处理的论文数（排除跳过的）
            actually_processed = processed_count

            self.console.print_summary("分析完成统计", {
                "总论文数": len(papers),
                "跳过论文": skip_count,
                "实际处理": actually_processed,
                "成功分析": success_count,
                "分析失败": fail_count,
                "成功率": f"{success_count/max(actually_processed, 1)*100:.1f}%" if actually_processed > 0 else "0.0%"
            })

        self.logger.info(f"批量分析完成，成功: {success_count}/{actually_processed}，跳过: {skip_count}")
        return results
    
    def analyze_single(self, paper: Paper, silent: bool = False) -> Optional[AnalysisResult]:
        """
        分析单篇论文
        
        Args:
            paper: 论文对象
            silent: 是否静默模式
            
        Returns:
            分析结果，失败返回None
        """
        if not self.use_ai or not self.ai_client:
            if not silent:
                self.console.print_warning("AI分析未启用，返回基础结果")
            
            # 返回基础结果
            return AnalysisResult(
                paper_id=paper.id,
                paper_url=paper.url,
                title=paper.title,
                translation=paper.translation,
                authors="",
                publish_date="",
                model_function="",
                page_content=""
            )
        
        # 添加重试机制
        max_retries = 3
        retry_delay = 2

        for attempt in range(max_retries):
            try:
                if not silent and attempt > 0:
                    self.console.print_info(f"重试第 {attempt} 次...")

                # 构建分析提示词
                prompt = self._build_analysis_prompt(paper)

                messages = [
                    {
                        "role": "user",
                        "content": [{
                            "type": "text",
                            "text": prompt
                        }]
                    }
                ]

                # 调用AI进行分析（带进度显示）
                import time
                import threading

                if not silent:
                    # 创建进度显示线程
                    progress_stop = threading.Event()
                    progress_thread = threading.Thread(
                        target=self._show_analysis_progress,
                        args=(progress_stop, f"分析论文: {paper.translation[:30]}...")
                    )
                    progress_thread.daemon = True
                    progress_thread.start()

                start_time = time.time()

                try:
                    # 使用线程超时处理（Windows兼容）
                    import concurrent.futures

                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        future = executor.submit(self.ai_client.chat, messages)
                        try:
                            response = future.result(timeout=90)  # 90秒超时
                        except concurrent.futures.TimeoutError:
                            if not silent:
                                progress_stop.set()
                                progress_thread.join(timeout=1)
                                print()  # 换行
                            raise TimeoutError(f"AI调用超时（90秒）")

                except TimeoutError:
                    raise  # 重新抛出超时异常
                finally:
                    if not silent:
                        progress_stop.set()
                        progress_thread.join(timeout=1)
                        print()  # 换行

                end_time = time.time()
                if not silent:
                    self.console.print_info(f"AI响应耗时: {end_time - start_time:.2f}秒")

                # 如果成功获得响应，跳出重试循环
                if response:
                    break
                else:
                    if attempt < max_retries - 1:
                        if not silent:
                            self.console.print_warning(f"AI响应为空，{retry_delay}秒后重试...")
                        time.sleep(retry_delay)
                        continue
                    else:
                        self.logger.error(f"AI分析失败，所有重试都返回空响应: {paper.id}")
                        return None

            except Exception as e:
                if attempt < max_retries - 1:
                    if not silent:
                        self.console.print_warning(f"AI调用异常: {e}，{retry_delay}秒后重试...")
                    self.logger.warning(f"AI调用异常，重试 {attempt + 1}/{max_retries}: {e}")
                    time.sleep(retry_delay)
                    continue
                else:
                    self.logger.error(f"AI分析失败，所有重试都异常: {paper.id} - {e}")
                    return None

        # 处理AI响应
        try:
            # 解析AI响应
            parsed_fields = self.parser.parse_analysis_content(response)

            # 创建分析结果
            result = AnalysisResult(
                paper_id=paper.id,
                paper_url=paper.url,
                title=paper.title,
                translation=paper.translation,
                authors=parsed_fields['authors'],
                publish_date=parsed_fields['publish_date'],
                model_function=parsed_fields['model_function'],
                page_content=response
            )

            return result

        except Exception as e:
            self.logger.error(f"解析AI响应异常: {paper.id} - {e}")
            return None
    
    def _build_analysis_prompt(self, paper: Paper) -> str:
        """
        构建AI分析提示词
        
        Args:
            paper: 论文对象
            
        Returns:
            提示词字符串
        """
        prompt = f"""你是一个AI论文分析专家。请访问以下arXiv论文链接，仔细阅读论文内容，然后严格按照指定格式输出分析结果。

## 信息获取策略：
1. 必须访问arXiv链接获取完整论文信息
2. 基于论文实际内容进行分析，不使用占位符
3. 确保所有字段都有准确、完整的内容

## 输出格式要求：
**作者团队**：[论文作者姓名或所属机构团队]
**发表日期**：[论文的发表日期，格式：YYYY-MM-DD]
**模型功能**：[模型的主要功能和用途，50字以内]

## 注意事项：
- 必须严格按照上述格式输出，每行以对应标签开头
- 每个字段后面直接跟具体内容，不要使用方括号
- 基于论文实际内容填写，不要使用占位符或模板
- 如果某项信息在论文中未明确提及，写"未明确提及"
- 所有字段都必须填写完整，不能留空

【待分析的论文信息】：
论文链接：{paper.url}
论文标题：{paper.title}
中文标题：{paper.translation}

请严格按照上述要求，访问论文链接并确保输出的所有字段都有完整、准确的内容。"""
        
        return prompt

    def _show_analysis_progress(self, stop_event, task_name):
        """
        显示AI分析进度动画

        Args:
            stop_event: 停止事件
            task_name: 任务名称
        """
        import sys
        import time

        spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        start_time = time.time()
        i = 0
        warning_shown = False

        while not stop_event.is_set():
            elapsed = int(time.time() - start_time)
            minutes, seconds = divmod(elapsed, 60)
            time_str = f"{minutes:02d}:{seconds:02d}"

            # 在75秒时显示警告
            if elapsed >= 75 and not warning_shown:
                sys.stdout.write(f'\r🧠 {task_name} {spinner[i % len(spinner)]} 已耗时: {time_str} ⚠️ 响应较慢...')
                warning_shown = True
            else:
                sys.stdout.write(f'\r🧠 {task_name} {spinner[i % len(spinner)]} 已耗时: {time_str}')

            sys.stdout.flush()

            time.sleep(0.1)
            i += 1

    def _create_progress_bar(self, current, total, width=50):
        """
        创建进度条

        Args:
            current: 当前进度
            total: 总数
            width: 进度条宽度

        Returns:
            进度条字符串
        """
        if total == 0:
            return "[" + "░" * width + "]"

        progress = current / total
        filled = int(width * progress)
        bar = "█" * filled + "░" * (width - filled)
        return f"[{bar}]"
    
    def _load_existing_results(self, file_path: Path) -> List[Dict[str, Any]]:
        """
        加载已存在的结果文件
        
        Args:
            file_path: 文件路径
            
        Returns:
            已存在的结果列表
        """
        if file_path.exists():
            try:
                data = self.file_manager.load_json(file_path)
                return data if isinstance(data, list) else []
            except Exception as e:
                self.logger.error(f"加载已存在结果失败: {e}")
                return []
        return []
    
    def _save_single_result(self, result: AnalysisResult, file_path: Path):
        """
        保存单个分析结果到文件
        
        Args:
            result: 分析结果
            file_path: 文件路径
        """
        try:
            # 加载现有结果
            existing_results = self._load_existing_results(file_path)
            
            # 移除已存在的相同ID论文
            existing_results = [
                r for r in existing_results 
                if self._extract_paper_id_from_result(r) != result.paper_id
            ]
            
            # 添加新结果
            existing_results.append(result.to_dict())
            
            # 保存到文件
            self.file_manager.save_json(existing_results, file_path)
            
        except Exception as e:
            self.logger.error(f"保存单个结果失败: {e}")
    
    def _extract_paper_id_from_result(self, result: Dict[str, Any]) -> str:
        """
        从结果中提取论文ID
        
        Args:
            result: 结果字典
            
        Returns:
            论文ID
        """
        # 尝试多种可能的字段名
        for field in ['paper_id', 'id']:
            if field in result:
                return result[field]
        
        # 从URL中提取
        url = result.get('paper_url', '')
        if url:
            return url.split('/')[-1]
        
        return ''
    
    def create_daily_report(self, date: str, analysis_results: List[AnalysisResult]) -> DailyReport:
        """
        创建日报
        
        Args:
            date: 日期字符串
            analysis_results: 分析结果列表
            
        Returns:
            日报对象
        """
        report = DailyReport(
            date=date,
            total_papers=len(analysis_results),
            analysis_results=analysis_results
        )
        
        return report
    
    def save_daily_report(self, report: DailyReport) -> bool:
        """
        保存日报到文件
        
        Args:
            report: 日报对象
            
        Returns:
            是否成功
        """
        try:
            # 确保报告目录存在
            reports_dir = Path(self.output_dir) / 'reports'
            self.file_manager.ensure_dir(reports_dir)
            
            # 构建文件路径
            file_path = reports_dir / f"{report.date}_report.json"
            
            # 保存报告
            success = report.save_to_file(str(file_path))
            
            if success:
                self.logger.info(f"日报保存成功: {file_path}")
            else:
                self.logger.error(f"日报保存失败: {file_path}")
            
            return success
            
        except Exception as e:
            self.logger.error(f"保存日报异常: {e}")
            return False
    
    def get_analysis_statistics(self) -> Dict[str, Any]:
        """
        获取分析统计信息
        
        Returns:
            统计信息字典
        """
        reports_dir = Path(self.output_dir) / 'reports'
        
        if not reports_dir.exists():
            return {"total_reports": 0, "reports": []}
        
        json_files = list(reports_dir.glob("*_report.json"))
        
        return {
            "total_reports": len(json_files),
            "reports": [f.stem for f in json_files],
            "reports_dir": str(reports_dir)
        }


# 便捷函数
def create_analyzer(config: Dict[str, Any]) -> PaperAnalyzer:
    """
    便捷函数：创建分析器实例
    
    Args:
        config: 配置字典
        
    Returns:
        PaperAnalyzer实例
    """
    return PaperAnalyzer(config)

def analyze_papers(papers: List[Paper], date: str = None,
                  output_dir: str = 'data/daily_reports',
                  ai_model: str = 'zhipu', silent: bool = False) -> List[AnalysisResult]:
    """
    便捷函数：分析论文
    
    Args:
        papers: 论文列表
        date: 日期字符串
        output_dir: 输出目录
        ai_model: AI模型类型
        silent: 是否静默模式
        
    Returns:
        分析结果列表
    """
    config = {
        'output_dir': output_dir,
        'ai_model': ai_model
    }
    analyzer = PaperAnalyzer(config)
    return analyzer.analyze_batch(papers, date, silent)
