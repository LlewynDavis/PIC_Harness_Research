# TASK-007 引用与链接核查

核查日期：2026-09-21

## 核查方法

1. 从正式报告提取全部外部链接和相对 Markdown 链接。
2. DOI 通过 Crossref REST API 核对题名、年份和期刊/会议；arXiv DOI 不在 Crossref 的条目通过 DOI 解析与 arXiv 落地页核对。
3. arXiv 和 GitHub 链接以 HTTP 状态和最终落地地址核对。
4. 正式报告的相对链接以本地解析后的真实路径核对。
5. 链接可访问只证明出处存在，不证明论文指标已复算、代码可运行或物理结论已复现。

## Crossref 已核对 DOI

| DOI | Crossref 题名（简写） | 年份 | 载体 | 结果 |
|---|---|---:|---|---|
| `10.1063/5.0300741` | AI agents for photonic integrated circuit design automation | 2025 | APL Machine Learning | 匹配 |
| `10.1364/PRJ.512298` | Silicon photonic integrated interrogator for fiber-optic DAS | 2024 | Photonics Research | 匹配 |
| `10.1364/OFC.2026.W4D.2` | Hybrid Photonic Integrated Interrogator for DAS | 2026 | OFC 2026 | 匹配 |
| `10.1364/OFC.2025.Tu2K.5` | Dual-Wavelength φ-OFDR using a hybrid-integrated laser | 2025 | OFC 2025 | 匹配 |
| `10.1038/s41467-023-43244-9` | On-chip silicon electro-optical modulator ... DAS | 2023 | Nature Communications | 匹配 |
| `10.1126/sciadv.adf8666` | Coherently parallel DAS using dual Kerr soliton microcombs | 2024 | Science Advances | 匹配 |
| `10.1038/s41586-020-03063-0` | 11 TOPS photonic convolutional accelerator | 2021 | Nature | 匹配 |
| `10.1038/s41586-020-03070-1` | Integrated photonic tensor core | 2021 | Nature | 匹配 |
| `10.1038/s41566-021-00796-w` | Reconfigurable diffractive processing unit | 2021 | Nature Photonics | 匹配 |
| `10.1038/s41586-022-04714-0` | On-chip photonic deep neural network | 2022 | Nature | 匹配 |
| `10.1126/science.abq8271` | Delocalized photonic deep learning ... edge | 2022 | Science | 匹配 |
| `10.1038/s41467-022-35506-9` | Microcomb-based integrated photonic processing unit | 2023 | Nature Communications | 匹配 |
| `10.1038/s41586-023-06558-8` | All-analog photoelectronic chip | 2023 | Nature | 匹配 |
| `10.1038/s41467-024-50677-3` | On-chip diffractive optics with in situ training | 2024 | Nature Communications | 匹配 |
| `10.1126/science.adl1203` | Photonic chiplet Taichi | 2024 | Science | 匹配；题名中的 AGI/TOPS-W 不作为本报告事实外推 |
| `10.1038/s41586-025-08786-6` | Integrated large-scale photonic accelerator | 2025 | Nature | 匹配 |
| `10.1038/s41586-025-08854-x` | Universal photonic AI acceleration | 2025 | Nature | 匹配 |
| `10.1038/s41467-025-65356-0` | Hundred-layer photonic deep learning | 2025 | Nature Communications | 匹配 |
| `10.1126/sciadv.adx8006` | Multi-agentic autonomous freeform metasurface design | 2025 | Science Advances | 匹配 |
| `10.1038/s41586-026-11044-y` | Reimagining research papers as ... AI agents | 2026 | Nature | 匹配 |

## arXiv / DOI 解析与仓库链接

| 链接 | HTTP / 解析结果 | 用途 |
|---|---|---|
| `arXiv:2306.04199` | 200 | 通信相干 PIC 复用 |
| `arXiv:2502.03159` | 200 | PICBench |
| `arXiv:2606.00915` | 200 | AutoPhotonicDesign |
| `arXiv:2608.01791` | 200 | PICopilot |
| `arXiv:2608.26113` | 200 | PICasso |
| `10.48550/arXiv.2609.00065` | DOI 200，解析到 arXiv | Scientific Agent Skills 方法引用；Crossref 404 属注册体系差异，不是坏 DOI |
| `github.com/gdsfactory/gdsfactory` | 200 | Tool Layer 官方仓库 |
| `github.com/gdsfactory/gplugins` | 200 | solver/process adapter 官方仓库 |
| `github.com/The-OpenROAD-Project/OpenROAD-MCP` | 200 | EDA Tool Contract 参照 |

## 本地引用

正式报告中的 9 个相对 Markdown 链接均解析为仓库内现存文件，包括 TASK-007 检索/审计/术语/路线文件、TASK-006 论文与来源索引，以及 TASK-005 技术地图、能力矩阵和参考架构。

## 未完成与边界

- 没有对全部 32 篇论文做逐条参考文献格式化或逐篇全文复现。
- Crossref 题名匹配不代表论文全文开放。
- 本轮没有验证付费墙后的所有补充材料、原始数据和实验代码。
- 只有 TASK-004/005/006 已记录的固定提交可沿用 `CODE VERIFIED`；官网最新主分支不能自动继承该标签。

