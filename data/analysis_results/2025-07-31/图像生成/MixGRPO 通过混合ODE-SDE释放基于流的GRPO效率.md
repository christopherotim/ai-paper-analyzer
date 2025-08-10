# MixGRPO: 通过混合ODE-SDE释放基于流的GRPO效率

**论文ID**：2507.21802
**英文标题**：MixGRPO: Unlocking Flow-based GRPO Efficiency with Mixed ODE-SDE
**中文标题**：MixGRPO: 通过混合ODE-SDE释放基于流的GRPO效率
**论文地址**：https://arxiv.org/abs/2507.21802

**作者团队**：Junzhe Li, Yutao Cui, Tao Huang, Yinping Ma, Chun Fan, Miles Yang, Zhao Zhong
**发表日期**：2025-07-29

**英文摘要**：
Although GRPO substantially enhances flow matching models in human preference
alignment of image generation, methods such as FlowGRPO still exhibit
inefficiency due to the necessity of sampling and optimizing over all denoising
steps specified by the Markov Decision Process (MDP). In this paper, we propose
MixGRPO, a novel framework that leverages the flexibility of mixed
sampling strategies through the integration of stochastic differential
equations (SDE) and ordinary differential equations (ODE). This streamlines the
optimization process within the MDP to improve efficiency and boost
performance. Specifically, MixGRPO introduces a sliding window mechanism, using
SDE sampling and GRPO-guided optimization only within the window, while
applying ODE sampling outside. This design confines sampling randomness to the
time-steps within the window, thereby reducing the optimization overhead, and
allowing for more focused gradient updates to accelerate convergence.
Additionally, as time-steps beyond the sliding window are not involved in
optimization, higher-order solvers are supported for sampling. So we present a
faster variant, termed MixGRPO-Flash, which further improves
training efficiency while achieving comparable performance. MixGRPO exhibits
substantial gains across multiple dimensions of human preference alignment,
outperforming DanceGRPO in both effectiveness and efficiency, with nearly 50%
lower training time. Notably, MixGRPO-Flash further reduces training time by 71%. Codes and models are available at
https://github.com/Tencent-Hunyuan/MixGRPO{MixGRPO}.

**中文摘要**：
尽管GRPO显著提升了图像生成中人类偏好对齐的流匹配模型，但像FlowGRPO这样的方法仍然表现出低效率，这是由于需要在马尔可夫决策过程(MDP)指定的所有去噪步骤上进行采样和优化的必要性。在本文中，我们提出了MixGRPO，一个新颖的框架，它通过整合随机微分方程(SDE)和常微分方程(ODE)，利用混合采样策略的灵活性。这简化了MDP内的优化过程，以提高效率和提升性能。具体而言，MixGRPO引入了一个滑动窗口机制，仅在窗口内使用SDE采样和GRPO引导的优化，而在窗口外应用ODE采样。这种设计将采样随机性限制在窗口内的时间步，从而减少优化开销，并允许更专注的梯度更新以加速收敛。此外，由于滑动窗口之外的时间步不参与优化，因此支持使用更高阶的求解器进行采样。因此，我们提出了一个更快的变体，称为MixGRPO-Flash，它在实现可比性能的同时进一步提高了训练效率。MixGRPO在人类偏好对齐的多个维度上表现出显著提升，在有效性和效率上都优于DanceGRPO，训练时间减少了近50%。值得注意的是，MixGRPO-Flash进一步将训练时间减少了71%。代码和模型可在https://github.com/Tencent-Hunyuan/MixGRPO{MixGRPO}获取。

**GitHub仓库**：https://github.com/Tencent-Hunyuan/MixGRPO
**项目页面**：https://tulvgengenr.github.io/MixGRPO-Project-Page/
**模型功能**：结合SDE和ODE混合采样策略，提升GRPO在流匹配模型中的训练效率，实现更快的收敛速度和更好的性能表现。

**技术特点**：MixGRPO创新性地结合了SDE和ODE混合采样策略，通过滑动窗口机制将随机采样限制在窗口内，显著减少优化开销；同时支持更高阶求解器采样，并提出了更快的变体MixGRPO-Flash，在保持可比性能的同时将训练时间减少了71%。

**应用场景**：高效图像生成平台，需要快速生成高质量图像的内容创作工具；基于用户偏好的个性化图像定制系统，如社交媒体内容生成；低延迟实时图像处理应用，如在线图像编辑工具和实时内容生成系统。

**分析时间**：2025-08-04T19:06:25.015605