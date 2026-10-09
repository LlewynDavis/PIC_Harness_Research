# Harness 课堂汇报｜项目重点版
制作日期：2026-10-09。当前交付为 Harness_课堂汇报_项目重点版.pptx 与同名 PDF。

完整口头讲稿另交付为 Harness_课堂汇报_完整讲稿.docx，4页、对应8张PPT。源文本为 spoken-script.md，运行 bundled Python 的 build_spoken_docx.py 可重建；speaker-notes.md 是较精简的备注稿。

- 8页、16:9、无附录。P1–P2课题，P3–P7现成项目，P8总结。
- 计划55/55/60/50/65/65/70/40秒，共7分40秒；尚未实际试讲。
- 5页项目引用5个原文 Figure：PhIDO Fig.1/5、PICopilot Fig.2、Kharel Fig.1(b)/2(a)。P4选择模型子图及原始图例，不拼成虚构实验。
- speaker-notes.md 及 PPT 内有逐页讲稿。完整题名、DOI、条件与图片来源见备注及 figure-and-evidence-index.md。
- 标题、页脚、备注可编辑；论文图为原始位图，图旁中文说明与原图明显分开。可在 build_source_projects.py 修改说明和布局；P1/P2/P8为SVG概念图。不是所有图形都为原生形状。
- 原7页初版保留为历史文件；build_source.py是初版源，build_source_projects.py是当前源。

运行 rebuild.ps1 可重建当前 PPT、PDF 和 PowerPoint PNG。本机 bundled runtime、presentation-skill 与 PowerPoint 为依赖。
重新提取原图：系统 Python 已安装 pymupdf，运行 stage_paper_figures.py --storage-root <本机Zotero storage目录>；脚本按附件 key 与 SHA 核对版本，只读PDF。

Zotero API重连成功（10.0.5，HTTP200），附件与既有核读版本一致。本次不扩大论文池、不做实验。PICopilot/Kharel原图公开再分发许可尚未核实，仅交付本地课堂文件，未推送或远程发布。
