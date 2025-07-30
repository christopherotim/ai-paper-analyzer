@echo off
chcp 65001 >nul
echo 开始创建HF论文分析系统虚拟环境...
echo.

echo 1. 检查Python版本...
python --version
if %errorlevel% neq 0 (
    echo.
    echo ❌ 错误：未找到Python
    echo.
    echo 💡 解决方案：
    echo    1. 下载并安装Python 3.11.9或更高版本
    echo    2. 下载地址：https://www.python.org/downloads/
    echo    3. 安装时务必勾选 "Add Python to PATH" 选项
    echo    4. 安装完成后重启命令行窗口
    echo.
    pause
    exit /b 1
)

echo.
echo 2. 检查venv模块...
python -m venv --help >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo ❌ 错误：Python的venv模块不可用
    echo.
    echo 💡 说明：
    echo    venv是Python 3.3+的内置模块，无需额外安装
    echo    如果出现此错误，可能是Python安装不完整
    echo.
    echo 💡 解决方案：
    echo    1. 重新安装Python（选择完整安装）
    echo    2. 或尝试修复当前Python安装
    echo.
    pause
    exit /b 1
)

echo ✅ Python环境检查通过

echo.
echo 3. 创建虚拟环境...
python -m venv hf-paper-env
if %errorlevel% neq 0 (
    echo.
    echo ❌ 错误：虚拟环境创建失败
    echo.
    echo 💡 可能原因：
    echo    1. 磁盘空间不足
    echo    2. 权限不足（尝试以管理员身份运行）
    echo    3. 路径包含特殊字符
    echo.
    pause
    exit /b 1
)

echo.
echo 4. 激活虚拟环境...
call hf-paper-env\Scripts\activate.bat

echo.
echo 5. 升级pip...
python -m pip install --upgrade pip

echo.
echo 6. 安装项目依赖...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo.
    echo ❌ 错误：依赖安装失败
    echo.
    echo 💡 可能原因：
    echo    1. 网络连接问题（检查网络或配置代理）
    echo    2. requirements.txt文件不存在或损坏
    echo    3. 某些包的版本不兼容
    echo.
    echo 💡 解决方案：
    echo    1. 检查网络连接
    echo    2. 尝试手动安装：pip install requests tqdm zhipuai volcengine PyYAML
    echo    3. 如果在公司网络，可能需要配置代理
    echo.
    pause
    exit /b 1
)

echo.
echo 7. 验证安装...
echo 检查关键依赖包：

pip show requests >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ requests 已安装
) else (
    echo ❌ requests 安装失败
)

pip show tqdm >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ tqdm 已安装
) else (
    echo ❌ tqdm 安装失败
)

pip show zhipuai >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ zhipuai 已安装
) else (
    echo ❌ zhipuai 安装失败
)

pip show volcengine >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ volcengine 已安装
) else (
    echo ❌ volcengine 安装失败
)

pip show PyYAML >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ PyYAML 已安装
) else (
    echo ❌ PyYAML 安装失败
)

pip show tkcalendar >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ tkcalendar 已安装
) else (
    echo ❌ tkcalendar 安装失败
)

echo.
echo ========================================
echo  虚拟环境安装完成！
echo ========================================
echo.
echo 下次使用时，请：
echo   1. 双击 "启动环境.bat" 激活环境
echo   2. 或手动运行：.\hf-paper-env\Scripts\Activate.ps1
echo.
echo 现在可以运行：
echo   python run.py --help
echo   python run.py status
echo   python run_gui.py
echo.
echo 详细使用说明请查看：
echo   - README.md
echo   - 虚拟环境使用指南.md
echo ========================================
echo.
echo 按任意键退出...
pause >nul
