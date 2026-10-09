# 项目重点版验证与交接

日期：2026-10-09。修订起点：4987e8907befd06b4875537662bf3b28a53de983；完成SHA由交付答复记录。原7页初版保留。

- 8页PPTX/PDF、8页备注；前两页课题，五页现成项目，最后一页总结。计划460秒，未试讲。
- 原图来自三篇既有论文。Zotero API先超时，用户启动后重连成功，版本10.0.5，API/connector均HTTP200；三项file-url及本地附件SHA已核对。未修改Zotero条目或PDF。
- 论文原图5个Figure引用覆盖P3–P7；PhIDO/PICopilot复用已有图，PhIDO局部/Kharel两图从对应PDF裁出，原始坐标、图例与含义保持。原图完整题名/DOI/页码见来源索引，数据条件在页面及备注。
- 构建QA：0溢出、0重叠、0占位、0几何错误/警告、0视觉警告、0设计错误/警告。首张非title的preflight提示与后续拼接的内容型开场一致，保留。
- PowerPoint导出8页PDF与1600×900PNG。主审实际查看全部联系图及关键页；独立只读视觉审查实际查看全部8页，确认关键结构/坐标/图例/引用完整，P8为总结；仅P5文字较靠右，缩短为中文后重新导出并检查。
- ZIP、PPT/PDF/备注页数、源图路径、来源与计划时间检查；提交前运行git diff --check。标题/脚注/讲稿为可编辑对象，原图与图旁注释位图的布局由源脚本编辑，不宣称全部为原生图形。
- 未试讲、未与同学DAS模块实际拼接、未在课堂投影设备验证。未独立复现论文结果或运行Agent/仿真。PICopilot/Kharel公开图片再分发许可未核实，未远程发布或推送。
- 修改范围为当前PPT工作区及docs/TASK.md、docs/CURRENT_STATE.md。用户原有DOCX修改及三个未跟踪PDF未纳入。

## Word 完整讲稿

- 用户追加要求后，按本对话完整口头稿创建DOCX，不修改PPT。源spoken-script.md，构建脚本build_spoken_docx.py。
- 4页A4，每页对应两张PPT，8个标题、8个建议用时、61个正文段落；与源Markdown逐段一致。总时间460秒是规划，未试讲。
- ZIP完整、标题样式黑色且无边框。render_docx.py实际尝试后因缺LibreOffice soffice.exe失败；本机Word COM成功导出4页PDF，bundled Poppler渲染4页PNG并逐页检查。初次模板标题蓝线已从样式移除，重新渲染确认无裁切、重叠或乱码。预览位于忽略的build/docx-review，仅供QA。
- 未上传外部应用，未改动原有用户调研DOCX/PDF。
