# TASK-005 Harness Capability Matrix 与 Verification Ladder

## C. Harness Capability Matrix

缩写：`I` = `IMPLEMENTED`，`P` = `PARTIAL`，`A` = `ABSENT`，`U` = `UNCLEAR`。括号内是决定该等级的一手证据或限制。

| Capability | PhIDO / Agentic | AutoPhotonicDesign | gdsfactory + gplugins | PICBench | OpenROAD-MCP | MetaChat |
|---|---|---|---|---|---|---|
| Spec / IR | `I` YAML/typed DSL | `P` Python/files | `P` typed netlist/PDK，非 requirement spec | `P` JSON SAX netlist | `P` Tcl/flow args，非 PIC IR | `P` API args/tags |
| Knowledge | `P` GraphRAG/PDK catalog，可降级 | `P` setup/script 中固化 | `I` PDK/cross-section models | `A` | `A` | `P` materials DB/agent |
| Planner | `P` staged/deterministic | `I` coding-agent loop | `A` | `A` | `A` external client owns planning | `I` AIM loop |
| Tool | `I` MCP + internal calls | `P` shell/file contract | `P` deterministic Python APIs | `P` evaluator calls SAX | `I` MCP schema/query/exec | `I` tag registry/backend APIs |
| Simulation | `P` SAX；FDTD 非主路径 | `I` Tidy3D/多物理 | `I` many adapters | `P` circuit-level only | `A` PIC simulation | `P` surrogate；FDFD checks |
| RESULT | `P` session fields/plots | `P` text/TSV/journal | `P` backend-specific files/models | `P` strings/log JSON | `I` structured execution results | `P` dict/files/plots |
| Evaluator | `P` structure/DRC/SAX | `I` deterministic FoM | `P` per-plugin | `I` golden SAX response | `P` ORFS gates, non-PIC | `P` FoM + QA benchmark |
| Retry | `P` selected routing/validation retry | `P` iteration/crash + revert | `A` library leaves policy to caller | `P` bounded feedback | `P` client-driven; timeout/errors | `P` 20-turn/tool retry |
| Layout | `I` gdsfactory GDS/routing | `I` geometry/GDS/routing cases | `I` | `A` | `P` electronic layout only | `P` metasurface GDS |
| DRC | `P` generic KLayout rules | `P` limited width/space | `P` KLayout hooks/capability | `A` | `P` electronic domain | `A` no verified DRC path |
| LVS | `A` | `A` | `P` ecosystem primitives, no unified demonstrated gate | `A` | `P` electronic-domain flow only | `A` |
| Signoff | `A` | `A` | `A` public generic ecosystem | `A` | `U` platform-dependent electronic flow; irrelevant to PIC | `A` |
| Benchmark | `P` structural benchmark | `P` case studies | `A` | `I` 24-task evaluator | `P` tool tests/perf, not design benchmark | `I` 101-question adjacent benchmark |

## Q4. 未来 PIC Harness Benchmark 评价层级

| Level | 自动判定对象 | 最小证据 | 能证明 | 不能证明 |
|---|---|---|---|---|
| B0 Protocol | schema、必填字段、单位、版本 | typed validation log | 输出可机器读取 | 电路正确 |
| B1 Syntax | JSON/YAML/Python/netlist 可解析 | parser/compiler result | 语法成立 | connectivity/功能 |
| B2 Connectivity | ports、instances、nets、无悬空/冲突 | graph/netlist checks | 拓扑基本一致 | 光学性能 |
| B3 Circuit Function | SAX/compact-model response 与 golden/constraint 比较 | model versions、sweep、metric | 指定 compact model 下功能匹配 | full-wave、版图寄生 |
| B4 Geometry | GDS 可生成、几何合法、端口对齐、无非法 overlap | geometry report、GDS hash | 几何构造成功 | foundry rule clean |
| B5 DRC | 明确 deck 的 rule checks | deck/version、violations、waivers | 在该规则集下通过 | LVS、PDK signoff |
| B6 Full-wave Spot Check | 固定材料/mesh/boundary/source 的 EM 仿真 | solver input+version、raw field/S params、convergence | 选定条件下数值响应 | process variation、制造 |
| B7 LVS / Connectivity | layout 与 intended netlist 的一致性 | extraction deck、mapping、mismatch report | 特定提取规则下连通一致 | performance/signoff |
| B8 PDK / Corners / Robustness | PDK constraints、corners、Monte Carlo/yield | licensed PDK evidence、corner set、statistics | 条件内鲁棒性 | foundry 接受 |
| B9 Foundry Signoff | foundry-defined tapeout gate | foundry-controlled reports | 对该 foundry 流程达到签核 | fabrication success/yield guarantee |

### Benchmark 计分原则

- 每一层单独报告 pass@k、cost、wall time、tool calls、retry count 和 human interventions；不压成一个“success rate”。
- pass@k 必须同时报告 `n`、`k`、样本预算、反馈轮数、模型版本和随机性设置。
- golden 需区分 exact structure、functional equivalence 和 tolerance-based physical metrics。
- simulator-based evaluator 必须绑定 solver、model library、wavelength grid、materials、mesh、boundary 与 metric script。
- 未运行的高层验证记 `NOT_RUN`，不是 `PASS`，也不以低层通过推断高层通过。

### PICBench 可复用与不可复用部分

- 可复用思想：NL task、golden、自动 evaluator、错误反馈、pass@k。
- 需要修正：端口对身份不能被 set comparison 丢失；波形比较要有显式容差/距离；syntax 与 function 分层；纳入 cost/feedback budget。
- 必须新增：geometry、DRC、full-wave spot-check、LVS/PDK/corner 可选高层。
- 不能声称：PICBench 已证明 fabrication validity、full-wave accuracy、LVS、PDK signoff、process corners 或 robustness。

## Q6. Verification Ladder 到达位置

层级顺序：

```text
Syntax
↓
Geometry Validity
↓
DRC
↓
Circuit-level Simulation
↓
Full-wave Simulation
↓
LVS / Connectivity
↓
PDK Compliance
↓
Process Corner / Robustness
↓
Foundry Signoff
```

| 对象 | 公开证据支持的最高层 | 关键限定 |
|---|---|---|
| PhIDO | Circuit-level Simulation | 有 GDS/generic DRC/SAX；主路径没有稳定 full-wave，论文 endpoint 是结构有效性 |
| PhIDO-Agentic | Circuit-level Simulation | typed gates/MCP 没有把 SAX 升级为 full-wave；可选门会降级 |
| AutoPhotonicDesign | Full-wave Simulation | Tidy3D 真实调用；有限 DRC；缺 LVS、foundry PDK/corners/signoff；部分 setup 经人工纠正 |
| gdsfactory + gplugins | Full-wave Simulation **capability** | 这是工具生态能力，不代表任何 agent 产物已通过该层；具体 backend/配置决定可信度 |
| PICBench | Circuit-level Simulation | 严格说是 compact-model functional evaluation；无 geometry/GDS，因此不是完整顺序通过 |
| OpenROAD-MCP | PIC ladder 不适用 | 电子 EDA 机制参照；不能把电子 flow gate 映射为 PIC signoff |
| MetaChat | Full-wave Simulation 的代理/spot-check 证据 | 优化内环是 surrogate；论文用 FDFD ground truth/结果检查；无 PIC DRC/LVS/PDK signoff |

## 三条禁止性解释

1. `GDS generated` 只表示序列化版图存在，不表示 geometry 合法、DRC clean 或 connectivity 正确。
2. `DRC clean` 只表示在给定 deck 下没有命中规则，不表示 LVS、性能、process corners 或 foundry signoff。
3. `solver called` 只表示执行发生；若没有输入 provenance、收敛与 metric evidence，不能表述为 physical correctness。
