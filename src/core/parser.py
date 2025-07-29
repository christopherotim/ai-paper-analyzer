"""
内容解析器模块
负责解析AI分析内容和清洗后的数据
"""
import re
from typing import Dict, List, Any, Optional
from ..utils.logger import get_logger
from ..models.paper import Paper, PaperCollection


class ContentParser:
    """
    内容解析器
    
    负责解析AI返回的分析内容和清洗后的数据
    """
    
    def __init__(self):
        """初始化解析器"""
        self.logger = get_logger('parser')
    
    def parse_analysis_content(self, content: str) -> Dict[str, str]:
        """
        解析AI返回的论文分析内容，提取结构化字段
        
        Args:
            content: AI返回的分析内容
            
        Returns:
            解析后的字段字典
        """
        parsed_data = {
            'authors': '',
            'publish_date': '',
            'model_function': ''
        }
        
        if not content or not isinstance(content, str):
            self.logger.warning("分析内容为空或格式错误")
            return parsed_data
        
        # 定义字段映射模式
        field_patterns = {
            'authors': [
                r'\*\*作者团队\*\*[：:]\s*([^\n\r]+)',
                r'作者团队[：:]\s*([^\n\r]+)',
                r'\*\*Authors\*\*[：:]\s*([^\n\r]+)',
                r'Authors[：:]\s*([^\n\r]+)'
            ],
            'publish_date': [
                r'\*\*发表日期\*\*[：:]\s*([^\n\r]+)',
                r'发表日期[：:]\s*([^\n\r]+)',
                r'\*\*发布日期\*\*[：:]\s*([^\n\r]+)',
                r'发布日期[：:]\s*([^\n\r]+)',
                r'\*\*Publication Date\*\*[：:]\s*([^\n\r]+)',
                r'Publication Date[：:]\s*([^\n\r]+)'
            ],
            'model_function': [
                r'\*\*模型功能\*\*[：:]\s*([^\n\r]+)',
                r'模型功能[：:]\s*([^\n\r]+)',
                r'\*\*功能描述\*\*[：:]\s*([^\n\r]+)',
                r'功能描述[：:]\s*([^\n\r]+)',
                r'\*\*Model Function\*\*[：:]\s*([^\n\r]+)',
                r'Model Function[：:]\s*([^\n\r]+)'
            ]
        }
        
        # 提取各个字段
        for field, patterns in field_patterns.items():
            for pattern in patterns:
                match = re.search(pattern, content, re.IGNORECASE)
                if match:
                    parsed_data[field] = match.group(1).strip()
                    break
        
        # 记录解析结果
        self.logger.debug(f"解析结果: {parsed_data}")
        
        return parsed_data
    
    def parse_cleaned_data(self, clean_data: List[str]) -> List[Paper]:
        """
        解析清洗后的数据，提取论文信息

        Args:
            clean_data: 清洗后的数据列表（字符串列表）

        Returns:
            论文对象列表
        """
        papers = []

        if not clean_data:
            self.logger.info("清洗数据为空")
            return papers

        # 处理字符串列表
        for content in clean_data:
            if not content or not isinstance(content, str):
                continue

            # 检查是否为空数据或错误信息
            if self._is_empty_or_error_content(content):
                continue

            # 解析论文信息
            paper_list = self._extract_papers_from_content(content)
            papers.extend(paper_list)

        self.logger.info(f"从清洗数据中解析出 {len(papers)} 篇论文")
        return papers

    
    def _is_empty_or_error_content(self, content: str) -> bool:
        """
        检查内容是否为空数据或错误信息
        
        Args:
            content: 内容字符串
            
        Returns:
            是否为空或错误内容
        """
        empty_indicators = [
            "无论文数据",
            "没有提供任何论文信息",
            "数据为空",
            "no papers",
            "empty data"
        ]
        
        content_lower = content.lower().strip()
        
        for indicator in empty_indicators:
            if indicator.lower() in content_lower:
                return True
        
        return len(content.strip()) == 0
    
    def _extract_papers_from_content(self, content: str) -> List[Paper]:
        """
        从单个内容中提取论文信息
        
        Args:
            content: 内容字符串
            
        Returns:
            论文对象列表
        """
        papers = []
        
        # 定义多种可能的论文信息格式
        patterns = [
            # 标准格式：1. 论文题目：... 中文翻译：... 论文ID：...
            r'(\d+)\.\s*论文题目：([^\n\r]+)\s*中文翻译：([^\n\r]+)\s*论文ID：([^\n\r]+)',
            # 简化格式：论文题目：... 中文翻译：... 论文ID：...
            r'论文题目：([^\n\r]+)\s*中文翻译：([^\n\r]+)\s*论文ID：([^\n\r]+)',
            # 带空格的格式
            r'论文题目：\s*([^\n\r]+)\s*中文翻译：\s*([^\n\r]+)\s*论文ID：\s*([^\n\r]+)',
            # 英文格式
            r'Title:\s*([^\n\r]+)\s*Translation:\s*([^\n\r]+)\s*ID:\s*([^\n\r]+)'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, content, re.MULTILINE | re.DOTALL)
            
            if matches:
                for match in matches:
                    try:
                        if len(match) == 4:  # 包含序号的格式
                            _, title, translation, paper_id = match
                        else:  # 不包含序号的格式
                            title, translation, paper_id = match
                        
                        # 清理数据
                        title = self._clean_text(title)
                        translation = self._clean_text(translation)
                        paper_id = self._clean_text(paper_id)
                        
                        # 验证论文ID格式
                        if not self._is_valid_arxiv_id(paper_id):
                            self.logger.warning(f"无效的arXiv ID: {paper_id}")
                            continue
                        
                        # 创建论文对象
                        paper = Paper(
                            id=paper_id,
                            title=title,
                            translation=translation,
                            url=f"https://arxiv.org/abs/{paper_id}"
                        )
                        
                        papers.append(paper)
                        self.logger.debug(f"解析论文: {paper_id} - {translation}")
                        
                    except Exception as e:
                        self.logger.error(f"解析论文信息失败: {e}")
                        continue
                
                break  # 找到匹配的模式就停止
        
        return papers
    
    def _clean_text(self, text: str) -> str:
        """
        清理文本内容
        
        Args:
            text: 原始文本
            
        Returns:
            清理后的文本
        """
        if not text:
            return ""
        
        # 移除多余的空白字符
        text = text.strip()
        
        # 移除引号
        text = text.strip('"').strip("'").strip('"').strip('"')
        
        # 移除多余的空格
        text = re.sub(r'\s+', ' ', text)
        
        return text
    
    def _is_valid_arxiv_id(self, paper_id: str) -> bool:
        """
        验证arXiv ID格式
        
        Args:
            paper_id: 论文ID
            
        Returns:
            是否有效
        """
        if not paper_id:
            return False
        
        # arXiv ID格式：YYMM.NNNNN 或 YYYY.NNNNN
        arxiv_pattern = r'^\d{4}\.\d{4,5}$'
        return bool(re.match(arxiv_pattern, paper_id))
    
    def parse_batch_analysis_results(self, results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        批量解析分析结果
        
        Args:
            results: 原始分析结果列表
            
        Returns:
            解析后的结果列表
        """
        parsed_results = []
        
        for result in results:
            try:
                if 'page_content' in result:
                    # 解析AI分析内容
                    parsed_fields = self.parse_analysis_content(result['page_content'])
                    
                    # 更新结果
                    result.update(parsed_fields)
                
                parsed_results.append(result)
                
            except Exception as e:
                self.logger.error(f"解析分析结果失败: {e}")
                # 保留原始结果
                parsed_results.append(result)
        
        return parsed_results
    
    def extract_paper_ids_from_content(self, content: str) -> List[str]:
        """
        从内容中提取论文ID列表
        
        Args:
            content: 内容字符串
            
        Returns:
            论文ID列表
        """
        paper_ids = []
        
        # 查找所有可能的arXiv ID
        arxiv_pattern = r'\b(\d{4}\.\d{4,5})\b'
        matches = re.findall(arxiv_pattern, content)
        
        for match in matches:
            if self._is_valid_arxiv_id(match):
                paper_ids.append(match)
        
        # 去重并保持顺序
        seen = set()
        unique_ids = []
        for paper_id in paper_ids:
            if paper_id not in seen:
                seen.add(paper_id)
                unique_ids.append(paper_id)
        
        return unique_ids
    
    def validate_analysis_result(self, result: Dict[str, Any]) -> bool:
        """
        验证分析结果的完整性
        
        Args:
            result: 分析结果字典
            
        Returns:
            是否有效
        """
        required_fields = ['title', 'translation']
        
        for field in required_fields:
            if not result.get(field, '').strip():
                return False
        
        # 检查论文ID格式
        paper_id = result.get('paper_id', '') or result.get('id', '')
        if paper_id and not self._is_valid_arxiv_id(paper_id):
            return False
        
        return True


# 便捷函数
def parse_analysis_content(content: str) -> Dict[str, str]:
    """
    便捷函数：解析AI分析内容
    
    Args:
        content: AI分析内容
        
    Returns:
        解析后的字段字典
    """
    parser = ContentParser()
    return parser.parse_analysis_content(content)

def parse_cleaned_data(clean_data: List[str]) -> List[Paper]:
    """
    便捷函数：解析清洗后的数据
    
    Args:
        clean_data: 清洗后的数据
        
    Returns:
        论文对象列表
    """
    parser = ContentParser()
    return parser.parse_cleaned_data(clean_data)

def create_parser() -> ContentParser:
    """
    便捷函数：创建解析器实例
    
    Returns:
        ContentParser实例
    """
    return ContentParser()
