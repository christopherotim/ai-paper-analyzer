# CUDA-L1：通过对比强化学习改进CUDA优化

**论文ID**：2507.14111
**英文标题**：CUDA-L1: Improving CUDA Optimization via Contrastive Reinforcement   Learning
**中文标题**：CUDA-L1：通过对比强化学习改进CUDA优化
**论文地址**：https://arxiv.org/abs/2507.14111

**作者团队**：Xiaoya Li, Xiaofei Sun, Albert Wang, Jiwei Li, Chris Shum
**发表日期**：2025-07-18

**英文摘要**：
The exponential growth in demand for GPU computing resources, driven by the
rapid advancement of Large Language Models, has created an urgent need for
automated CUDA optimization strategies. While recent advances in LLMs show
promise for code generation, current SOTA models (e.g. R1, o1) achieve low
success rates in improving CUDA speed. In this paper, we introduce CUDA-L1, an
automated reinforcement learning framework for CUDA optimization.
  CUDA-L1 achieves performance improvements on the CUDA optimization task:
trained on NVIDIA A100, it delivers an average speedup of x17.7 across all 250
CUDA kernels of KernelBench, with peak speedups reaching x449. Furthermore, the
model also demonstrates excellent portability across GPU architectures,
achieving average speedups of x17.8 on H100, x19.0 on RTX 3090, x16.5 on L40,
x14.7 on H800, and x13.9 on H20 despite being optimized specifically for A100.
Beyond these benchmark results, CUDA-L1 demonstrates several remarkable
properties: 1) Discovers a variety of CUDA optimization techniques and learns
to combine them strategically to achieve optimal performance; 2) Uncovers
fundamental principles of CUDA optimization; 3) Identifies non-obvious
performance bottlenecks and rejects seemingly beneficial optimizations that
harm performance.
  The capabilities of CUDA-L1 demonstrate that reinforcement learning can
transform an initially poor-performing LLM into an effective CUDA optimizer
through speedup-based reward signals alone, without human expertise or domain
knowledge. More importantly, the trained RL model extend the acquired reasoning
abilities to new kernels. This paradigm opens possibilities for automated
optimization of CUDA operations, and holds promise to substantially promote GPU
efficiency and alleviate the rising pressure on GPU computing resources.

**中文摘要**：
由大型语言模型的快速发展驱动的GPU计算资源需求呈指数级增长，这迫切需要自动化的CUDA优化策略。尽管最近LLMs的进展在代码生成方面显示出前景，但当前最先进的模型（如R1、o1）在提高CUDA速度方面的成功率较低。在本文中，我们介绍了CUDA-L1，一个用于CUDA优化的自动化强化学习框架。CUDA-L1在CUDA优化任务上实现了性能提升：在NVIDIA A100上训练后，它在KernelBench的所有250个CUDA内核上实现了平均17.7倍的加速，峰值加速达到449倍。此外，尽管该模型专门针对A100进行了优化，但它还显示出在GPU架构之间的卓越可移植性，在H100上实现了17.8倍的平均加速，在RTX 3090上实现了19.0倍，在L40上实现了16.5倍，在H800上实现了14.7倍，在H20上实现了13.9倍。除了这些基准测试结果外，CUDA-L1还展示了几个显著特性：1) 发现了多种CUDA优化技术，并学会了战略性地组合它们以实现最佳性能；2) 揭示了CUDA优化的基本原理；3) 识别出非明显的性能瓶颈，并拒绝那些看似有益但实际有害的优化。CUDA-L1的能力表明，仅通过基于加速的奖励信号，强化学习可以将最初表现不佳的LLM转变为有效的CUDA优化器，而无需人类专业知识或领域知识。更重要的是，训练好的RL模型将获得的推理能力扩展到新的内核。这种范式为CUDA操作的自动化优化开辟了可能性，有望显著提高GPU效率并缓解GPU计算资源日益增长的压力。

**GitHub仓库**：暂无
**项目页面**：暂无
**模型功能**：自动化CUDA优化框架，通过强化学习发现并组合优化技术，实现显著性能提升和跨架构可移植性。

**分析时间**：2025-08-04T19:21:06.069696
