# ARC-Hunyuan-Video-7B: 真实世界短视频的结构化视频理解

**论文ID**：2507.20939
**英文标题**：ARC-Hunyuan-Video-7B: Structured Video Comprehension of Real-World   Shorts
**中文标题**：ARC-Hunyuan-Video-7B: 真实世界短视频的结构化视频理解
**论文地址**：https://arxiv.org/abs/2507.20939

**作者团队**：Yuying Ge, Yixiao Ge, Chen Li, Teng Wang, Junfu Pu, Yizhuo Li, Lu Qiu, Jin Ma, Lisheng Duan, Xinyu Zuo, Jinwen Luo, Weibo Gu, Zexuan Li, Xiaojing Zhang, Yangyu Tao, Han Hu, Di Wang, Ying Shan
**发表日期**：2025-07-28

**英文摘要**：
Real-world user-generated short videos, especially those distributed on
platforms such as WeChat Channel and TikTok, dominate the mobile internet.
However, current large multimodal models lack essential temporally-structured,
detailed, and in-depth video comprehension capabilities, which are the
cornerstone of effective video search and recommendation, as well as emerging
video applications. Understanding real-world shorts is actually challenging due
to their complex visual elements, high information density in both visuals and
audio, and fast pacing that focuses on emotional expression and viewpoint
delivery. This requires advanced reasoning to effectively integrate multimodal
information, including visual, audio, and text. In this work, we introduce
ARC-Hunyuan-Video, a multimodal model that processes visual, audio, and textual
signals from raw video inputs end-to-end for structured comprehension. The
model is capable of multi-granularity timestamped video captioning and
summarization, open-ended video question answering, temporal video grounding,
and video reasoning. Leveraging high-quality data from an automated annotation
pipeline, our compact 7B-parameter model is trained through a comprehensive
regimen: pre-training, instruction fine-tuning, cold start, reinforcement
learning (RL) post-training, and final instruction fine-tuning. Quantitative
evaluations on our introduced benchmark ShortVid-Bench and qualitative
comparisons demonstrate its strong performance in real-world video
comprehension, and it supports zero-shot or fine-tuning with a few samples for
diverse downstream applications. The real-world production deployment of our
model has yielded tangible and measurable improvements in user engagement and
satisfaction, a success supported by its remarkable efficiency, with stress
tests indicating an inference time of just 10 seconds for a one-minute video on
H20 GPU.

**中文摘要**：
真实世界用户生成的短视频，特别是在微信频道和抖音等平台上传播的短视频，主导着移动互联网。然而，当前的大型多模态模型缺乏必要的时序结构化、详细和深入的视频理解能力，而这些能力是有效视频搜索和推荐以及新兴视频应用的基石。理解真实世界的短视频实际上具有挑战性，因为它们包含复杂的视觉元素，视听信息密度高，且节奏快速，专注于情感表达和观点传递。这需要先进的推理能力来有效整合视觉、音频和文本等多模态信息。在这项工作中，我们介绍了ARC-Hunyuan-Video，一个多模态模型，它从头到尾处理原始视频输入中的视觉、音频和文本信号，以实现结构化理解。该模型能够进行多粒度带时间戳的视频字幕生成和摘要、开放式视频问答、时序视频定位和视频推理。利用来自自动化标注流程的高质量数据，我们紧凑的70亿参数模型通过全面的训练流程进行训练：预训练、指令微调、冷启动、强化学习(RL)后训练和最终指令微调。在我们引入的基准ShortVid-Bench上进行定量评估和定性比较，展示了其在真实世界视频理解方面的强大性能，并支持零样本或少样本微调，适用于各种下游应用。我们模型的实际生产部署已在用户参与度和满意度方面带来了切实可衡量的改进，这一成功得益于其卓越的效率，压力测试表明在H20 GPU上处理一分钟视频的推理时间仅为10秒。

**GitHub仓库**：https://github.com/TencentARC/ARC-Hunyuan-Video-7B
**项目页面**：https://tencentarc.github.io/posts/arc-video-announcement/
**模型功能**：多模态视频理解，支持字幕生成、问答、定位和推理，应用于真实世界短视频分析

**分析时间**：2025-08-04T19:54:52.757942
