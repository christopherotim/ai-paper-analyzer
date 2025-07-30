@echo off
chcp 65001 >nul

echo.
echo ========================================
echo  正在激活HF论文分析系统虚拟环境...
echo ========================================

REM 激活虚拟环境
call hf-paper-env\Scripts\activate.bat

echo.
echo ========================================
echo  HF论文分析系统虚拟环境已激活
echo ========================================
echo.
echo 可用的包已安装完成
echo.
echo 现在可以运行程序了：
echo   python run.py status
echo   python 检查环境.py
echo   python run_gui.py
echo ========================================
echo.

REM 保持终端打开并显示提示符
cmd /k