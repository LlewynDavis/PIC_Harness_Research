"""Add TASK-016 evidence to the existing, user-edited TASK-007 DOCX.

The current DOCX is the input; this script does not rebuild from Markdown.
Run only once after backing up the current file. It refuses a second run.
"""

from __future__ import annotations

import os
from pathlib import Path

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

from build_task007_feishu_docx import (
    font_run,
    set_cell_border,
    set_cell_margin,
    set_cell_shading,
)


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "output/task-007/面向光子芯片智能设计的三方向技术调研_飞书上传版.docx"
FIG = ROOT / "references/task-016-evidence/figures"
PHIDO_ARCH = ROOT / "presentations/task-010-group-meeting-rebuild/assets/phido-fig1.png"
MARKER = "TASK-016 证据增强：七篇代表工作"


def after(element, block):
    element.addnext(block)
    return block


def paragraph(doc, cursor, text="", *, bold_prefix=None, size=9.6, caption=False, style=None):
    p = doc.add_paragraph(style=style or "Normal")
    p.paragraph_format.space_after = Pt(4 if caption else 6)
    p.paragraph_format.line_spacing = 1.16
    if bold_prefix and text.startswith(bold_prefix):
        font_run(p.add_run(bold_prefix), size=size, bold=True)
        font_run(p.add_run(text[len(bold_prefix):]), size=size)
    else:
        font_run(p.add_run(text), size=size)
    return after(cursor, p._p)


def heading(doc, cursor, text):
    p = doc.add_paragraph(style="Heading 4")
    p.paragraph_format.keep_with_next = True
    if text.startswith("4.2.8 "):
        p.paragraph_format.page_break_before = True
    run = font_run(p.add_run(text), size=10.2, bold=True, color="000000")
    run.italic = False
    return after(cursor, p._p)


def picture(doc, cursor, path, width, caption_text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(5)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.keep_with_next = True
    p.add_run().add_picture(str(path), width=Inches(width))
    cursor = after(cursor, p._p)
    return paragraph(doc, cursor, caption_text, size=8.2, caption=True)


def table(doc, cursor, rows, widths):
    t = doc.add_table(rows=len(rows), cols=len(rows[0]))
    t.autofit = False
    for ri, values in enumerate(rows):
        tr = t.rows[ri]
        pr = tr._tr.get_or_add_trPr()
        pr.append(OxmlElement("w:cantSplit"))
        if ri == 0:
            hd = OxmlElement("w:tblHeader")
            hd.set(qn("w:val"), "true")
            pr.append(hd)
        for ci, value in enumerate(values):
            cell = tr.cells[ci]
            cell.width = Inches(widths[ci])
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            set_cell_border(cell)
            set_cell_margin(cell, 90, 90, 90, 90)
            if ri == 0:
                set_cell_shading(cell, "274766")
            elif ri % 2 == 0:
                set_cell_shading(cell, "F4F7FA")
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.12
            for run in [p.add_run(value)]:
                font_run(run, size=8.35 if len(widths) == 4 else 8.7,
                         bold=(ri == 0), color="FFFFFF" if ri == 0 else "000000")
    return after(cursor, t._tbl)


def anchor(doc, prefix):
    found = [p for p in doc.paragraphs if p.text.startswith(prefix)]
    if len(found) != 1:
        raise ValueError(f"Expected one anchor {prefix!r}, found {len(found)}")
    return found[0]._p


def main():
    doc = Document(TARGET)
    if any(MARKER in p.text for p in doc.paragraphs):
        raise SystemExit("TASK-016 evidence already present; refusing duplicate insertion")

    c = anchor(doc, "Jin 等 2024 将")
    c = heading(doc, c, "证据增强｜Jin 2024 系统功能与外部依赖")
    c = paragraph(doc, c, "原图定位：Jin et al., 2024, Silicon photonic integrated interrogator for fiber-optic distributed acoustic sensing, Fig. 1(b)/3/5/6, DOI: 10.1364/PRJ.512298。Fig. 1(b) 显示片上 MZM、PC/BS、PBRS、90° hybrid 与四个平衡探测器；Fig. 3 另列片外窄线宽激光、EDFA、环行器、AWG、TIA、DAQ 和 DSP。原图再分发许可未核实，本 DOCX 不复制。")
    c = table(doc, c, [
        ["系统结果", "测试条件与原文定位", "证据边界"],
        ["12.1 km；1.14 m；59 pε/√Hz", "100 Hz PZT；5 kHz 重复率；gauge length 0.819 m；300 traces。Fig. 5、§4.B，PDF p.5–6。", "AUTHOR CLAIM；光源、放大、采集和处理仍在片外。"],
        ["49.0 km；3.78 m；81 pε/√Hz", "100 Hz PZT；1.5 kHz 重复率；gauge length 4.01 m；120 traces。Fig. 6、§4.B，PDF p.6–7。", "AUTHOR CLAIM；条件不同，不能只按两个噪声数字排序。"],
    ], [1.55, 3.1, 2.18])

    c = anchor(doc, "Cheng 等 2023 采用")
    c = heading(doc, c, "证据增强｜Cheng 2023 四微环调制器")
    c = paragraph(doc, c, "核心判断：四个半径 10 µm 的耦合微环针对 DAS 发射脉冲设计；器件消光比和 2 km Φ-OTDR 演示分属不同验证层级。")
    c = picture(doc, c, FIG / "cheng-fig1-device-spectrum.png", 6.0,
                "Source: Cheng et al., 2023, On-chip silicon electro-optical modulator with ultra-high extinction ratio for fiber-optic distributed acoustic sensing, Fig. 1(a–f), DOI: 10.1038/s41467-023-43244-9；PDF p.2；CC BY 4.0；仅裁去无关正文。")
    c = picture(doc, c, FIG / "cheng-fig2-extinction.png", 5.8,
                "Source: Cheng et al., 2023, Fig. 2(a–f), DOI: 10.1038/s41467-023-43244-9；PDF p.3；CC BY 4.0；保留坐标轴与图例。")
    c = table(doc, c, [
        ["关键结果", "条件与原文定位", "边界"],
        ["静态 71 dB；动态 68 dB", "静态 1549.74 nm、约 1.9 V；动态 self-heterodyne。Fig. 2，PDF p.3–4。", "AUTHOR CLAIM；两种 ER 口径不同。"],
        ["3.60 mW；上升/下降 6.54/0.40 ns", "高占空比驱动，器件约 0.99 V/3.65 mA；10–90% 边沿。Fig. 1(f)/2(f)，PDF p.3–4。", "AUTHOR CLAIM；功率仅属 EOM。"],
        ["2 km DAS；4 pε/√Hz", "500 Hz PZT；与 AOM 对照的 Φ-OTDR 台架。Fig. 4/5，PDF p.5–6。", "AUTHOR CLAIM；未证明完整收发系统片上化。"],
    ], [1.55, 3.1, 2.18])

    c = anchor(doc, "Sandmann 等 2023 探索")
    c = heading(doc, c, "证据增强｜Sandmann 2023 相干收发复用")
    c = paragraph(doc, c, "Source: Sandmann et al., 2023, Acoustic Sensing with Correlation and Coherent Detection using an Integrated Coherent Transceiver, Fig. 2/5、§III，PDF p.2–4，DOI: 10.48550/arXiv.2306.04199。Fig. 2 区分 IC-TROSA 与外部激光、EDFA、环行器及离线处理；Fig. 5 在 20 km launch fiber 后记录 200 Hz 扬声器扰动，约 0.9 rad 峰峰相位变化。结果为 AUTHOR CLAIM；会议短文未给出与 Jin 同口径的检测限/空间分辨率。原图版权限制未核实，故不复制。")

    c = anchor(doc, "通用光子 AI 加速器原型 2025 展示")
    c = heading(doc, c, "证据增强｜Ahmed 2025 光学核心与完整任务")
    c = paragraph(doc, c, "原图定位：Ahmed et al., 2025, Universal photonic artificial intelligence acceleration, Fig. 1/2、Table 1、Methods，PDF p.1–3/6/8，DOI: 10.1038/s41586-025-08854-x。Fig. 2 的 host/PCIe、数字控制接口、数据转换、PTC 和输出流水线说明：光电混合张量核执行矩阵向量运算，电子系统仍承担编译、控制、权重存储、转换、非线性和累加。原图再分发许可不明，本 DOCX 仅列精确定位。")
    c = table(doc, c, [
        ["论文报告", "任务/口径与原文定位", "证据边界"],
        ["65.5×10¹² ABFP16 ops/s", "4 个 128×128 PTC、2 个 DCI；500 MHz。主文、Fig. 1/2，PDF p.1–3/6。", "AUTHOR CLAIM；算子速率不是任务吞吐。"],
        ["ResNet18 CIFAR-10 86.4%；BERT-Tiny IMDb 83.2%", "对应 FP32 88.3%/86.2%；Table 1，PDF p.6。", "AUTHOR CLAIM；不同任务精度损失不同。"],
        ["BERT-Tiny SQuAD F1 12.0", "FP32 为 43.5；Table 1，PDF p.6。", "AUTHOR CLAIM；不能只摘较优任务。"],
        ["78 W 电子、1.6 W 光", "Methods 另列 8 只激光器各 1.25 W 电功率，PDF p.6/8。", "AUTHOR CLAIM；统一墙插及 energy/inference 为 UNKNOWN。"],
    ], [1.55, 3.1, 2.18])

    c = anchor(doc, "PhIDO 使用语言模型")
    c = heading(doc, c, "证据增强｜PhIDO 流程与 benchmark")
    c = picture(doc, c, PHIDO_ARCH, 6.0,
                "Source: Sharma et al., 2025, AI agents for photonic integrated circuit design automation, Fig. 1, DOI: 10.1063/5.0300741；PDF p.3；CC BY 4.0。图中 FDTD 为架构分支，不能据此认定进入公开主 benchmark。")
    c = picture(doc, c, FIG / "phido-fig5-complexity.png", 6.1,
                "Source: Sharma et al., 2025, Fig. 5, DOI: 10.1063/5.0300741；PDF p.8；CC BY 4.0。图中 S 的定义见 Table II：有效 schematic 与 GDSII。")
    c = table(doc, c, [
        ["任务/结果", "条件与原文定位", "证据边界"],
        ["102 prompts", "四级任务为 23/10/60/9；七个模型、每题五次。§III.A/C、Fig. 5，PDF p.6/8。", "FACT：benchmark 构成；每模型 510 次生成。"],
        ["单器件最高 91%；levels 1–3 最佳 pass@5 58%", "前者为摘要“up to”口径；后者为正文 §IV.A，PDF p.1/9。", "AUTHOR CLAIM；不等于目标器件性能合格。"],
    ], [1.55, 3.1, 2.18])

    c = anchor(doc, "但工程师需要提供目标、约束")
    c = heading(doc, c, "证据增强｜Kharel 2026 显式规则与仿真闭环")
    c = paragraph(doc, c, "Source: Kharel et al., 2026, Autonomous agentic design for photonics, Fig. 1–6、Table S2/S3、§2/S6，PDF p.3–10/19–20，DOI: 10.48550/arXiv.2606.00915。人类提供目标、仿真文件、几何/工艺约束与定量验收标准；Agent 在 DRC 闸门和求解器数值反馈下提出、保留或回退设计。")
    c = table(doc, c, [
        ["案例", "条件、结果与原文定位", "边界"],
        ["12 µm SiN 弯曲", "400 nm SiN、1550 nm、150 nm 最小特征、50 次仿真预算；0.460→0.109 dB。Fig. 2、§S2.1，PDF p.5/12–14。", "AUTHOR CLAIM：数值仿真，未流片。"],
        ["MRM 与 RF", "MRM 39 次迭代，VπL 0.53 V·cm、Cj 0.83 pF/mm；RF 45 次迭代，43–44 Ω。Fig. 3/4、§S3/S4。", "AUTHOR CLAIM；与目标 50 Ω 仍有差距。"],
        ["布线与多物理 MZM", "布线 192→0 DRC 违规、27 次迭代；MZM 修正初设后的九设计约 29–40 GHz。Fig. 5/6、Table S2/S3。", "AUTHOR CLAIM；验收规则和求解器由工程师提供。"],
    ], [1.55, 3.1, 2.18])
    c = paragraph(doc, c, "关键反例：多物理 MZM 首次设置在 30 GHz 给出 Z₀≈14.7–14.8 Ω，原文参考值约 48 Ω；工程师纠正模态识别和 junction shunt 重复计算后才进入后续循环。Table S2、§S6，PDF p.20。该证据支持“规则＋求解器反馈下迭代”，不支持宣称 Agent 独立建立了正确物理模型。", bold_prefix="关键反例：")

    c = anchor(doc, "PICopilot 以 48 个脚本任务")
    c = heading(doc, c, "证据增强｜PICopilot 内部反馈与外部评分")
    c = paragraph(doc, c, "Source: Jiang et al., 2026, PICopilot: An LLM-based Agentic Framework for Assisting Photonic Integrated Circuit Design via Script Generation, Fig. 2、§3.6/4.1.4、Table 2/3，PDF p.3/6–7，DOI: 10.48550/arXiv.2608.01791。Fig. 2 展示 Task Planner、手册 RAG、脚本生成与评价；内部 Script Evaluator 使用静态代码检查、自定义检查库和 LLM，并未直接执行 PIC 工具。")
    c = table(doc, c, [
        ["benchmark", "评分方法与原文定位", "边界"],
        ["48 项：12 基础、12 中级、24 高级", "外部执行生成脚本并与设计者 ground truth 比较；每任务 15 次，≥3 次成功计 solved。§4.1.4、Table 3，PDF p.7。", "FACT：任务与规则；不是内部仿真反馈。"],
        ["48/48 solved；pass@1 93.9%、pass@5 99.9%", "Table 2，PDF p.7。", "AUTHOR CLAIM；脚本功能一致不等于器件物理性能或代工签核。"],
    ], [1.55, 3.1, 2.18])

    c = anchor(doc, "OpenROAD-MCP 在电子设计自动化领域")
    c = heading(doc, c, "4.2.8 PhIDO、PICopilot 与 Kharel 的验证层级比较")
    c = paragraph(doc, c, MARKER + "。以下将八项比较维度转置排版，以便在竖版文档中阅读；完整原文定位见各证据卡及 TASK-016 证据日志。")
    c = table(doc, c, [
        ["维度", "PhIDO", "PICopilot", "Kharel 2026"],
        ["核心输入", "自然语言 PIC 要求", "自然语言脚本任务", "人类给定目标/约束/仿真文件"],
        ["Agent/Harness", "Interpreter＋Designer；DSL/RAG", "Planner＋Generator＋Synthesizer＋Evaluator；RAG", "coding Agent；迭代日志"],
        ["工具/Simulator", "GDSFactory、DRC、SAX", "内部静态检查；外部执行评分", "Tidy3D/PhotonForge 等求解器＋DRC"],
        ["输出", "schematic、DSL、GDSII", "Python 设计脚本", "仿真设计/布局及数值日志"],
        ["验证层级", "有效 schematic 与 GDSII", "参考输出功能一致", "工程师给定定量验收＋仿真/DRC"],
        ["物理约束", "PDK 组件、schema、路由/DRC", "手册检索、脚本静态检查", "最小特征、几何/工艺/物理一致性闸门"],
        ["当前边界", "非目标性能或 foundry signoff", "内部无数值求解器闭环", "专家纠正初设；无流片验证"],
    ], [0.87, 1.97, 1.97, 2.02])
    c = paragraph(doc, c, "这三项工作不能以单一成功率排序：输入对象、反馈位置与验收层级不同。INFERENCE；依据 Sharma Table II/§IV.A、Jiang §3.6/4.1.4、Kharel Fig. 1/Table S2/§S6。")

    c = anchor(doc, "本轮定向核验不构成穷尽式系统综述")
    c = heading(doc, c, "附录 A.1 本轮未核实问题")
    for s in [
        "PhIDO 逐模型、逐等级的精确原始数值表未核得；不从 Fig. 5 柱形估算伪精度。",
        "PICopilot 的 48 项原始脚本与运行日志未由本项目独立重算。",
        "Kharel 的求解器原始网格、跨 PDK 迁移和实物制造结果未验证。",
        "Jin 系统原始波形与片外设备统一功耗、Sandmann 的同口径检测限尚缺。",
        "Ahmed 的统一墙插功耗与各任务 energy/inference 未从现有主文确定。",
    ]:
        c = paragraph(doc, c, "UNKNOWN：" + s, size=9.4)
    c = paragraph(doc, c, "完整数据条件、原文页码与图示来源见仓库 references/task-016-evidence/ 的 key-data.csv、figure-sources.md、evidence-log.md 和 source-manifest.md。")

    temp = TARGET.with_suffix(".task016.tmp.docx")
    doc.save(temp)
    os.replace(temp, TARGET)
    print(TARGET)
    print(f"paragraphs={len(doc.paragraphs)} tables={len(doc.tables)} inline_images={len(doc.inline_shapes)}")


if __name__ == "__main__":
    main()
