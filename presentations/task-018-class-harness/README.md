# Harness 课堂汇报 可编辑版
制作日期：2026-10-09。当前交付为 Harness_课堂汇报_可编辑版.pptx 与同名 PDF；项目重点版文件同步更新为相同原生对象版本。

完整口头讲稿另交付为 Harness_课堂汇报_完整讲稿.docx，4页、对应8张PPT。源文本为 spoken-script.md，运行 bundled Python 的 build_spoken_docx.py 可重建；speaker-notes.md 是较精简的备注稿。

- 8页、16:9、无附录。P1–P2课题，P3–P7现成项目，P8总结。
- 计划55/55/60/50/65/65/70/40秒，共7分40秒；尚未实际试讲。
- 5页项目引用5个原文 Figure：PhIDO Fig.1/5、PICopilot Fig.2、Kharel Fig.1(b)/2(a)。P4选择模型子图及原始图例，不拼成虚构实验。
- speaker-notes.md 及 PPT 内有逐页讲稿。完整题名、DOI、条件与图片来源见备注及 figure-and-evidence-index.md。
- 93个原生文本对象，文字、说明框、框图、箭头和总结可逐项修改；P1/P2/P8没有图片。论文原图是6个独立图片对象，可单独移动、缩放、裁剪或替换。原图内部文字和曲线仍属于原始位图，没有误称为可编辑数据图。
- 原7页初版保留。build_source.py、build_source_projects.py为历史源；当前源为build_source_editable.py及outline.json的native_elements，build_native.cjs是工作区原生渲染扩展，调用标准技能的CLI而不修改技能安装文件。

运行 rebuild.ps1 可重建当前原生PPT、PDF和PowerPoint PNG，并执行对象/原图检查。本机 bundled runtime、presentation-skill 与 PowerPoint 为依赖。不要直接以通用build_workspace.py替代本工作区原生扩展，否则自定义native_elements不会被渲染。verify_native.py与verify_editability.ps1分别验证OOXML对象及PowerPoint临时编辑保存重开；记录见editability-check.json和editability-proof.txt。
重新提取原图：系统 Python 已安装 pymupdf，运行 stage_paper_figures.py --storage-root <本机Zotero storage目录>；脚本按附件 key 与 SHA 核对版本，只读PDF。

Zotero API重连成功（10.0.5，HTTP200），附件与既有核读版本一致。本次不扩大论文池、不做实验。PICopilot/Kharel原图公开再分发许可尚未核实，仅交付本地课堂文件，未推送或远程发布。
