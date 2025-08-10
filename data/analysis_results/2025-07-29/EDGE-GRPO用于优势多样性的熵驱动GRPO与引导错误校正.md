# EDGE-GRPO：用于优势多样性的熵驱动GRPO与引导错误校正

**论文ID**：2507.21848
**英文标题**：EDGE-GRPO: Entropy-Driven GRPO with Guided Error Correction for   Advantage Diversity
**中文标题**：EDGE-GRPO：用于优势多样性的熵驱动GRPO与引导错误校正
**论文地址**：https://arxiv.org/abs/2507.21848

**作者团队**：Xingjian Zhang, Siwei Wen, Wenjun Wu, Lei Huang
**发表日期**：2025-07-29

**英文摘要**：
Large Language Models (LLMs) have made remarkable progress in enhancing
step-by-step reasoning through reinforcement learning. However, the Group
Relative Policy Optimization (GRPO) algorithm, which relies on sparse reward
rules, often encounters the issue of identical rewards within groups, leading
to the advantage collapse problem. Existing works typically address this
challenge from two perspectives: enforcing model reflection to enhance response
diversity, and introducing internal feedback to augment the training signal
(advantage). In this work, we begin by analyzing the limitations of model
reflection and investigating the policy entropy of responses at the
fine-grained sample level. Based on our experimental findings, we propose the
EDGE-GRPO algorithm, which adopts Entropy-Driven Advantage
and Guided Error Correction to effectively mitigate the
problem of advantage collapse. Extensive experiments on several main reasoning
benchmarks demonstrate the effectiveness and superiority of our approach. It is
available at https://github.com/ZhangXJ199/EDGE-GRPO.

**中文摘要**：
大型语言模型（LLMs）通过强化学习在增强逐步推理方面取得了显著进展。然而，依赖于稀疏奖励规则的组相对策略优化（GRPO）算法经常遇到组内奖励相同的问题，导致优势崩溃问题。现有工作通常从两个角度解决这一挑战：强制模型反思以提高响应多样性，以及引入内部反馈来增强训练信号（优势）。在这项工作中，我们首先分析了模型反思的局限性，并研究了细粒度样本级别上响应的策略熵。基于我们的实验发现，我们提出了EDGE-GRPO算法，该算法采用熵驱动优势和引导错误校正，有效缓解了优势崩溃问题。在几个主要推理基准上的大量实验证明了我们方法的有效性和优越性。它可在 https://github.com/ZhangXJ199/EDGE-GRPO 获取。

**GitHub仓库**：暂无
**项目页面**：暂无
**模型功能**：解决GRPO算法优势崩溃问题，通过熵驱动优势和引导错误校正提升模型推理能力和响应多样性。

**分析时间**：2025-08-04T19:55:17.733920
