# TASK-005 Review Package

状态：`TASK-005_REVIEW_READY`

本目录是 L01 第二阶段的核心架构深挖材料，不是最终 L01 报告，也不包含工程实现。

## 交付物索引

1. [source-log.md](source-log.md)：检索词、论文/仓库、固定 commit、许可证、源码证据与 Qwen 中间材料审计；
2. [technical-map-and-objects.md](technical-map-and-objects.md)：技术层级地图和六个核心对象的五问拆解；
3. [capability-and-verification-matrix.md](capability-and-verification-matrix.md)：Harness Capability Matrix、benchmark levels 与 Verification Ladder；
4. [reference-architecture-v0.md](reference-architecture-v0.md)：Reference Architecture V0、DesignSpec 判断、Tool Contract、RESULT schema V0、最小状态机和 Build vs Reuse；
5. [research-gaps-and-route-seeds.md](research-gaps-and-route-seeds.md)：Research Gap Matrix、5 个路线种子、路线级对抗性审查、strongest counterexamples 和五大未决问题。

## 核心判断

- 当前仍没有公开证据支持一个可直接采用、全开源、通用、可复现并达到 PIC 物理/制造可信闭环的 Agent Harness。
- PhIDO 最接近 PIC 结构生成闭环；AutoPhotonicDesign 提供最强的真实 solver-in-the-loop 证据；gdsfactory/gplugins 是最成熟的 Tool Layer；PICBench 是可借鉴但层级有限的 Evaluator；OpenROAD-MCP 提供 Tool Contract/session 参照；MetaChat 提供 agent + surrogate + optimization 的相邻领域参照。
- 最可能需要自行补齐：最小 typed DesignSpec、agent-safe tool adapter、RESULT/evidence ledger、分层 evaluator、failure-aware state machine 和诚实的 verification ladder。
- 当前只提出路线种子，不选择最终路线。

## 证据边界

- 本轮只读取公开论文、官方文档和固定 commit 源码；没有运行候选代码或外部 solver。
- 外部论文指标是 `AUTHOR CLAIM`，不是本项目实验结果。
- `CODE VERIFIED` 表示实现存在，不表示运行成功或物理正确。
- MetaChat 根许可证未核验；PICopilot/PICasso 无公开实现时不作源码级结论。
- `D:\AI_PIC_Demo` 未被访问或修改。

## 下一步边界

等待 GPT 审查。审查通过前不得启动 TASK-006、不得实现架构、不得开始最终 L01 报告。
