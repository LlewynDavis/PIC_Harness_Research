# 检索记录

检索日期：2026-09-20；主要时间窗：2021–2026。

## 使用方法

- `nature-academic-search`：按多源搜索工作流建立候选池；OpenAlex fallback 因 HTTP 429 失败，未把其返回用于结论。
- `nature-reader`：定向阅读高价值论文的 HTML/PDF 正文，核对系统边界、外部组件、指标与限制。
- `scientific-critical-thinking`：对影响路线选择的主张检查反例、隐藏假设、失败模式、机会成本和简化替代。
- `literature-review`：在范围稳定后组织叙事综合；本轮不是系统综述或 meta-analysis。
- Qwen：通过项目主对话执行只读关键词扩展与候选整理；Codex 复核后才进入结论。

## DAS 查询

- `distributed acoustic sensing photonic integrated circuit`
- `distributed acoustic sensing silicon photonics`
- `integrated DAS interrogator`
- `coherent receiver distributed acoustic sensing silicon`
- `phase-sensitive OTDR integrated photonics`
- `coherent OTDR photonic integrated circuit`
- `distributed acoustic sensing integrated laser`
- `phi-OFDR hybrid-integrated laser`
- `distributed acoustic sensing microcomb`
- `ultra-high extinction ratio DAS modulator`

来源：Optica、Nature、Science Advances、IEEE Xplore、SPIE、arXiv、OFC/ICOCN 官方页面。直接组合检索在 arXiv 命中很少，不能据此推断领域为空；关键证据主要位于期刊和会议。

## Photonic AI 查询

- `photonic neural network interferometer chip inference`
- `MZI mesh photonic matrix multiplication AI accelerator`
- `microring resonator array photonic neural network inference`
- `microcomb photonic convolution accelerator`
- `diffractive optical neural network photonic chip`
- `optoelectronic hybrid photonic AI accelerator`
- `complete photonic inference system ResNet BERT`
- `photonic neural network in situ training`
- `system-level photonic accelerator energy ADC DAC control`

来源：Nature、Nature Photonics、Nature Communications、Science、Optica、PubMed、作者预印本和官方代码仓库。

## Paper2Agent 定向核验

- 论文：通过 DOI `10.1038/s41586-026-11044-y` 定位 Nature 正式版本，核对正文、Methods、评价样本、成功定义、结果与 Discussion 限制。
- 源码：只读浅克隆官方仓库并固定到 `8c2d059165ef8cdcb70dbea76655b9c2b55b38e6`；核对根许可证、`skills/paper2agent/`、Paper2MCP 工作流、Tool Contract 指南和 `verify_mcp_server.py`。
- 关键词核查：在固定源码中检索 PIC、EDA、PDK、gdsfactory、SAX、COMSOL、Lumerical、DRC 等领域词；未发现明确的 PIC/EDA 验证材料。
- 执行边界：没有安装依赖、运行仓库代码、生成 MCP Server 或复现实验；源码级判断均标为 `CODE VERIFIED`，而非 `RUN VERIFIED` 或物理验证。

## 交叉场景与逐项目增补核验

- 重新读取 TASK-005 固定提交源码索引与 TASK-006 一手来源，按统一问题补充 DAS、光子人工智能计算和面向智能体的 PIC 设计代表项目。
- 定向核对硅光集成 DAS 解调器、高消光比电光调制器、通信相干收发复用和混合集成激光的论文正文或官方摘要；搜索未发现人工智能智能体端到端设计并物理验证 DAS 光电混合集成芯片的公开证据，因此记为 `UNKNOWN（未知）`，而不是断言绝对不存在。
- 只读执行 `git ls-remote` 核对七个核心公开仓库主分支。PhIDO、PhIDO-Agentic、AutoPhotonicDesign、PICBench、Paper2Agent 与已记录提交一致；gdsfactory/gplugins 主分支已更新，只记录新提交标识，不对未经逐行重审的变化作源码级结论。
- 本轮没有克隆或运行新增项目、安装依赖、执行求解器、生成版图或复算论文指标。

## 纳入与排除

纳入：原始论文、作者预印本、出版社/会议官方页面、能改变路线判断的官方代码。

排除或降级：新闻稿单独证据、只读摘要却声称完整系统、FBG interrogator 冒充 DAS、普通 PIC 器件冒充 DAS、已撤稿论文、没有统一边界的营销性能。

## Qwen 审计

Qwen 的只读输出成功扩展了 Photonic AI 候选并指出 arXiv DAS 检索稀疏；但其“DAS PIC 侧证据不足”只反映 arXiv 覆盖。Codex 用 Optica/Nature/Science 一手论文补齐并纠正为：已有真实 PIC-DAS 端到端实验，但尚未形成公开、成熟、全芯片平台。
