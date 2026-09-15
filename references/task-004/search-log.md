# TASK-004 检索与核验日志

检索日期：2026-09-15（Asia/Shanghai）

## 方法

本轮按 `nature-academic-search` 的多源发现与去重路径执行：先用题名、DOI、arXiv
号定位论文，再以作者/项目官方仓库核验代码可见性、许可证和关键文件。去重优先使用
DOI / arXiv，项目则使用 canonical GitHub 仓库。`nature-reader` 只用于 Top 候选的
定向问题阅读，没有生成大规模全文翻译。对 Top 3 使用
`scientific-critical-thinking` 检查选择偏差、基线公平性、隐藏人工步骤、泛化和可复现性。

外部来源只作为公开证据；本轮没有运行任何候选代码或仿真，因此“仓库可见”不等于
“已在本机复现”。

## 主要检索词

- `"AI agents" "photonic integrated circuit" design automation`
- `PICopilot photonic integrated circuit script generation`
- `photonic design agent gdsfactory simulation loop`
- `silicon photonics LLM agent GDS DRC SAX`
- `agentic photonic inverse design FDTD`
- `EDA agent real tool simulation CAD RTL-to-GDS`
- `MCP EDA OpenROAD Yosys OpenLane`
- `scientific simulation agent framework autonomous loop`
- `LangGraph state checkpoint human in the loop`
- `AutoGen multi-agent tool use framework`

## 来源层级与类型规则

- 同行评审：出版社页/DOI 与论文正文优先。
- 预印本：arXiv 摘要和正文；不把预印本当成同行评审。
- 项目：官方 GitHub 仓库的 README、目录、关键源码和根许可证。
- 商业依赖：明确标出，即使调用它的 Harness 代码本身有开源许可证。
- “开源”：必须看到公开源码和可识别许可证；只有 README、论文口头声明或无许可证的
  公开代码，分别记作“材料可见”或“source-available，许可证未核实”。

## 关键一手来源

- PhIDO：论文 [arXiv:2508.14123](https://arxiv.org/abs/2508.14123)、
  [DOI 10.1063/5.0300741](https://doi.org/10.1063/5.0300741)、
  [MIT 仓库](https://github.com/JPPhotonics/PhIDO-Release)。
- PhIDO-Agentic：[官方仓库](https://github.com/JPPhotonics/PhIDO-Agentic)、
  [架构文档](https://github.com/JPPhotonics/PhIDO-Agentic/blob/main/ARCHITECTURE.md)、
  [数据 DOI](https://doi.org/10.5683/SP4/T5QU9C)。
- PICopilot：[arXiv:2608.01791](https://arxiv.org/abs/2608.01791)。
- PICasso：[arXiv:2608.26113](https://arxiv.org/abs/2608.26113)。
- AutoPhotonicDesign：[arXiv:2606.00915](https://arxiv.org/abs/2606.00915)、
  [MIT 仓库](https://github.com/flexcompute/autophotonicdesign)。
- PICBench：[arXiv:2502.03159](https://arxiv.org/abs/2502.03159)、
  [MIT 仓库](https://github.com/PICDA/PICBench)。
- gdsfactory / gplugins：[gdsfactory](https://github.com/gdsfactory/gdsfactory)、
  [gplugins](https://github.com/gdsfactory/gplugins)。
- MetaChat：[Science Advances DOI](https://doi.org/10.1126/sciadv.adx8006)、
  [arXiv:2503.20479](https://arxiv.org/abs/2503.20479)、
  [官方代码](https://github.com/jonfanlab/metachat)。
- evo-metaoptics：[DOI 10.1002/lpor.71739](https://doi.org/10.1002/lpor.71739)、
  [MIT 仓库](https://github.com/yi-huang-1/evo-metaoptics)。
- FermiLink：[arXiv:2604.03460](https://arxiv.org/abs/2604.03460)、
  [AGPL-3.0 仓库](https://github.com/TaoELi/FermiLink)。
- MCP4EDA：[arXiv:2507.19570](https://arxiv.org/abs/2507.19570)、
  [公开但未识别根许可证的仓库](https://github.com/NellyW8/MCP4EDA)。
- OpenROAD：[OpenROAD-MCP](https://github.com/The-OpenROAD-Project/OpenROAD-MCP)、
  [OpenROAD-Agent](https://github.com/OpenROAD-Assistant/OpenROAD-Agent)。
- ChatEDA：[Apache-2.0 仓库](https://github.com/wuhy68/ChatEDA)。
- RTLFixer：[arXiv:2311.16543](https://arxiv.org/abs/2311.16543)、
  [MIT 仓库](https://github.com/NVlabs/RTLFixer)。
- 其他架构参考：[eda-agent](https://github.com/salitronic/eda-agent)、
  [eda-agents](https://github.com/Mauricio-xx/eda-agents)、
  [LangGraph](https://github.com/langchain-ai/langgraph)、
  [AutoGen](https://github.com/microsoft/autogen)、
  [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)。

## Qwen 中间材料边界

Qwen Code 0.22.3 / `qwen3.8-27b` 通过一个直接的只读科研会话完成了 25 项候选召回和
12 条检索词扩展，没有通过 Codex“AI协同”任务转发，也未修改仓库。其输出主动标为
“未经一手核验”。Codex 复核发现其中 PICopilot
年份、题名、仿真工具，以及 RTLFixer 仓库归属等字段存在错记，因此只采用了检索词和
候选提示，没有把 Qwen 字段直接作为事实。
