# TASK-004 B/C：Top 5 与第一轮路线判断

## Top 5 架构对比

| 排名 | 对象与入选理由 | 输入 → IR → Tool → 反馈/状态 → 输出 | 自动闭环与人工点 | 可复用边界 |
|---|---|---|---|---|
| 1 | **PhIDO / PhIDO-Agentic 家族**：目前最贴近“PIC 需求到版图”的公开路线，且能观察从线性流水线到有门控状态机的演进 | NL → `DesignIntent`/component intents → DSL/DOT/gdsfactory YAML → KG/PDK MCP、Clingo、gdsfactory、SAX、KLayout → retry/critic/session → GDS | baseline 是阶段式部分闭环；Agentic 代码有拓扑/选择/路由 retry 和人工澄清/知识审核 | 直接复用前必须独立跑通；Bedrock 参数门可降级，完整物理 signoff 和 Agentic 评测仍缺 |
| 2 | **AutoPhotonicDesign**：最明确展示“Agent 真调用 DRC/FDTD、读结果、保留/丢弃并记忆”的光子闭环 | `program.md` → `design.py` 几何 → KLayout/Tidy3D/PhotonForge → plots+metric → TSV/journal → best design | 默认 50 轮无人干预；新器件的目标函数/初始几何由人配置 | 强器件优化 loop，可借鉴实验账本和 deterministic acceptance；不是电路级结构综合，且核心仿真有商业依赖 |
| 3 | **gdsfactory + gplugins**：开源 PIC 工具底座和结构化设计表示最成熟 | Python/YAML/netlist → component/layout → SAX/Meep/Tidy3D/Lumerical/FEM/KLayout 等 → GDS/OAS/报告 | 工具本身不负责 Agent 规划或跨轮决策 | 应作为候选执行层，而非对外宣称 Agent；可承载 PDK、IR、仿真、DRC/LVS 接口 |
| 4 | **MetaChat**：同行评审的光子“语义目标—工具—代理 Maxwell—自动修正”范例，尤其适合研究 human-in-loop 与高速 surrogate | 语义目标 → AIM 多 Agent messages/design variables → optimization APIs + FiLM WaveY-Net → 指标/用户反馈 → freeform layout | 可自主 course-correct，也显式允许用户交互 | 不是 PIC 电路；surrogate 的适用域与全波可信度需单独治理；公开仓库根许可证未核实 |
| 5 | **OpenROAD-MCP**：官方 EDA 工具接口、会话状态与可观测性最清楚，适合映射到 PIC Tool contract | MCP typed calls → OpenROAD session → query/exec → history/metrics/report images → RTL/GDS flow artifacts | MCP server 提供 Tool 与 session，不提供完整 Agent loop | 借鉴 read-only query vs mutating exec、session lifecycle、history/metrics；不能把它当 PIC Agent |

## 与目标闭环的能力映射

| 目标环节 | 现有最佳证据 | 尚缺 |
|---|---|---|
| 需求理解 | PhIDO `DesignIntent`、澄清问题、critic | 可版本化需求契约、单位/约束冲突处理、可追溯假设 |
| 结构化设计描述 | PhIDO DSL/DOT/YAML；gdsfactory YAML/netlist | 稳定 schema、PDK-independent logical IR 与 PDK-bound physical IR 分层 |
| Tool 注册/调用 | PhIDO-Agentic MCP；OpenROAD-MCP；gplugins | PIC 专用 typed error taxonomy、能力发现、权限/资源预算 |
| 仿真/设计 | gdsfactory/gplugins；AutoPhotonicDesign 真 Tidy3D/KLayout | 开源优先的多保真 solver routing、版本/环境锁定、缓存与成本控制 |
| 结果读取 | AutoPhotonicDesign metric/plots/journal；OpenROAD metrics/images | 统一 `RESULT` schema、原始输出不可变存档、单位和置信区间 |
| 判断/迭代 | AutoPhotonicDesign keep/discard；PhIDO retry/gates | 多目标 acceptance、失败分类、回滚、停止准则、重复实验与统计稳定性 |
| 版图/验证 | PhIDO/gdsfactory GDS；KLayout DRC；PICasso 论文声称 LVS | PDK 真实规则、LVS/连通/端口、仿真与版图一致性、tapeout signoff 边界 |

## 三个核心问题

### 1. 是否已有可直接满足最高目标的开源 Photonic Design Agent Harness？

**本轮结论：没有得到足够证据证明“可直接满足”。**

PhIDO-Agentic 的公开架构最接近完整链，AutoPhotonicDesign 的真实 DRC/FDTD 迭代最扎实，
但前者缺少与主张匹配的独立端到端评测和完整 signoff，后者是器件级优化且依赖商业云。
PICasso 在论文中最接近目标描述，但没有核到公开代码；PICopilot 的一手证据重点仍是脚本
生成。故不能把任何一项直接认定为开源、通用、可复现且物理可信的完整 PIC Harness。

### 2. 现有工作分别解决了哪些局部能力？

- PhIDO：需求分解、组件检索、PIC IR、GDS/SAX/DRC 串联；Agentic 分支增加 typed state、
  MCP、形式门控、critic 和 bounded retry。
- AutoPhotonicDesign：真实 solver/DRC 调用、图与指标回读、实验日志、失败学习、自动停止轮数。
- gdsfactory/gplugins：可执行的 PIC cell/netlist/layout/仿真/验证工具底座。
- MetaChat/evo-metaoptics：光子逆设计中的高频反馈、代理求解器、deterministic evaluator 与
  人机协作模式。
- OpenROAD-MCP/MCP4EDA/OpenROAD-Agent：typed Tool、会话隔离、命令执行、PPA/报告读取、
  编译/物理设计反馈纠错。
- FermiLink：package knowledge 与 workflow 分离、HPC 运行、planner/auditor、长周期实验循环。
- LangGraph/AutoGen/MCP SDK：状态、checkpoint、handoff、工具协议；仅是控制面参考。

### 3. 最可能需要自行补齐哪些核心模块？

1. **双层 DesignSpec/IR**：自然语言需求 → 可验证逻辑拓扑 → PDK 绑定版图参数；全程单位、
   来源、假设和版本可追踪。
2. **PIC Tool contract 与 adapter 层**：统一 gdsfactory、KLayout、SAX、开源/商业 EM solver 的
   输入、输出、超时、成本、错误和能力发现。
3. **证据化执行账本**：每次调用保存配置、环境、commit、原始输出、派生指标和不可变关联，
   防止 LLM 摘要替代物理结果。
4. **验证门与多保真策略**：语法/拓扑/端口 → 快速电路模型 → EM → DRC/LVS 的分级门控，
   明确哪些只是 surrogate、哪些是验证器。
5. **有界迭代与失败恢复**：错误分类、重试预算、回滚、停止条件、human approval、失败样本保留。
6. **公平 benchmark**：任务集、隐藏测试、同预算 baseline、重复运行、成功/失败完整披露，分别
   量化结构正确、功能正确、物理指标、版图可制造性、成本和时延。
7. **PDK 与签核治理**：开源演示 PDK 和真实受限 PDK 分离；许可证、数据权限、规则版本和
   “研究 DRC ≠ 代工签核”的边界。

## TASK-005 建议深挖顺序（仅建议，未启动）

1. PhIDO-Release 与 PhIDO-Agentic：逐文件验证控制流、三个 MCP server、retry 和实际 GDS/DRC。
2. AutoPhotonicDesign：复核 `program.md`、`simulate.py`、`orchestrate.py` 与各实验分支原始日志。
3. gdsfactory/gplugins：建立可用开源 vs 商业 adapter、IR 与验证能力矩阵。
4. PICasso：若作者代码发布，优先核验 YAML schema、DRC/LVS、SAX loop 和 PIC-Set。
5. MetaChat / OpenROAD-MCP：分别深挖 evaluator/人机回路与 session/tool contract，不作为 PIC
   系统直接移植。
