# 文本生成

# SmallThinker: 一类专为本地部署高效训练的大型语言模型

**论文ID**：2507.20984
**英文标题**：SmallThinker: A Family of Efficient Large Language Models Natively   Trained for Local Deployment
**中文标题**：SmallThinker: 一类专为本地部署高效训练的大型语言模型
**论文地址**：https://arxiv.org/abs/2507.20984

**作者团队**：Yixin Song, Zhenliang Xue, Dongliang Wei, Feiyang Chen, Jianxiang Gao, Junchen Liu, Hangyu Liang, Guangshuo Qin, Chengrong Tian, Bo Wen, Longyu Zhao, Xinrui Zheng, Zeyu Mi, Haibo Chen
**发表日期**：2025-07-28

**英文摘要**：
While frontier large language models (LLMs) continue to push capability
boundaries, their deployment remains confined to GPU-powered cloud
infrastructure. We challenge this paradigm with SmallThinker, a family of LLMs
natively designed - not adapted - for the unique constraints of local devices:
weak computational power, limited memory, and slow storage. Unlike traditional
approaches that mainly compress existing models built for clouds, we architect
SmallThinker from the ground up to thrive within these limitations. Our
innovation lies in a deployment-aware architecture that transforms constraints
into design principles. First, We introduce a two-level sparse structure
combining fine-grained Mixture-of-Experts (MoE) with sparse feed-forward
networks, drastically reducing computational demands without sacrificing model
capacity. Second, to conquer the I/O bottleneck of slow storage, we design a
pre-attention router that enables our co-designed inference engine to prefetch
expert parameters from storage while computing attention, effectively hiding
storage latency that would otherwise cripple on-device inference. Third, for
memory efficiency, we utilize NoPE-RoPE hybrid sparse attention mechanism to
slash KV cache requirements. We release SmallThinker-4B-A0.6B and
SmallThinker-21B-A3B, which achieve state-of-the-art performance scores and
even outperform larger LLMs. Remarkably, our co-designed system mostly
eliminates the need for expensive GPU hardware: with Q4_0 quantization, both
models exceed 20 tokens/s on ordinary consumer CPUs, while consuming only 1GB
and 8GB of memory respectively. SmallThinker is publicly available at
hf.co/PowerInfer/SmallThinker-4BA0.6B-Instruct and
hf.co/PowerInfer/SmallThinker-21BA3B-Instruct.

**中文摘要**：
尽管前沿大型语言模型(LLMs)不断扩展能力边界，但其部署仍局限于GPU驱动的云基础设施。我们通过SmallThinker挑战这一范式，这是一类专为本地设备的独特约束而原生设计(而非适配)的LLMs：计算能力弱、内存有限和存储速度慢。与传统主要压缩为云构建的现有模型的方法不同，我们从零开始构建SmallThinker架构，使其在这些限制条件下茁壮成长。我们的创新在于一种部署感知架构，将约束转化为设计原则。首先，我们引入了一种两级稀疏结构，结合细粒度专家混合(MoE)与稀疏前馈网络，大幅减少计算需求而不牺牲模型容量。其次，为克服慢速存储的I/O瓶颈，我们设计了一个预注意力路由器，使我们协同设计的推理引擎在计算注意力时能从存储预取专家参数，有效隐藏了否则会破坏设备端推理的存储延迟。第三，为提高内存效率，我们利用NoPE-RoPE混合稀疏注意力机制大幅减少KV缓存需求。我们发布了SmallThinker-4B-A0.6B和SmallThinker-21B-A3B，它们实现了最先进的性能分数，甚至超过了更大的LLMs。值得注意的是，我们协同设计的系统基本消除了对昂贵GPU硬件的需求：采用Q4_0量化后，这两个模型在普通消费级CPU上都能超过20 tokens/s，同时仅消耗1GB和8GB内存。SmallThinker已在hf.co/PowerInfer/SmallThinker-4BA0.6B-Instruct和hf.co/PowerInfer/SmallThinker-21BA3B-Instruct上公开提供。

**GitHub仓库**：暂无
**项目页面**：暂无
**模型功能**：专为本地设备设计的高效大型语言模型，通过创新架构解决计算资源限制，实现高性能本地部署。

**技术特点**：SmallThinker采用原生设计而非传统压缩方法，创新性地结合两级稀疏结构与预注意力路由器，在计算注意力时预取专家参数隐藏存储延迟，并利用NoPE-RoPE混合稀疏注意力机制大幅减少KV缓存需求，实现在普通消费级CPU上高效运行。

**应用场景**：1. 移动端智能助手：在智能手机或平板电脑上运行，提供实时对话、问答和内容创作功能；2. 离线文档处理：在无网络环境下进行文本摘要、翻译和编辑；3. 边缘计算环境：在工业设备或嵌入式系统中提供本地AI服务，确保数据安全与低延迟响应。

**分析时间**：2025-08-04T19:54:49.905729