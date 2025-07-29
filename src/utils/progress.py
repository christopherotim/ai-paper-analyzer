"""
进度管理模块
提供详细的进度显示和统计功能
"""
import time
from typing import Optional
from .console import ConsoleOutput


class ProgressManager:
    """进度管理器，提供详细的进度信息"""
    
    def __init__(self, total: int, desc: str):
        """
        初始化进度管理器
        
        Args:
            total: 总任务数
            desc: 任务描述
        """
        self.total = total
        self.current = 0
        self.desc = desc
        self.start_time = time.time()
        self.success_count = 0
        self.error_count = 0
        self.console = ConsoleOutput()
    
    def update(self, success: bool = True, item_name: str = ""):
        """
        更新进度
        
        Args:
            success: 是否成功
            item_name: 项目名称
        """
        self.current += 1
        if success:
            self.success_count += 1
            self.console.print_success(f"完成: {item_name} ({self.current}/{self.total})")
        else:
            self.error_count += 1
            self.console.print_error(f"失败: {item_name} ({self.current}/{self.total})")
        
        # 显示进度条和预估时间
        self._show_progress()
    
    def _show_progress(self):
        """显示详细进度信息"""
        elapsed = time.time() - self.start_time
        if self.current > 0:
            avg_time = elapsed / self.current
            remaining = (self.total - self.current) * avg_time
            
            # 计算进度百分比
            progress_percent = int(50 * self.current / self.total)
            progress_bar = "█" * progress_percent
            progress_bar += "░" * (50 - progress_percent)
            
            print(f"📊 进度: [{progress_bar}] {self.current}/{self.total} "
                  f"(成功:{self.success_count}, 失败:{self.error_count}) "
                  f"预计剩余: {remaining:.0f}秒")
    
    def get_stats(self) -> dict:
        """获取统计信息"""
        elapsed = time.time() - self.start_time
        return {
            "总任务数": self.total,
            "已完成": self.current,
            "成功数": self.success_count,
            "失败数": self.error_count,
            "成功率": f"{self.success_count/max(self.current, 1)*100:.1f}%",
            "耗时": f"{elapsed:.1f}秒"
        }
    
    def is_complete(self) -> bool:
        """检查是否完成"""
        return self.current >= self.total
    
    def get_remaining(self) -> int:
        """获取剩余任务数"""
        return max(0, self.total - self.current)
    
    def reset(self):
        """重置进度"""
        self.current = 0
        self.success_count = 0
        self.error_count = 0
        self.start_time = time.time()
    
    def finish(self):
        """完成进度显示"""
        stats = self.get_stats()
        self.console.print_summary(f"{self.desc} 完成统计", stats)


class SimpleProgress:
    """简单进度显示器"""
    
    def __init__(self, total: int, desc: str = "处理中"):
        self.total = total
        self.current = 0
        self.desc = desc
    
    def update(self, step: int = 1):
        """更新进度"""
        self.current += step
        percent = int(100 * self.current / self.total)
        bar_length = 30
        filled_length = int(bar_length * self.current / self.total)
        
        bar = "█" * filled_length + "░" * (bar_length - filled_length)
        ConsoleOutput.print_inline(f"{self.desc}: [{bar}] {percent}%")
        
        if self.current >= self.total:
            print()  # 换行
    
    def finish(self):
        """完成进度"""
        ConsoleOutput.print_success(f"{self.desc} 完成！")


# 便捷函数
def create_progress(total: int, desc: str) -> ProgressManager:
    """创建进度管理器"""
    return ProgressManager(total, desc)

def create_simple_progress(total: int, desc: str = "处理中") -> SimpleProgress:
    """创建简单进度显示器"""
    return SimpleProgress(total, desc)
