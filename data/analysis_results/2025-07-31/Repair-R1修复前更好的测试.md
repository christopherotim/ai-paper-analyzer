# Repair-R1：修复前更好的测试

**论文ID**：2507.22853
**英文标题**：Repair-R1: Better Test Before Repair
**中文标题**：Repair-R1：修复前更好的测试
**论文地址**：https://arxiv.org/abs/2507.22853

**作者团队**：Haichuan Hu, Xiaochen Xie, Quanjun Zhang
**发表日期**：2025-07-30

**英文摘要**：
APR (Automated Program Repair) aims to automatically locate program defects,
generate patches and validate the repairs. Existing techniques for APR are
often combined with LLMs (Large Language Models), which leverages the
code-related knowledge of LLMs to improve repair effectiveness. Current
LLM-based APR methods typically utilize test cases only during the inference
stage, adopting an iterative approach that performs repair first and validates
it through test execution afterward. This conventional paradigm neglects two
important aspects: the potential contribution of test cases in the training
phase, and the possibility of leveraging testing prior to repair. To address
this, we propose Repair-R1, which introduces test cases into the model's
training phase and shifts test generation to precede repair. The model is
required to first generate discriminative test cases that can distinguish
defective behaviors, and then perform repair based on these tests. This enables
the model to better locate defects and understand the underlying causes of
defects, thereby improving repair effectiveness. We implement Repair-R1 with
three different backbone models, using RL (reinforcement learning) to
co-optimize test generation and bug repair. Experimental results on four widely
adopted benchmarks demonstrate the superiority of Repair-R1. Specially,
compared to vanilla models, Repair-R1 improves repair success rate by 2.68\% to
48.29\%, test generation success rate by 16.38\% to 53.28\%, and test coverage
by 0.78\% to 53.96\%. We publish the code and weights at
https://github.com/Tomsawyerhu/APR-RL and
https://hf-mirror.com/tomhu/Qwen3-4B-RL-5000-step.

**中文摘要**：
APR（自动程序修复）旨在自动定位程序缺陷、生成补丁并验证修复结果。现有的APR技术通常与大型语言模型（LLM）结合，利用LLM的代码相关知识来提高修复效果。当前的基于LLM的APR方法通常仅在推理阶段使用测试用例，采用先执行修复然后通过测试执行验证的迭代方法。这种传统范式忽略了两个重要方面：测试用例在训练阶段的潜在贡献，以及在修复前利用测试的可能性。为此，我们提出了Repair-R1，它将测试用例引入模型的训练阶段，并将测试生成提前到修复之前。模型需要先生成能够区分缺陷行为的判别性测试用例，然后基于这些测试进行修复。这使得模型能够更好地定位缺陷并理解缺陷的根本原因，从而提高修复效果。我们使用三种不同的骨干模型实现了Repair-R1，利用强化学习（RL）共同优化测试生成和缺陷修复。在四个广泛采用的基准测试上的实验结果证明了Repair-R1的优越性。特别是，与基础模型相比，Repair-R1将修复成功率从2.68%提高到48.29%，测试生成成功率从16.38%提高到53.28%，测试覆盖率从0.78%提高到53.96%。我们在https://github.com/Tomsawyerhu/APR-RL和https://hf-mirror.com/tomhu/Qwen3-4B-RL-5000-step发布了代码和权重。

**GitHub仓库**：https://github.com/Tomsawyerhu/APR-RL
**项目页面**：暂无
**模型功能**：通过在修复前生成判别性测试用例，提高自动程序修复的成功率和缺陷定位准确性。

**分析时间**：2025-08-04T19:06:29.966219
