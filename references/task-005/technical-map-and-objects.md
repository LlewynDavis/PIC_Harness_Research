# TASK-005 技术层级地图与六对象拆解

证据标签沿用 [source-log.md](source-log.md)。层级状态只能取 `IMPLEMENTED`、`PARTIAL`、`ABSENT`、`UNCLEAR`。状态表示“公开实现实际覆盖程度”，不是作者愿景，也不是本项目复现结果。

## A. Agentic PIC 技术层级地图

| 技术层 | PhIDO / Agentic | AutoPhotonicDesign | gdsfactory + gplugins | PICBench | OpenROAD-MCP | MetaChat |
|---|---|---|---|---|---|---|
| Requirement / Natural Language | `IMPLEMENTED` | `PARTIAL` | `ABSENT` | `IMPLEMENTED` | `ABSENT` | `IMPLEMENTED` |
| DesignSpec / typed IR / DSL | `IMPLEMENTED` | `PARTIAL` | `PARTIAL` | `PARTIAL` | `PARTIAL` | `PARTIAL` |
| Agent / Harness / Planning | `PARTIAL` | `IMPLEMENTED` | `ABSENT` | `ABSENT` | `ABSENT` | `IMPLEMENTED` |
| Knowledge / RAG / PDK | `PARTIAL` | `PARTIAL` | `IMPLEMENTED` | `ABSENT` | `ABSENT` | `PARTIAL` |
| Tool Calling | `IMPLEMENTED` | `PARTIAL` | `PARTIAL` | `PARTIAL` | `IMPLEMENTED` | `IMPLEMENTED` |
| Device / Circuit Design | `IMPLEMENTED` | `IMPLEMENTED` | `IMPLEMENTED` | `PARTIAL` | `ABSENT` | `IMPLEMENTED` |
| Physical Simulation | `PARTIAL` | `IMPLEMENTED` | `IMPLEMENTED` | `ABSENT` | `ABSENT` | `PARTIAL` |
| Optimization / Inverse Design | `PARTIAL` | `IMPLEMENTED` | `PARTIAL` | `ABSENT` | `ABSENT` | `IMPLEMENTED` |
| Layout / GDS / Routing | `IMPLEMENTED` | `IMPLEMENTED` | `IMPLEMENTED` | `ABSENT` | `PARTIAL` | `PARTIAL` |
| Verification / DRC / Physical Checks | `PARTIAL` | `PARTIAL` | `PARTIAL` | `PARTIAL` | `PARTIAL` | `PARTIAL` |
| Feedback / Failure Recovery | `PARTIAL` | `PARTIAL` | `ABSENT` | `PARTIAL` | `PARTIAL` | `PARTIAL` |

### 地图的一手证据说明

- **PhIDO / Agentic**：`CODE VERIFIED` YAML/DSL、Pydantic `DesignIntent`/`CircuitDSL`、MCP tools、gdsfactory GDS、SAX 与 KLayout DRC 均有实现。`PARTIAL` 的原因是主路径没有全波物理仿真、知识与增强门可降级、state/retry 不是完整事务性恢复。
- **AutoPhotonicDesign**：`CODE VERIFIED` coding agent 可编辑脚本并调用 Tidy3D、KLayout 和 PhotonForge，`orchestrate.py` 自动 keep/discard/revert。NL 主要通过给 coding agent 的 program prompt 进入；没有独立 typed DesignSpec 或稳定 tool registry，因此相关层只到 `PARTIAL`。
- **gdsfactory + gplugins**：`CODE VERIFIED` typed netlist/PDK、GDS/routing、SAX 与多种 solver adapter。它是确定性 Tool Layer，不含 planner、统一 state/retry 或证据账本，不能称为 harness。
- **PICBench**：`CODE VERIFIED` NL 题目 → JSON netlist → SAX circuit response → golden comparison → error feedback。SAX 是 circuit-level compact-model evaluation，不是 physical/full-wave simulation；无 GDS/DRC/LVS。
- **OpenROAD-MCP**：`CODE VERIFIED` MCP schema、query/exec boundary、PTY session、history、structured errors 和 ORFS gate 汇总。其 layout/verification 发生在电子 EDA 域，因此作为 PIC 层级只记 `PARTIAL`，不能借用其 RTL-to-GDS 能力宣称 PIC coverage。
- **MetaChat**：`CODE VERIFIED` AIM 迭代 agent、工具 registry、materials agent、Docker/GPU 设计 backend、surrogate optimization 和 GDS 导出。物理层使用训练于 FDFD 的 surrogate；论文展示 FDFD 计算作结果检查，但不是每轮传统 full-wave solver，因此记 `PARTIAL`。

## B1. PhIDO / PhIDO-Agentic

### 1. 解决了什么具体问题？

把自然语言 PIC 需求转为结构化电路、原理图和可布线 GDS，并在通用 PDK 上做结构检查、SAX circuit simulation 与 DRC。Agentic 分支尝试用 typed contracts、MCP tools、形式化 topology gate 和显式 orchestration 提升基线的可控性。`FACT` / `CODE VERIFIED`

### 2. 技术路线

PhIDO 论文路线为 Interpreter → Designer → Layout → Circuit verification；YAML DSL 描述 components、connectivity、PDK 和目标波长，gdsfactory 生成版图，SAX 进行 circuit-level simulation，KLayout 运行 DRC。Agentic 源码进一步引入 `DesignIntent`、`CircuitDSL`、`PipelineFeedback`、PDK/catalog/builder MCP servers、Clingo gate、可选 Bedrock AR gate、routing retry 和统一 session。`AUTHOR CLAIM` + `CODE VERIFIED`

### 3. 实际做到什么程度？

- PhIDO 论文报告的主要 endpoint 是“有效 schematic + GDS”，不是性能合格或制造签核；测试为 102 prompts、每模型 510 trials，并有人工检查最早失败阶段。`AUTHOR CLAIM`
- 论文承认测试 prompt 曾由 o1 改写并经作者复核，约带来 3% 成功率提升；也承认 attrition bias。`AUTHOR CLAIM`
- Tidy3D/FDTD 只作为 proof-of-concept 支路，未成为主 release 的稳定验证路径；主循环是 SAX compact models。`AUTHOR CLAIM` / `CODE VERIFIED`
- Agentic 源码确实存在 MCP tool decorators、typed models、tool result 回填、路由/验证 retry 和 pause/resume state。`CODE VERIFIED`
- 没有本项目运行证据，Agentic 也没有独立同行评审性能证明。`FACT`

### 4. 关键缺口

- YAML/typed models 仍未证明能覆盖 foundry PDK 约束、器件性能约束、process corners 与 requirement trace 的完整语义；
- Clingo 缺失时和部分 PDK/SAX 能力缺失时会降级，增强验证依赖外部凭据；“门存在”不等于“门始终生效”；
- GDS、generic DRC 和 SAX 不等于 LVS、full-wave correctness、PDK compliance 或 signoff；
- state 仍混合 UI/session 数据，缺少不可变 evidence ledger、事务性 checkpoint/rollback 和统一 failure taxonomy；
- 论文 benchmark 主要测结构生成成功，不能证明性能优化泛化。

### 5. Research Gap → Our Entry Point

`可靠 requirement trace + typed DesignSpec + 不可静默降级的 verification gates` → 在不重建完整 PhIDO 的前提下，研究最小 PIC DesignSpec、gate activation evidence 和 staged validator；对任何跳过/降级都写入 RESULT，而不是默认为通过。`INFERENCE`

## B2. AutoPhotonicDesign

### 1. 解决了什么具体问题？

让 coding agent 在预先搭好的器件仿真目录中反复编辑 geometry/script，执行 DRC 与 Tidy3D/PhotonForge，解析确定性 FoM，并保留或回退设计。目标是器件级真实 simulation-in-the-loop 优化。`FACT` / `CODE VERIFIED`

### 2. 技术路线

`program.md` 规定 agent 只修改特定脚本，按 preview → DRC → simulate → evaluate → journal → keep/discard 流程工作；`simulate.py` 调用 `tidy3d.web.run`；`orchestrate.py` 从日志抽取指标并复制 best design 或回退；不同 Git branch 对应不同器件案例。`CODE VERIFIED`

### 3. 实际做到什么程度？

- 仓库中可确认真实云 solver 调用、仿真参数、metrics 计算、KLayout width/space 检查和 best-design 维护。`CODE VERIFIED`
- 论文报告多个器件、multiphysics 与 routing 案例，但本项目没有复算。`AUTHOR CLAIM`
- 论文明确记录：一个完整 multiphysics modulator 的初始 setup 需要人工专家纠正 port、symmetry 和 mesh，之后 agent 才进入自主闭环。`AUTHOR CLAIM`
- 工具调用是 coding agent 通过文件与 shell 执行，不是 typed Tool Contract；结果主要是文本/TSV/journal，`orchestrate.py` 用正则提取单一数值。`CODE VERIFIED`

### 4. 关键缺口

- 关键问题初始化、材料/边界/mesh 收敛、目标函数设计仍可能依赖专家；
- Tidy3D 云服务与 PhotonForge 带来商业依赖和可复现成本；
- 没有结构化 DesignSpec、统一 RESULT、solver provenance ledger 或跨工具参数语义；
- keep/discard 是窄 metric 比较，failure classification、retry budget、checkpoint 和 rollback 语义不完整；
- DRC 是有限规则检查，不是 foundry deck、LVS 或 signoff；论文人工修正暴露 setup correctness 的核心风险。

### 5. Research Gap → Our Entry Point

`真实 solver loop 已存在，但 setup/RESULT/失败语义不可审计` → 不复制其商业工作流，抽象一个 solver-independent RESULT envelope，强制记录 geometry hash、materials、mesh、boundary、wavelength、tool/version、raw artifact、metric script 与 human intervention。`INFERENCE`

## B3. gdsfactory + gplugins

### 1. 解决了什么具体问题？

提供 PIC 版图、routing、netlist、PDK 与仿真/工艺工具集成的确定性 Python 生态。它解决的是执行工具层，不是自然语言 agent。`FACT`

### 2. 技术路线

gdsfactory 用 Pydantic 模型表达 netlist、schematic、cross-section 和 PDK，并生成/读取 GDS；gplugins 用可选模块连接 SAX、Meep、Tidy3D、Femwell、Lumerical、KLayout、DEVSIM、Palace 等。`CODE VERIFIED`

### 3. 实际做到什么程度？

- YAML netlist 会进入 `Netlist.model_validate`，PDK 与 cross-section 使用 typed models 和 `extra="forbid"`。`CODE VERIFIED`
- Tidy3D adapter 真正调用 `web.run` 并保存 wavelength/S 参数；Meep 等也有独立 S 参数接口。`CODE VERIFIED`
- 部分 plugin 已有 Pydantic result models，但不同 solver 的结果形状仍不统一，部分字段仍是 `Any`/TODO。`CODE VERIFIED`
- 核心仓库 MIT，但可选 backend 包含商业/云工具；“生态开源”不意味着每个 solver 与 PDK 都可自由复现。`FACT`

### 4. 关键缺口

- 没有 Requirement/NL、planner、agent state、retry policy、evidence ledger 或统一 benchmark；
- Python API 不是自动等价于 agent-safe Tool Contract：权限、参数边界、超时、资源预算、幂等性和错误 taxonomy 仍需 wrapper；
- solver 输入/输出 schema 不统一，跨 solver 的 physical semantics 不可直接比较；
- 有 DRC/netlist 工具能力不等于已有统一 PIC LVS/signoff flow。

### 5. Research Gap → Our Entry Point

`成熟 PIC primitives 与 solver adapters 缺少 agent-safe boundary` → 复用 gdsfactory 核心模型与版图能力，对少量核准 backend 做薄 WRAP，建立显式 tool manifest、typed parameters、resource policy、structured error 与 RESULT adapter。`INFERENCE`

## B4. PICBench

### 1. 解决了什么具体问题？

评价 LLM 能否依据 24 个自然语言 PIC 电路题生成可解析、功能响应匹配的 JSON/SAX netlist。它是 Evaluator / Benchmark Layer，不是自动版图系统。`FACT`

### 2. 技术路线

题目包含 NL 描述和 golden netlist/response；`evaluation.py` 解析 JSON，映射模型，调用 `sax.circuit`，在 1.51–1.59 μm 上取 1000 点 transmission，与 golden response 比较；`gen_data.py` 计算 syntax/functional pass@k，并可把错误文本反馈给 LLM。`CODE VERIFIED`

### 3. 实际做到什么程度？

- syntax 的实质是 JSON 可解析、模型/端口能被 SAX 执行；functional 是 response 与 golden 的比较。`CODE VERIFIED`
- `compare_golden` 将响应向量 round 到 10 位再转为 set，因此端口对身份与重复项可能丢失；它并不是带物理容差的波形距离。`CODE VERIFIED`
- pass@k 采用组合估计公式；反馈循环可自动迭代。`CODE VERIFIED`
- 无 GDS、geometry、DRC、LVS、full-wave、PDK signoff 或 process corner。`CODE VERIFIED`

### 4. 关键缺口

- golden response 基于相同 SAX/模型体系，可能奖励“模型内等价”而非真实物理等价；
- set equality 与 10 位 round 的判定不保留端口语义，也没有频谱距离/容差分层；
- 24 题覆盖规模和复杂度有限，不能证明跨 PDK 泛化；
- feedback evaluation 把 evaluator error 直接交给模型，不等同完整 harness recovery；
- 无版图或制造验证层。

### 5. Research Gap → Our Entry Point

`自动 circuit-level evaluator 已有，但物理与版图评价断层` → 借鉴任务/golden/pass@k 组织方式，建立分层 benchmark：schema、connectivity、SAX functional、geometry、DRC、full-wave spot-check；每层独立报告，绝不合并成单一“已验证”标签。`INFERENCE`

## B5. OpenROAD-MCP（机制参照）

### 1. 解决了什么具体问题？

把 OpenROAD/ORFS 的命令、长期 PTY session、报告、metrics 和 flow gates 暴露为 MCP tools，供外部 AI client 调用。`FACT`

### 2. 技术路线

MCP server 与 OpenROAD manager 解耦；tool schema 约束参数；query 与 state-mutating exec 分离；每个 session 对应一个 `openroad -no_init` PTY；wire results 使用 Zod 类型和 nullable error；ORFS 结果可汇总 stage、gate 和日志错误。`CODE VERIFIED`

### 3. 实际做到什么程度？

- 工具、session lifecycle、history、metrics、命令白名单、timeout 和结构化错误均有源码/API 文档。`CODE VERIFIED`
- 这是稳定工具接口，不包含自主 planner，也不替代外部 agent。`CODE VERIFIED`
- 它面向数字电子 physical design；不能把其 RTL-to-GDS、PPA 或 gate 直接当作 PIC 能力。`FACT`
- 架构文档说明 session 可能累计，生产代码没有自动调度清理；长状态仍有资源治理风险。`CODE VERIFIED`

### 4. 关键缺口

- 命令级工具仍允许 agent 发送大量 Tcl，语义粒度可能过低；
- session history 是运行上下文，不是不可变科研 evidence ledger；
- 没有 PIC DesignSpec、PDK/solver semantics 或 verification ladder；
- tool success 仅证明命令执行，不证明设计目标或物理正确。

### 5. Research Gap → Our Entry Point

`成熟 MCP execution/session pattern 与 PIC 语义之间存在空层` → 复用其 query/exec 分权、typed response、session id、history 与 gate summary 思路，但 PIC adapter 应提升为任务级工具，返回统一 RESULT 与验证证据。`INFERENCE`

## B6. MetaChat（机制参照）

### 1. 解决了什么具体问题？

将自然语言 metasurface 目标交给 AIM Design Agent，并通过 materials agent、科学计算工具、FiLM WaveY-Net surrogate 和梯度优化生成 freeform metasurface。对象是 metasurface/nanophotonics，不是 PIC circuit。`FACT`

### 2. 技术路线

AIM 用 HTML-like tags 表达 self-thought、tool、agent 和 user interactions，循环直到 response tag；Design Agent 通过 API 把 lens/deflector 目标映射到 FoM，FiLM WaveY-Net 预测场，Stratton–Chu 得到 far field，自动微分优化 geometry。`AUTHOR CLAIM` / `CODE VERIFIED`

### 3. 实际做到什么程度？

- 论文用 270,000 条 FDFD ground truth 训练 surrogate，并在 30,000 测试集报告误差；这些是作者结果，本项目未复算。`AUTHOR CLAIM`
- benchmark 报告 101 个问题及 AIM/工具/Materials Agent ablation，但它主要测问答、计算与函数调用，不等于制造级设计 benchmark。`AUTHOR CLAIM`
- AIM 源码有 registry、tag parser、20 次 iteration budget 和 tool result 回填。`CODE VERIFIED`
- benchmark 目录的 neural-design API 只返回描述字符串；web backend 才真正启动 Docker/GPU optimization 并生成结果/GDS。两者不能混为同一复现证据。`CODE VERIFIED`
- 仓库根目录未发现许可证文件。代码公开可见，但合法复用状态为 `UNKNOWN`。`FACT`

### 4. 关键缺口

- surrogate 有明确训练域；超出 wavelength/material/topology 范围时的 OOD gate 和 fallback 不充分；
- 论文的 FDFD ground truth/结果展示不表示 agent 每轮调用 conventional full-wave solver；
- tag + `Any` 工具协议不是 typed scientific contract，参数和单位约束弱；
- GDS 导出不伴随 PIC PDK、DRC、LVS 或 signoff；
- 计算资源示例使用 8 GPUs 和 300,000 surrogate simulations，复现成本需单独衡量；
- 许可证缺失阻止直接 REUSE。

### 5. Research Gap → Our Entry Point

`快速 surrogate loop 缺少适用域与证据门` → 研究 surrogate RESULT 的 domain-of-validity、uncertainty/OOD、spot-check full-wave 与 human-escalation 字段；当前项目不直接复用 MetaChat 代码。`INFERENCE`

## 条件对象边界

- **PICopilot**：只可引用论文中多 agent、RAG、脚本任务等作者主张；没有公开实现时，Tool Calling、真实 solver、layout 和 failure recovery 均为 `UNKNOWN`。
- **PICasso**：论文声称 NL→YAML→GDS、PDK、P&R、DRC/LVS 与仿真反馈，但没有公开实现，本轮不得标成 `CODE VERIFIED`，也不据此作源码级 Build/Reuse 决策。
