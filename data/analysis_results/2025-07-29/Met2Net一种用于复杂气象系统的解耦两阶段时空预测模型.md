# Met^2Net：一种用于复杂气象系统的解耦两阶段时空预测模型

**论文ID**：2507.17189
**英文标题**：Met^2Net: A Decoupled Two-Stage Spatio-Temporal Forecasting Model for   Complex Meteorological Systems
**中文标题**：Met^2Net：一种用于复杂气象系统的解耦两阶段时空预测模型
**论文地址**：https://arxiv.org/abs/2507.17189

**作者团队**：Shaohan Li, Hao Yang, Min Chen, Xiaolin Qin
**发表日期**：2025-07-23

**英文摘要**：
The increasing frequency of extreme weather events due to global climate
change urges accurate weather prediction. Recently, great advances have been
made by the end-to-end methods, thanks to deep learning techniques,
but they face limitations of representation inconsistency in
multivariable integration and struggle to effectively capture the dependency
between variables, which is required in complex weather systems. Treating
different variables as distinct modalities and applying a two-stage
training approach from multimodal models can partially alleviate this issue,
but due to the inconformity in training tasks between the two stages, the
results are often suboptimal. To address these challenges, we propose an
implicit two-stage training method, configuring separate encoders and decoders
for each variable. In detailed, in the first stage, the Translator is frozen
while the Encoders and Decoders learn a shared latent space, in the second
stage, the Encoders and Decoders are frozen, and the Translator captures
inter-variable interactions for prediction. Besides, by introducing a
self-attention mechanism for multivariable fusion in the latent space, the
performance achieves further improvements. Empirically, extensive experiments
show the state-of-the-art performance of our method. Specifically, it reduces
the MSE for near-surface air temperature and relative humidity predictions by
28.82\% and 23.39\%, respectively. The source code is available at
https://github.com/ShremG/Met2Net.

**中文摘要**：
由于全球气候变化导致极端天气事件日益频繁，准确的天气预报变得至关重要。近年来，得益于深度学习技术，端到端方法取得了重大进展，但在多变量集成中存在表示不一致性的限制，并且难以有效捕捉复杂气象系统中所需的变量间依赖关系。将不同变量视为不同模态并应用来自多模态模型的两阶段训练方法可以部分缓解这一问题，但由于两个阶段训练任务的不一致性，结果往往不尽如人意。为解决这些挑战，我们提出了一种隐式两阶段训练方法，为每个变量配置独立的编码器和解码器。具体而言，在第一阶段，翻译器保持冻结状态，而编码器和解码器学习共享的潜在空间；在第二阶段，编码器和解码器保持冻结，翻译器捕获变量间交互以进行预测。此外，通过在潜在空间中引入多变量融合的自注意力机制，性能得到了进一步提升。实验表明，大量实验证明了我们方法的最新性能。具体而言，它将近地表空气温度和相对湿度预测的均方误差分别降低了28.82%和23.39%。源代码可在 https://github.com/ShremG/Met2Net 获取。

**GitHub仓库**：https://github.com/ShremG/Met2Net
**项目页面**：暂无
**模型功能**：复杂气象系统的时空预测，通过解耦两阶段训练方法捕捉变量间依赖关系，提高天气预报准确性。

**分析时间**：2025-08-04T19:55:09.978721
