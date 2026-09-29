# TASK-016 交接记录

- 起始 commit：`c02f121629f7eceb5d03e49d968894e48352cde9`；完成 commit：包含本文件的提交，准确 SHA 见任务交接答复。
- 状态：`REVIEW_READY`，等待 GPT 最终只读审查；本文件不表示验收通过。
- 写入范围：`docs/TASK.md`、`docs/CURRENT_STATE.md`、`references/task-007/formal-research-report.md`、`references/task-016-evidence/`、`presentations/task-010-group-meeting-rebuild/`。现有三方向结构未变。开始时已有的 `output/task-007/` DOCX 修改与同名未跟踪 PDF 没有写入或纳入提交。

## 交付与新增判断

| 交付 | 文件 | 主要内容 |
|---|---|---|
| 更新报告 | [`../task-007/formal-research-report.md`](../task-007/formal-research-report.md) | 增加原图、指标条件、片上/片外、验证层级与系统边界。 |
| 更新 PPT | [`../../presentations/task-010-group-meeting-rebuild/`](../../presentations/task-010-group-meeting-rebuild/) | 可编辑 20 页 PPTX、20 页 PDF、讲解备注、图示及证据索引；无附录。 |
| 原图清单 | [`figure-sources.md`](figure-sources.md) | 新增三张裁图：PhIDO Fig. 5；Cheng Fig. 1、Fig. 2。记录 DOI、页码、裁剪框、许可。 |
| 关键数据 | [`key-data.csv`](key-data.csv) | 七篇论文共 34 条指标/任务设置，含数值、单位、条件、定位、等级及边界。 |
| Agentic 对比 | [`agentic-pic-comparison.md`](agentic-pic-comparison.md) | PhIDO、PICopilot、Kharel 八列比较，重点分开输入、工具反馈和成功定义。 |
| 新证据日志 | [`evidence-log.md`](evidence-log.md) | A1–A3、D1–D3、P1、S1 八项新判断及原文定位。 |
| 原文版本 | [`source-manifest.md`](source-manifest.md) | Zotero 父级/附件 key、页数与 SHA-256；PDF 保持只读且不复制进仓库。 |
| 未核实项 | [`README.md#unknown`](README.md#unknown) | 原始运行日志、统计口径、实物验证、系统能耗、图像再分发许可等。 |

三项最关键的本轮判断：PICopilot 内部静态反馈与外部 benchmark 执行需要分开（Jiang §3.6/4.1.4）；Kharel 的数值闭环依赖工程师给定约束和正确仿真初设，首次多物理设置有人工修正反例（Kharel Fig. 1/Table S2/§S6）；光子核心 ops 与完整 AI 任务吞吐、准确率和墙插能耗口径不同（Ahmed Fig. 2/Table 1/Methods）。等级及细节见证据日志。

## 验证与未执行

- 从 Zotero 本地附件只读核对七篇 PDF 的图号、页码、数值、单位、条件及限制；裁图逐张核对坐标轴/图例，Cheng Fig. 2 在最终检查中重新裁剪以保留完整横轴。
- 数据 CSV：34 行、七篇论文，必填字段与证据等级有效。证据包和报告的本地相对链接检查无失效项。
- PPT 构建 QA：20 页；0 溢出、0 重叠、0 占位、0 视觉警告、0 设计错误/警告。PowerPoint 导出 20 页 PNG，检查全部页面联系图及重点页最终全尺寸图；PPTX 20/20 页有备注，PDF 20 页。
- 未运行论文代码、仿真或实验；没有独立重算作者原始数据；未在投影设备试讲；版权未明的 Jin/Sandmann/Ahmed 原图仅定位，PICopilot/Kharel 已有局部图的再分发许可仍待核实。
