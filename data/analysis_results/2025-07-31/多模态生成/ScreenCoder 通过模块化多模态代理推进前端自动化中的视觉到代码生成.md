# ScreenCoder: 通过模块化多模态代理推进前端自动化中的视觉到代码生成

**论文ID**：2507.22827
**英文标题**：ScreenCoder: Advancing Visual-to-Code Generation for Front-End Automation via Modular Multimodal Agents
**中文标题**：ScreenCoder: 通过模块化多模态代理推进前端自动化中的视觉到代码生成
**论文地址**：https://arxiv.org/abs/2507.22827

**作者团队**：Yilei Jiang, Yaozhi Zheng, Yuxuan Wan, Jiaming Han, Qunzhong Wang, Michael R. Lyu, Xiangyu Yue
**发表日期**：2025-07-30

**英文摘要**：
Automating the transformation of user interface (UI) designs into front-end
code holds significant promise for accelerating software development and
democratizing design workflows. While recent large language models (LLMs) have
demonstrated progress in text-to-code generation, many existing approaches rely
solely on natural language prompts, limiting their effectiveness in capturing
spatial layout and visual design intent. In contrast, UI development in
practice is inherently multimodal, often starting from visual sketches or
mockups. To address this gap, we introduce a modular multi-agent framework that
performs UI-to-code generation in three interpretable stages: grounding,
planning, and generation. The grounding agent uses a vision-language model to
detect and label UI components, the planning agent constructs a hierarchical
layout using front-end engineering priors, and the generation agent produces
HTML/CSS code via adaptive prompt-based synthesis. This design improves
robustness, interpretability, and fidelity over end-to-end black-box methods.
Furthermore, we extend the framework into a scalable data engine that
automatically produces large-scale image-code pairs. Using these synthetic
examples, we fine-tune and reinforce an open-source VLM, yielding notable gains
in UI understanding and code quality. Extensive experiments demonstrate that
our approach achieves state-of-the-art performance in layout accuracy,
structural coherence, and code correctness. Our code is made publicly available
at https://github.com/leigest519/ScreenCoder.

**中文摘要**：
将用户界面(UI)设计自动转换为前端代码，对于加速软件开发和民主化设计工作流程具有巨大潜力。尽管最近的大型语言模型(LLMs)在文本到代码生成方面已经取得了进展，但许多现有方法仅依赖自然语言提示，限制了它们在捕获空间布局和视觉设计意图方面的有效性。相比之下，UI开发在实践中本质上是多模态的，通常从视觉草图或模型开始。为了解决这一差距，我们引入了一个模块化多代理框架，它通过三个可解释的阶段执行UI到代码的生成：基础、规划和生成。基础代理使用视觉语言模型检测和标记UI组件，规划代理使用前端工程先验知识构建分层布局，生成代理通过自适应提示合成产生HTML/CSS代码。这种设计比端到端的黑盒方法提高了鲁棒性、可解释性和保真度。此外，我们将框架扩展为一个可扩展的数据引擎，自动生成大规模的图像-代码对。使用这些合成示例，我们对开源VLM进行了微调和强化，在UI理解和代码质量方面取得了显著提升。大量实验表明，我们的方法在布局准确性、结构连贯性和代码正确性方面达到了最先进的性能。我们的代码已在https://github.com/leigest519/ScreenCoder公开提供。

**GitHub仓库**：https://github.com/leigest519/ScreenCoder
**项目页面**：https://hf-mirror.com/spaces/Jimmyzheng-10/ScreenCoder
**模型功能**：通过模块化多代理框架将UI设计自动转换为前端代码，提高布局准确性和代码质量。

**技术特点**：采用模块化多代理框架，通过三个可解释阶段（基础、规划、生成）执行UI到代码的转换，比端到端黑盒方法提高了鲁棒性、可解释性和保真度；结合视觉语言模型和前端工程先验知识，能够准确捕获UI组件的视觉特征并构建合理的分层布局结构；开发了可扩展的数据引擎自动生成大规模图像-代码对，用于微调和强化开源VLM，显著提升了UI理解和代码生成质量。

**应用场景**：设计师到开发者的工作流自动化，将UI草图或模型自动转换为高质量前端代码，减少手动编码时间；快速原型开发，帮助产品团队将设计稿迅速转换为可交互的前端原型，加速产品迭代；网站和应用界面重构，分析现有设计稿并生成更新后的代码，高效完成界面升级。

**分析时间**：2025-08-04T19:06:11.697897