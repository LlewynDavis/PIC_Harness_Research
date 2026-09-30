# TASK-017 候选方向同步交接与核查

状态：`REVIEW_READY`，2026-09-30。起始 commit：`de0121904a3922836692d8448c22932a95dc085a`，分支 `main`；完成 commit 由最终交接答复给出。

## 来源与更新范围

直接授权来源是用户本轮附件“当前新的候选课题主线”，以及“保留我之前对调研报告的修改”。附件路径为本地 Codex attachments 中 `3cdb1ec6-844a-4c6a-85a1-4b633e68f3aa/已粘贴的文本.txt`。没有扩大文献池或修改既有证据截止日。

- 详细 Markdown 事实源：`references/task-007/candidate-research-direction.md`，十项分析、三幅概念图、五类方法比較与 H1–H3。
- 正式报告 Markdown 新增 §6.6；用户当前 DOCX 在第六章末局部增补同源详细内容。
- 门户新增首页、左导航入口及候选方向页；生成脚本对原 Markdown 只做相对链接适配。
- 当前 20 页 PPT 主改 P18/P19，P20 最小一致性修正；前 17 页的 outline 对象保持不变，没有大规模重构。

## DOCX 用户编辑保留

- 编辑前完整备份在 `tmp/task-017/report-user-baseline.docx`（本地忽略目录）。基线 SHA-256 与输出 SHA-256 见 `docx-preservation.json`。
- 逐 XML 块有序子序列比较：**282/282** 原正文块完全保留，包含格式、超链接、原有表格和图片关系引用。
- 原有 **13 张表、10 个媒体文件**保留；媒体按原包路径逐字节比较，styles/settings 采用 XML canonicalization 比较，均相同。新增 3 张表、3 幅自绘概念图，总表数 16。
- Word 只读导出 PDF 到 `tmp/task-017/docx/report.pdf`，共 **33 页**；六张联系图覆盖全部页面，新章节 P25–P29 全尺寸检查，未见裁切、表行拆断或乱码。
- 本机缺少 `soffice`，沿用已有可用 Word COM + bundled Poppler 渲染路径。PDF 只作为本地 QA，不替换用户已有 PDF；未上传飞书。
- 生成脚本 `scripts/update_task017_candidate_direction.py` 是一次性受保护插入脚本，已运行后拒绝重复增补；不要直接重跑旧全量 DOCX builder。

## PPT 与门户检查

- PPT：`build_workspace.py --qa --skip-render --overwrite`，20 页，溢出/重叠/占位/视觉警告/设计错误与警告均为 0；**14 条图示面积密度提示仍存在**，不宣称所有提示为零。
- PowerPoint 只读导出 20 张 PNG 与 PDF。P18–P20 全尺寸审阅；独立视觉审查指出回环/换行后修复，第二轮复查通过。原有纸面证据图和讲解备注保留。
- 门户：`mkdocs build --strict` 通过；已有路径绝对链接为 INFO 提示。候选页新链接无失效；浏览器实际检查 1920×1080，**3/3 Mermaid SVG**渲染、**18 条站内链接/锚点**可用，页面 JS error 为 0。只检查桌面，不做手机视口。
- Playwright CLI 未预装，不新增依赖；改用已有 bundled Playwright headless 进行本地只读检查，无 Computer Use。渲染脚本为 `scripts/check_task017_portal.cjs`。
- 首页本地入口：`http://127.0.0.1:8017/`；候选方向：`http://127.0.0.1:8017/task-007-candidate-direction.html`。该地址为本轮静态预览服务，不是远程发布。
- 常规启动：在仓库运行 `.\.venv\Scripts\python.exe -m mkdocs serve -a 127.0.0.1:8000`，访问 `http://127.0.0.1:8000/task-007-candidate-direction.html`。

## 研究边界与对抗性复核

`scientific-critical-thinking` 影响本轮措辞与比较：不把用户倾向当事实，不把既有能力擦除来制造 Research Gap，优先写清反例、假设和简单替代。

- 最强反例是 AutoPhotonicDesign 已有真实 solver 反馈与自主迭代；“现有 PIC Agent 只会生成脚本”与既有证据冲突，三端未采用此表述。
- 专家纠正多物理初设说明输入/模型条件边界，不证明所有 Agent 均无诊断能力。
- H1 缺口、H2 可靠性增益、H3 相对优化价值仍 UNKNOWN；没有同预算实验，不能宣称改进、首次解决或不可替代性。
- 双层职责、诊断预测、候选验证层级为 INFERENCE / USER RESEARCH PREFERENCE；DAS 的最终角色和硕士系统边界需导师确认。
- 五方法比较是概念分类，不是实验排名；传统优化与逆设计有交集，工具调用 Agent 可能已有诊断能力。
- `FACT` 指已有文献内容核读事实；性能仍 AUTHOR CLAIM；本轮没有新增 CODE VERIFIED 结果。

## 分工、未执行与剩余工作

- Codex 负责用户 DOCX 局部编辑、报告/门户/PPT 一致性、既有证据复核、测试与交付。独立只读视觉审查完成两轮。
- Qwen 非交互主科研 CLI 会话已派发一项只读证据/措辞审查，无写权限、无新调研；请求返回 `[API Error: Connection error. (cause: read ECONNRESET)]`，**未收到结果，不计入完成贡献，不据其输出形成结论**。
- 未执行新文献搜索、代码/求解器/benchmark 运行、物理实验、最终选题、Jev 调研或接入、GitHub push、飞书上传、远程门户发布。
- 工作树最终仍有两个用户预先存在的未跟踪 PDF；仅提交本任务修改，不纳入或删除这些文件。TASK-016 历史 REVIEW_READY 不自行升级为验收。
- 下一步是用户/GPT/导师审查候选概念与 H1–H3，而非自动启动实验或开发。
