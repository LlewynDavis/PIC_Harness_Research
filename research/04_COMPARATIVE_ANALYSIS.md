# 研究方向横向比较框架

## 文档定位

本文件服务于 Phase 1 技术路线调研。TASK-006 已按相同维度完成第一轮三方向比较；详细证据、条件与路线以 `references/task-006/` 为事实源。本文件保留长期比较框架，不复制研究结论。

## TASK-006 输出入口

- `references/task-006/three-direction-technical-map.md`
- `references/task-006/comparative-analysis-matrix.md`
- `references/task-006/candidate-research-routes.md`
- `references/task-006/critical-review-and-conditions.md`
- `references/task-006/source-log.md`

当前三条候选路线均为待验收研究判断，不等于最终选题或工程授权。

## Agentic PIC Design 新增分析维度

| 分析维度 | 需要回答的问题 | Agentic PIC Design 当前状态 |
|---|---|---|
| 模型/Harness 能力边界 | 哪些能力由模型承担，哪些必须外化？边界是否随任务变化？ | 待文献调研 |
| 确定性工具依赖程度 | 完成可验证设计需要哪些确定性工具？ | 待文献调研 |
| 物理 Validator 需求 | 哪一级验证才能支持相应物理主张？ | 待文献调研 |
| 动态知识依赖 | PDK、材料、软件接口和最新文献如何更新与追溯？ | 待文献调研 |
| 自适应工具调用价值 | 动态调用能否改善正确率与成本权衡？ | 待对照实验设计 |
| 不确定性感知需求 | 哪些不确定性指标能够预测搜索、仿真或人工介入需求？ | 待文献调研 |
| Benchmark 可构建程度 | 是否可获得任务、golden reference、工具轨迹和物理判据？ | 待可行性分析 |
| 可验证 Research Question | 是否能形成可证伪、可测量且范围适当的问题？ | 待路线收敛 |

## 后续横向比较规则

- 与其他候选方向比较时使用相同维度和证据等级，避免为 Agentic PIC Design 定制有利标准。
- 空白项只能在获得文献、源码、官方文档或实验依据后填写。
- 理论契合度不等于研究价值；还需比较数据可得性、实验成本、物理验证上限和毕业周期风险。
- 若某项无法可靠测量，应标记 `UNRESOLVED`，不得用定性印象替代。
