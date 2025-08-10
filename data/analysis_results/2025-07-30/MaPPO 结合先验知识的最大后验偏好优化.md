# MaPPO: 结合先验知识的最大后验偏好优化

**论文ID**：2507.21183
**英文标题**：MaPPO: Maximum a Posteriori Preference Optimization with Prior Knowledge
**中文标题**：MaPPO: 结合先验知识的最大后验偏好优化
**论文地址**：https://arxiv.org/abs/2507.21183

**作者团队**：Guangchen Lan, Sipeng Zhang, Tianle Wang, Yuwei Zhang, Daoan Zhang, Xinpeng Wei, Xiaoman Pan, Hongming Zhang, Dong-Jun Han, Christopher G. Brinton
**发表日期**：2025-07-27

**英文摘要**：
As the era of large language models (LLMs) on behalf of users unfolds,
Preference Optimization (PO) methods have become a central approach to aligning
LLMs with human preferences and improving performance. We propose Maximum a
Posteriori Preference Optimization (MaPPO), a framework for learning from
preferences that explicitly incorporates prior reward knowledge into the
optimization objective. While existing methods such as Direct Preference
Optimization (DPO) and its variants treat preference learning as a Maximum
Likelihood Estimation (MLE) problem, MaPPO extends this paradigm by integrating
prior reward estimates into a principled Maximum a Posteriori (MaP) objective.
This not only generalizes DPO and its variants, but also enhances alignment by
mitigating the oversimplified binary classification of responses. More
importantly, MaPPO introduces no additional hyperparameter, and supports
preference optimization in both offline and online settings. In addition, MaPPO
can be used as a plugin with consistent improvement on DPO variants, including
widely used SimPO, IPO, and CPO. Extensive empirical evaluations of different
model sizes and model series on three standard benchmarks, including MT-Bench,
AlpacaEval 2.0, and Arena-Hard, demonstrate consistent improvements in
alignment performance without sacrificing computational efficiency.

**中文摘要**：
随着代表用户的大型语言模型(LLMs)时代的展开，偏好优化(PO)方法已成为使LLMs与人类偏好保持一致并提高性能的核心方法。我们提出了最大后验偏好优化(MaPPO)，这是一个从偏好中学习的框架，明确地将先验奖励知识整合到优化目标中。虽然现有的方法如直接偏好优化(DPO)及其变体将偏好学习视为最大似然估计(MLE)问题，但MaPPO通过将先验奖励估计整合到有原则的最大后验(MaP)目标中扩展了这一范式。这不仅推广了DPO及其变体，还通过减轻对响应的过度简化二元分类来增强对齐。更重要的是，MaPPO不引入额外的超参数，并支持离线和在线设置下的偏好优化。此外，MaPPO可以作为插件使用，对DPO变体(包括广泛使用的SimPO、IPO和CPO)提供一致的改进。在不同模型大小和模型系列上的广泛经验评估，包括在MT-Bench、AlpacaEval 2.0和Arena-Hard三个标准基准测试上，证明了在不牺牲计算效率的情况下对齐性能的一致提升。

**GitHub仓库**：暂无
**项目页面**：暂无
**模型功能**：结合先验知识的偏好优化方法，提升LLMs与人类偏好对齐，无需额外超参数支持离线和在线场景。

**分析时间**：2025-08-04T19:21:04.733103
