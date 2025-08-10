# MoHoBench：通过不可回答的视觉问题评估多模态大语言模型的诚实性

**论文ID**：2507.21503
**英文标题**：MoHoBench: Assessing Honesty of Multimodal Large Language Models via   Unanswerable Visual Questions
**中文标题**：MoHoBench：通过不可回答的视觉问题评估多模态大语言模型的诚实性
**论文地址**：https://arxiv.org/abs/2507.21503

**作者团队**：Yanxu Zhu, Shitong Duan, Xiangxu Zhang, Jitao Sang, Peng Zhang, Tun Lu, Xiao Zhou, Jing Yao, Xiaoyuan Yi, Xing Xie
**发表日期**：2025-07-29

**英文摘要**：
Recently Multimodal Large Language Models (MLLMs) have achieved considerable
advancements in vision-language tasks, yet produce potentially harmful or
untrustworthy content. Despite substantial work investigating the
trustworthiness of language models, MMLMs' capability to act honestly,
especially when faced with visually unanswerable questions, remains largely
underexplored. This work presents the first systematic assessment of honesty
behaviors across various MLLMs. We ground honesty in models' response behaviors
to unanswerable visual questions, define four representative types of such
questions, and construct MoHoBench, a large-scale MMLM honest benchmark,
consisting of 12k+ visual question samples, whose quality is guaranteed by
multi-stage filtering and human verification. Using MoHoBench, we benchmarked
the honesty of 28 popular MMLMs and conducted a comprehensive analysis. Our
findings show that: (1) most models fail to appropriately refuse to answer when
necessary, and (2) MMLMs' honesty is not solely a language modeling issue, but
is deeply influenced by visual information, necessitating the development of
dedicated methods for multimodal honesty alignment. Therefore, we implemented
initial alignment methods using supervised and preference learning to improve
honesty behavior, providing a foundation for future work on trustworthy MLLMs.
Our data and code can be found at https://github.com/DSTTSD/MoHoBench.

**中文摘要**：
最近，多模态大语言模型(MLLMs)在视觉语言任务方面取得了显著进展，但可能产生有害或不可信的内容。尽管有大量工作研究语言模型的可信度，但MLLMs在面临视觉不可回答问题时表现出的诚实能力在很大程度上仍未得到充分探索。这项工作首次对各种MLLMs的诚实行为进行了系统性评估。我们将诚实性基于模型对不可回答视觉问题的响应行为，定义了四种代表性的此类问题，并构建了MoHoBench，一个大规模的MLLM诚实性基准，包含12k+个视觉问题样本，其质量通过多阶段过滤和人工验证得到保证。使用MoHoBench，我们对28个流行的MLLMs的诚实性进行了基准测试，并进行了全面分析。我们的发现显示：(1)大多数模型在必要时未能适当拒绝回答，以及(2)MLLMs的诚实性不仅仅是一个语言建模问题，而是深受视觉信息的影响，这需要开发专门的多模态诚实性对齐方法。因此，我们使用监督学习和偏好学习实施了初步的对齐方法，以改善诚实性行为，为未来可信MLLMs的工作奠定了基础。我们的数据和代码可以在https://github.com/DSTTSD/MoHoBench找到。

**GitHub仓库**：https://github.com/DSTTSD/MoHoBench
**项目页面**：暂无
**模型功能**：评估多模态大语言模型面对视觉不可回答问题时的诚实性，提高模型可靠性。

**分析时间**：2025-08-04T19:21:15.887443
