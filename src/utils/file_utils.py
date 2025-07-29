"""
文件操作工具模块
提供统一的文件读写和管理功能
"""
import os
import json
import shutil
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
from .logger import get_logger


class FileManager:
    """文件管理器，提供统一的文件操作接口"""
    
    def __init__(self, logger_name: str = "file_manager"):
        """初始化文件管理器"""
        self.logger = get_logger(logger_name)
    
    def ensure_dir(self, path: Union[str, Path]) -> bool:
        """
        确保目录存在，如果不存在则创建
        
        Args:
            path: 目录路径
            
        Returns:
            bool: 是否成功
        """
        try:
            Path(path).mkdir(parents=True, exist_ok=True)
            return True
        except Exception as e:
            self.logger.error(f"创建目录失败: {path}, 错误: {e}")
            return False
    
    def save_json(self, data: Any, path: Union[str, Path], indent: int = 4) -> bool:
        """
        保存JSON数据到文件
        
        Args:
            data: 要保存的数据
            path: 文件路径
            indent: JSON缩进
            
        Returns:
            bool: 是否成功
        """
        try:
            file_path = Path(path)
            self.ensure_dir(file_path.parent)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=indent)
            
            self.logger.info(f"JSON文件保存成功: {path}")
            return True
        except Exception as e:
            self.logger.error(f"JSON文件保存失败: {path}, 错误: {e}")
            return False
    
    def load_json(self, path: Union[str, Path]) -> Optional[Any]:
        """
        从文件加载JSON数据
        
        Args:
            path: 文件路径
            
        Returns:
            加载的数据，失败返回None
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.logger.debug(f"JSON文件加载成功: {path}")
            return data
        except FileNotFoundError:
            self.logger.warning(f"JSON文件不存在: {path}")
            return None
        except Exception as e:
            self.logger.error(f"JSON文件加载失败: {path}, 错误: {e}")
            return None
    
    def save_md(self, content: str, path: Union[str, Path]) -> bool:
        """
        保存Markdown内容到文件
        
        Args:
            content: Markdown内容
            path: 文件路径
            
        Returns:
            bool: 是否成功
        """
        try:
            file_path = Path(path)
            self.ensure_dir(file_path.parent)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.logger.info(f"MD文件保存成功: {path}")
            return True
        except Exception as e:
            self.logger.error(f"MD文件保存失败: {path}, 错误: {e}")
            return False
    
    def load_md(self, path: Union[str, Path]) -> Optional[str]:
        """
        从文件加载Markdown内容
        
        Args:
            path: 文件路径
            
        Returns:
            文件内容，失败返回None
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.logger.debug(f"MD文件加载成功: {path}")
            return content
        except FileNotFoundError:
            self.logger.warning(f"MD文件不存在: {path}")
            return None
        except Exception as e:
            self.logger.error(f"MD文件加载失败: {path}, 错误: {e}")
            return None
    
    def save_text(self, content: str, path: Union[str, Path]) -> bool:
        """
        保存文本内容到文件
        
        Args:
            content: 文本内容
            path: 文件路径
            
        Returns:
            bool: 是否成功
        """
        try:
            file_path = Path(path)
            self.ensure_dir(file_path.parent)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.logger.info(f"文本文件保存成功: {path}")
            return True
        except Exception as e:
            self.logger.error(f"文本文件保存失败: {path}, 错误: {e}")
            return False
    
    def load_text(self, path: Union[str, Path]) -> Optional[str]:
        """
        从文件加载文本内容
        
        Args:
            path: 文件路径
            
        Returns:
            文件内容，失败返回None
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.logger.debug(f"文本文件加载成功: {path}")
            return content
        except FileNotFoundError:
            self.logger.warning(f"文本文件不存在: {path}")
            return None
        except Exception as e:
            self.logger.error(f"文本文件加载失败: {path}, 错误: {e}")
            return None
    
    def copy_file(self, src: Union[str, Path], dst: Union[str, Path]) -> bool:
        """
        复制文件
        
        Args:
            src: 源文件路径
            dst: 目标文件路径
            
        Returns:
            bool: 是否成功
        """
        try:
            dst_path = Path(dst)
            self.ensure_dir(dst_path.parent)
            
            shutil.copy2(src, dst)
            self.logger.info(f"文件复制成功: {src} -> {dst}")
            return True
        except Exception as e:
            self.logger.error(f"文件复制失败: {src} -> {dst}, 错误: {e}")
            return False
    
    def move_file(self, src: Union[str, Path], dst: Union[str, Path]) -> bool:
        """
        移动文件
        
        Args:
            src: 源文件路径
            dst: 目标文件路径
            
        Returns:
            bool: 是否成功
        """
        try:
            dst_path = Path(dst)
            self.ensure_dir(dst_path.parent)
            
            shutil.move(src, dst)
            self.logger.info(f"文件移动成功: {src} -> {dst}")
            return True
        except Exception as e:
            self.logger.error(f"文件移动失败: {src} -> {dst}, 错误: {e}")
            return False
    
    def delete_file(self, path: Union[str, Path]) -> bool:
        """
        删除文件
        
        Args:
            path: 文件路径
            
        Returns:
            bool: 是否成功
        """
        try:
            Path(path).unlink()
            self.logger.info(f"文件删除成功: {path}")
            return True
        except FileNotFoundError:
            self.logger.warning(f"文件不存在: {path}")
            return True  # 文件不存在也算成功
        except Exception as e:
            self.logger.error(f"文件删除失败: {path}, 错误: {e}")
            return False
    
    def file_exists(self, path: Union[str, Path]) -> bool:
        """
        检查文件是否存在
        
        Args:
            path: 文件路径
            
        Returns:
            bool: 是否存在
        """
        return Path(path).exists()
    
    def get_file_size(self, path: Union[str, Path]) -> Optional[int]:
        """
        获取文件大小
        
        Args:
            path: 文件路径
            
        Returns:
            文件大小（字节），失败返回None
        """
        try:
            return Path(path).stat().st_size
        except Exception as e:
            self.logger.error(f"获取文件大小失败: {path}, 错误: {e}")
            return None


# 便捷函数
def save_json(data: Any, path: Union[str, Path], indent: int = 4) -> bool:
    """便捷函数：保存JSON"""
    return FileManager().save_json(data, path, indent)

def load_json(path: Union[str, Path]) -> Optional[Any]:
    """便捷函数：加载JSON"""
    return FileManager().load_json(path)

def save_md(content: str, path: Union[str, Path]) -> bool:
    """便捷函数：保存Markdown"""
    return FileManager().save_md(content, path)

def load_md(path: Union[str, Path]) -> Optional[str]:
    """便捷函数：加载Markdown"""
    return FileManager().load_md(path)
