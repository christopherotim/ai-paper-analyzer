# TARS：用于多模态大语言模型中减少幻觉的MinMax令牌自适应偏好策略

**论文ID**：2507.21584
**英文标题**：TARS: MinMax Token-Adaptive Preference Strategy for Hallucination Reduction in MLLMs
**中文标题**：TARS：用于多模态大语言模型中减少幻觉的MinMax令牌自适应偏好策略
**论文地址**：https://arxiv.org/abs/2507.21584

**作者团队**：Kejia Zhang, Keda Tao, Zhiming Luo, Chang Liu, Jiasheng Tang, Huan Wang
**发表日期**：2025-07-29

**英文摘要**：
Multimodal large language models (MLLMs) enable vision-language reasoning,
yet often generate plausible outputs that are factually incorrect or visually
ungrounded, thereby compromising their reliability. Direct preference
optimization (DPO) is a common strategy for correcting hallucinations by
aligning model outputs with human preferences. Existing DPO strategies
typically treat hallucination-related preferences as fixed targets, relying on
static supervision signals during training. This approach tends to overfit to
superficial linguistic cues in preference data, leading to distributional
rigidity and spurious correlations that impair grounding in causally relevant
visual information. To overcome this limitation, we propose TARS, a
token-adaptive preference strategy that reformulates DPO as a min-max
optimization problem. TARS maximizes token-level distributional shifts under
semantic constraints to simulate alignment uncertainty, and simultaneously
minimizes the expected preference loss under these controlled perturbations.
This joint objective preserves causal grounding while mitigating overfitting to
preference patterns, thereby reducing hallucinations in multimodal reasoning.
We evaluate TARS on multiple hallucination benchmarks and find consistently
strong performance. Using only 4.8k preference samples and no expert feedback,
TARS reduces hallucination rates from 26.4% to 13.2% and decreases cognition
value from 2.5 to 0.4. It outperforms standard DPO and matches GPT-4o on
several key metrics.

**中文摘要**：
多模态大语言模型(MLLMs)使视觉语言推理成为可能，但常常生成看似合理但事实错误或视觉基础不足的输出，从而降低了它们的可靠性。直接偏好优化(DPO)是一种通过将模型输出与人类偏好对齐来纠正幻觉的常见策略。现有的DPO策略通常将幻觉相关偏好视为固定目标，在训练期间依赖静态监督信号。这种方法倾向于过度拟合偏好数据中的表面语言线索，导致分布刚性和虚假相关性，损害了对因果相关视觉信息的理解。为了克服这一限制，我们提出了TARS，一种令牌自适应偏好策略，将DPO重新表述为最小-最大优化问题。TARS在语义约束下最大化令牌级别的分布偏移，以模拟对齐的不确定性，同时在这些受控扰动下最小化期望偏好损失。这种联合目标保留了因果基础，同时减轻了对偏好模式的过度拟合，从而减少多模态推理中的幻觉。我们在多个幻觉基准上评估了TARS，发现了一致的强大性能。仅使用4.8k偏好样本且无需专家反馈，TARS将幻觉率从26.4%降低到13.2%，并将认知值从2.5降低到0.4。它在多个关键指标上优于标准DPO，并匹配GPT-4o的性能。

**GitHub仓库**：https://github.com/KejiaZhang-Robust/TARS
**项目页面**：https://kejiazhang-robust.github.io/tars_web/
**模型功能**：通过令牌自适应偏好策略减少多模态大语言模型中的幻觉，提高视觉语言推理的可靠性。

**技术特点**：TARS将直接偏好优化(DPO)重新表述为最小-最大优化问题，通过在语义约束下最大化令牌级别的分布偏移来模拟对齐不确定性，同时最小化期望偏好损失，保留了因果基础并减轻对偏好模式的过度拟合。

**应用场景**：1) 多模态内容生成与编辑，提高生成内容的准确性和可靠性；2) 视觉问答系统，减少模型回答中的幻觉成分；3) 教育和培训内容生成，避免提供错误的事实性信息。

**分析时间**：2025-08-04T17:49:24.367143