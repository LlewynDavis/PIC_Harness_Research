# 当前真实状态

更新日期：2026-09-27

## TASK-012 本地论文知识库对接

- 用户于 2026-09-27 授权将当前项目论文逐篇接入独立 Obsidian Vault。以 `references/task-006/paper-and-repository-index.md` 中的 32 篇论文为范围，Zotero Local API 只读确认当前库共 36 篇父级论文：项目 32 篇中 PhIDO 已有详细卡，另外 31 篇新建首轮笔记；旧有的另外 4 篇逆向设计基础卡保留。本地 Vault 现有 36 张论文卡。
- 项目索引和固定对接说明位于独立 Vault 的 `论文知识库/01_Papers/PIC_Harness_Research_论文索引.md` 与 `论文知识库/00_System/PIC_Harness_Research_对接说明.md`。本机绝对路径仅保存在被 Git 忽略的 `configs/obsidian.local.yaml`，项目仓库不收纳论文卡与 PDF。
- 29 篇新导入项目论文的本地关联 PDF 可访问；Taichi 2024 和 FBG PIC 传感对照文献无本地 PDF，卡片标记待核读。首轮笔记基于 PDF 摘要/首页和已核验项目研究材料，不能视为全部 32 篇的逐页全文精读或论文结果复现。
- Zotero 未被修改。36 张卡的父级 item key、原文题名和 DOI 经 Local API 逐一核对；32 个项目索引的 Zotero 桌面定位链接与论文卡链接均通过结构检查。现行笔记不生成 BibTeX CiteKey。

## 仓库共享

- 用户于 2026-09-24 授权创建公开 GitHub 仓库 `https://github.com/LlewynDavis/PIC_Harness_Research`，用于向组员共享目前项目文件。已推送 `main`，并核验 GitHub 可见性为 `PUBLIC`、默认分支为 `main`、远程 HEAD 与本地提交一致。Office 临时锁文件由 `.gitignore` 排除。

## 已完成

- 2026-09-23 基于用户最新 P1–P20 大纲完成 `TASK-010｜首次正式组会 PPT 重做`：在 `presentations/task-010-group-meeting-rebuild/` 从空白 workspace 建立 20 页无附录学术汇报，交付可编辑 PPTX、20 页 PDF、20 页备注、14 张解释性 SVG 图、4 张带图号的原论文 Figure、图示/证据索引及 QA 记录。严格 QA 为 0 溢出、0 重叠、0 占位符、0 视觉警告；PowerPoint 导出 20 页 PNG 与 PDF。14 条面积密度提示经逐页视觉审阅保留。P18/P19 表述研究问题及个人倾向，未确定课题、算法或实验。Zotero API 本次超时，已直接只读使用本地三篇 PDF；原论文性能未复算，也未由汇报人完成实际口头试讲。

- 2026-09-23 按用户授权交付 `TASK-009｜PIC × AI Agent 科研英语词库 V1`：`learning/vocabulary/` 中有 200 条术语的 XLSX 和 UTF-8 TSV，覆盖光子学基础、器件与仿真、光子 AI、Agent Harness、论文英语五类。已读回核对文件与导入页一致；Knowt 账户内实际导入未执行。该学习资料未改动调研结论、技术路线、工程代码或实验状态。
- 用户进一步要求可在 iPhone 的 Knowt“从设备上传文件”入口直接选取文件；已补充 16 页 PDF，完整包含上述 200 对词条并上传至用户 Google Drive。Knowt 官方支持 PDF 生成词卡，但 App 内生成结果尚未由本项目实测，不能保证 AI 自动保留原有 200 张卡的数量与措辞。
- 用户随后改用墨墨记忆卡，且要求文件直接在对话中交付。已生成 200 张基础正反面卡的 `.apkg` 和同内容的 UTF-8 批量制卡 `.txt`；文件结构和内容与词库逐条核对通过，墨墨 iPhone App 的实际导入尚未实测。本次没有新增云端上传。

- 用户于 2026-09-23 授权的 `TASK-008｜组会调研 PPT 优化` 已完成图示化补充修订并处于 `REVIEW_READY`：基于 TASK-007 已验收报告与可编辑 workspace，形成无附录的 14 页独立 PPTX、PDF、14 页备注及图示来源/验证记录，位于 `presentations/task-008-group-meeting/`。主讲 12 张技术与分析页均有解释性图示或矩阵；两张原论文 Figure 只读取自 Zotero PDF，其他图示根据已核验材料重绘。TASK-007 原始交付和验收结论未修改；本次未开展新实验或确定最终研究方向。

- 已建立独立的 `PIC_Harness_Research` Git 仓库。
- 已建立最小长期维护目录与文档骨架。
- 已明确旧项目 `D:\AI_PIC_Demo` 的封存和只读边界。
- 已记录首批研究与工程决策。
- 已建立空的 `pic_harness` Python 包入口。
- 已建立 Codex 与 Qwen 的人工协同治理规则和 Qwen 薄入口。
- 最终十条协作规则已经本机 Qwen Code 0.22.3 只读审阅并逐条接受。
- Codex“AI协同”任务已作为 GPT、Codex 与 Qwen 的人工消息协调入口完成首次双向同步。
- GPT/ChatGPT 项目“AI协同”对话与项目限定 Qwen Code 通道均对 `TASK-003` 基线返回 `FINAL_ALIGN_ACK`，未报告实质分歧。
- 已完成 `TASK-004` 的第一轮公开证据调研：形成 20 个候选池、Top 5 架构对比、Top 3 对抗性审查和三项路线初判。
- 已实际核验候选的论文/预印本链接、公开仓库、根许可证识别结果与关键 README/架构代码路径；未发现证据充分、可直接满足最高目标的全开源 PIC Design Agent Harness。
- 已确认 Qwen 科研任务使用项目主对话或必要的新对话，Codex“AI协同”任务只用于对齐；本轮 Qwen 仅提供未经核验的候选召回，最终条目均由 Codex 复核。
- GPT 已在项目主对话对 `TASK-004_REVIEW_READY` 返回 `ACCEPT`；用户已正式确认 `TASK-004 = ACCEPTED / CLOSED`。
- 用户已正式启动 `TASK-005`。当前工作仅限核心架构的一手证据深挖、技术缺口分析、Reference Architecture V0 和候选路线种子，不包含工程实现或最终 L01 报告。
- 已完成 `TASK-005` 的审查包：六对象技术地图/架构拆解、Harness Capability Matrix、Verification Ladder、Reference Architecture V0、RESULT schema V0、最小状态机、Build vs Reuse、Research Gap Matrix、5 个路线种子和路线级对抗性审查，材料位于 `references/task-005/`。
- GPT 已在项目主对话对 `TASK-005_REVIEW_READY` 返回 `ACCEPT`；`TASK-005 = ACCEPTED / CLOSED`，无需返工。
- GPT 要求后续保留四项约束：先区分 device-level 与 circuit-level；verification 的诚实上限为 research-grade deterministic verification；区分实现复用与架构模式复用；DesignSpec 必须通过对照实验验证价值，不能预设为核心创新。
- 用户已于 2026-09-17 明确启动 `TASK-006` 文献框架整合任务；后续验收不得将其重置为 `NOT_STARTED`。
- 用户已正式启动 `TASK-005A｜Research Portal MVP`：仅用 MkDocs Material 为 `references/task-005/` 增加本地人工阅读层，原研究 Markdown 保持 Source of Truth，不增加研究结论。
- 已完成 `TASK-005A` 的最小门户实现：MkDocs Material 首页覆盖核心结论、技术地图、Capability Matrix、Reference Architecture V0、Research Gap → Entry Point、5 个路线种子和证据入口；左侧导航可进入原始研究材料的构建时嵌入页。
- 已通过 `mkdocs build --strict`、本地服务访问和真实浏览器检查；Mermaid 已渲染为 SVG，宽表格容器为横向滚动，验收截图位于 `output/playwright/`。`references/task-005/` 未被修改。
- GPT 已于 2026-09-20 针对提交 `0da0996543cff09f17751472f8e53efd2a8b8be9` 返回 `TASK-005A_ACCEPTED`；`TASK-005A = ACCEPTED / CLOSED`，不再增加非必要功能。
- `TASK-006` 已完成并由 GPT 验收关闭，无需重新启动或重复创建。
- 本轮 Qwen 科研子任务通过既有项目主对话下达，未使用“AI协同”通道，也未新建多余科研对话。其只读输出未被直接采用，Codex 已用固定 commit 源码和论文正文复核并纠正关键字段。
- 已纠正 Qwen 渠道记录：初次科研召回实际因 `qwen -c` 误入 `AI协同` 会话，随后已在既有 Qwen 项目主对话完成只读复核；该误用不再被表述为独立科研会话。
- 已完成 `TASK-006` 审查包：三方向技术地图、跨方向/内部比较、研究条件矩阵、三条候选路线、最小验证实验、对抗性审查与来源日志均位于 `references/task-006/`。
- 暂定路线优先级为：分层的面向智能体 PIC 评价基座优先；人工智能驱动的 DAS 光电混合集成设计约束传播，以及光子人工智能计算的器件误差—任务误差联合验证作为条件路线。该排序是已验收的 Phase 1 研究判断，不是已授权工程路线。
- GPT 于 2026-09-21 针对提交 `9cab614ce29b7ed4289f641c0d7a7eb5f277e24f` 返回 `TASK-006_ACCEPTED`；`TASK-006 = ACCEPTED / CLOSED`。该验收时点没有执行任务。
- 用户已于 2026-09-21 正式授权 `TASK-007｜PIC_Harness_Research 正式调研报告与组会汇报`；该任务已完成交付，并于 2026-09-23 获 GPT 验收，状态为 `ACCEPTED / CLOSED`。任务只做调研综合、关键全文复核、报告/PPT 和 Portal 更新，不包含实验设计、仿真、Harness 实现或最终路线选定。
- TASK-007 已形成六章正式中文报告、25 页可编辑组会 PPT、三方向候选路线与开放问题、全文证据审计、引用核验和 Portal 阅读层；交付提交为 `3ed876f5fce34d38a47907d6c68c476f6a51d090`。
- GPT 已针对交付提交 `3ed876f5fce34d38a47907d6c68c476f6a51d090` 返回 `TASK-007_ACCEPTED`；当前无执行中任务。
- Research Portal 已增加 TASK-006 中文总览与九个专题入口；TASK-005 已验收档案继续保留。
- Research Portal 左侧导航已改为分层文件夹：TASK-006 的项目细分页收纳在“三方向技术地图”，比较、候选路线和审查收纳在“比较与路线”；TASK-005 档案按“架构与能力”“路线与证据”折叠，原页面地址保持不变。
- Paper2Agent 已作为 `03 Agentic PIC Design` 下“科学计算工具自动构建与验证”的正式调研候选纳入 TASK-006 技术地图、内部比较与证据日志；当前仅完成论文与固定提交源码的只读核验，未安装、未执行、未接入 MCP，也未改变候选路线排序。
- 原“DAS 光电混合集成”独立方向已替换为“DAS 光电混合集成 × 面向智能体的 PIC 设计”交叉验证场景，目标明确为研究人工智能如何完成 DAS 系统需求到芯片/电子/封装约束、工具验证和失败修正的可追溯闭环。当前没有公开或本项目证据证明人工智能已端到端完成 DAS 光电混合集成芯片设计。
- TASK-006 已增加三个逐项目详解：5 组 DAS 物理基线、12 个光子人工智能计算代表项目、7 个面向智能体的 PIC 设计/机制参照项目；每项记录问题、方法、真实完成度、依赖、可借鉴机制、限制和与本课题关系。
- 已增加统一“论文与项目出处索引”：32 篇可信论文按 DAS、光子人工智能计算、Agentic PIC/方法分组，纯项目与工具另表登记；门户中的项目标题可直接跳转 DOI、arXiv、PubMed/PMC 或官方仓库。
- 已完成 Zotero 写入：本地 RIS 含 32 条唯一 DOI/题名记录；既有 PhIDO 加新增 31 条后，Zotero API 核验有 36 个顶层论文条目且题名唯一。新增记录已写入 `02_光子芯片设计自动化`、`03_AI智能体与设计代理`、`06_DAS与光纤传感` 和 `07_光计算与AI芯片`；英文分类尚未删除。
- 已核读用户提供的 Jin 等 OFC 2026 三页原文，将 InP–SOI 混合集成 DAS 解调器从摘要级来源提升为独立物理基线：确认低于 3 kHz 线宽的 InP 外腔激光、SOI 收发 PIC、微光学耦合/隔离、TEC 与约 40 mm × 40 mm × 10 mm 模块；同时保留 EDFA、环行器、AWG、TIA、DAQ、DSP 外置以及长期稳定性、良率、完整功耗/成本未知的证据边界。该证据未改变 TASK-006 路线排序。
- GPT 已针对 TASK-006 返回补充对抗性审查；Codex 将其中五层约束接口、独立验证原则、最小闭环和三种验证完成状态按 `INFERENCE` 去重纳入事实源。GPT 标为 `UNKNOWN` 的外部文献线索未因该回复自动升级为项目证据，也未改变三条候选路线排序。
- Qwen 项目主对话承担了本轮批量字段召回；Codex 已纠正其将数据集/项目混入论文表、PhIDO 期刊名错误及缺失 DOI 等问题，并以 Crossref、arXiv、PubMed/PMC 和仓库证据重新生成导入清单。

## 当前调研重点

项目仍处于 `Phase 1｜国内外研究现状、发展前景、核心难点和技术路线调研`。Agentic PIC Design 调研新增：

- Model vs Harness 能力边界；
- Internalization vs Externalization；
- Adaptive Tool Calling；
- Uncertainty-aware Agent；
- PIC Agent Benchmark。
- 科学计算方法到可测试、可追溯 Agent Tool 的半自动转换，以及与少量手写 Typed Tool Contract 的成本—可靠性对照。

上述内容均为候选理论框架、研究问题或待验证假设，不增加任何实现状态。

## 阶段触发提醒

- `DEFERRED`：已记录“Jev 类有限决策模型在 PIC Agent Harness 中的适用性”。当主要领域调研完成并开始收敛技术路线，或准备开展工具路由、失败分类、自适应 Tool Calling 对照实验时，Codex 应先询问用户是否纳入技术比较或实验设计；用户确认前不得启动相关调研、安装、接入或实现。
- 用户已于 2026-09-21 明确要求 Jev 类有限决策模型调研继续延后；当前不纳入 TASK-006，也不启动技术比较或实验设计。
- 用户已于 2026-09-21 取消此前讨论中的 `TASK-007｜实验设计`：当前 L01 阶段只做调研、证据综合与报告整理，不开展 benchmark、仿真、Harness 或其他实验设计。`TASK-007` 未创建、未授权、未启动；未来若要开展实验，必须另行提出任务并获得用户明确授权。
- 上一条记录只针对被取消的“实验设计版 TASK-007”。用户随后于 2026-09-21 另行授权同编号的“正式调研报告与组会汇报版 TASK-007”；两者任务内容不同，旧记录保留为历史，不限制当前报告任务。

## 尚未实现

- 尚未在研究平台代码中接入任何 LLM，包括 Qwen、GPT、Hermes 或 OpenHands。
- 尚未实现 Agent Harness、Single-Agent 或 Multi-Agent 系统。
- 尚未实现 Tool、MCP Server 或外部 API 集成。
- 尚未实现 DesignSpec 或其他结构化设计表示。
- 尚未接入光子芯片设计、仿真、优化或验证工具。
- 尚未建立 benchmark 数据集、指标或 baseline 结果。
- 尚未运行科研实验，也没有可报告的实验结果。
- 尚未选择 DAS 交叉场景或光子人工智能计算的具体实现路径。
- 尚未核验或接入用户协作拓扑中指定的本地 `Qwen3.8-27B`；本次只验证了 Qwen Code CLI 层的治理共识。
- 尚未建立自动消息桥；当前同步由 Codex 在获准任务内显式发送、读回和转述。
- 尚未在本机安装、运行或复现 `TASK-004` 候选系统；候选的物理结果和论文指标均是外部公开证据，不是本项目实验结果。
- 本轮 31 条新增文献已写入 Zotero；英文旧分类仍待用户确认后清理。

## 当前证据边界

本仓库当前证明项目骨架、双模型治理规则、一次人工三方对齐以及 `TASK-004`、`TASK-005` 的公开证据调研已经完成并获 GPT 验收；`TASK-005A` 的 MkDocs Material 人工阅读门户、`TASK-006` 三方向调研和 `TASK-007` 正式调研报告/组会汇报均已验收关闭。TASK-007 的路线判断仍只来自文献、源码和官方材料，不构成模型接入、软件复现、物理验证或科研实验；论文作者指标不得当作本项目实验结果。当前没有执行中任务。TASK-008 本轮 Zotero 启动后本地 API 与 Connector 均返回 200；只读检查配置的附件目录发现 10 份 PDF，其中可用于主讲原图的是 PhIDO 与 AutoPhotonicDesign；不假定全部顶层文献均具备可读 PDF。

## 更新规则

只记录已经由代码、测试、实验记录或可核验外部证据支持的状态。计划和设想写入 `docs/RESEARCH_PLAN.md`，当前唯一执行任务写入 `docs/TASK.md`。
