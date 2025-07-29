#!/usr/bin/env python3
"""
安装GUI批处理工具的依赖
"""
import subprocess
import sys

def install_package(package):
    """安装Python包"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ {package} 安装成功")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ {package} 安装失败")
        return False

def main():
    print("🔧 安装GUI批处理工具依赖...")
    print("=" * 50)
    
    # 必需的包
    packages = [
        "tkcalendar",  # 日期选择器
    ]
    
    success_count = 0
    for package in packages:
        print(f"📦 安装 {package}...")
        if install_package(package):
            success_count += 1
    
    print("=" * 50)
    if success_count == len(packages):
        print("🎉 所有依赖安装成功！")
        print("现在可以运行: python tools/batch_processor_gui.py")
    else:
        print(f"⚠️  {len(packages) - success_count} 个包安装失败")
        print("GUI工具仍可运行，但日期选择功能可能受限")

if __name__ == "__main__":
    main()
