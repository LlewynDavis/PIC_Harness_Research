# 一手证据与来源

## DAS 光电混合集成 × 面向智能体的 PIC 设计

下列论文证明 DAS 光子芯片和子模块的物理基线，不证明人工智能已经完成相关设计。人工智能任务映射属于本项目 `INFERENCE（推论）`，必须由后续受控实验验证。

| 对象 | 来源 | 本轮用途 | 证据边界 |
|---|---|---|---|
| Jin et al., 2024 | [Photonics Research](https://doi.org/10.1364/PRJ.512298) | SOI integrated interrogator 主基线 | 指标为作者报告；未复现实验 |
| Cheng et al., 2023 | [Nature Communications](https://doi.org/10.1038/s41467-023-43244-9) | 高 ER EOM 与真实 DAS A/B | 器件/子模块，不是完整 interrogator |
| Sandmann et al., 2023 | [arXiv:2306.04199](https://arxiv.org/abs/2306.04199) | 通信 coherent PIC 复用 | 预印本/会议级 proof-of-concept |
| Li et al., 2024 | [Science Advances](https://doi.org/10.1126/sciadv.adf8666) | 双微梳并行 DAS | 高性能但系统复杂度高 |
| Idjadi et al., 2025 | [OFC](https://doi.org/10.1364/OFC.2025.Tu2K.5) / [arXiv:2411.00237](https://arxiv.org/abs/2411.00237) | 混合集成双波长激光 + 37 km φ-OFDR | 会议证据；大量片外组件 |
| Jin et al., 2026 | [OFC](https://doi.org/10.1364/OFC.2026.W4D.2) | InP–SOI hybrid interrogator | 会议短文，长期稳定性/完整 BOM 不明 |
| Ip et al., 2022 | [JLT](https://doi.org/10.1109/JLT.2022.3219369) | 1007 km 非 PIC 反例 | 证明距离不由 PIC 集成自然带来 |
| Lin & Shi, 2022 | [Optics Letters](https://doi.org/10.1364/OL.460314) | FBG interrogator negative control | 不是 Rayleigh DAS |

## 光子人工智能计算（Photonic AI Computing）

| 对象 | 来源 | 本轮用途 | 证据边界 |
|---|---|---|---|
| Xu et al., 2021 | [Nature](https://doi.org/10.1038/s41586-020-03063-0) | 微梳卷积基线 | 混合系统，非完整片上 CNN |
| Feldmann et al., 2021 | [Nature](https://doi.org/10.1038/s41586-020-03070-1) | PCM 光子 tensor core | 核指标不等于完整推理吞吐 |
| Zhou et al., 2021 | [Nature Photonics](https://doi.org/10.1038/s41566-021-00796-w) | 自由空间可重构 DPU | 非 PIC；对准和数据加载边界 |
| Ashtiani et al., 2022 | [Nature](https://doi.org/10.1038/s41586-022-04714-0) | 片上 PDNN 与非线性 | 小规模任务，外部控制仍重要 |
| Sludds et al., 2022 | [Science / PubMed](https://pubmed.ncbi.nlm.nih.gov/36264813/) | Netcast 分布式推理 | 40 aJ 是接收端光能，不是墙插总能耗 |
| Bai et al., 2023 | [Nature Communications](https://doi.org/10.1038/s41467-022-35506-9) | 微梳 + MRR 权重库 | 原型实耗与未来集成投影必须分开 |
| Chen et al., 2023 | [Nature / PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620079/) | ACCEL 全模拟光电视觉 | 任务专用，operation 口径不可直接等同数字 MAC |
| Cheng et al., 2024 | [Nature Communications](https://doi.org/10.1038/s41467-024-50677-3) | TDONN 片上原位训练 | 输入预处理、FPGA/TEC 与热功耗仍存在 |
| Xu et al., 2024 | [Science / PubMed](https://pubmed.ncbi.nlm.nih.gov/38603505/) | Taichi chiplet | “AGI”是作者定位，不是通用智能验证 |
| Hua et al., 2025 | [Nature](https://doi.org/10.1038/s41586-025-08786-6) | PACE 大规模混合封装 | Ising 专用任务，不是通用 DNN |
| Ahmed et al., 2025 | [Nature](https://doi.org/10.1038/s41586-025-08854-x) / [官方代码与数据](https://github.com/lightmatter-ai/upaia-paper-2025) | 真实模型与完整软件/硬件系统 | 不同任务精度损失差异大 |
| Zhou et al., 2025 | [Nature Communications](https://doi.org/10.1038/s41467-025-65356-0) | 深层模型映射 | 单层芯片复用，不是数百物理层单片集成 |

## 面向智能体的 PIC 设计（Agentic PIC Design）

- [TASK-005 技术地图与对象拆解](/technical-map-and-objects.html)
- [TASK-005 能力与验证矩阵](/capability-and-verification-matrix.html)
- [TASK-005 参考架构 V0](/reference-architecture-v0.html)
- [TASK-005 研究缺口与路线种子](/research-gaps-and-route-seeds.html)

2026-09-20 远程主分支只读核对：PhIDO `6a8b8d6`、PhIDO-Agentic `4f4e671`、AutoPhotonicDesign `3b26505`、PICBench `ae1fb90`、Paper2Agent `8c2d059` 与既有记录一致；gdsfactory/gplugins 已分别更新为 `19e65ad` / `b454f1e`，最新差异未逐行重审，不能沿用旧提交的 `CODE VERIFIED（源码核验）` 标签覆盖新增内容。

| 对象 | 来源 | 本轮用途 | 证据边界 |
|---|---|---|---|
| Paper2Agent 论文 | [Nature 正式版本](https://doi.org/10.1038/s41586-026-11044-y) | 核验问题定义、构建流程、评价样本、成功判据、结果与限制 | 论文结果为 `AUTHOR CLAIM`；本项目未复算，不能迁移为 PIC 成功率 |
| Paper2Agent 源码 | [GitHub 固定提交 `8c2d059`](https://github.com/jmiao24/Paper2Agent/tree/8c2d059165ef8cdcb70dbea76655b9c2b55b38e6) | 核验当前 Skill/MCP 构建流程、Tool Contract、验证脚本、追溯字段与许可证 | `CODE VERIFIED` 仅表示只读源码可见；未安装、未执行、未验证物理正确性 |

## 方法引用

本轮对抗性证据审查使用：Kassis, T., Agarwal, V., He, Y., Patel, D., & Brueckner, A. M. (2026). *Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents*. arXiv:2609.00065. [DOI](https://doi.org/10.48550/arXiv.2609.00065).

该方法引用说明审查程序来源，不为任何 PIC 物理结论背书。
