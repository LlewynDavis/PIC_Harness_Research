# 图示、论文原图与证据索引

本演示文稿为 20 页主讲，无附录。`outline.json` 保存每页页脚、讲解备注；`build_source.py` 和 `assets/*.svg` 保存可修改的自绘图源。论文原图以裁剪后的 PNG 嵌入 PPTX，保留图号和必要的原图标注。所有作者指标均为论文报告，未由本项目复算。

| 页 | 核心图示及解释目标 | 主要依据与边界 |
| --- | --- | --- |
| P2 | 三方向关系图：区分传感物理系统、推理硬件与智能设计方法 | 项目 `README.md`；TASK-007 正式报告 §1。潜在交叉不表示既定实施阶段。 |
| P3 | 研究证据链：从领域地图到候选路线 | TASK-007 报告与全文证据审计；不是穷尽式系统综述。 |
| P4 | DAS 光路与返回信号：光源/调制/光纤/相干接收/TIA/ADC/DSP，本振支路单独标出 | TASK-007 §2；Jin 等 2024/2026；通用原理简图，不对应单篇实现。 |
| P5 | Jin 2024 片上功能与片外依赖清单；同页列两组带条件系统指标 | 根据 [Jin 等（2024）Fig. 1(b)/3/5/6](https://doi.org/10.1364/PRJ.512298) 改绘；不是论文原图。12.1 km/49.0 km 的 gauge length 与重复率分别在备注和[数据表](../../references/task-016-evidence/key-data.csv)。Sandmann 2023 Fig. 2/5 的 20 km、200 Hz 复用路线在备注说明。 |
| P6 | Cheng 2023 原始 Fig. 1：四微环、PIN、透射谱与脉冲；旁列器件和 DAS 边界 | [Cheng 等（2023）Fig. 1](https://doi.org/10.1038/s41467-023-43244-9) 原图局部；动态 ER、功耗和 2 km DAS 分别据 Fig. 2/4/5。CC BY 4.0。 |
| P7 | 光电混合推理链：电子输入、光学编码/线性运算、探测、电子后处理 | TASK-007 §3；通用 y=Wx 原理简图。 |
| P8 | MZI、微环/WDM、衍射结构对比 | TASK-007 §3；[Wetzstein 等 2020](https://doi.org/10.1038/s41586-020-2973-6) 等；均为机理简图，不是论文实际版图。 |
| P9 | Ahmed 2025 host/DCI/PTC/电子输出链，区分光电混合算子与任务级准确率 | 根据 [Ahmed 等（2025）Fig. 1/2 与 Table 1](https://doi.org/10.1038/s41586-025-08854-x) 改绘；非论文原图。65.5×10¹² ops/s 为论文 operation 口径；CIFAR-10 与 SQuAD 结果不能并成单一精度。原图为 Nature 独家许可，未新增复制。 |
| P10 | 1×2 MMI 器件 + 六环节设计流程 | TASK-005 技术地图；TASK-007 Agentic PIC 章节。教学示意，未运行仿真。 |
| P11 | 脚本生成与物理求解器在环对比 | [PICopilot §3.6/§4.1.4](https://doi.org/10.48550/arXiv.2608.01791) 区分内部静态反馈和外部 benchmark 执行；[Kharel Fig. 1/§2](https://doi.org/10.48550/arXiv.2606.00915) 支持右侧真实求解器循环。 |
| P12 | 需求—Harness—知识/工具—证据—反馈参考架构 | TASK-005 参考架构与 TASK-007 §4 综合改绘；非单篇论文实现。 |
| P13 | PhIDO 自然语言到设计/版图/电路验证 | [Sharma 等（2025）Fig. 1](https://doi.org/10.1063/5.0300741) 原图，Zotero PDF p.3。102 个 prompt 和复杂度结果据 Fig. 5、Table II，PDF p.8/9；`S` 是有效 schematic/GDSII，不是性能资格。 |
| P14 | PICopilot 脚本生成框架与两种反馈口径 | [Jiang 等（2026）Fig. 2](https://doi.org/10.48550/arXiv.2608.01791) 原图，Zotero PDF p.3；内部静态评价 §3.6 p.6，外部 benchmark Table 2/3 p.7。 |
| P15 | Kharel 弯曲器件求解器迭代及多物理反例 | [Kharel 等（2026）Fig. 2](https://doi.org/10.48550/arXiv.2606.00915) 原图，Zotero PDF p.5；0.109 dB 对 0.460 dB 的条件见 §S2；多物理初设问题见 Table S2 p.20。 |
| P16 | PhIDO/PICopilot/Kharel 的输入、反馈、判据及物理约束矩阵 | 三篇原文位置见[八列比较表](../../references/task-016-evidence/agentic-pic-comparison.md)；是跨论文统一对照，不是单篇论文 Figure。 |
| P17 | 三方向比较与候选 A/B/C | TASK-006/007 候选路线总结；均为推论、待讨论，不是选定课题。 |
| P18 | 需求—物理约束—工具—验证的研究问题推导 | P13–P16 所列论文证据与 TASK-007 研究缺口；第二层是待进一步核验的问题，不是“领域普遍没有约束能力”的结论。 |
| P19 | 个人研究倾向与三个未决问题 | 用户在本任务中确认的最新倾向；不是最终技术方案、算法或实验计划。 |

## 论文原图文件与版权记录

| 本地图片 | 来源、裁剪 | 使用条件 |
| --- | --- | --- |
| `assets/cheng-fig1-device-spectrum.png` | Cheng 等 2023 Nature Communications Fig. 1(a–f)；从 Zotero PDF p.2 裁出图框，未改动曲线、坐标轴和图例；详细裁剪坐标见[来源记录](../../references/task-016-evidence/figure-sources.md)。 | 原文 PDF p.9 明示 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)；P6 已标作者、题名、图号与 DOI。 |
| `assets/phido-fig1.png` | Sharma 等 2025 PDF 第 3 页 Fig. 1；PDF 坐标 `(66,405,555,650)` pt。 | PDF 第 2 页声明 CC BY 4.0；已在 P13 标注。 |
| `assets/picopilot-fig2.png` | Jiang 等 2026 PDF 第 3 页 Fig. 2；`(88,73,526,281)` pt。 | arXiv 页面仅查到非独占分发许可，未查到 CC 授权；P14 标明学术汇报引用，若公开再发布需确认授权或改绘。 |
| `assets/autopd-fig2.png` | Kharel 等 2026 PDF 第 5 页 Fig. 2；`(84,66,544,616)` pt。 | arXiv 页面仅查到非独占分发许可，未查到 CC 授权；P15 标明学术汇报引用，若公开再发布需确认授权或改绘。 |

TASK-016 时 Zotero 本地 API 与 Connector 均可用；上述七篇代表工作均已定位本地 PDF，key、页数与 SHA-256 见[核读清单](../../references/task-016-evidence/source-manifest.md)。未修改 Zotero 条目、标签、Collection 或附件。旧 `assets/accel-fig1b.png`、`assets/p06-jin-module.svg` 是 TASK-010 历史构建资源，现行 P6/P9 不引用；原文件保留供追溯。

## 裁剪与一致性检查

- P13–P15 未使用整页 PDF；保留了原图题号、关键箭头、图例或坐标轴。
- P6 Cheng Fig. 1 保留结构、谱图、脉冲各子图及坐标图例；P9 为 Ahmed Fig. 2 改绘，未把自绘图标作论文原图。
- P15 保留横轴 `Experiment`、纵轴弯曲损耗和 `discarded/kept/best so far` 图例。
- 所有 SVG 技术图示均是解释性改绘，不作为实际芯片实验照片或仿真结果。
