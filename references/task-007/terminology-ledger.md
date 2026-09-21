# TASK-007 术语表

| 中文统一表述 | 英文 / 缩写 | 本报告使用边界 |
|---|---|---|
| 分布式声学传感 | Distributed Acoustic Sensing, DAS | 指利用光纤分布式感知动态应变/振动；不把 FBG 点式/准分布式解调器称为 DAS。 |
| 光子集成电路 | Photonic Integrated Circuit, PIC | 指在芯片上集成多个光子器件与互连。 |
| 光电混合集成 | Photonic–electronic / heterogeneous integration | 必须说明光源、PIC、电子、封装和算法哪些片内、模块内或片外。 |
| 面向智能体的 PIC 设计 | Agentic PIC Design | 强调规划、工具执行、结果读取、评价与迭代；仅生成代码不自动归入完整闭环。 |
| 智能体执行框架 | Agent Harness | 组织模型、状态、工具、证据、权限、重试和终止条件的执行层。 |
| 设计规格 / 类型化中间表示 | DesignSpec / typed IR | 将需求、单位、约束、接口和来源结构化；其净收益仍是待验证假设。 |
| 工具契约 | Tool Contract | 明确输入 schema、单位、参数验证、输出、异常和执行边界的调用接口。 |
| 仿真在环 | Simulation-in-the-loop | 仿真结果进入评价并驱动下一轮设计；单次运行 solver 不算闭环。 |
| 结构化结果 | RESULT | 同时保存输入、环境、原始产物、指标、验证状态和失败信息的结果记录。 |
| 证据账本 | Evidence Ledger | 将需求、工具调用、结果、判断、失败和版本串联的可追溯记录。 |
| 设计规则检查 | Design Rule Check, DRC | 检查几何规则；不等同于连接正确、物理性能或 foundry signoff。 |
| 版图与原理图一致性 | Layout Versus Schematic, LVS | 检查版图提取连接与原理图/网表一致；不等同于物理性能验证。 |
| 工艺设计套件 | Process Design Kit, PDK | 工艺规则、器件模型、版图单元和验证资源的集合；“通用 PDK”不等于 foundry PDK。 |
| 全波仿真 | Full-wave simulation | 例如 FDTD/FEM；必须记录材料、网格、边界、波长、版本和收敛信息。 |
| 紧凑模型 / 电路级仿真 | Compact-model / circuit-level simulation | 以器件 S 参数或解析模型组成电路；不能替代器件全波或制造验证。 |
| 马赫–曾德尔干涉仪 | Mach–Zehnder Interferometer, MZI | 光子矩阵计算常用干涉单元，也可用于调制。 |
| 微环谐振器 | Microring Resonator, MRR | 可用于权重、滤波和调制；对工艺误差与温度敏感。 |
| 波分复用 | Wavelength-Division Multiplexing, WDM | 以多个波长并行承载计算或传感通道。 |
| 光学神经网络 | Optical / photonic neural network | 报告时必须说明非线性、存储、控制和数据转换是否电子完成。 |
| 推理演示 | inference demonstration | 只有运行真实任务/模型才称任务级演示；核心算子测试不等于完整推理系统。 |
| 芯片实验 | chip experiment | 有实物芯片测量；与数值仿真、封装模块实验和完整系统实验分开。 |
| 系统级能效 | system-level energy efficiency | 应纳入激光、ADC/DAC、驱动、控制、温控和数据移动；核心 TOPS/W 不自动等同系统能效。 |

