# 当前任务与任务记录

## TASK-009：PIC × AI Agent 科研英语词库 V1

- 状态：`DELIVERED`（2026-09-23，待用户在 Knowt 实际导入）
- 授权来源：用户明确要求直接制作约 200 张专业科研英语单词卡，交付 Excel 与 UTF-8 TSV。
- 允许范围：复用本仓库已核验调研及术语表，并核对 Knowt 官方手动导入说明；仅新增 `learning/vocabulary/` 成品及本任务记录。
- 禁止范围：不修改原研究结论、技术路线、代码，不运行科研实验，不访问 `D:\AI_PIC_Demo`，不宣称已在用户账户中导入成功。
- 交付：`learning/vocabulary/PIC_AI_Research_Vocabulary_V1.xlsx` 和 `learning/vocabulary/Knowt_Import_V1.tsv`，共 200 条；A/B/C/D/E 分别 40/45/35/45/35。
- 验证：独立用只读 `openpyxl` 打开 XLSX，核对两张工作表、列名、数量、分类、术语去重、非空字段及 200 行导入页与 TSV 逐行一致；两张工作表首段已渲染目视检查。Knowt 网页端粘贴导入尚未在用户账户实测。
- iPhone 直传补充：用户提供 Knowt App“从设备上传文件”截图后，按 Knowt 官方支持的 PDF 文件入口，新增 `learning/vocabulary/Knowt_iPhone_Upload_V1.pdf`。PDF 为 16 页，每条以 `Term` 和 `Definition` 连续排版；文本读回检查 200 对，按忽略换行的原文核对均与 Excel 导入页一致，并目视检查首、中、末页。文件已上传至用户 Google Drive 且核对为 PDF。Knowt 的 PDF 路径使用 AI 生成卡片，是否逐字保留 200 张需用户上传后在 App 内检查。

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
