#!/usr/bin/env python3
"""
论文分析系统主程序入口
整合所有功能模块，提供统一的命令行接口
"""
import sys
import argparse
import re
import os
from datetime import datetime
from pathlib import Path
from typing import List, Optional

# 设置控制台编码为UTF-8，解决Windows下的Unicode字符显示问题
if sys.platform.startswith('win'):
    try:
        # 设置控制台代码页为UTF-8
        os.system('chcp 65001 > nul')
        # 重新配置stdout和stderr的编码
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        # 如果设置失败，使用替换模式处理不支持的字符
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from .utils.config import get_config
from .utils.console import ConsoleOutput
from .utils.logger import get_logger
from .utils.progress import ProgressManager
from .core.downloader import MetadataDownloader
from .core.cleaner import DataCleaner
from .core.analyzer import PaperAnalyzer
from .core.classifier import PaperClassifier
from .core.parser import ContentParser
from .models.report import AnalysisResult, DailyReport


class PaperAnalysisApp:
    """
    论文分析应用程序主类
    
    整合所有功能模块，提供统一的分析流程
    """
    
    def __init__(self):
        """初始化应用程序"""
        # 加载配置
        self.config = get_config()
        
        # 初始化工具
        self.console = ConsoleOutput()
        self.logger = get_logger('main_app')
        
        # 显示启动信息
        self.logger.info("论文分析系统启动")
        
        # 获取应用配置
        self.app_config = {
            'output_dir': self.config.get_app_config('default_output_dir'),
            'analysis_dir': self.config.get_app_config('default_analysis_dir'),
            'ai_model': self.config.get_default_provider(),
            'use_ai': self.config.get_app_config('enable_ai'),
            'batch_size': self.config.get_app_config('batch_size'),
            'api_delay': self.config.get_app_config('api_request_delay')
        }
        
        self.logger.info(f"应用配置: {self.app_config}")
    
    def run_daily_analysis(self, date: str, silent: bool = False) -> bool:
        """
        运行日常分析流程
        
        Args:
            date: 分析日期 (YYYY-MM-DD)
            silent: 是否静默模式
            
        Returns:
            是否成功
        """
        if not validate_date_format(date):
            if not silent:
                self.console.print_error(f"无效的日期格式: {date}，请使用 YYYY-MM-DD 格式")
            return False
        
        if not silent:
            self.console.print_header(f"开始日常分析流程 - {date}", 0)
        
        self.logger.info(f"开始日常分析: {date}")
        
        try:
            # 步骤1: 下载元数据
            if not self._download_metadata(date, silent):
                return False
            
            # 步骤2: 清洗数据
            if not self._clean_data(date, silent):
                return False
            
            # 步骤3: AI分析
            if not self._analyze_papers(date, silent):
                return False
            
            if not silent:
                self.console.print_success(f"日常分析完成: {date}")
            
            self.logger.info(f"日常分析完成: {date}")
            return True
            
        except Exception as e:
            if not silent:
                self.console.print_error(f"日常分析失败: {e}")
            self.logger.error(f"日常分析异常: {e}")
            return False
    
    def run_advanced_analysis(self, date: str, analysis_results: List[AnalysisResult] = None, 
                            silent: bool = False) -> bool:
        """
        运行高级分析流程（分类和汇总）
        
        Args:
            date: 分析日期
            analysis_results: 分析结果列表，如果为None则自动加载
            silent: 是否静默模式
            
        Returns:
            是否成功
        """
        if not validate_date_format(date):
            if not silent:
                self.console.print_error(f"无效的日期格式: {date}")
            return False
        
        if not silent:
            self.console.print_header(f"开始高级分析流程 - {date}", 0)
        
        self.logger.info(f"开始高级分析: {date}")
        
        try:
            # 加载分析结果（如果未提供）
            if analysis_results is None:
                analysis_results = self.load_analysis_results(date)
                if not analysis_results:
                    if not silent:
                        self.console.print_error(f"未找到 {date} 的分析结果")
                    return False
            
            # 步骤1: MD切分
            if not silent:
                self.console.print_separator()
                self.console.print_header("✂️ 步骤1：MD切分", 1)
                self.console.print_separator()

            if not self._split_to_md(date, analysis_results, silent):
                return False

            # 步骤2: 智能分类
            if not silent:
                self.console.print_separator()
                self.console.print_header("🏷️ 步骤2：智能分类与总结", 1)
                self.console.print_separator()

            if not self._classify_papers(date, analysis_results, silent):
                return False

            # 步骤3: 生成汇总报告
            if not silent:
                self.console.print_separator()
                self.console.print_header("📊 步骤3：生成分类汇总", 1)
                self.console.print_separator()

            if not self._generate_summary(date, silent):
                return False
            
            if not silent:
                self.console.print_success(f"高级分析完成: {date}")
            
            self.logger.info(f"高级分析完成: {date}")
            return True
            
        except Exception as e:
            if not silent:
                self.console.print_error(f"高级分析失败: {e}")
            self.logger.error(f"高级分析异常: {e}")
            return False
    
    def _download_metadata(self, date: str, silent: bool) -> bool:
        """下载元数据"""
        downloader = MetadataDownloader(self.app_config)
        return downloader.download(date, silent)
    
    def _clean_data(self, date: str, silent: bool) -> bool:
        """清洗数据"""
        # 创建专门用于清洗的配置，禁用AI
        clean_config = self.app_config.copy()
        clean_config['use_ai'] = False  # 明确禁用AI，使用规则清洗
        
        cleaner = DataCleaner(clean_config)
        return cleaner.clean(date, silent)
    
    def _analyze_papers(self, date: str, silent: bool) -> bool:
        """分析论文"""
        # 加载清洗后的数据
        cleaner = DataCleaner(self.app_config)
        
        cleaned_data = cleaner.load_cleaned_data(date)
        if not cleaned_data:
            if not silent:
                self.console.print_error(f"未找到 {date} 的清洗数据")
            return False
        
        # 现在cleaned_data已经是结构化的字典列表
        if not cleaned_data:
            if not silent:
                self.console.print_warning(f"{date} 没有有效的论文数据")
            return True  # 空数据不算失败
        
        # 将字典数据转换为Paper对象
        from .models.paper import Paper
        papers = []
        
        for data in cleaned_data:
            try:
                # 使用Paper.from_dict方法转换
                paper = Paper.from_dict(data)
                papers.append(paper)
            except Exception as e:
                # 如果from_dict失败，尝试from_legacy_format
                try:
                    paper = Paper.from_legacy_format(data)
                    papers.append(paper)
                except Exception as e2:
                    if not silent:
                        self.console.print_warning(f"跳过无效论文数据: {e2}")
                    self.logger.warning(f"转换论文数据失败: {e2}")
                    continue
        
        if not papers:
            if not silent:
                self.console.print_warning(f"{date} 没有有效的论文数据")
            return True  # 空数据不算失败
        
        # AI分析
        analyzer = PaperAnalyzer(self.app_config)
        
        try:
            results = analyzer.analyze_batch(papers, date, silent)
            return len(results) > 0 or len(papers) == 0
        except Exception as e:
            if not silent:
                self.console.print_error(f"论文分析失败: {e}")
            self.logger.error(f"论文分析异常: {e}")
            return False
    
    def _classify_papers(self, date: str, analysis_results: List[AnalysisResult], 
                        silent: bool) -> bool:
        """分类论文"""
        if not analysis_results:
            if not silent:
                self.console.print_warning("没有分析结果需要分类")
            return True
        
        classifier = PaperClassifier({
            **self.app_config,
            'output_dir': self.app_config['analysis_dir']
        })
        
        # 分类论文
        classification_results = classifier.classify_papers(analysis_results, date, silent)
        
        # 保存分类结果
        if classification_results:
            success = classifier.save_classification_results(date, classification_results)
            if not success:
                if not silent:
                    self.console.print_error("保存分类结果失败")
                return False
        
        return True
    
    def _generate_summary(self, date: str, silent: bool) -> bool:
        """生成汇总报告"""
        try:
            # 加载分类结果
            classifier = PaperClassifier({
                **self.app_config,
                'output_dir': self.app_config['analysis_dir']
            })

            # 生成汇总报告
            success = classifier.generate_summary_report(date, silent)

            if success and not silent:
                output_dir = Path(self.app_config['analysis_dir']) / date
                summary_file = output_dir / "模型分类汇总.md"
                self.console.print_success(f"📊 汇总报告已生成: {summary_file}")

            return success

        except Exception as e:
            if not silent:
                self.console.print_error(f"汇总报告生成失败: {e}")
            self.logger.error(f"汇总报告生成异常: {e}")
            return False
    
    def load_analysis_results(self, date: str) -> List[AnalysisResult]:
        """
        加载分析结果（支持直接从JSON文件加载）

        Args:
            date: 日期字符串

        Returns:
            分析结果列表
        """
        try:
            # 尝试加载JSON报告文件
            reports_dir = Path(self.app_config['output_dir']) / 'reports'
            report_file = reports_dir / f"{date}_report.json"

            if not report_file.exists():
                self.logger.warning(f"未找到 {date} 的分析结果文件: {report_file}")
                return []

            # 直接从JSON文件加载数据
            import json
            with open(report_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 转换为AnalysisResult对象列表
            analysis_results = []

            # 处理不同的JSON格式
            if isinstance(data, list):
                # 如果是列表格式（直接的论文列表）
                for item in data:
                    if isinstance(item, dict):
                        analysis_result = self._convert_dict_to_analysis_result(item)
                        if analysis_result:
                            analysis_results.append(analysis_result)
            elif isinstance(data, dict) and 'analysis_results' in data:
                # 如果是DailyReport格式
                for item in data['analysis_results']:
                    analysis_result = self._convert_dict_to_analysis_result(item)
                    if analysis_result:
                        analysis_results.append(analysis_result)

            self.logger.info(f"成功加载 {len(analysis_results)} 个分析结果")
            return analysis_results

        except Exception as e:
            self.logger.error(f"加载分析结果失败: {e}")
            return []

    def _convert_dict_to_analysis_result(self, item: dict) -> Optional[AnalysisResult]:
        """
        将字典转换为AnalysisResult对象

        Args:
            item: 字典数据

        Returns:
            AnalysisResult对象或None
        """
        try:
            # 使用AnalysisResult的from_dict方法，它已经支持新旧格式
            return AnalysisResult.from_dict(item)
        except Exception as e:
            # 如果from_dict失败，尝试from_legacy_format
            try:
                return AnalysisResult.from_legacy_format(item)
            except Exception as e2:
                self.logger.warning(f"转换分析结果失败: {e2}")
                return None

    def _split_to_md(self, date: str, analysis_results: List[AnalysisResult], silent: bool) -> bool:
        """MD切分步骤"""
        try:
            classifier = PaperClassifier({
                **self.app_config,
                'output_dir': self.app_config['analysis_dir']
            })

            # 执行MD切分
            success = classifier.split_to_md(analysis_results, date, silent)

            if success and not silent:
                output_dir = Path(self.app_config['analysis_dir']) / date
                self.console.print_success(f"✂️ MD切分完成: {output_dir}")

            return success

        except Exception as e:
            if not silent:
                self.console.print_error(f"MD切分失败: {e}")
            self.logger.error(f"MD切分异常: {e}")
            return False
    
    def get_system_status(self) -> dict:
        """
        获取系统状态
        
        Returns:
            系统状态字典
        """
        config_summary = self.config.get_config_summary()
        
        return {
            "配置状态": "正常",
            "默认AI提供商": config_summary["default_provider"],
            "可用AI提供商": config_summary["usable_providers"],
            "输出目录": self.app_config["output_dir"],
            "分析目录": self.app_config["analysis_dir"],
            "AI功能": "启用" if self.app_config["use_ai"] else "禁用"
        }


def create_argument_parser() -> argparse.ArgumentParser:
    """
    创建命令行参数解析器
    
    Returns:
        ArgumentParser实例
    """
    parser = argparse.ArgumentParser(
        description="""
📊 论文分析系统 v2.0 - 自动化论文下载、分析和分类

🎯 功能特性:
  • 自动从HuggingFace获取最新论文数据
  • AI驱动的智能论文分析和分类
  • 生成详细的分析报告和分类汇总
  • 支持批量处理和增量更新
  • 提供GUI和命令行两种使用方式

🎨 GUI版本 (推荐新手):
  python run_gui.py                      # 启动图形界面
  python tools/batch_processor_gui.py    # 批处理图形界面
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
📋 使用示例:

🔹 基础分析 (Basic):
  python run.py basic                     # 分析今天的论文
  python run.py basic 2024-05-15         # 分析指定日期的论文
  python run.py basic 2024-05-15 --silent # 静默模式运行

🔹 进阶分析 (Advanced):
  python run.py advanced                 # 分析今天的论文（需要先运行basic）
  python run.py advanced 2024-05-15      # 分析指定日期的论文
  python run.py advanced --silent        # 静默模式运行

🔹 系统状态:
  python run.py status                   # 查看系统配置和状态

🔹 批量处理:
  python tools/batch_processor.py daily --start 2024-05-15 --end 2024-05-20
  python tools/batch_processor.py advanced --auto
  python tools/batch_processor.py pipeline --start 2024-05-15 --end 2024-05-17

⚙️  配置说明:
  • AI模型配置: config/models.yaml
  • 日志配置: config/logging.yaml
  • 输出目录: data/daily_reports (basic), data/analysis_results (advanced)

🔧 故障排除:
  1. 确保已配置AI API密钥 (config/models.yaml)
  2. 检查网络连接 (访问HuggingFace和AI服务)
  3. 确保有足够的磁盘空间
  4. 日期格式必须为 YYYY-MM-DD
  5. Advanced分析需要对应的Basic分析结果

💡 获取详细帮助:
  python run.py basic --help         # 查看基础分析详细说明
  python run.py advanced --help      # 查看进阶分析详细说明
  python run.py status --help        # 查看系统状态详细说明

📚 更多帮助:
  • 查看README.md了解详细使用说明
  • 查看tools/README.md了解批处理工具
  • 使用GUI版本获得更友好的用户体验
        """
    )
    
    # 添加子命令
    subparsers = parser.add_subparsers(
        dest='command',
        help='可用命令 (使用 COMMAND --help 查看详细说明)',
        metavar='COMMAND',
        description='选择要执行的分析类型。每个命令都支持 --help 参数查看详细使用说明。'
    )

    # 基本分析命令
    basic_parser = subparsers.add_parser(
        'basic',
        help='📅 运行基础日报分析 (使用 basic --help 查看详细说明)',
        description="""
📅 基础分析 (Basic Analysis)

功能说明:
  • 从HuggingFace获取指定日期的论文数据
  • 使用AI进行论文内容分析和清洗
  • 生成结构化的分析报告
  • 输出到 data/daily_reports/ 目录

处理流程:
  1. 数据获取 - 从HF API获取论文列表
  2. 数据清洗 - AI分析论文内容和质量
  3. 报告生成 - 生成JSON和Markdown报告

适用场景:
  • 日常论文跟踪和分析
  • 为进阶分析提供数据基础
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    basic_parser.add_argument(
        'date',
        nargs='?',
        help='分析日期 (YYYY-MM-DD格式)，默认为今天'
    )
    basic_parser.add_argument(
        '--silent',
        action='store_true',
        help='静默模式，减少输出信息'
    )

    # 高级分析命令
    advanced_parser = subparsers.add_parser(
        'advanced',
        help='🔍 运行进阶智能分析 (使用 advanced --help 查看详细说明)',
        description="""
🔍 进阶分析 (Advanced Analysis)

功能说明:
  • 基于Basic分析结果进行深度分析
  • AI驱动的智能论文分类
  • 生成分类汇总和详细报告
  • 输出到 data/analysis_results/ 目录

处理流程:
  1. MD切分 - 将分析结果切分为独立文件
  2. 智能分类 - AI分析并分类论文
  3. 汇总报告 - 生成分类统计和汇总

前置条件:
  • 必须先运行对应日期的Basic分析
  • 确保AI API配置正确

适用场景:
  • 深度论文分类和整理
  • 生成专业的分析报告
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    advanced_parser.add_argument(
        'date',
        nargs='?',
        help='分析日期 (YYYY-MM-DD格式)，默认为今天'
    )
    advanced_parser.add_argument(
        '--silent',
        action='store_true',
        help='静默模式，减少输出信息'
    )

    # 状态查看命令
    status_parser = subparsers.add_parser(
        'status',
        help='📊 查看系统状态和配置 (使用 status --help 查看详细说明)',
        description="""
📊 系统状态 (System Status)

功能说明:
  • 显示当前系统配置信息
  • 检查AI API连接状态
  • 显示输出目录和文件统计
  • 验证依赖和环境配置

检查项目:
  • 配置文件加载状态
  • AI模型配置
  • 输出目录状态
  • 日志配置
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    return parser

def validate_date_format(date_str: str) -> bool:
    """
    验证日期格式
    
    Args:
        date_str: 日期字符串
        
    Returns:
        是否有效
    """
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(pattern, date_str):
        return False
    
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def main() -> int:
    """
    主函数
    
    Returns:
        退出码
    """
    try:
        # 解析命令行参数
        parser = create_argument_parser()
        args = parser.parse_args()
        
        if not args.command:
            parser.print_help()
            return 1
        
        # 创建应用实例
        app = PaperAnalysisApp()
        
        # 执行相应命令
        if args.command == 'basic':
            # 如果没有提供日期，使用今天的日期
            date = args.date or datetime.now().strftime('%Y-%m-%d')
            success = app.run_daily_analysis(date, args.silent)
            return 0 if success else 1

        elif args.command == 'advanced':
            # 如果没有提供日期，使用今天的日期
            date = args.date or datetime.now().strftime('%Y-%m-%d')
            # 先加载分析结果
            analysis_results = app.load_analysis_results(date)
            success = app.run_advanced_analysis(date, analysis_results, args.silent)
            return 0 if success else 1
            
        elif args.command == 'status':
            status = app.get_system_status()
            console = ConsoleOutput()
            console.print_header("系统状态", 0)
            for key, value in status.items():
                console.print_info(f"{key}: {value}")
            return 0
        
        else:
            parser.print_help()
            return 1
            
    except KeyboardInterrupt:
        print("\n用户中断操作")
        return 130
    except Exception as e:
        print(f"程序异常: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
