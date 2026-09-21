# 论文与项目出处索引

本页把调研中的“论文”和“软件项目”分开登记。论文标题或项目名均可直接点击进入一手出处；存在代码时另列官方仓库。仓库链接仅证明公开可访问，是否可复用仍以许可证与固定提交核验为准。

## Zotero 导入记录

| 项目 | 结果 |
|---|---|
| 可信论文记录 | 32 条：DAS 8、光子人工智能计算 12、Agentic PIC / 方法 12 |
| Zotero 已有 | 1 条：PhIDO / *AI agents for photonic integrated circuit design automation* |
| 已导入 | 31 条新增；与既有 PhIDO 合计 36 个顶层论文条目 |
| 明确排除 | PhIDO-Agentic 数据集 DOI `10.5683/SP4/T5QU9C`；纯仓库/官方文档；无可验证书目信息的项目 |
| 本地预检文件 | `references/task-006/zotero-import-ids.txt`；`references/task-006/zotero-import-dry-run/task-006-zotero-import.ris` |

RIS 共 32 条，`TY` 与 `ER` 记录数一致；已按四个中文主分类完成 Zotero 写入。Zotero API 核验顶层条目 36 个、题名唯一 36 个。

### 建议写入位置

| Zotero 现有收藏夹 | 记录 | 预计新增 |
|---|---:|---:|
| `02_光子芯片设计自动化` | PhIDO、AutoPhotonicDesign、PICBench、PICopilot、PICasso | 4（PhIDO 已存在） |
| `03_AI智能体与设计代理` | MetaChat、evo-metaoptics、FermiLink、MCP4EDA、RTLFixer、Paper2Agent、Scientific Agent Skills | 7 |
| `06_DAS与光纤传感` | 本页 DAS 论文 8 条 | 8 |
| `07_光计算与AI芯片` | 本页光子人工智能计算论文 12 条 | 12 |

合计新增 31 条，写入目标为上述四个中文主分类；英文分类尚未删除。

## 面向智能体的 PIC 设计与方法论文

| 对象 | 论文出处 | 官方仓库 | 说明 |
|---|---|---|---|
| [PhIDO](https://doi.org/10.1063/5.0300741) | APL Machine Learning, 2025 | [PhIDO-Release `6a8b8d6`](https://github.com/JPPhotonics/PhIDO-Release/tree/6a8b8d695f0af9247db1a9bbe0511307a8301b4d) | Zotero 已有；MIT |
| [AutoPhotonicDesign](https://arxiv.org/abs/2606.00915) | arXiv:2606.00915 | [固定提交 `3b26505`](https://github.com/flexcompute/autophotonicdesign/tree/3b265056586a2923b58f60fd9efe73530a03b1d4) | 预印本；MIT |
| [PICBench](https://arxiv.org/abs/2502.03159) | arXiv:2502.03159 | [固定提交 `ae1fb90`](https://github.com/PICDA/PICBench/tree/ae1fb905860bcfcc9a6c439795911266414274ff) | 预印本；MIT |
| [PICopilot](https://arxiv.org/abs/2608.01791) | arXiv:2608.01791 | 未核验到公开实现 | 预印本 |
| [PICasso](https://arxiv.org/abs/2608.26113) | arXiv:2608.26113 | 未核验到公开实现 | 预印本 |
| [MetaChat](https://doi.org/10.1126/sciadv.adx8006) | Science Advances, 2025 | [固定提交 `e66dedb`](https://github.com/jonfanlab/metachat/tree/e66deddbc96e4fe3e78837e069c44a4d15cf558c) | 未发现根许可证 |
| [evo-metaoptics](https://doi.org/10.1002/lpor.71739) | Laser & Photonics Reviews, 2026 | [官方仓库](https://github.com/yi-huang-1/evo-metaoptics) | MIT；当前调研未固定提交 |
| [FermiLink](https://arxiv.org/abs/2604.03460) | arXiv:2604.03460 | [官方仓库](https://github.com/TaoELi/FermiLink) | AGPL-3.0；当前调研未固定提交 |
| [MCP4EDA](https://arxiv.org/abs/2507.19570) | arXiv:2507.19570 | [官方仓库](https://github.com/NellyW8/MCP4EDA) | 未识别根许可证 |
| [RTLFixer](https://arxiv.org/abs/2311.16543) | arXiv:2311.16543 | [官方仓库](https://github.com/NVlabs/RTLFixer) | MIT；当前调研未固定提交 |
| [Paper2Agent](https://doi.org/10.1038/s41586-026-11044-y) | Nature, 2026 | [固定提交 `8c2d059`](https://github.com/jmiao24/Paper2Agent/tree/8c2d059165ef8cdcb70dbea76655b9c2b55b38e6) | MIT |
| [Scientific Agent Skills](https://arxiv.org/abs/2609.00065) | arXiv:2609.00065 | [官方仓库](https://github.com/K-Dense-AI/claude-scientific-skills) | 方法引用；不作为 PIC 实现证据 |

## DAS 光电混合集成论文

| 对象 | 论文出处 | 定位 |
|---|---|---|
| [硅光集成 DAS 解调器](https://doi.org/10.1364/PRJ.512298) | Photonics Research, 2024 | SOI 集成 interrogator 主基线 |
| [超高消光比硅基电光调制器](https://doi.org/10.1038/s41467-023-43244-9) | Nature Communications, 2023 | 器件/子模块证据 |
| [通信相干收发芯片用于声学传感](https://arxiv.org/abs/2306.04199) | arXiv:2306.04199, 2023 | 预印本/会议级 proof-of-concept |
| [双微梳并行 DAS](https://doi.org/10.1126/sciadv.adf8666) | Science Advances, 2024 | 高性能系统基线 |
| [混合集成双波长激光与 φ-OFDR](https://doi.org/10.1364/OFC.2025.Tu2K.5) | OFC 2025 | 会议论文；对应 arXiv:2411.00237 |
| [InP–SOI 混合集成解调器](https://doi.org/10.1364/OFC.2026.W4D.2) | OFC 2026 | 会议短文 |
| [1007 km DAS 非 PIC 反例](https://doi.org/10.1109/JLT.2022.3219369) | Journal of Lightwave Technology, 2022 | 距离不由 PIC 集成自然带来 |
| [PIC 光纤温度/应变传感阴性对照](https://doi.org/10.1364/OL.460314) | Optics Letters, 2022 | FBG interrogator，不是 Rayleigh DAS |

## 光子人工智能计算论文

| 对象 | 论文出处 | 代码/数据 |
|---|---|---|
| [微梳光子卷积加速器](https://doi.org/10.1038/s41586-020-03063-0) | Nature, 2021 | 未登记官方仓库 |
| [相变材料光子张量核](https://doi.org/10.1038/s41586-020-03070-1) | Nature, 2021 | 未登记官方仓库 |
| [可重构衍射处理器](https://doi.org/10.1038/s41566-021-00796-w) | Nature Photonics, 2021 | 未登记官方仓库 |
| [片上光子深度神经网络](https://doi.org/10.1038/s41586-022-04714-0) | Nature, 2022 | 未登记官方仓库 |
| [Netcast 分布式光子推理](https://doi.org/10.1126/science.abq8271) | Science, 2022 | [PubMed](https://pubmed.ncbi.nlm.nih.gov/36264813/) |
| [微梳集成光子处理单元](https://doi.org/10.1038/s41467-022-35506-9) | Nature Communications, 2023 | 未登记官方仓库 |
| [ACCEL 全模拟光电视觉](https://doi.org/10.1038/s41586-023-06558-8) | Nature, 2023 | [PMC 全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620079/) |
| [片上可训练衍射网络](https://doi.org/10.1038/s41467-024-50677-3) | Nature Communications, 2024 | 未登记官方仓库 |
| [Taichi 光子芯粒系统](https://doi.org/10.1126/science.adl1203) | Science, 2024 | [PubMed](https://pubmed.ncbi.nlm.nih.gov/38603505/) |
| [PACE 光电混合计算引擎](https://doi.org/10.1038/s41586-025-08786-6) | Nature, 2025 | 未登记官方仓库 |
| [通用光子人工智能加速器原型](https://doi.org/10.1038/s41586-025-08854-x) | Nature, 2025 | [官方代码与数据](https://github.com/lightmatter-ai/upaia-paper-2025) |
| [百层光子深度学习](https://doi.org/10.1038/s41467-025-65356-0) | Nature Communications, 2025 | 未登记官方仓库 |

## 纯项目与工具出处

这些对象用于 Tool Layer、Harness 或协议机制参照，不应作为论文记录导入 Zotero。

| 项目 | 官方地址 | 本轮核验状态 |
|---|---|---|
| [PhIDO-Agentic](https://github.com/JPPhotonics/PhIDO-Agentic/tree/4f4e671d0871188ff826273b1ad78d8a13180292) | 固定提交 `4f4e671` | MIT；无独立同行评审论文 |
| [gdsfactory](https://github.com/gdsfactory/gdsfactory/tree/4d31c842eb676abecd00e7b8e3a61c3883bfe6cd) | 固定提交 `4d31c84` | MIT；PIC Tool Layer |
| [gplugins](https://github.com/gdsfactory/gplugins/tree/adc7b6fae66cc86f3ac98b8695564a8dbc695e37) | 固定提交 `adc7b6f` | MIT；solver/process adapter |
| [OpenROAD-MCP](https://github.com/The-OpenROAD-Project/OpenROAD-MCP/tree/9dc80d3706fbcd8144cccb639fa21af7b933cbf5) | 固定提交 `9dc80d3` | BSD-3-Clause |
| [OpenROAD-Agent](https://github.com/OpenROAD-Assistant/OpenROAD-Agent) | 官方仓库 | BSD-3-Clause；论文标识待补 |
| [ChatEDA](https://github.com/wuhy68/ChatEDA) | 官方仓库 | Apache-2.0；论文标识待补 |
| [eda-agent](https://github.com/salitronic/eda-agent) | 官方仓库 | Apache-2.0；实验性项目 |
| [eda-agents](https://github.com/Mauricio-xx/eda-agents) | 官方仓库 | Apache-2.0；实验性项目 |
| [LangGraph](https://github.com/langchain-ai/langgraph) | 官方仓库 | MIT；通用编排参照 |
| [AutoGen](https://github.com/microsoft/autogen) | 官方仓库 | 代码 MIT；通用多智能体参照 |
| [Model Context Protocol Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 官方仓库 | MIT；Tool 协议参照 |

## 证据边界

- 论文链接证明出处，不证明作者指标已被本项目复算。
- 仓库公开不自动等于许可证允许复用；许可证未知的项目继续标记 `UNKNOWN`。
- 固定提交只表示本轮源码审查的版本边界；未固定提交的项目不得沿用 `CODE VERIFIED` 标签。
- Zotero 是文献管理层，不替代本仓库 Markdown 中的研究判断、证据标签与固定提交记录。
