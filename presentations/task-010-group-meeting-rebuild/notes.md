# TASK-010 制作说明

- 听众：导师与课题组师兄师姐；首次正式调研汇报。
- 目标：20 页主讲、约 19 分钟；三方向完整介绍，P10–P16 深入 Agentic PIC。
- 结构：新工作区从空白 scaffold 写成；未沿用 TASK-008 的页面结构或视觉布局。此前用户明确要求不保留附录，因此当前交付无附录。
- 来源：TASK-005/006/007 已验收材料和原论文；完整页码及图号见 `figure-and-evidence-index.md`。
- 图示：`build_source.py` 生成 14 张解释性 SVG；P9、P13–P15 为四张论文原始 Figure 局部。SVG 源码可以修改，PPTX 中文字、标题和讲解备注可编辑；原始论文图是图片对象。
- 标注：物理/仿真/系统结果沿用论文作者口径。本项目未运行这些实验或复算指标。P18 是研究问题推导，P19 是个人倾向，不是最终课题。
- 字体和版式：`editorial-minimal`，16:9，正文白底、技术图示用墨绿/蓝/橙表示功能层级。封面为三行标题，避免中文长标题压到副标题。
- Zotero：本次本地 API 超时；直接只读使用已定位的 PhIDO、PICopilot、AutoPhotonicDesign PDF。未修改文献库。
- 讲解备注：全部 20 页写在 `outline.json` 的 `notes` 字段并进入 PPTX notes slide。
- 版权：ACCEL、PhIDO 为 CC BY 4.0；PICopilot 和 AutoPhotonicDesign 未确认开放复用授权，仅用于带署名的内部学术汇报引用。若公开发布演示文稿，需要先复核授权或改绘这两张图。
