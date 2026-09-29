# PIC_Harness_Research 首次正式组会调研 PPT

20 页主讲、无附录。正式成品：

- `PIC_Harness_Research_首次组会调研_20页.pptx`：可编辑 PowerPoint，20 页讲解备注。
- `PIC_Harness_Research_首次组会调研_20页.pdf`：快速检查版。
- `figure-and-evidence-index.md`：逐页图示、论文原图、裁剪、引用和许可。
- `qa-summary.md`：逐页验收、计时安排与验证限制。

2026-09-29 的 TASK-016 证据增强版保留 20 页结构：P5 使用 Jin 2024 带条件 DAS 证据，P6 新增 Cheng 2023 CC BY 原图，P9 根据 Ahmed 2025 系统图改绘；P13–P16 补足 PhIDO/PICopilot/Kharel 的 benchmark 定义、内部反馈与数值验收边界。逐项数据与 UNKNOWN 位于 [`references/task-016-evidence/`](../../references/task-016-evidence/README.md)。已有 DOCX 用户改动未被本轮构建覆盖。

## 可重复构建

在仓库根目录运行：

```powershell
python presentations/task-010-group-meeting-rebuild/build_source.py
& 'C:\Users\ASUS\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' C:\Users\ASUS\.codex\skills\presentation-skill\scripts\build_workspace.py --workspace presentations/task-010-group-meeting-rebuild --qa --skip-render --overwrite
```

`build_source.py` 生成 `outline.json` 与解释性 SVG 技术图。现行页面使用四张论文原图局部：Cheng、PhIDO、PICopilot、Kharel；`assets/` 保留初版 ACCEL 资源但现行 P9 不再引用。PowerPoint COM 用于把 `build/deck-workspace.pptx` 渲染为页面 PNG，并导出 PDF；`build/` 为可再生成产物，正式成品另存于工作区根目录。

页面文案和备注应修改 `build_source.py` 后重建；原论文图可在 `assets/` 更换，图号、裁剪和授权记录同步更新 `figure-and-evidence-index.md`。本演示文稿未运行任何新物理仿真或实验。
