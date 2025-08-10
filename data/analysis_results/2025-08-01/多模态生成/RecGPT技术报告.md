# RecGPT技术报告

**论文ID**：2507.22879
**英文标题**：RecGPT Technical Report
**中文标题**：RecGPT技术报告
**论文地址**：https://arxiv.org/abs/2507.22879

**作者团队**：Chao Yi, Dian Chen, Gaoyang Guo, Jiakai Tang, Jian Wu, Jing Yu, Sunhao Dai, Wen Chen, Wenjun Yang, Yuning Jiang, Zhujin Gao, Bo Zheng, Chi Li, Dimin Wang, Dixuan Wang, Fan Li, Fan Zhang, Haibin Chen, Haozhuang Liu, Jialin Zhu, Jiamang Wang, Jiawei Wu, Jin Cui, Ju Huang, Kai Zhang, Kan Liu, Lang Tian, Liang Rao, Longbin Li, Lulu Zhao, Mao Zhang, Na He, Peiyang Wang, Qiqi Huang, Tao Luo, Wenbo Su, Xiaoxiao He, Xin Tong, Xu Chen, Xunke Xi, Yang Li, Yaxuan Wu, Yeqiu Yang, Yi Hu, Yinnan Song, Yuchen Li, Yujie Luo, Yujin Yuan, Yuliang Yan, Zhengyang Wang, Zhibo Xiao, Zhixin Ma, Zile Zhou
**发表日期**：2025-07-30

**英文摘要**：
Recommender systems are among the most impactful applications of artificial intelligence, serving as critical infrastructure connecting users, merchants, and platforms. However, most current industrial systems remain heavily reliant on historical co-occurrence patterns and log-fitting objectives, i.e., optimizing for past user interactions without explicitly modeling user intent. This log-fitting approach often leads to overfitting to narrow historical preferences, failing to capture users' evolving and latent interests. As a result, it reinforces filter bubbles and long-tail phenomena, ultimately harming user experience and threatening the sustainability of the whole recommendation ecosystem.
  To address these challenges, we rethink the overall design paradigm of recommender systems and propose RecGPT, a next-generation framework that places user intent at the center of the recommendation pipeline. By integrating large language models (LLMs) into key stages of user interest mining, item retrieval, and explanation generation, RecGPT transforms log-fitting recommendation into an intent-centric process. To effectively align general-purpose LLMs to the above domain-specific recommendation tasks at scale, RecGPT incorporates a multi-stage training paradigm, which integrates reasoning-enhanced pre-alignment and self-training evolution, guided by a Human-LLM cooperative judge system. Currently, RecGPT has been fully deployed on the Taobao App. Online experiments demonstrate that RecGPT achieves consistent performance gains across stakeholders: users benefit from increased content diversity and satisfaction, merchants and the platform gain greater exposure and conversions. These comprehensive improvement results across all stakeholders validates that LLM-driven, intent-centric design can foster a more sustainable and mutually beneficial recommendation ecosystem.

**中文摘要**：
推荐系统是人工智能最具影响力的应用之一，作为连接用户、商家和平台的关键基础设施。然而，当前大多数工业系统仍然严重依赖历史共现模式和日志拟合目标，即优化过去的用户交互而不明确建模用户意图。这种日志拟合方法往往导致对狭窄历史偏好的过拟合，无法捕捉用户不断演变的潜在兴趣。因此，它强化了过滤气泡和长尾现象，最终损害用户体验并威胁整个推荐生态系统的可持续性。为应对这些挑战，我们重新思考了推荐系统的整体设计范式，并提出RecGPT，这是一个以用户意图为中心的下一代推荐框架。通过将大型语言模型（LLMs）整合到用户兴趣挖掘、项目检索和解释生成的关键阶段，RecGPT将日志拟合推荐转变为以意图为中心的过程。为了有效地将通用LLMs大规模对齐到上述领域特定的推荐任务，RecGPT采用多阶段训练范式，该范式结合了推理增强的预对齐和自我训练演化，并由人-LLM协同判断系统指导。目前，RecGPT已在淘宝App上全面部署。在线实验表明，RecGPT在所有利益相关者中实现了一致的性能提升：用户从增加的内容多样性和满意度中受益，商家和平台获得了更大的曝光率和转化率。所有利益相关者这些全面的改进结果验证了LLM驱动的、以意图为中心的设计可以培育一个更可持续和互利共赢的推荐生态系统。

**GitHub仓库**：暂无
**项目页面**：暂无
**模型功能**：以用户意图为中心的推荐框架，整合LLM实现兴趣挖掘、检索和解释生成，构建更可持续的推荐生态系统

**技术特点**：RecGPT创新性地将传统基于日志拟合的推荐系统转变为以用户意图为中心的框架，通过将大型语言模型整合到用户兴趣挖掘、项目检索和解释生成的关键阶段，解决了传统推荐系统无法捕捉用户潜在兴趣的问题。同时，它采用多阶段训练范式，结合推理增强的预对齐和自我训练演化，并由人-LLM协同判断系统指导，有效将通用LLMs对齐到特定推荐任务。

**应用场景**：1. 电商平台（如淘宝App）的商品推荐系统，提高用户满意度和平台转化率；2. 个性化内容推荐，解决过滤气泡和长尾现象，增强内容多样性；3. 智能推荐解释生成，帮助用户理解推荐理由，提高推荐接受度和用户体验。

**分析时间**：2025-08-04T17:48:14.199948