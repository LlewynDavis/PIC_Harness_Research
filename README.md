# PIC_Harness_Research

`PIC_Harness_Research` 是一个面向光子芯片设计的 AI Agent Harness 研究平台，也是研究生阶段长期维护的科研主仓库。

项目目标是建立可复现、可比较、可验证的研究环境，用实验回答以下问题：不同大语言模型如何完成光子芯片设计任务；Agent Harness 应如何组织模型、工具、结构化表示和验证器；哪些能力来自 LLM，哪些结论必须由物理仿真或数值验证给出。

## 研究方向

长期研究范围包括：

1. 不同 LLM 在光子芯片设计任务中的能力；
2. Qwen 本地模型与 GPT 等模型的比较；
3. Agent Harness 架构；
4. Tool、MCP 与 API 调用；
5. DesignSpec 等结构化设计表示；
6. 光子芯片设计、仿真、优化和验证工具接入；
7. Single-Agent 与 Multi-Agent；
8. Agent benchmark 与科研实验；
9. DAS 光电混合集成设计作为潜在验证场景；
10. Photonic AI Computing 作为潜在扩展方向。

这些是研究候选方向，不代表当前已经实现，也不构成提前建设复杂系统的依据。

## 当前阶段

当前只建立长期维护所需的最小仓库骨架。仓库尚未实现 Agent、模型接入、工具调用、DesignSpec、MCP Server、仿真流程或 benchmark。

下一阶段首先建立一个可测量的 Single-Agent benchmark baseline，再根据实验结果决定后续架构。

## 核心原则

- MVP-first
- 实验驱动
- 可复现
- 最小复杂度
- LLM 负责推理和决策，仿真器与验证器负责物理和数值真实性

## 仓库结构

- `docs/`：当前状态、唯一任务、决策记录和研究计划。
- `src/pic_harness/`：后续研究平台的 Python 包；当前仅保留包入口。
- `tests/`：后续与实现风险相称的自动化测试。
- `experiments/`：科研实验事实记录。
- `configs/`：可提交的非敏感配置与模板。
- `scripts/`：少量可复现的辅助脚本。
- `references/`：参考资料索引，不用于存放未经许可的大文件。

## 旧项目边界

`D:\AI_PIC_Demo` 已正式封存。它只作为前期原型、工程经验参考和可复用实现的候选来源，不是本项目的架构基线。未经独立任务授权，不得从旧项目复制代码或修改旧项目。

## 开发起点

本项目要求 Python 3.11 或更高版本。当前没有运行时依赖。

```powershell
python -m pip install -e .
python -c "import pic_harness"
```

开始任何工作前，请阅读 `AGENTS.md`、`docs/CURRENT_STATE.md`、`docs/TASK.md` 和 `docs/DECISIONS.md`。

## 研究门户（Research Portal）

TASK-005 研究材料可通过本地 MkDocs Material 门户阅读。PowerShell 启动方式：

```powershell
cd G:\PIC_Harness_Research
.\portal\setup.ps1
.\portal\serve.ps1
```

浏览器打开 `http://127.0.0.1:8000/`。原始研究内容仍以 `references/task-005/` 为唯一事实源（Source of Truth）。
