# X-Omni：强化学习让离散自回归图像生成模型再次强大

**论文ID**：2507.22058
**英文标题**：X-Omni: Reinforcement Learning Makes Discrete Autoregressive Image   Generative Models Great Again
**中文标题**：X-Omni：强化学习让离散自回归图像生成模型再次强大
**论文地址**：https://arxiv.org/abs/2507.22058

**作者团队**：Zigang Geng, Yibing Wang, Yeyao Ma, Chen Li, Yongming Rao, Shuyang Gu, Zhao Zhong, Qinglin Lu, Han Hu, Xiaosong Zhang, Linus, Di Wang, Jie Jiang
**发表日期**：2025-07-29

**英文摘要**：
Numerous efforts have been made to extend the ``next token prediction''
paradigm to visual contents, aiming to create a unified approach for both image
generation and understanding. Nevertheless, attempts to generate images through
autoregressive modeling with discrete tokens have been plagued by issues such
as low visual fidelity, distorted outputs, and failure to adhere to complex
instructions when rendering intricate details. These shortcomings are likely
attributed to cumulative errors during autoregressive inference or information
loss incurred during the discretization process. Probably due to this
challenge, recent research has increasingly shifted toward jointly training
image generation with diffusion objectives and language generation with
autoregressive objectives, moving away from unified modeling approaches. In
this work, we demonstrate that reinforcement learning can effectively mitigate
artifacts and largely enhance the generation quality of a discrete
autoregressive modeling method, thereby enabling seamless integration of image
and language generation. Our framework comprises a semantic image tokenizer, a
unified autoregressive model for both language and images, and an offline
diffusion decoder for image generation, termed X-Omni. X-Omni achieves
state-of-the-art performance in image generation tasks using a 7B language
model, producing images with high aesthetic quality while exhibiting strong
capabilities in following instructions and rendering long texts.

**中文摘要**：
已经付出了大量努力将"下一个令牌预测"范式扩展到视觉内容，旨在为图像生成和理解创建统一的方法。然而，通过离散令牌的自回归建模尝试生成图像一直受到诸如低视觉保真度、输出失真以及渲染复杂细节时无法遵循复杂指令等问题困扰。这些缺点可能归因于自回归推理过程中的累积误差或离散化过程中造成的信息损失。可能正是因为这一挑战，最近的研究越来越多地转向联合训练图像生成（使用扩散目标）和语言生成（使用自回归目标），逐渐远离统一的建模方法。在这项工作中，我们证明了强化学习可以有效减轻伪影并显著提高离散自回归建模方法的生成质量，从而实现图像和语言生成的无缝集成。我们的框架包括一个语义图像标记器、一个用于语言和图像的统一自回归模型，以及一个用于图像生成的离线扩散解码器，称为X-Omni。X-Omni在使用7B语言模型的图像生成任务中实现了最先进的性能，生成具有高美学质量的图像，同时展现出遵循指令和渲染长文本的强大能力。

**GitHub仓库**：https://github.com/X-Omni-Team/X-Omni
**项目页面**：https://x-omni-team.github.io
**模型功能**：结合强化学习的离散自回归图像生成模型，实现高质量图像生成与语言图像统一生成。

**分析时间**：2025-08-04T19:21:00.919386
