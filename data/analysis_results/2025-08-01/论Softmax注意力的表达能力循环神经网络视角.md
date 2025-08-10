# 论Softmax注意力的表达能力：循环神经网络视角

**论文ID**：2507.23632
**英文标题**：On the Expressiveness of Softmax Attention: A Recurrent Neural Network   Perspective
**中文标题**：论Softmax注意力的表达能力：循环神经网络视角
**论文地址**：https://arxiv.org/abs/2507.23632

**作者团队**：Gabriel Mongaras, Eric C. Larson
**发表日期**：2025-07-31

**英文摘要**：
Since its introduction, softmax attention has become the backbone of modern
transformer architectures due to its expressiveness and scalability across a
wide range of tasks. However, the main drawback of softmax attention is the
quadratic memory requirement and computational complexity with respect to the
sequence length. By replacing the softmax nonlinearity, linear attention and
similar methods have been introduced to avoid the quadratic bottleneck of
softmax attention. Despite these linear forms of attention being derived from
the original softmax formulation, they typically lag in terms of downstream
accuracy. While strong intuition of the softmax nonlinearity on the query and
key inner product suggests that it has desirable properties compared to other
nonlinearities, the question of why this discrepancy exists still remains
unanswered. This work demonstrates that linear attention is an approximation of
softmax attention by deriving the recurrent form of softmax attention. Using
this form, each part of softmax attention can be described in the language of
recurrent neural networks (RNNs). Describing softmax attention as an RNN allows
for the ablation of the components of softmax attention to understand the
importance of each part and how they interact. In this way, our work helps
explain why softmax attention is more expressive than its counterparts.

**中文摘要**：
自Softmax注意力机制引入以来，由于其广泛的任务表达能力和可扩展性，它已成为现代Transformer架构的骨干。然而，Softmax注意力的主要缺点是其对序列长度的二次方内存需求和计算复杂度。通过替换Softmax非线性函数，线性注意力及类似方法被提出以避免Softmax注意力的二次瓶颈。尽管这些线性注意力形式源于原始Softmax公式，但在下游任务准确性方面通常表现较差。虽然Softmax非线性在查询和键内积上的强烈直觉表明它比其他非线性函数具有更理想的特性，但这种差异存在的原因仍未得到解答。本研究通过推导Softmax注意力的循环形式，证明了线性注意力是Softmax注意力的一种近似。利用这种形式，Softmax注意力的每个部分都可以用循环神经网络(RNN)的语言来描述。将Softmax注意力描述为RNN，可以对Softmax注意力组件进行消融研究，以理解每个部分的重要性及其相互作用方式。通过这种方式，我们的工作有助于解释为什么Softmax注意力比其对应方法更具表现力。

**GitHub仓库**：https://github.com/gmongaras/On-the-Expressiveness-of-Softmax-Attention-A-Recurrent-Neural-Network-Perspective
**项目页面**：暂无
**模型功能**：分析Softmax注意力的循环神经网络表示，解释其比线性注意力更具表现力的原因。

**分析时间**：2025-08-04T17:49:55.295239
