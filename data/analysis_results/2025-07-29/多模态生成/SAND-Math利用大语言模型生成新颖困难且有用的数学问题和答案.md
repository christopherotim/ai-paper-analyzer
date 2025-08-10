# 文本生成

# SAND-Math：利用大语言模型生成新颖、困难且有用的数学问题和答案

**论文ID**：2507.20527
**英文标题**：SAND-Math: Using LLMs to Generate Novel, Difficult and Useful   Mathematics Questions and Answers
**中文标题**：SAND-Math：利用大语言模型生成新颖、困难且有用的数学问题和答案
**论文地址**：https://arxiv.org/abs/2507.20527

**作者团队**：Chaitanya Manem, Pratik Prabhanjan Brahma, Prakamya Mishra, Zicheng Liu, Emad Barsoum
**发表日期**：2025-07-28

**英文摘要**：
The demand for Large Language Models (LLMs) capable of sophisticated
mathematical reasoning is growing across industries. However, the development
of performant mathematical LLMs is critically bottlenecked by the scarcity of
difficult, novel training data. We introduce SAND-Math (Synthetic
Augmented Novel and Difficult Mathematics problems and solutions), a pipeline
that addresses this by first generating high-quality problems from scratch and
then systematically elevating their complexity via a new Difficulty
Hiking step. We demonstrate the effectiveness of our approach through two key
findings. First, augmenting a strong baseline with SAND-Math data significantly
boosts performance, outperforming the next-best synthetic dataset by
uparrow 17.85 absolute points on the AIME25 benchmark. Second, in a
dedicated ablation study, we show our Difficulty Hiking process is highly
effective: by increasing average problem difficulty from 5.02 to 5.98, this
step lifts AIME25 performance from 46.38\% to 49.23\%. The full generation
pipeline, final dataset, and a fine-tuned model form a practical and scalable
toolkit for building more capable and efficient mathematical reasoning LLMs.
SAND-Math dataset is released here:
https://hf-mirror.com/datasets/amd/SAND-MATH{https://hf-mirror.com/datasets/amd/SAND-MATH}

**中文摘要**：
各行各业对能够进行复杂数学推理的大型语言模型(LLMs)的需求正在增长。然而，高性能数学LLM的发展受到困难、新颖训练数据稀缺的关键瓶颈限制。我们介绍了SAND-Math（合成增强新颖和困难的数学问题和解决方案），这是一个通过首先从头开始生成高质量问题，然后通过新的难度提升步骤系统地提高其复杂度来解决这一问题的流程。我们通过两个关键发现证明了我们方法的有效性。首先，用SAND-Math数据增强一个强大的基线模型显著提高了性能，在AIME25基准测试上比次优合成数据集高出17.85个绝对点。其次，在专门的消融研究中，我们展示了我们的难度提升过程非常有效：通过将平均问题难度从5.02提高到5.98，这一步骤将AIME25性能从46.38%提升到49.23%。完整的生成流程、最终数据集和微调模型构成了构建更强大、更高效的数学推理LLM的实用且可扩展的工具包。SAND-Math数据集在此发布：https://hf-mirror.com/datasets/amd/SAND-MATH

**GitHub仓库**：暂无
**项目页面**：暂无
**模型功能**：生成高质量数学问题并提升难度，解决数学LLM训练数据稀缺问题，提升数学推理能力。

**技术特点**：SAND-Math引入了完整的数学问题生成流程，包含从零开始生成高质量问题和通过创新的"难度提升"步骤系统性提高问题复杂度两个核心环节，解决了数学LLM训练数据稀缺的关键瓶颈。实验证明该方法显著有效，使用SAND-Math数据增强的模型在AIME25基准测试上比次优合成数据集高出17.85个绝对点。

**应用场景**：1) 数学教育领域，为在线学习平台和智能辅导系统生成个性化、难度递进的数学练习题和解答；2) 数学大语言模型训练，为数学推理LLM提供高质量、高难度的训练数据，提升模型解决复杂数学问题的能力；3) 数学竞赛培训，生成具有挑战性的竞赛级数学题目，帮助学生准备各类数学竞赛。

**分析时间**：2025-08-04T19:55:20.690235