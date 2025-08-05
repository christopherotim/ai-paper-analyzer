# 🏗️ AI Paper Intelligence - Architecture v2 (aligned with v2.0/v2.1)

<div align="center">

[English (v2)](./ARCHITECTURE.v2.en.md) | [简体中文 v2](./ARCHITECTURE.v2.md)

</div>

This document is the authoritative, code-aligned architecture for v2.0/v2.1. It focuses on module-to-file mapping, real data flows and artifact paths, Rage Mode concurrency and caching, data models matched to code, and differences from the legacy doc. Designed for both users and developers to get productive fast.

Contents

- Quick Index (typical scenarios)
- Overview and Boundaries
- Elevator Summary (3 minutes)
- Module-to-Directory Mapping (code-level)
- Architecture Diagram (file-accurate)
- End-to-End Flow & Artifacts
- Data Models (fields + JSON sample)
- v2.0/v2.1 Key Features
- Rage Mode Parameters & Behavior
- Performance & Resilience
- Configuration & Environment (minimal must-read)
- Run & Deployment (brief)
- Security, Extensibility & Roadmap (status labels)
- Glossary & Naming
- Version Changes vs Legacy
- Appendix A: Module API Quick Reference
- Appendix B: Artifact naming and skip/dedupe strategy
- Appendix C: Troubleshooting checklist

## 🚦 Quick Index (typical scenarios)

- Only run daily basic analysis → see “Elevator Summary” and “End-to-End Flow” (basic)
- Need classification and summary → run advanced, see “End-to-End Flow” and “Rage Mode”
- Want acceleration → see “Rage Mode Parameters & Behavior”
- Can’t find outputs → see “End-to-End Flow & Artifacts”
- Switch AI providers → see “Configuration & Environment”
- Something broke → see “Appendix C: Troubleshooting”

## 🎯 Overview and Boundaries

Goals

- Automate fetching daily paper metadata from HuggingFace, perform cleaning, AI-assisted analysis, smart classification, and summary; output structured JSON reports and human-readable Markdown.

Users & Value

- Researchers/Engineers: one-command basic/advanced runs; fast insights, classification, and summary; concurrency and caching to reduce waiting and cost.

Boundaries (3 lines)

- Input: HF daily metadata API + user configuration
- Processing: download → clean → AI analyze → split MD → classify → summarize
- Output: JSON daily report + categorized Markdown + classification summary

Interfaces

- CLI: basic, advanced, status (see README)
- GUI: run_gui.py, tools/batch_processor_gui.py (reuses core modules)
- Batch: tools/batch_processor.py (mentioned in README)

## ⚡ Elevator Summary (3 minutes)

Prerequisites

- Python 3.8+, pip install -r requirements.txt
- Properly set provider API Keys (e.g., ZHIPUAI_API_KEY, ARK_API_KEY)
- Network/proxy can reach the provider services

What you get

- Daily insights with one command: JSON report + categorized Markdown + summary

How to run

- Basic (today): python run.py basic
  - If it fails, check: API Key validity, network/proxy availability, whether today has data
- Specific date + Rage Mode: python run.py basic 2025-08-01 --rageMode
  - If it fails, check: date format YYYY-MM-DD, API rate/credits, network timeout
- Classification & summary: python run.py advanced 2025-08-01
  - If it fails, check: the date’s daily JSON exists (see artifact paths below)

Where are outputs (examples)

- data/daily_reports/metadata/2025-08-01.json (metadata; view in any editor)
- data/daily_reports/cleaned/2025-08-01_clean.json (cleaned; structured JSON)
- data/daily_reports/reports/2025-08-01_report.json (daily; incremental writes)
- data/analysis_results/2025-08-01/category/\*.md, classification_summary.md, classification_stats.json (open .md directly)

Notes

- advanced depends on the date’s basic daily report
- Rage Mode fits stable network and sufficient API credits

## 🧱 Module-to-Directory Mapping (code-level)

Entry & Orchestration

- CLI entry and commands: src/main.py
  - basic: download → clean → analyze
  - advanced: split MD → classify → summarize
  - status: config and environment summary

Core business modules

- Metadata download: src/core/downloader.py
  - MetadataDownloader → data/daily_reports/metadata/{date}.json
- Cleaning: src/core/cleaner.py
  - DataCleaner: rule-based by default; AI cleaning framework (parsing TBD)
  - Output: data/daily_reports/cleaned/{date}\_clean.json
- Analysis: src/core/analyzer.py
  - PaperAnalyzer: sequential/concurrent (Rage Mode), immediate append to report.json
  - Cache: src/core/cache_manager.py (PaperCacheManager)
  - Output: data/daily_reports/reports/{date}\_report.json
- Classification & MD: src/core/classifier.py
  - split_to_md: generate per-paper MD under date folder
  - classify_papers: sequential or 5-concurrent; skip if same-name MD exists (CACHED)
  - generate_summary_report: classification_summary.md, classification_stats.json
- Parser: src/core/parser.py
  - ContentParser: parse AI/cleaning text, extract fields/IDs and validate
- Cache: src/core/cache_manager.py
  - PaperCacheManager: hash keys, expiry purge, read/write hits

Models & data structures

- Paper: src/models/paper.py (Paper, PaperCollection)
- Reports/Results: src/models/report.py
  - AnalysisResult (EN/ZH split), ClassificationResult, DailyReport, AnalysisSummary

Infrastructure

- AI clients: src/utils/ai_client.py
  - AIClient base, Zhipu/Doubao implementations, Retry wrapper, enhanced factory (config-driven)
- Others: src/utils/config.py | logger.py | file_utils.py | progress.py | console.py

Legacy term mapping

- Data Fetcher (doc) → MetadataDownloader (code)
- Report Generator (doc concept) → analyzer (daily JSON) + classifier (summary MD)

## 🏛️ Architecture Diagram (file-accurate)

```text
┌─────────────────────────────────────────────────────────────┐
│                         UI Layer                            │
├─────────────────────┬───────────────────────────────────────┤
│ GUI (Tkinter)       │ CLI (Argparse)                        │
│ run_gui.py          │ src/main.py                           │
└─────────────────────┴───────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                     Business Layer                           │
├───────────────────────────┬──────────────────────────────────┤
│ Main Controller           │ Batch Tools (tools/*.py)         │
│ src/main.py (App)         │ pipeline/daily/advanced          │
└───────────────────────────┴──────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                       Core Layer                             │
├───────────────┬───────────────┬───────────────┬─────────────┤
│ Downloader    │ Cleaner       │ Analyzer      │ Classifier   │
│ core/downloader.py           │ core/analyzer.py │ core/classifier.py │
├───────────────┴───────────────┴───────────────┼─────────────┤
│ Parser (core/parser.py)                       │ Cache (core/cache_manager.py)
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                      Infrastructure                          │
├─────────────┬──────────────┬──────────────┬─────────────────┤
│ AI Client   │ File Utils   │ Logger       │ Config/Console  │
│ utils/ai_client.py │ utils/file_utils.py │ utils/logger.py  │
│ utils/progress.py  │ utils/config.py     │ utils/console.py │
└─────────────┴──────────────┴──────────────┴─────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                         Data Layer                           │
├──────────────┬──────────────┬──────────────┬────────────────┤
│ metadata     │ cleaned      │ reports      │ analysis_results│
│ JSON         │ JSON         │ JSON         │ MD/summary JSON │
└──────────────┴──────────────┴──────────────┴────────────────┘
```

## 🔄 End-to-End Flow & Artifacts

Flow overview

1. basic (CLI)

- MetadataDownloader.download → DataCleaner.clean → PaperAnalyzer.analyze_batch / analyze_batch_concurrent
- Output: data/daily_reports/reports/{date}\_report.json (incremental writes to avoid long-run loss)
- Resume-friendly: re-running the same date automatically skips processed paper_id and reuses cache hits (no extra args)

2. advanced (CLI)

- load_analysis_results → PaperClassifier.split_to_md → classify_papers → generate_summary_report
- Outputs:
  - data/analysis_results/{date}/category/per-paper.md
  - data/analysis_results/{date}/classification_summary.md
  - data/analysis_results/{date}/classification_stats.json

3. Rage Mode (v2.1)

- ThreadPool-based 5-concurrency (analysis/classification), real-time progress and stats; cache hit/skip to reduce duplication; analysis still writes incrementally.

Artifact paths

- Metadata: data/daily_reports/metadata/{date}.json (e.g., 2025-08-01.json)
- Cleaned: data/daily_reports/cleaned/{date}\_clean.json (e.g., 2025-08-01_clean.json)
- Daily JSON: data/daily_reports/reports/{date}\_report.json (e.g., 2025-08-01_report.json)
- Classification: data/analysis_results/{date}/
  - {category}/per-paper.md (open .md to read classified content)
  - classification_summary.md (category counts and overview)
  - classification_stats.json (classification stats and hit rates)

Skip/Dedupe strategy

- Analysis: read existing report.json at start, skip processed paper_id; return cached AnalysisResult when hit.
- Classification: if an MD with the same safe title exists under category, mark CACHED and skip (force recompute by deleting the MD then rerun).

## 🧩 Data Models (fields & JSON sample)

Paper (src/models/paper.py)

- Fields: id, title, translation, url, authors, publish_date, summary, github_repo, project_page, model_function
- from_dict and from_legacy_format support legacy pass-through
- arXiv ID and URL validation

AnalysisResult (src/models/report.py)

- Fields (EN/ZH split): id, title_en, title_zh, url, authors, publish_date, summary_en, summary_zh, github_repo, project_page, model_function, analysis_time
- Backward-compat props: paper_id (=id), title (=title_en), translation (=title_zh)
- JSON sample (simplified):

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
  "model_function": "Multimodal understanding and generation",
  "analysis_time": "2025-08-05T09:30:00"
}
```

ClassificationResult

- Fields: paper_id, category, confidence, md_content, classification_time

DailyReport

- Fields: date, total_papers, analysis_results[], generation_time, metadata

Legacy → New mapping (common)

- title → title_en
- translation → title_zh
- summary → summary_en; summary_zh is AI-translated or fallback-generated
- id/paper_id → id (compatible)

## 🚀 v2.0/v2.1 Key Features

v2.0

- Rule-first cleaning (AI optional)
- Structured daily JSON output, unified CLI/GUI entry
- Full logging and progress UX
- Standardized data model (preps for v2.1)

v2.1 Rage Mode

- 5-thread concurrency (analysis/classification), real-time progress, stats output
- Analysis: immediate per-item save to report.json; failures don’t affect completed data
- Cache hits and skip: PaperCacheManager (analysis), same-name MD under category (classification)

## 🔥 Rage Mode Parameters & Behavior

Fixed parameters (current)

- Concurrency: 5 (ThreadPool)
- Analysis timeout: 90s per call; Retries: 3; Exponential backoff
- Classification: concurrency 5, progress clock, per-item failure doesn’t block overall

Behavior

- Analysis reads existing {date}\_report.json to skip processed IDs; reuse cache when hit
- Write each item immediately to JSON to reduce long-run risk
- Classification marks CACHED when same-name MD exists
- advanced classification also uses concurrency=5 (same as analysis in basic)

When to use / avoid

- Use: batch processing, higher throughput, stable network
- Avoid: unstable network, strict rate limits, tight API credits

## ⚙️ Performance & Resilience

Concurrency model

- ThreadPool + incremental writes + skip processed IDs
- Stats: success/failure/skip, avg latency, concurrency efficiency (console/logs)

Retry/Timeout

- Analysis AI: retries + 90s timeout + progress feedback
- Classification AI: progress timing and error logs
- Downloader: base timeout and error handling (suggested mirror rotation & parameterized retry; see roadmap)

Cache (analysis)

- PaperCacheManager: hash key (id + title + summary snippet), default expiry 30 days
- Return AnalysisResult on hit to reduce repeated cost

Naming conflicts & dedupe

- Analysis: dedupe by processed IDs from existing report.json
- Classification: current filename from Chinese title; collision-prone. Recommendation: safe_title\_\_{paper_id}.md (roadmap)

## 🧰 Configuration & Environment (minimal must-read)

Must-know

- Default provider and model: defaults in utils/config.py (override via env or config file)
- API Keys: set provider env vars (e.g., ZHIPUAI_API_KEY, ARK_API_KEY)
- Output directories: default under data/, override in config

Common changes

- Switch provider: set provider.default or use EnhancedAIClientFactory
- Network proxy/timeout: downloader supports proxies and timeout

Minimal config snippet (optional, save as config/app.yaml or override via env)

```yaml
provider:
  default: zhipu # or doubao
output:
  base_dir: data # customize output root
ai:
  retries: 3
  timeout_seconds: 90
# Inject API Keys via environment variables, e.g.:
#   ZHIPUAI_API_KEY=xxxx
#   ARK_API_KEY=xxxx
```

Platform notes

- Windows console set to UTF-8 in src/main.py; if garbled, switch code page manually in the terminal

Config sources

- utils/config.py (output dir, default provider, AI toggles, batch size, API delay, etc.)
- utils/ai_client.py enhanced factory (retry-capable AI client from config)

Downloader params

- api_url (mirrorable), timeout, proxies

Platform compatibility

- Windows console UTF-8 setup (chcp and redirection in main.py)

## 📦 Run & Deployment (brief)

- Local: Python 3.8+, install requirements.txt, set AI Keys, run run.py basic / advanced or GUI.
- Container: refer to Dockerfile and docker-compose (mount data, logs, config).
- For details see README.

## 🔒 Security, Extensibility & Roadmap (status labels)

Implemented

- Basic logging, file and config management
- AI Keys via env/config injection

Planned/Suggested (not yet implemented)

- Encrypted key storage and whitelisted HTTP client
- Downloader mirror rotation with exponential backoff
- Configurable concurrency/backoff/timeout/retry + CLI overrides
- MD naming include paper_id to prevent collisions
- Monitoring, health checks, service endpoints

## 📚 Glossary & Naming

- Basic analysis: download/clean/analyze, outputs daily JSON
- Advanced analysis: split/classify/summarize, outputs categorized MD and summary
- Rage Mode: concurrency=5 with real-time progress
- Cache hit (analysis): hit in PaperCacheManager
- CACHED skip (classification): same-name MD exists; e.g., if "safe-title.md" exists, rerun shows CACHED and skips. Force recompute by deleting the MD and rerun.
- Artifact paths: metadata/cleaned/reports/analysis_results

## 🗂️ Version Changes vs Legacy

- Naming: Fetcher → Downloader (MetadataDownloader)
- Data model: AnalysisResult split EN/ZH (title_en/title_zh, summary_en/summary_zh) with compat props
- Rage Mode: concurrency + incremental save; stronger cache hit/skip strategies
- “Blueprint” parts in legacy (encryption, whitelisted HTTP, monitoring, microservice) are now clearly labeled as Roadmap/Suggested to avoid confusion

## Appendix A: Module API Quick Reference

- MetadataDownloader.download(date) → metadata json path
- DataCleaner.clean(input_path) → cleaned json path
- PaperAnalyzer.analyze_batch / analyze_batch_concurrent(input) → report json path
- PaperClassifier.split_to_md(results, date_dir) → per-paper MDs
- PaperClassifier.classify_papers(date_dir) → categorized MDs
- PaperClassifier.generate_summary_report(date_dir) → classification_summary.md, classification_stats.json
- PaperCacheManager.get/put(key, value), purge_expired()

## Appendix B: Artifact naming & skip/dedupe

- Daily report: {date}\_report.json, append-per-item to be resilient to failures
- Classification MD: by Chinese title currently; collision-prone → recommendation safe_title\_\_{paper_id}.md
- Skip rules:
  - Analysis: skip processed IDs using existing daily report
  - Classification: mark CACHED if same-name MD exists; delete to force recompute

## Appendix C: Troubleshooting checklist

- Download failures: check network/proxy; switch or configure api_url mirror; raise timeout; retry basic.
- AI failures: confirm API Key env vars; check credits and rate limits; watch for 90s timeout; lower concurrency or run in batches.
- Filesystem: ensure data/ is writable; create missing directories; beware of long paths on Windows.
