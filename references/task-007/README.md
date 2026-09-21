# TASK-007 正式调研报告与组会汇报

状态：`ACTIVE`

证据截止：2026-09-21

## 任务定位

本目录将 TASK-004、TASK-005 和 TASK-006 已验收材料综合为正式中文技术调研报告、组会汇报材料和可追溯的证据核查记录。它不启动实验、仿真或工程实现，也不确定最终研究方向。

## 交付物

- `formal-research-report.md`：正式技术调研报告正文（Source of Truth）。
- `full-text-evidence-audit.md`：影响核心判断的全文核查与证据边界。
- `search-and-screening-log.md`：本轮补充检索、筛选范围与停止规则。
- `terminology-ledger.md`：中英文术语与统一表述。
- `candidate-routes-and-open-questions.md`：2–3 条候选路线与待讨论问题。
- `citation-verification.md`：引用、链接和书目信息核查记录。

组会 PPT 与门户页面是上述 Markdown 的展示层，不替代本目录的研究事实源。

## 证据标签

- `FACT（事实）`：论文正文、官方技术文档或公开代码直接支持。
- `AUTHOR CLAIM（作者报告）`：作者报告、但本项目未复算或复现。
- `CODE VERIFIED（源码核验）`：固定提交的代码结构可见；不等于成功运行或物理正确。
- `INFERENCE（推论）`：基于多项证据形成的研究分析。
- `UNKNOWN（未知）`：当前证据不足。

## 范围边界

- 不把论文指标当作本项目实验结果。
- 不把脚本生成等同于稳定工具调用。
- 不把求解器被调用等同于物理正确。
- 不把 GDS、DRC、LVS 或 signoff 相互替代。
- 不评估课题组现有设备、商业软件、PDK 或流片条件。
- 不设计实验、成功判据或实现计划。

