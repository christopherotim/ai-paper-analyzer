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