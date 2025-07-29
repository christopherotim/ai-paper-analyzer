"""
AI客户端封装模块
提供统一的AI模型调用接口
"""
import os
import time
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from .logger import get_logger


class AIClient(ABC):
    """AI客户端抽象基类"""
    
    def __init__(self, api_key: str, model_name: str):
        """
        初始化AI客户端
        
        Args:
            api_key: API密钥
            model_name: 模型名称
        """
        self.api_key = api_key
        self.model_name = model_name
        self.logger = get_logger(f"ai_client_{model_name}")
    
    @abstractmethod
    def chat(self, messages: List[Dict[str, Any]], **kwargs) -> str:
        """
        发送聊天请求
        
        Args:
            messages: 消息列表
            **kwargs: 其他参数
            
        Returns:
            AI回复内容
        """
        pass
    
    def _log_api_call(self, messages: List[Dict], response: str, duration: float):
        """记录API调用"""
        self.logger.log_api_call(
            f"{self.model_name}_chat",
            "success",
            duration
        )
        self.logger.debug(f"请求消息数: {len(messages)}, 响应长度: {len(response)}")


class ZhipuClient(AIClient):
    """智谱AI客户端"""
    
    def __init__(self, api_key: str, model_name: str = "GLM-4.5-Air"):
        """初始化智谱AI客户端"""
        super().__init__(api_key, model_name)
        try:
            from zhipuai import ZhipuAI
            self.client = ZhipuAI(api_key=api_key)
        except ImportError:
            raise ImportError("请安装zhipuai库: pip install zhipuai")
    
    def chat(self, messages: List[Dict[str, Any]], **kwargs) -> str:
        """
        发送聊天请求到智谱AI
        
        Args:
            messages: 消息列表
            **kwargs: 其他参数
            
        Returns:
            AI回复内容
        """
        start_time = time.time()
        
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                stream=False,
                **kwargs
            )
            
            content = response.choices[0].message.content
            duration = time.time() - start_time
            
            self._log_api_call(messages, content, duration)
            return content
            
        except Exception as e:
            duration = time.time() - start_time
            self.logger.error(f"智谱AI调用失败: {e}, 耗时: {duration:.2f}秒")
            raise


class DoubaoClient(AIClient):
    """豆包AI客户端"""
    
    def __init__(self, api_key: str, model_name: str = "doubao-1-5-pro-32k-250115"):
        """初始化豆包AI客户端"""
        super().__init__(api_key, model_name)
        try:
            from volcenginesdkarkruntime import Ark
            self.client = Ark(
                base_url="https://ark.cn-beijing.volces.com/api/v3",
                api_key=api_key,
            )
        except ImportError:
            raise ImportError("请安装volcenginesdkarkruntime库")
    
    def chat(self, messages: List[Dict[str, Any]], **kwargs) -> str:
        """
        发送聊天请求到豆包AI
        
        Args:
            messages: 消息列表
            **kwargs: 其他参数
            
        Returns:
            AI回复内容
        """
        start_time = time.time()
        
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                stream=False,
                **kwargs
            )
            
            content = response.choices[0].message.content
            duration = time.time() - start_time
            
            self._log_api_call(messages, content, duration)
            return content
            
        except Exception as e:
            duration = time.time() - start_time
            self.logger.error(f"豆包AI调用失败: {e}, 耗时: {duration:.2f}秒")
            raise


class AIClientFactory:
    """AI客户端工厂类"""
    
    @staticmethod
    def create_client(model_type: str, api_key: str = None, model_name: str = None) -> AIClient:
        """
        创建AI客户端
        
        Args:
            model_type: 模型类型 ('zhipu' 或 'doubao')
            api_key: API密钥，如果为None则从环境变量获取
            model_name: 模型名称，如果为None则使用默认值
            
        Returns:
            AI客户端实例
        """
        if model_type.lower() == 'zhipu':
            api_key = api_key or os.environ.get("ZHIPUAI_API_KEY")
            if not api_key:
                raise ValueError("请设置环境变量 ZHIPUAI_API_KEY 或提供api_key参数")
            
            model_name = model_name or "GLM-4.5-Air"
            return ZhipuClient(api_key, model_name)
            
        elif model_type.lower() == 'doubao':
            api_key = api_key or os.environ.get("ARK_API_KEY")
            if not api_key:
                raise ValueError("请设置环境变量 ARK_API_KEY 或提供api_key参数")
            
            model_name = model_name or "doubao-1-5-pro-32k-250115"
            return DoubaoClient(api_key, model_name)
            
        else:
            raise ValueError(f"不支持的模型类型: {model_type}")
    
    @staticmethod
    def get_available_models() -> Dict[str, List[str]]:
        """获取可用的模型列表"""
        return {
            "zhipu": ["GLM-4.5-Air", "GLM-4", "GLM-3-Turbo"],
            "doubao": ["doubao-1-5-pro-32k-250115", "doubao-pro-32k"]
        }


class RetryableAIClient:
    """带重试功能的AI客户端包装器"""
    
    def __init__(self, client: AIClient, max_retries: int = 3, retry_delay: float = 2.0):
        """
        初始化重试客户端
        
        Args:
            client: AI客户端实例
            max_retries: 最大重试次数
            retry_delay: 重试延迟（秒）
        """
        self.client = client
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.logger = get_logger("retryable_ai_client")
    
    def chat(self, messages: List[Dict[str, Any]], **kwargs) -> Optional[str]:
        """
        带重试的聊天请求
        
        Args:
            messages: 消息列表
            **kwargs: 其他参数
            
        Returns:
            AI回复内容，失败返回None
        """
        for attempt in range(self.max_retries):
            try:
                return self.client.chat(messages, **kwargs)
                
            except Exception as e:
                self.logger.warning(f"第{attempt + 1}次尝试失败: {e}")
                
                if attempt < self.max_retries - 1:
                    delay = self.retry_delay * (2 ** attempt)  # 指数退避
                    self.logger.info(f"等待{delay}秒后重试...")
                    time.sleep(delay)
                else:
                    self.logger.error(f"所有重试都失败了，放弃请求")
                    return None
        
        return None


# 便捷函数
def create_ai_client(model_type: str, api_key: str = None, model_name: str = None) -> AIClient:
    """便捷函数：创建AI客户端"""
    return AIClientFactory.create_client(model_type, api_key, model_name)

def create_retryable_client(model_type: str, max_retries: int = 3,
                          api_key: str = None, model_name: str = None) -> RetryableAIClient:
    """便捷函数：创建带重试的AI客户端"""
    client = create_ai_client(model_type, api_key, model_name)
    return RetryableAIClient(client, max_retries)


class EnhancedAIClientFactory:
    """
    增强的AI客户端工厂

    基于配置文件创建AI客户端，支持多种AI提供商
    """

    def __init__(self, config_manager=None):
        """
        初始化增强工厂

        Args:
            config_manager: 配置管理器实例
        """
        if config_manager is None:
            from .config import get_config
            config_manager = get_config()

        self.config_manager = config_manager
        self.logger = get_logger('enhanced_ai_factory')

    def create_from_config(self, provider: str = None, model_name: str = None,
                          max_retries: int = 3) -> RetryableAIClient:
        """
        从配置创建AI客户端

        Args:
            provider: AI提供商名称，如果为None则使用默认提供商
            model_name: 模型名称，如果为None则使用默认模型
            max_retries: 最大重试次数

        Returns:
            RetryableAIClient实例
        """
        # 使用默认提供商
        if provider is None:
            provider = self.config_manager.get_default_provider()

        # 检查提供商是否可用
        if not self.config_manager.is_provider_available(provider):
            raise ValueError(f"AI提供商 {provider} 不可用或配置不完整")

        # 获取配置
        ai_config = self.config_manager.get_ai_config(provider)
        model_config = self.config_manager.get_model_config(provider, model_name)

        if not ai_config or not model_config:
            raise ValueError(f"无法获取 {provider} 的配置信息")

        # 获取API密钥
        api_key = self.config_manager.get_api_key(provider)
        if not api_key:
            raise ValueError(f"AI提供商 {provider} 的API密钥未设置")

        # 确定最终使用的模型名称
        final_model_name = model_name or ai_config.get('default_model')

        # 创建客户端
        try:
            client = create_ai_client(provider, api_key, final_model_name)
            retryable_client = RetryableAIClient(
                client,
                max_retries=max_retries,
                retry_delay=ai_config.get('retry_delay', 2.0)
            )

            self.logger.info(f"成功创建AI客户端: {provider}/{final_model_name}")
            return retryable_client

        except Exception as e:
            self.logger.error(f"创建AI客户端失败: {provider}/{final_model_name} - {e}")
            raise

    def get_available_models(self) -> Dict[str, List[str]]:
        """
        获取所有可用的AI模型

        Returns:
            提供商到模型列表的映射
        """
        available_models = {}

        for provider in self.config_manager.get_available_providers():
            if self.config_manager.is_provider_available(provider):
                models = self.config_manager.get_available_models(provider)
                available_models[provider] = models

        return available_models

    def get_recommended_provider(self) -> str:
        """
        获取推荐的AI提供商（优先使用可用的默认提供商）

        Returns:
            推荐的提供商名称
        """
        default_provider = self.config_manager.get_default_provider()

        # 如果默认提供商可用，直接返回
        if self.config_manager.is_provider_available(default_provider):
            return default_provider

        # 否则返回第一个可用的提供商
        for provider in self.config_manager.get_available_providers():
            if self.config_manager.is_provider_available(provider):
                self.logger.warning(f"默认提供商 {default_provider} 不可用，使用 {provider}")
                return provider

        raise RuntimeError("没有可用的AI提供商")


# 全局增强工厂实例
_enhanced_factory = None

def get_enhanced_factory() -> EnhancedAIClientFactory:
    """
    获取全局增强工厂实例

    Returns:
        EnhancedAIClientFactory实例
    """
    global _enhanced_factory

    if _enhanced_factory is None:
        _enhanced_factory = EnhancedAIClientFactory()

    return _enhanced_factory

def create_client_from_config(provider: str = None, model_name: str = None,
                            max_retries: int = 3) -> RetryableAIClient:
    """
    便捷函数：从配置创建AI客户端

    Args:
        provider: AI提供商名称
        model_name: 模型名称
        max_retries: 最大重试次数

    Returns:
        RetryableAIClient实例
    """
    return get_enhanced_factory().create_from_config(provider, model_name, max_retries)
