# Rep-MTL: 利用表示级任务显著性增强多任务学习性能

**论文ID**：2507.21049
**英文标题**：Rep-MTL: Unleashing the Power of Representation-level Task Saliency for   Multi-Task Learning
**中文标题**：Rep-MTL: 利用表示级任务显著性增强多任务学习性能
**论文地址**：https://arxiv.org/abs/2507.21049

**作者团队**：Zedong Wang, Siyuan Li, Dan Xu
**发表日期**：2025-07-28

**英文摘要**：
Despite the promise of Multi-Task Learning in leveraging complementary
knowledge across tasks, existing multi-task optimization (MTO) techniques
remain fixated on resolving conflicts via optimizer-centric loss scaling and
gradient manipulation strategies, yet fail to deliver consistent gains. In this
paper, we argue that the shared representation space, where task interactions
naturally occur, offers rich information and potential for operations
complementary to existing optimizers, especially for facilitating the
inter-task complementarity, which is rarely explored in MTO. This intuition
leads to Rep-MTL, which exploits the representation-level task saliency to
quantify interactions between task-specific optimization and shared
representation learning. By steering these saliencies through entropy-based
penalization and sample-wise cross-task alignment, Rep-MTL aims to mitigate
negative transfer by maintaining the effective training of individual tasks
instead pure conflict-solving, while explicitly promoting complementary
information sharing. Experiments are conducted on four challenging MTL
benchmarks covering both task-shift and domain-shift scenarios. The results
show that Rep-MTL, even paired with the basic equal weighting policy, achieves
competitive performance gains with favorable efficiency. Beyond standard
performance metrics, Power Law exponent analysis demonstrates Rep-MTL's
efficacy in balancing task-specific learning and cross-task sharing. The
project page is available at HERE.

**中文摘要**：
尽管多任务学习在利用任务间互补知识方面前景广阔，但现有的多任务优化(MTO)技术仍然专注于通过以优化器为中心的损失缩放和梯度操作策略来解决冲突，却未能带来持续的提升。在本文中，我们认为共享表示空间——任务交互自然发生的地方——提供了丰富的信息和进行操作的潜力，这些操作与现有优化器互补，特别是促进任务间互补性，这在MTO中很少被探索。这一直觉催生了Rep-MTL，它利用表示级任务显著性来量化特定任务优化与共享表示学习之间的交互。通过基于熵的惩罚和样本级跨任务对齐来引导这些显著性，Rep-MTL旨在通过保持各个任务的有效训练而非纯粹解决冲突来缓解负迁移，同时明确促进互补信息的共享。我们在涵盖任务偏移和域偏移场景的四个具有挑战性的多任务学习基准上进行了实验。结果表明，即使与基本的等权重策略配对，Rep-MTL也能实现具有良好效率的竞争性性能提升。除了标准性能指标外，幂律指数分析证明了Rep-MTL在平衡特定任务学习和跨任务共享方面的有效性。项目页面可在HERE获取。

**GitHub仓库**：https://github.com/Jacky1128/Rep-MTL
**项目页面**：https://jacky1128.github.io/RepMTL/
**模型功能**：利用表示级任务显著性量化任务交互，促进互补信息共享，提升多任务学习性能。

**分析时间**：2025-08-04T19:54:46.052213
