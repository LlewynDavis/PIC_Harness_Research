# TASK-016 新增证据日志

本日志把本轮新增的报告判断连接到原文 Figure/Table/Section。`FACT` 表示可在论文或附件中直接核对的结构与任务设置；论文性能结果保留 `AUTHOR CLAIM`，不代表本项目独立复现。逐项数值、单位和条件见 [`key-data.csv`](key-data.csv)；PDF 版本与哈希见 [`source-manifest.md`](source-manifest.md)。

| ID | 报告中使用的判断 | 原文证据及定位 | 等级与边界 |
|---|---|---|---|
| T016-A1 | PhIDO 把自然语言要求转为结构化 PIC 设计与版图，102 prompt 覆盖四个复杂度等级。 | Sharma et al., 2025, Fig. 1/5、Table II、§III.A/IV.A；PDF p.3/6/8–9；DOI 10.1063/5.0300741。 | `FACT`：流程与 benchmark 定义；`AUTHOR CLAIM`：成功率。`S` 是有效 schematic/GDSII，非目标光学性能。 |
| T016-A2 | PICopilot 的 Agent 内部评价主要是静态代码/自定义检查；48 任务 benchmark 在外部执行脚本并比对输出。 | Jiang et al., 2026, Fig. 2、§3.6/4.1.4、Table 2/3；PDF p.3/6–7；DOI 10.48550/arXiv.2608.01791。 | `FACT`：两层评价方法；`AUTHOR CLAIM`：48/48 与 pass@k。外部执行不代表内部数值仿真闭环。 |
| T016-A3 | Kharel 的 Agent 在工程师给定目标、规则、求解器与验收函数下迭代；多物理初始设置错误曾由工程师修正。 | Kharel et al., 2026, Fig. 1–6、Table S2/S3、§2/S6；PDF p.3–10/19–20；DOI 10.48550/arXiv.2606.00915。 | `FACT`：论文公开的流程与反例；`AUTHOR CLAIM`：仿真改进数值；`INFERENCE`：不能据此证明独立建立正确物理模型。无实物流片验证。 |
| T016-D1 | Jin 2024 的 SOI PIC 集成收发与探测光路，但 DAS 链路仍依赖片外激光、EDFA、环行器、采集与 DSP。 | Jin et al., 2024, Fig. 1(b)/3/5/6、§4.B/5；PDF p.3/5–8；DOI 10.1364/PRJ.512298。 | `FACT`：功能与系统拓扑；`AUTHOR CLAIM`：12.1/49.0 km 下的分辨率与噪声。两组条件不同，原始波形未公开。 |
| T016-D2 | Cheng 四微环器件改善 DAS 发射脉冲，器件指标与 2 km Φ-OTDR 结果需分开陈述。 | Cheng et al., 2023, Fig. 1/2/4/5、Discussion；PDF p.2–6；DOI 10.1038/s41467-023-43244-9。 | `FACT`：器件/台架结构；`AUTHOR CLAIM`：ER、功耗、边沿与噪声。3.60 mW 仅为 EOM，不是全系统功耗。 |
| T016-D3 | Sandmann 将通信相干收发模块复用于 CC-OTDR，20 km 后检测到 200 Hz 扰动。 | Sandmann et al., 2023, Fig. 2/5、§III；PDF p.2–4；DOI 10.48550/arXiv.2306.04199。 | `AUTHOR CLAIM`：相位响应。会议短文未给与 Jin 同口径的检测限/空间分辨率。 |
| T016-P1 | Ahmed 光电张量核只承担计算链中的矩阵向量运算；任务准确率与电子控制、存储、转换和能耗必须一起看。 | Ahmed et al., 2025, Fig. 1/2、Table 1、Methods；PDF p.1–3/6/8；DOI 10.1038/s41586-025-08854-x。 | `FACT`：系统模块与任务口径；`AUTHOR CLAIM`：ops、功耗和准确率；`UNKNOWN`：统一墙插功耗与各任务 energy/inference。 |
| T016-S1 | 三篇 Agentic PIC 论文的输入、Agent 反馈与成功定义不同，不能直接按成功率排序。 | Sharma Table II/§IV.A；Jiang §3.6/4.1.4；Kharel Fig. 1/Table S2/§S6；对应 PDF 定位见 A1–A3。 | `INFERENCE`：跨论文比较。见 [`agentic-pic-comparison.md`](agentic-pic-comparison.md)。 |

图像可再分发范围、裁剪框与图号见 [`figure-sources.md`](figure-sources.md)。未核实问题集中在 [`README.md` 的 UNKNOWN 节](README.md#未解决与-unknown)。
