"""
元数据下载器模块
负责从HuggingFace API下载论文元数据
"""
import os
import json
import requests
from pathlib import Path
from typing import Dict, Any, Optional
from ..utils.console import ConsoleOutput
from ..utils.logger import get_logger
from ..utils.file_utils import FileManager


class MetadataDownloader:
    """
    论文元数据下载器
    
    负责从HuggingFace API下载每日论文数据
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        初始化下载器
        
        Args:
            config: 配置字典，包含output_dir等配置
        """
        self.config = config
        self.console = ConsoleOutput()
        self.logger = get_logger('downloader')
        self.file_manager = FileManager('downloader')
        
        # 设置默认配置
        self.output_dir = config.get('output_dir', 'data/daily_reports')
        self.api_base_url = config.get('api_url', 'https://hf-mirror.com/api/daily_papers')
        self.timeout = config.get('timeout', 30)
        self.proxies = config.get('proxies', {"http": None, "https": None})
    
    def download(self, date: str, silent: bool = False) -> bool:
        """
        下载指定日期的论文元数据
        
        Args:
            date: 日期字符串 (YYYY-MM-DD)
            silent: 是否静默模式
            
        Returns:
            bool: 是否成功
        """
        if not silent:
            self.console.print_header("下载论文元数据", 1)
        
        # 构建API URL
        url = f"{self.api_base_url}?date={date}"
        
        if not silent:
            self.console.print_info(f"请求API: {url}")
        
        self.logger.info(f"开始下载 {date} 的论文元数据")
        
        try:
            # 发送HTTP请求
            response = self._fetch_from_api(url)
            
            if response is None:
                return False
            
            # 保存元数据
            success = self._save_metadata(date, response)
            
            if success and not silent:
                metadata_file = self._get_metadata_file_path(date)
                self.console.print_success(f"元数据已保存: {metadata_file}")
                self.logger.info(f"成功下载并保存元数据到: {metadata_file}")
            
            return success
            
        except Exception as e:
            if not silent:
                self.console.print_error(f"下载失败: {e}")
            self.logger.error(f"下载异常: {e}")
            return False
    
    def _fetch_from_api(self, url: str) -> Optional[Dict[str, Any]]:
        """
        从API获取数据
        
        Args:
            url: API URL
            
        Returns:
            API响应数据，失败返回None
        """
        try:
            response = requests.get(
                url,
                proxies=self.proxies,
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                self.logger.info(f"API请求成功，状态码: {response.status_code}")
                return response.json()
            else:
                self.console.print_warning(f"API返回状态码: {response.status_code}")
                self.logger.warning(f"API请求失败，状态码: {response.status_code}")
                return None
                
        except requests.exceptions.Timeout:
            self.console.print_error(f"请求超时 (>{self.timeout}秒)")
            self.logger.error(f"API请求超时: {url}")
            return None
        except requests.exceptions.ConnectionError:
            self.console.print_error("网络连接错误")
            self.logger.error(f"网络连接错误: {url}")
            return None
        except requests.exceptions.RequestException as e:
            self.console.print_error(f"请求异常: {e}")
            self.logger.error(f"请求异常: {url}, 错误: {e}")
            return None
        except json.JSONDecodeError as e:
            self.console.print_error(f"JSON解析失败: {e}")
            self.logger.error(f"JSON解析失败: {url}, 错误: {e}")
            return None
    
    def _save_metadata(self, date: str, data: Dict[str, Any]) -> bool:
        """
        保存元数据到文件
        
        Args:
            date: 日期字符串
            data: 元数据
            
        Returns:
            bool: 是否成功
        """
        try:
            # 确保元数据目录存在
            metadata_dir = Path(self.output_dir) / 'metadata'
            self.file_manager.ensure_dir(metadata_dir)
            
            # 构建文件路径
            file_path = metadata_dir / f"{date}.json"
            
            # 保存数据
            success = self.file_manager.save_json(data, file_path)
            
            if success:
                self.logger.info(f"元数据保存成功: {file_path}")
            else:
                self.logger.error(f"元数据保存失败: {file_path}")
            
            return success
            
        except Exception as e:
            self.logger.error(f"保存元数据异常: {e}")
            return False
    
    def _get_metadata_file_path(self, date: str) -> str:
        """
        获取元数据文件路径
        
        Args:
            date: 日期字符串
            
        Returns:
            文件路径字符串
        """
        return str(Path(self.output_dir) / 'metadata' / f"{date}.json")
    
    def check_metadata_exists(self, date: str) -> bool:
        """
        检查元数据文件是否已存在
        
        Args:
            date: 日期字符串
            
        Returns:
            bool: 是否存在
        """
        file_path = self._get_metadata_file_path(date)
        return Path(file_path).exists()
    
    def get_metadata_info(self, date: str) -> Optional[Dict[str, Any]]:
        """
        获取元数据文件信息
        
        Args:
            date: 日期字符串
            
        Returns:
            元数据信息，包含文件大小、修改时间等
        """
        file_path = Path(self._get_metadata_file_path(date))
        
        if not file_path.exists():
            return None
        
        try:
            stat = file_path.stat()
            return {
                "file_path": str(file_path),
                "file_size": stat.st_size,
                "modified_time": stat.st_mtime,
                "exists": True
            }
        except Exception as e:
            self.logger.error(f"获取文件信息失败: {e}")
            return None
    
    def load_metadata(self, date: str) -> Optional[Dict[str, Any]]:
        """
        加载已下载的元数据
        
        Args:
            date: 日期字符串
            
        Returns:
            元数据内容，失败返回None
        """
        file_path = self._get_metadata_file_path(date)
        return self.file_manager.load_json(file_path)
    
    def get_download_statistics(self) -> Dict[str, Any]:
        """
        获取下载统计信息
        
        Returns:
            统计信息字典
        """
        metadata_dir = Path(self.output_dir) / 'metadata'
        
        if not metadata_dir.exists():
            return {"total_files": 0, "files": []}
        
        json_files = list(metadata_dir.glob("*.json"))
        
        return {
            "total_files": len(json_files),
            "files": [f.stem for f in json_files],
            "metadata_dir": str(metadata_dir)
        }


# 便捷函数
def create_downloader(config: Dict[str, Any]) -> MetadataDownloader:
    """
    便捷函数：创建下载器实例
    
    Args:
        config: 配置字典
        
    Returns:
        MetadataDownloader实例
    """
    return MetadataDownloader(config)

def download_metadata(date: str, output_dir: str = 'data/daily_reports',
                     silent: bool = False) -> bool:
    """
    便捷函数：下载元数据
    
    Args:
        date: 日期字符串
        output_dir: 输出目录
        silent: 是否静默模式
        
    Returns:
        bool: 是否成功
    """
    config = {'output_dir': output_dir}
    downloader = MetadataDownloader(config)
    return downloader.download(date, silent)
