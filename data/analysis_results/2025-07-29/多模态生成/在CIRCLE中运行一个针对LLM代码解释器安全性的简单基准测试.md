# 代码生成与数据增强

# 在CIRCLE中运行？一个针对LLM代码解释器安全性的简单基准测试

**论文ID**：2507.19399
**英文标题**：Running in CIRCLE? A Simple Benchmark for LLM Code Interpreter Security
**中文标题**：在CIRCLE中运行？一个针对LLM代码解释器安全性的简单基准测试
**论文地址**：https://arxiv.org/abs/2507.19399

**作者团队**：Gabriel Chua
**发表日期**：2025-07-25

**英文摘要**：
As large language models (LLMs) increasingly integrate native code
interpreters, they enable powerful real-time execution capabilities,
substantially expanding their utility. However, such integrations introduce
potential system-level cybersecurity threats, fundamentally different from
prompt-based vulnerabilities. To systematically evaluate these
interpreter-specific risks, we propose CIRCLE (Code-Interpreter Resilience
Check for LLM Exploits), a simple benchmark comprising 1,260 prompts targeting
CPU, memory, and disk resource exhaustion. Each risk category includes
explicitly malicious ("direct") and plausibly benign ("indirect") prompt
variants. Our automated evaluation framework assesses not only whether LLMs
refuse or generates risky code, but also executes the generated code within the
interpreter environment to evaluate code correctness, simplifications made by
the LLM to make the code safe, or execution timeouts. Evaluating 7 commercially
available models from OpenAI and Google, we uncover significant and
inconsistent vulnerabilities. For instance, evaluations show substantial
disparities even within providers - OpenAI's o4-mini correctly refuses risky
requests at 7.1%, notably higher rates compared to GPT-4.1 at 0.5%. Results
particularly underscore that indirect, socially-engineered prompts
substantially weaken model defenses. This highlights an urgent need for
interpreter-specific cybersecurity benchmarks, dedicated mitigation tools
(e.g., guardrails), and clear industry standards to guide safe and responsible
deployment of LLM interpreter integrations. The benchmark dataset and
evaluation code are publicly released to foster further research.

**中文摘要**：
随着大型语言模型(LLMs)越来越多地集成原生代码解释器，它们能够实现强大的实时执行能力，大大扩展了它们的实用性。然而，这种集成引入了潜在的系统性网络安全威胁，这些威胁与基于提示的漏洞有根本不同。为了系统性地评估这些特定于解释器的风险，我们提出了CIRCLE（针对LLM漏洞的代码解释器弹性检查），这是一个包含1260个提示的简单基准测试，这些提示针对CPU、内存和磁盘资源耗尽。每个风险类别都包含明确的恶意("直接")和看似良性("间接")的提示变体。我们的自动化评估框架不仅评估LLM是否拒绝或生成有风险的代码，还在解释器环境中执行生成的代码，以评估代码的正确性、LLM为使代码安全所做的简化或执行超时。评估了OpenAI和Google的7个商业可用模型，我们发现存在显著且不一致的漏洞。例如，评估显示，即使在提供商内部也存在巨大差异——OpenAI的o4-mini正确拒绝风险请求的比例为7.1%，明显高于GPT-4.1的0.5%。结果特别强调，间接的、社会工程学的提示显著削弱了模型的防御能力。这突显了对特定于解释器的网络安全基准测试、专门的缓解工具（例如护栏）以及明确的行业标准的迫切需求，以指导LLM解释器集成的安全和负责任的部署。基准测试数据集和评估代码已公开发布，以促进进一步的研究。

**GitHub仓库**：暂无
**项目页面**：暂无
**模型功能**：评估LLM代码解释器防御资源耗尽攻击的能力，包括直接和间接提示变体。

**技术特点**：CIRCLE基准测试首创性地将直接恶意提示和间接社会工程学提示相结合，全面评估LLM代码解释器面对资源耗尽攻击时的防御能力；自动化评估框架不仅检测代码拒绝情况，还执行生成的代码以评估实际安全效果，突破了传统仅基于文本分析的评估局限。

**应用场景**：LLM代码解释器的安全漏洞检测与修复；开发针对代码解释器的安全防护工具和护栏系统；制定企业级LLM解释器集成的安全标准和最佳实践指南。

**分析时间**：2025-08-04T19:55:27.369131