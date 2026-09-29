# 新增及引用 Figure / Table 来源记录

仓库新增裁图仅来自 PDF 明示 CC BY 4.0 的 PhIDO 与 Cheng。裁图只去掉论文正文和外边缘，保留各子图、坐标轴、单位、图例及原始数据；图题、原文页码和 DOI 在使用处另写，不在位图上改写原始内容。

| 交付图 / 原文定位 | 解释的问题 | 来源与改动 | 许可及限制 |
|---|---|---|---|
| [`figures/phido-fig5-complexity.png`](figures/phido-fig5-complexity.png)；Fig. 5，PDF p.8 | 102 个任务的复杂度分布，以及成功/失败随等级变化 | Sharma et al., 2025, *AI agents for photonic integrated circuit design automation*, Fig. 5, DOI [10.1063/5.0300741](https://doi.org/10.1063/5.0300741)；PDF 裁剪框 `(35,85,560,370)` pt，3×。 | PDF p.1 明示 CC BY 4.0；保留原图内完整图注、颜色图例与柱形。 |
| [`figures/cheng-fig1-device-spectrum.png`](figures/cheng-fig1-device-spectrum.png)；Fig. 1(a–f)，PDF p.2 | 四微环结构怎样对应 transmission spectrum 与脉冲 | Cheng et al., 2023, *On-chip silicon electro-optical modulator with ultra-high extinction ratio for fiber-optic distributed acoustic sensing*, Fig. 1, DOI [10.1038/s41467-023-43244-9](https://doi.org/10.1038/s41467-023-43244-9)；框 `(115,475,485,690)` pt，3×。 | PDF p.9 明示 CC BY 4.0。保留六个子图、谱线图例与坐标；原图题注在报告中引用。 |
| [`figures/cheng-fig2-extinction.png`](figures/cheng-fig2-extinction.png)；Fig. 2(a–f)，PDF p.3 | 静态与 self-heterodyne 动态 ER 的测量方式和差异 | Cheng et al., 2023，Fig. 2，同 DOI；框 `(110,415,485,668)` pt，3×。 | 同上。保留六个子图与完整坐标轴；没有改动曲线和基线。 |
| 既有 `presentations/task-010-group-meeting-rebuild/assets/phido-fig1.png`；Fig. 1，PDF p.3 | PhIDO 四段流程 | Sharma et al., 2025，Fig. 1，同 DOI；现有 PPT P13。 | CC BY 4.0。 |
| 既有 `presentations/task-010-group-meeting-rebuild/assets/picopilot-fig2.png`；Fig. 2，PDF p.3 | Planner、RAG 生成、合成、静态评价 | Jiang et al., 2026, *PICopilot: An LLM-based Agentic Framework for Assisting Photonic Integrated Circuit Design via Script Generation*, Fig. 2, DOI [10.48550/arXiv.2608.01791](https://doi.org/10.48550/arXiv.2608.01791)。 | 既有学术汇报局部裁图；再分发许可未核实。 |
| 既有 `presentations/task-010-group-meeting-rebuild/assets/autopd-fig2.png`；Fig. 2，PDF p.5 | 求解器反馈下的弯曲器件迭代与损耗 | Kharel et al., 2026, *Autonomous agentic design for photonics*, Fig. 2, DOI [10.48550/arXiv.2606.00915](https://doi.org/10.48550/arXiv.2606.00915)。 | 既有学术汇报局部裁图；再分发许可未核实。 |

以下图像**只定位，不在本轮复制到仓库**：Jin 2024 Fig. 1/3/5/6（PDF p.3/5/6/7；Photonics Research PDF 未明示可再分发许可）；Sandmann 2023 Fig. 2/5（PDF p.2/4；本地会议 PDF 含 IEEE/VDE 使用限制）；Ahmed 2025 Fig. 2 与 Table 1（PDF p.3/6；PDF 标注 Springer Nature 独家许可）。其技术关系仅在 PPT 中明确标“根据原文改绘”或在证据表中列原文定位。

Kharel Fig. 1（PDF p.3）可解释 Agent→规则→求解器→验收迭代；在 PPT 中只依据该图和 §2 绘制简化流程，并标明改绘。Fig. 3/4/5/6 及 Table S2/S3 的指标见本包正文，未拼接成虚构同一实验图。
