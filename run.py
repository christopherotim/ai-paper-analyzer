#!/usr/bin/env python3
"""
论文分析系统启动脚本
提供便捷的启动方式
"""
import sys
import os
from pathlib import Path

# 确保src目录在Python路径中
current_dir = Path(__file__).parent
src_dir = current_dir / 'src'
sys.path.insert(0, str(src_dir))

# 导入主程序
from src.main import main

if __name__ == '__main__':
    # 直接调用主程序
    sys.exit(main())
