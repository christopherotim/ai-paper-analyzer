# ForCenNet: 前景中心网络用于文档图像校正

**论文ID**：2507.19804
**英文标题**：ForCenNet: Foreground-Centric Network for Document Image Rectification
**中文标题**：ForCenNet: 前景中心网络用于文档图像校正
**论文地址**：https://arxiv.org/abs/2507.19804

**作者团队**：Peng Cai, Qiang Li, Kaicheng Yang, Dong Guo, Jia Li, Nan Zhou, Xiang An, Ninghua Yang, Jiankang Deng
**发表日期**：2025-07-26

**英文摘要**：
Document image rectification aims to eliminate geometric deformation in
photographed documents to facilitate text recognition. However, existing
methods often neglect the significance of foreground elements, which provide
essential geometric references and layout information for document image
correction. In this paper, we introduce Foreground-Centric Network (ForCenNet)
to eliminate geometric distortions in document images. Specifically, we
initially propose a foreground-centric label generation method, which extracts
detailed foreground elements from an undistorted image. Then we introduce a
foreground-centric mask mechanism to enhance the distinction between readable
and background regions. Furthermore, we design a curvature consistency loss to
leverage the detailed foreground labels to help the model understand the
distorted geometric distribution. Extensive experiments demonstrate that
ForCenNet achieves new state-of-the-art on four real-world benchmarks, such as
DocUNet, DIR300, WarpDoc, and DocReal. Quantitative analysis shows that the
proposed method effectively undistorts layout elements, such as text lines and
table borders. The resources for further comparison are provided at
https://github.com/caipeng328/ForCenNet.

**中文摘要**：
文档图像校正旨在消除拍摄文档中的几何变形，以便于文本识别。然而，现有方法常常忽略前景元素的重要性，这些元素为文档图像校正提供了必要的几何参考和布局信息。在本文中，我们引入了前景中心网络(ForCenNet)来消除文档图像中的几何失真。具体而言，我们首先提出了一种前景中心标签生成方法，该方法从未失真图像中提取详细的前景元素。然后，我们引入了一种前景中心掩码机制，以增强可读区域和背景区域之间的区分度。此外，我们设计了一种曲率一致性损失，利用详细的前景标签来帮助模型理解失真的几何分布。大量实验表明，ForCenNet在DocUNet、DIR300、WarpDoc和DocReal四个真实世界基准测试上取得了新的最先进性能。定量分析表明，所提出的方法能够有效校正布局元素，如文本行和表格边框。进一步比较的资源可在https://github.com/caipeng328/ForCenNet获取。

**GitHub仓库**：https://github.com/caipeng328/ForCenNet
**项目页面**：暂无
**模型功能**：ForCenNet是一个专注于前景元素的文档图像校正网络，通过提取前景参考信息消除文档图像中的几何变形，提升文本识别效果。

**分析时间**：2025-08-04T19:55:13.845872
