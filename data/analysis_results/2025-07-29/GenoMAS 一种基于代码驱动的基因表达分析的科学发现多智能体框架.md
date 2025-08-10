# GenoMAS: 一种基于代码驱动的基因表达分析的科学发现多智能体框架

**论文ID**：2507.21035
**英文标题**：GenoMAS: A Multi-Agent Framework for Scientific Discovery via   Code-Driven Gene Expression Analysis
**中文标题**：GenoMAS: 一种基于代码驱动的基因表达分析的科学发现多智能体框架
**论文地址**：https://arxiv.org/abs/2507.21035

**作者团队**：Haoyang Liu, Yijiang Li, Haohan Wang
**发表日期**：2025-07-28

**英文摘要**：
Gene expression analysis holds the key to many biomedical discoveries, yet
extracting insights from raw transcriptomic data remains formidable due to the
complexity of multiple large, semi-structured files and the need for extensive
domain expertise. Current automation approaches are often limited by either
inflexible workflows that break down in edge cases or by fully autonomous
agents that lack the necessary precision for rigorous scientific inquiry.
GenoMAS charts a different course by presenting a team of LLM-based scientists
that integrates the reliability of structured workflows with the adaptability
of autonomous agents. GenoMAS orchestrates six specialized LLM agents through
typed message-passing protocols, each contributing complementary strengths to a
shared analytic canvas. At the heart of GenoMAS lies a guided-planning
framework: programming agents unfold high-level task guidelines into Action
Units and, at each juncture, elect to advance, revise, bypass, or backtrack,
thereby maintaining logical coherence while bending gracefully to the
idiosyncrasies of genomic data.
  On the GenoTEX benchmark, GenoMAS reaches a Composite Similarity Correlation
of 89.13% for data preprocessing and an F_1 of 60.48% for gene
identification, surpassing the best prior art by 10.61% and 16.85%
respectively. Beyond metrics, GenoMAS surfaces biologically plausible
gene-phenotype associations corroborated by the literature, all while adjusting
for latent confounders. Code is available at https://github.com/Liu-Hy/GenoMAS.

**中文摘要**：
基因表达分析是许多生物医学发现的关键，然而，由于多个大型半结构化文件的复杂性以及对广泛领域专业知识的需求，从原始转录组数据中提取见解仍然是一项艰巨任务。当前的自动化方法通常受到限制：要么是在边缘情况下失效的僵化工作流，要么是缺乏严谨科学研究所需必要精度的完全自主智能体。GenoMAS开辟了一条新路径，它呈现了一支基于大语言模型(LLM)的科学家团队，将结构化工作流的可靠性与自主智能体的适应性相结合。GenoMAS通过类型化消息传递协议协调六个专门的LLM智能体，每个智能体为共享的分析画布贡献互补的优势。GenoMAS的核心是一个引导式规划框架：编程智能体将高层任务指导展开为行动单元(Action Units)，并在每个节点选择前进、修订、绕过或回溯，从而在优雅地适应基因组数据特性的同时保持逻辑连贯性。在GenoTEX基准测试中，GenoMAS在数据预处理方面达到89.13%的复合相似性相关性，在基因识别方面达到60.48%的F1值，分别比之前的最佳方法高出10.61%和16.85%。除了指标之外，GenoMAS还揭示出文献支持的生物学合理的基因-表型关联，同时调整了潜在的混杂因素。代码可在https://github.com/Liu-Hy/GenoMAS获取。

**GitHub仓库**：https://github.com/Liu-Hy/GenoMAS
**项目页面**：暂无
**模型功能**：基于LLM的多智能体框架，通过代码驱动的基因表达分析实现科学发现，结合结构化工作流与自主智能体的优势。

**分析时间**：2025-08-04T19:55:31.307048
