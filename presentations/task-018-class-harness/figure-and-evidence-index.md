# 当前版本图示与证据索引

日期：2026-10-09。图片是论文原图的裁剪/缩放；中文注释单独放在右侧，不改原图。正式题名、来源、Figure和DOI如下。原始PDF不复制进仓库。

| 页 | 原图与来源 | 解释问题与证据边界 |
|---|---|---|
| P1 | 自绘SVG；candidate-research-direction.md §2–4 | Harness职责分工，概念层 INFERENCE。 |
| P2 | 自绘SVG；同上§2–4 | 物理诊断与设计决策的拟研究问题，尚未验证。 |
| P3 | Sharma et al., 2025, *AI agents for photonic integrated circuit design automation*, Fig.1, PDF p.3, DOI:10.1063/5.0300741；复用task-010已有裁图 | Interpreter/Designer/Layout/Circuit Verification；图中FDTD非主发布分支。CC BY 4.0。 |
| P4 | Sharma et al., 2025, 同题，Fig.5（Gemini-2.5-pro/GPT-4o局部与原图图例），PDF p.8；Table II p.9，同DOI | 102描述、四级23/10/60/9；左柱pass@1、右柱pass@5。S仅结构有效。原图裁框见paper-figure-manifest.json。CC BY 4.0。 |
| P5 | Jiang et al., 2026, *PICopilot: An LLM-based Agentic Framework for Assisting Photonic Integrated Circuit Design via Script Generation*, Fig.2, PDF p.3；§3.6 p.6、Table2/3 p.7，DOI:10.48550/arXiv.2608.01791；复用task-010已有裁图 | 内部静态反馈与外部执行评分不同。48项，12/12/24分组，每项15次，≥3次成功计Solved。方法为FACT，完成结果为AUTHOR CLAIM。再分发许可未核实。 |
| P6 | Kharel et al., 2026, *Autonomous agentic design for photonics*, Fig.1(b), PDF p.3；Table S2 p.20，DOI:10.48550/arXiv.2606.00915 | 人类初设/目标/约束→规则/求解器→保留回退。多物理初设曾由专家纠错。新裁图保留完整环路与Human/Outputs。再分发许可未核实。 |
| P7 | Kharel et al., 2026, 同题，Fig.2(a), PDF p.5；§S2.1 p.12–14，同DOI | 400nm SiN、1550nm、12µm半径、150nm最小特征、50次仿真预算下，作者报告弯曲损耗0.460→0.109dB。保留负dB原坐标与kept/discarded图例。AUTHOR CLAIM，非本项目复现/流片。 |
| P8 | 自绘总结SVG；TASK-016三项目比较与候选方向材料§2–8 | 区分结构、脚本、数值验证层级；候选方法增益仍UNKNOWN。 |

三篇附件由Zotero Local API file-url确认；三个PDF SHA与TASK-016 source-manifest完全一致。论文原文和数据没有修改。P4/P6/P7新裁框及PDF版本绑定见paper-figure-manifest.json；5页图旁说明可通过build_source_projects.py修改。

PICopilot/Kharel原图再分发许可未核实，当前使用范围为本地课堂文件；没有远程发布或推送。制作日期不代表新文献检索截止日期。
