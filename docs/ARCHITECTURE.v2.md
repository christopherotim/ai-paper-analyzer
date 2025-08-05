# 🏗️ AI 论文智能分析系统 - 技术架构设计 v2（对齐 v2.0/v2.1 实现）

<div align="center">

[English v2](./ARCHITECTURE.v2.en.md) | [简体中文 v2](./ARCHITECTURE.v2.md)

</div>

本版本为对齐代码实现的最新技术架构文档，聚焦“目录-模块-文件一一映射、真实数据流与产物路径、Rage Mode 并发与缓存策略、数据模型字段与代码一致、与旧版差异标注”。适合作为开发者快速理解当前项目的权威参考。

目录

- 快速索引（典型场景）
- 系统概述与边界
- 电梯摘要（3 分钟看懂）
- 模块与目录映射（代码级）
- 架构图（与文件名一致）
- 端到端数据流与阶段产物
- 数据模型（字段与 JSON 示例）
- v2.0/v2.1 核心特性
- Rage Mode 参数与行为
- 性能策略与容错
- 配置与环境（最少必读）
- 部署与运行（简版）
- 安全、扩展与规划（状态标注）
- 术语表与命名规范
- 版本变更与旧版差异
- 附录 A：模块 API 速查表
- 附录 B：产物命名与去重/跳过策略
- 附录 C：常见卡点自检清单

## 🚦 快速索引（典型场景）

- 我想每天只跑基础分析 → 见「电梯摘要」与「端到端数据流」的 basic 流程
- 我想生成分类与汇总报告 → 运行 advanced，见「端到端数据流」与「Rage Mode」
- 我想加速分析/分类 → 见「Rage Mode 参数与行为」
- 我想找输出文件在哪 → 见「端到端数据流与阶段产物」
- 我想换用别的 AI 提供商 → 见「配置与环境（最少必读）」
- 我遇到运行问题 → 见「附录 C：常见卡点自检清单」

## 🎯 系统概述与边界

系统目标

- 自动化从 HuggingFace 获取每日论文元数据，完成数据清洗、AI 辅助分析、智能分类与汇总，输出结构化 JSON 报表与可读的 Markdown 文件。

用户与价值

- 研究者/工程师：一键跑通 basic 和 advanced，快速获得当天论文洞察、分类与汇总；支持并发加速、缓存跳过和批处理，降低等待与成本。

系统边界（三行式）

- 输入：HuggingFace 每日论文 API + 用户配置
- 处理：下载 → 清洗 → AI 分析 → MD 切分 → 分类 → 汇总
- 输出：JSON 日报 + 分类 MD 文档 + 分类汇总

运行方式

- CLI：basic、advanced、status（详见 README）
- GUI：run_gui.py、tools/batch_processor_gui.py（与 CLI 复用核心模块）
- 批处理：tools/batch_processor.py（README 提及）

## ⚡ 电梯摘要（3 分钟看懂）

先决条件

- Python 3.8+，pip install -r requirements.txt
- 已正确设置 AI 提供商的 API Key（如 ZHIPUAI_API_KEY、ARK_API_KEY）
- 网络/代理可访问提供商服务（如使用公司代理，请先在系统或环境中配置）

你将得到什么

- 每日一键获取论文洞察：JSON 日报 + 分类 Markdown + 分类汇总

如何一键运行

- 基础分析（当天）：python run.py basic
  - 失败优先检查：API Key 是否生效、网络/代理是否可用、当日是否有数据
- 指定日期 + 狂暴模式：python run.py basic 2025-08-01 --rageMode
  - 失败优先检查：日期格式是否为 YYYY-MM-DD、API 限流/余额、网络超时
- 生成分类与汇总：python run.py advanced 2025-08-01
  - 失败优先检查：对应日期的日报 JSON 是否已生成（见下方产出路径）

产出在哪里（示例）

- data/daily_reports/metadata/2025-08-01.json（元数据；任意编辑器可查看）
- data/daily_reports/cleaned/2025-08-01_clean.json（清洗结果；JSON 结构化）
- data/daily_reports/reports/2025-08-01_report.json（日报；分析结果累积写入）
- data/analysis_results/2025-08-01/分类目录/\*.md、模型分类汇总.md、classification_stats.json（分类产物；直接打开 .md 即可阅读）

提示

- advanced 依赖对应日期的 basic 日报
- Rage Mode 适合网络稳定且 API 余额充足的场景

## 🧱 模块与目录映射（代码级）

入口与调度

- CLI 主入口与命令定义：src/main.py
  - basic：下载 → 清洗 → 分析
  - advanced：MD 切分 → 分类 → 汇总
  - status：配置与环境摘要

核心业务模块

- 元数据下载：src/core/downloader.py
  - MetadataDownloader：下载到 data/daily_reports/metadata/{date}.json
- 清洗：src/core/cleaner.py
  - DataCleaner：规则清洗（默认），AI 清洗框架（解析待完善）
  - 产物：data/daily_reports/cleaned/{date}\_clean.json
- 分析：src/core/analyzer.py
  - PaperAnalyzer：顺序/并发分析（Rage Mode），即时追加写入 report.json
  - 依赖缓存：src/core/cache_manager.py（PaperCacheManager）
  - 产物：data/daily_reports/reports/{date}\_report.json
- 分类与 MD：src/core/classifier.py
  - split_to_md：由分析结果生成单篇 MD（date 目录下）
  - classify_papers：串行/并发分类，已存在同名 MD 时跳过（CACHED）
  - generate_summary_report：模型分类汇总.md、classification_stats.json
- 解析器：src/core/parser.py
  - ContentParser：AI 响应/清洗文本解析、ID 校验与提取
- 缓存：src/core/cache_manager.py
  - PaperCacheManager：哈希键、过期清理、缓存命中读取/写入

模型与数据结构

- 论文：src/models/paper.py（Paper、PaperCollection）
- 报告/结果：src/models/report.py
  - AnalysisResult（中英文分离）、ClassificationResult、DailyReport、AnalysisSummary

基础设施

- AI 客户端：src/utils/ai_client.py
  - AIClient 抽象、Zhipu/Doubao 实现、Retry 包装器、增强工厂（配置驱动）
- 其他：src/utils/config.py | logger.py | file_utils.py | progress.py | console.py

与旧版术语对应

- Data Fetcher（文档） → MetadataDownloader（代码）
- Report Generator（文档概念） → 分散在 analyzer（日报 JSON）与 classifier（汇总 MD）

## 🏛️ 架构图（与文件名一致）

```text
┌─────────────────────────────────────────────────────────────┐
│                     用户接口层 UI Layer                     │
├─────────────────────┬───────────────────────────────────────┤
│ GUI (Tkinter)       │ CLI (Argparse)                        │
│ run_gui.py          │ src/main.py                           │
└─────────────────────┴───────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                   业务逻辑层 Business Layer                  │
├───────────────────────────┬──────────────────────────────────┤
│ Main Controller           │ Batch Tools (tools/*.py)         │
│ src/main.py (App)         │ pipeline/daily/advanced          │
└───────────────────────────┴──────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                     核心服务层 Core Layer                    │
├───────────────┬───────────────┬───────────────┬─────────────┤
│ Downloader    │ Cleaner       │ Analyzer      │ Classifier   │
│ core/downloader.py           │ core/analyzer.py │ core/classifier.py │
├───────────────┴───────────────┴───────────────┼─────────────┤
│ Parser (core/parser.py)                       │ Cache (core/cache_manager.py)
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                基础设施层 Infrastructure Layer               │
├─────────────┬──────────────┬──────────────┬─────────────────┤
│ AI Client   │ File Utils   │ Logger       │ Config/Console  │
│ utils/ai_client.py │ utils/file_utils.py │ utils/logger.py  │
│ utils/progress.py  │ utils/config.py     │ utils/console.py │
└─────────────┴──────────────┴──────────────┴─────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                      数据层 Data Layer                       │
├──────────────┬──────────────┬──────────────┬────────────────┤
│ metadata     │ cleaned      │ reports      │ analysis_results│
│ JSON         │ JSON         │ JSON         │ MD/summary JSON │
└──────────────┴──────────────┴──────────────┴────────────────┘
```

## 🔄 端到端数据流与阶段产物

流程总览

1. basic（CLI）

- MetadataDownloader.download → DataCleaner.clean → PaperAnalyzer.analyze_batch / analyze_batch_concurrent
- 输出：data/daily_reports/reports/{date}\_report.json（即时追加写入，避免长任务丢失）
- 断点续跑：对同一日期重跑会自动跳过已处理的 paper_id，并复用命中的缓存结果（无需额外参数）

2. advanced（CLI）

- load_analysis_results → PaperClassifier.split_to_md → classify_papers → generate_summary_report
- 输出：
  - data/analysis_results/{date}/分类目录/单篇论文.md
  - data/analysis_results/{date}/模型分类汇总.md
  - data/analysis_results/{date}/classification_stats.json

3. Rage Mode 并发（v2.1）

- 基于线程池的 5 并发（分析/分类），实时进度条与统计输出；支持缓存命中与跳过，减少重复调用；分析阶段仍即时落盘。

产物路径明细

- 元数据：data/daily_reports/metadata/{date}.json（示例：2025-08-01.json）
- 清洗数据：data/daily_reports/cleaned/{date}\_clean.json（示例：2025-08-01_clean.json）
- 日报 JSON：data/daily_reports/reports/{date}\_report.json（示例：2025-08-01_report.json）
- 分类结果：data/analysis_results/{date}/
  - {分类名称}/单篇论文.md（直接打开即可查看具体分类内容）
  - 模型分类汇总.md（各类别与数量的汇总）
  - classification_stats.json（分类统计与命中率等信息）

跳过/去重策略

- 分析：启动前读取既有 report.json，跳过已处理 paper_id；命中缓存则直接返回 AnalysisResult。
- 分类：若分类目录下已存在相同标题生成的 MD，标记 CACHED 跳过（如需强制重算，删除对应 MD 后重跑）。

## 🧩 数据模型（字段与 JSON 示例）

Paper（src/models/paper.py）

- 字段：id, title, translation, url, authors, publish_date, summary, github_repo, project_page, model_function
- from_dict 与 from_legacy_format 支持旧字段透传
- arXiv ID 与 URL 校验

AnalysisResult（src/models/report.py）

- 字段（中英文分离）：id, title_en, title_zh, url, authors, publish_date, summary_en, summary_zh, github_repo, project_page, model_function, analysis_time
- 兼容属性：paper_id（=id）, title（=title_en）, translation（=title_zh）
- JSON 示例（简化）：

```json
{
  "id": "2405.08317",
  "title_en": "Vision-Language Model ...",
  "title_zh": "视觉语言模型 ...",
  "url": "https://arxiv.org/abs/2405.08317",
  "authors": "Alice, Bob",
  "publish_date": "2025-07-31",
  "summary_en": "This paper proposes ...",
  "summary_zh": "本文提出 ...",
  "github_repo": "https://github.com/xxx",
  "project_page": "https://project.site",
  "model_function": "多模态理解与生成",
  "analysis_time": "2025-08-05T09:30:00"
}
```

ClassificationResult

- 字段：paper_id, category, confidence, md_content, classification_time

DailyReport

- 字段：date, total_papers, analysis_results[], generation_time, metadata

旧 → 新字段映射（常见）

- title → title_en
- translation → title_zh
- summary → summary_en；summary_zh 由 AI 翻译或回退生成
- id/paper_id → id（兼容）

## 🚀 v2.0/v2.1 核心特性

v2.0

- 规则优先的数据清洗（AI 清洗可选）
- 结构化日报 JSON 输出，统一 CLI/GUI 入口
- 完整日志与进度体验
- 数据模型标准化（为 v2.1 做准备）

v2.1 Rage Mode

- 5 并发线程池（分析/分类），实时进度条，统计输出
- 分析阶段：即时保存单条结果到 report.json，失败不影响已完成数据
- 缓存命中与跳过：PaperCacheManager（分析），分类目录同名 MD（分类）

## 🔥 Rage Mode 参数与行为

固定参数（当前实现）

- 并发度：5（线程池）
- 分析超时：90s/次调用；重试：3 次；指数退避
- 分类：并发 5，进度时钟显示，错误单条不影响整体

行为说明

- 分析会先读取已存在的 {date}\_report.json，跳过已处理 ID；命中缓存直接复用结果
- 每条完成即写入 JSON，降低长任务失败风险
- 分类阶段若检测到同名 MD 文件则标记 CACHED 跳过
- advanced 流程中的分类同样使用并发=5（与 basic 中分析阶段一致）

适用/不适用

- 适用：批量处理、多论文高吞吐、网络稳定
- 不适用：网络抖动、提供商限流严格、API 余额紧张

## ⚙️ 性能策略与容错

并发模型

- 线程池 + 即时落盘 + 跳过已处理 ID
- 统计：成功/失败/跳过、平均耗时、并发效率等（控制台/日志）

重试/超时

- 分析 AI 调用：重试 + 90s 超时 + 进度反馈
- 分类 AI 调用：进度计时与错误日志
- Downloader：基础超时与错误处理（建议引入镜像轮询与重试参数化，见“规划”）

缓存策略（分析）

- PaperCacheManager：hash 键（id+title+summary 片段），默认 30 天过期
- 命中后直接返回 AnalysisResult，减少重复成本

命名冲突与去重

- 分析：通过已存在 report.json 提取 paper_id 去重
- 分类：当前按中文标题生成文件名，易冲突；建议规范为 safe_title\_\_{paper_id}.md（规划项）

## 🧰 配置与环境（最少必读）

必改/必知

- 默认 AI 提供商与模型：utils/config.py 的默认设置（通过环境或配置文件覆盖）
- API Key：按提供商要求设置环境变量（如 ZHIPUAI_API_KEY、ARK_API_KEY）
- 输出目录：默认 data/ 路径，可在配置中调整

常见修改示例

- 切换 AI 提供商：配置默认 provider 或通过 EnhancedAIClientFactory 指定
- 网络代理与超时：downloader 支持 proxies 与 timeout

最小配置片段（可选，保存为 config/app.yaml 或通过环境变量覆盖）

```yaml
provider:
  default: zhipu # 或 doubao
output:
  base_dir: data # 自定义输出根目录
ai:
  retries: 3
  timeout_seconds: 90
# API Key 请通过环境变量注入，例如：
#   ZHIPUAI_API_KEY=xxxx
#   ARK_API_KEY=xxxx
```

平台提示

- Windows 控制台已适配 UTF-8（src/main.py 冒头），如仍乱码，可尝试在终端手动切换代码页

配置来源

- utils/config.py（默认输出目录、默认 AI 提供商、AI 开关、批大小、API 延迟等）
- utils/ai_client.py 增强工厂：从配置创建可重试 AI 客户端

Downloader 参数

- api_url（可换镜像）、timeout、proxies

平台兼容

- Windows 控制台 UTF-8 适配（main.py 冒头设置 chcp 与重定向）

附录 C：常见卡点自检清单（扩展）

- 下载失败类：检查网络与代理；更换/配置 api_url 镜像；提高 timeout；重试运行 basic。
- AI 调用失败类：确认 API Key 环境变量已生效；检查账号余额与限流；观察是否发生 90s 超时并适当降低并发或分批运行。
- 文件系统类：确保 data/ 路径可写；若路径不存在让程序自动创建或手动创建；Windows 下注意路径过长问题。

## 📦 部署与运行（简版）

- 本地：Python 3.8+，安装 requirements.txt，配置好 AI Key，运行 run.py basic / advanced 或 GUI。
- 容器：参考 Dockerfile 与 docker-compose（数据、logs、config 挂载）。
- 详细说明以 README 为准。

## 🔒 安全、扩展与规划（状态标注）

当前已实现

- 基础日志、文件与配置管理
- AI Key 通过环境/配置注入

规划/建议（尚未落地的蓝图）

- API Key 加密存储与白名单 HTTP 客户端
- Downloader 多镜像轮询与指数退避
- 并发度/退避/超时/重试配置化与命令行覆盖
- MD 命名规范引入 paper_id，避免重名
- 监控与健康检查、微服务化接口

## 📚 术语表与命名规范

- Basic 分析：下载/清洗/分析过程，产出日报 JSON
- Advanced 分析：MD 切分/分类/汇总，产出分类 MD 与汇总
- Rage Mode：并发=5 的高性能模式，带实时进度
- 缓存命中（分析）：命中 PaperCacheManager 的历史结果
- CACHED 跳过（分类）：存在同名 MD 时不重复分类；例：若已存在“安全标题.md”，再次运行将显示 CACHED 并跳过。如需强制重算，请删除该 MD 后重跑。
- 产物路径：metadata/cleaned/reports/analysis_results

## 🗂️ 版本变更与旧版差异

- 命名映射：Fetcher → Downloader(MetadataDownloader)
- 数据模型：AnalysisResult 改为中英分离（title_en/title_zh，summary_en/summary_zh），提供兼容属性
- 新增 Rage Mode 并发与即时落盘；缓存命中与跳过策略强化
- 文档蓝图部分（加密、白名单 HTTP、监控、微服务）改为“规划/建议”标注，避免误解为已实现
