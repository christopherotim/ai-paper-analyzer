# DreamScene: 基于3D高斯的全端到端文本到3D场景生成

**论文ID**：2507.13985
**英文标题**：DreamScene: 3D Gaussian-based End-to-end Text-to-3D Scene Generation
**中文标题**：DreamScene: 基于3D高斯的全端到端文本到3D场景生成
**论文地址**：https://arxiv.org/abs/2507.13985

**作者团队**：Haoran Li, Yuli Tian, Kun Lan, Yong Liao, Lin Wang, Pan Hui, Peng Yuan Zhou
**发表日期**：2025-07-18

**英文摘要**：
Generating 3D scenes from natural language holds great promise for
applications in gaming, film, and design. However, existing methods struggle
with automation, 3D consistency, and fine-grained control. We present
DreamScene, an end-to-end framework for high-quality and editable 3D scene
generation from text or dialogue. DreamScene begins with a scene planning
module, where a GPT-4 agent infers object semantics and spatial constraints to
construct a hybrid graph. A graph-based placement algorithm then produces a
structured, collision-free layout. Based on this layout, Formation Pattern
Sampling (FPS) generates object geometry using multi-timestep sampling and
reconstructive optimization, enabling fast and realistic synthesis. To ensure
global consistent, DreamScene employs a progressive camera sampling strategy
tailored to both indoor and outdoor settings. Finally, the system supports
fine-grained scene editing, including object movement, appearance changes, and
4D dynamic motion. Experiments demonstrate that DreamScene surpasses prior
methods in quality, consistency, and flexibility, offering a practical solution
for open-domain 3D content creation. Code and demos are available at
https://jahnsonblack.github.io/DreamScene-Full/.

**中文摘要**：
从自然语言生成3D场景在游戏、电影和设计领域具有巨大应用前景。然而，现有方法在自动化、3D一致性和细粒度控制方面存在困难。我们提出了DreamScene，一个从文本或对话生成高质量且可编辑3D场景的全端到端框架。DreamScene首先从场景规划模块开始，其中GPT-4代理推断对象语义和空间约束以构建混合图。然后，基于图的放置算法生成结构化的无碰撞布局。基于此布局，形成模式采样(FPS)使用多时间步采样和重构优化生成对象几何形状，实现快速且真实的合成。为确保全局一致性，DreamScene采用针对室内和室外环境定制的渐进式相机采样策略。最后，该系统支持细粒度场景编辑，包括对象移动、外观变化和4D动态运动。实验证明，DreamScene在质量、一致性和灵活性方面超越了先前的方法，为开放域3D内容创作提供了实用的解决方案。代码和演示可在https://jahnsonblack.github.io/DreamScene-Full/获取。

**GitHub仓库**：https://github.com/DreamScene-Project/DreamScene
**项目页面**：https://jahnsonblack.github.io/DreamScene-Full/
**模型功能**：基于文本或对话生成高质量且可编辑的3D场景，支持细粒度编辑和4D动态。

**技术特点**：DreamScene创新性地结合GPT-4代理进行场景规划与混合图构建，通过基于图的放置算法生成结构化无碰撞布局，并采用形成模式采样(FPS)技术实现多时间步采样与重构优化，确保快速且真实的几何形状合成，同时支持细粒度场景编辑和4D动态运动。

**应用场景**：游戏开发中快速生成游戏场景和关卡；电影和动画制作中创建场景和背景；室内设计和建筑设计中根据描述生成室内或建筑场景。

**分析时间**：2025-08-04T19:06:37.622204