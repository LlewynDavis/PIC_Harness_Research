# TASK-008 主讲图示来源与解释目标

本表对应 `outline.json` 的 14 页主讲版。概念图来自已验收调研材料，是研究综合示意，不能读作某篇论文的原始器件结构或本项目实测结果。原论文图片单独标出 Fig. 编号和裁剪范围。未使用装饰性图片。

| 页 | 图示 | 要解释的问题 | 来源与边界 |
| --- | --- | --- | --- |
| 2 | 三目标关系图 | DAS 物理场景、光子 AI 硬件和 Agentic PIC 方法如何联系 | `references/task-007/formal-research-report.md` §1.1；概念重绘，联系为候选研究框架。 |
| 3 | 证据标签流图 | 原文、作者报告、调研推论和未知如何影响可说的结论 | 正式报告 §1.2、`full-text-evidence-audit.md`；概念重绘。 |
| 4 | DAS 系统链路图 | 光源、调制、传感光纤、相干接收、电子与算法怎样共同决定指标 | 正式报告 §2.1；通用系统概念图，非单片集成结构。 |
| 5 | DAS 集成边界图 | Jin 2024 PIC 与 Jin 2026 混合模块分别把哪些环节纳入芯片/模块 | Jin 等（2024），doi:10.1364/PRJ.512298；Jin 等（2026），doi:10.1364/OFC.2026.W4D.2；据正式报告 §2.2–2.3 重绘，距离均为作者报告。两篇 PDF 未在当前 Zotero 附件目录找到。 |
| 6 | 光子 AI 完整推理链路图 | 光域线性运算与电子输入、探测、控制和数据移动的边界 | 正式报告 §3.1–3.5；通用概念重绘。 |
| 7 | 三类计算架构对比图 | MZI、MRR/WDM 与衍射/芯粒架构的计算机制和限制 | 正式报告 §3.2–3.4；架构家族示意，图中代表工作并非同一器件结构。相关目标论文 PDF 未在当前 Zotero 附件目录找到。 |
| 8 | AutoPhotonicDesign 原图 | 人工目标如何进入 Agent 的设计、DRC、仿真与保留/丢弃循环 | Kharel 等（2026），*Autonomous agentic design for photonics*，arXiv:2606.00915，PDF 第 3 页 Fig. 1(b)。从本地 Zotero 附件 `NP249BAB` 裁剪 `(297,315,548,475)` pt，仅截取 (b) 面板；无重排或改标。表示该论文流程。 |
| 9 | PhIDO 原图 | Interpreter、Designer、Layout、Circuit Verification 如何衔接 | Sharma 等（2025），*APL Machine Learning* 4, 046113，doi:10.1063/5.0300741，PDF 第 3 页 Fig. 1。从本地 Zotero 附件 `KGSYYKEY` 裁剪 `(70,408,550,647)` pt；无重排或改标。图中的 FDTD 分支不能视为主发布已验证。 |
| 10 | 代表工作能力矩阵 | PhIDO、AutoPhotonicDesign、PICBench 与 gdsfactory 分别覆盖哪些设计环节 | 正式报告 §4.2–4.4、`references/task-005/technical-map-and-objects.md`；跨工作概念矩阵；gdsfactory 是工具生态，不是 Agent 成果。 |
| 11 | 三方向技术比较矩阵 | 三个方向的路径、文献演示与待补证据怎样同层比较 | 正式报告 §5.1–5.3、TASK-006 对比矩阵；待补证据为调研推论。 |
| 12 | 已验证能力到缺口图 | 为什么从已有验证推导出跨工具证据、系统约束与总成本等问题 | 正式报告 §5.3；缺口与切入点均为推论，并非“全领域无人研究”。 |
| 13 | 路线 A/B/C 推导图 | 候选路线如何从研究现状经证据断点形成 | `references/task-007/candidate-routes-and-open-questions.md`；尚未选择最终课题。 |

## Zotero 与图片使用记录

- Zotero 启动后，本地 API 与 Connector 均返回 200；API 显示 Zotero 10.0.3、36 个顶层条目。只读检索定位 PhIDO 条目 `HDJD3R59`/PDF `KGSYYKEY`，以及 AutoPhotonicDesign 同名预印本条目与 PDF `NP249BAB`。后者附件的 API `parentItem` 字段指向 `FGRQLSTE`，但 `/children` 列表未回传该附件；因此以可打开的原始 PDF 标题、作者、Fig. 1(b) 和 arXiv 号核对，不把该父子列表当作完整性证据。未修改文献、附件、Collection 或标签。
- Jin 2024/2026 与 Taichi 条目在 API 中可检索到，但其 `/children` 列表为空；配置的本地附件目录也未找到这几篇的 PDF。
- PhIDO PDF SHA-256：`F7063EF2DD4C1F37267684E809276897577B5A00F21DA605CE52C3422CC17CD2`。PDF 第 2 页声明文章内容除另有注明外采用 CC BY 4.0；图示在 PPT 页脚保留作者、年份、期刊、DOI 和 Fig. 编号。
- AutoPhotonicDesign PDF SHA-256：`DAEF5A9DE80FC3DD72286CCD63E8A36362DBA31328549BA24DEDB30FDD2AB683`。附件中未定位到明确许可声明；本次只作有来源标注的组会讲解摘图，对外公开传播前应核实使用许可。
- 两处裁剪均保留了所讲解流程的节点、箭头和图内标注；没有将不同论文的图像拼接成一项成果。生成的裁剪 PNG 保存在 `assets/paper-figures/`，不需要 Zotero 在线运行即可重建本 PPT。
- SVG 概念图生成源为 `assets/diagrams/build_explanatory_svgs.py`。PowerPoint 中的 SVG 为矢量图形，文字/箭头的精确修订应回到生成源；论文原图为高分辨率裁剪 PNG，无法作为原生形状逐节点编辑。
