# 音频生成

# Music Arena：文本到音乐的实时评估

**论文ID**：2507.20900
**英文标题**：Music Arena: Live Evaluation for Text-to-Music
**中文标题**：Music Arena：文本到音乐的实时评估
**论文地址**：https://arxiv.org/abs/2507.20900

**作者团队**：Yonghyun Kim, Wayne Chi, Anastasios N. Angelopoulos, Wei-Lin Chiang, Koichi Saito, Shinji Watanabe, Yuki Mitsufuji, Chris Donahue
**发表日期**：2025-07-28

**英文摘要**：
We present Music Arena, an open platform for scalable human preference
evaluation of text-to-music (TTM) models. Soliciting human preferences via
listening studies is the gold standard for evaluation in TTM, but these studies
are expensive to conduct and difficult to compare, as study protocols may
differ across systems. Moreover, human preferences might help researchers align
their TTM systems or improve automatic evaluation metrics, but an open and
renewable source of preferences does not currently exist. We aim to fill these
gaps by offering *live* evaluation for TTM. In Music Arena, real-world users
input text prompts of their choosing and compare outputs from two TTM systems,
and their preferences are used to compile a leaderboard. While Music Arena
follows recent evaluation trends in other AI domains, we also design it with
key features tailored to music: an LLM-based routing system to navigate the
heterogeneous type signatures of TTM systems, and the collection of *detailed*
preferences including listening data and natural language feedback. We also
propose a rolling data release policy with user privacy guarantees, providing a
renewable source of preference data and increasing platform transparency.
Through its standardized evaluation protocol, transparent data access policies,
and music-specific features, Music Arena not only addresses key challenges in
the TTM ecosystem but also demonstrates how live evaluation can be thoughtfully
adapted to unique characteristics of specific AI domains.
  Music Arena is available at: https://music-arena.org

**中文摘要**：
我们提出了Music Arena，一个用于可扩展人类偏好评估文本到音乐(TTM)模型的开放平台。通过听力研究征求人类偏好是TTM评估的金标准，但这些研究成本高昂且难以比较，因为不同系统的研究协议可能不同。此外，人类偏好可能帮助研究人员调整其TTM系统或改进自动评估指标，但目前不存在开放且可再生的偏好来源。我们旨在通过为TTM提供*实时*评估来填补这些空白。在Music Arena中，现实世界的用户输入他们选择的文本提示，并比较来自两个TTM系统的输出，他们的偏好被用来编制排行榜。虽然Music Arena遵循了其他AI领域的最新评估趋势，但我们还设计了针对音乐的关键功能：基于LLM的路由系统来导航TTM系统的异构类型签名，以及收集包括听力和自然语言反馈在内的*详细*偏好。我们还提出了滚动数据发布政策与用户隐私保证，提供可再生的偏好数据来源并增加平台透明度。通过其标准化的评估协议、透明的数据访问政策和音乐特定功能，Music Arena不仅解决了TTM生态系统中的关键挑战，还展示了如何将实时评估深思熟虑地适应特定AI领域的独特特征。Music Arena可在以下网址访问：https://music-arena.org

**GitHub仓库**：暂无
**项目页面**：暂无
**模型功能**：文本到音乐模型的实时人类偏好评估平台，通过标准化协议解决TTM评估挑战

**技术特点**：基于LLM的路由系统导航TTM系统的异构类型签名，能处理不同格式的音乐生成系统；收集详细的用户偏好数据包括听力和自然语言反馈，为模型改进提供更全面的评估依据；采用滚动数据发布政策与用户隐私保证，提供可再生的偏好数据来源并增加平台透明度。

**应用场景**：文本到音乐模型的标准化评估和排行榜生成，帮助研究人员和开发者了解模型性能；TTM模型的优化和对齐，通过人类偏好数据指导模型改进方向；自动评估指标的校准和验证，利用真实人类偏好数据提升自动评估的准确性。

**分析时间**：2025-08-04T19:55:19.332429