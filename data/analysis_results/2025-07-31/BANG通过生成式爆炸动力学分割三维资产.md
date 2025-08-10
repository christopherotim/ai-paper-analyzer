# BANG：通过生成式爆炸动力学分割三维资产

**论文ID**：2507.21493
**英文标题**：BANG: Dividing 3D Assets via Generative Exploded Dynamics
**中文标题**：BANG：通过生成式爆炸动力学分割三维资产
**论文地址**：https://arxiv.org/abs/2507.21493

**作者团队**：Longwen Zhang, Qixuan Zhang, Haoran Jiang, Yinuo Bai, Wei Yang, Lan Xu, Jingyi Yu
**发表日期**：2025-07-29

**英文摘要**：
3D creation has always been a unique human strength, driven by our ability to
deconstruct and reassemble objects using our eyes, mind and hand. However,
current 3D design tools struggle to replicate this natural process, requiring
considerable artistic expertise and manual labor. This paper introduces BANG, a
novel generative approach that bridges 3D generation and reasoning, allowing
for intuitive and flexible part-level decomposition of 3D objects. At the heart
of BANG is "Generative Exploded Dynamics", which creates a smooth sequence of
exploded states for an input geometry, progressively separating parts while
preserving their geometric and semantic coherence.
  BANG utilizes a pre-trained large-scale latent diffusion model, fine-tuned
for exploded dynamics with a lightweight exploded view adapter, allowing
precise control over the decomposition process. It also incorporates a temporal
attention module to ensure smooth transitions and consistency across time. BANG
enhances control with spatial prompts, such as bounding boxes and surface
regions, enabling users to specify which parts to decompose and how. This
interaction can be extended with multimodal models like GPT-4, enabling
2D-to-3D manipulations for more intuitive and creative workflows.
  The capabilities of BANG extend to generating detailed part-level geometry,
associating parts with functional descriptions, and facilitating
component-aware 3D creation and manufacturing workflows. Additionally, BANG
offers applications in 3D printing, where separable parts are generated for
easy printing and reassembly. In essence, BANG enables seamless transformation
from imaginative concepts to detailed 3D assets, offering a new perspective on
creation that resonates with human intuition.

**中文摘要**：
三维创作一直是一种独特的人类优势，源于我们能够使用眼睛、心灵和手来解构和重新组装物体的能力。然而，当前的三维设计工具难以复制这一自然过程，需要相当的艺术专业知识和人工劳动。本文介绍了BANG，一种新颖的生成式方法，它连接了三维生成和推理，允许对三维对象进行直观且灵活的部分级分解。BANG的核心是"生成式爆炸动力学"，它为输入几何体创建一系列平滑的爆炸状态，在保持几何和语义一致性的同时逐步分离各个部分。BANG利用预训练的大规模潜在扩散模型，通过轻量级的爆炸视图适配器针对爆炸动力学进行了微调，从而能够精确控制分解过程。它还集成了一个时间注意力模块，确保时间上的平滑过渡和一致性。BANG通过空间提示（如边界框和表面区域）增强控制，使用户能够指定要分解的部分以及如何分解。这种交互可以通过GPT-4等多模态模型进行扩展，实现2D到3D的操作，以提供更直观和创造性的工作流程。BANG的能力扩展到生成详细的部分级几何体，将部分与功能描述相关联，并促进组件感知的三维创作和制造工作流程。此外，BANG在三维打印方面也有应用，可生成可分离的部分以便于打印和重新组装。本质上，BANG实现了从想象概念到详细三维资产的无缝转换，提供了一种与人类直觉共鸣的创作新视角。

**GitHub仓库**：暂无
**项目页面**：https://sites.google.com/view/bang7355608
**模型功能**：通过生成式爆炸动力学实现三维资产的部分级分解，支持精确控制和创造性工作流程

**分析时间**：2025-08-04T19:06:10.159608
