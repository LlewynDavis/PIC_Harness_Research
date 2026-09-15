# TASK-004 Top 3 对抗性证据审查

方法：依照 `scientific-critical-thinking`，把“系统主张”拆成可观察因果链，检查选择偏差、
基线公平性、隐藏人工步骤、泛化、失败披露和代码能否复现。结论只针对公开证据。

## 1. PhIDO / PhIDO-Agentic

- **Demo 是否冒充完整自动设计**：baseline 确有 NL→DSL/DOT/YAML→GDS、SAX、KLayout
  代码链，不只是界面 Demo；但“DRC 通过”只是 demo PDK 规则，不等于 foundry signoff。
- **仿真是否由工具产生**：代码和 README 明确接 SAX，知识库含预计算 FDTD 数据；这是工具
  产生/消费的电路级结果，但不是每个候选都自动跑全波 Maxwell。
- **成功案例选择**：论文给出 102 prompts 和复杂度分层，优于只秀案例；pass@5 也说明单次
  可靠性不足。Agentic 后续尚缺同等级公开失败分布。
- **baseline 公平性**：公开摘要可支持模型间任务表现比较，但无法仅凭摘要确认所有模型预算、
  prompt、重试和工具权限完全一致；标为待正文逐表审计。
- **隐藏人工步骤**：baseline 有 guided 与 step-by-step 两种模式；Agentic 还明确有需求澄清和
  KG review queue。不能称全程无人工。
- **泛化**：只证明内置组件库/demo PDK/测试描述范围；未证明跨 PDK、未知拓扑、工艺角或大
  规模网表泛化。
- **开源复现**：MIT 仓库、依赖、测试表和关键代码可见；但 API keys、版本冲突、Agentic 的
  Neo4j/Clingo/Bedrock 依赖使“可看代码”与“一键复现论文”有距离。
- **审查结论**：是最相关的公开研究基线，但最高目标仍为“部分满足”。Agentic 的完整性目前
  主要由仓库自述和源码结构支持，不能把它的架构清单当成独立验证结果。

## 2. AutoPhotonicDesign

- **Demo 是否冒充系统**：存在固定 loop、实际脚本、各器件分支、journal 和 best design，超过
  一次性代码生成；但它解决的是已定义 objective 下的器件几何搜索，不是从系统需求综合 PIC。
- **仿真是否由工具产生**：明确提交 Tidy3D FDTD，读取 field/metric，并在 KLayout 做 DRC；
  这是本轮最强的真实 Tool→结果回读证据。
- **成功案例选择**：仓库报告八类结果并保留 journal，但公开 README 以最佳结果为主。需要读取
  每分支所有尝试、云任务 IDs、失败/费用后才能排除 survivor bias。
- **baseline 公平性**：需核对论文中人与优化器/不同 Agent 的相同仿真预算、初始设计和停止条件；
  README 的 headline 指标不足以证明优于经典 inverse design。
- **隐藏人工步骤**：人必须写 `program.md`，对新器件修改初始 `design.py` 和 `evaluate()`；路由
  分支还使用 PhotonForge。所谓无人工仅适用于配置完成后的循环。
- **泛化**：多器件分支提供一定 breadth，但没有证明同一未改模板可零样本覆盖新器件/PDK。
- **开源复现**：Harness MIT；Tidy3D 付费云/API key，PhotonForge 商业，故不是全栈开源路径。
- **审查结论**：非常值得复用“实验账本 + deterministic metric + keep/discard”模式；不可把
  器件级闭环外推为完整 PIC 自动设计或完全开源复现。

## 3. gdsfactory / gplugins

- **Demo 是否冒充 Agent**：官方定位是设计自动化与插件生态，不是 Agent。任何“Agent 能力”
  必须来自外部 planner/harness，不能由它的丰富 API 推断。
- **结果是否由真实工具产生**：版图/GDS、netlist 与开源或商业 solver/DRC adapter 是实接口；
  但 adapter 存在不等于环境已安装、任务已成功运行或结果物理可信。
- **成功案例选择与 baseline**：它不是以 Agent 成功率为主张的研究系统，Agent benchmark 问题
  不适用；应改审 API 稳定性、版本锁定、PDK 范围和 solver 一致性。
- **隐藏人工步骤**：组件定义、PDK、模型、端口、仿真配置与验收阈值都需要领域专家提供。
- **泛化**：可扩展性强，但跨 foundry/PDK 的可移植性受许可和工艺模型限制。
- **开源复现**：核心两个仓库均 MIT 且源码可见；Lumerical/Tidy3D 等某些后端不是开源，必须
  做 adapter 级许可证/成本标注。
- **审查结论**：是首选执行底座，不是现成 Harness。它降低工具实现成本，却没有解决需求理解、
  状态、迭代策略、失败恢复、证据治理或 benchmark 公平性。

## 共同风险

- “生成 GDS”不等于“通过 LVS/DRC/光学指标/工艺角/代工签核”。
- “调用 simulation API”不等于使用了正确模型、边界条件、网格收敛或材料参数。
- pass@k 会使用多次采样预算；不得与单次成功率直接比较。
- 成功任务数若不公开失败轨迹、人工修订和总预算，会高估自动性。
- 开放仓库但无许可证，不满足可合法复用意义上的“开源”。
