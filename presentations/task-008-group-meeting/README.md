# TASK-008 组会调研 PPT 优化版

本目录是 TASK-007 已验收演示文稿的独立优化 workspace。原始文件保持在 `presentations/task-007-group-meeting/`。

## 结构

- 第 1–14 页：15–20 分钟主讲，每页含讲解备注。
- 第 15–25 页：代表工作、系统边界、验证阶梯和反例附录。
- `compose_outline.py`：从 TASK-007 的 `outline.json` 生成此目录的 `outline.json`，并记录主讲页重组与补充。
- `TASK-008-组会调研优化版.pptx`：正式可编辑文件；PDF 为快速预览。

## 构建

```powershell
python presentations/task-008-group-meeting/compose_outline.py
python C:\Users\ASUS\.codex\skills\presentation-skill\scripts\build_workspace.py --workspace presentations/task-008-group-meeting --overwrite
```

该 workspace 的 Markdown 和 JSON 是修改源；正式报告 `references/task-007/formal-research-report.md` 仍是研究事实源。
