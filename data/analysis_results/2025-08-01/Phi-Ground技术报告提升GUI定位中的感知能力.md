# Phi-Ground技术报告：提升GUI定位中的感知能力

**论文ID**：2507.23779
**英文标题**：Phi-Ground Tech Report: Advancing Perception in GUI Grounding
**中文标题**：Phi-Ground技术报告：提升GUI定位中的感知能力
**论文地址**：https://arxiv.org/abs/2507.23779

**作者团队**：Miaosen Zhang, Ziqiang Xu, Jialiang Zhu, Qi Dai, Kai Qiu, Yifan Yang, Chong Luo, Tianyi Chen, Justin Wagle, Tim Franklin, Baining Guo
**发表日期**：2025-07-31

**英文摘要**：
With the development of multimodal reasoning models, Computer Use Agents
(CUAs), akin to Jarvis from "Iron Man", are becoming a reality. GUI
grounding is a core component for CUAs to execute actual actions, similar to
mechanical control in robotics, and it directly leads to the success or failure
of the system. It determines actions such as clicking and typing, as well as
related parameters like the coordinates for clicks. Current end-to-end
grounding models still achieve less than 65\% accuracy on challenging
benchmarks like ScreenSpot-pro and UI-Vision, indicating they are far from
being ready for deployment. % , as a single misclick can result in unacceptable
consequences. In this work, we conduct an empirical study on the training of
grounding models, examining details from data collection to model training.
Ultimately, we developed the Phi-Ground model family, which achieves
state-of-the-art performance across all five grounding benchmarks for models
under 10B parameters in agent settings. In the end-to-end model setting, our
model still achieves SOTA results with scores of \textbf{43.2} on
ScreenSpot-pro and \textbf{27.2} on UI-Vision. We believe that the
various details discussed in this paper, along with our successes and failures,
not only clarify the construction of grounding models but also benefit other
perception tasks. Project homepage:
https://zhangmiaosen2000.github.io/Phi-Ground/{https://zhangmiaosen2000.github.io/Phi-Ground/}

**中文摘要**：
随着多模态推理模型的发展，类似于"钢铁侠"中的Jarvis的计算机使用代理(CUAs)正成为现实。GUI定位是CUAs执行实际操作的核心组件，类似于机器人中的机械控制，它直接决定了系统的成功或失败。它决定了点击和键入等操作，以及点击等相关参数，如坐标。当前的端到端定位模型在ScreenSpot-pro和UI-Vision等具有挑战性的基准测试上仍低于65%的准确率，表明它们远未准备好部署，因为一次错误的点击可能导致不可接受的后果。在这项工作中，我们对定位模型的训练进行了实证研究，检查了从数据收集到模型训练的细节。最终，我们开发了Phi-Ground模型家族，在代理设置下，所有10B参数以下的模型在所有五个定位基准测试中都达到了最先进的性能。在端到端模型设置中，我们的模型在ScreenSpot-pro上仍取得了43.2分的SOTA结果，在UI-Vision上取得了27.2分的SOTA结果。我们相信，本文讨论的各种细节，以及我们的成功和失败，不仅阐明了定位模型的构建，也有益于其他感知任务。项目主页：https://zhangmiaosen2000.github.io/Phi-Ground/ GitHub仓库：https://github.com/zhangmiaosen2000/Phi-Ground 项目页面：https://zhangmiaosen2000.github.io/Phi-Ground/

**GitHub仓库**：https://github.com/zhangmiaosen2000/Phi-Ground
**项目页面**：https://zhangmiaosen2000.github.io/Phi-Ground/
**模型功能**：提升计算机使用代理在GUI界面上的定位感知能力，实现精准点击和键入操作。

**分析时间**：2025-08-04T17:47:53.353162
