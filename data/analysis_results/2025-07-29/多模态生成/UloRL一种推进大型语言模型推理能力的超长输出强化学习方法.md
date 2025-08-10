# 文本生成

# UloRL：一种推进大型语言模型推理能力的超长输出强化学习方法

**论文ID**：2507.19766
**英文标题**：UloRL:An Ultra-Long Output Reinforcement Learning Approach for Advancing   Large Language Models' Reasoning Abilities
**中文标题**：UloRL：一种推进大型语言模型推理能力的超长输出强化学习方法
**论文地址**：https://arxiv.org/abs/2507.19766

**作者团队**：Dong Du, Shulin Liu, Tao Yang, Shaohua Chen, Yang Li
**发表日期**：2025-07-26

**英文摘要**：
Recent advances in large language models (LLMs) have highlighted the
potential of reinforcement learning with verifiable rewards (RLVR) to enhance
reasoning capabilities through extended output sequences. However, traditional
RL frameworks face inefficiencies when handling ultra-long outputs due to
long-tail sequence distributions and entropy collapse during training. To
address these challenges, we propose an Ultra-Long Output Reinforcement
Learning (UloRL) approach for advancing large language models' reasoning
abilities. Specifically, we divide ultra long output decoding into short
segments, enabling efficient training by mitigating delays caused by long-tail
samples. Additionally, we introduce dynamic masking of well-Mastered Positive
Tokens (MPTs) to prevent entropy collapse. Experimental results demonstrate the
effectiveness of our approach. On the Qwen3-30B-A3B model, RL with segment
rollout achieved 2.06x increase in training speed, while RL training with
128k-token outputs improves the model's performance on AIME2025 from 70.9\% to
85.1\% and on BeyondAIME from 50.7\% to 61.9\%, even surpassing Qwen3-235B-A22B
with remarkable gains. These findings underscore the potential of our methods
to advance the reasoning capabilities of LLMs with ultra-long sequence
generation. We will release our code and model for further use by the
community.

**中文摘要**：
近期大型语言模型（LLMs）的进展凸显了通过可验证奖励的强化学习（RLVR）增强推理能力的潜力，该方法通过扩展输出序列实现。然而，当处理超长输出时，传统的强化学习框架面临效率低下的问题，这主要是由于长尾序列分布和训练过程中的熵崩溃。为应对这些挑战，我们提出了一种超长输出强化学习（UloRL）方法，用于提升大型语言模型的推理能力。具体而言，我们将超长输出解码划分为短片段，通过减轻长尾样本引起的延迟，实现高效训练。此外，我们引入了对已掌握的正向标记（MPTs）的动态掩码，以防止熵崩溃。实验结果证明了我们方法的有效性。在Qwen3-30B-A3B模型上，采用分段展开的强化学习实现了2.06倍的速度提升，而使用128k-token输出的强化学习训练则将模型在AIME2025上的性能从70.9%提高到85.1%，在BeyondAIME上从50.7%提高到61.9%，甚至显著超越了Qwen3-235B-A22B的性能。这些研究结果强调了我们的方法在通过超长序列生成推进LLMs推理能力方面的潜力。我们将发布我们的代码和模型，供社区进一步使用。

**GitHub仓库**：暂无
**项目页面**：暂无
**模型功能**：通过分段解码和动态掩码技术，解决长尾序列分布和熵崩溃问题，提升大型语言模型的推理能力。

**技术特点**：提出将超长输出解码划分为短片段的方法，有效减轻长尾样本引起的训练延迟，实现2.06倍的速度提升；引入对已掌握的正向标记(MPTs)的动态掩码技术，有效防止训练过程中的熵崩溃问题；通过128k-token输出的强化学习训练，显著提升了模型在复杂推理任务上的性能。

**应用场景**：复杂数学问题求解，如AIME等高级数学竞赛问题的自动求解系统；长文本推理任务，需要生成大量连贯文本并进行逻辑推理的应用场景；高级语言模型训练，作为强化学习框架，用于提升大型语言模型在复杂推理任务上的表现。

**分析时间**：2025-08-04T19:55:09.418105