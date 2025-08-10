# VL-Cogito：面向高级多模态推理的渐进式课程强化学习

**论文ID**：2507.22607
**英文标题**：VL-Cogito: Progressive Curriculum Reinforcement Learning for Advanced Multimodal Reasoning
**中文标题**：VL-Cogito：面向高级多模态推理的渐进式课程强化学习
**论文地址**：https://arxiv.org/abs/2507.22607

**作者团队**：Ruifeng Yuan, Chenghao Xiao, Sicong Leng, Jianyu Wang, Long Li, Weiwen Xu, Hou Pong Chan, Deli Zhao, Tingyang Xu, Zhongyu Wei, Hao Zhang, Yu Rong
**发表日期**：2025-07-30

**英文摘要**：
Reinforcement learning has proven its effectiveness in enhancing the reasoning capabilities of large language models. Recent research efforts have progressively extended this paradigm to multimodal reasoning tasks. Due to the inherent complexity and diversity of multimodal tasks, especially in semantic content and problem formulations, existing models often exhibit unstable performance across various domains and difficulty levels. To address these limitations, we propose VL-Cogito, an advanced multimodal reasoning model trained via a novel multi-stage Progressive Curriculum Reinforcement Learning (PCuRL) framework. PCuRL systematically guides the model through tasks of gradually increasing difficulty, substantially improving its reasoning abilities across diverse multimodal contexts. The framework introduces two key innovations: (1) an online difficulty soft weighting mechanism, dynamically adjusting training difficulty across successive RL training stages; and (2) a dynamic length reward mechanism, which encourages the model to adaptively regulate its reasoning path length according to task complexity, thus balancing reasoning efficiency with correctness. Experimental evaluations demonstrate that VL-Cogito consistently matches or surpasses existing reasoning-oriented models across mainstream multimodal benchmarks spanning mathematics, science, logic, and general understanding, validating the effectiveness of our approach.

**中文摘要**：
强化学习已被证明在提升大型语言模型的推理能力方面具有有效性。最近的研究工作已逐步将这一范式扩展到多模态推理任务中。由于多模态任务固有的复杂性和多样性，特别是在语义内容和问题表述方面，现有模型通常在不同领域和难度水平上表现出不稳定的表现。为解决这些局限性，我们提出了VL-Cogito，这是一个通过新颖的多阶段渐进式课程强化学习(PCuRL)框架训练的高级多模态推理模型。PCuRL系统性地引导模型逐步完成难度递增的任务，显著提高了其在多样化多模态环境中的推理能力。该框架引入了两个关键创新：(1)在线难度软加权机制，在连续的RL训练阶段动态调整训练难度；(2)动态长度奖励机制，鼓励模型根据任务复杂度自适应调节其推理路径长度，从而平衡推理效率与正确性。实验评估表明，VL-Cogito在跨越数学、科学、逻辑和通用理解等主流多模态基准测试中，持续匹配或超越现有面向推理的模型，验证了我们方法的有效性。

**GitHub仓库**：暂无
**项目页面**：暂无
**模型功能**：通过渐进式课程强化学习提升多模态推理能力，平衡推理效率与正确性，适用于数学、科学、逻辑等多领域任务

**技术特点**：提出多阶段渐进式课程强化学习(PCuRL)框架，系统引导模型完成难度递增任务；创新性地引入在线难度软加权机制，动态调整训练难度；设计动态长度奖励机制，使模型能根据任务复杂度自适应调节推理路径长度，平衡推理效率与正确性。

**应用场景**：教育领域智能辅导，解决数学、科学等学科的多模态问题；专业咨询领域，为医疗、法律等提供基于多模态数据的推理分析；智能助手应用，在通用理解场景中帮助用户分析和解决复杂的多模态问题。

**分析时间**：2025-08-04T19:06:08.149686