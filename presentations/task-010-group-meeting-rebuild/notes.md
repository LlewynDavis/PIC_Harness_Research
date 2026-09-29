# TASK-010 制作说明与 TASK-016 证据增强

- 听众：导师与课题组师兄师姐；首次正式调研汇报。
- 目标：20 页主讲、约 19 分钟；三方向完整介绍，P10–P16 深入 Agentic PIC。
- 结构：新工作区从空白 scaffold 写成；未沿用 TASK-008 的页面结构或视觉布局。此前用户明确要求不保留附录，因此当前交付无附录。
- 来源：TASK-005/006/007 已验收材料和原论文；完整页码及图号见 `figure-and-evidence-index.md`。
- 图示：`build_source.py` 生成解释性 SVG；现行 P6、P13–P15 为四张论文原始 Figure 局部，P5/P9 根据 Jin 2024/Ahmed 2025 原文改绘。SVG 源码可以修改，PPTX 中文字、标题和讲解备注可编辑；原始论文图是图片对象。
- 标注：物理/仿真/系统结果沿用论文作者口径。本项目未运行这些实验或复算指标。P18 是研究问题推导，P19 是个人倾向，不是最终课题。
- 字体和版式：`editorial-minimal`，16:9，正文白底、技术图示用墨绿/蓝/橙表示功能层级。封面为三行标题，避免中文长标题压到副标题。
- Zotero：TASK-010 初版制作时 API 曾超时；TASK-016 已现场确认 API 与 Connector 可用，七篇优先论文的 PDF 均能只读访问。附件 key、哈希、页码见 `references/task-016-evidence/source-manifest.md`；未修改文献库。
- 讲解备注：全部 20 页写在 `outline.json` 的 `notes` 字段并进入 PPTX notes slide。
- 版权：现行 P6 Cheng 与 P13 PhIDO 为 CC BY 4.0；P14 PICopilot 和 P15 Kharel 沿用既有带署名局部裁图，未确认公开再分发许可。公开发布演示文稿前须核权利或改绘 P14/P15。Jin 2024、Sandmann 2023、Ahmed 2025 的原图未新增复制。
- TASK-016 数据边界：P5 的 12.1/49.0 km 指标条件、P6 的器件电耗、P9 的任务准确率与操作吞吐、P13 的 `S` 定义、P14 的内部/外部反馈区别、P15 的专家纠错均已写入讲解备注；本项目未复算实验。
