# TASK-007 补充检索与筛选记录

## 方法定位

本轮是**定向范围综述与证据综合**，不是穷尽式系统综述，也不宣称满足 PRISMA。候选池主要继承 TASK-004 至 TASK-006；仅当新的一手证据可能改变“研究现状、代表路线或候选路线”的判断时补充检索。

## 检索记录

| 日期 | 来源 | 检索式 | 用途 | 结果处理 |
|---|---|---|---|---|
| 2026-09-21 | Volcengine Search | `2026 photonic integrated circuit design agent LLM autonomous design` | 核对 2026 年 Agentic PIC 新工作 | PhIDO、AutoPhotonicDesign、PICopilot、PICasso 等仍覆盖主要公开对象；未发现足以改变“尚无完整开源闭环”的新一手证据。 |
| 2026-09-21 | Volcengine Search | `2025 2026 integrated photonic DAS interrogator silicon photonics` | 核对 DAS 集成前端与 2026 进展 | 保留 Jin 2024 与 Jin 2026 为集成解调器主证据；以全文/会议原文核读为准。 |
| 2026-09-21 | Volcengine Search | `2025 2026 photonic AI accelerator system inference chip energy accuracy` | 核对光子 AI 系统级工作 | PACE、通用光子 AI 加速器、深层映射等仍为主要 2025 代表；不按新闻稿扩充。 |
| 2026-09-21 | Volcengine Search | `PICBench PhIDO AutoPhotonicDesign MetaChat Paper2Agent` | 补齐论文、仓库和评价层证据 | 回到 arXiv、PMC、Nature/Science、官方仓库和固定提交核验；二手报道不进入核心证据链。 |

## 纳入规则

1. 优先同行评审论文；2025–2026 新方向可纳入有足够方法与结果细节的预印本。
2. 涉及“开源”时必须有公开仓库，并分别记录许可证、固定提交和代码可见性。
3. 代表性工作必须能明确定位到器件、电路、系统、Tool、Harness、Evaluator 或 Benchmark 层。
4. 会影响路线判断的结论优先全文核读；无法取得全文时降低证据强度。
5. DAS 与光子 AI 指标只有在系统边界、任务、精度和测量口径相容时才比较。

## 排除规则

- 仅有营销页、媒体报道或无原始技术资料的项目。
- 把“使用 LLM”“生成 Python”直接包装为 Agent 闭环、但没有执行与反馈证据的工作。
- 题名相似但属于 FBG 解调、通信、成像或通用 EDA，且不能直接支撑本报告问题的文献。
- 重复书目、数据集 DOI、纯仓库和无法核实出处的记录。

## 停止规则

当新增结果不再改变三方向的主要技术路线、代表系统、证据边界或候选路线时停止扩充。TASK-007 不进行持续监测；后续文献更新须由新任务授权。

## 继承材料规模（非 PRISMA 流程）

| 阶段/来源 | 数量 | 含义 |
|---|---:|---|
| TASK-004 候选池 | 20 个论文/项目 | Agentic PIC 与 Harness 第一轮公开候选；不是三方向全部文献。 |
| TASK-005 深挖 | 6 个核心对象 + 条件对象 | 架构、工具、评价与验证层的一手证据拆解。 |
| TASK-006 论文索引 | 32 篇 | DAS 8、光子 AI 12、Agentic PIC/方法 12；另有纯项目/工具，不计入论文数。 |
| TASK-007 重点全文/正文核证 | 见全文证据审计 | 按“是否影响正式结论和候选路线”抽样，不是全部 32 篇逐篇全文综述。 |

这些数字属于不同阶段和对象类型，不能串成“检索到 N 篇、排除 M 篇”的伪 PRISMA 流程。
