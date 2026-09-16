# TASK-005 Research Gap Matrix、路线种子与对抗性审查

本文件只收敛“值得继续研究的问题”，不选择最终路线，不启动 TASK-006。

## F. Research Gap → Our Entry Point Matrix

| Area | Current State | Research Gap | Existing Evidence | Our Available Conditions | Our Entry Point | Main Risk | Simpler Alternative |
|---|---|---|---|---|---|---|---|
| DesignSpec / typed IR | PhIDO typed DSL；gdsfactory typed netlist/PDK | requirement trace、units、constraints、verification obligations 未统一 | PhIDO models + GF Pydantic | 可从公开 schema 和 circuit task 开始 | 最小 typed PIC spec + trace + validation | 过度设计 DSL | JSON envelope 包现有 GF netlist |
| Agent orchestration | PhIDO staged gates；Auto file loop；MetaChat AIM | 没有兼顾可审计、预算和物理门的通用 PIC harness | 三种互补架构 | 可做单 Agent、确定性状态机研究 | evidence-first bounded harness | scope 膨胀成通用 agent 平台 | 固定 workflow，无自由规划 |
| PDK / RAG | GF PDK models；PhIDO GraphRAG/catalog | PDK truth、文献知识、许可和版本 provenance 混杂 | PhIDO-Agentic + GF | 公开 PDK/文档可用，foundry PDK 未授权 | PDK snapshot + traceable retrieval；RAG 后置 | 把检索文本当规则真值 | 只用 allowlisted structured PDK |
| Tool adapter | gplugins API；OpenROAD-MCP protocol pattern | PIC API 缺统一 schema、权限、timeout、cost、error | gplugins + OpenROAD-MCP | 可 wrap 少量工具 | task-level typed adapter + query/exec split | 封装成本高、语义丢失 | 只 wrap GF + SAX 两工具 |
| Solver integration | Auto 真实 Tidy3D；gplugins 多 backend；MetaChat surrogate | 输入 provenance、收敛、backend 可比性和许可不统一 | source-level adapters/papers | 可先做 circuit solver；full-wave 成本高 | RESULT-bound solver adapter | solver lock-in/成本 | SAX-only baseline + one EM spot-check |
| RESULT / evidence ledger | Auto journal、OpenROAD result、plugin files | 无统一不可变 scientific result envelope | 多项目各有局部结构 | 文档层可先定义最小 schema | RESULT V0 + artifact hashes + evaluator provenance | schema 先行但无实验验证 | JSON envelope + raw directory manifest |
| Optimization loop | Auto/MetaChat 有 keep/gradient；PhIDO 有有限优化 | goal、budget、rollback、multi-objective 与验证门未统一 | Auto orchestrate；MetaChat FoM | 可先限单 metric/bounded retry | evaluator-driven accept/retry | 指标投机与局部最优 | 无优化，仅生成+验证 |
| Layout | gdsfactory 成熟；PhIDO 调用 GF | NL/spec 到可靠 placement/routing、复杂拓扑仍弱 | PhIDO Level4 错误；GF routing | 开源 layout stack 可用 | 复用 GF，研究 failure-aware routing evidence | 难题变成几何算法项目 | 只支持模板化拓扑 |
| Verification | generic DRC/SAX/full-wave 分散 | 层级、gate semantics、LVS/PDK/corners 断裂 | 六对象均未到 PIC signoff | 可做公开规则与仿真层，不能承诺 foundry signoff | 显式 verification ladder + NOT_RUN | “验证”措辞被过度升级 | 三层：syntax/circuit/DRC |
| Failure recovery | selected retry/journal/session 已有 | failure taxonomy、checkpoint、rollback、终止条件不完整 | PhIDO/Auto/MetaChat/OpenROAD | 可用确定性状态机，不需 multi-agent | 最小 failure-aware state machine | recovery policy 本身引入错误 | fail-fast + human escalation |
| Benchmark | PICBench circuit-level；PhIDO structural；MetaChat QA | 缺版图/物理分层、预算公平和可制造性评价 | 24-task PICBench + other case studies | 可先扩评价定义，不必马上建大数据集 | layered benchmark protocol | 数据集构建成本与 leakage | 先审计 5–10 个固定 tasks |

## G. Candidate Routes Seed

### Seed 1：Evidence-grounded PIC Harness

```text
Research Problem
→ 现有闭环难以证明每次工具结果、metric 与决策来自何处
→ Core Method
→ typed RESULT + append-only evidence ledger + deterministic evaluator + bounded state machine
→ Existing Foundation
→ AutoPhotonicDesign journal/keep-discard；OpenROAD structured results；PhIDO staged flow
→ Research Gap
→ 缺统一 solver provenance、failure semantics、human-intervention trace
→ Our Entry Point
→ circuit-first：GF/SAX 一条窄路径，所有结果写 RESULT V0
→ Required Tools
→ gdsfactory、SAX、hash/artifact store、schema validator
→ Main Risk
→ 贡献可能偏系统工程，需用错误检测率/可复现性/恢复质量形成研究问题
```

### Seed 2：Typed PIC DesignSpec 与可验证 requirement trace

```text
Research Problem
→ NL 到网表/版图之间的隐含假设和约束丢失
→ Core Method
→ 最小 typed IR + units + PDK allowlist + verification obligations + bidirectional trace
→ Existing Foundation
→ PhIDO DesignIntent/CircuitDSL；gdsfactory typed netlist/PDK；PICBench task format
→ Research Gap
→ 现有表示没有证明跨 circuit/device、性能和验证层的可靠性
→ Our Entry Point
→ 先限制 circuit topology 与公开 PDK，比较 typed validation 对失败率的影响
→ Required Tools
→ Pydantic/JSON Schema、gdsfactory netlist/PDK、SAX evaluator
→ Main Risk
→ 容易重造 DSL；需与“直接 Python/YAML”基线公平比较
```

### Seed 3：Agent-safe PIC Tool Contract

```text
Research Problem
→ PIC 工具 API 可调用，但不是安全、可审计、可恢复的 agent tools
→ Core Method
→ query/exec 分权、typed params、capability manifest、resource budget、structured errors
→ Existing Foundation
→ OpenROAD-MCP tool/session；gdsfactory/gplugins deterministic APIs；PhIDO-Agentic MCP
→ Research Gap
→ 缺 PIC-specific semantics、RESULT commitment 和 solver/licensing boundary
→ Our Entry Point
→ 只 wrap gdsfactory netlist/layout、SAX 和一个 DRC adapter
→ Required Tools
→ MCP 或等价协议、GF/SAX/KLayout、schema validation
→ Main Risk
→ MCP 本身可能不是科研贡献；价值必须落在错误隔离和可复现评价
```

### Seed 4：Layered PIC Agent Benchmark

```text
Research Problem
→ 现有 benchmark 只测结构或 SAX 功能，无法定位物理与版图失败
→ Core Method
→ syntax/connectivity/circuit/geometry/DRC/full-wave 分层 evaluator 与等预算 pass@k
→ Existing Foundation
→ PICBench tasks/pass@k；PhIDO structural benchmark；gplugins solver adapters
→ Research Gap
→ golden 语义、波形容差、版图/物理任务和预算公平未解决
→ Our Entry Point
→ 修正 PICBench evaluator，并添加小规模 geometry/DRC 层
→ Required Tools
→ SAX、gdsfactory、KLayout；可选 Meep/Tidy3D spot-check
→ Main Risk
→ golden 和任务构建工作量大，且可能被训练数据污染
```

### Seed 5：Failure-aware Simulation-in-the-loop

```text
Research Problem
→ agent 能调用 solver，但错误、数值失败、超时和 setup 缺陷常被混为一次失败
→ Core Method
→ failure taxonomy + checkpoint + retry policy + human escalation + termination budget
→ Existing Foundation
→ Auto keep/discard/crash；MetaChat retry；PhIDO routing gates；OpenROAD session errors
→ Research Gap
→ 没有跨工具的恢复语义，也没有量化 recovery 是否改善结果
→ Our Entry Point
→ 在窄 solver loop 中注入可控失败，比较 fail-fast、blind retry 与 classified recovery
→ Required Tools
→ GF/SAX/一个 EM solver、state machine、failure injection harness
→ Main Risk
→ 工程复杂度和 solver 成本高；TASK-005 仅保留为路线种子
```

## 影响路线判断的关键证据链

### Claim 1：Agentic PIC 正从 script generation 走向 simulation-in-the-loop

- 支持证据：PhIDO 已连接结构生成、SAX 与 DRC；AutoPhotonicDesign 真实调用 Tidy3D 并自动 keep/discard；MetaChat 连接 agent 与 surrogate optimization。`CODE VERIFIED` / `AUTHOR CLAIM`
- strongest counterexample：PhIDO 的论文 endpoint 仍是结构有效性；MetaChat 内环是训练代理且非 PIC；AutoPhotonicDesign 依赖人工修正 setup 和商业基础设施。
- evidence gap：没有统一任务集上对 script-only 与 solver-loop 的公平比较；也没有跨 PDK 泛化或 fabrication 结果。
- hidden assumptions：solver setup 正确、metric 与真实目标一致、计算预算可接受。
- failure modes：错误 mesh/boundary 产生高置信错误结果；agent 优化 metric loophole；只展示成功分支。
- opportunity cost：过早接 full-wave 会挤压 DesignSpec/evaluator 的基础工作。
- simpler alternative：先做 circuit-level deterministic loop，再以少量 EM spot-check 验证。
- 结论：趋势判断可保留为 `INFERENCE`，不能写成已完成的行业事实。

### Claim 2：Typed DesignSpec 是值得研究的核心缺口

- 支持证据：PhIDO-Agentic 主动从 mutable session 转向 Pydantic contracts；gdsfactory 本身依靠 typed netlist/PDK；PICBench 评价依赖固定 JSON netlist。`CODE VERIFIED`
- strongest counterexample：AutoPhotonicDesign 用文件/Python contract 仍能完成高价值器件优化，说明 typed IR 不是所有窄任务的必要条件。
- evidence gap：没有 ablation 证明 typed spec 能显著提高 end-to-end success、减少物理错误或提升跨 PDK 泛化。
- hidden assumptions：IR 能表达足够多物理语义而不僵化；模型能稳定生成该 IR。
- failure modes：schema 合法但物理错误；IR 复杂度高于 Python；规则更新滞后。
- opportunity cost：大量时间花在 schema，而不是 evaluator 和真实工具验证。
- simpler alternative：在现有 gdsfactory netlist 外包一层 requirement/verification envelope。
- 结论：保留为高优先级 seed，但必须设计与 direct Python/YAML 的对照实验。

### Claim 3：统一 RESULT / evidence ledger 是可信 Harness 的中心模块

- 支持证据：Auto 只有文本/TSV/journal；PhIDO 依赖 session；gplugins 结果 backend-specific；OpenROAD 的 structured result 主要是执行级。没有对象同时记录完整 solver inputs、artifacts、metric provenance、human intervention 和 gate ladder。`CODE VERIFIED`
- strongest counterexample：对单一窄任务，NPZ + journal + Git commit 可能已经足够，统一 schema 会增加摩擦。
- evidence gap：尚未通过真实实验量化 RESULT 对重现、故障诊断和错误检测的收益。
- hidden assumptions：所有 solver metadata 可自动获取；artifact storage 成本可控。
- failure modes：字段完整但内容错误；hash 指向不可访问的商业产物；schema 漂移。
- opportunity cost：构建基础设施而缺少新的设计能力。
- simpler alternative：最小 JSON envelope + raw directory manifest，不建复杂数据库。
- 结论：V0 采用最小 envelope，并把科研价值绑定到可复现/诊断指标。

### Claim 4：gdsfactory/gplugins 是最合理的执行底座

- 支持证据：typed PDK/netlist、layout/routing、SAX 与多个 solver adapter，MIT 核心。`CODE VERIFIED`
- strongest counterexample：gplugins 后端异构、部分商业、结果 schema 不统一；成熟 API 不代表 agent-safe tool。
- evidence gap：目标任务、PDK 和 full-wave backend 尚未最终选择，也没有本机兼容性实验。
- hidden assumptions：未来路线仍以 gdsfactory 数据模型为中心；目标 foundry 兼容。
- failure modes：版本锁、commercial credential、solver mismatch、PDK license。
- opportunity cost：过早锁定生态会排除更合适的 device-level stack。
- simpler alternative：先复用 gdsfactory + SAX，不承诺完整 gplugins。
- 结论：layout/netlist 记 `REUSE`，solver adapter 记 `WRAP`，完整生态不作整体采用。

## Strongest counterexamples 汇总

1. **“PhIDO-Agentic 已是完整 PIC Harness”**：源码本身记录 Clingo/AR/PDK 能力可降级，主路径仍止于 GDS/generic DRC/SAX，且缺独立论文级 E2E 证明。
2. **“AutoPhotonicDesign 已提供全开源可复现闭环”**：Tidy3D/PhotonForge/集群依赖明显，论文关键 multiphysics setup 经人工纠正。
3. **“PICBench 已实现物理评价”**：评价代码只调用 SAX compact models；golden 比较还会丢失端口对身份。
4. **“MetaChat 是 PIC full-wave agent”**：对象是 metasurface；优化内环是 surrogate；benchmark 侧 design API 与 web backend 的真实执行路径不同；根许可证未核验。
5. **“GDS + DRC = 验证完成”**：六对象无一公开证明 PIC foundry signoff；多数连 LVS、corners 都未覆盖。

## 当前仍未解决的 5 个最大问题

1. **最小目标域**：先做 circuit-level harness、device-level inverse design，还是二者分层？混合会使 DesignSpec 与 evaluator 失控。
2. **公开且可信的验证上限**：在没有 foundry PDK/LVS/signoff 访问时，哪些层可成为本项目可重复、诚实的最高结论？
3. **DesignSpec 的最小必要性**：typed envelope 能否比直接 gdsfactory YAML/Python 显著降低失败，需要 ablation 而非主观判断。
4. **solver 路线与预算**：SAX + 哪一个开源/可访问 EM solver 能构成公平 baseline，商业 Tidy3D 是否只作可选参照？
5. **研究贡献形式**：Tool wrapper、RESULT schema、failure recovery、benchmark 哪一项能形成可测科学问题，而不是只做工程拼装？
