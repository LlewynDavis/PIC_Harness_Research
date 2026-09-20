# 候选研究路线与最小验证实验

本轮保留三条路线，不做最终选题。优先级是基于当前证据和“已知软件条件、未知硬件条件”的暂定判断。

## Route 1｜分层 Agentic PIC Benchmark + 两个可证伪假设

**Research Problem**

现有 PIC Agent 工作无法可靠区分模型、表示、工具、求解器和验证失败，也没有证明 typed IR 或 adaptive tool calling 的净收益。

**Core Method**

先构建 5–10 个 circuit-first 固定任务和 syntax/connectivity/SAX/geometry/DRC 分层 evaluator；每次运行保留最小 RESULT、原始产物、成本、重试与人工介入。随后只选择一个主假设：

- H1：minimal typed DesignSpec 是否优于 direct Python/YAML；或
- H2：adaptive tool calling 是否优于 fixed risk policy。

**Minimum Experiment**

1. 用人工构造的 valid/invalid artifacts 测 evaluator 检出率和误报率。
2. 固定模型、任务、工具、采样和总预算。
3. H1 比较约束遗漏、分层 pass@k、修复轮数、工具错误、时间与 Token。
4. H2 比较 no-tool、fixed-access、adaptive-access 的正确率、漏调用、冗余调用、工具次数和成本。

**Success / Failure**

- 成功：评价层自身可靠；至少一个假设在预注册指标和多个任务上有稳定净收益。
- 失败：只提高 schema 合法率，物理/功能正确率不变；收益来自额外预算；adaptive policy 不优于固定策略。

**Required Conditions**

Python、可调用 LLM、gdsfactory、SAX、KLayout/规则文件、可固定版本的任务与模型。模型接口、版本、预算和 KLayout/PDK 状态仍需确认。

**Main Risk / Simpler Alternative**

风险是变成基础设施工程或小样本自证。简化方案为 5 个任务、JSON + raw files + Git、syntax/circuit/DRC 三层，并用固定风险策略替代 adaptive policy。

## 路线 2｜人工智能驱动的 DAS 光电混合集成设计约束传播

**Research Problem**

已有 PIC-DAS 论文证明子模块和集成收发可以工作，但尚未证明人工智能智能体能够把“距离、分辨率、灵敏度、带宽与成本”可靠转化为光源、调制、相干接收、电子和封装约束，并通过工具得到可核验设计。

**Core Method**

以公开绝缘体上硅解调器、高消光比电光调制器和相干收发器为物理基线，建立“需求结构化 → 架构选择 → 参数分配 → 链路/噪声预算 → 工具验证 → 失败修正”闭环。模型必须覆盖耦合、调制、90° 光学混合器、光电探测/跨阻放大、模数转换、激光线宽/相对强度噪声、掺铒光纤放大和数字信号处理。

**Minimum Experiment**

1. 固定一个边界清晰的 DAS 收发子任务，并用 Jin 2024、Cheng 2023、Sandmann 2023 的公开结果校准数量级。
2. 建立带单位、容差和来源的需求/设计约束，并准备人工专家标准答案。
3. 在相同任务、工具和预算下比较人工设计、固定规则、无工具语言模型和工具型智能体。
4. 评价约束遗漏、参数正确率、无效工具调用、链路指标误差、失败定位、时间与成本。
5. 若后续另获硬件授权，再做“只替换片上电光调制器或接收器”的同系统对照。

**Success / Failure**

- 成功：评价器本身可靠；智能体在多个预注册任务上比无工具模型或固定规则减少关键约束遗漏，并生成可由确定性模型复算的结果。
- 失败：只生成更完整的文字；数值依赖事后人工修正；结果来自更多预算；不同论文边界无法统一；系统结论对未知外部组件高度敏感。

**Required Conditions**

MATLAB/Python；可固定版本的语言模型；人工专家标准答案；若进入器件级则需 COMSOL、Lumerical、绝缘体上硅/氮化硅工艺设计套件。硬件对照还需窄线宽激光、掺铒光纤放大器、环行器、光电探测/跨阻放大、模数/数模转换、长光纤、压电陶瓷、温控与封装；目前均未确认。

**Main Risk / Simpler Alternative**

研究可能退化为语言模型填写已知链路预算，或因评价器不可靠而自证。简化方案是先只研究“接收器噪声/偏振衰落”或“电光调制器消光比/串扰”单一因果链，并比较固定表单、确定性规则和工具型智能体。

## Route 3｜Photonic AI 器件误差 → MVM → 任务精度联合验证

**Research Problem**

大量工作分别报告器件、光学核或任务指标，完整系统能耗和工艺/热误差向任务精度传播的证据不统一。

**Core Method**

选择 4×4 MZI mesh 或 4/8 通道 MRR weight bank，建立几何/材料/温度偏差 → S 参数/传输矩阵 → MVM 误差 → 任务精度链条，比较 nominal-only、静态校准与鲁棒训练。

**Minimum Experiment**

1. 固定同一小型分类或信号任务与数字 reference。
2. 扫描 fabrication、loss、crosstalk、thermal drift 与控制预算。
3. 报告平均值和 95 分位最坏误差、有效位数、任务精度、控制功率与重校准次数。
4. 若比较 MZI/MRR，固定矩阵规模、精度、吞吐和系统边界。

**Success / Failure**

- 成功：鲁棒设计/校准在多随机种子下同时改善最坏 MVM 误差和任务精度，且成本没有被隐藏到数字补偿。
- 失败：改善只来自额外模型容量/数字后处理；只有单一噪声种子有效；调谐功耗或校准频率不可接受。

**Required Conditions**

Python/ML 框架、紧凑模型、Lumerical/COMSOL、gdsfactory；若流片则需 PDK、DRC/LVS、封装、激光、探测、DAC/ADC、FPGA/控制。后半部分当前未确认。

**Main Risk / Simpler Alternative**

方向拥挤且容易落入“再做一个噪声仿真”。简化方案是只研究 MRR 热串扰—精度—控制成本 Pareto，或只做完整光电接口成本模型作为支撑 benchmark。

## 暂定排序

1. **Route 1：优先**——最符合已确认的软件条件，能产出后续路线共用的测量基础。
2. **路线 2：条件优先**——直接对应“人工智能设计 DAS 光电混合集成芯片”的目标，但应从可校准的子系统约束传播对照开始，而不是直接承诺全芯片或流片。
3. **Route 3：条件保留**——论文基础强，最小仿真可行；是否成为主线取决于模型/PDK/算力和导师对创新性的判断。

该排序是 `INFERENCE`，不是最终选题决策。
