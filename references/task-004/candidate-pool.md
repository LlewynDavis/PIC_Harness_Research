# TASK-004 A：候选池

状态：第一轮已核验候选池；不是 L01 最终综述。访问日期均为 2026-09-15。

闭环级别定义：`G` 仅生成脚本/结构；`T` 调用真实工具但不自带迭代控制；`P` 有结果
读取和局部自动迭代；`E` 有公开证据支持接近端到端闭环，但仍不等同于流片签核。每项
只给一个基于现有公开证据的主导档位；论文或项目更高的自我声明另写在证据缺口中。

| # | 候选（类型，年份） | 一手证据与开源核验 | 可执行链与闭环判定 | 证据缺口 / 价值 |
|---|---|---|---|---|
| 1 | **PhIDO / Sharma et al.**（同行评审论文，2025） | [论文](https://doi.org/10.1063/5.0300741)，[arXiv](https://arxiv.org/abs/2508.14123)，[仓库](https://github.com/JPPhotonics/PhIDO-Release)公开、MIT、代码可见 | NL → entity/spec → DSL/DOT/gdsfactory YAML → GDS；SAX 电路仿真；KLayout DRC。单向自动流水线，优化与 DRC 在末端，判 `P` | 102 个描述；论文报告单器件最高 91%，≤15 元件 pass@5 约 57%。没有证明完整 PDK signoff、跨 PDK 泛化或失败后全链重规划 |
| 2 | **PhIDO-Agentic**（后续研究代码/硕士论文材料，2026） | [仓库](https://github.com/JPPhotonics/PhIDO-Agentic)公开、MIT、源码可见；[数据 DOI](https://doi.org/10.5683/SP4/T5QU9C) | 代码可见 `DesignIntent`、KG/PDK MCP tools、Clingo 拓扑门、critic、选择验证、路由 retry、gdsfactory export；按当前已验证证据判 `P` | 项目架构自称接近 `E`，但极新、外部采用近乎为空且自证成分高。参数门依赖 AWS Bedrock 且可降级；未见与论文同等级的端到端独立评测 |
| 3 | **PICopilot**（预印本，2026） | [arXiv:2608.01791](https://arxiv.org/abs/2608.01791)；未核到作者公开仓库或许可证 | 多 Agent + feedback + RAG，目标是从 NL 生成 PIC 设计脚本；从现有一手证据只能判 `G`，不能认定真实仿真闭环 | 48 个脚本任务均完成、比 GPT-5+通用 RAG 多 21 个是作者报告；缺代码、执行轨迹、版图/仿真闭环证据 |
| 4 | **PICasso**（预印本，2026） | [arXiv:2608.26113](https://arxiv.org/abs/2608.26113)；未核到公开仓库或许可证 | 声称 NL → YAML → GDS、PDK 注入、P&R、DRC/LVS、SAX 与仿真反馈优化，论文层面判 `E`，可复现层面未证 | 36 任务；结构 Spec@3 最高 92.7%，复杂任务功能 Spec@3 最高 52%；无代码使关键 Tool/循环/隐藏人工步骤无法核验 |
| 5 | **AutoPhotonicDesign**（预印本+项目，2026） | [论文](https://arxiv.org/abs/2606.00915)，[仓库](https://github.com/flexcompute/autophotonicdesign)公开、MIT、分支实验记录可见 | `program.md` → 修改 `design.py` → preview/KLayout DRC → Tidy3D FDTD → 读取图场/指标 → keep/discard → journal，固定 50 次，判 `E`（器件级） | 真 Tool、真结果回读、失败记忆最强；但 Tidy3D 为付费云，routing 另依赖 PhotonForge；目标指标/evaluate 仍需人为为新器件配置 |
| 6 | **PICBench**（预印本+benchmark，2025） | [论文](https://arxiv.org/abs/2502.03159)，[仓库](https://github.com/PICDA/PICBench)公开、MIT、测试用例可见 | 对 LLM 生成 PIC netlist 做语法和功能自动评价，判“评测器”，不是 Agent | 可为未来 benchmark / evaluator 提供基线；不覆盖自动工具编排、状态或版图签核 |
| 7 | **gdsfactory + gplugins**（开源项目生态，持续） | [gdsfactory](https://github.com/gdsfactory/gdsfactory)与[gplugins](https://github.com/gdsfactory/gplugins)均公开、MIT、源码/测试可见 | Python/YAML → cell/netlist/layout → GDS/OAS；插件连接 SAX、Meep、Tidy3D、Lumerical、FEM、KLayout 等。判 `T`，本身非 Agent | 最成熟的 PIC 可执行底座；Harness 仍需补 DesignSpec、策略、状态、迭代、故障和证据层 |
| 8 | **MetaChat**（同行评审论文+项目，2025） | [Science Advances](https://doi.org/10.1126/sciadv.adx8006)，[仓库](https://github.com/jonfanlab/metachat)源码/数据路径可见；GitHub 未识别根许可证，故不标“已核实开源” | 语义目标 → AIM 多 Agent/人机交互 → 优化 APIs → FiLM WaveY-Net Maxwell surrogate → 自主修正 → 自由形状版图，判 `E`（超表面） | 闭环强但不是 PIC 电路；核心物理反馈是代理模型而非每轮全波求解。许可证缺口影响直接复用 |
| 9 | **evo-metaoptics**（同行评审论文+项目，2026） | [论文](https://doi.org/10.1002/lpor.71739)，[仓库](https://github.com/yi-huang-1/evo-metaoptics)公开、MIT、核心 runtime/evaluator 可见 | coding agent 写 inverse-design 函数 → TorchRDIT 执行 → deterministic evaluator → 自演化，按公开范围判 `P`（超表面） | 不是 PIC；公开范围明确不含完整论文实验套件和报告生成，不能声称完全复现论文 |
| 10 | **FermiLink**（预印本+项目，2026） | [论文](https://arxiv.org/abs/2604.03460)，[仓库](https://github.com/TaoELi/FermiLink)公开、AGPL-3.0 | 目标 → package KB/skill → planner/task loop → 本地或 HPC 真仿真 → auditor/记忆，判 `E`（通用科学仿真） | 132 个图复现中 74 个得到图，30 个高保真、35 个定性一致；说明自动执行不等于科研正确。未提供 PIC 专用 IR/PDK/signoff |
| 11 | **MCP4EDA**（预印本+项目，2025） | [论文](https://arxiv.org/abs/2507.19570)，[仓库](https://github.com/NellyW8/MCP4EDA)源码可见但 GitHub 未识别根许可证，不能称已核实开源 | MCP 暴露 Yosys/Icarus/OpenLane/KLayout/报告读取，可产 GDS；服务器自身判 `T`，自主循环主要在外部 MCP client | 真工具桥接很有参考价值，但服务器本身不是完整 planner/state machine；论文改进指标需独立复现 |
| 12 | **OpenROAD-MCP**（官方开源项目，2026） | [仓库](https://github.com/The-OpenROAD-Project/OpenROAD-MCP)公开、BSD-3-Clause、API/测试可见 | MCP 提供 session、query/exec、history、metrics、report image；底层 OpenROAD/ORFS 可 RTL→GDS，判 `T` | 强工具契约、会话和可观测性参考；没有 PIC 语义，也不自带目标判断/迭代策略 |
| 13 | **OpenROAD-Agent**（论文伴随项目，2025） | [仓库](https://github.com/OpenROAD-Assistant/OpenROAD-Agent)公开、BSD-3-Clause，代码、数据和模型权重路径可见 | LLM 在 OpenROAD 中生成并执行 Python，读错误反馈并修正，判 `P` | 报告脚本任务准确率 94%；主要证明脚本交互/纠错，不是完整 RTL→GDS 自主设计或 PIC Harness |
| 14 | **ChatEDA**（同行评审论文伴随项目，2024） | [仓库](https://github.com/wuhy68/ChatEDA)公开、Apache-2.0；论文信息见仓库 | LLM 以 EDA API/任务分解驱动工具，按公开材料可证范围判 `P` | 仓库体量和可运行入口需进一步核查；不要把论文“autonomous”直接等同全闭环 |
| 15 | **RTLFixer**（预印本+项目，2023） | [论文](https://arxiv.org/abs/2311.16543)，[仓库](https://github.com/NVlabs/RTLFixer)公开、MIT | RAG/ReAct → 编译器真实反馈 → 修复 Verilog，判 `P`（局部编译闭环） | 212 个错误样本约 98.5% 修复是窄任务结果；不涉及物理设计和 GDS |
| 16 | **salitronic/eda-agent**（实验性开源项目，2026） | [仓库](https://github.com/salitronic/eda-agent)公开、Apache-2.0、源码可见 | MCP 连接活动 Altium/KiCad/EasyEDA 会话，含 SPICE、设计审查、批量变更；按服务器本身判 `T` | 真实 CAD 接口值得参考；非光子，Altium 后端专有，项目自报能力尚缺论文级评估 |
| 17 | **eda-agents**（实验性开源项目，2026） | [仓库](https://github.com/Mauricio-xx/eda-agents)公开、Apache-2.0、源码可见 | Pydantic 结构 + ngspice/LibreLane/KLayout/OpenROAD 等仿真/物理流程，判 `P`（按代码/README） | 外部验证和采用极少；提交的 benchmark/证据仍是项目自证材料 |
| 18 | **LangGraph**（通用编排项目） | [仓库](https://github.com/langchain-ai/langgraph)公开、MIT | 状态图、checkpoint、interrupt/retry，判 Harness 控制平面参考 | 不是 EDA/PIC，不提供物理工具、DesignSpec 或设计正确性 |
| 19 | **AutoGen**（通用多 Agent 项目） | [仓库](https://github.com/microsoft/autogen)公开；根 `LICENSE` 为 CC-BY-4.0，代码另由 [`LICENSE-CODE`](https://github.com/microsoft/autogen/blob/main/LICENSE-CODE) 明确采用 MIT | 多 Agent 会话与 Tool 调用参考 | 不是 PIC 系统；“多 Agent”本身不增加物理可信度或闭环完整性 |
| 20 | **Model Context Protocol Python SDK**（通用 Tool 协议） | [仓库](https://github.com/modelcontextprotocol/python-sdk)公开、MIT | typed tool/resource/prompt transport，判接口层 | 只解决协议和发现，不解决 planner、状态、恢复、验证或设计策略 |

## 池内分类结论

- 真正直接面向 PIC 电路：1–7；其中 3、4 暂无已核实公开实现，6 是 benchmark，7 是工具底座。
- 相邻光子器件闭环：8–9；物理对象是 metasurface，不可与 PIC 电路等同。
- 真仿真/EDA Harness 类比：10–17；解决工具连接、会话、反馈或局部闭环。
- 通用控制面参考：18–20；不得计为 PIC 自动设计候选。
