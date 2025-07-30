#!/bin/bash
# HF论文分析系统 - 虚拟环境自动安装脚本 (macOS/Linux版本)
# 支持macOS和Linux系统的一键环境配置

echo "========================================"
echo " HF论文分析系统 - 环境自动安装"
echo "========================================"
echo ""

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 检测操作系统 - 使用POSIX兼容的方法
OS_TYPE=""
case "$OSTYPE" in
    darwin*)
        OS_TYPE="macOS"
        ;;
    linux-gnu*|linux*)
        OS_TYPE="Linux"
        ;;
    *)
        echo -e "${RED}❌ 不支持的操作系统: $OSTYPE${NC}"
        echo "此脚本仅支持macOS和Linux系统"
        exit 1
        ;;
esac

echo -e "${BLUE}🖥️  检测到操作系统: $OS_TYPE${NC}"
echo ""

# 1. 检查Python版本
echo -e "${BLUE}1. 检查Python版本...${NC}"
if command -v python3 >/dev/null 2>&1; then
    PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2)
    PYTHON_MAJOR=$(echo "$PYTHON_VERSION" | cut -d'.' -f1)
    PYTHON_MINOR=$(echo "$PYTHON_VERSION" | cut -d'.' -f2)
    
    echo -e "${GREEN}✅ Python版本: $PYTHON_VERSION${NC}"
    
    if [ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -ge 8 ]; then
        echo -e "${GREEN}✅ Python版本满足要求 (>=3.8)${NC}"
    else
        echo -e "${RED}❌ Python版本过低，需要3.8或更高版本${NC}"
        echo -e "${YELLOW}💡 请访问 https://www.python.org/downloads/ 下载最新版本${NC}"
        exit 1
    fi
else
    echo -e "${RED}❌ 未找到Python3，请先安装Python${NC}"
    echo -e "${YELLOW}💡 安装建议:${NC}"
    if [ "$OS_TYPE" = "macOS" ]; then
        echo "   - 官网下载: https://www.python.org/downloads/macos/"
        echo "   - 使用Homebrew: brew install python@3.11"
    else
        echo "   - Ubuntu/Debian: sudo apt install python3 python3-venv python3-pip"
        echo "   - CentOS/RHEL: sudo yum install python3 python3-pip"
    fi
    exit 1
fi

# 2. 检查venv模块
echo ""
echo -e "${BLUE}2. 检查venv模块支持...${NC}"
if python3 -m venv --help >/dev/null 2>&1; then
    echo -e "${GREEN}✅ venv模块可用${NC}"
else
    echo -e "${RED}❌ venv模块不可用${NC}"
    if [ "$OS_TYPE" = "Linux" ]; then
        echo -e "${YELLOW}💡 请安装python3-venv包:${NC}"
        echo "   sudo apt install python3-venv  # Ubuntu/Debian"
        echo "   sudo yum install python3-venv  # CentOS/RHEL"
    fi
    exit 1
fi

# 3. 创建虚拟环境
echo ""
echo -e "${BLUE}3. 创建虚拟环境...${NC}"
if [ -d "hf-paper-env" ]; then
    echo -e "${YELLOW}⚠️  虚拟环境已存在，将重新创建${NC}"
    rm -rf hf-paper-env
fi

if python3 -m venv hf-paper-env; then
    echo -e "${GREEN}✅ 虚拟环境创建成功${NC}"
else
    echo -e "${RED}❌ 虚拟环境创建失败${NC}"
    exit 1
fi

# 4. 激活虚拟环境
echo ""
echo -e "${BLUE}4. 激活虚拟环境...${NC}"
. hf-paper-env/bin/activate

if [ -n "$VIRTUAL_ENV" ]; then
    echo -e "${GREEN}✅ 虚拟环境激活成功${NC}"
    echo -e "${GREEN}   当前环境: $VIRTUAL_ENV${NC}"
else
    echo -e "${RED}❌ 虚拟环境激活失败${NC}"
    exit 1
fi

# 5. 升级pip
echo ""
echo -e "${BLUE}5. 升级pip到最新版本...${NC}"
if python -m pip install --upgrade pip; then
    PIP_VERSION=$(pip --version | cut -d' ' -f2)
    echo -e "${GREEN}✅ pip升级成功，版本: $PIP_VERSION${NC}"
else
    echo -e "${YELLOW}⚠️  pip升级失败，但不影响后续安装${NC}"
fi

# 6. 安装项目依赖
echo ""
echo -e "${BLUE}6. 安装项目依赖包...${NC}"
if [ ! -f "requirements.txt" ]; then
    echo -e "${RED}❌ 未找到requirements.txt文件${NC}"
    echo "请确保在项目根目录下运行此脚本"
    exit 1
fi

echo -e "${YELLOW}📦 正在安装依赖包，请稍候...${NC}"
if pip install -r requirements.txt; then
    echo -e "${GREEN}✅ 依赖包安装成功${NC}"
else
    echo -e "${RED}❌ 依赖包安装失败${NC}"
    echo "请检查网络连接或requirements.txt文件"
    exit 1
fi

# 7. 验证关键包安装
echo ""
echo -e "${BLUE}7. 验证关键包安装状态...${NC}"

# 定义要检查的包
packages=("requests" "tqdm" "zhipuai" "volcengine" "PyYAML" "tkcalendar" "beautifulsoup4" "markdown" "pandas")

for package in "${packages[@]}"; do
    if pip show "$package" >/dev/null 2>&1; then
        version=$(pip show "$package" | grep Version | cut -d' ' -f2)
        echo -e "${GREEN}✅ $package ($version)${NC}"
    else
        echo -e "${RED}❌ $package (未安装)${NC}"
    fi
done

# 8. 检查启动脚本
echo ""
echo -e "${BLUE}8. 检查启动脚本...${NC}"

if [ -f "启动环境.sh" ]; then
    chmod +x 启动环境.sh
    echo -e "${GREEN}✅ 启动脚本已存在并设置执行权限${NC}"
else
    echo -e "${YELLOW}⚠️  启动脚本不存在，请手动创建或重新下载项目${NC}"
fi

# 安装完成
echo ""
echo "========================================"
echo -e "${GREEN}🎉 安装完成！${NC}"
echo "========================================"
echo ""
echo -e "${YELLOW}📋 下次使用时，请：${NC}"
echo -e "${BLUE}  1. 运行启动脚本: ./启动环境.sh${NC}"
echo -e "${BLUE}  2. 或手动激活: source hf-paper-env/bin/activate${NC}"
echo ""
echo -e "${YELLOW}🚀 现在可以运行：${NC}"
echo -e "${BLUE}  python run.py status     # 查看系统状态${NC}"
echo -e "${BLUE}  python 检查环境.py        # 环境诊断${NC}"
echo -e "${BLUE}  python run_gui.py        # 启动GUI界面${NC}"
echo ""
echo -e "${YELLOW}📖 详细使用说明请查看：${NC}"
echo "  - README.md"
echo "  - 虚拟环境使用指南.md"
echo ""
echo "========================================"
echo ""
echo "按回车键退出..."
read dummy
