# NeRF是3D高斯溅射的有价值助手

**论文ID**：2507.23374
**英文标题**：NeRF Is a Valuable Assistant for 3D Gaussian Splatting
**中文标题**：NeRF是3D高斯溅射的有价值助手
**论文地址**：https://arxiv.org/abs/2507.23374

**作者团队**：Shuangkang Fang, I-Chao Shen, Takeo Igarashi, Yufeng Wang, ZeSheng Wang, Yi Yang, Wenrui Ding, Shuchang Zhou
**发表日期**：2025-07-31

**英文摘要**：
We introduce NeRF-GS, a novel framework that jointly optimizes Neural
Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS). This framework
leverages the inherent continuous spatial representation of NeRF to mitigate
several limitations of 3DGS, including sensitivity to Gaussian initialization,
limited spatial awareness, and weak inter-Gaussian correlations, thereby
enhancing its performance. In NeRF-GS, we revisit the design of 3DGS and
progressively align its spatial features with NeRF, enabling both
representations to be optimized within the same scene through shared 3D spatial
information. We further address the formal distinctions between the two
approaches by optimizing residual vectors for both implicit features and
Gaussian positions to enhance the personalized capabilities of 3DGS.
Experimental results on benchmark datasets show that NeRF-GS surpasses existing
methods and achieves state-of-the-art performance. This outcome confirms that
NeRF and 3DGS are complementary rather than competing, offering new insights
into hybrid approaches that combine 3DGS and NeRF for efficient 3D scene
representation.

**中文摘要**：
我们提出了NeRF-GS，一种联合优化神经辐射场(NeRF)和3D高斯溅射(3DGS)的新颖框架。该框架利用NeRF固有的连续空间表示来缓解3DGS的几个局限性，包括对高斯初始化的敏感性、有限的空间感知能力和弱高斯间相关性，从而提高其性能。在NeRF-GS中，我们重新审视了3DGS的设计，并逐步将其空间特征与NeRF对齐，通过共享的3D空间信息使两种表示能够在同一场景内进行优化。我们进一步通过优化隐式特征和高斯位置的残差向量来解决两种方法之间的形式差异，以增强3DGS的个性化能力。在基准数据集上的实验结果表明，NeRF-GS超越了现有方法并取得了最先进的性能。这一结果证实了NeRF和3DGS是互补而非竞争关系，为结合3DGS和NeRF的高效3D场景表示的混合方法提供了新的见解。

**GitHub仓库**：暂无
**项目页面**：暂无
**模型功能**：联合优化NeRF和3DGS，利用NeRF的连续空间表示增强3DGS性能，实现互补的高效3D场景表示。

**技术特点**：提出NeRF-GS框架首次联合优化NeRF和3DGS，通过共享3D空间信息使两种表示在同一场景内协同优化，解决了3DGS对高斯初始化敏感、空间感知有限和弱高斯间相关性的问题；通过优化隐式特征和高斯位置的残差向量，增强了3DGS的个性化能力。

**应用场景**：高质量3D场景重建与可视化，适用于文化遗产数字化和建筑可视化；虚拟现实和增强现实内容创作，为沉浸式体验提供更真实的3D环境；电影和游戏产业中的3D资产生成，加速虚拟场景和角色的创建流程。

**分析时间**：2025-08-04T17:49:16.497628