# MetaCLIP 2: 全球扩展配方

**论文ID**：2507.22062
**英文标题**：MetaCLIP 2: A Worldwide Scaling Recipe
**中文标题**：MetaCLIP 2: 全球扩展配方
**论文地址**：https://arxiv.org/abs/2507.22062

**作者团队**：Yung-Sung Chuang, Yang Li, Dong Wang, Ching-Feng Yeh, Kehan Lyu, Ramya Raghavendra, James Glass, Lifei Huang, Jason Weston, Luke Zettlemoyer, Xinlei Chen, Zhuang Liu, Saining Xie, Wen-tau Yih, Shang-Wen Li, Hu Xu
**发表日期**：2025-07-29

**英文摘要**：
Contrastive Language-Image Pretraining (CLIP) is a popular foundation model,
supporting from zero-shot classification, retrieval to encoders for multimodal
large language models (MLLMs). Although CLIP is successfully trained on
billion-scale image-text pairs from the English world, scaling CLIP's training
further to learning from the worldwide web data is still challenging: (1) no
curation method is available to handle data points from non-English world; (2)
the English performance from existing multilingual CLIP is worse than its
English-only counterpart, i.e., "curse of multilinguality" that is common in
LLMs. Here, we present MetaCLIP 2, the first recipe training CLIP from scratch
on worldwide web-scale image-text pairs. To generalize our findings, we conduct
rigorous ablations with minimal changes that are necessary to address the above
challenges and present a recipe enabling mutual benefits from English and
non-English world data. In zero-shot ImageNet classification, MetaCLIP 2
ViT-H/14 surpasses its English-only counterpart by 0.8% and mSigLIP by 0.7%,
and surprisingly sets new state-of-the-art without system-level confounding
factors (e.g., translation, bespoke architecture changes) on multilingual
benchmarks, such as CVQA with 57.4%, Babel-ImageNet with 50.2% and XM3600 with
64.3% on image-to-text retrieval.

**中文摘要**：
对比语言-图像预训练（CLIP）是一种流行的基础模型，支持从零样本分类、检索到多模态大语言模型（MLLM）的编码器。尽管CLIP已经在英语世界的十亿级图像-文本对上成功训练，但进一步扩展CLIP的训练以从全球网络数据中学习仍然具有挑战性：(1) 没有可用的人工筛选方法来处理非英语世界的数据点；(2) 现有多语言CLIP的英语性能比其仅英语版本差，即LLMs中常见的"多语言诅咒"。在这里，我们提出了MetaCLIP 2，这是第一个在全球网络规模的图像-文本对上从头开始训练CLIP的配方。为了推广我们的发现，我们进行了严格的消融实验，仅进行了必要的最小更改来解决上述挑战，并提出了一种能够从英语和非英语世界数据中实现互利共赢的配方。在零样本ImageNet分类中，MetaCLIP 2 ViT-H/14比其仅英语版本高出0.8%，比mSigLIP高出0.7%，并且在多语言基准测试上令人惊讶地创造了新的最先进水平，没有系统层面的混杂因素（例如翻译、专有架构更改），如在图像到文本检索任务上的CVQA达到57.4%，Babel-ImageNet达到50.2%，XM3600达到64.3%。

**GitHub仓库**：暂无
**项目页面**：暂无
**模型功能**：全球多语言CLIP模型，实现英语与非英语数据的互利共赢，在多语言图像理解任务上取得最先进性能。

**分析时间**：2025-08-04T19:06:11.707444
