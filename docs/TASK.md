# 当前任务与任务记录

## TASK-021：Agent 仿真反馈决策路径比较与新报告辅助整理

- 状态：`ACTIVE`（2026-10-14）；用户已授权重新整理仅聚焦最高层级 Agent 的报告，并要求继续原流程。编号为本仓库顺序登记，不改变旧任务验收。
- 起点：`1f5b3120fffa9b267d65cf2e23f5aff6df294dcf`，`main`。开始时三个已跟踪 Office 文件有用户修改、三个 PDF 未跟踪，全部保留。
- 当前研究对象（2026-10-15 用户确认）：AI 根据真实需求、物理规律和制造约束，完成可靠的器件与电路设计。电路层面先纳入器件组合、连接关系和功能/响应评价；版图、路由与完整制造验证按已有证据比较，不扩大为本轮实施任务。
- 当前切入口：保留反馈驱动的决策，将“优化动作选择”提升为“设计方案与修复动作选择”。此前用户原问题“Agent 如何依据仿真反馈，合理选择修复设置、继续调参或改变策略，使优化更可靠地继续推进？”作为切入口形成历史保留；波导弯曲损耗作为案例，不作为整个研究对象。
- 本轮追加授权：以用户当前文件为基线局部修改前三章，先留存修改前快照；同步大纲、任务、状态与决策。第四章及后续章节继续讨论后撰写，不覆盖旧报告或用户 Office/PDF。
- 本次允许写入：新增 `references/task-021/` 独立比较工作稿、流程覆盖图、原文/源码证据索引及 QA；更新任务、状态、决策。辅助用户形成理解和判断，不把助手推断写成用户的理解，不替用户最终定题。
- 保留：TASK-004/005/006/007 和后续补充成果、现有 DOCX/PPT/PDF 及门户；旧报告作为引用，不覆盖重建。DAS 仅背景；本轮不扩展光子 AI 计算。商业求解器可以纳入比较，不强制全开源。
- 长期记忆/跨任务持续进化：`DEFERRED / 待研究`，按用户最新要求仅保留观点，不作为本轮主模块。当前任务内的迭代记录仍属已有方法基础。Jev 继续使用用户此前确认的 `DEFERRED`，不启动调研或接入。
- 禁止：实验设计/执行、器件仿真、Harness 工程开发、最终路线选定、旧项目迁移、Zotero 修改、远程发布；不把个人就业/技能考量写进调研方案。不做手机视口。
- 时间：用户要求本周末交报告；按当前日期理解为 2026-10-17/18，计划 10-16 形成可读初稿，具体提交日尚未指定。不宣称初稿或正式 DOCX 已完成。
- 验证：证据定位/版本、覆盖图与文字一致、链接和 SVG 结构、`git diff --check`；用户已有六个文件前后 SHA-256 保持一致。未复现外部系统，源码只读检查不等于运行验证。
- 本轮交付进度：独立工作稿、证据索引与覆盖图已落盘。PNG 已渲染目视检查；36 个图表状态一致、15 个本地链接可解析、`git diff --check` 通过、六个用户原文件哈希不变。详见 `references/task-021/qa-and-progress.md`。新正式报告未完成，任务保持 `ACTIVE`；旧 TASK-020 等 `REVIEW_READY` 记录仍为历史待审，不自动验收。
- 继续流程进度：新增三张反馈决策证据卡，定向补核固定版本 RF 指令/晋升函数和 bend 平台期/联合搜索轨迹；推荐细化为探索/确认区分、条件性平台期及动作预期证据。增补后 20 个本地链接可解析，六个用户原文件哈希仍不变，`git diff --check` 通过。没有证明新方法收益或实际错误晋升，报告内容仍待用户理解与判断。
- 用户已确认六章大纲，第五章深入一条初步推荐方案，其余简表比较；授权按章节讨论撰写，从第一章开始。允许在 `references/task-021/chapters/` 保存章节讨论稿及 `report-outline.md` 保存已确认大纲；每章未经用户确认不标为定稿，不自动撰写后续章节。暂拟标题不等同最终课题名称。
- 第一章追加修订：用户已自行修改细节，要求正文只保留 1.1–1.3，删除反复强调边界的防御性说明。以当前用户版本为基线，保留用户新增观点；移存 1.4/1.5 和编辑附记，留档修改前全文。后续正文直接表达观点，证据条件写在相关分析/附注中，不堆免责声明。本轮只整理第一章，不展开第二章。
- 第一章讨论确认：用户接受 Agent 复用示例/模板或自主建立初始模型，研究重点保留在后续自主优化决策；已局部补入 1.2。后续继续讨论三类动作和可靠推进的含义，第一章整体仍待确认。
- 用户确认“改变策略”同时包括搜索方式调整与器件设计思路切换，已补入 1.3；接下来讨论可靠推进的含义，未展开第二章。
- 用户现已确认可靠推进的核心表述，已补入第一章 1.3；第一章三个核心定义完成对齐。按照逐章讨论授权进入第二章路径比较讨论，尚不生成第二章正文；不将局部定义确认等同整份报告验收。
- 第二章当前用户取向：Agent 的自主性主要体现于决策，工具受控执行，暂不追求自由编码；固定工作流能够满足自主优化。讨论记录见 `chapters/02-discussion-notes.md`，尚未选定最终架构；继续讨论设置可调范围与专家介入。
- 用户认可预先允许范围内自主调整参数/设置、关键建模变化请专家介入，并授权交付初版。本轮新增第二章正文初版 `chapters/02-existing-agent-paths-and-coverage.md`，复用既有图示和证据，保持第一章及旧交付不变，不自动写第三章。
- 用户认为第二章正文大致可用并修改了少量细节；本轮只按当前版本修改图 2-1 及必要图注。新增主干流程+项目纯色覆盖条 SVG/PNG，删除图内标题/说明/E 编号和重复状态文字，原覆盖判定不变；保留旧图源及正文用户修改。
- 2026-10-15 用户采用工具扩展安排：现有工具支持范围内自主探索，新建模/计算能力由人参与补充检查，再提供给 Agent。正文 2.5 局部增补，其他用户修改不变；继续讨论受控动作分支与比较优先级，不开始工程实现。
- 用户采用固定主流程＋受控动作分支，正文 2.5 已局部增补；剩余讨论为路径比较优先级，未确定框架或开发系统。
- 用户现已采用比较顺序：自主优化能力、推进的可靠性、实现代价。正文 2.5 已补入，保留其他用户修改；第二章三项讨论已对齐，进入第三章反馈证据与动作选择讨论，未生成第三章正文、未将章节整体标为定稿。
- 第三章用户选择基本检查每轮保留、深入检查按需触发，理由为节约 Token 和时间成本；已记入 `chapters/03-discussion-notes.md`。节约效果仍为未验证推断，继续讨论触发依据与候选/确认分工，不设计实验或生成第三章正文。
- 用户采用优良候选先保留待确认、异常改善或设置变化时优先检查、最佳方案确认前集中核查；已补入第三章讨论记录。下一步讨论多种原因并存时的诊断动作选择，未确定数值判据或执行实验。
- 用户确认诊断检查排序取向为原因可能性 > 误判风险 > 检查成本，已保存第三章讨论记录；可能性证据口径仍待明确，未定义概率或排序算法。后续讨论继续调参与策略切换的依据。
- 用户采用停滞后的检查顺序：先检查参数范围和搜索方式，再考虑设计家族切换；已保存讨论记录。助手提出第三章四节写作提纲供整体确认，未生成正文、未设平台期阈值。
- 用户现已采用第三章四节提纲并授权撰写初版；新增 `chapters/03-simulation-feedback-and-decisions.md`，以既有原文及固定源码证据组织反馈、诊断、搜索调整和候选确认。保留第一、二章及旧用户文件，正文待审，不自动写第四章。
- 用户要求第三章增加流程图；新增 `assets/feedback-guided-design-flow.svg/.png` 并作为图 3-1 嵌入章首。以用户当前已改正文为基线，只增加图片、图注和源图链接，不改其他文字；不新增实现或研究结论。
- 用户要求修正图 3-1 连线排版：新增 v2 SVG/PNG，分离继续探索与核查未通过两条回路线及接入点，标签避开连线；第三章仅更新图片与 SVG 两处路径。原图保留，流程内容不变。
- 用户采用第三章三项细节建议：必需条件先过再权衡指标；允许依据候选解释开展受控可回退尝试；关键建模假设变更、持续证据冲突或能力不足时专家介入。已局部补入第三章并增加电路流程说明例子，无新增实验或论文效果主张，图和其他用户文字保留。
- 用户要求进入第四章，新增 `chapters/04-discussion-notes.md`，整理 H1–H3 初步证据判断与待讨论项；先讨论 H1 的已有能力与可靠决策问题，不直接生成第四章正文，不改前三章或把第三章整体自动验收。
- 用户认可 H1 的研究优先级：现有诊断证据支持合理行动，通过后续反馈修正判断，不以准确识别所有根本原因为首要目标。已保存第四章讨论记录，接续 H2 的物理知识作用与独立增益讨论；未生成第四章正文。
- 用户讨论 H2/H3 后认可整理第四章初版；新增 `chapters/04-gaps-and-hypothesis-judgments.md`，四节综合已有诊断能力、物理知识作用、相对规则/优化器增量与具体缺口。正文待审，H2/H3 效果不标为已证；前三章及旧用户文件保持，不展开第五章或生成 DOCX。
- 用户要求“开始第五章”，沿用已确认的单方案深入/其他简表结构，新增 `chapters/05-candidate-entry-and-preliminary-scheme.md` 供讨论初版及讨论记录。具体化反馈条件、行动依据与后续观察，保留前四章实时用户编辑；初步方法待审，不写第六章、不实施或选定最终路线。
- 用户要求将 5.3 流程制图：新增概念流程 SVG/PNG，并插入第五章图 5-1 及图注。仅展示当前流程、反馈回路与职责，不改变用户已编辑正文或增加研究结论；渲染和连线排版检查后交付。
- 用户要求简短撰写第六章：新增 `chapters/06-conclusions-and-discussion.md`，三段总结已有结论、反馈驱动的初步倾向及待讨论问题。六章讨论稿已齐但未整体验收，前五章保持，不自动汇编、生成 DOCX、实施或发布。
- 用户最新明确要求六章原封不动拼接为完整版：新增 `references/task-021/chapters/完整调研报告.md`。与原章节同目录以保持所有链接、图文和原措辞不变，按第一至第六章顺序拼接，仅增加章间空行；原分章文件保留，不作润色、删减、去重、DOCX 转换或远程同步。
- 用户追加要求将参考文献整理到文末：以当前已有人类修改的完整版为基线，先留档，移除章内参考列表、合并重复来源并统一正文引用编号。24 条分章记录整理为 8 条来源，27 处引文完成映射；仅调整参考记录和编号，其他正文与分章文件不动，不重新检索或补造书目信息。
- 用户选择先补 3.3 配图：仅在当前完整版插入图 3-2 与图注，使用官方 arXiv v1 Fig.2 完整 PNG，展示迭代轨迹、最终波导光谱及场分布；保留坐标、图例和数据，不编绘中间结构或因果对应。原分章、其他正文与文末八条参考不改，不添加另外两处建议图。
- 用户要求将优化过程简要补入正文：在完整版图 3-2 后增补一段，概述欧拉过渡、宽度渐变、偏移方向尝试及联合搜索，引用既有 [1,7]；其余正文、图片和参考列表保持，不扩大调研或实施范围。
- 2026-10-15 用户要求先转成 PDF：仅从当前完整版导出本地 PDF，允许新增 `references/task-021/export_report_pdf.py`、`output/pdf/` 交付及 `tmp/pdfs/` 版面核查产物；不应用全文审查建议、不修改 Markdown 正文或旧 Office/PDF，不远程发布。验证源文件哈希、文字/图表完整性及实际分页渲染。
- PDF 导出完成：19 页、11 表、4 图，当前完整版源文件哈希不变；362 个文字单元全部可定位，Poppler 全页渲染及联系图目视检查通过。导出与限制记录见 `references/task-021/pdf-export-qa.md`；未提交/推送，内容审查建议尚未执行，任务保持 ACTIVE。
- 用户追加 PDF 排版要求已应用：正文段间额外空白取消，首行缩进两个汉字；四幅图适当等比缩小并浮动至页面下部，取消文末强制分页。新版 15 页，11 表/4 图保留，362 个文字单元核对无缺失，源 Markdown 哈希不变；实际全页渲染检查通过，仅排版更新。
- 2026-10-16 用户要求 Word 版且内容不变：授权新增当前完整版的 DOCX 导出脚本、本地 `output/task-021/` Word 交付及 `tmp/pdfs/task-021-docx/` 渲染检查；正文、引用及旧交付不改，不应用此前内容审查意见，不远程同步。采用可编辑段落与表格、原始图片，并核对文字完整性与实际分页。
- 2026-10-16 用户要求将最近成果提交到仓库；本轮允许范围增加为将当前工作树中的已完成文档、交付物和事实源更新形成 Git 本地提交。保留所有文件内容；`tmp/` 下分页渲染与 QA 临时产物继续留在本机、不纳入提交。现行禁止远程发布仍有效，因此本轮不推送 GitHub。
- 后续范围变更（2026-10-16）：用户要求“合并提交”；结合本地 `main` 超前公开远端 `main` 的上下文，授权将现有本地提交快进推送至 `origin/main`，供组员在公开仓库查看。该授权仅覆盖当前本地提交，不创建 PR，不涉及其他外部发布；覆盖上方原“禁止远程发布”边界。推送前已 fetch，确认远端 `main` 是本地 `HEAD` 的祖先。
- Word 版已生成：15 页、11 张原生表格、4 图、8 条参考来源，362 个文字单元无缺失，原 Markdown 与 PDF 哈希不变。标准渲染器缺少 LibreOffice 后采用 Word COM 只读导出与 Poppler 实际逐页检查，详见 `references/task-021/docx-export-qa.md`；未提交/推送，任务仍 ACTIVE。

---

## TASK-020：课题组介绍 Harness 两页节选

- 状态：`REVIEW_READY`（2026-10-10）。用户指定桌面Harness可编辑PPT，要求节选一页原理和一个例子，使用刚保存的工程光学模板；已交付可插入的两页模块。
- 起点：`816552ef8a92fbb941131c13a9f0da47e1e36058`；已有用户DOCX修改及三个未跟踪PDF保留。
- 范围：新增 `presentations/task-020-group-topic-excerpt/` 两页模块与源、预览、QA；只读桌面源PPT及个人模板引用。选源P1原理与P7 Kharel波导弯曲仿真案例，保留原图/条件/来源。导入模板正文母版与布局，框图/说明/导航为原生对象，图为独立图片。
- 不新增论文、研究方向、实验或实现；不修改原文件、现有Harness/用户DOCX，不推送。未提供课题组完整PPT，因此交付可插入的两页模块，不宣称已经合并。
- 验证：来源与数据保持，模板主题/母版/画布与字体匹配，原图SHA与桌面源一致，文字可编辑、两页实际渲染/视觉检查、git diff --check。
- 完成记录：从模板正文页4/6导入，形成两页PPTX/PDF，32个原生文字对象、独立原图/校徽与原生箭头；模板母版/主题XML一致，画布13.3333×7.5英寸。PowerPoint实际修改并保存重开验证、两页导出及独立视觉审查完成。0溢出/重叠；通用几何token与原模板满宽导航冲突的13项保留并记录，见新工作区qa-summary.md。原始输入不变，未实际并入完整课题组PPT。

---

## TASK-019：保存工程光学 PPT 默认格式模板

- 状态：`REVIEW_READY`（2026-10-10）。用户指定微信临时目录中的工程光学课程汇报PPT作为以后制作PPT的格式模板，个人模板已创建并核验。
- 起点：`aa1609cca5fd29cfcafa6650354fbf39badfe7c3`，`main`。已有两个用户DOCX修改和三个未跟踪PDF，保留且不纳入提交。
- 范围：只读参考PPT，检查封面/正文/结尾、主题、字体与母版；使用template-creator官方脚本在个人skills目录创建参考模板；新增格式使用记录与项目默认入口，保存用户明确要求的长期偏好。不修改原参考文件或现有Harness交付。
- 模板只沿用格式，姓名、学号、内容与文献替换为当次资料；保留原生可编辑对象，不把新页面截图作为交付。用户后续明确指定的格式优先。
- 验证：原PPT与保留副本SHA一致；实际渲染及预览视觉检查；模板SKILL/manifest/agent/preview/reference文件齐全；格式记录可定位；git diff --check。不开展科研、实验或远程发布。
- 完成记录：官方create-template-skill.mjs生成`artifact-template-engineering-optics`，kind为presentation。完整参考14页、2母版、16:9、微软雅黑、白底深青色；PowerPoint渲染14页并检查。保留参考SHA为`6cdcf2d54733b902d606a0c9719a3ac212237cf00fb29859a54541328c9a4332`，与原文件一致；五类必需模板文件齐全。默认入口见docs/PPT_TEMPLATE.md，并保存用户明确要求的长期偏好记录。现有Harness文件和用户DOCX/PDF不修改、不纳入提交；完成SHA由答复记录。

---

## TASK-018：课堂课题方向汇报 Harness 初版

- 状态：`REVIEW_READY`（2026-10-09，可编辑版）。当前八页保持两页课题、五页现成项目、最后一页总结，计划7分40秒。已按用户要求将整页合成图拆为可编辑对象。
- 起点：`7aee380b729505d6dbac471e954093bdea6ac0cc`，分支 `main`。用户已有 DOCX 修改与三个未跟踪 PDF 保留，不纳入提交。
- 范围：`presentations/task-018-class-harness/` 独立工作区、PPTX/PDF、图示、逐页讲稿与来源索引、QA 记录；更新任务和当前状态。原七页初版保留，当前八页项目重点版。
- 内容：只讲 Harness，承接同学 DAS 模块；计划 7–8 分钟。沿用既有三项目证据和物理诊断/决策候选主线，不新增调研，不实施 Agent、仿真或实验。Jev 继续 DEFERRED，本轮只转换现有内容为课堂汇报。
- 修订范围：P1–P2 讲课题与研究切入点；P3–P7 讲 PhIDO 架构/基准、PICopilot、Kharel 闭环/案例。可只读已有 Zotero 附件，复用现有原图并补充对应 Figure 裁图；裁剪保留图例、坐标和数据，注明来源。仅本地课堂文件，未授权远程发布；再分发许可未核实项继续记录。
- 验证：结构、来源与假设标注、七页备注与时间分配、构建 QA、PowerPoint 逐页渲染视觉检查、文件路径及 `git diff --check`。讲述时间为规划，未经实际试讲。
- 完成记录：交付独立七页 PPTX/PDF、六幅解释性 SVG、原生论文比较表及七页备注；计划 450 秒。构建为 0 溢出/重叠/占位/设计错误，P3 有一条空白比例几何提示，视觉检查后保留。PowerPoint 导出七页并逐页与独立视觉审查；修正 P3 单字换行、行分隔和 P5 输入框间距。详见新工作区 `qa-summary.md`，完成 commit SHA 由答复给出。
- 修订交付：当前八页项目重点版，P1–P2课题、P3–P7项目原图、P8总结；时间110/310/40秒，共460秒。Zotero启动后API/connector均HTTP200，三个附件URL及PDF哈希与TASK-016核读版本一致。引用PhIDO Fig.1/5、PICopilot Fig.2、Kharel Fig.1(b)/2(a)，原图说明与数据边界见索引和备注。构建QA零溢出/重叠/几何/视觉/设计错误，PowerPoint导出八页并完成主审与独立视觉检查。仅本地交付，未实际试讲或远程发布。
- Word 追加授权：用户于 2026-10-09 要求将本对话完整口头文本稿交付为 Word。允许新增讲稿源 Markdown、DOCX 与最小构建脚本；仅排版，不改变研究事实。起点 `40591a6f095388539f1756b1bf2f704b1d4fe75f`，渲染并检查后交付。
- Word 交付：`Harness_课堂汇报_完整讲稿.docx`，四页、八段对应PPT内容、逐页建议用时，总规划460秒。61个正文段落与源Markdown逐段一致；Word导出四页，Poppler渲染并逐页检查。内置render_docx因本机缺soffice失败，采用Word COM替代；未实际试讲。源为`spoken-script.md`，构建脚本为`build_spoken_docx.py`。
- 可编辑性修订起点：`efcf49756928d8cfd9da37c5ee67680fe258ad4f`。将框图/箭头/中文说明/总结转换为原生对象，论文原图保持独立图片。允许增加当前工作区的最小原生渲染扩展并修改源/重建脚本；不改文献内容与讲稿。开始时用户另有完整讲稿DOCX修改，保留且不提交。验证原生对象数量、原图独立性、选中文本临时编辑读回、构建QA与八页渲染。
- 可编辑版交付：93个原生文本对象；P1/P2/P8无图片，图形与箭头为原生形状；P3–P7共6个独立原图对象（P4子图与图例分开），媒体SHA与源图片逐一一致。PowerPoint临时副本修改中文说明并移动原图，保存重开读回通过，交付文件哈希不变。构建0溢出/重叠/设计/视觉错误，P2/P8两条密度提示经八页主审与独立视觉检查保留。当前源outline.json的native_elements由build_source_editable.py生成，通过工作区build_native.cjs扩展标准技能渲染；未改技能安装文件。

---

## TASK-017：候选物理驱动自主 PIC 方向三端同步

- 状态：`REVIEW_READY`（2026-09-30）；用户授权同步附件候选主线，明确保留现有 DOCX 用户修改。
- 起始提交：`de0121904a3922836692d8448c22932a95dc085a`，`main`。已有 DOCX 修改和两个未跟踪用户 PDF；不覆盖 PDF。
- 范围：正式报告候选路线章节、现有用户 DOCX 局部增补、门户候选方向入口与图示、当前 20 页 PPT P18–P19 及 P20 必要一致性修正；相关来源、编辑脚本、核查及治理记录。
- 边界：物理驱动的自主光子芯片设计（Physics-guided Autonomous PIC Design）仅为 `USER RESEARCH PREFERENCE / INFERENCE`；H1–H3 未验证。保留三方向、既有研究证据和历史任务。TASK-016 仍待审查，不自行验收。
- 禁止：新调研、实现、仿真、benchmark、实验方案细化、最终定题、上传飞书及远程发布。Jev 继续 `DEFERRED`（用户本轮明确确认）。
- 验证：原 DOCX 正文/表格/图像保留，三端术语一致，论文定位与推断边界检查，DOCX/PPT 渲染审阅，门户严格构建及桌面检查，`git diff --check`，提交后等待审查。
- 完成记录：保留 282 个原始正文 XML 块、13 张表和 10 个媒体，当前 DOCX 渲染 33 页；20 页 PPT 局部更新及复查、门户 3 图/18 链接检查通过。QA 与未执行事项见 `references/task-017-candidate-direction/qa-and-handoff.md`；完成 SHA 由交接答复记录，不自行验收。

---

## TASK-016：调研报告证据可视化增强

- 状态：`REVIEW_READY`（2026-09-29，DOCX 与网页端增补已完成，待 GPT 只读审查）；首轮交付 commit `e3a3f8316c0b18d7b2f890ba6f921fdb41a0f9ef` 已完成，用户随后要求将同样的证据增强应用于现有飞书上传版 DOCX 和 Research Portal 网页端。不自行宣布验收。
- 授权来源：用户在本对话给出的“调研报告证据可视化增强”任务。
- 起始提交：`c02f121629f7eceb5d03e49d968894e48352cde9`，分支 `main`。开始时已有用户工作树改动：`output/task-007/面向光子芯片智能设计的三方向技术调研_飞书上传版.docx` 修改及同名 PDF 未跟踪；前者经用户追加授权后以当前版本为基础增补并纳入本轮提交，后者不纳入。
- 目标：在不扩大论文池、不改三方向和核心判断框架的前提下，为 PhIDO、PICopilot、Kharel 2026、Jin 2024、Cheng 2023、Sandmann 2023、Ahmed 2025 增补论文原图、原始结果口径、来源定位和证据边界，并形成 Agentic PIC 三项目比较。
- 允许修改：现有调研 Markdown、最新组会 PPT 的源工作区和再生交付、独立证据日志与图表来源索引，以及本任务和当前状态记录。Zotero 与 PDF 只读；可在仓库交付中使用许可明确的原图，许可不明时保留定位或改绘。
- 禁止范围：不新增方向或大量论文；不实施 Agent、simulator、benchmark、仿真、流片或实验；不修改 `D:\AI_PIC_Demo`；不把作者结果当成本项目复现；不覆盖用户未跟踪 PDF。
- 验证：逐项回到论文 PDF 核对图号、页码、数值、单位、条件和限制；图像裁剪保留含义；报告/PPT 结构与视觉检查、引用/路径检查及 `git diff --check`；列出 UNKNOWN。最终提交 completion commit 后等待 GPT 只读审查。

### 完成记录

- 首轮起始 commit 为 `c02f121629f7eceb5d03e49d968894e48352cde9`，首轮完成 commit 为 `e3a3f8316c0b18d7b2f890ba6f921fdb41a0f9ef`；DOCX/网页增补完成 commit 的准确 SHA 在交接答复中给出。保留了用户 DOCX 原有修改，未改动用户 PDF。
- `references/task-016-evidence/` 为本轮证据包：七篇本地 Zotero PDF 的 item key、SHA-256 与页数，逐项数据/条件/证据等级表，Figure 来源与许可、Agentic PIC 三项目八列比较，以及 unresolved/UNKNOWN。
- `references/task-007/formal-research-report.md` 增加 PhIDO/Cheng 已许可原图、关键证据定位及系统与验证边界；`presentations/task-010-group-meeting-rebuild/` 的 20 页无附录 PPTX/PDF 同步更新。未改已确认的三方向结构和核心判断框架。
- 核验：七篇 Zotero 本地原文只读访问、原图裁剪审阅；PPT 构建 QA 为 0 溢出/重叠/占位/视觉警告和 0 设计错误/警告；PowerPoint 导出 20/20 页 PNG 和 PDF，20 页联系图与关键页全尺寸检查；路径、CSV 和引用检查及 `git diff --check` 通过。14 条面积密度提示为技术图示占页的几何提示，见 PPT `qa-summary.md`。
- 未执行：论文实验复现、仿真、独立原始数据重算、全系统能效复核、版权未明原图再分发、投影设备试讲。详见证据包 UNKNOWN 列表。等待 GPT 最终只读审查。

### DOCX 增补边界（用户 2026-09-29 追加授权）

- 起点：`e3a3f8316c0b18d7b2f890ba6f921fdb41a0f9ef`。允许在用户当前已修改的 `output/task-007/面向光子芯片智能设计的三方向技术调研_飞书上传版.docx` 上局部加入 TASK-016 已核验的原图、数据、三项目比较与 UNKNOWN，不从 Markdown 整体重建；保留用户日期及原有内容，并在写入前备份。允许增加可复现的最小编辑脚本及任务/状态记录。
- 同名 `output/task-007/面向光子芯片智能设计的三方向技术调研.pdf` 是用户已有未跟踪文件，本轮不覆盖；不增加论文池、研究判断或实验。DOCX 图像仅使用许可明确的 PhIDO/Cheng 原图，版权未明论文保留 Figure/Table 定位或改绘。
- 验证：前后文本及图表保留比对、DOCX 结构与来源/条件检查、逐页渲染视觉审阅、`git diff --check`；提交增补 commit 后等待 GPT 最终只读审查。
- 网页端追加范围：`portal/docs/task-007-report.md` 已在构建时嵌入更新后的 Markdown 事实源；本轮允许修正证据图示的站内资源路径、增加证据包阅读入口、更新过时首页状态，并运行 `mkdocs build --strict` 和浏览器/生成 HTML 检查。门户继续只做展示层，不复制版权未明原图、不产生新的研究结论。
- 增补交付：以用户已修改 DOCX 为基线局部增补七篇代表工作证据卡、四张许可明确的论文 Figure、三项目八列比较和 UNKNOWN；Research Portal 同步正式报告和证据包阅读页，导航、图示和数据表可用。具体保留检查、渲染、站内链接、许可边界和未执行事项见 `references/task-016-evidence/docx-portal-qa.md`。本地门户未远程发布，DOCX 未上传飞书。

---

## TASK-015：TASK-007 正式调研报告本地 DOCX 整理

- 状态：`REVIEW_READY`（2026-09-29，待用户检查文件）。
- 授权来源：用户明确选择“完整报告的可上传 DOCX；只交付本地文件”。
- 起始提交：`3c5c5eff4a5fe37af86e89e39a67b9f8f5dcb843`；开始时 `main` 工作树干净。
- 范围：只读使用已验收的 `references/task-007/formal-research-report.md` 与 `references/task-006/paper-and-repository-index.md`，生成本地完整 DOCX；原 Markdown、证据和研究结论不修改。不上传飞书、不开展新调研或实验。
- 交付：`output/task-007/面向光子芯片智能设计的三方向技术调研_飞书上传版.docx`；可复现构建脚本 `scripts/build_task007_feishu_docx.py`。正文保留六章、参考文献入口和附录 A/B；附录 C 依据既有出处索引列出 32 篇论文与 11 个工具/项目入口。
- 验证：DOCX ZIP 结构完整；含 62 个标题段落、6 张表、2 张架构图、70 个外部超链接，无 MkDocs 本地相对链接；Word 导出 20 页 PDF 并逐页检查页面 PNG，未见表格单行拆断、裁切或乱码。内置 `render_docx.py` 因本机缺少 `soffice.exe` 失败，改用本机 Word COM 导出和 bundled Poppler 预览。未实际上传飞书，导入后样式仍需用户在飞书核对。
- 后续：等待用户检查；不自动开始新的研究、实验或工程任务。

---

## TASK-014：现有论文卡批量迁移至 V2 模板

- 状态：`COMPLETE`（2026-09-27）。
- 起始提交：`b0b894c65fefc22cbe02f6a363650ca2679473fc`；开始时 `main` 工作树干净。
- 授权来源：用户要求“全部用新模版写”。
- 范围：仅对独立 Vault `论文知识库/01_Papers` 中的 36 张既有论文卡做结构迁移，统一为 V2 七区块与 L1/L2 元数据；索引、清单、模板、其他笔记不改。
- 允许修改：36 张论文卡；本地备份、迁移脚本与核验记录；本仓库任务与状态文档。
- 禁止范围：不改 Zotero、PDF、论文书目事实、分类/标签或 `D:\AI_PIC_Demo`；不凭篇幅自动标 L2，不把 AI 文本冒充本人理解；不上传个人笔记到 GitHub。
- 验收：先只读清点和 dry-run；写入前备份全部 36 张卡；迁移后每张卡有七个 V2 区块且全部原正文保留、原 YAML 字段值不丢；36 个 Zotero key/DOI/标题不变；索引链接继续可用；记录无法自动判定的待核项和 `git diff --check`。
- 完成记录：36 张论文卡全部按 V2 七区块重排，其中 31 张原四段式首轮卡、5 张旧版详细卡；所有卡 `note_level: L1`，原始段落保留在对应区块下。旧卡中名为“我的理解”的原内容迁至“AI 解读（待人工确认）”，新的“我的理解（仅本人填写）”保持空白；没有自行填补全文证据或复现状态。
- 本地备份与核验：逐卡原件和 SHA-256 manifest 位于独立 Vault 的 `.local_migrations/TASK-014_2026-09-27_originals/`；迁移脚本为 `.local_migrations/task014_migrate_cards_v2.py`。正式写入前 dry-run 预估 36 项，写入后重新 dry-run 为 `to_change=0`；备份对比验证 36 卡的原 YAML 值、正文各段、H1 和 32 个项目索引链接保留。未实际在 Obsidian UI 逐张检查排版，未重新阅读全文核对科研判断。

---

## TASK-013：本地 Obsidian 论文卡模板 V2

- 状态：`COMPLETE`（2026-09-27）。
- 起始提交：`dac0e57b4a0fa0d5ca464be5211e007c047a9096`；开始时 `main` 工作树干净。
- 授权来源：用户在核对 GPT 的 L1/L2 模板建议后要求“那开始”。
- 目标：为固定对接的独立 Obsidian Vault 重设计论文卡模板，让同一张卡从首轮速览 L1 升级到核读证据 L2，保留作者报告、原文事实、项目复核和 AI 推断的边界。
- 允许修改：独立 Vault 的论文卡模板及必要使用说明；本仓库的任务和当前状态记录。
- 禁止范围：不批量改写现有 36 张论文卡；不修改 Zotero、PDF、Collection、标签或 `D:\AI_PIC_Demo`；不上传个人笔记到 GitHub；不把 L2 视作已复现。
- 验收：旧模板可恢复；V2 Markdown/YAML 可读；字段和现有卡片可以逐步兼容；明确 L1/L2 升级条件、来源定位、AI 解读与本人理解分离；校验路径、文件内容和 `git diff --check`。
- 完成记录：在独立 Vault 将原 `99_Templates/03_Obsidian论文卡模板.md` 保留为 `03_Obsidian论文卡模板_V1备份.md`，原位改写 V2；新增 `00_System/08_论文卡V2使用说明.md`。V2 用一张卡的 `note_level: L1/L2` 表达证据深度，正文缩为 7 区块；作者报告的数字不因有来源定位而被视为独立验证，AI 解读与本人理解分离。
- 验证与边界：V2 Frontmatter 可由 PyYAML 解析，恰有 7 个二级区块；模板与说明在预期 Vault 路径可读。已有 36 张论文卡未批量改写，Zotero 与 `D:\AI_PIC_Demo` 未修改；未进行实际 Obsidian UI 渲染或新论文填卡测试。

---

## TASK-012：项目论文笔记接入独立 Obsidian 知识库

- 状态：`COMPLETE`（2026-09-27）。
- 起始提交：`71e09968995baacdde0965e3e3ce2b1c538c3102`；开始时 `main` 工作树干净。
- 授权来源：用户要求“对当前项目所有论文依次做笔记放到 Obsidian；现在该项目论文固定与该笔记仓库对接”。
- 范围：以 `references/task-006/paper-and-repository-index.md` 的 32 篇项目论文为当前批次，核对 Zotero item key、原文和既有研究证据；在独立本地知识库 `GPT_Zotero_Paper_Knowledge_V1` 建立或复用论文卡、项目索引与对接说明。早期另外四张逆向设计论文卡保留为已有知识，不重复创建。
- 允许修改：本仓库的任务、状态、长期决策与对接说明及本地忽略配置；独立 Obsidian 知识库中的相关论文卡、索引和主页入口。
- 禁止范围：不修改 Zotero 条目、附件或标签；不复制 PDF 到公开仓库；不修改 `D:\AI_PIC_Demo`；不把作者报告当作本项目实验结论；不发布内部笔记到 GitHub。
- 验收：32 篇项目论文逐一对应 Zotero key 与唯一 Obsidian 论文卡；每卡列出原始出处、研究问题、方法、证据边界与项目关联；现有五卡不覆盖正文；项目索引和主页链接可解析；本地 Vault 路径写入被 Git 忽略的配置；执行 YAML、链接、文件覆盖和 `git diff --check` 核验。
- 完成记录：独立 Vault 新增 31 张项目论文首轮笔记并复用 PhIDO 详细卡，形成 32 篇项目索引；早期其他四卡保留。新卡保留原文题名/DOI、Zotero 父级 key、来源层级、研究问题、方法、证据边界、项目关系和待复核项；未安装 Better BibTeX 或生成虚构 CiteKey。32 个 key 可从 Obsidian 索引定位 Zotero Desktop。
- 证据与限制：Zotero Local API 只读核验当前 36 篇父级论文；项目新导入论文中 29 篇本地 PDF 可访问，Taichi 2024 与 Lin 2022 两篇无本地 PDF，明确标记待核读原文。当前 31 张新卡为首轮笔记，并未逐页精读所有全文、复算作者实验或进行物理验证。
- 验证：36 张卡 YAML 可解析、父级 key 唯一、题名与 DOI 和 Zotero 记录一致；项目索引 32 条 Zotero URI 与 32 张对应论文卡可解析；本机 Vault 配置被 Git 忽略；仓库文档执行 `git diff --check` 与状态检查。

---

## TASK-011：创建并发布同名 GitHub 仓库

- 状态：`COMPLETE`（2026-09-24）
- 起始提交：`c4ff280a72398bf7c41e20680648c59fd12b6d5f`
- 授权来源：用户要求将目前项目文件放到 GitHub 并使组员可见，随后明确确认仓库公开。
- 目标：在当前 GitHub 个人账号下创建公开的 `PIC_Harness_Research` 仓库，将本地项目提交和 `main` 分支推送为 `origin`。
- 允许范围：新增 GitHub 远程仓库、配置 `origin`、推送项目提交；更新任务/状态文档以记录边界与实际结果；提交当前工作树中的项目文档改动；忽略 Office 临时锁文件。
- 禁止范围：不邀请或向任何人发送消息；不改写研究内容；不删除用户文件；不推送 PowerPoint 临时锁文件。
- 验收：远程仓库 URL、可见性、默认分支及远程 HEAD 与本地 `main` 一致；`git status` 干净；`git diff --check` 通过。
- 完成记录：已创建并配置 `origin`：`https://github.com/LlewynDavis/PIC_Harness_Research`。`gh repo view` 核验仓库为 `PUBLIC`、默认分支为 `main`；`git ls-remote --heads origin` 返回的远程 `main` 为 `2a8a725d98c0b607668f8bc8bef52501d5564665`，与本地 HEAD 一致。`git diff --check` 通过；推送后工作树干净。Office 临时锁文件未纳入版本控制。

## TASK-010：基于最新大纲重做首次正式组会 PPT

- 状态：`REVIEW_READY`（2026-09-23，待用户审阅）
- 起始提交：`7abc0f1a2f68d3867fa26dbfe0ff558ac9c49b87`
- 授权来源：用户提供完整 P1–P20 新大纲，要求直接从新工作区重做学术 PPT，保留已核验研究内容与论文证据，不沿用旧版页面结构和视觉布局。
- 目标：交付约 20 页、15–20 分钟的可编辑 PPTX、PDF 预览、逐页简短讲解备注及图示/引文证据索引；三方向均覆盖，P10–P16 深入 Agentic PIC，P17–P19 递进形成比较、待研究问题及个人倾向。
- 允许范围：只读复核已验收 TASK-005/006/007 调研成果和 Zotero PDF；在 `presentations/task-010-group-meeting-rebuild/` 新建独立 workspace、绘制准确技术图示、裁剪并标注许可允许的论文 Figure；更新本任务及 `docs/CURRENT_STATE.md`；执行完整内容、渲染和几何 QA。
- 禁止范围：不改写已验收研究结论，不运行实验、仿真、Benchmark 或 Agent/Harness 开发，不将候选路线和个人倾向写成已定课题，不修改 Zotero 库或 `D:\AI_PIC_Demo`。工作树已有 `AGENTS.md` 未提交改动不属于本任务。
- 验收：核对原图与技术主张、证据边界和 P18–P19 措辞；渲染逐页检查可读性、讲解备注、来源和引用；运行 workspace QA、PPTX/PDF 读回及 `git diff --check`。附录是否保留按用户对最新大纲与此前“不保留附录”的澄清处理。

### 完成记录

- 全新独立 workspace：`presentations/task-010-group-meeting-rebuild/`；20 页主讲，无附录，保留此前用户明确提出的“不保留附录”。TASK-007/008 原始交付未修改。
- 正式 PPTX/PDF 为该目录下 `PIC_Harness_Research_首次组会调研_20页.*`；每页均有讲解备注。14 张自绘 SVG 图与 4 张论文 Figure 分别承担原理/综合分析和真实成果展示；页码、来源、局部裁剪、许可和边界详见 `figure-and-evidence-index.md`。
- P17–P19 按新大纲组织为跨方向比较、四层问题推导、个人研究倾向；未把 A/B/C 或需求解析写成最终课题/创新点。
- 验证：presentation-skill 严格 QA 退出 0，溢出/重叠/占位符/视觉警告均 0；14 条图示面积密度提示经人工视觉检查为非阻断；PowerPoint 成功导出 20/20 页 PNG 和 PDF，PPTX 20 页与 20 页备注、PDF 20 页读回通过。图示逐页审查与时长安排见 `qa-summary.md`。本项目未复算论文实验或完成汇报人的实讲计时。
- Zotero API 在本次制作时超时；已有 PhIDO、PICopilot、AutoPhotonicDesign PDF 本地附件可只读访问。Jin 2026 原图附件未找到，用已核验材料改绘；ACCEL 使用官方开放获取 Fig. 1(b)。未修改 Zotero 库。
- 工作树原有 `AGENTS.md` 未提交改动不属于本任务，不纳入交付提交。

---

## TASK-009：PIC × AI Agent 科研英语词库 V1

- 状态：`DELIVERED`（2026-09-23，待用户在 Knowt 实际导入）
- 授权来源：用户明确要求直接制作约 200 张专业科研英语单词卡，交付 Excel 与 UTF-8 TSV。
- 允许范围：复用本仓库已核验调研及术语表，并核对 Knowt 官方手动导入说明；仅新增 `learning/vocabulary/` 成品及本任务记录。
- 禁止范围：不修改原研究结论、技术路线、代码，不运行科研实验，不访问 `D:\AI_PIC_Demo`，不宣称已在用户账户中导入成功。
- 交付：`learning/vocabulary/PIC_AI_Research_Vocabulary_V1.xlsx` 和 `learning/vocabulary/Knowt_Import_V1.tsv`，共 200 条；A/B/C/D/E 分别 40/45/35/45/35。
- 验证：独立用只读 `openpyxl` 打开 XLSX，核对两张工作表、列名、数量、分类、术语去重、非空字段及 200 行导入页与 TSV 逐行一致；两张工作表首段已渲染目视检查。Knowt 网页端粘贴导入尚未在用户账户实测。
- iPhone 直传补充：用户提供 Knowt App“从设备上传文件”截图后，按 Knowt 官方支持的 PDF 文件入口，新增 `learning/vocabulary/Knowt_iPhone_Upload_V1.pdf`。PDF 为 16 页，每条以 `Term` 和 `Definition` 连续排版；文本读回检查 200 对，按忽略换行的原文核对均与 Excel 导入页一致，并目视检查首、中、末页。文件已上传至用户 Google Drive 且核对为 PDF。Knowt 的 PDF 路径使用 AI 生成卡片，是否逐字保留 200 张需用户上传后在 App 内检查。
- 墨墨记忆卡补充：用户改为要求可在 iPhone 导入的墨墨格式，并要求在对话中直接交付、不再上传云端。新增 `learning/vocabulary/PIC_AI_Markji_V1.apkg`（基础正反面 Anki 牌组）及 `learning/vocabulary/PIC_AI_Markji_Text_Import_V1.txt`（墨墨批量制卡文本备用）。两者各含 200 张卡，与原 XLSX 导入页逐条一致；已检查 APKG 的 ZIP/SQLite 结构、200 条唯一笔记及 200 张卡，检查 TXT 的 UTF-8 编码、分隔符和 200 组正反面。尚未在用户 iPhone 的墨墨 App 中实测导入。

---

## TASK-008：组会调研 PPT 优化

- 状态：`REVIEW_READY`（图示化补充修订已交付，待用户审阅）
- 启动日期：2026-09-23
- 起始提交：`18e19afb51fb77d9f540e6294822d7c11375647e`
- 授权来源：用户提供完整 PPT 优化规格，明确授权直接制作并交付。
- 前置任务：`TASK-007 = ACCEPTED / CLOSED`；其原始交付与验收记录保持不变。

### 目标与允许范围

以 TASK-007 正式报告、证据审计和可编辑 PPT workspace 为基线，形成供导师和课题组 15–20 分钟讨论使用的正式可编辑 PPTX：约 12–14 页主讲、来源标注及逐页讲解备注。用户已补充要求最终版不保留附录。允许在独立 PPT 优化 workspace 内重排和精简已验收内容、修正证据表述、生成预览并执行内容与视觉检查；更新本任务和当前状态记录。

### 禁止范围

不重启或改写 TASK-007 验收，不修改已验收的原始研究证据，不做完整新调研、实验设计、仿真、Benchmark、Agent/Harness 实现或最终路线选择；不访问或修改 `D:\AI_PIC_Demo`。不把作者指标或推断写成本项目验证结果。

### 验收与交接

交付可打开、可编辑的 PPTX，主讲备注、学术引用及 PDF 预览。核对三方向技术判断与正式报告一致；运行 workspace QA、逐页渲染检查、引用/路径检查和 `git diff --check`。提交时记录本任务文件、验证及限制，并排除工作树原有的 `AGENTS.md` 未提交改动。

### 完成记录

- 完成日期：2026-09-23；交付提交为本节所在提交。
- 独立 workspace：`presentations/task-008-group-meeting/`。正式可编辑 PPTX 与 PDF 预览均在该目录；TASK-007 原始 workspace、报告和验收结论未修改。
- 初次交付结构为 14 页主讲、11 页附录；下方补充修订按用户要求删除附录，现以 14 页无附录版本为准。
- 初次交付验证为 25 页渲染；下方补充修订对最终 14 页重新执行构建、渲染、PDF 与严格 QA，详情见该 workspace 的 `qa-summary.md`。
- 未执行：新一轮完整调研、实验、仿真、Benchmark、Agent/Harness 实现或最终选线。
- 既有工作树 `AGENTS.md` 未提交改动不属于本任务，未纳入交付提交。

### 图示化补充修订（2026-09-23）

- 授权来源：用户在当前任务中要求提高主讲 PPT 的技术图示解释质量。
- 允许范围：只修订 TASK-008 workspace 的主讲页图示、讲解备注、引用和 PDF/PPTX，保留已验收报告与 TASK-007 原始交付；以已核验材料为依据重绘可追溯技术示意、能力覆盖和路线推导。
- 验收重点：每张图说明一个技术问题；检查结构、箭头、参数和证据来源；主讲技术分析页优先使用解释性图示或可视化矩阵；逐页渲染复核并记录图示作用与限制。
- 禁止范围延续本任务原有边界：不新增无关文献调研、实验、仿真、Benchmark、Harness 实现或最终选线。
- 用户进一步要求删除附录，并优先检查 Zotero 代表论文 PDF 的原始 Figure；允许只读访问附件和在本任务 PPT 中引用、裁剪有来源标注的论文图，不修改 Zotero 库。
- 修订结果：最终仅 14 页主讲，14/14 页含备注；第 2–13 页均使用有解释作用的图示或矩阵。10 张矢量概念图与两张原论文 Figure 分别解释系统链路、集成边界、计算架构、设计循环、工作覆盖、研究缺口和路线推导。两张 Figure 来源于 PhIDO Fig. 1 与 AutoPhotonicDesign Fig. 1(b)，图号和裁剪范围记录在 `diagram-sources.md`。
- 最终验证：PowerPoint 导出 14/14 页 PNG 和 14 页 PDF；严格 QA 退出 0，溢出/重叠/占位符/视觉警告/设计错误均为 0。10 条图示覆盖面积较大的密度提示经人工逐页检查为非阻断；`python-pptx` 与 `pypdf` 均读回 14 页。Zotero 启动后本地 API 与 Connector 均恢复 200，核对了两张论文 Figure 的条目与附件；DAS/光子 AI 目标论文附件仍未找到，因此使用来源明确的概念重绘图。未在会议投影设备上预演；外部指标未复算。

---

## TASK-007：PIC_Harness_Research 正式调研报告与组会汇报

- 状态：`ACCEPTED / CLOSED`
- 启动日期：2026-09-21
- 起始提交：`bf28b08ab667a86df575cff7c70f81fab8f73ee5`
- 前置任务：`TASK-004 / TASK-005 / TASK-005A / TASK-006 = ACCEPTED / CLOSED`
- 授权来源：用户在当前对话中提供完整 TASK-007 规格并明确授权启动。
- 执行协调器：Codex；Qwen 项目主对话承担有收益的独立只读抽取、初稿和交叉检查，结果须由 Codex 回到全文、代码或官方材料复核。

### 目标

基于 TASK-004、005、006 已验收成果，形成正式中文技术调研报告、约 20–25 页组会 PPT、更新后的 Research Portal、引用与证据核查记录，以及 2–3 条不预设为最终方向的候选研究路线。报告服务于 DAS 光电混合集成芯片、Photonic AI Computing 和通用光芯片设计 Agent Harness 三层课题目标。

### 方法

- 采用结构化 scoping review（范围综述）与主题综合，不把本轮误称为穷尽式系统综述或元分析；
- 使用 `literature-review` 组织范围、筛选、主题综合和引用核验；
- 使用 `nature-academic-search` 仅补充缺失代表工作与核验引文；
- 使用 `nature-reader` 对影响研究现状与候选路线的核心论文做全文、页码、图表和方法级核证；
- 使用 `scientific-critical-thinking` 对路线级结论、性能口径、系统边界和最强反例进行对抗性审查；
- 延续 `FACT / AUTHOR CLAIM / CODE VERIFIED / INFERENCE / UNKNOWN` 标签，并明确理论、数值仿真、芯片实验和系统级演示的差别。

### 允许范围

- 复用并综合 TASK-004、005、006 的研究材料，不简单拼接旧 Markdown；
- 对现有候选集进行定向全文复核、引文核验和必要的少量补证据；
- 在 `references/task-007/` 编写正式报告、证据矩阵、术语表、全文核查记录和候选路线总结；
- 使用 presentation-skill 的持久化 workspace 制作可编辑 PPTX，并执行几何与视觉 QA；
- 将正式报告、三方向现状、比较矩阵和候选路线接入现有 MkDocs Portal；
- 更新项目事实源并形成可追溯 Git 提交。

### 禁止范围

- 不开展课题组资源匹配或实施可行性评估；
- 不设计最小实验、成败判据、实验预算或具体实施协议；
- 不确定最终研究方向、论文创新点或工程路线；
- 不实现或运行 Agent、Harness、MCP、Tool Adapter、benchmark、solver、仿真或芯片设计；
- 不把论文作者指标写成本项目实验结果，不把个人偏好写成既定科研路线；
- 不访问或修改 `D:\AI_PIC_Demo`；
- 不自动启动后续工程任务。

### 核心交付物

1. 正式技术调研报告；
2. 约 20–25 页、面向 20 分钟组会的可编辑 PPT；
3. 更新后的 Research Portal；
4. 引用、全文与证据核查记录；
5. 2–3 条 Candidate Research Routes 与尚待解决问题总结。

### 验收要求

- 三方向均按“技术原理 → 主要路线 → 代表成果 → 实际进展 → 难点 → Research Gap”综合；
- 重要结论可追溯到论文全文、官方技术文档、公开代码或实验数据；
- 明确区分器件、芯片、光电混合模块和完整系统，及 GDS、DRC、LVS、物理仿真、PDK compliance、foundry signoff；
- 报告与 PPT 不预设最终研究方向，不包含实验设计；
- 引用元数据、DOI/URL、正文引用和参考文献表一致；
- PPT 通过 presentation-skill 的自动 QA 和至少一轮渲染后视觉复核；
- Portal 通过 `mkdocs build --strict`；文档通过 `git diff --check`，最终形成干净提交。

### 完成回传

完成后进入 `TASK-007_REVIEW_READY`，回传 Git commit、工作树状态、报告与 PPT 路径、Portal 入口、章节概览、证据与质量检查、未决问题，以及 Qwen 子任务和 Codex 复核记录。等待 GPT 和用户验收，不自动进入工程实现或研究路线选定。

### 完成记录

- 完成日期：2026-09-21。
- 交付提交：`3ed876f5fce34d38a47907d6c68c476f6a51d090`。
- 正式报告及证据记录：`references/task-007/`。
- 组会 PPT：`presentations/task-007-group-meeting/TASK-007-组会汇报.pptx`；25 页，可编辑源为同目录 `outline.json` 和 workspace 文件。
- Portal：新增 TASK-007 首页、正式报告、全文证据审计、引用核验、检索、术语和候选路线页面。
- Qwen：在既有项目主对话完成一次只读术语、证据标签和跨文件矛盾审计；Codex 复核后采纳“作者指标统一降为作者报告”“明确全文核读途径”等建议，驳回其因并发时点导致的文件缺失误报及无证据的 PhIDO 期刊名质疑。
- 引用核验：Crossref 核对 20 个核心 DOI 的题名、年份和载体；5 个 arXiv、1 个 arXiv DOI 和 3 个官方仓库链接可解析；报告 9 个本地引用均已解析。
- PPT 自动 QA：25 页，overflow 0、overlap 0、placeholder 0、geometry error 0、design error/warning 0/0；保留 3 个非阻断 geometry warning。
- PPT 视觉 QA：因本机无 `soffice`，使用 Microsoft PowerPoint 导出 25/25 张 1600×900 PNG；第一轮发现并修复 Mermaid 中文字体缺失和末页失衡，第二轮复查通过。
- Portal：`mkdocs build --strict` 通过；静态产物含首页、报告、证据审计、路线和引用页面。
- 未执行：实验、仿真、benchmark、Agent/Harness 实现、课题组资源匹配或最终路线选择。
- GPT 验收：2026-09-23 针对交付提交 `3ed876f5fce34d38a47907d6c68c476f6a51d090` 返回 `TASK-007_ACCEPTED`，状态为 `ACCEPTED / CLOSED`。
- 关闭边界：TASK-007 的调研报告与组会汇报交付已完成；当前没有新的执行任务。验收不代表确定了最终研究路线，也不授权实验、仿真或工程实现；后续工作须另行建立并授权任务。

---

# 最近关闭任务记录

## TASK-006：三方向比较与候选研究路线收敛

- 状态：`ACCEPTED / CLOSED`
- 首次启动日期：2026-09-17；综合路线任务确认日期：2026-09-20
- 起始提交：`0da0996543cff09f17751472f8e53efd2a8b8be9`
- 前置任务：`TASK-004 / TASK-005 / TASK-005A = ACCEPTED / CLOSED`
- 授权来源：用户提供完整 TASK-006 规格并要求在已有工作基础上继续执行。
- 执行协调器：Codex；Qwen 项目主对话承担有收益的独立只读子任务，结果须由 Codex 复核。

### 目标

在 Phase 1 范围内比较“DAS 光电混合集成 × 面向智能体的 PIC 设计”交叉场景、光子人工智能计算，以及面向智能体的 PIC 设计通用方法，并完成跨方向和内部切入点比较，最终提出 2–3 条可开展最小验证实验的候选研究路线。

### 现有基础

- `research/03_AGENTIC_PIC_DESIGN.md` 已形成模型内化/Harness 外化、RQ-01 至 RQ-06、Benchmark 与失败归因候选框架；
- `research/04_COMPARATIVE_ANALYSIS.md` 已形成横向比较维度草案；
- TASK-004/005 已验收证据继续有效，不重新开展无边界扫描；
- 上述内容是本轮输入，不是已经完成综合路线收敛的证明。
- 用户已授权将 Paper2Agent 增补为 `03 Agentic PIC Design` 下的正式调研候选，仅核验论文、源码和 PIC 迁移边界；不安装、不运行、不接入，也不据此改变研究路线。
- 用户已要求以“DAS 光电混合集成 × 面向智能体的 PIC 设计”替换原先孤立的 DAS 方向，并对技术地图中的代表项目逐项补充问题、路线、输入输出、完成度、依赖、验证、局限和本项目关系；非必要英文改为中文，必须保留的英文术语首次出现时给出中文解释。

### 允许范围

- 补充 2021–2026 DAS 交叉场景与光子人工智能计算的一手文献和官方证据；
- 继续整理 Agentic PIC Design 的研究缺口、内部子方向和最小实验；
- 新增 `references/task-006/` 调研、比较、路线、证据与对抗性审查 Markdown；
- 更新 `research/`、`docs/` 与现有 MkDocs Research Portal 的阅读入口；
- 使用 `nature-academic-search`、`nature-reader`、`scientific-critical-thinking` 和范围稳定后的 `literature-review`；
- 更新事实源并形成可追溯 Git 提交。

### 禁止范围

- 不实现 Agent、MCP、Tool Adapter、simulator、benchmark 或新的 PIC Harness 功能；
- 不运行正式仿真、工程实验或物理验证；
- 不把外部论文指标表述为本项目实验结果；
- 不把未确认的软件许可证、算力、PDK、流片、封装或测试条件视为已具备；
- 不修改或访问 `D:\AI_PIC_Demo`；
- 不启动 TASK-007，不撰写最终 L01 报告。

### 核心交付物

1. 三方向领域全景与技术地图；
2. 跨方向 Comparative Analysis Matrix 与 Agentic PIC 内部比较；
3. 研究条件确认矩阵；
4. 2–3 条 Candidate Research Routes；
5. 每条路线的最小验证实验、成功/失败判据、风险与简化替代方案；
6. 路线级对抗性审查、关键证据链与 strongest counterexamples；
7. Research Portal 阅读入口。

### 证据与验收规则

- 核心判断标记 `FACT / AUTHOR CLAIM / CODE VERIFIED / INFERENCE / UNKNOWN`；
- 三方向均须给出技术路线、代表工作、实际能力、限制和 Research Gap；
- Agentic PIC 内部须比较 DesignSpec/IR、Tool/Solver Adapter、RESULT/Evidence Ledger、Adaptive Tool Calling、Verification/Benchmark 与 Failure Recovery；
- 必须区分理论、数值仿真、芯片实验、完整系统，以及 device-level 与 circuit/system-level；
- 候选路线必须从证据推导，不能只是开源项目拼装；
- 完成后进入 `TASK-006_REVIEW_READY`，附 Git、门户、关键证据、反例和待导师/李师兄确认条件；用户验收前不启动 TASK-007。

### 完成记录

- 完成日期：2026-09-20。
- 交付目录：`references/task-006/`；门户入口位于 `portal/docs/task-006-*.md`。
- 已形成三方向技术地图、跨方向矩阵、Agentic PIC 内部比较、条件确认矩阵、三条候选路线、最小实验及成败判据、路线级反例和一手来源日志。
- 已增补 Paper2Agent 候选技术记录，并将其定位到“科学方法/代码 → Tool Registry/Adapter”的构建与验证入口；未把作者成功率迁移到 PIC，也未将自动工具生成确定为技术路线。
- 已将原 DAS 独立方向重构为“DAS 光电混合集成 × 面向智能体的 PIC 设计”交叉验证场景，并为 DAS 物理基线、光子人工智能计算和面向智能体的 PIC 设计代表项目建立逐项详解；没有把交叉场景写成已经实现的系统。
- 已整理 Research Portal 标签层级：三方向细分页、比较与路线、TASK-005 档案分别使用可折叠导航文件夹，减少一级标签数量并保留原页面地址。
- 已增加论文与项目出处索引及门户入口；32 篇论文与 11 个纯项目/工具分开登记，项目标题可直接打开一手论文或官方仓库，固定提交与许可证边界继续保留。
- 已生成并核对 32 条唯一记录的 Zotero RIS 包；既有 PhIDO 加新增 31 条已通过官方 Connector 写入四个中文主分类，API 核验顶层条目 36 个且题名唯一。英文旧分类尚未删除。
- 已对用户提供的 Jin 等 OFC 2026 原文完成页级核读，并把 InP–SOI 混合集成 DAS 解调器拆为独立项目；全文证据用于收窄激光–PIC–封装接口缺口，不把 3 页会议结果外推为完整系统、长期可靠性或制造证据，也不改变当前候选路线排序。
- 已读回 GPT 的 TASK-006 补充对抗性审查，并将五层约束接口、独立验证原则、最小闭环与验证层级按 `INFERENCE` 去重纳入研究事实源；未将 GPT 标为 `UNKNOWN` 的外部线索直接写成已核验证据，也未改变候选路线排序。
- 本轮 Qwen 只读批量抽取已由 Codex 复核；数据集 DOI、纯仓库、重复预印本和错误期刊字段未进入最终文献集合。
- Qwen 通过既有项目主对话完成 DAS/PAC 只读候选整理；Codex 已纠正其 arXiv DAS 覆盖不足，并回到 Optica、Nature、Science、IEEE 等一手来源复核。
- 未执行 Agent/benchmark/simulator 实现、正式仿真、流片、封装或物理实验；外部作者指标均未复算。
- 当前只进入审查，不启动 TASK-007。
- 用户已取消此前讨论中的 `TASK-007｜实验设计`。TASK-006 验收后的当前允许方向仅为调研证据整合与经授权的 L01 报告整理；不得自动起草或实施 benchmark、仿真、Harness、对照实验或其他实验设计。
- GPT 验收：2026-09-21 针对提交 `9cab614ce29b7ed4289f641c0d7a7eb5f277e24f` 返回 `TASK-006_ACCEPTED`，状态为 `ACCEPTED / CLOSED`。
- 关闭边界：TASK-006 的调研交付已经完成。当前不存在执行任务；后续只能在用户另行授权后开展 L01 报告整理或新任务，不得自动启动工程、实验或 TASK-007。

### 延后研究事项（不属于当前执行范围）

#### Jev 类有限决策模型在 PIC Agent Harness 中的适用性

- 状态：`DEFERRED`。
- 候选用途：未来可评估其作为 Harness 决策组件，用于工具路由、失败分类和自适应 Tool Calling 等场景。
- 比较要求：与确定性规则以及现有通用 LLM/Qwen 方案进行受控比较，判断是否确实带来准确性、可靠性、成本或效率收益。
- 证据边界：目前没有 PIC 场景下的充分验证证据，不将其确定为技术路线或核心创新点。
- 触发时机：完成主要领域调研并开始收敛技术路线，或准备设计工具路由、失败分类、自适应 Tool Calling 对照实验时。
- 触发动作：Codex 应主动询问用户：“此前记录了 Jev 类有限决策模型这一候选方案。当前是否需要将其纳入技术比较或实验设计？”
- 授权边界：用户确认前，不启动 Jev 专项调研，不安装、接入或实现 Jev，也不为此创建新的执行任务。
- 最新状态：用户于 2026-09-21 明确要求该调研暂时延后，继续保持 `DEFERRED`。

---

# 前置已关闭任务记录

## TASK-005A：Research Portal MVP

- 状态：`ACCEPTED / CLOSED`
- 启动日期：2026-09-16
- 前置任务：`TASK-005 = ACCEPTED / CLOSED`
- 授权来源：用户在当前对话中正式批准。
- 执行协调器：Codex；主要搭建工作优先委托既有 Qwen 项目主对话，Codex 负责最终复核、运行和截图验收。

### 目标

基于 `references/task-005/` 现有 Markdown，使用 MkDocs Material 建立最小可用的本地 Research Portal。原 Markdown 保持 Source of Truth；Portal 只增加人工阅读层，不修改研究结论或证据。

### 允许范围

- 新增 MkDocs 配置、Portal 首页、必要的轻量 CSS/JavaScript 和依赖/启动说明；
- 通过链接、导航或构建时映射访问现有 `references/task-005/` Markdown；
- 为长表格增加横向滚动，为 Mermaid 增加本地渲染支持；
- 本地安装仅用于验证的 Python 文档依赖；
- 更新本任务状态和当前事实源。

### 禁止范围

- 不重写、删除或复制改写 `references/task-005/` 的研究内容；
- 不新增研究结论；
- 不引入 React、Vue、数据库或后端服务；
- 不实现 Agent、Tool、MCP、DesignSpec、RESULT、benchmark 或仿真功能；
- 不访问或修改 `D:\AI_PIC_Demo`；
- 不启动 TASK-006。

### 首页与导航验收

首页须在 5–10 分钟内覆盖：一句话结论、技术地图、Capability Matrix、Reference Architecture V0、Research Gap → Entry Point、5 个 Route Seeds 和 Evidence/Source Log 入口。左侧导航按 Overview、Technical Map、Capability Matrix、Reference Architecture、Research Gaps、Candidate Routes、Evidence & Sources 组织。详细证据链接到原 Markdown。

### 验证方法

- `mkdocs build --strict` 成功；
- 本地 `mkdocs serve` 可启动并访问；
- 浏览器检查首页、导航、原始 Markdown 链接、横向表格和 Mermaid；
- 保存页面截图；
- 核对 `references/task-005/` 原文件未被修改；
- 执行 `git diff --check` 并形成干净 commit。

### 完成回传

完成后进入 `TASK-005A_REVIEW_READY`，附启动方式、页面结构和截图。用户验收前不启动 TASK-006。

### 完成记录

- 完成日期：2026-09-16。
- 起始提交：`f4e88819535633cacf2d2d5f6d1c2fcfa7757129`。
- 门户实现与验收证据提交：`b1f9c74650451734fd11d381387684fecb4ab82d`。
- 已新增 MkDocs Material 配置、中文总览首页、七组中文左侧导航、Source of Truth 包装页、宽表格滚动样式、Mermaid 渲染脚本、PowerShell 安装/启动脚本和本地截图；必要英文技术术语均附中文表达。
- `references/task-005/` 未修改；门户通过构建时嵌入和链接读取原 Markdown，不复制改写研究结论。
- Qwen 项目主对话只提供信息架构、文件结构和验证清单草案；由于该会话无 shell/写入能力，实际文件修改、MkDocs 配置纠错、浏览器验证和截图均由 Codex 完成。Codex 已纠正其不适用的 snippet 语法和 Mermaid formatter 名称。
- 已验证：`mkdocs build --strict` 成功；本地服务可访问；首页、七组导航、证据页、宽表格横向滚动和 Mermaid SVG 均经真实浏览器检查；截图位于 `output/playwright/`。
- 在 `TASK-005A` 交接提交形成时尚未启动 TASK-006；此项只记录当时状态，不覆盖用户随后对 TASK-006 的明确启动授权。
- GPT 验收：2026-09-20 针对提交 `0da0996543cff09f17751472f8e53efd2a8b8be9` 返回 `TASK-005A_ACCEPTED`，状态为 `ACCEPTED / CLOSED`。
- 验收结论：本地构建、页面访问、内容展示和原始证据保留符合要求；原 Markdown 继续作为 Source of Truth，MkDocs 作为统一阅读展示层。
- 关闭边界：不再为 TASK-005A 增加非必要功能；后续调研可以复用当前展示结构，但不得据此扩大网页工程范围。
- 后续状态：保留已经启动的 `TASK-006`，不得重置为 `NOT_STARTED`，也无需重新启动或重复创建。

---

## TASK-005：L01 核心架构深挖与 PIC Harness 技术路线收敛

- 状态：`ACCEPTED / CLOSED`
- 启动日期：2026-09-16
- 前置任务：`TASK-004 = ACCEPTED / CLOSED`
- 授权来源：用户在当前对话中正式批准启动，并给出完整范围、方法、交付物和验收标准。
- 执行协调器：Codex。
- 目标：对 TASK-004 核心对象进行一手证据级深挖，连接“现有工作 → 技术缺口 → 本项目可能切入点”。本任务不是最终 L01 报告，也不进行代码实现。

## 核心对象

必须深挖：PhIDO / PhIDO-Agentic、AutoPhotonicDesign、gdsfactory + gplugins、PICBench。

架构机制参照：OpenROAD-MCP、MetaChat。

条件对象：PICopilot 仅使用可验证论文证据；PICasso 无公开实现时不得作源码级结论。除非出现会实质改变当前判断的一手证据，不继续无边界扩充候选池。

## 方法与证据规则

- 显式使用 `nature-reader` 定向精读；使用 `scientific-critical-thinking` 审查会影响路线选择的结论；`nature-academic-search` 仅用于补证据，不做大规模方向扫描。
- 本轮不启动 `literature-review` 或 `nature-literature-pipeline`。
- Qwen 科研子任务由 Codex 统一通过项目主对话或必要的新对话下达，并尽量减少对话数。Qwen 输出只是中间材料，未经 Codex 一手证据复核不得进入结论。
- 每项证据和判断明确区分 `FACT`、`AUTHOR CLAIM`、`CODE VERIFIED`、`INFERENCE`、`UNKNOWN`。
- 论文目标、README 宣传、LLM 输出和合理猜测均不能替代源码、论文正文、官方文档或可复核结果。

## 强制技术层级地图

每个核心对象映射到：

```text
Requirement / Natural Language
↓
DesignSpec / typed IR / DSL
↓
Agent / Harness / Planning
↓
Knowledge / RAG / PDK
↓
Tool Calling
↓
Device / Circuit Design
↓
Physical Simulation
↓
Optimization / Inverse Design
↓
Layout / GDS / Routing
↓
Verification / DRC / Physical Checks
↓
Feedback / Failure Recovery
```

每层只能标记 `IMPLEMENTED`、`PARTIAL`、`ABSENT` 或 `UNCLEAR`，并给一手证据。

## 每个对象统一问题

1. 解决了什么具体问题；
2. 采用了什么技术路线；
3. 实际做到什么程度；
4. 还存在什么关键缺口；
5. 哪些缺口是本项目现有条件可能切入的。

第五项形成 `Research Gap → Our Entry Point`；证据不足时标记 `UNRESOLVED`。

## 六个重点专题

1. **DesignSpec / IR**：NL 入口、JSON/schema/DSL/netlist/Python、typed validation、约束表达和 PDK/device knowledge 绑定。
2. **Agent / Harness / Tool Adapter**：tool schema、参数验证、registry、执行边界、session、错误处理、structured output；区分脚本生成与稳定 Tool Contract。
3. **Physical Simulation → RESULT**：核验 solver 实际执行、输入追溯、材料/网格/边界/波长、结构化输出、指标计算和失败处理；形成 RESULT schema V0 草案。
4. **Evaluation / Benchmark**：深挖 PICBench 的 golden reference、simulator-based evaluation、functional metric、syntax validation、pass@k 和自动判定边界；形成分层 benchmark。
5. **State / Retry / Failure Recovery**：比较 experiment history、checkpoint、retry budget、failure class、keep/discard、rollback、human intervention 和 termination；形成最小状态机草案。
6. **Verification Ladder**：严格区分 Syntax、Geometry Validity、DRC、Circuit-level Simulation、Full-wave Simulation、LVS/Connectivity、PDK Compliance、Process Corner/Robustness、Foundry Signoff。

不得把 GDS generated、DRC clean 或 solver called 表述为“设计已验证”。

## 核心交付物

A. 核心工作技术层级地图。

B. 六个核心对象架构拆解，逐层标记 `IMPLEMENTED / PARTIAL / ABSENT / UNCLEAR`。

C. Harness Capability Matrix，至少包含 Spec/IR、Knowledge、Planner、Tool、Simulation、RESULT、Evaluator、Retry、Layout、DRC、LVS、Signoff、Benchmark。

D. PIC_Harness_Research Reference Architecture V0：Requirement → DesignSpec/IR → Planner/Harness → Knowledge/PDK → Tool Registry/Adapter → Execution/Solver → RESULT → Evaluator → State/Evidence Ledger → Retry/Recovery → Layout → Verification Gate。

E. Build vs Reuse，每项只允许 `REUSE`、`WRAP`、`BUILD` 或 `UNDECIDED`。

F. Research Gap → Our Entry Point Matrix。每项记录 Current State、Research Gap、Existing Evidence、Our Available Conditions、Our Entry Point、Main Risk 和 Simpler Alternative。

G. 3–5 个 Candidate Route Seeds，暂不最终确定路线。

另需形成 RESULT schema V0、PIC Harness 最小状态机、分层 benchmark、路线关键证据链、strongest counterexamples 和当前五个最大未决问题。

## 验收标准

- 至少 4 个核心对象完成一手材料或源码级拆解；
- 所有重要判断可追溯到论文、代码或官方文档；
- 明确区分五类证据标签；
- gdsfactory/gplugins 按 Tool Layer 分析；PICBench 按 Evaluator/Benchmark Layer 分析；
- 明确 AutoPhotonicDesign 的科研证据限制；
- 不把 DRC 等同 LVS/signoff，不把 solver invocation 等同 physical correctness；
- 形成有证据支撑的 Reference Architecture V0、主要 Research Gaps 和至少 3 个 Route Seeds；
- 不写工程代码，不启动 TASK-006，不开始撰写最终 L01 报告。

## 禁止范围与停止条件

- 不修改或复制 `D:\AI_PIC_Demo`；
- 不实现 Agent、MCP、RAG、DesignSpec、RESULT、benchmark、仿真或验证功能；
- 不安装或迁移候选框架作为工程依赖；
- 不将外部论文结果表述为本项目实验结果；
- 完成后只进入 `TASK-005_REVIEW_READY` 并提交规定材料；GPT 验收前不得启动 TASK-006。

## 验证方法

- 论文结论核对正文、图表、方法、实验与限制，而不只读摘要；
- 开源项目记录仓库 URL、许可证、核验 commit、关键源码路径和实际调用边界；
- 路线级判断给出多来源证据、strongest counterexample、evidence gap、hidden assumptions、failure modes、opportunity cost 和 simpler alternative；
- 文档完成后执行路径检查、字段完整性检查、`git diff --check` 和 Git 状态检查。

## 完成与验收记录

- 完成日期：2026-09-16。
- 交付目录：`references/task-005/`。
- 已完成：技术层级地图、六对象五问拆解、Harness Capability Matrix、Verification Ladder、Reference Architecture V0、RESULT schema V0、最小状态机、Build vs Reuse、Research Gap Matrix、5 个 Candidate Route Seeds、路线级对抗性审查和五大未决问题。
- Qwen：通过既有项目主对话完成一次六对象合并的只读字段/缺口抽取；Codex 已对核心字段逐项回到论文、官方文档和固定 commit 源码复核，并纠正 PICBench simulation 层级、MetaChat stub/backend 差异等问题。
- 未执行：候选代码、solver、DRC、benchmark 或物理实验；外部论文指标均未复算。
- GPT 验收：2026-09-16 返回 `ACCEPT`，无需打回修改。
- 后续约束：TASK-006 必须先区分 device-level 与 circuit-level；verification 使用 `Research-grade deterministic verification` 的诚实上限；正式报告区分 implementation reuse 与 architecture-pattern reuse；DesignSpec 仍是待实验验证的工程假设，不得预设为科研创新。
- 验收当时边界：`TASK-006 = NOT_STARTED`。该句记录 TASK-005 验收时点；用户后续已独立授权启动 TASK-006。
