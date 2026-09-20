# 当前唯一执行任务

## TASK-006：三方向比较与候选研究路线收敛

- 状态：`TASK-006_REVIEW_READY`
- 首次启动日期：2026-09-17；综合路线任务确认日期：2026-09-20
- 起始提交：`0da0996543cff09f17751472f8e53efd2a8b8be9`
- 前置任务：`TASK-004 / TASK-005 / TASK-005A = ACCEPTED / CLOSED`
- 授权来源：用户提供完整 TASK-006 规格并要求在已有工作基础上继续执行。
- 执行协调器：Codex；Qwen 项目主对话承担有收益的独立只读子任务，结果须由 Codex 复核。

### 目标

在 Phase 1 范围内比较 DAS 光电混合集成、Photonic AI Computing 与 Agentic PIC Design 三条研究线，并完成跨方向与 Agentic PIC 内部切入点比较，最终提出 2–3 条可开展最小验证实验的候选研究路线。

### 现有基础

- `research/03_AGENTIC_PIC_DESIGN.md` 已形成模型内化/Harness 外化、RQ-01 至 RQ-06、Benchmark 与失败归因候选框架；
- `research/04_COMPARATIVE_ANALYSIS.md` 已形成横向比较维度草案；
- TASK-004/005 已验收证据继续有效，不重新开展无边界扫描；
- 上述内容是本轮输入，不是已经完成综合路线收敛的证明。

### 允许范围

- 补充 2021–2026 DAS 与 Photonic AI Computing 的一手文献和官方证据；
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
- Qwen 通过既有项目主对话完成 DAS/PAC 只读候选整理；Codex 已纠正其 arXiv DAS 覆盖不足，并回到 Optica、Nature、Science、IEEE 等一手来源复核。
- 未执行 Agent/benchmark/simulator 实现、正式仿真、流片、封装或物理实验；外部作者指标均未复算。
- 当前只进入审查，不启动 TASK-007。

### 延后研究事项（不属于当前执行范围）

#### Jev 类有限决策模型在 PIC Agent Harness 中的适用性

- 状态：`DEFERRED`。
- 候选用途：未来可评估其作为 Harness 决策组件，用于工具路由、失败分类和自适应 Tool Calling 等场景。
- 比较要求：与确定性规则以及现有通用 LLM/Qwen 方案进行受控比较，判断是否确实带来准确性、可靠性、成本或效率收益。
- 证据边界：目前没有 PIC 场景下的充分验证证据，不将其确定为技术路线或核心创新点。
- 触发时机：完成主要领域调研并开始收敛技术路线，或准备设计工具路由、失败分类、自适应 Tool Calling 对照实验时。
- 触发动作：Codex 应主动询问用户：“此前记录了 Jev 类有限决策模型这一候选方案。当前是否需要将其纳入技术比较或实验设计？”
- 授权边界：用户确认前，不启动 Jev 专项调研，不安装、接入或实现 Jev，也不为此创建新的执行任务。

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
