"""
数据清洗器模块
负责清洗和结构化论文元数据
"""
import json
import re
from pathlib import Path
from typing import Dict, Any, List, Optional
from ..utils.console import ConsoleOutput
from ..utils.logger import get_logger
from ..utils.file_utils import FileManager
from ..utils.ai_client import create_ai_client, create_retryable_client


class DataCleaner:
    """
    数据清洗器
    
    负责清洗从API获取的原始论文数据，提取结构化信息
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        初始化清洗器
        
        Args:
            config: 配置字典
        """
        self.config = config
        self.console = ConsoleOutput()
        self.logger = get_logger('cleaner')
        self.file_manager = FileManager('cleaner')
        
        # 设置默认配置
        self.output_dir = config.get('output_dir', 'data/daily_reports')
        self.ai_model = config.get('ai_model', 'zhipu')
        self.use_ai = config.get('use_ai', True)
        
        # 初始化AI客户端
        self.ai_client = None
        if self.use_ai:
            try:
                self.ai_client = create_retryable_client(
                    self.ai_model,
                    max_retries=3
                )
            except Exception as e:
                self.logger.warning(f"AI客户端初始化失败: {e}")
                self.use_ai = False
    
    def clean(self, date: str, silent: bool = False) -> bool:
        """
        清洗指定日期的论文数据
        
        Args:
            date: 日期字符串 (YYYY-MM-DD)
            silent: 是否静默模式
            
        Returns:
            bool: 是否成功
        """
        if not silent:
            self.console.print_header("清洗结构化数据", 2)
        
        self.logger.info(f"开始清洗 {date} 的论文数据")
        
        try:
            # 加载原始元数据
            raw_data = self._load_metadata(date)
            if raw_data is None:
                if not silent:
                    self.console.print_error(f"未找到 {date} 的元数据文件")
                return False
            
            # 清洗数据
            cleaned_data = self._clean_data(raw_data, silent)
            
            # 保存清洗后的数据
            success = self._save_cleaned_data(date, cleaned_data)
            
            if success and not silent:
                clean_file = self._get_cleaned_file_path(date)
                self.console.print_success(f"清洗数据已保存: {clean_file}")
                self.logger.info(f"数据清洗完成: {clean_file}")
            
            return success
            
        except Exception as e:
            if not silent:
                self.console.print_error(f"数据清洗失败: {e}")
            self.logger.error(f"数据清洗异常: {e}")
            return False
    
    def _load_metadata(self, date: str) -> Optional[List[Dict[str, Any]]]:
        """
        加载原始元数据
        
        Args:
            date: 日期字符串
            
        Returns:
            原始数据列表，失败返回None
        """
        metadata_file = Path(self.output_dir) / 'metadata' / f"{date}.json"
        
        if not metadata_file.exists():
            self.logger.error(f"元数据文件不存在: {metadata_file}")
            return None
        
        try:
            data = self.file_manager.load_json(metadata_file)
            
            # 处理不同的数据格式
            if isinstance(data, list):
                return data
            elif isinstance(data, dict):
                # 如果是字典，可能包含错误信息或其他格式
                if "error" in data:
                    self.logger.warning(f"元数据包含错误信息: {data['error']}")
                    return []
                else:
                    return [data]
            else:
                self.logger.warning(f"未知的数据格式: {type(data)}")
                return []
                
        except Exception as e:
            self.logger.error(f"加载元数据失败: {e}")
            return None
    
    def _clean_data(self, raw_data: List[Dict[str, Any]], silent: bool = False) -> List[Dict[str, Any]]:
        """
        清洗原始数据
        
        Args:
            raw_data: 原始数据列表
            silent: 是否静默模式
            
        Returns:
            清洗后的数据列表
        """
        if not raw_data:
            self.logger.info("原始数据为空，返回空列表")
            return []
        
        cleaned_data = []
        
        if self.use_ai and self.ai_client:
            # 使用AI清洗数据
            cleaned_data = self._clean_with_ai(raw_data, silent)
        else:
            # 使用规则清洗数据
            cleaned_data = self._clean_with_rules(raw_data, silent)
        
        self.logger.info(f"数据清洗完成，原始数据: {len(raw_data)} 条，清洗后: {len(cleaned_data)} 条")
        return cleaned_data
    
    def _clean_with_ai(self, raw_data: List[Dict[str, Any]], silent: bool = False) -> List[str]:
        """
        使用AI清洗数据
        
        Args:
            raw_data: 原始数据
            silent: 是否静默模式
            
        Returns:
            清洗后的数据
        """
        if not silent:
            self.console.print_info("调用AI进行数据清洗...")
            self.console.print_info(f"原始数据量: {len(raw_data)} 条记录")
            self.console.print_info("正在预处理数据，精简内容...")

        try:
            # 构建AI提示词
            prompt = self._build_cleaning_prompt(raw_data)

            if not silent:
                self.console.print_info(f"提示词长度: {len(prompt)} 字符")
                self.console.print_info("正在发送请求到AI服务...")

            messages = [
                {"role": "system", "content": "你是一个专业的数据清洗助手，负责从原始论文数据中提取结构化信息。"},
                {"role": "user", "content": prompt}
            ]

            # 调用AI（带进度显示）
            if not silent:
                import threading
                import time

                # 创建进度显示线程
                progress_stop = threading.Event()
                progress_thread = threading.Thread(
                    target=self._show_ai_progress,
                    args=(progress_stop, "AI数据清洗")
                )
                progress_thread.daemon = True
                progress_thread.start()

            try:
                response = self.ai_client.chat(messages)
            finally:
                if not silent:
                    progress_stop.set()
                    progress_thread.join(timeout=1)
                    print()  # 换行

            if not silent:
                if response:
                    self.console.print_info(f"AI响应成功，长度: {len(response)} 字符")
                else:
                    self.console.print_warning("AI响应为空")
            
            if response:
                # 解析AI响应
                cleaned_data = self._parse_ai_response(response)
                self.logger.info(f"AI清洗成功，提取了 {len(cleaned_data)} 条记录")
                return cleaned_data
            else:
                self.logger.warning("AI响应为空，回退到规则清洗")
                return self._clean_with_rules(raw_data, silent)
                
        except Exception as e:
            self.logger.error(f"AI清洗失败: {e}")
            if not silent:
                self.console.print_warning("AI清洗失败，使用规则清洗")
            return self._clean_with_rules(raw_data, silent)
    
    def _clean_with_rules(self, raw_data: List[Dict[str, Any]], silent: bool = False) -> List[str]:
        """
        使用规则清洗数据
        
        Args:
            raw_data: 原始数据
            silent: 是否静默模式
            
        Returns:
            清洗后的数据
        """
        if not silent:
            self.console.print_info("使用规则进行数据清洗...")
        
        cleaned_strings = []

        for i, item in enumerate(raw_data, 1):
            try:
                cleaned_item = self._extract_paper_info(item)
                if cleaned_item:
                    # 转换为字符串格式，兼容原有解析器
                    paper_string = f"""{i}. 论文题目：{cleaned_item['title']}
   中文翻译：{cleaned_item['translation']}
   论文ID：{cleaned_item['id']}
   作者：{cleaned_item['authors']}
   发表日期：{cleaned_item['publish_date']}"""
                    cleaned_strings.append(paper_string)
            except Exception as e:
                self.logger.warning(f"清洗单条数据失败: {e}")
                continue

        return cleaned_strings
    
    def _extract_paper_info(self, item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        从单条原始数据中提取论文信息
        
        Args:
            item: 原始数据项
            
        Returns:
            提取的论文信息，失败返回None
        """
        try:
            # 处理不同的数据结构
            paper_data = item.get('paper', item)
            
            # 提取基本信息
            paper_id = paper_data.get('id', '')
            title = paper_data.get('title', '')
            
            # 如果缺少关键信息，跳过
            if not paper_id or not title:
                return None
            
            # 构建清洗后的数据
            cleaned_item = {
                'id': paper_id,
                'title': title,
                'translation': title,  # 默认使用英文标题，后续可以翻译
                'url': f"https://arxiv.org/abs/{paper_id}",
                'authors': paper_data.get('authors', ''),
                'publish_date': paper_data.get('publishedDate', ''),
                'model_function': ''  # 需要后续分析填充
            }
            
            return cleaned_item
            
        except Exception as e:
            self.logger.error(f"提取论文信息失败: {e}")
            return None

    def _preprocess_raw_data(self, raw_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        预处理原始数据，提取关键信息并精简

        Args:
            raw_data: 原始数据列表

        Returns:
            精简后的数据列表
        """
        processed_data = []

        for item in raw_data:
            try:
                paper = item.get('paper', {})

                # 提取作者名称列表
                authors = []
                for author in paper.get('authors', []):
                    if isinstance(author, dict):
                        name = author.get('name', '')
                        if name:
                            authors.append(name)
                    elif isinstance(author, str):
                        authors.append(author)

                # 提取关键信息（保留更多有用字段）
                processed_item = {
                    'id': paper.get('id', ''),
                    'title': paper.get('title', '').strip().replace('\n', ' '),
                    'summary': paper.get('summary', '').strip()[:800],  # 保留摘要，适当限制长度
                    'ai_summary': paper.get('ai_summary', '').strip(),  # AI生成的简短摘要
                    'ai_keywords': paper.get('ai_keywords', [])[:15],  # 保留关键词，限制数量
                    'authors': authors[:8],  # 适当限制作者数量
                    'publishedAt': paper.get('publishedAt', ''),
                    'githubRepo': paper.get('githubRepo', ''),  # GitHub仓库
                    'projectPage': paper.get('projectPage', ''),  # 项目页面
                    'url': paper.get('url', f"https://arxiv.org/abs/{paper.get('id', '')}")
                }

                # 只保留有效的论文（有ID和标题）
                if processed_item['id'] and processed_item['title']:
                    processed_data.append(processed_item)

            except Exception as e:
                self.logger.warning(f"预处理数据项失败: {e}")
                continue

        self.logger.info(f"数据预处理完成: 原始 {len(raw_data)} 条 -> 精简 {len(processed_data)} 条")
        return processed_data

    def _build_cleaning_prompt(self, raw_data: List[Dict[str, Any]]) -> str:
        """
        构建AI清洗提示词
        
        Args:
            raw_data: 原始数据
            
        Returns:
            提示词字符串
        """
        # 预处理数据，精简内容
        processed_data = self._preprocess_raw_data(raw_data)

        # 限制数据量，避免提示词过长
        sample_data = processed_data[:15] if len(processed_data) > 15 else processed_data

        prompt = f"""请从以下论文数据中提取结构化信息。数据已经过预处理，包含了论文的核心信息：

论文数据：
{json.dumps(sample_data, ensure_ascii=False, indent=2)}

请按以下格式输出每篇论文的信息：
1. 论文题目：[英文标题]
   中文翻译：[基于标题、摘要和关键词生成准确的中文翻译]
   论文ID：[arXiv ID]
   作者：[作者姓名，用逗号分隔]
   发表日期：[YYYY-MM-DD格式]

2. 论文题目：[英文标题]
   中文翻译：[基于标题、摘要和关键词生成准确的中文翻译]
   论文ID：[arXiv ID]
   作者：[作者姓名，用逗号分隔]
   发表日期：[YYYY-MM-DD格式]

注意事项：
- 利用提供的summary、ai_summary和ai_keywords字段来更好地理解论文内容
- 中文翻译要准确反映论文的核心内容和技术特点
- 如果有GitHub仓库或项目页面，说明这是一个有实际代码实现的项目
- 请确保提取所有论文的信息，按照上述格式逐一列出"""
        
        return prompt

    def _show_ai_progress(self, stop_event, task_name):
        """
        显示AI处理进度动画

        Args:
            stop_event: 停止事件
            task_name: 任务名称
        """
        import sys
        import time

        spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        start_time = time.time()
        i = 0

        while not stop_event.is_set():
            elapsed = int(time.time() - start_time)
            minutes, seconds = divmod(elapsed, 60)
            time_str = f"{minutes:02d}:{seconds:02d}"

            sys.stdout.write(f'\r🤖 {task_name}中 {spinner[i % len(spinner)]} 已耗时: {time_str}')
            sys.stdout.flush()

            time.sleep(0.1)
            i += 1
    
    def _parse_ai_response(self, response: str) -> List[str]:
        """
        解析AI响应，返回字符串列表（兼容原有解析器）

        Args:
            response: AI响应文本

        Returns:
            解析后的字符串列表
        """
        # 直接返回AI响应作为单个字符串，让解析器处理
        # 这样保持与原有系统的兼容性
        if response and response.strip():
            return [response.strip()]
        else:
            return []
    
    def _save_cleaned_data(self, date: str, data: List[str]) -> bool:
        """
        保存清洗后的数据
        
        Args:
            date: 日期字符串
            data: 清洗后的数据
            
        Returns:
            bool: 是否成功
        """
        try:
            # 确保清洗数据目录存在
            cleaned_dir = Path(self.output_dir) / 'cleaned'
            self.file_manager.ensure_dir(cleaned_dir)
            
            # 构建文件路径
            file_path = cleaned_dir / f"{date}_clean.json"
            
            # 保存数据
            success = self.file_manager.save_json(data, file_path)
            
            if success:
                self.logger.info(f"清洗数据保存成功: {file_path}")
            else:
                self.logger.error(f"清洗数据保存失败: {file_path}")
            
            return success
            
        except Exception as e:
            self.logger.error(f"保存清洗数据异常: {e}")
            return False
    
    def _get_cleaned_file_path(self, date: str) -> str:
        """
        获取清洗数据文件路径
        
        Args:
            date: 日期字符串
            
        Returns:
            文件路径字符串
        """
        return str(Path(self.output_dir) / 'cleaned' / f"{date}_clean.json")
    
    def load_cleaned_data(self, date: str) -> Optional[List[Dict[str, Any]]]:
        """
        加载已清洗的数据
        
        Args:
            date: 日期字符串
            
        Returns:
            清洗后的数据，失败返回None
        """
        file_path = self._get_cleaned_file_path(date)
        return self.file_manager.load_json(file_path)
    
    def check_cleaned_exists(self, date: str) -> bool:
        """
        检查清洗数据是否存在
        
        Args:
            date: 日期字符串
            
        Returns:
            bool: 是否存在
        """
        file_path = self._get_cleaned_file_path(date)
        return Path(file_path).exists()


# 便捷函数
def create_cleaner(config: Dict[str, Any]) -> DataCleaner:
    """
    便捷函数：创建清洗器实例
    
    Args:
        config: 配置字典
        
    Returns:
        DataCleaner实例
    """
    return DataCleaner(config)

def clean_data(date: str, output_dir: str = 'data/daily_reports',
               ai_model: str = 'zhipu', silent: bool = False) -> bool:
    """
    便捷函数：清洗数据
    
    Args:
        date: 日期字符串
        output_dir: 输出目录
        ai_model: AI模型类型
        silent: 是否静默模式
        
    Returns:
        bool: 是否成功
    """
    config = {
        'output_dir': output_dir,
        'ai_model': ai_model
    }
    cleaner = DataCleaner(config)
    return cleaner.clean(date, silent)
