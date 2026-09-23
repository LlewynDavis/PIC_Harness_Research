# TASK-008 组会调研 PPT 交付检查

日期：2026-09-23。基线：TASK-007 已验收提交 `3ed876f5fce34d38a47907d6c68c476f6a51d090`；本次起始 HEAD `18e19afb51fb77d9f540e6294822d7c11375647e`。

## 内容与结构

- 主讲 14 页、附录 11 页，共 25 页；主讲页 14/14 含讲解备注，按 15–20 分钟安排。
- 保留原版 DAS 与 Agentic PIC 概念流程图、代表论文、验证阶梯和候选路线；将细节论文表、OFC 2026 模块边界、Reference Architecture V0 与反例移至附录。
- 新增同维度跨方向比较、从代表工作推导的缺口、A/B/C 路线并列和组内讨论页。路线定义与 TASK-007 候选路线一致，未选定最终方向。
- 将 Jin 2024/2026/Cheng 2023 分别定位为 PIC 前端、混合模块与器件；Netcast 的 40 aJ 明确为接收端光能；PhIDO、AutoPhotonicDesign、PICBench 的验证上限与正式报告一致。
- 论文出处按页列在来源行；两张主讲概念流程图明确标为基于已验收材料重绘。图像不可作为论文实物结构或本项目实现证据。

## 执行过的验证

- `build_workspace.py --qa --skip-render --overwrite` 与最终文件的 `qa_gate.py --strict-geometry --skip-render` 均退出 0；planning validation 为 0 error、0 warning。
- 结构 QA：文本溢出 0、重叠 0、占位符 0、几何错误 0、设计错误/警告 0/0；另有 6 个非阻断几何警告（5 个轻微留白、1 个附录页密度）。
- Microsoft PowerPoint 只读打开最终 PPTX，并导出 25/25 张 1600×900 PNG 与 25 页 PDF；检查整套缩略图，并放大核对封面、代表工作、研究缺口、路线比较、讨论页及末页。修复了封面模板默认英文标签与末页孤行标点。
- `python-pptx` 读回 25 页、16:9 画布、14/14 主讲备注；13 个原生表格和 3 张概念图。PDF 经 `pypdf` 读回 25 页。
- 对照 `references/task-007/formal-research-report.md`、`full-text-evidence-audit.md`、`candidate-routes-and-open-questions.md` 及 TASK-006 路线材料检查关键判断；未开展新的领域检索或实验。

## 限制

- 图示是高分辨率图片，文本、形状与表格可在 PowerPoint 中编辑；图中箭头/节点如需调整，应修改本目录 `.mmd` 原文件并重新渲染。
- 页脚引用为追溯而设，投影讲解时应口头解释主表内容；本次未在实际会议投影设备上预演。
- 外部论文指标未由本项目复现；没有物理或系统级验证结论。
