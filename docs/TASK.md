# 当前唯一执行任务

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
- 当前边界：`TASK-006 = NOT_STARTED`。本次验收不自动授权启动 TASK-006。
