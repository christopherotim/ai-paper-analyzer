"""
报告数据模型
定义分析报告相关的数据结构
"""
from dataclasses import dataclass, asdict, field
from typing import Dict, Any, List, Optional
from datetime import datetime
import json


@dataclass
class AnalysisResult:
    """
    论文分析结果模型
    
    Attributes:
        paper_id: 论文ID
        paper_url: 论文链接
        title: 英文标题
        translation: 中文标题
        authors: 作者团队
        publish_date: 发表日期
        model_function: 模型功能
        page_content: 原始分析内容
        analysis_time: 分析时间
    """
    paper_id: str
    paper_url: str
    title: str
    translation: str
    authors: str
    publish_date: str
    model_function: str
    page_content: str = ""
    analysis_time: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def __post_init__(self):
        """初始化后处理"""
        # 清理字段中的多余空白
        self.title = self.title.strip()
        self.translation = self.translation.strip()
        self.authors = self.authors.strip()
        self.model_function = self.model_function.strip()
        self.page_content = self.page_content.strip()
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'AnalysisResult':
        """从字典创建AnalysisResult实例"""
        return cls(
            paper_id=data.get('paper_id', ''),
            paper_url=data.get('paper_url', ''),
            title=data.get('title', ''),
            translation=data.get('translation', ''),
            authors=data.get('authors', ''),
            publish_date=data.get('publish_date', ''),
            model_function=data.get('model_function', ''),
            page_content=data.get('page_content', ''),
            analysis_time=data.get('analysis_time', datetime.now().isoformat())
        )
    
    @classmethod
    def from_legacy_format(cls, data: Dict[str, Any]) -> 'AnalysisResult':
        """从旧格式数据创建实例"""
        # 处理不同的字段名映射
        paper_id = data.get('id') or data.get('paper_id') or ""
        paper_url = data.get('url') or data.get('paper_url') or ""
        
        # 如果没有URL但有ID，生成URL
        if not paper_url and paper_id:
            paper_url = f"https://arxiv.org/abs/{paper_id}"
        
        return cls(
            paper_id=paper_id,
            paper_url=paper_url,
            title=data.get('title', ''),
            translation=data.get('translation', ''),
            authors=data.get('authors', ''),
            publish_date=data.get('publish_date', ''),
            model_function=data.get('model_function', ''),
            page_content=data.get('page_content', ''),
            analysis_time=data.get('analysis_time', datetime.now().isoformat())
        )
    
    def get_short_summary(self, max_length: int = 100) -> str:
        """获取简短摘要"""
        if len(self.model_function) <= max_length:
            return self.model_function
        return self.model_function[:max_length-3] + "..."
    
    def is_valid(self) -> bool:
        """检查数据是否有效"""
        required_fields = [self.paper_id, self.title, self.translation]
        return all(field.strip() for field in required_fields)
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"AnalysisResult({self.paper_id}: {self.translation[:30]}...)"


@dataclass
class ClassificationResult:
    """
    论文分类结果模型
    
    Attributes:
        paper_id: 论文ID
        category: 分类名称
        confidence: 置信度
        md_content: 生成的MD内容
        classification_time: 分类时间
    """
    paper_id: str
    category: str
    confidence: float
    md_content: str
    classification_time: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ClassificationResult':
        """从字典创建ClassificationResult实例"""
        return cls(
            paper_id=data.get('paper_id', ''),
            category=data.get('category', ''),
            confidence=data.get('confidence', 0.0),
            md_content=data.get('md_content', ''),
            classification_time=data.get('classification_time', datetime.now().isoformat())
        )
    
    def is_high_confidence(self, threshold: float = 0.8) -> bool:
        """检查是否高置信度"""
        return self.confidence >= threshold
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"ClassificationResult({self.paper_id}: {self.category}, {self.confidence:.2f})"


@dataclass
class DailyReport:
    """
    每日报告模型
    
    Attributes:
        date: 报告日期
        total_papers: 论文总数
        analysis_results: 分析结果列表
        generation_time: 生成时间
        metadata: 元数据
    """
    date: str
    total_papers: int
    analysis_results: List[AnalysisResult]
    generation_time: str = field(default_factory=lambda: datetime.now().isoformat())
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """初始化后处理"""
        # 确保analysis_results是列表
        if not isinstance(self.analysis_results, list):
            self.analysis_results = []
        
        # 更新论文总数
        self.total_papers = len(self.analysis_results)
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            'date': self.date,
            'total_papers': self.total_papers,
            'analysis_results': [result.to_dict() for result in self.analysis_results],
            'generation_time': self.generation_time,
            'metadata': self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DailyReport':
        """从字典创建DailyReport实例"""
        analysis_results = []
        for result_data in data.get('analysis_results', []):
            try:
                result = AnalysisResult.from_dict(result_data)
                analysis_results.append(result)
            except Exception:
                # 尝试从旧格式创建
                try:
                    result = AnalysisResult.from_legacy_format(result_data)
                    analysis_results.append(result)
                except Exception:
                    continue
        
        return cls(
            date=data.get('date', ''),
            total_papers=data.get('total_papers', len(analysis_results)),
            analysis_results=analysis_results,
            generation_time=data.get('generation_time', datetime.now().isoformat()),
            metadata=data.get('metadata', {})
        )
    
    def add_analysis_result(self, result: AnalysisResult):
        """添加分析结果"""
        if not isinstance(result, AnalysisResult):
            raise TypeError("必须是AnalysisResult实例")
        
        self.analysis_results.append(result)
        self.total_papers = len(self.analysis_results)
    
    def get_successful_analyses(self) -> List[AnalysisResult]:
        """获取成功的分析结果"""
        return [result for result in self.analysis_results if result.is_valid()]
    
    def get_statistics(self) -> Dict[str, Any]:
        """获取统计信息"""
        successful = self.get_successful_analyses()
        
        return {
            "总论文数": self.total_papers,
            "成功分析": len(successful),
            "失败分析": self.total_papers - len(successful),
            "成功率": f"{len(successful)/max(self.total_papers, 1)*100:.1f}%",
            "生成时间": self.generation_time,
            "日期": self.date
        }
    
    def save_to_file(self, file_path: str) -> bool:
        """保存到文件"""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.to_dict(), f, ensure_ascii=False, indent=4)
            return True
        except Exception:
            return False
    
    @classmethod
    def load_from_file(cls, file_path: str) -> Optional['DailyReport']:
        """从文件加载"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return cls.from_dict(data)
        except Exception:
            return None
    
    def __len__(self) -> int:
        """获取分析结果数量"""
        return len(self.analysis_results)
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"DailyReport({self.date}: {self.total_papers} papers)"


@dataclass
class AnalysisSummary:
    """
    分析汇总模型
    
    Attributes:
        date: 日期
        categories: 分类统计
        total_papers: 总论文数
        classification_results: 分类结果列表
    """
    date: str
    categories: Dict[str, int]
    total_papers: int
    classification_results: List[ClassificationResult] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            'date': self.date,
            'categories': self.categories,
            'total_papers': self.total_papers,
            'classification_results': [result.to_dict() for result in self.classification_results]
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'AnalysisSummary':
        """从字典创建AnalysisSummary实例"""
        classification_results = []
        for result_data in data.get('classification_results', []):
            try:
                result = ClassificationResult.from_dict(result_data)
                classification_results.append(result)
            except Exception:
                continue
        
        return cls(
            date=data.get('date', ''),
            categories=data.get('categories', {}),
            total_papers=data.get('total_papers', 0),
            classification_results=classification_results
        )
    
    def get_top_categories(self, top_n: int = 5) -> List[tuple]:
        """获取前N个分类"""
        sorted_categories = sorted(self.categories.items(), key=lambda x: x[1], reverse=True)
        return sorted_categories[:top_n]
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"AnalysisSummary({self.date}: {len(self.categories)} categories, {self.total_papers} papers)"


# 便捷函数
def create_analysis_result(paper_id: str, title: str, translation: str, **kwargs) -> AnalysisResult:
    """便捷函数：创建分析结果"""
    return AnalysisResult(
        paper_id=paper_id,
        paper_url=f"https://arxiv.org/abs/{paper_id}",
        title=title,
        translation=translation,
        **kwargs
    )

def create_daily_report(date: str, analysis_results: List[AnalysisResult] = None) -> DailyReport:
    """便捷函数：创建日报"""
    return DailyReport(
        date=date,
        total_papers=len(analysis_results) if analysis_results else 0,
        analysis_results=analysis_results or []
    )
