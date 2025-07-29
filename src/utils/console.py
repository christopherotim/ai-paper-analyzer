"""
控制台输出美化模块
提供统一的控制台输出格式和样式
"""
import sys
from typing import Dict, Any


class ConsoleOutput:
    """统一的控制台输出管理器"""
    
    @staticmethod
    def print_header(title: str, step: int = None):
        """打印步骤标题"""
        if step:
            print(f"\n{'='*60}")
            print(f"📋 步骤{step}：{title}")
            print(f"{'='*60}")
        else:
            print(f"\n🎯 {title}")

    @staticmethod
    def print_separator(length: int = 50):
        """打印分隔线（类似旧脚本）"""
        print("=" * length)
    
    @staticmethod
    def print_success(message: str):
        """打印成功信息"""
        print(f"✅ {message}")
    
    @staticmethod
    def print_error(message: str):
        """打印错误信息"""
        print(f"❌ {message}")
    
    @staticmethod
    def print_warning(message: str):
        """打印警告信息"""
        print(f"⚠️  {message}")
    
    @staticmethod
    def print_info(message: str):
        """打印信息"""
        print(f"📡 {message}")
    
    @staticmethod
    def print_progress(current: int, total: int, item_name: str):
        """打印处理进度"""
        print(f"🔍 处理第 {current}/{total} 项: {item_name}")
    
    @staticmethod
    def print_summary(title: str, stats: Dict[str, Any]):
        """打印汇总信息"""
        print(f"\n{'='*60}")
        print(f"📊 {title}")
        print(f"{'='*60}")
        for key, value in stats.items():
            print(f"📈 {key}: {value}")
    
    @staticmethod
    def print_separator(char: str = "=", length: int = 50):
        """打印分隔线"""
        print(char * length)
    
    @staticmethod
    def print_task_start(task_name: str):
        """打印任务开始"""
        print(f"\n🚀 开始任务: {task_name}")
    
    @staticmethod
    def print_task_complete(task_name: str):
        """打印任务完成"""
        print(f"🎉 任务完成: {task_name}")
    
    @staticmethod
    def print_loading(message: str):
        """打印加载信息"""
        print(f"⏳ {message}...")
    
    @staticmethod
    def print_skip(message: str):
        """打印跳过信息"""
        print(f"⏭️  跳过: {message}")
    
    @staticmethod
    def print_retry(message: str, attempt: int):
        """打印重试信息"""
        print(f"🔄 重试第 {attempt} 次: {message}")
    
    @staticmethod
    def clear_line():
        """清除当前行"""
        sys.stdout.write('\r\033[K')
        sys.stdout.flush()
    
    @staticmethod
    def print_inline(message: str):
        """在同一行打印信息（不换行）"""
        sys.stdout.write(f"\r{message}")
        sys.stdout.flush()


# 便捷函数，可以直接导入使用
def print_header(title: str, step: int = None):
    """便捷函数：打印标题"""
    ConsoleOutput.print_header(title, step)

def print_success(message: str):
    """便捷函数：打印成功信息"""
    ConsoleOutput.print_success(message)

def print_error(message: str):
    """便捷函数：打印错误信息"""
    ConsoleOutput.print_error(message)

def print_warning(message: str):
    """便捷函数：打印警告信息"""
    ConsoleOutput.print_warning(message)

def print_info(message: str):
    """便捷函数：打印信息"""
    ConsoleOutput.print_info(message)
