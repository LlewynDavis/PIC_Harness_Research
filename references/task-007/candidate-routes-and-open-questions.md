# 候选研究路线与待讨论问题

本页给出 TASK-007 基于公开证据形成的 `INFERENCE（推论）`。三条路线均是供导师讨论的研究候选，不是已经确定的方向；本任务不评价课题组资源、不设计实验，也不设定成败阈值。

## Route A｜证据优先的 Agentic PIC Harness 方法研究

**研究问题**  
如何让光子芯片设计 Agent 的需求、设计表示、工具调用、物理结果、验证结论和失败恢复形成可追溯链条，并能清楚区分“模型生成”“工具执行”和“验证通过”？

**已有工作基础**  
PhIDO 提供自然语言到结构化电路、版图与紧凑模型的 proof-of-concept；AutoPhotonicDesign 展示真实求解器在环；gdsfactory/gplugins 提供确定性工具层；PICBench 提供电路生成与自动评价；OpenROAD-MCP 提供专业 EDA 工具的会话、权限和错误机制参照。

**Research Gap**  
现有工作仍缺少跨工具统一证据语义、严格执行边界、分层验证状态和可审计的失败恢复。公开证据也没有证明 typed IR、多 Agent 或自适应工具调用一定优于简单 Python/file contract。

**核心技术方法（候选）**  
采用最小 typed Tool Contract、RESULT/evidence ledger 和 verification ladder，将 Requirement、Spec、Execution、Evidence、Decision 分开；把求解器和规则检查器视为独立证据源，而不是 LLM 的附属文本工具。

**初步系统架构**

```text
Requirement
→ Minimal DesignSpec / direct contract
→ Planner / Harness
→ Typed Tool Adapter
→ Deterministic PIC Tool
→ RESULT + Raw Artifact
→ Independent Evaluator
→ Evidence Ledger
→ Retry / Escalation / Termination
```

**主要技术难点**  
跨求解器输入/输出语义统一、单位和模型适用域、证据版本化、失败分类、评价器独立性，以及避免把工程封装误写成科研创新。

## Route B｜DAS 系统需求到光电混合集成约束的可追溯传播

**研究问题**  
如何将距离、空间分辨率、灵敏度、带宽、偏振与稳定性等 DAS 系统需求，可靠地传播为激光、调制、相干接收、电子、封装与信号处理约束？

**已有工作基础**  
Jin 2024 证明 SOI 收发 PIC 进入真实 DAS；Jin 2026 将窄线宽 InP 外腔激光与 SOI PIC 混合集成为模块；高消光比调制器、通信相干收发复用和微梳并行 DAS 分别提供器件、电路和系统基线。

**Research Gap**  
论文通常优化一个子系统，并使用不同的距离、标距、带宽、噪声统计和外部物料边界；尚无公开证据证明 Agent 已把这些系统目标端到端转为可验证芯片设计。

**核心技术方法（候选）**  
建立带来源、单位、容差和层级的需求—约束图，显式连接器件、光电电路、封装和 DAS 系统模型；任何结论都返回对应模型条件和外部组件边界。

**初步系统架构**

```text
DAS Requirement
→ System Budget
→ Device / Circuit / Package Constraints
→ Domain Models and Tools
→ Layered Evidence
→ Requirement Traceability Report
```

**主要技术难点**  
跨域模型校准、不可比指标、真实 PDK/封装参数、电子和 DSP 的共同影响、长期漂移，以及“流程闭合”与“物理/系统验证”之间的证据跃迁。

## Route C｜光子 AI 的器件误差—任务精度—系统成本联合证据链

**研究问题**  
如何在统一边界下解释光子计算器件误差、校准与数据转换开销怎样传播到模型精度、吞吐、能耗和系统可扩展性？

**已有工作基础**  
MZI/相干网格、MRR/WDM/微梳和衍射/自由空间系统均有芯片或系统演示；Netcast、ACCEL、Taichi、PACE 和通用光子 AI 加速器覆盖不同任务与集成层级。

**Research Gap**  
operation/MAC/FLOP、核心功耗/墙插功耗、模拟精度/任务精度和原型/未来投影口径不统一；跨平台比较常忽略激光、ADC/DAC、控制、温控、存储和数据移动。

**核心技术方法（候选）**  
建立可追溯的 system boundary 与误差—成本图：器件误差和漂移 → 光学算子误差 → 网络层误差 → 任务指标，同时记录全部光电转换、控制和存储开销。

**初步系统架构**

```text
Device / Fabrication / Thermal Error
→ Optical Operator Error
→ Layer and Model Error
→ Task Accuracy
→ Laser + Conversion + Control + Memory Cost
→ Comparable System Record
```

**主要技术难点**  
跨论文数据缺失、私有芯片/编译栈、任务和精度不可比、误差相关性、动态校准，以及避免把文献归一化模型误写成真实硬件测量。

## 三路线关系

| 比较维度 | Route A | Route B | Route C |
|---|---|---|---|
| 主要研究对象 | Agent/Harness 方法 | DAS 跨域设计约束 | 光子 AI 系统证据链 |
| 物理目标 | 通用 PIC 设计流程 | DAS 光电混合集成系统 | AI 推理/优化硬件系统 |
| 可复用基础 | PhIDO、AutoPhotonicDesign、gdsfactory、PICBench | 集成 DAS 前端、调制器、混合集成激光、系统模型 | MZI/MRR/衍射架构、任务级演示、公开数据 |
| 最大证据缺口 | 架构净收益与完整验证闭环 | 系统指标到器件/封装参数映射 | 统一边界下的准确度与总成本 |
| 与其他路线的接口 | 为 B/C 提供可追溯执行与验证框架 | 为 A 提供高价值、跨域物理场景 | 为 A 提供误差/系统评价问题，也可与 DAS 信号处理相连 |

## 当前必须保留的开放问题

1. 面向 PIC 的 DesignSpec 应是新的 typed IR，还是对 Python/netlist/PDK contract 的薄封装？
2. 如何保证 evaluator 与生成器相互独立，避免同一模型既生成又“自证正确”？
3. 哪些失败属于模型推理、工具接口、数值求解、物理不可行或规格冲突？
4. DAS 指标如何在不同距离、标距、带宽、统计定义和外部 BOM 下公平比较？
5. 光子 AI 的 energy/operation、TOPS/W 和任务精度应采用何种共同系统边界？
6. 软件级流程、物理仿真和实物/系统测量分别能支持多强的科研结论？
7. typed IR、RAG、MCP、多 Agent 和自适应工具调用中，哪些是必要机制，哪些只是可替换工程实现？
8. 公开代码和数据是否足以复现关键结论；如果不足，报告应如何表达不可验证部分？

