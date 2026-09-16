# TASK-005 一手证据与检索日志

检索与核验日期：2026-09-16（Asia/Shanghai）

## 证据纪律

本轮使用五类标签：

- `FACT`：可由论文元数据、许可证、仓库结构或官方文档直接确认；
- `AUTHOR CLAIM`：作者在论文或 README 中报告，但本项目没有复现实验；
- `CODE VERIFIED`：Codex 已在固定 commit 的公开源码中定位到实现；
- `INFERENCE`：基于多项一手证据作出的受限判断；
- `UNKNOWN`：现有公开材料不足，不能补全。

`CODE VERIFIED` 只表示实现可在源码中确认，不表示代码已在本机运行，更不表示物理正确、可制造或通过 foundry signoff。本轮没有执行候选系统、没有运行仿真，也没有产生本项目实验数据。

## Skill 路径

- `nature-academic-search`：用于多源定位与少量补证据，不进行新的大规模方向扫描；
- `nature-reader`：围绕 DesignSpec、Tool、solver、RESULT、state、verification 和 benchmark 定向精读正文；
- `scientific-critical-thinking`：只强审查会改变路线选择的结论；
- 未启动 `literature-review` 或 `nature-literature-pipeline`。

## 补充检索记录

| 日期 | 来源 | 检索词 | 用途 |
|---|---|---|---|
| 2026-09-16 | Volcengine web search | `PhIDO photonic integrated design optimization agent APL Photonics code` | 核对论文、DOI、官方仓库 |
| 2026-09-16 | Volcengine web search | `AutoPhotonicDesign agentic photonic design arxiv GitHub` | 核对预印本与官方仓库 |
| 2026-09-16 | Volcengine web search | `PICBench photonic integrated circuit benchmark arxiv GitHub` | 核对预印本、仓库和评价代码 |
| 2026-09-16 | Volcengine web search | `MetaChat photonic metamaterial design Science Advances code` | 核对同行评审论文、预印本与官方仓库 |

检索结果只用于定位。一切路线级判断均回到论文正文、固定 commit 源码或官方文档。

## 论文与项目快照

| 对象 | 一手论文/官方页 | 公开仓库 | 核验 commit | 许可证核验 | 本轮证据角色 |
|---|---|---|---|---|---|
| PhIDO | [arXiv:2508.14123](https://arxiv.org/abs/2508.14123)；[DOI 10.1063/5.0300741](https://doi.org/10.1063/5.0300741) | [JPPhotonics/PhIDO-Release](https://github.com/JPPhotonics/PhIDO-Release) | `6a8b8d695f0af9247db1a9bbe0511307a8301b4d` | 根 `LICENSE` 为 MIT | PIC 端到端结构生成基线 |
| PhIDO-Agentic | 未核验到独立同行评审论文 | [JPPhotonics/PhIDO-Agentic](https://github.com/JPPhotonics/PhIDO-Agentic) | `4f4e671d0871188ff826273b1ad78d8a13180292` | 根 `LICENSE` 为 MIT | typed contracts、MCP、门控状态机原型 |
| AutoPhotonicDesign | [arXiv:2606.00915](https://arxiv.org/abs/2606.00915) | [flexcompute/autophotonicdesign](https://github.com/flexcompute/autophotonicdesign) | `3b265056586a2923b58f60fd9efe73530a03b1d4` | 根 `LICENSE` 为 MIT | 真实 solver-in-the-loop 器件优化 |
| gdsfactory | [官方文档](https://gdsfactory.github.io/gdsfactory/) | [gdsfactory/gdsfactory](https://github.com/gdsfactory/gdsfactory) | `4d31c842eb676abecd00e7b8e3a61c3883bfe6cd` | 根 `LICENSE` 为 MIT | PIC Tool Layer |
| gplugins | [官方文档](https://gdsfactory.github.io/gplugins/) | [gdsfactory/gplugins](https://github.com/gdsfactory/gplugins) | `adc7b6fae66cc86f3ac98b8695564a8dbc695e37` | 根 `LICENSE` 为 MIT | solver/process adapter 层 |
| PICBench | [arXiv:2502.03159](https://arxiv.org/abs/2502.03159) | [PICDA/PICBench](https://github.com/PICDA/PICBench) | `ae1fb905860bcfcc9a6c439795911266414274ff` | 根 `LICENSE` 为 MIT | Evaluator / Benchmark Layer |
| OpenROAD-MCP | [官方 API 文档](https://github.com/The-OpenROAD-Project/OpenROAD-MCP/blob/main/docs/API.md) | [The-OpenROAD-Project/OpenROAD-MCP](https://github.com/The-OpenROAD-Project/OpenROAD-MCP) | `9dc80d3706fbcd8144cccb639fa21af7b933cbf5` | 根 `LICENSE` 为 BSD-3-Clause | 稳定 Tool Contract 与 session 参照 |
| MetaChat | [Science Advances DOI](https://doi.org/10.1126/sciadv.adx8006)；[arXiv:2503.20479](https://arxiv.org/abs/2503.20479) | [jonfanlab/metachat](https://github.com/jonfanlab/metachat) | `e66deddbc96e4fe3e78837e069c44a4d15cf558c` | **未发现根许可证文件** | 相邻领域的 agent + surrogate + optimization 参照 |
| PICopilot | [arXiv:2608.01791](https://arxiv.org/abs/2608.01791) | 未核验到公开实现 | — | — | 只保留论文级条件证据 |
| PICasso | [arXiv:2608.26113](https://arxiv.org/abs/2608.26113) | 未核验到公开实现 | — | — | 不作源码级结论 |

## 关键源码证据索引

### PhIDO / PhIDO-Agentic

- `PhIDO-Release/PhotonicsAI/Photon/webapp.py`：分阶段 session state、YAML/DSL、schematic、layout、SAX、DRC 流程；
- `PhIDO-Release/PhotonicsAI/Photon/DemoPDK.py`：`gf.read.from_yaml`、SAX circuit 构建、S 参数模型需求和基于 SAX 的优化；
- `PhIDO-Agentic/mcp_servers/models.py`：`UserRequirement`、`DesignIntent`、`CircuitDSL`、`PipelineFeedback` 等 Pydantic 数据契约；
- `PhIDO-Agentic/mcp_servers/pdk_catalog_server.py` 与 `schematic_builder_server.py`：`@mcp.tool()` 注册；
- `PhIDO-Agentic/mcp_servers/interpreter_agent.py`：真实 tool dispatch、tool result 回填与暂停/继续；
- `PhIDO-Agentic/mcp_servers/pipeline_orchestrator.py`：路由 retry、validation retry、统一 session、GDS/SAX/KLayout DRC 阶段；
- `PhIDO-Agentic/mcp_servers/clingo_validator.py`：Clingo 拓扑门；缺少 Clingo 时会降级；
- `PhIDO-Agentic/mcp_servers/ar_validator.py`：`AR_ENABLED`/凭据控制的增强验证；
- `PhIDO-Agentic/ARCHITECTURE.md`：作者明确记录外部服务依赖、no-op/降级和验证深度不足。

### AutoPhotonicDesign

- `program.md`：允许 coding agent 编辑的文件边界、固定执行步骤、DRC、simulate、keep/discard 和 30 次 FDTD 预算；
- `simulate.py`：调用 `tidy3d.web.run`，读取仿真数据并调用确定性 `evaluate`，异常写入 crash；
- `orchestrate.py`：从文本日志用正则抽取单一 metric，比较 best，执行 keep/discard/revert；
- `design.py`：材料、波长、source、monitor、grid 和边界等仿真设置；
- `drc.py`：GDS 导出与有限的 KLayout width/space 检查。

### gdsfactory / gplugins

- `gdsfactory/read/from_yaml.py`：YAML 读取后执行 `Netlist.model_validate`；
- `gdsfactory/schematic.py`、`pdk.py`、`cross_section/base.py`：Pydantic 模型和 `extra="forbid"` 约束；
- `gplugins/tidy3d/component.py`：`write_sparameters` 调用 `web.run`，保存 wavelength 与 S 参数；
- `gplugins/gmeep/`：Meep S 参数接口；
- `gplugins/common/base_models/simulation.py`：部分结构化仿真结果模型；
- `gplugins/klayout/`：KLayout 相关连接与 netlist 支持；
- `gplugins/pyproject.toml`：开源与商业 solver 的可选依赖并存。

### PICBench

- `PICBench/evaluation.py`：JSON 解析、模型映射、`sax.circuit`、1.51–1.59 μm/1000 点扫描和 golden response 比较；
- `compare_golden` 把每条响应四舍五入到 10 位后转为 set 比较，丢失端口对身份与顺序；
- `PICBench/gen_data.py`：标准组合公式的 pass@k 估计、错误反馈循环和输出日志；
- 评价止于 netlist/SAX 电路功能层，没有 GDS、DRC、LVS、full-wave 或 signoff。

### OpenROAD-MCP

- `ARCHITECTURE.md`：MCP server、manager、PTY session、命令白名单、Zod result types 与 snake_case wire boundary；
- `docs/API.md`：tool 参数、session 生命周期、结构化 response、history、metrics、ORFS stage/gate 汇总；
- 每种结果都有 nullable `error`，query/exec 分离，session 通过 `session_id` 保持连续；
- 它是数字 EDA 参照，不是 PIC 工具链，也不是自主 planner。

### MetaChat

- 论文第 5–7 页：AIM 通过标签解析反复调用工具、其他 agent 和用户；
- 论文第 11–14 页：FiLM WaveY-Net 用 270,000 条 FDFD ground-truth 训练，30,000 条测试集报告代理误差；
- 论文第 14–18 页：API 把 lens/deflector 目标映射到 FoM，代理求解器与自动微分优化；
- `metachat-aim/core/tools/base.py`：`ToolCall`/`BaseTool` 接口使用宽泛 `Any`，不是 typed scientific contract；
- `metachat-aim/agent/cot_iterative_tools.py`：registry、最多 20 次迭代、标签解析、tool output 回填；
- `metachat-aim/tools/design/api.py`：benchmark 侧 neural-design API 返回描述字符串，不能当作真实 solver 运行证据；
- `web-app/backend/tools/design/api.py`：真实 Docker/GPU job、进度监控、失败返回、结果文件和 gdspy GDS 导出；
- 该项目面向 metasurface，不是 PIC circuit；根许可证缺失，复用法律状态 `UNKNOWN`。

## Qwen 中间材料审计

本轮只复用既有 Qwen 项目主对话 `d6e85530-4e52-46ac-a5bf-6e798d92b214`，下达一次只读、六对象合并抽取任务，没有新建多余科研对话，也没有使用“AI协同”下达科研工作。Qwen 明确声明未执行 shell、未读本地源码、没有 `CODE VERIFIED` 项，因此其输出只作为缺口清单。

Codex 复核后的主要纠正：

- Qwen 把 PICBench 的 SAX 计算标成“物理仿真”；本报告纠正为 circuit-level evaluator；
- Qwen 对 OpenROAD-MCP 的 planner/agent 层判断过于简化；本报告将其限定为 Tool Contract/session 参照；
- Qwen 没有识别 MetaChat benchmark API stub 与 web backend 真实执行路径的差异；本报告分开处理；
- Qwen 提醒的 PhIDO-Agentic 门控降级、AutoPhotonicDesign 商业依赖和统一 RESULT 缺口，经源码复核后保留。

## 仍未完成的验证

- 没有运行任何候选仓库、solver、DRC 或 benchmark；
- 没有验证 PhIDO-Agentic 在所有可选门开启时的端到端可复现轨迹；
- 没有复算论文指标，也没有检查 AutoPhotonicDesign 所有分支的全部 journal；
- 没有获得 MetaChat 明确的开源许可证；
- 没有 foundry PDK、LVS deck、process corner 或 signoff 证据。
