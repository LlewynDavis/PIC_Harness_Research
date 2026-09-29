<div class="sot-note">事实源：<code>references/task-016-evidence/agentic-pic-comparison.md</code>。本页为构建时阅读副本。</div>

# Agentic PIC 三项目证据比较

此表比较论文实际展示的输入、处理与验证对象。数值和实现细节均回到原文定位；论文结果仍是 `AUTHOR CLAIM`，不是本项目复现。

| 项目 | 核心输入 | Agent / Harness | 工具 / Simulator | 输出 | 验证层级 | 物理约束处理方式 | 当前边界 |
|---|---|---|---|---|---|---|---|
| [PhIDO](https://doi.org/10.1063/5.0300741) | 自然语言 PIC 描述，含功能块、连接、部分参数 | Interpreter 和 Designer 两个 LLM Agent；RAG、YAML DSL、Pydantic schema | 模板/PDK 描述；GDSFactory 版图与 DRC；SAX 电路模型 | schematic、PIC DSL、GDSII | benchmark `S`=有效 schematic 与 GDSII；102 prompt、510 次/模型，结构有效性 | 提取用户参数，匹配 PDK 组件；路由规则与 DRC；SAX 可供电路评价 | 论文明确以结构有效为主；非目标光学性能通过、真实 PDK 签核或流片。Fig. 1/Table II，PDF p.3/9，§II.E。 |
| [PICopilot](https://doi.org/10.48550/arXiv.2608.01791) | 自然语言脚本任务，版图、DRC、FDTD 等工具操作 | Task Planner、功能专用 Script Generator、Synthesizer、Evaluator；工具手册 RAG | 内部：静态代码检查＋自定义检查库＋LLM；benchmark 外部：执行脚本、比对参考输出 | Python PIC 设计脚本 | 48 任务的功能输出一致；每任务 15 次，≥3 次成功计 `#Solved` | 工具 API 手册检索与静态代码检查；未展示内部物理求解器反馈 | 内部反馈不等于 execution feedback；脚本功能正确不等于器件目标性能，公开实现未核。Fig. 2/Table 2–3，PDF p.3/7，§3.6。 |
| [Kharel 2026](https://doi.org/10.48550/arXiv.2606.00915) | 人类提供的目标、约束、初始仿真文件、可编辑设计参数与评价器 | 通用 coding Agent，日志记录假设与迭代；可切换拓扑和策略 | Tidy3D 等多物理求解器、PhotonForge、几何/工艺/物理一致性 DRC | 仿真设计、布线布局、数值指标及日志 | 工程师给定的定量 acceptance criteria；器件/多物理仿真、DRC | 最小特征、几何、工艺栈、浮置区域、光模交叠等显式闸门；仿真结果决定保留/回退 | 多物理初设曾出错，专家修正后才进入自治优化；未流片验证。Fig. 1–6/Table S2–S3，PDF p.3–10/20。 |

**可复核的差异。** PhIDO 主要检验 `NL → 结构化设计/GDS`；PICopilot 检验 `NL → 脚本及外部执行评分`；Kharel 检验 `人类给定目标和评价器 → 显式规则 → 数值求解器 → 定量验收与迭代`。三者的输入、成功定义和验证层级不同，因此不能用单一成功率排序。`INFERENCE`，依据上表所列 Fig./Table/Section。

**当前问题。** 与“AI 如何理解真实 PIC 设计需求与物理约束？”最直接相关的缺口是：从自然语言到形式化约束后，能否在 PDK、几何、求解器和验收判据之间传递一致语义；当评价器或仿真设置本身错误时如何发现。Kharel §S6 的人工修正是具体反例，不支持宣称 Agent 已独立建立正确物理模型。
