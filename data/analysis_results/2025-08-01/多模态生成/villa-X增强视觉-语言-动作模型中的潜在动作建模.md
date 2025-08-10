# villa-X：增强视觉-语言-动作模型中的潜在动作建模

**论文ID**：2507.23682
**英文标题**：villa-X: Enhancing Latent Action Modeling in Vision-Language-Action Models
**中文标题**：villa-X：增强视觉-语言-动作模型中的潜在动作建模
**论文地址**：https://arxiv.org/abs/2507.23682

**作者团队**：Xiaoyu Chen, Hangxing Wei, Pushi Zhang, Chuheng Zhang, Kaixin Wang, Yanjiang Guo, Rushuai Yang, Yucen Wang, Xinquan Xiao, Li Zhao, Jianyu Chen, Jiang Bian
**发表日期**：2025-07-31

**英文摘要**：
Visual-Language-Action (VLA) models have emerged as a popular paradigm for learning robot manipulation policies that can follow language instructions and generalize to novel scenarios. Recent work has begun to explore the incorporation of latent actions, an abstract representation of visual change between two frames, into VLA pre-training. In this paper, we introduce villa-X, a novel Visual-Language-Latent-Action (ViLLA) framework that advances latent action modeling for learning generalizable robot manipulation policies. Our approach improves both how latent actions are learned and how they are incorporated into VLA pre-training. Together, these contributions enable villa-X to achieve superior performance across simulated environments including SIMPLER and LIBERO, as well as on two real-world robot setups including gripper and dexterous hand manipulation. We believe the ViLLA paradigm holds significant promise, and that our villa-X provides a strong foundation for future research.

**中文摘要**：
视觉-语言-动作（VLA）模型已经成为一种流行的范式，用于学习能够遵循语言指令并泛化到新场景的机器人操作策略。最近的工作开始探索将潜在动作（两帧之间视觉变化的抽象表示）纳入VLA预训练中。在本文中，我们介绍了villa-X，这是一种新颖的视觉-语言-潜在动作（ViLLA）框架，它改进了潜在动作建模，用于学习可泛化的机器人操作策略。我们的方法改进了潜在动作的学习方式以及它们如何被纳入VLA预训练。这些贡献共同使villa-X能够在包括SIMPLER和LIBERO在内的模拟环境以及包括夹爪和灵巧手操作在内的两个真实机器人设置上实现卓越性能。我们认为ViLLA范式具有巨大潜力，而我们的villa-X为未来研究提供了坚实的基础。

**GitHub仓库**：https://github.com/microsoft/villa-x/
**项目页面**：https://microsoft.github.io/villa-x/
**模型功能**：改进潜在动作建模，实现可泛化的机器人操作策略，遵循语言指令并适应新场景。

**技术特点**：villa-X框架创新性地改进了潜在动作的学习方式，通过引入视觉-语言-潜在动作（ViLLA）范式，将两帧间视觉变化的抽象表示更有效地整合到模型中。该方法同时优化了潜在动作如何被纳入VLA预训练的过程，使模型能够学习更泛化的机器人操作策略，在模拟和真实环境中均表现出色。

**应用场景**：1. 工业自动化中的精密装配任务，如电子元件的抓取和放置；2. 家庭服务机器人执行日常物品操作，如整理桌面、收纳物品；3. 康复训练辅助系统，通过语言指令引导患者进行手部康复动作训练。

**分析时间**：2025-08-04T17:48:25.597131