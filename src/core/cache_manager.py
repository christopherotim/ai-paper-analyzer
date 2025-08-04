"""
缓存管理器模块
负责论文分析结果的缓存管理，避免重复分析
"""
import json
import hashlib
import time
from pathlib import Path
from typing import Dict, Any, Optional
from ..models.paper import Paper
from ..models.report import AnalysisResult
from ..utils.logger import get_logger


class PaperCacheManager:
    """
    论文分析缓存管理器
    
    负责缓存论文分析结果，避免重复分析相同论文
    """
    
    def __init__(self, cache_dir: str = "data/daily_reports/cache"):
        """
        初始化缓存管理器
        
        Args:
            cache_dir: 缓存目录路径
        """
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.logger = get_logger('cache_manager')
        
        # 缓存配置
        self.cache_expire_days = 30  # 缓存过期天数
        
        self.logger.info(f"缓存管理器初始化完成，缓存目录: {self.cache_dir}")
    
    def get_cache_key(self, paper: Paper) -> str:
        """
        生成论文的缓存键
        
        Args:
            paper: 论文对象
            
        Returns:
            缓存键字符串
        """
        # 使用论文ID、标题和摘要的前100字符生成唯一键
        content = f"{paper.id}_{paper.title}_{paper.summary[:100]}"
        return hashlib.md5(content.encode('utf-8')).hexdigest()
    
    def get_cached_result(self, paper: Paper) -> Optional[AnalysisResult]:
        """
        获取缓存的分析结果
        
        Args:
            paper: 论文对象
            
        Returns:
            缓存的分析结果，如果不存在或过期则返回None
        """
        try:
            cache_key = self.get_cache_key(paper)
            cache_file = self.cache_dir / f"{cache_key}.json"
            
            if not cache_file.exists():
                return None
            
            # 检查缓存是否过期
            if self._is_cache_expired(cache_file):
                self.logger.info(f"缓存已过期，删除: {cache_file.name}")
                cache_file.unlink()
                return None
            
            # 加载缓存数据
            with open(cache_file, 'r', encoding='utf-8') as f:
                cache_data = json.load(f)
            
            # 转换为AnalysisResult对象
            result = AnalysisResult.from_dict(cache_data['result'])
            
            self.logger.info(f"🎯 缓存命中: {paper.id}")
            return result
            
        except Exception as e:
            self.logger.warning(f"获取缓存失败: {paper.id} - {e}")
            return None
    
    def save_to_cache(self, paper: Paper, result: AnalysisResult) -> bool:
        """
        保存分析结果到缓存
        
        Args:
            paper: 论文对象
            result: 分析结果
            
        Returns:
            是否保存成功
        """
        try:
            cache_key = self.get_cache_key(paper)
            cache_file = self.cache_dir / f"{cache_key}.json"
            
            # 构建缓存数据
            cache_data = {
                'paper_id': paper.id,
                'paper_title': paper.title,
                'cache_time': time.time(),
                'result': result.to_dict()
            }
            
            # 保存到文件
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(cache_data, f, ensure_ascii=False, indent=2)
            
            self.logger.info(f"💾 缓存保存: {paper.id}")
            return True
            
        except Exception as e:
            self.logger.error(f"缓存保存失败: {paper.id} - {e}")
            return False
    
    def _is_cache_expired(self, cache_file: Path) -> bool:
        """
        检查缓存是否过期
        
        Args:
            cache_file: 缓存文件路径
            
        Returns:
            是否过期
        """
        try:
            # 检查文件修改时间
            file_mtime = cache_file.stat().st_mtime
            current_time = time.time()
            
            # 计算过期时间（秒）
            expire_seconds = self.cache_expire_days * 24 * 60 * 60
            
            return (current_time - file_mtime) > expire_seconds
            
        except Exception as e:
            self.logger.warning(f"检查缓存过期失败: {e}")
            return True  # 出错时认为已过期
    
    def clear_expired_cache(self) -> int:
        """
        清理过期的缓存文件
        
        Returns:
            清理的文件数量
        """
        cleared_count = 0
        
        try:
            for cache_file in self.cache_dir.glob("*.json"):
                if self._is_cache_expired(cache_file):
                    cache_file.unlink()
                    cleared_count += 1
            
            if cleared_count > 0:
                self.logger.info(f"🧹 清理过期缓存: {cleared_count} 个文件")
            
        except Exception as e:
            self.logger.error(f"清理缓存失败: {e}")
        
        return cleared_count
    
    def get_cache_stats(self) -> Dict[str, Any]:
        """
        获取缓存统计信息
        
        Returns:
            缓存统计字典
        """
        try:
            cache_files = list(self.cache_dir.glob("*.json"))
            total_files = len(cache_files)
            
            # 计算缓存大小
            total_size = sum(f.stat().st_size for f in cache_files)
            size_mb = total_size / (1024 * 1024)
            
            # 统计过期文件
            expired_count = sum(1 for f in cache_files if self._is_cache_expired(f))
            
            return {
                "总缓存文件": total_files,
                "缓存大小": f"{size_mb:.2f} MB",
                "过期文件": expired_count,
                "有效文件": total_files - expired_count,
                "缓存目录": str(self.cache_dir)
            }
            
        except Exception as e:
            self.logger.error(f"获取缓存统计失败: {e}")
            return {"错误": str(e)}
    
    def clear_all_cache(self) -> int:
        """
        清理所有缓存文件
        
        Returns:
            清理的文件数量
        """
        cleared_count = 0
        
        try:
            for cache_file in self.cache_dir.glob("*.json"):
                cache_file.unlink()
                cleared_count += 1
            
            self.logger.info(f"🧹 清理所有缓存: {cleared_count} 个文件")
            
        except Exception as e:
            self.logger.error(f"清理所有缓存失败: {e}")
        
        return cleared_count