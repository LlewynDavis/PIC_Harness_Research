# TASK-016 DOCX 与网页端增补交接

日期：2026-09-29。起点：`e3a3f8316c0b18d7b2f890ba6f921fdb41a0f9ef`。状态：待 GPT 最终只读审查；本记录不代表验收。

## 修改与证据范围

- `output/task-007/面向光子芯片智能设计的三方向技术调研_飞书上传版.docx`：在用户当前已修改版本上局部插入七篇代表工作的“判断—原图或原文定位—数据/条件—证据边界”内容，以及 PhIDO/PICopilot/Kharel 八列比较与 UNKNOWN。四张新增原图分别为 Cheng Fig. 1、Fig. 2，PhIDO Fig. 1、Fig. 5；版权许可未核实的论文图不嵌入。
- `scripts/update_task016_feishu_docx.py`：一次性、可核查的局部 DOCX 增补脚本；检测到 TASK-016 标记后拒绝重复插入。当前 DOCX 写入前已另存本机临时备份。
- `scripts/sync_task016_portal.py`：从 `references/` 事实源生成门户报告与证据页，复制三张已许可证据图和数据 CSV；PICopilot/Kharel 原图以 DOI、图号、PDF 页码定位代替。新增导航并让 `portal/serve.ps1` 在严格构建前同步。
- 源报告元数据更新为 2026-09-29 的七篇定向核读，原候选论文池截止日期 2026-09-21 保留在括注。证据和判断以 `README.md`、`evidence-log.md`、`key-data.csv` 及 `figure-sources.md` 为准。

## 已执行检查

| 检查 | 结果 |
|---|---|
| DOCX 完整性与原内容保留 | ZIP 检查通过；原 231 个段落按顺序保留，原 6 张表按顺序保留，原 2 张图片仍在；用户改动的“证据截止：2026-09-29”保留。增补后为 263 段、13 表、6 图。 |
| DOCX 逐页视觉检查 | 本机 Word COM 导出 28 页 PDF，渲染 28 页 PNG；联系图逐页及关键页全尺寸审阅，未见正文/表格裁切、重叠或乱码。八列比较位于独立页面。内置 `render_docx.py` 因缺少 `soffice.exe` 未运行成功，已使用 Word 导出替代。 |
| 门户构建 | `.venv\Scripts\python.exe -m mkdocs build --strict` 成功，无 warning/error；既有 TASK-006 页面绝对链接仍输出 INFO。 |
| 网页资源与视觉 | 正式报告和证据页的相对链接目标、八个跨页锚点、三张嵌入图片路径均存在；浏览器检查证据页导航、七篇内容、图表和来源标注，未见空白或破图。 |

## 尚未执行与 UNKNOWN

- 未将 DOCX 实际上传飞书，也未核验飞书导入后的排版。
- 未将本地 Research Portal 远程发布；仅验证本地构建与浏览器呈现。
- 未独立复现实验、重算论文原始运行日志或核验完整系统墙插能耗。PICopilot/Kharel 图像再分发许可未核实；网页不分发这两图。其余未核实项仍见[证据包 UNKNOWN](README.md#unknown)。
- 未改动用户已有且未跟踪的同名 PDF。

## 本次 completion commit 修改文件

| 范围 | 文件 |
|---|---|
| DOCX 与脚本 | `output/task-007/面向光子芯片智能设计的三方向技术调研_飞书上传版.docx`；`scripts/update_task016_feishu_docx.py` |
| 报告事实源与记录 | `references/task-007/formal-research-report.md`；`references/task-016-evidence/{README.md,evidence-log.md,handoff.md,docx-portal-qa.md}` |
| 门户同步 | `scripts/sync_task016_portal.py`；`portal/serve.ps1`；`portal/docs/{index.md,task-007-report.md}`；`mkdocs.yml` |
| 门户证据副本 | `portal/docs/task-016-evidence/{README.md,agentic-pic-comparison.md,evidence-log.md,figure-sources.md,key-data.csv,source-manifest.md}`；`figures/{cheng-fig1-device-spectrum.png,cheng-fig2-extinction.png,phido-fig5-complexity.png}` |
| 项目事实源与说明 | `README.md`；`docs/{TASK.md,CURRENT_STATE.md}` |
