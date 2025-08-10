# MIRepNet：一种基于脑电图的运动想象分类流水线与基础模型

**论文ID**：2507.20254
**英文标题**：MIRepNet: A Pipeline and Foundation Model for EEG-Based Motor Imagery   Classification
**中文标题**：MIRepNet：一种基于脑电图的运动想象分类流水线与基础模型
**论文地址**：https://arxiv.org/abs/2507.20254

**作者团队**：Dingkun Liu, Zhu Chen, Jingwei Luo, Shijie Lian, Dongrui Wu
**发表日期**：2025-07-27

**英文摘要**：
Brain-computer interfaces (BCIs) enable direct communication between the
brain and external devices. Recent EEG foundation models aim to learn
generalized representations across diverse BCI paradigms. However, these
approaches overlook fundamental paradigm-specific neurophysiological
distinctions, limiting their generalization ability. Importantly, in practical
BCI deployments, the specific paradigm such as motor imagery (MI) for stroke
rehabilitation or assistive robotics, is generally determined prior to data
acquisition. This paper proposes MIRepNet, the first EEG foundation model
tailored for the MI paradigm. MIRepNet comprises a high-quality EEG
preprocessing pipeline incorporating a neurophysiologically-informed channel
template, adaptable to EEG headsets with arbitrary electrode configurations.
Furthermore, we introduce a hybrid pretraining strategy that combines
self-supervised masked token reconstruction and supervised MI classification,
facilitating rapid adaptation and accurate decoding on novel downstream MI
tasks with fewer than 30 trials per class. Extensive evaluations across five
public MI datasets demonstrated that MIRepNet consistently achieved
state-of-the-art performance, significantly outperforming both specialized and
generalized EEG models. Our code will be available on
GitHubhttps://github.com/staraink/MIRepNet.

**中文摘要**：
脑机接口(BCIs)实现大脑与外部设备之间的直接通信。最近的脑电图(EEG)基础模型旨在学习跨多种BCI范式的通用表征。然而，这些方法忽视了范式特定的基本神经生理学差异，限制了它们的泛化能力。重要的是，在实际的BCI部署中，特定的范式(如用于中风康复或辅助机器人的运动想象(MI))通常在数据采集前就已确定。本文提出了MIRepNet，这是首个专为MI范式定制的EEG基础模型。MIRepNet包含高质量的EEG预处理流水线，该流水线融入了神经生理学信息引导的通道模板，可适应具有任意电极配置的EEG头戴设备。此外，我们引入了一种混合预训练策略，结合了自监督的掩码令牌重建和监督式MI分类，使得在新型下游MI任务上(每类少于30次试验)能够快速适应和准确解码。在五个公共MI数据集上的广泛评估表明，MIRepNet始终取得了最先进的性能，显著优于专用和通用EEG模型。我们的代码将在GitHub上提供：https://github.com/staraink/MIRepNet。

**GitHub仓库**：https://github.com/staraink/MIRepNet
**项目页面**：暂无
**模型功能**：专为运动想象范式设计的EEG基础模型，包含高质量预处理流水线和混合预训练策略，实现快速适应和准确解码。

**分析时间**：2025-08-04T19:21:01.241871
