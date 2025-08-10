# Step-3规模大却经济实惠：面向成本效益解码的模型-系统协同设计

**论文ID**：2507.19427
**英文标题**：Step-3 is Large yet Affordable: Model-system Co-design for Cost-effective Decoding
**中文标题**：Step-3规模大却经济实惠：面向成本效益解码的模型-系统协同设计
**论文地址**：https://arxiv.org/abs/2507.19427

**作者团队**：StepFun, Bin Wang, Bojun Wang, Changyi Wan, Guanzhe Huang, Hanpeng Hu, Haonan Jia, Hao Nie, Mingliang Li, Nuo Chen, Siyu Chen, Song Yuan, Wuxun Xie, Xiaoniu Song, Xing Chen, Xingping Yang, Xuelin Zhang, Yanbo Yu, Yaoyu Wang, Yibo Zhu, Yimin Jiang, Yu Zhou, Yuanwei Lu, Houyi Li, Jingcheng Hu, Ka Man Lo, Ailin Huang, Binxing Jiao, Bo Li, Boyu Chen, Changxin Miao, Chang Lou, Chen Hu, Chen Xu, Chenfeng Yu, Chengyuan Yao, Daokuan Lv, Dapeng Shi, Deshan Sun, Ding Huang, Dingyuan Hu, Dongqing Pang, Enle Liu, Fajie Zhang, Fanqi Wan, Gulin Yan, Han Zhang, Han Zhou, Hanghao Wu, Hangyu Guo, Hanqi Chen, Hanshan Zhang, Hao Wu, Haocheng Zhang, Haolong Yan, Haoran Lv, Haoran Wei, Hebin Zhou, Heng Wang, Heng Wang, Hongxin Li, Hongyu Zhou, Hongyuan Wang, Huiyong Guo, Jia Wang, Jiaohao Gong, Jialing Xie, Jian Zhou, Jianjian Sun, Jiaoren Wu, Jiaran Zhang, Jiayu Liu, Jie Cheng, Jie Luo, Jie Yan, Jie Yang, Jieyi Hou, Jinguang Zhang, Jinlan Cao, Jisheng Yin, Junfeng Liu, Junhao Huang, Junzhe Lin, Kaijun Tan, Kaixiang Li, Kang An, Kangheng Lin, Kenkun Liu, Lei Yang, Liang Zhao, Liangyu Chen, Lieyu Shi, Liguo Tan, Lin Lin, Lin Zhang, Lina Chen, Liwen Huang, Liying Shi, Longlong Gu, Mei Chen, Mengqiang Ren, Ming Li, Mingzhe Chen, Na Wang, Nan Wu, Qi Han, Qian Zhao, Qiang Zhang, Qianni Liu, Qiaohui Chen, Qiling Wu, Qinglin He, Qinyuan Tan, Qiufeng Wang, Qiuping Wu, Qiuyan Liang, Quan Sun, Rui Li, Ruihang Miao, Ruosi Wan, Ruyan Guo, Shangwu Zhong, Shaoliang Pang, Shengjie Fan, Shijie Shang, Shilei Jiang, Shiliang Yang, Shiming Hao, Shuli Gao, Siming Huang, Siqi Liu, Tiancheng Cao, Tianhao Cheng, Tianhao Peng, Wang You, Wei Ji, Wen Sun, Wenjin Deng, Wenqing He, Wenzhen Zheng, Xi Chen, Xiangwen Kong, Xianzhen Luo, Xiaobo Yang, Xiaojia Liu, Xiaoxiao Ren, Xin Han, Xin Li, Xin Wu, Xu Zhao, Yanan Wei, Yang Li, Yangguang Li, Yangshijie Xu, Yanming Xu, Yaqiang Shi, Yeqing Shen, Yi Yang, Yifei Yang, Yifeng Gong, Yihan Chen, Yijing Yang, Yinmin Zhang, Yizhuang Zhou, Yuanhao Ding, Yuantao Fan, Yuanzhen Yang, Yuchu Luo, Yue Peng, Yufan Lu, Yuhang Deng, Yuhe Yin, Yujie Liu, Yukun Chen, Yuling Zhao, Yun Mou, Yunlong Li, Yunzhou Ju, Yusheng Li, Yuxiang Yang, Yuxiang Zhang, Yuyang Chen, Zejia Weng, Zhe Xie, Zheng Ge, Zheng Gong, Zhenyi Lu, Zhewei Huang, Zhichao Chang, Zhiguo Huang, Zhirui Wang, Zidong Yang, Zili Wang, Ziqi Wang, Zixin Zhang, Binxing Jiao, Daxin Jiang, Heung-Yeung Shum, Xiangyu Zhang
**发表日期**：2025-07-25

**英文摘要**：
Large language models (LLMs) face low hardware efficiency during decoding,
especially for long-context reasoning tasks. This paper introduces Step-3, a
321B-parameter VLM with hardware-aware model-system co-design optimized for
minimizing decoding costs. Step-3 innovates in two key dimensions: (1) A novel
Multi-Matrix Factorization Attention (MFA) mechanism that significantly reduces
both KV cache size and computation while maintaining high attention
expressiveness, and (2) Attention-FFN Disaggregation (AFD), a distributed
inference system that decouples attention and Feed-Forward Network (FFN) layers
into specialized subsystems. This co-design achieves unprecedented cost
efficiency: Step-3 significantly reduces theoretical decoding costs compared
with models like DeepSeek-V3 and Qwen3 MoE 235B, with the gains widening at
longer context. Step-3 achieves low cost while activating 38B parameters per
token (more than DeepSeek-V3 and Qwen3 MoE 235B), demonstrating that
hardware-aligned attention arithmetic intensity, MoE sparsity, and AFD are
critical to cost-effectiveness. We perform a head-to-head comparison with
DeepSeek-V3 in its favorable scenarios. Our implementation on Hopper GPUs
achieves a decoding throughput of up to 4,039 tokens per second per GPU under
50ms TPOT SLA (4K context, FP8, no MTP). It is higher than DeepSeek-V3's 2,324
in the same setup and sets a new Pareto frontier for LLM decoding.

**中文摘要**：
大型语言模型(LLMs)在解码过程中面临硬件效率低下的问题，尤其是在长上下文推理任务中。本文介绍了Step-3，一个具有硬件感知的模型-系统协同设计优化的3210亿参数VLM(视觉语言模型)，旨在最小化解码成本。Step-3在两个关键维度上进行了创新：(1) 一种新颖的多矩阵分解注意力(MFA)机制，在保持高注意力表达能力的同时，显著减少了KV缓存大小和计算量；(2) 注意力-前馈网络解耦(AFD)，一种分布式推理系统，将注意力和前馈网络(FFN)层解耦到专门的子系统中。这种协同设计实现了前所未有的成本效率：与DeepSeek-V3和Qwen3 MoE 235B等模型相比，Step-3显著降低了理论解码成本，且在更长上下文时优势更加明显。Step-3在激活每token 380亿参数(多于DeepSeek-V3和Qwen3 MoE 235B)的同时实现了低成本，这表明硬件对齐的注意力计算强度、MoE稀疏性和AFD对成本效益至关重要。我们在DeepSeek-V3的有利场景下进行了直接比较。在Hopper GPU上的实现下，在50ms TPOT SLA(4K上下文，FP8，无MTP)条件下，每GPU解码吞吐量高达4,039 tokens/秒，高于相同设置下DeepSeek-V3的2,324，为LLM解码设立了新的帕累托前沿。

**GitHub仓库**：暂无
**项目页面**：暂无
**模型功能**：面向长上下文推理的高效解码模型，通过创新协同设计显著降低解码成本。

**技术特点**：多矩阵分解注意力(MFA)机制在保持高表达能力的同时显著减少KV缓存和计算量；注意力-前馈网络解耦(AFD)分布式系统将模型层解耦到专门子系统，实现硬件对齐的注意力计算强度和MoE稀疏性，大幅提升解码效率。

**应用场景**：长文档处理与分析系统，如学术论文摘要生成；大规模多轮对话系统，支持长上下文连贯交互；资源受限环境下的智能客服系统，实现高吞吐量低成本的实时响应。

**分析时间**：2025-08-04T19:06:24.669645