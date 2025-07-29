"""
论文数据模型
定义论文相关的数据结构
"""
from dataclasses import dataclass, asdict
from typing import Dict, Any, Optional
import re


@dataclass
class Paper:
    """
    论文数据模型
    
    Attributes:
        id: 论文ID (如: 2405.08317)
        title: 英文标题
        translation: 中文翻译标题
        url: arXiv链接
        authors: 作者团队信息
        publish_date: 发表日期
        model_function: 模型功能描述
    """
    id: str
    title: str
    translation: str
    url: str
    authors: str = ""
    publish_date: str = ""
    model_function: str = ""
    
    def __post_init__(self):
        """初始化后处理"""
        # 确保URL格式正确
        if self.url and not self.url.startswith('http'):
            self.url = f"https://arxiv.org/abs/{self.id}"
        
        # 清理字段中的多余空白
        self.title = self.title.strip()
        self.translation = self.translation.strip()
        self.authors = self.authors.strip()
        self.model_function = self.model_function.strip()
    
    def to_dict(self) -> Dict[str, Any]:
        """
        转换为字典格式
        
        Returns:
            字典格式的论文数据
        """
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Paper':
        """
        从字典创建Paper实例
        
        Args:
            data: 包含论文数据的字典
            
        Returns:
            Paper实例
        """
        # 提取必需字段
        required_fields = ['id', 'title', 'translation', 'url']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"缺少必需字段: {field}")
        
        return cls(
            id=data['id'],
            title=data['title'],
            translation=data['translation'],
            url=data['url'],
            authors=data.get('authors', ''),
            publish_date=data.get('publish_date', ''),
            model_function=data.get('model_function', '')
        )
    
    @classmethod
    def from_legacy_format(cls, data: Dict[str, Any]) -> 'Paper':
        """
        从旧格式数据创建Paper实例
        兼容现有的JSON数据格式
        
        Args:
            data: 旧格式的论文数据
            
        Returns:
            Paper实例
        """
        # 处理不同的字段名映射
        paper_id = data.get('id') or data.get('paper_id') or ""
        title = data.get('title') or ""
        translation = data.get('translation') or ""
        url = data.get('url') or data.get('paper_url') or ""
        
        # 如果没有URL但有ID，生成URL
        if not url and paper_id:
            url = f"https://arxiv.org/abs/{paper_id}"
        
        return cls(
            id=paper_id,
            title=title,
            translation=translation,
            url=url,
            authors=data.get('authors', ''),
            publish_date=data.get('publish_date', ''),
            model_function=data.get('model_function', '')
        )
    
    def get_arxiv_id(self) -> str:
        """
        获取arXiv ID
        
        Returns:
            arXiv ID
        """
        return self.id
    
    def get_short_title(self, max_length: int = 50) -> str:
        """
        获取简短标题（用于显示）
        
        Args:
            max_length: 最大长度
            
        Returns:
            简短标题
        """
        if len(self.translation) <= max_length:
            return self.translation
        return self.translation[:max_length-3] + "..."
    
    def has_analysis_data(self) -> bool:
        """
        检查是否包含分析数据
        
        Returns:
            是否包含分析数据
        """
        return bool(self.authors and self.publish_date and self.model_function)
    
    def validate(self) -> bool:
        """
        验证数据完整性
        
        Returns:
            是否有效
        """
        # 检查必需字段
        if not all([self.id, self.title, self.translation, self.url]):
            return False
        
        # 检查ID格式（arXiv格式）
        arxiv_pattern = r'^\d{4}\.\d{4,5}$'
        if not re.match(arxiv_pattern, self.id):
            return False
        
        # 检查URL格式
        if not self.url.startswith('https://arxiv.org/abs/'):
            return False
        
        return True
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"Paper({self.id}: {self.get_short_title()})"
    
    def __repr__(self) -> str:
        """详细字符串表示"""
        return (f"Paper(id='{self.id}', title='{self.title[:30]}...', "
                f"translation='{self.translation[:30]}...', "
                f"has_analysis={self.has_analysis_data()})")


class PaperCollection:
    """论文集合管理类"""
    
    def __init__(self, papers: Optional[list] = None):
        """
        初始化论文集合
        
        Args:
            papers: 论文列表
        """
        self.papers = papers or []
    
    def add_paper(self, paper: Paper):
        """添加论文"""
        if not isinstance(paper, Paper):
            raise TypeError("必须是Paper实例")
        self.papers.append(paper)
    
    def get_paper_by_id(self, paper_id: str) -> Optional[Paper]:
        """根据ID获取论文"""
        for paper in self.papers:
            if paper.id == paper_id:
                return paper
        return None
    
    def get_papers_by_date(self, date: str) -> list:
        """根据日期获取论文"""
        return [p for p in self.papers if p.publish_date == date]
    
    def get_analyzed_papers(self) -> list:
        """获取已分析的论文"""
        return [p for p in self.papers if p.has_analysis_data()]
    
    def to_dict_list(self) -> list:
        """转换为字典列表"""
        return [paper.to_dict() for paper in self.papers]
    
    def __len__(self) -> int:
        """获取论文数量"""
        return len(self.papers)
    
    def __iter__(self):
        """迭代器"""
        return iter(self.papers)


# 便捷函数
def create_paper(id: str, title: str, translation: str, url: str = None, **kwargs) -> Paper:
    """
    便捷函数：创建论文实例
    
    Args:
        id: 论文ID
        title: 英文标题
        translation: 中文标题
        url: 论文链接
        **kwargs: 其他字段
        
    Returns:
        Paper实例
    """
    if not url:
        url = f"https://arxiv.org/abs/{id}"
    
    return Paper(
        id=id,
        title=title,
        translation=translation,
        url=url,
        **kwargs
    )

def papers_from_dict_list(data_list: list) -> PaperCollection:
    """
    从字典列表创建论文集合
    
    Args:
        data_list: 字典列表
        
    Returns:
        PaperCollection实例
    """
    papers = []
    for data in data_list:
        try:
            paper = Paper.from_dict(data)
            papers.append(paper)
        except Exception as e:
            # 尝试从旧格式创建
            try:
                paper = Paper.from_legacy_format(data)
                papers.append(paper)
            except Exception:
                # 跳过无效数据
                continue
    
    return PaperCollection(papers)
