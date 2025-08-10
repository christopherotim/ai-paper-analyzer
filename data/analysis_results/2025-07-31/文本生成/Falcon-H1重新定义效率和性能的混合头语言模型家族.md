# Falcon-H1：重新定义效率和性能的混合头语言模型家族

**论文ID**：2507.22448
**英文标题**：Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance
**中文标题**：Falcon-H1：重新定义效率和性能的混合头语言模型家族
**论文地址**：https://arxiv.org/abs/2507.22448

**作者团队**：Jingwei Zuo, Maksim Velikanov, Ilyas Chahed, Younes Belkada, Dhia Eddine Rhayem, Guillaume Kunsch, Hakim Hacid, Hamza Yous, Brahim Farhat, Ibrahim Khadraoui, Mugariya Farooq, Giulia Campesan, Ruxandra Cojocaru, Yasser Djilali, Shi Hu, Iheb Chaabane, Puneesh Khanna, Mohamed El Amine Seddik, Ngoc Dung Huynh, Phuc Le Khac, Leen AlQadi, Billel Mokeddem, Mohamed Chami, Abdalgader Abubaker, Mikhail Lubinets, Kacper Piskorski, Slim Frikha
**发表日期**：2025-07-30

**英文摘要**：
In this report, we introduce Falcon-H1, a new series of large language models
(LLMs) featuring hybrid architecture designs optimized for both high
performance and efficiency across diverse use cases. Unlike earlier Falcon
models built solely on Transformer or Mamba architectures, Falcon-H1 adopts a
parallel hybrid approach that combines Transformer-based attention with State
Space Models (SSMs), known for superior long-context memory and computational
efficiency. We systematically revisited model design, data strategy, and
training dynamics, challenging conventional practices in the field. Falcon-H1
is released in multiple configurations, including base and instruction-tuned
variants at 0.5B, 1.5B, 1.5B-deep, 3B, 7B, and 34B parameters. Quantized
instruction-tuned models are also available, totaling over 30 checkpoints on
HF Mirror Hub. Falcon-H1 models demonstrate state-of-the-art performance and
exceptional parameter and training efficiency. The flagship Falcon-H1-34B
matches or outperforms models up to 70B scale, such as Qwen3-32B, Qwen2.5-72B,
and Llama3.3-70B, while using fewer parameters and less data. Smaller models
show similar trends: the Falcon-H1-1.5B-Deep rivals current leading 7B-10B
models, and Falcon-H1-0.5B performs comparably to typical 7B models from 2024.
These models excel across reasoning, mathematics, multilingual tasks,
instruction following, and scientific knowledge. With support for up to 256K
context tokens and 18 languages, Falcon-H1 is suitable for a wide range of
applications. All models are released under a permissive open-source license,
underscoring our commitment to accessible and impactful AI research.

**中文摘要**：
在本报告中，我们介绍了Falcon-H1，这是一系列新型大型语言模型(LLMs)，采用混合架构设计，针对不同用例的高性能和效率进行了优化。与仅基于Transformer或Mamba架构构建的早期Falcon模型不同，Falcon-H1采用并行混合方法，结合了基于Transformer的注意力机制和状态空间模型(SSMs)，后者以其卓越的长上下文记忆和计算效率而闻名。我们系统性地重新审视了模型设计、数据策略和训练动态，挑战了该领域的传统实践。Falcon-H1以多种配置发布，包括0.5B、1.5B、1.5B-deep、3B、7B和34B参数的基础和指令微调版本。也可使用量化指令微调模型，在HF Mirror Hub上总共提供超过30个检查点。Falcon-H1模型展示了最先进的性能和卓越的参数和训练效率。旗舰模型Falcon-H1-34B匹配或超越了高达70B规模的模型，如Qwen3-32B、Qwen2.5-72B和Llama3.3-70B，同时使用更少的参数和更少的数据。较小的模型也显示出类似的趋势：Falcon-H1-1.5B-Deep可与当前领先的7B-10B模型相媲美，而Falcon-H1-0.5B的性能与2024年的典型7B模型相当。这些模型在推理、数学、多语言任务、指令遵循和科学知识方面表现出色。凭借对高达256K上下文标记和18种语言的支持，Falcon-H1适用于广泛的应用场景。所有模型均在宽松的开源许可证下发布，彰显了我们对可访问且影响深远的AI研究的承诺。

**GitHub仓库**：https://github.com/tiiuae/Falcon-H1/
**项目页面**：https://tiiuae.github.io/Falcon-H1/
**模型功能**：混合架构大型语言模型，结合Transformer与SSM，实现高性能与高效率的平衡。

**技术特点**：采用并行混合架构，结合Transformer注意力机制与状态空间模型(SSMs)，实现高性能与高效率的平衡；通过系统性重新审视模型设计、数据策略和训练动态，挑战了传统LLM设计实践；相比传统架构，使用更少的参数和训练数据就能达到甚至超越更大规模模型的性能。

**应用场景**：长文本处理与分析：支持高达256K上下文标记，适合处理长文档、法律文件、学术论文等；多语言应用与服务：支持18种语言，可应用于跨语言翻译、多语言客服、国际化内容创作；专业知识领域应用：在科学知识、推理和数学任务上表现出色，可应用于科研辅助、教育辅导、专业咨询。

**分析时间**：2025-08-04T19:06:12.915292