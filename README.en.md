# 🤖 AI Paper Intelligence Analysis System

<div align="center">

[English](./README.en.md) | [简体中文](./README.md)

</div>

<div align="center">

[ARCHITECTURE](./docs/ARCHITECTURE.v2.en.md) | [技术架构](./docs/ARCHITECTURE.v2.md)

</div>

> **One-click fetch, intelligent analysis, automatic classification** - Let AI help you read papers and escape from information overload!

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![AI Models](https://img.shields.io/badge/AI-Zhipu|Doubao|OpenAI|Qwen-orange.svg)](#)

Hundreds of AI papers are published daily - tired of manual screening? Let AI help you! This system automatically fetches the latest papers from HuggingFace, uses multiple AI models for intelligent analysis and classification, and generates readable analysis reports.

<!-- 📸 Screenshot needed: Main interface -->

![System Main Interface](screenshots/main-interface.png)

## ⚡ Get Started in 30 Seconds

### 🚀 v2.0 Major Updates

**🎯 Brand new optimized AI analysis pipeline with 10x speed improvement!**

- ✅ **Smart Data Cleaning** - Default rule-based cleaning, no AI dependency, completed in seconds
- ✅ **AI Analysis Acceleration** - Optimized prompt strategy, processing time reduced from 60-90s/paper to 5-10s/paper
- ✅ **Bilingual Separation** - Complete bilingual data structure supporting title_en/title_zh, summary_en/summary_zh
- ✅ **Enhanced MD Splitting** - Generate rich MD files with GitHub repos, project pages, complete abstracts
- ✅ **Smart Classification Optimization** - Only add "Technical Features" and "Application Scenarios" to existing MD, avoid duplicate work

**📊 Performance Comparison**:

- Data Cleaning: AI dependency → Rule-based cleaning (completed in seconds)
- Paper Analysis: 60-90s/paper → 5-10s/paper
- Data Completeness: Basic fields → Including GitHub, project pages, bilingual abstracts
- AI Efficiency: Duplicate generation → Focus on translation and core analysis

### 🔥 v2.1 Rage Mode Updates

**⚡ Brand new Rage Mode with 5x speed improvement!**

- ✅ **🔥 Rage Mode** - 5-concurrent AI processing, Basic analysis from 3 minutes to 34 seconds
- ✅ **📊 Real-time Progress Bar** - Fixed position display with progress and timing, more intuitive experience
- ✅ **🧠 Smart Caching** - Auto-skip processed papers, avoid duplicate work
- ✅ **⚡ Lightning Classification** - Advanced classification from 2 minutes to 45 seconds

**🎯 Rage Mode Usage**:

```bash
# Basic Rage Mode - 5-concurrent AI analysis
python run.py basic 2025-07-29 --rageMode

# Advanced Rage Mode - 5-concurrent smart classification
python run.py advanced 2025-07-29 --rageMode
```

**📊 Rage Mode Real-time Progress**:

```
🔥 狂暴模式进度: [███████████████████████████░░░] 10/11 (90.9%) | 成功:10 失败:0 | 耗时:00:34
```

### 🛠️ One-Click Environment Setup (Zero Barrier)

**Say goodbye to complex environment configuration, one-click to start your AI paper analysis journey!**

```bash
# Windows Users
Double-click 安装环境.bat  # Windows one-click install all dependencies
# Or command line: .\安装环境.bat

# macOS/Linux Users
chmod +x 安装环境.sh && ./安装环境.sh  # One-click install all dependencies
```

**🎯 One-click script automatically completes**:

- ✅ **Python Environment Detection** - Auto-verify Python version and venv support
- ✅ **Virtual Environment Creation** - Isolate project dependencies, avoid conflicts
- ✅ **Dependency Installation** - Auto-install all required AI model SDKs
- ✅ **Environment Verification** - Intelligently detect installation status, ensure availability
- ✅ **Usage Guidance** - Provide detailed next-step instructions

**🚀 Ready to use after installation**:

```bash
# Windows Users
Double-click 启动环境.bat    # Activate environment and start using

# macOS/Linux Users
chmod +x 启动环境.sh && ./启动环境.sh  # Activate environment and start using

# Or directly launch GUI
python run_gui.py
```

<!-- 📸 Screenshot needed: One-click installation process -->

![One-click Installation Process](screenshots/one-click-install1.png)
![One-click Installation Process](screenshots/one-click-install2.png)
![One-click Installation Process](screenshots/one-click-install3.png)

### 🎨 GUI Version (Recommended for Beginners)

```bash
python run_gui.py
```

**Zero barrier to entry**: Click "Start Analysis" → Select Date → Wait for Completion ✨

<!-- 📸 Screenshot needed: GUI workflow -->

![GUI Workflow](screenshots/gui-workflow-gui.gif)
![CLI Workflow](screenshots/gui-workflow-cli.gif)

### 💻 Command Line Version (Recommended for Professionals)

```bash
python run.py basic 2025-07-29
```

**One command does it all**: Auto-download, analyze, generate reports

<!-- 📸 Screenshot needed: CLI execution process -->

![CLI Execution](screenshots/cli-execution1.png)
![CLI Execution](screenshots/cli-execution2.png)

## 🎯 Core Features

| Feature                             | Description                                                           | Value                                                 |
| ----------------------------------- | --------------------------------------------------------------------- | ----------------------------------------------------- |
| 🛠️ **Smart Environment Management** | One-click install, intelligent diagnosis, auto-fix environment issues | Zero barrier entry, goodbye to configuration troubles |
| 📡 **Auto Fetch**                   | Get latest paper data from HuggingFace                                | No manual search, ensure nothing is missed            |
| 🤖 **AI Analysis**                  | Support Zhipu AI, Doubao, OpenAI, Qwen, etc.                          | Multi-model cross-validation, improve accuracy        |
| 📊 **Smart Classification**         | Automatic tagging and topic categorization                            | Quickly locate research areas of interest             |
| 📈 **Visual Reports**               | Generate structured analysis reports                                  | Clear research trends and hotspots at a glance        |
| ⚡ **Batch Processing**             | Support multi-date batch analysis                                     | Efficiently process large amounts of data             |
| 🔄 **Incremental Updates**          | Intelligently detect processed content                                | Avoid duplicate work, save time                       |
| 🔥 **Rage Mode**                    | 5-concurrent processing, real-time progress bar, smart caching        | Lightning speed, 3-5x performance boost               |

## 🚀 Use Cases

### 👨‍🔬 Researchers

- **Quick field updates**: Daily auto-fetch relevant paper abstracts
- **Discover research hotspots**: AI automatically identifies trending research directions
- **Track competitors**: Monitor latest achievements from specific institutions or authors

### 👨‍💼 Product Managers

- **Technology trend analysis**: Understand AI technology development directions
- **Competitive tech research**: Analyze competitors' technology layouts
- **Product planning reference**: Make product roadmaps based on latest research

### 👨‍💻 Developers

- **Technology selection reference**: Learn about latest algorithms and tools
- **Learning resource discovery**: Find papers worth deep research
- **Inspiration source**: Get project ideas from latest research

### 👨‍🎓 Students and Scholars

- **Literature research**: Quickly filter relevant research literature
- **Study planning**: Adjust learning focus based on hotspots
- **Paper writing**: Understand latest research status and development trends

## 🛠️ Installation & Configuration

### 1. Get Project

```bash
# Clone project
git clone https://github.com/ZsTs119/ai-paper-analyzer.git
cd ai-paper-analyzer
```

### 2. Smart Environment Configuration

**🎯 Method 1: One-Click Auto Install (Highly Recommended)**

```bash
# Windows Users
Double-click 安装环境.bat        # Double-click to run
# Or command line: .\安装环境.bat

# macOS/Linux Users
chmod +x 安装环境.sh     # Add execute permission
./安装环境.sh            # Run installation script
```

**✨ Auto Install Script Features**:

- 🔍 **Smart Detection** - Auto-check Python version and environment support
- 🏗️ **Virtual Environment** - Auto-create isolated Python virtual environment
- 📦 **Dependency Management** - Auto-install all required AI model SDKs and toolkits
- ✅ **Installation Verification** - Intelligently verify installation status of each dependency
- 📖 **Usage Guidance** - Provide detailed usage instructions after installation

**🛠️ Method 2: Manual Installation (Advanced Users)**

```bash
# Create virtual environment
python -m venv hf-paper-env

# Activate virtual environment
# Windows PowerShell
.\hf-paper-env\Scripts\Activate.ps1
# Windows CMD
hf-paper-env\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt
```

**🔧 Smart Environment Diagnostic Tool**

After installation, you can use the smart diagnostic tool to check environment status anytime:

```bash
python 检查环境.py  # Comprehensive detection of Python environment, dependencies, config files, etc.
```

<!-- 📸 Screenshot needed: Environment diagnostic tool interface -->

![Environment Diagnostic Tool](screenshots/environment-check1.png)
![Environment Diagnostic Tool](screenshots/environment-check2.png)

### 2. API Key Configuration

Support multiple AI services, choose one:

| AI Service | Environment Variable | Get Address                                                                                                    |
| ---------- | -------------------- | -------------------------------------------------------------------------------------------------------------- |
| Zhipu AI   | `ZHIPUAI_API_KEY`    | [Zhipu AI Open Platform](https://www.bigmodel.cn/invite?icode=hk0Lc1L7oGy17bOhwrIMDGczbXFgPRGIalpycrEwJ28%3D/) |
| Doubao AI  | `ARK_API_KEY`        | [Volcano Engine](https://console.volcengine.com/)                                                              |
| OpenAI     | `OPENAI_API_KEY`     | [OpenAI Platform](https://platform.openai.com/)                                                                |
| Qwen       | `DASHSCOPE_API_KEY`  | [Alibaba Cloud DashScope](https://dashscope.aliyun.com/)                                                       |

**Method 1: GUI Configuration (Recommended)**

```bash
python run_gui.py
# Click "Configure API Key" button, enter key and test connection
```

<!-- 📸 Screenshot needed: API key configuration interface -->

![API Key Configuration](screenshots/api-config.png)

**Method 2: Environment Variables**

```bash
# Windows
set ZHIPUAI_API_KEY=your_api_key_here

# Linux/Mac
export ZHIPUAI_API_KEY=your_api_key_here
```

### 3. Verify Installation

```bash
python run.py status  # Check system status
```

## 📖 User Guide

### 🎨 GUI Interface (Zero Barrier)

1. **Launch Interface**

   ```bash
   python run_gui.py
   ```

2. **Basic Operations**

   - Select AI model (Zhipu AI, Doubao, etc.)
   - Click "Configure API Key" to set key
   - Select analysis date
   - Click "Start Analysis"

3. **Advanced Features**
   - Real-time analysis progress
   - Silent mode operation
   - Batch process multiple dates

<!-- 📸 Screenshot needed: GUI detailed operation steps -->

![GUI Operation Steps](screenshots/gui-steps1.png)
![GUI Operation Steps](screenshots/gui-steps2.png)
![GUI Operation Steps](screenshots/gui-steps3.png)

### 💻 Command Line Scripts (Professional & Efficient)

#### Basic Analysis

```bash
# Analyze today's papers
python run.py basic

# Analyze specific date
python run.py basic 2025-07-29

# Silent mode
python run.py basic 2025-07-29 --silent
```

#### 🔥 Rage Mode (Lightning Speed Processing)

```bash
# Basic Rage Mode - 5-concurrent AI analysis
python run.py basic 2025-07-29 --rageMode

# Advanced Rage Mode - 5-concurrent smart classification
python run.py advanced 2025-07-29 --rageMode

# Rage Mode + Silent operation
python run.py basic 2025-07-29 --rageMode --silent
```

**⚡ Rage Mode Features**:

- 🚀 **Lightning Processing** - 5x performance boost, from minutes to seconds
- 📊 **Real-time Feedback** - Dynamic progress bar showing processing status and timing
- 🧠 **Smart Optimization** - Auto-skip processed content, save time
- ⚠️ **Requirements** - Stable network and sufficient API balance needed

#### Advanced Analysis

```bash
# Deep analysis of basic analysis results
python run.py advanced 2025-07-29

# Auto mode (recommended)
python run.py advanced --auto
```

#### Batch Processing

```bash
# Batch analyze multiple dates
python tools/batch_processor.py daily --start 2025-07-25 --end 2025-07-29

# Complete pipeline processing
python tools/batch_processor.py pipeline --start 2025-07-25 --end 2025-07-27
```

#### System Status

```bash
# View configuration and running status
python run.py status
```

<!-- 📸 Screenshot needed: CLI execution examples -->

![CLI Examples](screenshots/cli-examples0.png)
![CLI Examples](screenshots/cli-examples1.png)
![CLI Examples](screenshots/cli-examples2.png)
![CLI Examples](screenshots/cli-examples3.png)

## 📊 Output Results

### 📁 File Structure

```
data/
├── daily_reports/           # Basic analysis results
│   ├── metadata/           # Original paper metadata
│   ├── cleaned/            # Cleaned structured data
│   └── reports/            # Generated analysis reports
└── analysis_results/       # Advanced analysis results
    ├── categories/         # Classification statistics
    ├── trends/            # Trend analysis
    └── summaries/         # Comprehensive reports
```

### 📋 Report Content

#### 🆕 v2.0 Enhanced Report Format

**Basic Analysis Reports** (`data/daily_reports/reports/`):

- **Bilingual Separated Data**: Complete bilingual titles and abstracts
- **Paper Basic Information**: ID, authors, publication date, paper links
- **Project Resource Links**: GitHub repositories, project pages (if available)
- **AI Smart Translation**: Accurate Chinese title and abstract translations
- **Model Function Analysis**: Function descriptions based on content

**Advanced Analysis Reports** (`data/analysis_results/`):

- **Rich MD Files**: Structured documents containing complete paper information
- **Technical Features Analysis**: AI-summarized core technical innovations
- **Application Scenario Identification**: Specific feasible application domains
- **Smart Classification Tags**: Auto-identified research field classifications
- **Trend Statistical Summary**: Paper counts and distribution by category

#### 📊 New Data Structure Example

```json
{
  "id": "2507.23726",
  "title_en": "Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving",
  "title_zh": "Seed-Prover：用于自动定理证明的深度和广度推理",
  "url": "https://arxiv.org/abs/2507.23726",
  "authors": "Luoxin Chen, Jinming Gu, ...",
  "publish_date": "2025-07-31",
  "summary_en": "LLMs have demonstrated strong mathematical reasoning...",
  "summary_zh": "大型语言模型通过利用带有长链式思维的强化学习...",
  "github_repo": "https://github.com/ByteDance-Seed/Seed-Prover",
  "project_page": "暂无",
  "model_function": "基于Lean反馈迭代完善证明的定理证明模型"
}
```

```MarkDown
# Seed-Prover：用于自动定理证明的深度和广度推理

**论文ID**：2507.23726
**英文标题**：Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving
**中文标题**：Seed-Prover：用于自动定理证明的深度和广度推理
**论文地址**：https://arxiv.org/abs/2507.23726

**作者团队**：Luoxin Chen, Jinming Gu, Liankai Huang, Wenhao Huang, Zhicheng Jiang, Allan Jie, Xiaoran Jin, Xing Jin, Chenggang Li, Kaijing Ma, Cheng Ren, Jiawei Shen, Wenlei Shi, Tong Sun, He Sun, Jiahui Wang, Siran Wang, Zhihong Wang, Chenrui Wei, Shufa Wei, Yonghui Wu, Yuchen Wu, Yihang Xia, Huajian Xin, Fan Yang, Huaiyuan Ying, Hongyi Yuan, Zheng Yuan, Tianyang Zhan, Chi Zhang, Yue Zhang, Ge Zhang, Tianyun Zhao, Jianqiu Zhao, Yichi Zhou, Thomas Hanwen Zhu
**发表日期**：2025-07-31

**英文摘要**：
LLMs have demonstrated strong mathematical reasoning abilities by leveraging
reinforcement learning with long chain-of-thought, yet they continue to
struggle with theorem proving due to the lack of clear supervision signals when
solely using natural language. Dedicated domain-specific languages like Lean
provide clear supervision via formal verification of proofs, enabling effective
training through reinforcement learning. In this work, we propose
Seed-Prover, a lemma-style whole-proof reasoning model. Seed-Prover
can iteratively refine its proof based on Lean feedback, proved lemmas, and
self-summarization. To solve IMO-level contest problems, we design three
test-time inference strategies that enable both deep and broad reasoning.
Seed-Prover proves 78.1% of formalized past IMO problems, saturates MiniF2F,
and achieves over 50\% on PutnamBench, outperforming the previous
state-of-the-art by a large margin. To address the lack of geometry support in
Lean, we introduce a geometry reasoning engine Seed-Geometry, which
outperforms previous formal geometry engines. We use these two systems to
participate in IMO 2025 and fully prove 5 out of 6 problems. This work
represents a significant advancement in automated mathematical reasoning,
demonstrating the effectiveness of formal verification with long
chain-of-thought reasoning.

**中文摘要**：
大型语言模型(LLMs)通过利用带有长链式思维的强化学习展现了强大的数学推理能力，但由于仅使用自然语言时缺乏明确的监督信号，它们在定理证明方面仍然存在困难。专门的领域特定语言(如Lean)通过证明的形式验证提供清晰的监督，从而能够通过强化学习进行有效训练。在这项工作中，我们提出了Seed-Prover，一种基于引理的全证明推理模型。Seed-Prover可以根据Lean反馈、已证明的引理和自我总结来迭代地完善其证明。为了解决IMO级别的竞赛问题，我们设计了三种测试时推理策略，实现了深度和广度的推理。Seed-Prover证明了78.1%的已形式化的过去IMO问题，达到了MiniF2F的饱和度，并在PutnamBench上获得了超过50%的分数，大幅超越了之前的最先进水平。为了解决Lean中几何支持的不足，我们引入了几何推理引擎Seed-Geometry，其性能超过了之前的形式几何引擎。我们使用这两个系统参加了IMO 2025，并完全证明了6个问题中的5个。这项工作代表了自动数学推理的重大进展，证明了带有长链式思维的形式验证的有效性。

**GitHub仓库**：https://github.com/ByteDance-Seed/Seed-Prover
**项目页面**：暂无
**模型功能**：基于Lean反馈迭代完善证明的定理证明模型，能解决IMO级别数学竞赛问题，并支持几何推理。

**技术特点**：Seed-Prover采用引理式全证明推理架构，能够根据Lean的形式验证反馈、已证明引理和自我总结迭代完善证明；设计了三种测试时推理策略实现深度和广度推理的结合；专门开发了Seed-Geometry几何推理引擎，弥补了Lean在几何支持方面的不足。

**应用场景**：国际数学奥林匹克竞赛(IMO)等高水平数学竞赛题目的自动求解；数学定理的形式化验证与证明生成；复杂几何问题的自动化推理与证明。

**分析时间**：2025-08-04T17:47:34.432313
```

## 🔧 Advanced Configuration

### AI Model Configuration

Edit `config/models.yaml` to customize AI model parameters:

```yaml
ai_models:
  zhipu:
    name: "Zhipu AI"
    default_model: "GLM-4.5-Air"
    api_base: "https://open.bigmodel.cn/api/paas/v4/"
    max_tokens: 4000
    temperature: 0.3
  openai:
    name: "OpenAI"
    default_model: "gpt-4"
    api_base: "https://api.openai.com/v1/"
    max_tokens: 4000
    temperature: 0.3
```

### Logging Configuration

Edit `config/logging.yaml` to adjust log level and output format:

```yaml
version: 1
formatters:
  default:
    format: "%(asctime)s [%(levelname)s] %(message)s"
handlers:
  console:
    class: logging.StreamHandler
    level: INFO
    formatter: default
  file:
    class: logging.FileHandler
    level: DEBUG
    formatter: default
    filename: logs/app.log
```

### Application Configuration

Edit `config/app.yaml` to modify output directory, batch size, etc.:

```yaml
output_dir: "data/daily_reports"
analysis_dir: "data/analysis_results"
ai_model: "zhipu"
use_ai: true
batch_size: 10
api_delay: 1
```

## 🎨 Classification System

The system supports the following intelligent classifications:

### 🤖 AI Model Categories

- **Text Generation**: Large language models, dialogue systems, text summarization
- **Image Generation**: Image synthesis, style transfer, image editing
- **Video Generation**: Video synthesis, animation generation, video editing
- **Audio Generation**: Speech synthesis, music generation, audio processing
- **3D Generation**: 3D modeling, scene generation, virtual reality
- **Multimodal Generation**: Cross-modal conversion, multimodal understanding
- **Cross-modal Generation**: Text-to-image, image-to-text, etc.
- **Game & Strategy Generation**: Game AI, strategy optimization
- **Scientific Computing & Data Generation**: Scientific simulation, data analysis

<!-- 📸 Screenshot needed: Classification results -->

![Classification Results](screenshots/classification-results.png)

## 🎯 Best Practices

### 📅 Daily Usage Recommendations

1. **Daily scheduled runs**: Recommend running previous day's analysis every morning
2. **Choose appropriate AI model**: Zhipu AI for cost-effectiveness, OpenAI for better quality
3. **Batch processing**: Process weekly data in batches on weekends
4. **Regular cleanup**: Regularly clean old analysis results to save storage space

### ⚡ Performance Optimization

1. **Concurrent processing**: Increase `batch_size` parameter to improve processing speed
2. **API rate limiting**: Adjust `api_delay` to avoid triggering API limits
3. **Cache utilization**: Repeated analysis automatically uses cached results

### 🛡️ Error Handling

1. **Network issues**: System automatically retries, no manual intervention needed
2. **API limits**: Automatically reduces request frequency
3. **Data anomalies**: Abnormal data will be marked and skipped

## 🔍 Troubleshooting

### 🛠️ Smart Diagnostic Tool

**Encountering issues? Let the AI-era smart diagnostic tool help you quickly locate and solve problems!**

```bash
python 检查环境.py  # One-click comprehensive system status diagnosis
```

**🎯 Smart Diagnosis Coverage**:

- ✅ **Python Environment Check** - Version compatibility, path configuration, venv support
- ✅ **Virtual Environment Status** - Activation status, directory structure, dependency integrity
- ✅ **Dependency Verification** - Installation status of all AI model SDKs and toolkits
- ✅ **Project File Check** - Config files, script tools, directory structure integrity
- ✅ **Smart Suggestions** - Provide specific solutions for discovered issues

**🚀 Quick Fix Tools**:

```bash
# One-click environment issue fix
# Windows: Double-click 安装环境.bat
# macOS/Linux: ./安装环境.sh

# Quick environment startup
# Windows: Double-click 启动环境.bat
# macOS/Linux: ./启动环境.sh

# View detailed usage guide
虚拟环境使用指南.md      # Complete environment management documentation
```

**💡 Diagnostic Result Example**:

```
🔍 HF Paper Analysis System - Environment Diagnostic Tool
==================================================
✅ Python Version: Python 3.11.9 (Requirements met)
✅ Virtual Environment: Currently in virtual environment
✅ Dependency Check: All 9 packages installed successfully
✅ Project Files: All required files exist
==================================================
💡 System status is good, ready to use!
```

<!-- 📸 Screenshot needed: Smart diagnostic tool results -->

![Smart Diagnosis Results](screenshots/environment-check1.png)
![Smart Diagnosis Results](screenshots/environment-check2.png)

### Common Issues & Solutions

#### 1. API Key Related Issues

**Issue**: "Invalid API key" prompt

```
❌ API key invalid or expired
```

**Solutions**:

- Check if API key is correctly copied (watch for leading/trailing spaces)
- Confirm API key hasn't expired and has sufficient balance
- Use GUI's "Test Connection" feature to verify key

**Issue**: "Insufficient API permissions" prompt

```
❌ Insufficient API key permissions, please check model access rights
```

**Solutions**:

- Confirm API key has access to corresponding model
- Contact AI service provider to enable appropriate permissions
- Try using other supported AI models

#### 2. Network Connection Issues

**Issue**: Connection timeout or network errors

```
❌ Connection timeout, please check network connection
❌ Network connection failed, please check network settings
```

**Solutions**:

- Check if network connection is normal
- Confirm firewall isn't blocking program network access
- If on corporate network, contact network admin to open relevant domain access
- Try using VPN or proxy

#### 3. Encoding Issues

**Issue**: Encoding errors on Windows

```
'gbk' codec can't encode character
```

**Solutions**:

- Ensure using UTF-8 encoded terminal
- Run in PowerShell: `chcp 65001`
- Use GUI version to avoid encoding issues

#### 4. Dependency Package Issues

**Issue**: Missing dependency packages

```
ModuleNotFoundError: No module named 'xxx'
```

**Solutions**:

```bash
# Reinstall dependencies
pip install -r requirements.txt

# Or install missing package individually
pip install package_name
```

#### 5. Permission Issues

**Issue**: Insufficient file write permissions

```
PermissionError: [Errno 13] Permission denied
```

**Solutions**:

- Ensure write permissions to project directory
- Windows users can try running as administrator
- Check if data directory exists and is writable

### 📋 System Requirements

#### Minimum Requirements

- **Python**: 3.8+ (System will auto-detect version compatibility)
- **Memory**: 4GB RAM
- **Storage**: 2GB available space
- **Network**: Stable internet connection

#### Recommended Configuration

- **Python**: 3.10+ (Recommend 3.11.9 for optimal performance)
- **Memory**: 8GB+ RAM
- **Storage**: 10GB+ available space (for storing analysis results)
- **Network**: High-speed stable network connection

#### 🛠️ Environment Management Tools

**No need to worry about complex environment configuration! The system provides a complete environment management toolchain:**

| Tool                  | Function                                             | Use Case                                          |
| --------------------- | ---------------------------------------------------- | ------------------------------------------------- |
| `安装环境.bat/.sh`    | One-click install all dependencies and configuration | First installation or environment reconfiguration |
| `启动环境.bat/.sh`    | Quick virtual environment activation                 | Daily environment activation before use           |
| `检查环境.py`         | Smart system status diagnosis                        | Troubleshooting or installation verification      |
| `虚拟环境使用指南.md` | Detailed environment management documentation        | In-depth understanding of environment management  |

**💡 Environment Management Best Practices**:

- 🎯 **New Users**:
  - Windows: Simply double-click `安装环境.bat` → `启动环境.bat` → Start using
  - macOS/Linux: `./安装环境.sh` → `./启动环境.sh` → Start using
- 🔧 **When Issues Arise**: Run `python 检查环境.py` for smart diagnostic suggestions
- 📖 **Advanced Customization**: Refer to `虚拟环境使用指南.md` for advanced configuration

### 🐛 Debug Mode

Enable verbose logging:

```bash
# Set log level to DEBUG
export LOG_LEVEL=DEBUG

# Or modify in config file
# config/logging.yaml
```

View detailed error information:

```bash
# Use --verbose parameter
python run.py basic 2025-07-29 --verbose

# View log file
tail -f logs/app.log
```

## 🤝 Contributing

Welcome to submit Issues and Pull Requests!

### Development Environment Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Code formatting
black src/ tests/
```

### Commit Guidelines

- Feature development: `feat: add new feature`
- Bug fixes: `fix: fix some issue`
- Documentation updates: `docs: update documentation`

## ❓ Frequently Asked Questions (FAQ)

### Q1: Which AI models are supported?

**A**: Currently supports the following AI models:

- **Zhipu AI**: GLM-4.5-Air, GLM-4, etc.
- **Doubao AI**: doubao-pro-32k, etc.
- **OpenAI**: GPT-4, GPT-3.5-turbo, etc.
- **Qwen**: qwen-plus, qwen-turbo, etc.
- **ERNIE**: Requires additional secret_key configuration
- **Hunyuan**: Requires additional secret_key and signature algorithm configuration

### Q2: How many papers can be processed daily?

**A**: Processing capacity depends on:

- **API limits**: Call frequency limits of various AI service providers
- **Network speed**: Speed of downloading and uploading data
- **Hardware configuration**: CPU and memory affect processing speed
- Typically can process 50-200 papers daily

### Q3: How accurate are the analysis results?

**A**: Analysis accuracy depends on:

- **AI model quality**: GPT-4 > Zhipu AI > other models
- **Paper quality**: Well-structured papers have better analysis results
- **Prompt optimization**: System uses specially optimized prompts
- Recommend using multiple models for cross-validation of important results

### Q4: How to improve processing speed?

**A**: Optimization suggestions:

- Increase `batch_size` parameter (note API limits)
- Use faster AI models (like Zhipu AI)
- Ensure stable network connection
- Use SSD storage to improve I/O speed

### Q5: Where is data stored?

**A**: All data is stored locally:

- **Raw data**: `data/daily_reports/metadata/`
- **Cleaned data**: `data/daily_reports/cleaned/`
- **Analysis results**: `data/daily_reports/reports/`
- **Classification results**: `data/analysis_results/`

### Q6: How to backup and restore data?

**A**: Backup recommendations:

```bash
# Backup all data
tar -czf backup_$(date +%Y%m%d).tar.gz data/

# Restore data
tar -xzf backup_20250729.tar.gz
```

### Q7: Can classifications be customized?

**A**: Yes, by modifying prompts:

- Edit classification prompts in `src/core/classifier.py`
- Modify classification knowledge base content
- Retrain or adjust AI model parameters

### Q8: Does it support offline use?

**A**: Partial features support offline:

- **Data download**: Requires network connection
- **AI analysis**: Requires calling online AI services
- **Result viewing**: Can view generated results offline
- **Batch processing**: Can process downloaded data offline (without AI analysis)

### Q9: How to handle large amounts of historical data?

**A**: Batch processing recommendations:

```bash
# Use batch processing tool
python tools/batch_processor.py daily --start 2025-01-01 --end 2025-07-29

# Process in batches to avoid API limits
python tools/batch_processor.py daily --start 2025-01-01 --end 2025-01-31
python tools/batch_processor.py daily --start 2025-02-01 --end 2025-02-28
```

### Q10: How to get help when encountering problems?

**A**: Ways to get help:

1. **Check documentation**: Read this README and tools/README.md
2. **Check logs**: View logs/app.log file
3. **Submit Issues**: Submit detailed problem descriptions on GitHub
4. **Community discussion**: Participate in project discussion area
5. **Contact developers**: Contact via email or other means

## 📈 Performance Benchmarks

### 🚀 v2.0 Performance Improvement Comparison

| Processing Stage         | v1.0 (Old)             | v2.0 (New)           | Improvement       |
| ------------------------ | ---------------------- | -------------------- | ----------------- |
| **Data Cleaning**        | AI required, 30-60s    | Rule-based, 1-3s     | **20x faster**    |
| **Paper Analysis**       | 60-90s/paper           | 5-10s/paper          | **10x faster**    |
| **MD Splitting**         | Basic info             | Rich info, seconds   | **3x more info**  |
| **Smart Classification** | Regenerate all content | Only add core fields | **2x efficiency** |

### 🔥 v2.1 Rage Mode Performance Boost

| Processing Mode | Basic Analysis Time | Advanced Classification Time | Improvement   | Key Features               |
| --------------- | ------------------- | ---------------------------- | ------------- | -------------------------- |
| **Normal Mode** | ~3 minutes          | ~2 minutes                   | Baseline      | Serial processing, stable  |
| **🔥Rage Mode** | ~34 seconds         | ~45 seconds                  | **5x faster** | 5-concurrent, progress bar |

**🎯 Rage Mode Features**:

- **5-Concurrent Processing** - Process 5 papers simultaneously, fully utilize API concurrency
- **Real-time Progress Bar** - Fixed position display of processing progress and timing statistics
- **Smart Caching Mechanism** - Auto-detect processed content, avoid duplicate work
- **Thread-Safe Design** - Stable concurrent processing, ensure data consistency

### Processing Speed Reference (v2.0)

| Configuration           | Paper Count | Processing Time | Average Speed   | v1.0 Comparison |
| ----------------------- | ----------- | --------------- | --------------- | --------------- |
| Basic Config            | 50 papers   | 5-8 minutes     | 6-10 papers/min | **3x faster**   |
| Recommended Config      | 100 papers  | 8-15 minutes    | 7-12 papers/min | **3x faster**   |
| High Performance Config | 200 papers  | 15-25 minutes   | 8-13 papers/min | **3x faster**   |

### 🎯 v2.0 Optimization Highlights

- ✅ **Smart Data Cleaning**: From AI dependency to rule-based cleaning, 20x speed improvement
- ✅ **AI Analysis Optimization**: No external link access, focus on translation and analysis, 10x speed improvement
- ✅ **Data Structure Optimization**: Bilingual separation, more complete information, more efficient processing
- ✅ **Intelligent Workflow**: Avoid duplicate work, AI focuses on most valuable tasks

### Resource Usage

- **Memory usage**: Typically 200-500MB (same as v1.0)
- **Storage space**: About 1.5-2.5MB analysis results per paper (richer information)
- **Network traffic**: About 50-200KB per paper (reduced external access)
- **API calls**: 60% fewer invalid calls, lower cost

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [HuggingFace](https://huggingface.co/) - Providing paper data source
- [Zhipu AI](https://open.bigmodel.cn/) - AI analysis service
- All contributors and users for their support

## 👨‍💻 Author

- ZsTs119
- Email: zsts@foxmail.com
- GitHub: https://github.com/ZsTs119

---

⭐ If this project helps you, please give us a Star!

📧 Have questions or suggestions? Welcome to submit [Issues](../../issues) or contact us.

# View log file

tail -f logs/app.log

```

```
