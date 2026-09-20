# 三方向技术地图

## A｜DAS 光电混合集成

```text
窄线宽光源 / 稳频
→ 高消光比脉冲或扫频调制
→ 传感光纤中的 Rayleigh 回波
→ 双偏振 I/Q 相干接收
→ ADC / DSP / 相位解调
→ 位置、应变与声学事件
```

| 路线 | 代表证据 | 实际达到 | 主要缺口 |
|---|---|---|---|
| SOI 专用收发 interrogator | Jin et al. 2024, `10.1364/PRJ.512298` | `AUTHOR CLAIM`：12.1 km/59 pε/√Hz/1.14 m；49 km/81 pε/√Hz/3.78 m | 激光、放大、环行器、采集/DSP、封装与长期稳定性仍片外或未完整报告 |
| 专用高消光 EOM | Cheng et al. 2023, `10.1038/s41467-023-43244-9` | `AUTHOR CLAIM`：68 dB，接入 2 km DAS 达 4 pε/√Hz | 只替换调制子模块；无频移，不能代表完整 interrogator |
| 通信 coherent PIC 复用 | Sandmann et al. 2023, arXiv:2306.04199 | `AUTHOR CLAIM`：20 km C-OTDR，最高展示 1.75 kHz 声学信号 | 通信器件的高带宽不自动满足 DAS 的低相噪、高 ER 与低漂移 |
| 微梳并行 DAS | Li et al. 2024, `10.1126/sciadv.adf8666` | `AUTHOR CLAIM`：10 路相干累加，560 fε/√Hz@1 kHz、5 m | 双 soliton、泵浦、WDM、探测与 DSP 复杂，系统成本边界不完整 |
| 混合集成激光 + SiN/SOI | Idjadi 2025；Jin 2026 | 已进入 37 km φ-OFDR 与 10 km 混合 interrogator 演示 | 会议级证据较多；异质集成、锁定、热控和封装门槛高 |

`FACT`：已有 PIC 真正进入 DAS 端到端实验。`INFERENCE`：最成熟的公开基线仍是“片上收发核心 + 大量片外光电与 DSP”，不能称全芯片 DAS。

### 系统需求 → 芯片指标

| DAS 需求 | PIC / 电子指标 | 不可省略的系统因素 |
|---|---|---|
| 距离 | 激光频噪/相干长度、耦合和波导损耗、PD/TIA 噪声、LO 功率 | EDFA、环行器、光纤损耗、非线性 |
| 空间分辨率 | 脉冲边沿/宽度或扫频带宽、调制带宽 | 采样、窗函数与解调算法 |
| 应变灵敏度 | ER、RIN、相位噪声、BPD CMRR、ADC ENOB | gauge length、频率、距离和单位口径 |
| 偏振 fading | PBS/PBRS、双偏振 90° hybrid、通道匹配 | 输入 SOP、MIMO/融合算法 |
| 可靠性 | 微环/干涉仪热漂移、bias、laser lock、耦合漂移 | TEC、控制器、重锁与长期现场数据 |
| SWaP / 成本 | 裸片面积与光电功耗 | driver、TEC、封装、FPGA/ADC、外部光学 BOM |

## B｜Photonic AI Computing

```text
MZI / coherent mesh ─┐
MRR / WDM / microcomb├→ 光子线性核 → O/E → 电子非线性、存储、控制
衍射 / slab / free-space┘
```

| 路线 | 代表证据 | 实际达到 | 主要缺口 |
|---|---|---|---|
| MZI / 相干 mesh | Ashtiani 2022；PACE 2025；Ahmed 2025 | 从小规模端到端分类到 64×64 MVM 和真实模型运行 | 相位漂移、O(N²) 调谐、插损、EIC/封装、校准功耗 |
| MRR / WDM / microcomb | Xu 2021；Bai 2023；Netcast 2022 | 高并行卷积、权重库与分布式 MVM | 谐振热漂移、工艺偏差、comb/laser、DAC/ADC 和系统总功耗 |
| 衍射 / 自由空间 / slab | ACCEL 2023；TDONN 2024；Taichi 2024 | 任务级系统、片上可训练衍射和多 chiplet 演示 | 可重构代价、对准、任务专用性、非线性和控制 |
| 光电混合完整系统 | Netcast、ACCEL、PACE、Lightmatter | `FACT`：真实模型/真实任务已经运行 | 没有统一的系统边界、同任务/同精度/同工艺公平基线 |

`FACT`：该方向已越过“只有概念或 MNIST”的阶段。`INFERENCE`：竞争焦点已经从单个光学核扩展到封装、校准、编译、数据移动和真实模型精度，但跨平台系统优势仍未得到统一证明。

## C｜Agentic PIC Design

```text
Requirement
→ minimal DesignSpec / constraints
→ Planner / Harness
→ typed Tool Adapter
→ deterministic PIC tools
→ RESULT + raw artifacts
→ layered Evaluator
→ State / retry / human escalation
```

| 子方向 | 当前基础 | 尚未解决 |
|---|---|---|
| DesignSpec / typed IR | PhIDO DSL、gdsfactory typed netlist、PICBench JSON | 是否优于直接 Python/YAML 尚无因果性实验 |
| Tool / Solver Adapter | gdsfactory/gplugins API、OpenROAD-MCP 模式 | PIC 特定单位、权限、预算、错误分类和证据承诺不统一 |
| RESULT / Evidence Ledger | 多项目各有局部日志/结果 | 统一 envelope 是否改善重放、诊断与复核尚未验证 |
| Adaptive Tool Calling | 有候选假设和对照框架 | uncertainty proxy、决策阈值和正确率—成本关系未知 |
| Verification / Benchmark | PICBench circuit-level；TASK-005 ladder | 缺 geometry/DRC/物理分层、等预算与失败归因 |
| Failure Recovery | 多系统有局部 retry/session | 缺跨工具 failure taxonomy、rollback、termination 与收益实验 |
| 科学方法 → Tool 构建 | Paper2Agent 论文与固定提交源码展示了从可执行研究资产到 typed MCP Tool、参考运行、独立验证和追溯记录的流程 | 未见 PIC/EDA/PDK 公开验证；参考行为一致不等于物理或制造正确；相对手写成熟 API wrapper 的收益未知 |

`FACT`：现有项目各自覆盖局部能力。`INFERENCE`：当前最可证伪的切口是先建立可信评价基座，再检验 typed IR 或 adaptive tool calling，而不是先造完整 Harness。

Paper2Agent 的正式候选记录见[科学计算工具自动构建与验证](/task-006-paper2agent.html)。它位于 Tool Registry/Adapter 的**构建与验证入口**，不改变当前路线排序，也不代表已选择自动工具生成。
