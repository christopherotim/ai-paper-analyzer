# JAM：一款具有细粒度可控性和美学对齐功能的小型基于流的歌曲生成器

**论文ID**：2507.20880
**英文标题**：JAM: A Tiny Flow-based Song Generator with Fine-grained Controllability   and Aesthetic Alignment
**中文标题**：JAM：一款具有细粒度可控性和美学对齐功能的小型基于流的歌曲生成器
**论文地址**：https://arxiv.org/abs/2507.20880

**作者团队**：Renhang Liu, Chia-Yu Hung, Navonil Majumder, Taylor Gautreaux, Amir Ali Bagherzadeh, Chuan Li, Dorien Herremans, Soujanya Poria
**发表日期**：2025-07-28

**英文摘要**：
Diffusion and flow-matching models have revolutionized automatic
text-to-audio generation in recent times. These models are increasingly capable
of generating high quality and faithful audio outputs capturing to speech and
acoustic events. However, there is still much room for improvement in creative
audio generation that primarily involves music and songs. Recent open
lyrics-to-song models, such as, DiffRhythm, ACE-Step, and LeVo, have set an
acceptable standard in automatic song generation for recreational use. However,
these models lack fine-grained word-level controllability often desired by
musicians in their workflows. To the best of our knowledge, our
flow-matching-based JAM is the first effort toward endowing word-level timing
and duration control in song generation, allowing fine-grained vocal control.
To enhance the quality of generated songs to better align with human
preferences, we implement aesthetic alignment through Direct Preference
Optimization, which iteratively refines the model using a synthetic dataset,
eliminating the need or manual data annotations. Furthermore, we aim to
standardize the evaluation of such lyrics-to-song models through our public
evaluation dataset JAME. We show that JAM outperforms the existing models in
terms of the music-specific attributes.

**中文摘要**：
扩散模型和流匹配模型最近彻底改变了自动文本到音频生成。这些模型越来越能够生成高质量、忠实的音频输出，捕捉语音和声学事件。然而，在主要涉及音乐和歌曲的创意音频生成方面仍有很大的改进空间。最近的开放歌词到歌曲模型，如DiffRhythm、ACE-Step和LeVo，已经为休闲用途的自动歌曲生成设定了可接受的标准。然而，这些模型缺乏音乐人在工作流程中通常需要的细粒度词级可控性。据我们所知，我们基于流匹配的JAM是首次尝试在歌曲生成中赋予词级时间和持续时间控制，从而实现细粒度的声乐控制。为了提高生成歌曲的质量，使其更好地符合人类偏好，我们通过直接偏好优化实现了美学对齐，该方法使用合成数据集迭代地改进模型，消除了手动数据标注的需要。此外，我们旨在通过我们的公共评估数据集JAME来标准化此类歌词到歌曲模型的评估。我们表明，JAM在音乐特定属性方面优于现有模型。

**GitHub仓库**：https://github.com/declare-lab/jamify
**项目页面**：https://declare-lab.github.io/jamify
**模型功能**：基于流匹配的歌曲生成器，提供词级时间控制和美学对齐功能，生成高质量音乐。

**分析时间**：2025-08-04T19:55:12.355897
