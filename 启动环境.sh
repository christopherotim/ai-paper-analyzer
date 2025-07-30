#!/bin/bash
# HF论文分析系统 - 虚拟环境启动脚本 (macOS/Linux版本)

# 检查是否支持颜色输出
if [ -t 1 ] && command -v tput >/dev/null 2>&1 && [ "$(tput colors)" -ge 8 ]; then
    # 颜色定义
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    BLUE='\033[0;34m'
    NC='\033[0m' # No Color
    USE_COLOR=true
else
    # 不支持颜色时使用空字符串
    RED=''
    GREEN=''
    YELLOW=''
    BLUE=''
    NC=''
    USE_COLOR=false
fi

# 安全的echo函数
safe_echo() {
    if [ "$USE_COLOR" = true ]; then
        echo -e "$1"
    else
        # 移除颜色代码后输出
        echo "$1" | sed 's/\\033\[[0-9;]*m//g'
    fi
}

echo ""
echo "========================================"
echo " 正在激活HF论文分析系统虚拟环境..."
echo "========================================"

# 检查虚拟环境是否存在
if [ ! -d "hf-paper-env" ]; then
    safe_echo "${RED}❌ 虚拟环境不存在${NC}"
    safe_echo "${YELLOW}💡 请先运行安装脚本：${NC}"
    echo "   ./安装环境.sh"
    echo ""
    echo "按回车键退出..."
    read dummy
    exit 1
fi

# 检查激活脚本是否存在
if [ ! -f "hf-paper-env/bin/activate" ]; then
    safe_echo "${RED}❌ 虚拟环境激活脚本不存在${NC}"
    safe_echo "${YELLOW}💡 虚拟环境可能已损坏，请重新安装：${NC}"
    echo "   rm -rf hf-paper-env"
    echo "   ./安装环境.sh"
    echo ""
    echo "按回车键退出..."
    read dummy
    exit 1
fi

# 激活虚拟环境
. hf-paper-env/bin/activate

# 检查是否激活成功 - 使用POSIX兼容的语法
if [ -n "$VIRTUAL_ENV" ]; then
    echo ""
    echo "========================================"
    safe_echo "${GREEN} HF论文分析系统虚拟环境已激活${NC}"
    echo "========================================"
    echo ""
    safe_echo "${GREEN}可用的包已安装完成${NC}"
    echo ""
    safe_echo "${BLUE}现在可以运行程序了：${NC}"
    safe_echo "${YELLOW}  python run.py status     ${NC}# 查看系统状态"
    safe_echo "${YELLOW}  python 检查环境.py        ${NC}# 环境诊断"
    safe_echo "${YELLOW}  python run_gui.py        ${NC}# 启动GUI界面"
    echo "========================================"
    echo ""
    
    # 启动新的shell会话，保持环境激活
    # 检测当前shell类型 - 使用更安全的方法
    if [ -n "${ZSH_VERSION:-}" ]; then
        # 使用zsh
        exec zsh
    elif [ -n "${BASH_VERSION:-}" ]; then
        # 使用bash
        exec bash
    else
        # 默认使用当前shell
        exec "${SHELL:-/bin/sh}"
    fi
else
    safe_echo "${RED}❌ 虚拟环境激活失败${NC}"
    safe_echo "${YELLOW}💡 可能的解决方案：${NC}"
    echo "   1. 检查Python是否正确安装"
    echo "   2. 重新创建虚拟环境：./安装环境.sh"
    echo "   3. 手动激活：source hf-paper-env/bin/activate"
    echo ""
    echo "按回车键退出..."
    read dummy
    exit 1
fi
