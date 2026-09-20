# Paper2Agent 候选技术记录

状态：`FORMAL RESEARCH CANDIDATE`，归属 `03 Agentic PIC Design`。

核验日期：2026-09-20。

本轮边界：只读论文与固定源码提交；未安装、未执行、未复现实验，也未生成或接入任何 PIC Tool/MCP。

## 1. 技术定位

**候选问题：能否将具有参考代码和可验证结果的 PIC 科学计算方法，半自动转化为受控、可测试、可追溯的 Agent Tools？**

Paper2Agent 处理的核心对象不是“论文文本问答”，而是论文背后的可执行研究资产。论文把 manuscript、supplement、code、data、tutorial 和 workflow 作为研究输出的一部分，并将可执行功能封装为 MCP 工具，再由 paper-specific agent 使用。[论文正式版本](https://doi.org/10.1038/s41586-026-11044-y)

当前公开仓库进一步把交付物分成两部分：[Paper2Skill](https://github.com/jmiao24/Paper2Agent/tree/8c2d059165ef8cdcb70dbea76655b9c2b55b38e6/skills/paper2agent/paper2skill) 从论文生成面向 Agent 的知识 Skill；[Paper2MCP](https://github.com/jmiao24/Paper2Agent/blob/8c2d059165ef8cdcb70dbea76655b9c2b55b38e6/skills/paper2agent/paper2mcp/SKILL.md) 从代码仓库构建并验证 MCP Server。组合模式输出论文 Skill、测试后的 MCP Server 及安装说明。

| 问题 | 核验结论 | 证据等级 |
|---|---|---|
| 输入是什么 | 论文可以用于知识提取；生成可执行工具仍依赖可定位、可运行的代码、数据、教程或工作流，以及相应环境 | `FACT / CODE VERIFIED` |
| 输出是什么 | 论文方法输出 paper-specific MCP Server 与 Agent；当前仓库输出 Skill 和测试后的 MCP Server 包 | `FACT / CODE VERIFIED` |
| 解决什么问题 | 将已有科学代码转成 Agent 可调用、可复用、带测试证据的工具，并改善计算工作流复用 | `FACT` |
| 是否是完整科研自动化 | 不是。它可支持计算、分析与多 Agent 科研案例，但不能自动证明新科学方法、物理模型或制造约束正确 | `FACT / INFERENCE` |

## 2. 技术路线

### 2.1 论文报告的构建流程

论文方法依次执行：定位并下载代码库；建立隔离环境；发现并分类教程；用示例数据运行与审计教程；抽取可复用函数并生成 MCP 工具和测试；最后组装带 manifest、版本信息和基础安全默认值的 MCP Server。`AUTHOR CLAIM`：失败的测试最多自动修复六次，仍失败的工具被排除并保留日志。

论文的自动测试覆盖三类参考结果：期望文件是否存在；数值结果是否在 3% 浮点容差内；图像感知哈希的 Hamming distance 是否小于 20。它们验证的是对教程或参考运行的再现，不能单独证明科学模型或物理设置正确。

### 2.2 当前源码可见机制

固定核验提交：[`8c2d059165ef8cdcb70dbea76655b9c2b55b38e6`](https://github.com/jmiao24/Paper2Agent/tree/8c2d059165ef8cdcb70dbea76655b9c2b55b38e6)，提交日期 2026-09-17；根许可证为 [MIT](https://github.com/jmiao24/Paper2Agent/blob/8c2d059165ef8cdcb70dbea76655b9c2b55b38e6/LICENSE)。本轮只读源码，没有运行。

| 环节 | 当前源码中的机制 | 证据等级 |
|---|---|---|
| 定位可执行代码 | 先运行上游仓库、发现教程/示例，再建立可封装功能清单；工具必须绑定现有代码，禁止凭空发明科学功能 | `CODE VERIFIED` |
| 功能提取 | 优先直接调用上游 Python API、脚本或 CLI；只写最小 wrapper，避免重写算法 | `CODE VERIFIED` |
| Tool Contract | 使用带描述的 typed 参数、枚举选择、默认值及结构化返回；要求保留标识符、单位、假设和原生 artifact | `CODE VERIFIED` |
| 环境与数据 | 记录依赖、源码 commit/tree hash、参考运行、数据与 artifact；允许为上游项目建立隔离环境 | `CODE VERIFIED` |
| 测试与失败处理 | 实现者先测试，再由不同 verifier 用新输入、错误输入和上游直接调用做独立比较；失败必须保留，不能降低测试强度掩盖 | `CODE VERIFIED` |
| MCP 暴露 | 生成 stdio MCP Server；[`verify_mcp_server.py`](https://github.com/jmiao24/Paper2Agent/blob/8c2d059165ef8cdcb70dbea76655b9c2b55b38e6/skills/paper2agent/paper2mcp/scripts/verify_mcp_server.py) 检查工具清单、输入 schema、接受调用、artifact、错误和超时 | `CODE VERIFIED` |
| 追溯 | workflow state 记录源码版本、agent 身份、reference/test artifact、hash、排除项和验证结果 | `CODE VERIFIED` |

### 2.3 Tool Contract、测试与运行的关系

```text
上游论文资产与源码
→ 参考运行和结果
→ 最小 Tool Contract / wrapper
→ 单元与独立对照验证
→ MCP transport/runtime 验证
→ Agent 调用
```

每一层只支持下一层的局部结论：schema 正确不代表工具运行正确；工具运行正确不代表与上游结果一致；与单个参考结果一致不代表模型适用于新设计；以上全部通过也不代表 PIC 物理、PDK 或制造约束正确。

## 3. 实际做到的程度

下表均为论文作者报告，本项目未复算。

| 评价范围 | 样本与成功判据 | 作者报告 | 适用边界 |
|---|---|---|---|
| 计算生物学 | 100 篇论文；成功定义为工具抽取、执行和自动验证端到端完成且无需人工介入 | 74/100 篇完成 agentification；599 个候选工具中 593 个通过自动验证 | 失败主要涉及缺少可执行代码、数据/模型 artifact、环境依赖或脚本难以泛化 |
| 教程衍生问题 | 300 个问题 | Paper2Agent + Claude Sonnet 4：91.2±1.6%；Claude + repository：80.3±2.3% | 模型、题目和评分设置特定；不能迁移为 PIC 成功率 |
| 非生物学代码库 | 10 个学科项目、42 个任务、每项 5 次运行 | 98.1±0.8% | 列出的领域不包含 PIC、EDA 或专业光子仿真 |
| 数据发现/综合 | 26 篇 data/discovery paper、100 个综合问题 | 89.0±3.1%；browser baseline 82.0±3.8% | 属于作者报告的信息综合评价，不是物理验证 |

`FACT`：论文讨论部分明确承认，不是每篇论文都能可靠 agentify；代码、文档、环境不完整会失败，开放式推理仍需要 human-in-the-loop，并存在维护、安全、知识产权和归属问题。

`CODE VERIFIED`：当前仓库能看到用于工具构建、独立验证、MCP 运行检查和 artifact 追溯的程序化步骤。

`UNKNOWN`：本轮没有找到它对 PIC、EDA、PDK、COMSOL、Lumerical、gdsfactory 或 SAX 的公开验证；也没有找到通用的多日求解、持久 checkpoint、许可证调度和中断恢复证据。多步骤工具组合不等于已支持有状态、长时间运行的专业仿真任务。

## 4. PIC 迁移缺口与风险

| 类型 | 观察或待验证项 | 当前判断 |
|---|---|---|
| 已观察缺口 | 论文的大规模实验中 26/100 个计算生物学项目未端到端成功，原因包括代码、数据、模型 artifact 或环境不完整 | 没有完整可执行研究资产时，自动转换的覆盖率受限；但不能据此断言所有缺代码论文都失败 |
| 已观察缺口 | 自动验证以文件、数值容差、图像相似度和上游直接调用为主 | 可证明参考行为一致性，不能自动验证端口定义、材料、网格、边界条件、收敛或制造约束 |
| 待验证风险 | COMSOL/Lumerical、云 API、license server、PDK 与受限数据 | 需要显式凭据边界、许可证合规、环境探测和不可用时的安全失败；原项目是否完整支持尚无 PIC 证据 |
| 待验证风险 | Tool 输入输出的类型、单位与物理语义 | Python 类型和描述是基础，但 PIC 还需单位、坐标系、端口、偏振、波长、材料来源、网格及适用域约束 |
| 待验证风险 | 原论文参考结果对新设计的外推 | 教程回归通过只能说明复现一个参考点；新拓扑、新工艺或参数域需要独立物理验证和适用域检查 |
| 待验证风险 | 自动生成代码的执行权限与资源消耗 | 应限制命令、文件、网络、求解预算和输出位置，并对未知代码采取隔离、人工审阅和可终止执行 |
| 待验证风险 | 来源、版本、测试与人工介入的追溯 | 当前 workflow state 提供了良好起点；PIC 仍需把 solver/PDK/license/config/raw result 纳入统一 Evidence Ledger |
| 待验证风险 | 与直接复用成熟 API 的成本比较 | 自动生成可能减少长尾方法接入成本，也可能增加审查、环境修复和维护成本；必须与手写少量 typed wrapper 做对照 |

## 5. 与现有对象的关系

| 对象 | 已有重点 | Paper2Agent 可能补充的层 | 不能替代 |
|---|---|---|---|
| PhIDO / PhIDO-Agentic | 自然语言 PIC 设计、结构化电路表示与工具编排 | 把新的、已有代码支持的科学方法封装成可调用工具 | PIC 需求理解、设计表示和领域编排本身 |
| AutoPhotonicDesign | Coding Agent 调用真实求解器执行器件级优化 | 将可复用求解/分析步骤固化为带契约、测试和来源的工具 | 优化策略、求解器真实性和器件物理验证 |
| gdsfactory + gplugins | 成熟 PIC 设计、版图和仿真 API 生态 | 从教程/项目中发现长尾可复用步骤并建立追溯测试 | 成熟 API 本身；稳定场景可能直接手写 wrapper 更简单 |
| PICBench | 光子电路生成任务与 simulator-based 评价 | 为 benchmark 提供可追溯工具构建和参考行为证据 | PIC 任务集、golden reference、评分器和物理评价 |

`INFERENCE`：Paper2Agent 最独特的候选位置是 Reference Architecture 中的“科学方法/代码 → Tool Registry/Adapter”接入过程。它补充的是新工具如何被构建和验证，不重复 Planner、PIC benchmark 或确定性求解器。

## 6. Research Gap → Our Entry Point

### 候选研究问题

能否将具有参考代码和可验证结果的 PIC 科学计算方法，半自动转化为受控、可测试、可追溯的 Agent Tools？

### 更简单的替代方案

直接选择 gdsfactory、SAX 等成熟接口，人工编写 2–3 个最小 Typed Tool Contract，并保留版本、输入、原始输出和测试记录，可能已经满足早期研究需求。自动工具生成只有在以下指标上优于这一基线时才值得成为后续研究对象：

- 首次接入与维护工时；
- Tool Contract 缺陷率和参数/单位遗漏率；
- 参考行为复现率及新输入错误检出率；
- 来源、版本、测试和人工修正的可追溯性；
- Agent 任务正确率、失败可诊断性、运行成本和资源风险。

### 当前结论

Paper2Agent 现作为“科学计算工具自动构建与验证”正式候选机制纳入 `03 Agentic PIC Design`。它不是既定技术路线或核心创新点。本项目尚未证明其能构建 PIC 专业工具、验证物理模型或制造约束，也不把论文作者报告的成功率迁移到 PIC 场景。是否开展对照实验，须由后续任务和用户另行授权。
