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

## 纳入与排除

纳入：原始论文、作者预印本、出版社/会议官方页面、能改变路线判断的官方代码。

排除或降级：新闻稿单独证据、只读摘要却声称完整系统、FBG interrogator 冒充 DAS、普通 PIC 器件冒充 DAS、已撤稿论文、没有统一边界的营销性能。

## Qwen 审计

Qwen 的只读输出成功扩展了 Photonic AI 候选并指出 arXiv DAS 检索稀疏；但其“DAS PIC 侧证据不足”只反映 arXiv 覆盖。Codex 用 Optica/Nature/Science 一手论文补齐并纠正为：已有真实 PIC-DAS 端到端实验，但尚未形成公开、成熟、全芯片平台。
