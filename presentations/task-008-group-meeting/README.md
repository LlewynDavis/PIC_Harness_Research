# TASK-008 组会调研 PPT 优化版

本目录是 TASK-007 已验收演示文稿的独立优化 workspace。原始文件保持在 `presentations/task-007-group-meeting/`。

## 结构

- 第 1–14 页：15–20 分钟主讲，每页含讲解备注；按用户要求不保留附录。
- `compose_outline.py`：从 TASK-007 的 `outline.json` 生成此目录的 `outline.json`，并记录主讲页重组与补充。
- `assets/diagrams/build_explanatory_svgs.py`：生成可追溯的矢量原理图、能力矩阵与路线推导图。
- `assets/paper-figures/`：从本地 Zotero PDF 截取的 PhIDO Fig. 1 与 AutoPhotonicDesign Fig. 1(b)。
- `diagram-sources.md`：逐页图示目的、论文图号、裁剪范围、证据边界与图片使用记录。
- `TASK-008-组会调研优化版.pptx`：正式可编辑文件；PDF 为快速预览。

## 构建

```powershell
python presentations/task-008-group-meeting/assets/diagrams/build_explanatory_svgs.py
python presentations/task-008-group-meeting/compose_outline.py
python C:\Users\ASUS\.codex\skills\presentation-skill\scripts\build_workspace.py --workspace presentations/task-008-group-meeting --qa --skip-render --overwrite
```

该 workspace 的 Python、SVG、Markdown 和 JSON 是可修改来源；原论文局部截图为图片对象。正式报告 `references/task-007/formal-research-report.md` 仍是研究事实源。
