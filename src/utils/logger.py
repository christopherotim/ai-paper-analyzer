"""
日志系统模块
提供统一的日志管理功能
"""
import os
import logging
import logging.handlers
from datetime import datetime
from pathlib import Path
from typing import Optional


class Logger:
    """统一的日志管理系统"""
    
    def __init__(self, name: str, date: str = None, log_level: str = "INFO"):
        """
        初始化日志器
        
        Args:
            name: 日志器名称
            date: 日期字符串，用于日志文件命名
            log_level: 日志级别
        """
        self.name = name
        self.date = date or datetime.now().strftime('%Y-%m-%d')
        self.logger = logging.getLogger(name)
        self.log_level = getattr(logging, log_level.upper(), logging.INFO)
        
        # 避免重复添加处理器
        if not self.logger.handlers:
            self._setup_logger()
    
    def _setup_logger(self):
        """配置日志器"""
        self.logger.setLevel(self.log_level)
        
        # 控制台输出处理器
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] %(message)s',
            datefmt='%H:%M:%S'
        )
        console_handler.setFormatter(console_formatter)
        console_handler.setLevel(self.log_level)
        
        # 文件输出处理器
        log_dir = Path("logs/daily")
        log_dir.mkdir(parents=True, exist_ok=True)
        
        log_file = log_dir / f"{self.date}.log"
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        )
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.DEBUG)  # 文件记录所有级别
        
        # 错误日志处理器
        error_dir = Path("logs/error")
        error_dir.mkdir(parents=True, exist_ok=True)
        
        error_file = error_dir / f"{self.date}_error.log"
        error_handler = logging.FileHandler(error_file, encoding='utf-8')
        error_handler.setFormatter(file_formatter)
        error_handler.setLevel(logging.ERROR)
        
        # 添加处理器
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(error_handler)
    
    def debug(self, message: str):
        """记录调试信息"""
        self.logger.debug(message)
    
    def info(self, message: str):
        """记录信息"""
        self.logger.info(message)
    
    def warning(self, message: str):
        """记录警告"""
        self.logger.warning(message)
    
    def error(self, message: str):
        """记录错误"""
        self.logger.error(message)
    
    def critical(self, message: str):
        """记录严重错误"""
        self.logger.critical(message)
    
    def log_function_call(self, func_name: str, args: dict = None):
        """记录函数调用"""
        if args:
            self.debug(f"调用函数: {func_name}, 参数: {args}")
        else:
            self.debug(f"调用函数: {func_name}")
    
    def log_performance(self, operation: str, duration: float):
        """记录性能信息"""
        self.info(f"性能统计: {operation} 耗时 {duration:.2f}秒")
    
    def log_api_call(self, api_name: str, status: str, duration: float = None):
        """记录API调用"""
        if duration:
            self.info(f"API调用: {api_name}, 状态: {status}, 耗时: {duration:.2f}秒")
        else:
            self.info(f"API调用: {api_name}, 状态: {status}")


class FileLogger:
    """简单的文件日志器"""
    
    def __init__(self, log_file: str):
        """
        初始化文件日志器
        
        Args:
            log_file: 日志文件路径
        """
        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
    
    def write(self, message: str, level: str = "INFO"):
        """写入日志"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] [{level}] {message}\n"
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)
    
    def info(self, message: str):
        """记录信息"""
        self.write(message, "INFO")
    
    def error(self, message: str):
        """记录错误"""
        self.write(message, "ERROR")
    
    def warning(self, message: str):
        """记录警告"""
        self.write(message, "WARNING")


# 便捷函数
def get_logger(name: str, date: str = None) -> Logger:
    """获取日志器"""
    return Logger(name, date)

def get_file_logger(log_file: str) -> FileLogger:
    """获取文件日志器"""
    return FileLogger(log_file)
