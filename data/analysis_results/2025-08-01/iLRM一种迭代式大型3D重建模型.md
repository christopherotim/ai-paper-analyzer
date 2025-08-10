# iLRM：一种迭代式大型3D重建模型

**论文ID**：2507.23277
**英文标题**：iLRM: An Iterative Large 3D Reconstruction Model
**中文标题**：iLRM：一种迭代式大型3D重建模型
**论文地址**：https://arxiv.org/abs/2507.23277

**作者团队**：Gyeongjin Kang, Seungtae Nam, Xiangyu Sun, Sameh Khamis, Abdelrahman Mohamed, Eunbyung Park
**发表日期**：2025-07-31

**英文摘要**：
Feed-forward 3D modeling has emerged as a promising approach for rapid and
high-quality 3D reconstruction. In particular, directly generating explicit 3D
representations, such as 3D Gaussian splatting, has attracted significant
attention due to its fast and high-quality rendering, as well as numerous
applications. However, many state-of-the-art methods, primarily based on
transformer architectures, suffer from severe scalability issues because they
rely on full attention across image tokens from multiple input views, resulting
in prohibitive computational costs as the number of views or image resolution
increases. Toward a scalable and efficient feed-forward 3D reconstruction, we
introduce an iterative Large 3D Reconstruction Model (iLRM) that generates 3D
Gaussian representations through an iterative refinement mechanism, guided by
three core principles: (1) decoupling the scene representation from input-view
images to enable compact 3D representations; (2) decomposing fully-attentional
multi-view interactions into a two-stage attention scheme to reduce
computational costs; and (3) injecting high-resolution information at every
layer to achieve high-fidelity reconstruction. Experimental results on widely
used datasets, such as RE10K and DL3DV, demonstrate that iLRM outperforms
existing methods in both reconstruction quality and speed. Notably, iLRM
exhibits superior scalability, delivering significantly higher reconstruction
quality under comparable computational cost by efficiently leveraging a larger
number of input views.

**中文摘要**：
前馈3D建模已成为一种快速高质量3D重建的前沿方法。特别是，直接生成显式3D表示（如3D高斯泼溅）因其快速高质量的渲染效果以及众多应用场景而受到广泛关注。然而，许多最先进的方法主要基于Transformer架构，存在严重的可扩展性问题，因为它们依赖于跨多个输入视图的图像令牌的全注意力机制，导致随着视图数量或图像分辨率的增加，计算成本变得过高。为了实现可扩展且高效的前馈3D重建，我们引入了一种迭代式大型3D重建模型(iLRM)，该模型通过迭代细化机制生成3D高斯表示，并遵循三个核心原则：(1)将场景表示与输入视图图像解耦，以实现紧凑的3D表示；(2)将全注意力的多视图交互分解为两阶段注意力方案，以降低计算成本；(3)在每个层注入高分辨率信息，以实现高保真度的重建。在RE10K和DL3DV等常用数据集上的实验结果表明，iLRM在重建质量和速度方面均优于现有方法。值得注意的是，iLRM表现出卓越的可扩展性，通过有效利用更多的输入视图，在可比的计算成本下提供显著更高的重建质量。

**GitHub仓库**：https://github.com/Gynjn/iLRM
**项目页面**：https://gynjn.github.io/iLRM/
**模型功能**：迭代式3D重建模型，通过两阶段注意力方案实现高质量、高效率的3D高斯表示重建

**分析时间**：2025-08-04T17:48:06.333775
