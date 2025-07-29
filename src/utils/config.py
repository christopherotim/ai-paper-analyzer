"""
配置管理系统
提供统一的配置管理功能，支持多种AI模型配置
"""
import os
import yaml
import logging.config
from pathlib import Path
from typing import Dict, Any, Optional, List
from .logger import get_logger


class ConfigManager:
    """
    配置管理器
    
    负责加载和管理所有配置文件，提供统一的配置访问接口
    """
    
    def __init__(self, config_dir: str = "config"):
        """
        初始化配置管理器
        
        Args:
            config_dir: 配置文件目录
        """
        self.config_dir = Path(config_dir)
        self.logger = get_logger('config_manager')
        
        # 配置缓存
        self._models_config = None
        self._logging_config = None
        
        # 加载配置
        self._load_configs()
    
    def _load_configs(self):
        """加载所有配置文件"""
        try:
            # 加载模型配置
            self._load_models_config()
            
            # 加载日志配置
            self._load_logging_config()
            
            self.logger.info("配置文件加载完成")
            
        except Exception as e:
            self.logger.error(f"配置文件加载失败: {e}")
            raise
    
    def _load_models_config(self):
        """加载AI模型配置"""
        models_file = self.config_dir / "models.yaml"
        
        if not models_file.exists():
            raise FileNotFoundError(f"模型配置文件不存在: {models_file}")
        
        try:
            with open(models_file, 'r', encoding='utf-8') as f:
                self._models_config = yaml.safe_load(f)
            
            self.logger.info(f"模型配置加载成功: {models_file}")
            
        except Exception as e:
            self.logger.error(f"模型配置加载失败: {e}")
            raise
    
    def _load_logging_config(self):
        """加载日志配置"""
        logging_file = self.config_dir / "logging.yaml"
        
        if not logging_file.exists():
            self.logger.warning(f"日志配置文件不存在: {logging_file}")
            return
        
        try:
            with open(logging_file, 'r', encoding='utf-8') as f:
                self._logging_config = yaml.safe_load(f)
            
            # 确保日志目录存在
            self._ensure_log_directories()
            
            # 应用日志配置
            logging.config.dictConfig(self._logging_config)
            
            self.logger.info(f"日志配置加载成功: {logging_file}")
            
        except Exception as e:
            self.logger.error(f"日志配置加载失败: {e}")
    
    def _ensure_log_directories(self):
        """确保日志目录存在"""
        log_dirs = ["logs/daily", "logs/error", "logs/debug"]
        
        for log_dir in log_dirs:
            Path(log_dir).mkdir(parents=True, exist_ok=True)
    
    def get_ai_config(self, provider: str) -> Optional[Dict[str, Any]]:
        """
        获取AI提供商配置
        
        Args:
            provider: AI提供商名称 (如: zhipu, openai, doubao等)
            
        Returns:
            AI提供商配置字典，不存在返回None
        """
        if not self._models_config:
            return None
        
        return self._models_config.get('ai_models', {}).get(provider)
    
    def get_model_config(self, provider: str, model_name: str = None) -> Optional[Dict[str, Any]]:
        """
        获取特定模型配置
        
        Args:
            provider: AI提供商名称
            model_name: 模型名称，如果为None则返回默认模型配置
            
        Returns:
            模型配置字典，不存在返回None
        """
        ai_config = self.get_ai_config(provider)
        if not ai_config:
            return None
        
        models = ai_config.get('models', {})
        
        if model_name is None:
            # 返回默认模型配置
            default_model = ai_config.get('default_model')
            if default_model and default_model in models:
                return models[default_model]
            else:
                # 返回第一个可用模型
                return next(iter(models.values())) if models else None
        else:
            return models.get(model_name)
    
    def get_default_provider(self) -> str:
        """
        获取默认AI提供商
        
        Returns:
            默认AI提供商名称
        """
        if not self._models_config:
            return 'zhipu'  # 默认使用智谱
        
        return self._models_config.get('default_model', 'zhipu')
    
    def get_available_providers(self) -> List[str]:
        """
        获取所有可用的AI提供商列表
        
        Returns:
            AI提供商名称列表
        """
        if not self._models_config:
            return []
        
        return list(self._models_config.get('ai_models', {}).keys())
    
    def get_available_models(self, provider: str) -> List[str]:
        """
        获取指定提供商的所有可用模型
        
        Args:
            provider: AI提供商名称
            
        Returns:
            模型名称列表
        """
        ai_config = self.get_ai_config(provider)
        if not ai_config:
            return []
        
        return list(ai_config.get('models', {}).keys())
    
    def get_app_config(self, key: str = None) -> Any:
        """
        获取应用配置
        
        Args:
            key: 配置键名，如果为None则返回所有应用配置
            
        Returns:
            配置值或配置字典
        """
        if not self._models_config:
            return None
        
        app_config = self._models_config.get('app_config', {})
        
        if key is None:
            return app_config
        else:
            return app_config.get(key)
    
    def get_proxy_config(self) -> Dict[str, Any]:
        """
        获取代理配置
        
        Returns:
            代理配置字典
        """
        if not self._models_config:
            return {}
        
        return self._models_config.get('proxy_config', {})
    
    def validate_provider_config(self, provider: str) -> bool:
        """
        验证AI提供商配置是否完整
        
        Args:
            provider: AI提供商名称
            
        Returns:
            是否配置完整
        """
        ai_config = self.get_ai_config(provider)
        if not ai_config:
            return False
        
        # 检查必需字段
        required_fields = ['name', 'api_key_env', 'models']
        for field in required_fields:
            if field not in ai_config:
                self.logger.warning(f"AI提供商 {provider} 缺少必需字段: {field}")
                return False
        
        # 检查是否有可用模型
        models = ai_config.get('models', {})
        if not models:
            self.logger.warning(f"AI提供商 {provider} 没有配置任何模型")
            return False
        
        return True
    
    def get_api_key(self, provider: str) -> Optional[str]:
        """
        获取AI提供商的API密钥

        Args:
            provider: AI提供商名称

        Returns:
            API密钥，不存在返回None
        """
        ai_config = self.get_ai_config(provider)
        if not ai_config:
            return None

        api_key_env = ai_config.get('api_key_env')
        if not api_key_env:
            return None

        # 跨平台环境变量读取
        return self._get_environment_variable(api_key_env)

    def _get_environment_variable(self, var_name: str) -> Optional[str]:
        """
        跨平台获取环境变量

        Args:
            var_name: 环境变量名称

        Returns:
            环境变量值，不存在返回None
        """
        import platform

        # 首先尝试从当前进程环境变量获取
        value = os.environ.get(var_name)
        if value:
            return value

        # 如果当前进程环境变量没有，尝试从系统环境变量获取
        try:
            if platform.system() == "Windows":
                # Windows系统：使用PowerShell获取系统环境变量
                try:
                    import subprocess

                    # 尝试获取用户级环境变量
                    result = subprocess.run([
                        'powershell', '-Command',
                        f'[System.Environment]::GetEnvironmentVariable("{var_name}", "User")'
                    ], capture_output=True, text=True, timeout=10)

                    if result.returncode == 0 and result.stdout.strip():
                        value = result.stdout.strip()
                        # 同时设置到当前进程环境变量中，避免重复调用
                        os.environ[var_name] = value
                        return value

                    # 如果用户级没有，尝试系统级环境变量
                    result = subprocess.run([
                        'powershell', '-Command',
                        f'[System.Environment]::GetEnvironmentVariable("{var_name}", "Machine")'
                    ], capture_output=True, text=True, timeout=10)

                    if result.returncode == 0 and result.stdout.strip():
                        value = result.stdout.strip()
                        # 同时设置到当前进程环境变量中，避免重复调用
                        os.environ[var_name] = value
                        return value

                except (subprocess.TimeoutExpired, subprocess.SubprocessError, FileNotFoundError) as e:
                    self.logger.warning(f"PowerShell调用失败: {e}")

                return None
            else:
                # Unix/Linux/macOS系统：使用标准方法
                return os.environ.get(var_name)

        except Exception as e:
            self.logger.warning(f"获取环境变量 {var_name} 失败: {e}")
            return None
    
    def is_provider_available(self, provider: str) -> bool:
        """
        检查AI提供商是否可用（配置完整且有API密钥）
        
        Args:
            provider: AI提供商名称
            
        Returns:
            是否可用
        """
        # 检查配置是否完整
        if not self.validate_provider_config(provider):
            return False
        
        # 检查API密钥是否存在
        api_key = self.get_api_key(provider)
        if not api_key:
            self.logger.warning(f"AI提供商 {provider} 的API密钥未设置")
            return False
        
        return True
    
    def reload_config(self):
        """重新加载配置文件"""
        self.logger.info("重新加载配置文件")
        self._models_config = None
        self._logging_config = None
        self._load_configs()
    
    def get_config_summary(self) -> Dict[str, Any]:
        """
        获取配置摘要信息
        
        Returns:
            配置摘要字典
        """
        summary = {
            "default_provider": self.get_default_provider(),
            "available_providers": self.get_available_providers(),
            "available_providers_count": len(self.get_available_providers()),
            "usable_providers": [p for p in self.get_available_providers() if self.is_provider_available(p)],
            "app_config": self.get_app_config(),
            "proxy_enabled": bool(self.get_proxy_config().get('http_proxy') or self.get_proxy_config().get('https_proxy'))
        }
        
        # 添加每个提供商的模型数量
        provider_models = {}
        for provider in self.get_available_providers():
            provider_models[provider] = len(self.get_available_models(provider))
        
        summary["provider_models"] = provider_models
        
        return summary


# 全局配置管理器实例
_config_manager = None

def get_config() -> ConfigManager:
    """
    获取全局配置管理器实例
    
    Returns:
        ConfigManager实例
    """
    global _config_manager
    
    if _config_manager is None:
        _config_manager = ConfigManager()
    
    return _config_manager

def reload_config():
    """重新加载全局配置"""
    global _config_manager
    
    if _config_manager is not None:
        _config_manager.reload_config()
    else:
        _config_manager = ConfigManager()

# 便捷函数
def get_ai_config(provider: str) -> Optional[Dict[str, Any]]:
    """便捷函数：获取AI配置"""
    return get_config().get_ai_config(provider)

def get_model_config(provider: str, model_name: str = None) -> Optional[Dict[str, Any]]:
    """便捷函数：获取模型配置"""
    return get_config().get_model_config(provider, model_name)

def get_default_provider() -> str:
    """便捷函数：获取默认AI提供商"""
    return get_config().get_default_provider()

def is_provider_available(provider: str) -> bool:
    """便捷函数：检查AI提供商是否可用"""
    return get_config().is_provider_available(provider)
