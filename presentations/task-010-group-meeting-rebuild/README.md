# PIC_Harness_Research 首次正式组会调研 PPT

20 页主讲、无附录。正式成品：

- `PIC_Harness_Research_首次组会调研_20页.pptx`：可编辑 PowerPoint，20 页讲解备注。
- `PIC_Harness_Research_首次组会调研_20页.pdf`：快速检查版。
- `figure-and-evidence-index.md`：逐页图示、论文原图、裁剪、引用和许可。
- `qa-summary.md`：逐页验收、计时安排与验证限制。

## 可重复构建

在仓库根目录运行：

```powershell
python presentations/task-010-group-meeting-rebuild/build_source.py
& 'C:\Users\ASUS\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' C:\Users\ASUS\.codex\skills\presentation-skill\scripts\build_workspace.py --workspace presentations/task-010-group-meeting-rebuild --qa --skip-render --overwrite
```

`build_source.py` 生成 `outline.json` 与 14 张 SVG 技术图。`assets/` 另含四张论文原图局部：ACCEL、PhIDO、PICopilot、AutoPhotonicDesign。PowerPoint COM 用于把 `build/deck-workspace.pptx` 渲染为页面 PNG，并导出 PDF；`build/` 为可再生成产物，正式成品另存于工作区根目录。

页面文案和备注应修改 `build_source.py` 后重建；原论文图可在 `assets/` 更换，图号、裁剪和授权记录同步更新 `figure-and-evidence-index.md`。本演示文稿未运行任何新物理仿真或实验。
