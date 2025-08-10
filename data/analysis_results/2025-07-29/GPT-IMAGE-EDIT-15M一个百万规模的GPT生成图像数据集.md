# GPT-IMAGE-EDIT-1.5M：一个百万规模的GPT生成图像数据集

**论文ID**：2507.21033
**英文标题**：GPT-IMAGE-EDIT-1.5M: A Million-Scale, GPT-Generated Image Dataset
**中文标题**：GPT-IMAGE-EDIT-1.5M：一个百万规模的GPT生成图像数据集
**论文地址**：https://arxiv.org/abs/2507.21033

**作者团队**：Yuhan Wang, Siwei Yang, Bingchen Zhao, Letian Zhang, Qing Liu, Yuyin Zhou, Cihang Xie
**发表日期**：2025-07-28

**英文摘要**：
Recent advancements in large multimodal models like GPT-4o have set a new
standard for high-fidelity, instruction-guided image editing. However, the
proprietary nature of these models and their training data creates a
significant barrier for open-source research. To bridge this gap, we introduce
GPT-IMAGE-EDIT-1.5M, a publicly available, large-scale image-editing corpus
containing more than 1.5 million high-quality triplets (instruction, source
image, edited image). We systematically construct this dataset by leveraging
the versatile capabilities of GPT-4o to unify and refine three popular
image-editing datasets: OmniEdit, HQ-Edit, and UltraEdit. Specifically, our
methodology involves 1) regenerating output images to enhance visual quality
and instruction alignment, and 2) selectively rewriting prompts to improve
semantic clarity. To validate the efficacy of our dataset, we fine-tune
advanced open-source models on GPT-IMAGE-EDIT-1.5M. The empirical results are
exciting, e.g., the fine-tuned FluxKontext achieves highly competitive
performance across a comprehensive suite of benchmarks, including 7.24 on
GEdit-EN, 3.80 on ImgEdit-Full, and 8.78 on Complex-Edit, showing stronger
instruction following and higher perceptual quality while maintaining identity.
These scores markedly exceed all previously published open-source methods and
substantially narrow the gap to leading proprietary models. We hope the full
release of GPT-IMAGE-EDIT-1.5M can help to catalyze further open research in
instruction-guided image editing.

**中文摘要**：
像GPT-4o这样的大型多模态模型的最新进展为高保真、指令引导的图像编辑树立了新标准。然而，这些模型及其训练数据的专有性质为开源研究造成了重大障碍。为了弥合这一差距，我们推出了GPT-IMAGE-EDIT-1.5M，这是一个公开可用的、大规模图像编辑语料库，包含超过150万组高质量三元组（指令、源图像、编辑后图像）。我们利用GPT-4o的多功能能力系统地构建了这个数据集，以统一和优化三个流行的图像编辑数据集：OmniEdit、HQ-Edit和UltraEdit。具体来说，我们的方法包括：1) 重新生成输出图像以提高视觉质量和指令对齐度，以及2) 选择性重写提示以提高语义清晰度。为了验证我们数据集的有效性，我们在GPT-IMAGE-EDIT-1.5M上对先进的开源模型进行了微调。实验结果令人振奋，例如，微调后的FluxKontext在全面的基准测试中实现了极具竞争力的性能，包括在GEdit-EN上达到7.24分，在ImgEdit-Full上达到3.80分，在Complex-Edit上达到8.78分，显示出更强的指令遵循能力和更高的感知质量，同时保持身份一致性。这些分数明显超过了所有先前发布的开源方法，并显著缩小了与领先专有模型的差距。我们希望GPT-IMAGE-EDIT-1.5M的完整发布能够促进指令引导图像编辑领域的进一步开放研究。

**GitHub仓库**：https://github.com/wyhlovecpp/GPT-Image-Edit
**项目页面**：https://ucsc-vlaa.github.io/GPT-Image-Edit/
**模型功能**：提供大规模高质量图像编辑数据集，用于训练开源图像编辑模型，缩小与专有模型的性能差距。

**分析时间**：2025-08-04T19:55:02.217827
