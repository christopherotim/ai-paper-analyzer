#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python环境检查脚本
用于诊断Python环境和依赖包状态
"""

import sys
import os
import subprocess
from pathlib import Path

def print_header(title):
    """打印标题"""
    print(f"\n{'='*50}")
    print(f" {title}")
    print(f"{'='*50}")

def print_status(item, status, details=""):
    """打印状态信息"""
    status_icon = "✅" if status else "❌"
    print(f"{status_icon} {item}")
    if details:
        print(f"   {details}")

def check_python_version():
    """检查Python版本"""
    print_header("Python环境检查")
    
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"
    print_status("Python版本", True, f"Python {version_str}")
    
    # 检查版本是否满足要求
    if version >= (3, 11):
        print_status("版本要求", True, "满足项目要求 (>=3.11)")
    else:
        print_status("版本要求", False, f"需要Python 3.11+，当前版本: {version_str}")
    
    # 检查Python路径
    print_status("Python路径", True, sys.executable)

def check_venv_support():
    """检查venv模块支持"""
    print_header("虚拟环境支持检查")
    
    try:
        import venv
        print_status("venv模块", True, "Python内置venv模块可用")
        
        # 检查venv命令
        result = subprocess.run([sys.executable, "-m", "venv", "--help"], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print_status("venv命令", True, "可以创建虚拟环境")
        else:
            print_status("venv命令", False, "venv命令执行失败")
            
    except ImportError:
        print_status("venv模块", False, "venv模块不可用")
    except subprocess.TimeoutExpired:
        print_status("venv命令", False, "venv命令执行超时")
    except Exception as e:
        print_status("venv命令", False, f"检查失败: {e}")

def check_virtual_env():
    """检查虚拟环境状态"""
    print_header("虚拟环境状态")
    
    # 检查是否在虚拟环境中
    in_venv = hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    
    if in_venv:
        print_status("虚拟环境", True, f"当前在虚拟环境中: {sys.prefix}")
    else:
        print_status("虚拟环境", False, "当前在系统Python环境中")
    
    # 检查项目虚拟环境是否存在
    venv_path = Path("hf-paper-env")
    if venv_path.exists():
        print_status("项目虚拟环境", True, f"hf-paper-env 目录存在")
        
        # 检查虚拟环境结构
        scripts_path = venv_path / "Scripts" if os.name == 'nt' else venv_path / "bin"
        if scripts_path.exists():
            print_status("虚拟环境结构", True, "虚拟环境结构完整")
        else:
            print_status("虚拟环境结构", False, "虚拟环境结构不完整")
    else:
        print_status("项目虚拟环境", False, "hf-paper-env 目录不存在")

def check_dependencies():
    """检查依赖包"""
    print_header("依赖包检查")
    
    # 包名映射：显示名称 -> 实际导入名称
    required_packages = {
        "requests": "requests",
        "tqdm": "tqdm", 
        "zhipuai": "zhipuai",
        "volcengine": "volcengine",
        "PyYAML": "yaml",  # PyYAML包的导入名是yaml
        "tkcalendar": "tkcalendar",  # GUI日历控件
        "beautifulsoup4": "bs4",  # beautifulsoup4包的导入名是bs4
        "markdown": "markdown",
        "pandas": "pandas"
    }
    
    for display_name, import_name in required_packages.items():
        try:
            __import__(import_name)
            print_status(display_name, True, "已安装")
        except ImportError:
            print_status(display_name, False, "未安装")

def check_project_files():
    """检查项目文件"""
    print_header("项目文件检查")
    
    required_files = [
        "requirements.txt",
        "run.py",
        "安装环境.bat",
        "启动环境.bat",
        "虚拟环境使用指南.md"
    ]
    
    for file_name in required_files:
        file_path = Path(file_name)
        if file_path.exists():
            print_status(file_name, True, f"文件存在 ({file_path.stat().st_size} 字节)")
        else:
            print_status(file_name, False, "文件不存在")

def check_config_files():
    """检查配置文件"""
    print_header("配置文件检查")
    
    config_dir = Path("config")
    if config_dir.exists():
        print_status("config目录", True, "配置目录存在")
        
        config_files = ["models.yaml", "logging.yaml"]
        for config_file in config_files:
            config_path = config_dir / config_file
            if config_path.exists():
                print_status(config_file, True, "配置文件存在")
            else:
                print_status(config_file, False, "配置文件不存在")
    else:
        print_status("config目录", False, "配置目录不存在")

def main():
    """主函数"""
    print("🔍 HF论文分析系统 - 环境诊断工具")
    print("=" * 50)
    
    try:
        check_python_version()
        check_venv_support()
        check_virtual_env()
        check_dependencies()
        check_project_files()
        check_config_files()
        
        print_header("诊断完成")
        print("💡 如果发现问题，请参考以下解决方案：")
        print("   1. Python版本问题：重新安装Python 3.11+")
        print("   2. 虚拟环境问题：运行 安装环境.bat")
        print("   3. 依赖包问题：激活虚拟环境后运行 pip install -r requirements.txt")
        print("   4. 配置文件问题：检查config目录和相关配置文件")
        print("\n📖 详细说明请查看：虚拟环境使用指南.md")
        
    except KeyboardInterrupt:
        print("\n\n⚠️ 用户中断了检查过程")
    except Exception as e:
        print(f"\n\n❌ 检查过程中出现错误: {e}")
        print("请将此错误信息反馈给开发者")

if __name__ == "__main__":
    main()