# 图示、论文原图与证据索引

本演示文稿为 20 页主讲，无附录。`outline.json` 保存每页页脚、讲解备注；`build_source.py` 和 `assets/*.svg` 保存可修改的自绘图源。论文原图以裁剪后的 PNG 嵌入 PPTX，保留图号和必要的原图标注。所有作者指标均为论文报告，未由本项目复算。

| 页 | 核心图示及解释目标 | 主要依据与边界 |
| --- | --- | --- |
| P2 | 三方向关系图：区分传感物理系统、推理硬件与智能设计方法 | 项目 `README.md`；TASK-007 正式报告 §1。潜在交叉不表示既定实施阶段。 |
| P3 | 研究证据链：从领域地图到候选路线 | TASK-007 报告与全文证据审计；不是穷尽式系统综述。 |
| P4 | DAS 光路与返回信号：光源/调制/光纤/相干接收/TIA/ADC/DSP，本振支路单独标出 | TASK-007 §2；Jin 等 2024/2026；通用原理简图，不对应单篇实现。 |
| P5 | 分立系统、SOI PIC、混合集成模块的功能边界 | [Jin 等 2024](https://doi.org/10.1364/PRJ.512298)；[Jin 等 2026](https://doi.org/10.1364/OFC.2026.W4D.2)。 |
| P6 | Jin 2026 混合集成模块与外置系统边界 | 根据 [Jin 等（2026）OFC W4D.2](https://doi.org/10.1364/OFC.2026.W4D.2) 和 TASK-007 §2 改绘。原始 PDF 未在当前 Zotero 附件中找到；图不是论文原图。`<3 kHz`、模块尺寸、10 km 演示及其他数字均按作者口径。 |
| P7 | 光电混合推理链：电子输入、光学编码/线性运算、探测、电子后处理 | TASK-007 §3；通用 y=Wx 原理简图。 |
| P8 | MZI、微环/WDM、衍射结构对比 | TASK-007 §3；[Wetzstein 等 2020](https://doi.org/10.1038/s41586-020-2973-6) 等；均为机理简图，不是论文实际版图。 |
| P9 | ACCEL 实际计算链 | [Chen 等（2023）Nature，Fig. 1(b)](https://doi.org/10.1038/s41586-023-06558-8) 原图局部。论文页面为 [PMC10620079](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620079/)，原图来自 Nature 静态图像。只展示 b 子图，保留 OAC、EAC、PD、脉冲及图例；85.5%/82.0%/92.6% 来自论文摘要；系统能效和延迟按论文 operation 与任务边界，不与通用数字 AI 直接比较。 |
| P10 | 1×2 MMI 器件 + 六环节设计流程 | TASK-005 技术地图；TASK-007 Agentic PIC 章节。教学示意，未运行仿真。 |
| P11 | LLM 脚本生成与 Agent 工具循环对比 | PhIDO、PICopilot、AutoPhotonicDesign 原文；不暗示所有 Agent 已有完整自治闭环。 |
| P12 | 需求—Harness—知识/工具—证据—反馈参考架构 | TASK-005 参考架构与 TASK-007 §4 综合改绘；非单篇论文实现。 |
| P13 | PhIDO 自然语言到设计/版图/电路验证 | [Sharma 等（2025）APL Machine Learning，Fig. 1](https://doi.org/10.1063/5.0300741) 原图，Zotero PDF 第 3 页裁剪。结构与 SAX 验证不等于器件性能或代工签核。 |
| P14 | PICopilot 脚本生成框架 | [Jiang 等（2026）arXiv:2608.01791，Fig. 2](https://arxiv.org/abs/2608.01791) 原图，Zotero PDF 第 3 页裁剪。48 项为脚本任务；未核验公开代码或自治工具执行。 |
| P15 | AutoPhotonicDesign 物理求解器迭代结果 | [Kharel 等（2026）arXiv:2606.00915，Fig. 2](https://arxiv.org/abs/2606.00915) 原图，Zotero PDF 第 5 页裁剪。50 是该弯曲器件图中的实验次数；人类设定目标/约束/evaluator。 |
| P16 | 代表工作能力与证据矩阵 | TASK-005 能力矩阵；TASK-007 §4 和原文。`论文` 指文中展示，`作者` 指作者报告，`代码` 仅 PhIDO 固定提交只读核验；`未明确/未核` 不等于领域不存在。 |
| P17 | 三方向比较与候选 A/B/C | TASK-006/007 候选路线总结；均为推论、待讨论，不是选定课题。 |
| P18 | 需求—物理约束—工具—验证的研究问题推导 | P13–P16 所列论文证据与 TASK-007 研究缺口；第二层是待进一步核验的问题，不是“领域普遍没有约束能力”的结论。 |
| P19 | 个人研究倾向与三个未决问题 | 用户在本任务中确认的最新倾向；不是最终技术方案、算法或实验计划。 |

## 论文原图文件与版权记录

| 本地图片 | 来源、裁剪 | 使用条件 |
| --- | --- | --- |
| `assets/accel-fig1b.png` | Chen 等 2023 Nature Fig. 1(b)；从 2079×1108 原图裁出下方 b 子图。 | 原文开放获取声明为 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，已在 P9 标注作者、论文、图号、局部及许可。 |
| `assets/phido-fig1.png` | Sharma 等 2025 PDF 第 3 页 Fig. 1；PDF 坐标 `(66,405,555,650)` pt。 | PDF 第 2 页声明 CC BY 4.0；已在 P13 标注。 |
| `assets/picopilot-fig2.png` | Jiang 等 2026 PDF 第 3 页 Fig. 2；`(88,73,526,281)` pt。 | arXiv 页面仅查到非独占分发许可，未查到 CC 授权；P14 标明学术汇报引用，若公开再发布需确认授权或改绘。 |
| `assets/autopd-fig2.png` | Kharel 等 2026 PDF 第 5 页 Fig. 2；`(84,66,544,616)` pt。 | arXiv 页面仅查到非独占分发许可，未查到 CC 授权；P15 标明学术汇报引用，若公开再发布需确认授权或改绘。 |

Zotero 本地 API 在本次制作时超时；上述三篇 Agentic PIC 论文的已定位 PDF 附件可直接只读访问。未修改 Zotero 条目、标签、Collection 或附件。DAS Jin 2026 与光子 AI ACCEL 未在本地 Zotero PDF 中找到；ACCEL 从官方开放获取论文图取得，Jin 2026 按已核验论文和报告重绘。

## 裁剪与一致性检查

- P13–P15 未使用整页 PDF；保留了原图题号、关键箭头、图例或坐标轴。
- P9 仅保留原 Fig. 1(b)，没有把 Fig. 1(a)/(c) 的内容误称为本次裁图。
- P15 保留横轴 `Experiment`、纵轴弯曲损耗和 `discarded/kept/best so far` 图例。
- 所有 SVG 技术图示均是解释性改绘，不作为实际芯片实验照片或仿真结果。
