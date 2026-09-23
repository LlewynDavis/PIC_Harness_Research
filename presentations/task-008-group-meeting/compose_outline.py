"""Rearrange the accepted TASK-007 deck for a 15–20 minute group meeting.

The TASK-007 outline remains unchanged; this script writes only this
workspace's canonical outline.json. All technical claims trace to TASK-007.
"""

import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "presentations/task-007-group-meeting/outline.json"
TARGET = Path(__file__).with_name("outline.json")
original = json.loads(SOURCE.read_text(encoding="utf-8"))
source_slides = original["slides"]


def reuse(number, **changes):
    slide = copy.deepcopy(source_slides[number - 1])
    slide.update(changes)
    return slide


def content(title, variant, **fields):
    return {"type": "content", "variant": variant, "title": title, **fields}


main = [
    reuse(1,
          title_layout="split-hero",
          subtitle="DAS 光电混合集成 · 光子人工智能计算 · Agentic PIC Design\n汇报人：林子涵｜纤维光学与生物光子学课题组｜2026-09-23",
          notes="核心问题：三个导师目标的研究现状与候选切入点。先说明这是文献调研汇报，论文成果属于原作者，本项目尚未开展物理实验；下一页界定三目标。"),
    reuse(2,
          title="三个目标分别对应物理场景、计算硬件与设计方法",
          cards=[
              {"title": "DAS｜物理场景", "body": "AI 辅助设计光电混合集成芯片；关注系统需求到器件、电子和封装的约束。"},
              {"title": "光子 AI｜计算硬件", "body": "让光学计算承担部分 AI 推理运算；关注任务精度与完整系统成本。"},
              {"title": "Agentic PIC｜设计方法", "body": "让 Agent/Harness 组织需求、设计工具、物理验证与失败修正。"},
          ],
          summary_callout="三者是导师提出的研究目标；已有文献进展不等于本项目已实现，也不构成单一连续路线。",
          notes="核心问题：三个目标各指向什么。重点解释 DAS 是可研究的物理场景，光子 AI 是计算硬件，Agentic PIC 是设计方法；它们可相互联系但不能互相替代。下一页说明证据如何分级。"),
    reuse(3,
          title="用已核验文献回答路线、进展、缺口与候选问题",
          body="承接 TASK-004/005/006；按技术路线比较代表工作，并定向核读会影响结论的原文。这是范围综述，不声称穷尽全领域。",
          highlights=["FACT / CODE VERIFIED：原文或固定源码可核对", "AUTHOR CLAIM：作者报告，未由本项目复算", "INFERENCE：跨工作技术判断", "UNKNOWN：证据尚不足"],
          notes="核心问题：为什么这些结论可信。口头解释事实、作者报告、推断和未知四类即可；强调没有把文献性能当成本项目成果。接下来先看 DAS 的完整系统链。"),
    reuse(6,
          title="DAS 指标由光源、传感链路、接收与算法共同决定",
          caption="基于正式报告 2.1 节重绘的概念链路；不是某篇论文已集成的单片结构。",
          sources=["TASK-007 正式报告 §2.1；概念图依据该节重绘"],
          notes="核心问题：DAS 为什么不能只看单一器件。沿图从光源、传感光纤、相干接收讲到采集与 DSP，点出距离、空间分辨率、灵敏度受测试条件共同影响。下一页用代表论文定位集成层级。"),
    reuse(8,
          title="DAS 已有 PIC 与混合模块进入真实传感实验",
          rows=[
              ["Jin 2024｜PIC 前端", "SOI 调制与相干接收进入 12.1/49 km DAS", "激光、放大、采集、DSP 外置"],
              ["Jin 2026｜混合模块", "InP 激光 + SOI PIC；10 km 演示", "会议短文；系统电子与 DSP 外置"],
              ["Cheng 2023｜器件", "高消光比调制器进入 2 km 台架", "只替换发射子模块"],
          ],
          caption="距离和性能均为作者报告；不同试验条件下不作直接排名。",
          sources=["Jin 2024 doi:10.1364/PRJ.512298；Jin 2026 doi:10.1364/OFC.2026.W4D.2；Cheng 2023 doi:10.1038/s41467-023-43244-9"],
          notes="核心问题：现有集成究竟做到哪一级。逐行区分器件、PIC 前端、混合模块与完整 DAS 系统；提醒 2026 工作不是全系统片上化。若追问指标，可回到正式报告对应论文与证据审计。下一页转向光子 AI 的三种计算架构。"),
    reuse(12,
          title="光子 AI 主要以干涉、波长复用与衍射承担线性运算",
          rows=[
              ["MZI / 相干网格", "可编程矩阵变换", "芯片网络与光学 MAC", "相位漂移、校准、插损"],
              ["MRR / WDM / 微梳", "波长并行与权重映射", "卷积、光网络推理", "热漂移、工艺偏差、光源"],
              ["衍射 / 芯粒", "传播并行与规模扩展", "任务级或芯粒演示", "对准、重构、接口"],
          ],
          sources=["TASK-007 正式报告 §3.1–3.4；代表论文出处见附录"],
          notes="核心问题：光在 AI 推理中做什么。解释光学路径主要承担线性算子，数据输入输出、控制及非线性仍需系统支持。三行分别对应可编程、波长并行和传播并行架构。下一页看真实演示与系统边界。"),
    reuse(13,
          title="真实任务演示已出现，但核心指标不能代替系统结论",
          rows=[
              ["Netcast 2022", "分布式光电推理", "40 aJ 是接收端光能，不是墙插能耗"],
              ["ACCEL 2023", "全模拟光电视觉任务", "任务专用，operation 口径有别"],
              ["Taichi 2024", "光子芯粒与任务演示", "“AGI”是作者定位"],
              ["PACE 2025", "2.5D 64×64 MAC 与 Ising", "外部激光；非通用 DNN 推理"],
          ],
          sources=["Netcast doi:10.1126/science.abq8271；ACCEL doi:10.1038/s41586-023-06558-8；Taichi doi:10.1126/science.adl1203；PACE doi:10.1038/s41586-025-08786-6"],
          notes="核心问题：论文验证了任务还是仅有算子。突出 Netcast 的局部能量口径与 PACE 的任务边界；所有指标为作者报告。系统评价还要计入激光、ADC/DAC、控制、存储与精度。下一页转向让 Agent 设计 PIC 的工具链。"),
    reuse(17,
          title="Agentic PIC 的价值取决于工具结果能否形成验证闭环",
          caption="基于 TASK-005 技术地图重绘的概念流程；不是本项目已实现的 Harness。",
          sources=["TASK-005 technical-map-and-objects.md；TASK-007 正式报告 §4.1"],
          notes="核心问题：Agentic PIC 比生成脚本多了什么。沿图说明需求→Harness/Tool Contract→CAD/solver/EDA→结果和修正；求解器、规则检查与原始产物才提供可核验数值证据。下一页把代表工作放到各环节。"),
    reuse(18,
          title="代表工作覆盖结构化设计、仿真迭代与电路评价",
          headers=["环节与工作", "已有验证", "仍需谨慎"],
          rows=[
              ["结构化链｜PhIDO 2025", "NL→DSL→GDS/DRC→SAX", "主要是结构/电路级 proof-of-concept"],
              ["仿真在环｜AutoPhotonicDesign 2026", "真实 solver 驱动迭代", "需工程师配置与专家纠错"],
              ["电路评价｜PICBench 2025", "JSON netlist + SAX 评价", "未到全波/版图签核"],
              ["确定性工具｜gdsfactory", "版图/PDK/求解器接口", "工具层本身不证明 Agent 能力"],
          ],
          sources=["PhIDO doi:10.1063/5.0300741；AutoPhotonicDesign arXiv:2606.00915；PICBench arXiv:2502.03159；github.com/gdsfactory/gdsfactory"],
          notes="核心问题：现有研究究竟覆盖哪段技术链。用四行定位工作，重点讲 PhIDO 与 AutoPhotonicDesign 的互补证据和共同边界；不要把脚本、工具调用或 DRC 等同制造级自动设计。下一页进行三个方向的同层级比较。"),
    reuse(22,
          title="三方向的共同断点是需求、工具与结论之间的证据链",
          headers=["方向 / 目标", "主要技术路径", "文献已验证", "待补证据"],
          rows=[
              ["DAS｜稳定传感", "PIC/混合模块与系统链路", "真实光纤中的 PIC/模块", "需求→器件/封装约束"],
              ["光子 AI｜任务计算", "干涉/WDM/衍射与光电接口", "芯片及任务级演示", "误差→精度与总成本"],
              ["Agentic PIC｜设计方法", "结构化输入、工具、验证", "局部工具闭环", "独立评价与跨层验证"],
          ],
          sources=["TASK-007 正式报告 §5.1–5.3；TASK-006 comparative-analysis-matrix.md"],
          notes="核心问题：横向比较应看同一层级的目标、路径、验证与缺口。表格不给主观分数，也不推断方向优劣；三者都存在从局部证据到系统结论的断点。下一页将断点转成候选研究问题。"),
    content("代表性缺口从已有能力推导，而非由“未检索到”证明", "table",
            headers=["已有工作 → 已验证", "尚未解决 / 证据等级", "潜在切入点（推论）"],
            rows=[
                ["PhIDO / AutoPhotonicDesign：结构链与求解器迭代", "跨工具证据语义和独立评价不足｜INFERENCE", "最小 Tool Contract + 证据账本"],
                ["Jin 2024/2026：PIC 与混合模块进入 DAS", "系统指标到器件/封装约束缺少闭环证据｜INFERENCE", "带单位与来源的需求—约束图"],
                ["Netcast / PACE 等：任务或计算核心演示", "误差、精度与完整系统成本口径不统一｜INFERENCE", "统一系统边界与误差—成本链"],
            ],
            column_weights=[2.0, 2.3, 2.0],
            sources=["TASK-007 正式报告 §5.3；TASK-007 full-text-evidence-audit.md；论文见前页"],
            notes="核心问题：怎样从文献形成可信的研究问题。每一行按已有工作、实际验证、仍缺什么、候选切入点讲；三个缺口是跨文献推论，不是整个领域绝无相关工作。下一页对应到已验收的 A/B/C 路线。"),
    content("A/B/C 是三条待讨论的研究路线，不是已选课题", "table",
            headers=["路线 / 问题", "技术切入与对应缺口", "基础工作", "核心困难 / 未确认"],
            rows=[
                ["A｜如何让 PIC Agent 结论可追溯？", "最小工具契约、证据账本、分层验证；补跨工具证据链", "PhIDO / AutoPhotonicDesign / PICBench", "机制净收益、评价独立性"],
                ["B｜如何把 DAS 指标传到芯片约束？", "需求—器件/电路/封装约束图；补跨域映射", "Jin 2024/2026 等", "模型校准、指标可比性"],
                ["C｜误差如何影响任务与总成本？", "器件误差—任务精度—系统成本链；补统一边界", "Netcast / ACCEL / PACE 等", "数据缺失、跨平台口径"],
            ],
            column_weights=[1.8, 2.5, 1.5, 1.8],
            sources=["TASK-007 candidate-routes-and-open-questions.md §Route A/B/C；TASK-006 candidate-research-routes.md"],
            notes="核心问题：三路线各研究什么、依赖什么证据。A 是方法与验证，B 是 DAS 跨域约束，C 是光子 AI 系统证据；均为已验收调研中的候选，尚未选择最终方向。下一页收束三个领域的事实与推断。"),
    content("文献证明局部进展；系统级可信结论仍需补证据", "table",
            headers=["方向", "文献支持的事实 / 作者报告", "调研判断与尚待确认"],
            rows=[
                ["DAS", "PIC 与混合模块已进入真实传感实验", "AI 端到端设计证据不足；系统约束传播待研究"],
                ["光子 AI", "芯片与任务级演示已出现", "核心指标不能代替系统能效；统一边界待确认"],
                ["Agentic PIC", "结构化设计、仿真在环、电路评价均有案例", "制造级可信闭环及方法净收益尚未证实"],
            ],
            sources=["TASK-007 正式报告 §6.4；本项目未复现实验或确定路线"],
            notes="核心问题：听众应带走什么。逐行区分文献事实、作者报告与我们的技术判断；不要把三条候选路线说成研究成果。下一页交给导师和课题组讨论优先补什么证据。"),
    content("请讨论研究问题、证据层级与下一轮调研重点", "cards-3",
            cards=[
                {"title": "聚焦问题", "body": "三个目标中，哪些技术问题最值得进一步收窄？"},
                {"title": "证据边界", "body": "A/B/C 各自还缺哪些一手论文、公开数据或可核验条件？"},
                {"title": "下轮调研", "body": "应优先精读哪些代表工作，才能支持后续方向选择？"},
            ],
            summary_callout="当前只请求研究方向讨论；不把未授权的实验、流片或工程计划当作既定安排。",
            sources=["TASK-007 正式报告 §6.5；candidate-routes-and-open-questions.md"],
          notes="核心问题：邀请组内判断下一阶段该补什么证据。依次讨论聚焦问题、证据层级与代表论文；若被问到实验计划，说明当前工作仅为调研，具体方案需另立任务。论文和验证层级细节可回到正式报告核对。"),
]

main.insert(9, content(
    "代表工作覆盖设计链的不同环节，验证上限并不相同", "flow",
    assets={"diagram": "assets/diagrams/07-capability-matrix.svg"},
    footer="依据 Sharma 等 2025、Kharel 等 2026、Wu 等 2025 与 gdsfactory 官方源码梳理；概念矩阵，详见图示来源表。",
    sources=["TASK-007 正式报告 §4.2–4.4；TASK-005 technical-map-and-objects.md"],
    notes="核心问题：代表性工作分别覆盖设计链的哪些步骤。矩阵只映射论文或源码可以定位的环节，不将工具生态当作 Agent 成果，也不把结构/电路仿真外推到制造级签核。下一页比较三个研究方向。",
))
# The added capability matrix replaces the old conclusion table. The discussion
# page remains the closing slide; the formal report holds detailed evidence.
main.pop(13)

diagram_pages = {
    1: ("01-three-goals.svg", "根据 TASK-007 正式报告 §1.1 重绘；三目标关系是研究框架，不表示已实现统一系统。"),
    3: ("02-das-system.svg", "根据 TASK-007 正式报告 §2.1 重绘的通用 DAS 链路；非某论文单片实现。"),
    4: ("03-das-integration.svg", "据 Jin 等（2024，doi:10.1364/PRJ.512298）与 Jin 等（2026，doi:10.1364/OFC.2026.W4D.2）重绘；距离为作者报告。"),
    5: ("04-photonic-system.svg", "根据 TASK-007 正式报告 §3.1–3.5 重绘；通用计算系统链路，非单篇论文结构。"),
    6: ("05-photonic-families.svg", "根据 TASK-007 正式报告 §3.2–3.4 重绘；每列为架构家族概念，不对应单一论文器件。"),
    11: ("08-evidence-gaps.svg", "依据 TASK-007 正式报告 §5.3 重绘；缺口与切入点均为跨文献推论。"),
    12: ("09-route-derivation.svg", "依据 TASK-007 candidate-routes-and-open-questions.md 重绘；A/B/C 均未选定。"),
    2: ("10-evidence-labels.svg", "依据 TASK-007 正式报告 §1.2 与 full-text-evidence-audit.md 重绘；标签界定结论的证据级别。"),
    10: ("11-cross-direction-matrix.svg", "依据 TASK-007 正式报告 §5.1–5.3 与 TASK-006 对比矩阵重绘；待补证据为调研推论。"),
}
for idx, (filename, footer) in diagram_pages.items():
    slide = main[idx]
    slide["variant"] = "flow"
    slide["slide_intent"] = "process"
    slide["visual_intent"] = "flow"
    slide["assets"] = {"diagram": f"assets/diagrams/{filename}"}
    slide["footer"] = footer
    for key in ("body", "highlights", "cards", "rows", "headers", "summary_callout", "caption"):
        slide.pop(key, None)

main[7].update({
    "title": "AutoPhotonicDesign：目标进入设计、校验与仿真循环",
    "variant": "flow",
    "assets": {"diagram": "assets/paper-figures/autopd-fig1b.png"},
    "footer": "Kharel 等（2026），Fig. 1(b)，arXiv:2606.00915；原图局部裁剪。显示该论文工作流，非本项目实现。",
    "sources": ["Kharel 等，Autonomous agentic design for photonics，arXiv:2606.00915，Fig. 1(b)"],
    "notes": "核心问题：真实 Agent 设计循环如何连接人给定的目标、设计修改、规则校验、物理仿真与结果记录。这是 AutoPhotonicDesign 论文 Fig. 1(b) 原图局部，不是本项目实现；论文实验仍需要工程师前期配置和专家纠错。下一页对比 PhIDO 的不同覆盖方式。",
})
main[8].update({
    "title": "PhIDO 原图展示自然语言到版图、规则与电路评价的分段流程",
    "variant": "flow",
    "assets": {"diagram": "assets/paper-figures/phido-fig1.png"},
    "footer": "Sharma 等（2025），Fig. 1，APL Machine Learning，doi:10.1063/5.0300741；原图裁剪。FDTD 支路不代表主发布已验证。",
    "sources": ["Sharma 等，AI agents for photonic integrated circuit design automation，APL Machine Learning 4, 046113 (2025)，Fig. 1"],
    "notes": "核心问题：PhIDO 的四段流程分别验证到哪里。用原论文 Fig. 1 说明 Interpreter、Designer、Layout、Circuit Verification 的关系；指出论文主要证明结构和电路流程，FDTD 因版本兼容未进入主发布，不能读成器件物理性能达标。下一页用矩阵对比代表工作覆盖与验证上限。",
})
for idx in (7, 8):
    for key in ("body", "highlights", "cards", "rows", "headers", "summary_callout", "caption"):
        main[idx].pop(key, None)

outline = copy.deepcopy(original)
outline["slides"] = main
assert len(main) == 14
assert all(slide.get("notes") for slide in main)
TARGET.write_text(json.dumps(outline, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Wrote {TARGET}: {len(main)} main, no appendix")
