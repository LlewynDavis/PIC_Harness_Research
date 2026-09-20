# 条件矩阵与路线级对抗性审查

## 当前条件

| 条件 | 状态 | 对路线的影响 |
|---|---|---|
| Python、MATLAB、COMSOL、Lumerical、gdsfactory、PIC 自动化经验 | `USER-PROVIDED / 版本与许可证待核` | 支持三路线的早期建模；不能据此断言商业 solver/模块当前可用 |
| LLM API / 本地模型、稳定调用预算 | `UNKNOWN` | Route 1 的正式对照实验前必须确认 |
| gdsfactory/gplugins、SAX、KLayout 的安装版本 | `UNKNOWN` | Route 1 evaluator 与 Tool baseline 前必须固定 |
| SOI / SiN / LNOI PDK、规则 deck、LVS/signoff | `UNKNOWN` | 决定 Route 2/3 能否越过抽象模型与公开 PDK |
| foundry / MPW / tapeout 经费和时间 | `UNKNOWN` | 未确认前不得把流片写入最小实验承诺 |
| 封装、fiber array、wire bonding、TEC | `UNKNOWN` | DAS 和 Photonic AI 实验的关键瓶颈 |
| DAS：窄线宽激光、EDFA、环行器、AWG/ADC、长光纤、PZT | `UNKNOWN` | 未确认时 Route 2 只做模型与公开数据校准 |
| PAC：高速 DAC/ADC、FPGA、微梳、探测/TIA、光电封装 | `UNKNOWN` | 未确认时 Route 3 只做小型器件—任务联合仿真 |
| GPU/工作站/集群规格 | `UNKNOWN` | 影响 Monte Carlo、全波仿真与 LLM benchmark 规模 |

## 需要导师 / 李师兄确认的优先问题

1. 是否能合法稳定使用 COMSOL、Lumerical 的具体模块和版本？
2. 当前可用的 PDK、版图规则、DRC/LVS 以及是否允许科研发表公开参数？
3. 是否有明确的 MPW/流片窗口、经费、封装与测试合作条件？
4. DAS 台架是否已有窄线宽光源、EDFA、环行器、平衡接收、ADC/AWG、光纤卷和 PZT？
5. Photonic AI 是否有高速 DAC/ADC、FPGA、探测/TIA、温控和封装条件？
6. 可用于 Agent benchmark 的模型/API、预算、数据保密和复现约束是什么？
7. 毕业周期更看重软件方法、系统模型，还是必须包含流片/硬件实验？

## 影响路线选择的关键证据链

### Claim 1｜DAS 已存在 PIC 端到端实验，但不是全芯片系统

- `FACT/AUTHOR CLAIM`：2024 SOI interrogator 包含片上 MZM、偏振处理和双偏振 I/Q receiver，并报告 49 km 结果。
- `FACT/AUTHOR CLAIM`：2023 高 ER EOM 在真实 2 km DAS 中与商业 AOM 对比。
- `COUNTEREVIDENCE`：激光、放大、环行、采集、DSP、封装/控制仍未闭合。
- `INFERENCE`：研究空白不是“让 PIC 第一次进入 DAS”，而是系统约束传播、公平 A/B、稳定性和可制造性。

### Claim 2｜Photonic AI 已有真实系统，但系统优势不可由核心 TOPS/W 推出

- `FACT`：ACCEL、Netcast、PACE、Lightmatter 等已运行真实任务/模型。
- `AUTHOR CLAIM`：论文报告高吞吐、低延迟或高能效。
- `COUNTEREVIDENCE`：部分数字只覆盖接收端光能、核心投影或未来集成估算；ADC/DAC、激光、温控、控制、数据移动边界不统一。
- `INFERENCE`：可研究价值更集中在完整误差与成本链，而不是复制超大系统。

### Claim 3｜Agentic PIC 正在形成局部闭环，但关键架构收益未经对照实验

- `CODE VERIFIED`：TASK-005 已确认 PhIDO、AutoPhotonicDesign、gdsfactory/gplugins、PICBench 等覆盖局部能力。
- `COUNTEREVIDENCE`：没有公开系统同时达到通用、全开源、物理可信、制造级闭环；typed IR、ledger 和 adaptive calling 的净收益均未验证。
- `INFERENCE`：应先建最小测量基座，再检验单一假设。

## Strongest counterexamples

1. **PIC 不必然让 DAS 距离更长。** 非 PIC 放大通信链路已报告 1007 km sensing；PIC 的直接价值更可能是 SWaP、集成和可制造性。
2. **68 dB EOM 不等于 DAS 集成已解决。** 它只替换一个子模块，且某些异频方案仍需要频移器件。
3. **高 TOPS/W 不等于完整系统更优。** 原型总功耗、未来投影、光能/乘法和墙插功耗不可混用。
4. **Photonic AI 不再只会 MNIST。** Lightmatter 等已运行多类真实模型；反过来也不能把少数成功系统泛化为整个领域成熟。
5. **百层映射不等于百层单片物理集成。** 层复用、外部存储与控制仍须计入。
6. **typed DesignSpec 可能没有净收益。** 窄任务用直接 Python/file contract 也能完成；必须做等预算 ablation。
7. **adaptive policy 可能输给固定策略。** 模型自报置信度可能不校准，复杂策略只会增加调用和归因难度。
8. **MCP/Tool wrapper 本身不是科研创新。** 若 typed Python function 已足够，应选择更简单实现。

## 五个最大未决问题

1. 当前真正可用的 PDK、solver、DRC/LVS、模型 API 与预算是什么？
2. Route 1 的 5–10 个任务如何避免只测 schema/evaluator compliance？
3. DAS 跨论文的灵敏度、距离、gauge length、带宽与外部 BOM 能否统一到可校准模型？
4. Photonic AI 如何统一“operation/MAC/FLOP、系统功耗、精度和数据加载”边界？
5. 最终选题需要达到 software-only、simulation-backed 还是 hardware/tapeout 证据层级？

## 机会成本

- 选择 Route 1：可能牺牲器件/硬件新颖性，但最快获得可复现实验和方法论基线。
- 选择 Route 2：应用叙事清晰，但硬件和系统参数缺口可能使研究停留在模型校准。
- 选择 Route 3：文献与工具基础丰富，但竞争激烈，必须用可追溯误差链和公平边界避免增量工作。
