# 当前唯一执行任务

## TASK-004：L01 光子芯片设计 Agent / Harness 架构第一轮调研

- 状态：`COMPLETED`
- 日期：2026-09-15
- 授权来源：用户在当前对话中给出完整任务、角色分工、验收标准和禁止范围。
- 上游目标：L01——芯片设计 Agent 项目架构调研，形成调研报告；重点要求“框架完整、路径开源”。
- 执行协调器：Codex。
- 目标：先建立可信候选池和架构对比基线，不直接写 L01 最终综述。

## 研究范围

第一优先级：

- Photonic Integrated Circuit / silicon photonics + LLM / Agent；
- PIC design automation agent；
- EDA agent / engineering design agent；
- LLM 调用真实 simulation / CAD / EDA tool；
- Agentic scientific workflow / tool-use framework。

已知对象至少纳入 Sharma et al. 2025、PICopilot、gdsfactory / gplugins 生态。

第二优先级仅作为 Harness 架构参考：MCP 类 Tool 接口、LangGraph、AutoGen 等 Agent orchestration。通用 Agent 框架不得与真正 PIC 自动设计系统混为一类。

## 方法与角色

- 显式使用 `nature-academic-search` 建立论文和项目候选池，覆盖 2021–2026，记录检索词、来源、日期、DOI / GitHub，并区分同行评审论文、预印本、GitHub 项目和商业产品。
- 仅对筛出的高价值代表对象使用 `nature-reader` 精读。
- 对 Top 3 使用 `scientific-critical-thinking` 做对抗性证据审查。
- 本轮不启动 `literature-review` 或 `nature-literature-pipeline`。
- Codex 负责拆解、检索复核、GitHub / 代码结构 / README / 许可证核验、真实 Tool 调用检查和最终判断。
- Qwen 只承担候选扩展、论文初筛、内容与架构字段初抽取；其输出是中间材料，未经 Codex 一手证据复核不得进入最终结论。
- Qwen 科研子任务通过项目主对话或必要的新对话下达，并尽量复用主对话、减少对话数；Codex“AI协同”任务只用于对齐，不用于科研任务下达。

## 统一抽取字段

- 对象类型与时间；
- 论文 DOI / 预印本链接 / GitHub；
- 代码可见性与许可证；
- Agent 输入与输出；
- 结构化中间表示；
- Tool 注册与真实调用方式；
- 状态管理与自动迭代；
- 人类干预与失败恢复；
- 是否生成版图、是否完成验证；
- 实验指标、baseline 与证据缺口；
- 闭环级别：代码生成、单次 Tool 调用、部分闭环或端到端闭环。

## 交付结果

A. 约 10–20 个经核验的有效论文 / 项目候选池，宁缺毋滥。

B. Top 5 架构对比表，说明入选理由并为每个对象提供论文或代码一手证据。

C. 第一轮路线判断：

1. 是否已经存在可直接满足最高目标的开源 Photonic Design Agent Harness；
2. 现有工作分别解决了 Harness 的哪些局部能力；
3. 最可能需要自行补齐哪些核心模块。

## 验收标准

- 至少发现并核验 10 个有效候选；
- Top 5 每个都有论文或代码的一手证据；
- “开源”必须实际核验仓库、许可证和代码可见性；
- 区分“LLM 生成脚本”和“Agent 调用真实 Tool”；
- 区分“单次工具调用”和“闭环自动设计”；
- 至少对 Top 3 做一次对抗性证据审查；
- 明确指出证据缺口，不自行脑补；
- 不开始写 L01 最终报告；
- 不扩展到新的工程实现任务。

## 禁止范围与停止条件

- 不修改或复制 `D:\AI_PIC_Demo`；
- 不实现 Agent、MCP、RAG、仿真集成、DesignSpec、benchmark 或其他工程功能；
- 不把通用 Agent 框架表述为 PIC 自动设计系统；
- 不把 LLM、Qwen 或论文作者的陈述当作物理真值或开源证明；
- 完成后只回传 `TASK-004_REVIEW_READY` 与规定材料；GPT 审查完成前不自动启动 TASK-005。

## 验证方法

- 对论文核对出版社、DOI、arXiv 或作者项目页等一手来源；
- 对开源项目核对实际仓库、许可证文件、关键源码与提交可见性；
- 对闭环能力核对方法、代码路径、工具调用、输出读取和迭代控制证据；
- 文档完成后执行路径检查、字段完整性检查、`git diff --check` 和 Git 状态检查。

## 完成记录

- 完成日期：2026-09-15。
- 交付位置：`references/task-004/`。
- 候选池：20 个；已区分直接 PIC、相邻光子器件、EDA/科学 Harness 和通用控制面。
- Top 5：PhIDO/PhIDO-Agentic、AutoPhotonicDesign、gdsfactory/gplugins、MetaChat、OpenROAD-MCP；每项均有论文或官方代码一手证据。
- Top 3 对抗性审查：PhIDO/PhIDO-Agentic、AutoPhotonicDesign、gdsfactory/gplugins。
- 关键判断：没有足够证据证明现有项目可直接满足全开源、可复现、物理可信的完整 PIC Design Agent Harness。
- 开源核验：区分 MIT/BSD/Apache/AGPL 等可识别许可证、公开但未识别根许可证、以及未发现公开仓库三种状态。
- 闭环核验：区分脚本生成、真实 Tool 接口、局部结果反馈和接近端到端的自动迭代。
- 未执行：未安装或运行外部候选，未做候选软件/论文实验复现，未启动 L01 最终综述或 `TASK-005`，未实施任何 Agent/MCP/仿真功能。
- GPT 主对话审查：`ACCEPT`，并给出 `TASK-005` 草案；是否实际启动仍由用户决定。
- Qwen 渠道纠正：初次 `qwen -c` 错误恢复了 `AI协同` 会话；随后已在项目主对话完成只读复核。该错误及修正均记录在 `references/task-004/search-log.md`。
