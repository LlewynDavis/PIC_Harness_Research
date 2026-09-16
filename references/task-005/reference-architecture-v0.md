# TASK-005 PIC_Harness_Research Reference Architecture V0

本文件是研究架构草案，不是实现 SPEC。它不授权新增代码、依赖、MCP、solver 或实验。

## D. Reference Architecture V0

```text
Requirement / Natural Language
  │  preserve raw request + ambiguity
  ▼
DesignSpec / typed IR ─────────────── Knowledge / PDK Snapshot
  │ schema + units + constraints       │ versioned, licensed, query evidence
  ▼                                    ▼
Planner / Harness ───────────────► Tool Registry / Adapter
  │ plan, budgets, gates                │ typed params, capabilities, policy
  ▼                                    ▼
State / Evidence Ledger ◄──────── Execution / Solver
  │ append-only events                  │ isolated deterministic boundary
  │                                    ▼
  ├─────────────────────────────── RESULT Envelope
  │                                    │ raw artifacts + metrics + provenance
  ▼                                    ▼
Retry / Recovery ◄─────────────── Evaluator
  │ classified failure                 │ deterministic, level-specific
  ▼
Layout / GDS / Routing
  ▼
Verification Gates
  ├─ syntax / connectivity / geometry
  ├─ DRC / circuit / full-wave
  └─ optional LVS / PDK / corners / signoff
```

### Trust boundaries

- LLM 可以提出 DesignSpec/plan/candidate action，但不能签发物理通过结论。
- Tool adapter 只证明请求合法并被执行；RESULT 才承载执行证据。
- Evaluator 必须是脚本/规则/solver 输出驱动，LLM 只能解释，不能覆盖指标。
- 每个 verification gate 独立记录 `PASS`、`FAIL`、`NOT_RUN` 或 `UNKNOWN`。
- PDK、商业 solver 和 foundry 证据必须显式受许可证与访问边界约束。

## Q1. DesignSpec / typed IR 判断

### 当前状态

- PhIDO 已证明 YAML/DSL 与 typed `DesignIntent`/`CircuitDSL` 能连接 NL、components、connectivity 和 gdsfactory。`CODE VERIFIED`
- gdsfactory 已提供 typed netlist、PDK、cross-section 和 YAML validation。`CODE VERIFIED`
- AutoPhotonicDesign 证明窄任务中 Python 文件本身可充当可执行表示，但它缺少 requirement trace 和跨工具 schema。`CODE VERIFIED`
- PICBench 证明 JSON netlist 足以做 circuit-level evaluator，但不含 layout/PDK/physics constraints。`CODE VERIFIED`

### 初步结论

现有工作没有解决“可靠的通用 PIC DesignSpec”。最明显的 gap 不是再造一个通用 DSL，而是让最小 typed IR 同时表达：需求可追踪性、单位、端口与连接、允许的 PDK cells、性能约束、验证义务和证据状态。`INFERENCE`

### V0 最小字段

```yaml
spec_version: string
requirement:
  raw_text: string
  normalized_goals: []
  assumptions: []
  unresolved_ambiguities: []
design:
  domain: circuit | device
  pdk_ref: {name, version, hash, access_class}
  components: []
  connections: []
  ports: []
constraints:
  wavelengths: []
  units: {}
  geometry: []
  performance: []
verification_obligations: []
traceability: []
```

它不是最终 schema；尤其 device geometry、material model 和 foundry rule representation 仍为 `UNRESOLVED`。

## Q2. Agent / Harness / Tool Adapter 判断

稳定 Tool Contract 至少要包括：

```text
tool_id + version
capability and verification level
typed parameters + units
preconditions + required assets
read/query vs mutate/execute permission
timeout + resource/cost budget
idempotency/cache semantics
structured result + error taxonomy
artifact/provenance commitments
```

证据支持的组合路线是：借鉴 OpenROAD-MCP 的 query/exec、session、structured error 和 gate summary；复用 gdsfactory/gplugins 的确定性工具；吸收 PhIDO-Agentic 的 typed intent/gates。但三者目前没有合成一个经验证的 PIC Harness。`INFERENCE`

`LLM 生成/编辑 Python` 可以作为受控实验 adapter，却不等同稳定 Tool Contract：它扩大执行面、参数验证弱、回滚与 provenance 难统一。AutoPhotonicDesign 说明该路线能工作，也同时暴露其科学可审计性边界。

## Q3. RESULT schema V0

RESULT 是“某次确定性工具执行和评价的证据封套”，不是 LLM 摘要，也不是只含一个 FoM 的日志。

```yaml
result_schema_version: "0.1-draft"
run:
  run_id: string
  parent_run_id: string | null
  iteration: integer
  started_at: timestamp
  ended_at: timestamp
  status: success | failed | partial | cancelled
provenance:
  repo_commit: string
  design_spec_hash: string
  tool: {id, version, adapter_version}
  environment: {os, runtime, container_digest, dependency_lock_hash}
  pdk: {name, version, hash, access_class}
inputs:
  geometry_hash: string
  netlist_hash: string | null
  materials: []
  wavelength_or_frequency: {}
  mesh: {}
  boundary_conditions: {}
  sources: []
  monitors: []
  solver_options: {}
execution:
  command_or_api: string
  resource_budget: {}
  resource_usage: {}
  cache_hit: boolean
  tool_exit: {code, signal, timeout}
artifacts:
  raw_outputs: []
  logs: []
  fields: []
  sparameters: []
  gds: []
metrics:
  values: []
  evaluator: {id, version, script_hash}
  tolerance: {}
verification:
  gates: []
  highest_attempted_level: string
  highest_passed_level: string
failure:
  class: input | dependency | resource | tool | numerical | geometry | verification | policy | unknown
  retryable: boolean
  evidence: []
human_intervention:
  occurred: boolean
  actions: []
decision:
  action: accept | retry | rollback | escalate | reject
  reason_codes: []
```

### V0 约束

- raw artifacts 用 hash +受控路径引用，不能只保存自然语言摘要；
- metric 必须绑定 evaluator/version/script hash；
- mesh/material/boundary/wavelength 缺失时，physical result 不得标为完整；
- solver invocation 与 evaluator pass 分离；
- commercial/cloud job 要记录 task/job id、版本、cost/resource 和可获取性；
- surrogate 要额外记录 training-domain reference、OOD/uncertainty 与 full-wave spot-check 状态。

## Q5. PIC Harness 最小状态机草案

```text
RECEIVED
  ├─ ambiguity → WAITING_FOR_HUMAN
  ▼
SPEC_VALIDATING ─fail→ FAILED_SPEC
  ▼
PLANNED ─budget/policy fail→ REJECTED_POLICY
  ▼
TOOL_READY ─dependency fail→ BLOCKED_DEPENDENCY
  ▼
EXECUTING ─timeout/crash→ CLASSIFY_FAILURE
  ▼
RESULT_CAPTURED ─incomplete→ CLASSIFY_FAILURE
  ▼
EVALUATING
  ├─ pass terminal gates → ACCEPTED
  ├─ retryable + budget → CHECKPOINT → RETRY_PLANNING → EXECUTING
  ├─ rollbackable → ROLLBACK → RETRY_PLANNING
  ├─ ambiguity/unsafe → WAITING_FOR_HUMAN
  └─ nonretryable/budget exhausted → FAILED
```

### 最小状态字段

- immutable `run_id`、parent/iteration、DesignSpec hash；
- plan、active tool、budget remaining、checkpoint artifact hashes；
- failure class、retry count、retry reason、keep/discard decision；
- human intervention 与 termination reason；
- append-only event history，禁止把失败样本覆盖为成功样本。

### 恢复策略

- `input/spec`：回到 DesignSpec 或请求人工澄清；
- `dependency/resource/policy`：不盲重试，等待资源或改变已授权配置；
- `tool transient`：同输入有限重试并保留每次结果；
- `numerical`：只有明确的 mesh/solver adjustment policy 才重试；
- `geometry/verification`：从最近有效 checkpoint 生成新 candidate；
- retry budget 耗尽后终止，不能由 LLM 自行扩大计算预算。

## E. Build vs Reuse

每项只使用任务规定的四类决策；这是 V0 取向，不是工程授权。

| 模块 | 决策 | 依据 |
|---|---|---|
| Requirement intake | `BUILD` | 需要本项目的 scope、ambiguity 与 provenance 边界 |
| DesignSpec / typed IR | `BUILD` | 可借鉴 PhIDO/gdsfactory，但现有 schema 不覆盖完整 trace/verification obligation |
| Planner / Harness | `BUILD` | 现有对象各自绑定特定 workflow，缺统一可信闭环 |
| PDK / component models | `REUSE` | 优先复用 gdsfactory/公开 PDK abstractions；foundry PDK 另受权限约束 |
| Knowledge / RAG | `UNDECIDED` | PhIDO-Agentic 有 GraphRAG，但当前尚无证据证明是最小路径必需 |
| Tool Registry | `BUILD` | 需要 PIC-specific capability/verification/resource policy |
| gdsfactory APIs | `REUSE` | 成熟 deterministic PIC layout/netlist primitives |
| gplugins / solver backends | `WRAP` | 后端语义、许可证、输入输出和失败模式不统一 |
| OpenROAD-MCP patterns | `REUSE` | 复用架构思想与协议模式，不复用电子域工具本身 |
| Execution sandbox/session | `BUILD` | 需本项目资源、权限、artifact 与 lifecycle 规则 |
| RESULT envelope | `BUILD` | 没有现成统一 scientific evidence schema |
| Evaluator | `BUILD` | 可复用 SAX/DRC/solver，但需分层 gate 和明确 metric |
| State / Evidence Ledger | `BUILD` | session/journal 不能满足不可变审计需求 |
| Layout / routing | `REUSE` | gdsfactory 是首选底座 |
| DRC integration | `WRAP` | 需绑定具体 deck/version/waiver 与 RESULT |
| LVS | `UNDECIDED` | 公共 PIC LVS 与目标 PDK 可用性尚未闭合 |
| Foundry signoff | `UNDECIDED` | 取决于未来 foundry/PDK 授权，不能自行承诺 |
| Benchmark | `BUILD` | PICBench 结构可借鉴，但需要多层物理/版图评价 |
| Surrogate solver | `UNDECIDED` | MetaChat 显示潜力，但域外风险和数据成本尚高 |

## V0 的最小可研究范围

Reference Architecture 并不意味着一次实现所有层。当前证据更支持从一个 circuit-first、evidence-first 的窄闭环开始：typed spec → gdsfactory/SAX tool adapter → RESULT → deterministic evaluator → bounded retry → optional GDS/DRC gate。Full-wave、RAG、LVS、foundry PDK 和 surrogate 应作为独立研究问题逐级加入，而不是 V0 默认依赖。`INFERENCE`
