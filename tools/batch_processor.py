#!/usr/bin/env python3
"""
统一批处理工具
功能：批量处理基础日报和进阶分析
"""
import os
import sys
import subprocess
import argparse
import re
from datetime import datetime, timedelta
from pathlib import Path

class BatchProcessor:
    def __init__(self):
        self.success_count = 0
        self.failed_dates = []
        self.skipped_dates = []
        
    def generate_date_range(self, start_date, end_date):
        """生成日期范围"""
        try:
            start = datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError as e:
            print(f"❌ 日期格式错误: {e}")
            print("💡 请使用 YYYY-MM-DD 格式")
            return []
        
        if start > end:
            print("❌ 开始日期不能晚于结束日期")
            return []
        
        # 限制最大范围为1年
        if (end - start).days > 365:
            print("❌ 日期范围不能超过1年（365天）")
            return []
        
        dates = []
        current = start
        while current <= end:
            dates.append(current.strftime('%Y-%m-%d'))
            current += timedelta(days=1)
        
        return dates
    
    def detect_daily_dates(self):
        """检测可进行daily处理的日期（基于HF数据）"""
        # 这里可以扩展为检测HF数据的逻辑
        # 目前返回空列表，表示需要手动指定日期
        return []
    
    def detect_advanced_dates(self):
        """检测可进行advanced处理的日期（基于daily结果）"""
        dates = []
        reports_dir = Path("data/daily_reports/reports")

        if reports_dir.exists():
            for file in reports_dir.iterdir():
                if file.is_file() and file.name.endswith('_report.json'):
                    # 提取日期
                    date_str = file.name.replace('_report.json', '')
                    if re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
                        dates.append(date_str)

        return sorted(dates)
    
    def check_daily_completed(self, date):
        """检查daily是否已完成"""
        report_file = Path(f"data/daily_reports/reports/{date}_report.json")
        return report_file.exists()
    
    def check_advanced_completed(self, date):
        """检查advanced是否已完成"""
        analysis_dir = Path(f"data/analysis_results/{date}")
        summary_file = analysis_dir / "模型分类汇总.md"
        return summary_file.exists()
    
    def run_daily(self, date, skip_existing=True):
        """运行daily处理"""
        if skip_existing and self.check_daily_completed(date):
            print(f"⏭️  跳过已完成的daily: {date}")
            self.skipped_dates.append(date)
            return True
        
        try:
            cmd = [sys.executable, "run.py", "basic", date]
            print(f"🔄 执行命令: {' '.join(cmd)}")

            # 正常执行，不设置超时限制
            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode == 0:
                print(f"✅ Daily {date} 处理成功")
                self.success_count += 1
                return True
            else:
                print(f"❌ Daily {date} 处理失败")

                # 检查输出中的错误信息
                output = result.stdout + result.stderr
                if "未找到对应的HF数据" in output:
                    print(f"💡 原因: 该日期没有HF数据")
                elif "API调用失败" in output:
                    print(f"💡 原因: AI API调用失败")
                elif result.stderr:
                    # 显示关键错误信息
                    error_lines = result.stderr.strip().split('\n')
                    for line in error_lines[-3:]:  # 显示最后3行错误
                        if line.strip():
                            print(f"💡 错误: {line.strip()}")

                self.failed_dates.append(date)
                return False

        except Exception as e:
            print(f"❌ Daily {date} 处理异常: {e}")
            self.failed_dates.append(date)
            return False
    
    def run_advanced(self, date, skip_existing=True):
        """运行advanced处理"""
        # 检查前置条件
        if not self.check_daily_completed(date):
            print(f"❌ {date} 缺少daily结果，无法进行advanced分析")
            self.failed_dates.append(date)
            return False
        
        if skip_existing and self.check_advanced_completed(date):
            print(f"⏭️  跳过已完成的advanced: {date}")
            self.skipped_dates.append(date)
            return True
        
        try:
            cmd = [sys.executable, "run.py", "advanced", date]
            print(f"🔄 执行命令: {' '.join(cmd)}")

            # 正常执行，不设置超时限制
            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode == 0:
                print(f"✅ Advanced {date} 处理成功")
                self.success_count += 1
                return True
            else:
                print(f"❌ Advanced {date} 处理失败")

                # 检查输出中的错误信息
                output = result.stdout + result.stderr
                if "汇总报告生成失败" in output:
                    print(f"💡 原因: 汇总报告生成失败")
                elif "分类失败" in output:
                    print(f"💡 原因: 论文分类失败")
                elif "API调用失败" in output:
                    print(f"💡 原因: AI API调用失败")
                elif result.stderr:
                    # 显示关键错误信息
                    error_lines = result.stderr.strip().split('\n')
                    for line in error_lines[-3:]:  # 显示最后3行错误
                        if line.strip():
                            print(f"💡 错误: {line.strip()}")

                self.failed_dates.append(date)
                return False

        except Exception as e:
            print(f"❌ Advanced {date} 处理异常: {e}")
            self.failed_dates.append(date)
            return False
    
    def batch_daily(self, dates, skip_existing=True):
        """批量daily处理"""
        print(f"🎯 开始批量Daily处理")
        print(f"📅 日期范围: {len(dates)} 个日期")
        print(f"📋 日期列表: {dates}")
        print(f"⚙️  跳过已完成: {'是' if skip_existing else '否'}")

        import time
        start_time = time.time()

        for i, date in enumerate(dates, 1):
            print(f"\n{'='*60}")
            print(f"📅 处理Daily [{i}/{len(dates)}]: {date}")
            print(f"{'='*60}")

            date_start = time.time()
            success = self.run_daily(date, skip_existing)
            date_end = time.time()

            if success:
                print(f"⏱️  耗时: {date_end - date_start:.1f}秒")

            # 显示剩余预估时间
            if i < len(dates):
                avg_time = (time.time() - start_time) / i
                remaining_time = avg_time * (len(dates) - i)
                print(f"📊 进度: {i}/{len(dates)} 完成，预计剩余: {remaining_time/60:.1f}分钟")

        total_time = time.time() - start_time
        print(f"\n⏱️  总耗时: {total_time/60:.1f}分钟")
        self.print_summary("Daily")
    
    def batch_advanced(self, dates, skip_existing=True):
        """批量advanced处理"""
        print(f"🎯 开始批量Advanced处理")
        print(f"📅 日期范围: {len(dates)} 个日期")
        print(f"📋 日期列表: {dates}")
        print(f"⚙️  跳过已完成: {'是' if skip_existing else '否'}")

        import time
        start_time = time.time()

        for i, date in enumerate(dates, 1):
            print(f"\n{'='*60}")
            print(f"📅 处理Advanced [{i}/{len(dates)}]: {date}")
            print(f"{'='*60}")

            date_start = time.time()
            success = self.run_advanced(date, skip_existing)
            date_end = time.time()

            if success:
                print(f"⏱️  耗时: {date_end - date_start:.1f}秒")

            # 显示剩余预估时间
            if i < len(dates):
                avg_time = (time.time() - start_time) / i
                remaining_time = avg_time * (len(dates) - i)
                print(f"📊 进度: {i}/{len(dates)} 完成，预计剩余: {remaining_time/60:.1f}分钟")

        total_time = time.time() - start_time
        print(f"\n⏱️  总耗时: {total_time/60:.1f}分钟")
        self.print_summary("Advanced")
    
    def batch_pipeline(self, dates, skip_existing=True):
        """批量流水线处理（Daily + Advanced）"""
        print(f"🎯 开始批量流水线处理")
        print(f"📅 日期范围: {len(dates)} 个日期")
        print(f"📋 日期列表: {dates}")
        
        for i, date in enumerate(dates, 1):
            print(f"\n{'='*60}")
            print(f"📅 流水线处理 [{i}/{len(dates)}]: {date}")
            print(f"{'='*60}")
            
            # 先执行Daily
            print(f"🔄 步骤1: Daily处理")
            daily_success = self.run_daily(date, skip_existing)
            
            if daily_success:
                # 再执行Advanced
                print(f"🔄 步骤2: Advanced处理")
                self.run_advanced(date, skip_existing)
            else:
                print(f"❌ Daily失败，跳过Advanced处理")
        
        self.print_summary("Pipeline")
    
    def print_summary(self, task_type):
        """打印汇总结果"""
        total = self.success_count + len(self.failed_dates) + len(self.skipped_dates)
        
        print(f"\n{'='*60}")
        print(f"📊 {task_type} 批量处理完成")
        print(f"{'='*60}")
        print(f"📈 总计: {total} 个日期")
        print(f"✅ 成功: {self.success_count}")
        print(f"⏭️  跳过: {len(self.skipped_dates)}")
        print(f"❌ 失败: {len(self.failed_dates)}")
        
        if self.skipped_dates:
            print(f"⏭️  跳过的日期: {self.skipped_dates}")
        
        if self.failed_dates:
            print(f"❌ 失败的日期: {self.failed_dates}")
        else:
            print(f"🎉 所有日期处理成功！")

def main():
    parser = argparse.ArgumentParser(
        description="""
🔄 论文分析系统 - 批处理工具 v2.0

🎯 功能特性:
  • 批量处理多个日期的论文分析任务
  • 支持Daily、Advanced和Pipeline三种模式
  • 智能跳过已完成的任务，支持增量处理
  • 实时进度显示和详细的统计信息
  • 完善的错误处理和重试机制

🎨 GUI版本 (推荐):
  python tools/batch_processor_gui.py    # 启动图形界面版本
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
📋 使用示例:

🔹 批量Daily处理:
  python tools/batch_processor.py daily --start 2024-05-15 --end 2024-05-20
  python tools/batch_processor.py daily --start 2024-05-15 --end 2024-05-20 --force

🔹 批量Advanced处理:
  python tools/batch_processor.py advanced --auto
  python tools/batch_processor.py advanced --start 2024-05-15 --end 2024-05-20

🔹 完整流水线处理:
  python tools/batch_processor.py pipeline --start 2024-05-15 --end 2024-05-20

⚙️  参数说明:
  • --start: 开始日期 (YYYY-MM-DD格式)
  • --end: 结束日期 (YYYY-MM-DD格式)
  • --auto: 自动检测可处理的日期 (仅Advanced)
  • --force: 强制重新处理已完成的任务

🛡️ 安全限制:
  • 日期范围最大不超过1年 (365天)
  • 自动跳过已完成的任务 (除非使用--force)
  • Advanced处理需要对应的Daily结果

💡 获取详细帮助:
  python tools/batch_processor.py daily --help      # 查看Daily模式详细说明
  python tools/batch_processor.py advanced --help   # 查看Advanced模式详细说明
  python tools/batch_processor.py pipeline --help   # 查看Pipeline模式详细说明

💡 使用建议:
  • 首次使用建议先用小范围日期测试
  • 大批量处理建议分批进行
  • 遇到网络问题可重新运行 (自动跳过已完成)
        """
    )
    subparsers = parser.add_subparsers(
        dest='command',
        help='处理类型 (使用 MODE --help 查看详细说明)',
        metavar='MODE',
        description='选择批处理模式。每个模式都支持 --help 参数查看详细使用说明。'
    )
    
    # Daily子命令
    daily_parser = subparsers.add_parser(
        'daily',
        help='📅 批量Daily处理 (使用 daily --help 查看详细说明)',
        description='批量执行基础日报分析，适合处理多个日期的论文数据获取和初步分析'
    )
    daily_parser.add_argument('--start', required=True, help='开始日期 (YYYY-MM-DD格式)')
    daily_parser.add_argument('--end', required=True, help='结束日期 (YYYY-MM-DD格式)')
    daily_parser.add_argument('--force', action='store_true', help='强制重新处理已完成的日期')

    # Advanced子命令
    advanced_parser = subparsers.add_parser(
        'advanced',
        help='🔍 批量Advanced处理 (使用 advanced --help 查看详细说明)',
        description='批量执行进阶智能分析，基于Daily结果进行深度分类和汇总'
    )
    advanced_group = advanced_parser.add_mutually_exclusive_group(required=True)
    advanced_group.add_argument('--auto', action='store_true', help='自动检测所有可处理的日期')
    advanced_group.add_argument('--start', help='开始日期 (YYYY-MM-DD格式)')
    advanced_parser.add_argument('--end', help='结束日期 (YYYY-MM-DD格式，与--start配合使用)')
    advanced_parser.add_argument('--force', action='store_true', help='强制重新处理已完成的日期')

    # Pipeline子命令
    pipeline_parser = subparsers.add_parser(
        'pipeline',
        help='🔄 批量流水线处理 (使用 pipeline --help 查看详细说明)',
        description='完整的流水线处理，依次执行Daily和Advanced分析，一键完成全流程'
    )
    pipeline_parser.add_argument('--start', required=True, help='开始日期 (YYYY-MM-DD格式)')
    pipeline_parser.add_argument('--end', required=True, help='结束日期 (YYYY-MM-DD格式)')
    pipeline_parser.add_argument('--force', action='store_true', help='强制重新处理已完成的日期')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    processor = BatchProcessor()
    
    if args.command == 'daily':
        dates = processor.generate_date_range(args.start, args.end)
        if dates:
            processor.batch_daily(dates, skip_existing=not args.force)
    
    elif args.command == 'advanced':
        if args.auto:
            dates = processor.detect_advanced_dates()
            if not dates:
                print("❌ 未找到任何可进行Advanced分析的日期")
                print("💡 请先运行Daily处理创建数据")
                return
        else:
            if not args.end:
                print("❌ 使用--start时必须同时指定--end")
                return
            dates = processor.generate_date_range(args.start, args.end)
        
        if dates:
            processor.batch_advanced(dates, skip_existing=not args.force)
    
    elif args.command == 'pipeline':
        dates = processor.generate_date_range(args.start, args.end)
        if dates:
            processor.batch_pipeline(dates, skip_existing=not args.force)

if __name__ == '__main__':
    main()
