"""Build source-linked, vector technical diagrams for TASK-008 slides.

These diagrams visualize statements already present in TASK-005/006/007.
They are conceptual redrawings, never paper figures or measured results.
"""

from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET


OUT = Path(__file__).resolve().parent
W, H = 1200, 520
NAVY = "#0B2545"
BLUE = "#155C83"
TEAL = "#087F8C"
ORANGE = "#B96920"
RED = "#B84343"
INK = "#1B2838"
MUTED = "#526477"
LINE = "#C8D3DE"
PALE = "#F4F7FA"
PBLUE = "#EAF3F8"
PTEAL = "#E8F4F2"
PORANGE = "#FFF2E5"
PRED = "#FCEEEE"


class SVG:
    def __init__(self):
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
            '<rect width="1200" height="520" fill="#FFFFFF"/>',
        ]

    def shape(self, tag, **attrs):
        a = " ".join(f'{k.replace("_", "-")}="{escape(str(v), quote=True)}"' for k, v in attrs.items())
        self.parts.append(f"<{tag} {a}/>")

    def rect(self, x, y, w, h, fill="#FFFFFF", stroke=LINE, rx=12, sw=2, dash=None):
        attrs = dict(x=x, y=y, width=w, height=h, rx=rx, fill=fill,
                     stroke=stroke, stroke_width=sw)
        if dash:
            attrs["stroke_dasharray"] = dash
        self.shape("rect", **attrs)

    def line(self, x1, y1, x2, y2, color=BLUE, width=4, dash=None):
        attrs = dict(x1=x1, y1=y1, x2=x2, y2=y2, stroke=color,
                     stroke_width=width, stroke_linecap="round")
        if dash:
            attrs["stroke_dasharray"] = dash
        self.shape("line", **attrs)

    def arrow(self, x1, y1, x2, y2, color=BLUE, width=4, dash=None, head=12):
        import math
        self.line(x1, y1, x2, y2, color, width, dash)
        angle = math.atan2(y2 - y1, x2 - x1)
        a = angle + 2.55
        b = angle - 2.55
        pts = [(x2, y2), (x2 + head * math.cos(a), y2 + head * math.sin(a)),
               (x2 + head * math.cos(b), y2 + head * math.sin(b))]
        self.shape("polygon", points=" ".join(f"{x:.1f},{y:.1f}" for x, y in pts), fill=color)

    def path(self, d, color=BLUE, width=4, fill="none", dash=None):
        attrs = dict(d=d, fill=fill, stroke=color, stroke_width=width,
                     stroke_linecap="round", stroke_linejoin="round")
        if dash:
            attrs["stroke_dasharray"] = dash
        self.shape("path", **attrs)

    def circle(self, cx, cy, r, fill="#FFFFFF", stroke=BLUE, sw=2):
        self.shape("circle", cx=cx, cy=cy, r=r, fill=fill, stroke=stroke, stroke_width=sw)

    def text(self, x, y, value, size=26, color=INK, weight=400, anchor="middle"):
        self.parts.append(
            f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" '
            f'font-weight="{weight}" text-anchor="{anchor}" '
            'font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif">'
            f'{escape(value)}</text>'
        )

    def lines(self, x, y, values, size=26, gap=34, color=INK, weight=400, anchor="middle"):
        for i, value in enumerate(values):
            self.text(x, y + i * gap, value, size, color, weight, anchor)

    def tag(self, x, y, value, color=BLUE, fill=PBLUE, w=None):
        w = w or max(105, 24 + len(value) * 19)
        self.rect(x, y, w, 42, fill, color, 21, 1.3)
        self.text(x + w / 2, y + 29, value, 21, color, 600)

    def save(self, name):
        self.parts.append("</svg>")
        path = OUT / name
        path.write_text("\n".join(self.parts) + "\n", encoding="utf-8")
        ET.parse(path)
        return path


def relation():
    s = SVG()
    blocks = [
        (35, BLUE, PBLUE, "DAS 光电混合集成", "具体物理系统", ["光源→传感光纤", "→相干接收与解调"]),
        (420, TEAL, PTEAL, "光子 AI 计算", "计算硬件", ["输入→光学线性核", "→探测与电子处理"]),
        (805, ORANGE, PORANGE, "Agentic PIC Design", "设计方法与工具链", ["需求→工具调用", "→物理证据与修正"]),
    ]
    for x, c, pale, title, kind, body in blocks:
        s.rect(x, 70, 350, 280, pale, c, 14, 2.2)
        s.rect(x, 70, 350, 58, c, c, 12, 0)
        s.text(x + 175, 108, title, 25, "#FFFFFF", 700)
        s.text(x + 175, 173, kind, 29, c, 700)
        s.lines(x + 175, 229, body, 24, 38)
    s.arrow(978, 371, 210, 371, ORANGE, 3, "9 8", 11)
    s.arrow(978, 405, 595, 405, ORANGE, 3, "9 8", 11)
    s.text(595, 452, "Agent 方法可服务物理场景或计算硬件；这是候选联系，非已完成路线", 24, MUTED)
    s.save("01-three-goals.svg")


def evidence_labels():
    s = SVG()
    s.rect(30, 174, 245, 172, PBLUE, BLUE, 16, 2.5)
    s.lines(152, 225, ["论文原文 / 固定源码", "公开数据与实验条件"], 25, 46, BLUE, 700)
    rows = [
        (26, BLUE, PBLUE, "FACT / CODE VERIFIED", "可直接定位的结构、方法或源码行为", "报告为可核对事实"),
        (149, TEAL, PTEAL, "AUTHOR CLAIM", "论文给出但本项目未独立复算的指标", "说清作者与测试条件"),
        (272, ORANGE, PORANGE, "INFERENCE", "多篇工作之间的能力与缺口判断", "标为调研推论"),
        (395, RED, PRED, "UNKNOWN", "原文、数据或条件仍不足", "明确保留未决项"),
    ]
    for y, c, pale, label, definition, use in rows:
        s.arrow(283, 260, 346, y + 52, c, 3)
        s.rect(356, y, 470, 102, pale, c, 12, 2)
        s.text(380, y + 39, label, 23, c, 700, "start")
        s.text(380, y + 76, definition, 20, INK, 400, "start")
        s.arrow(832, y + 51, 883, y + 51, c, 3)
        s.rect(891, y, 283, 102, "#FFFFFF", c, 12, 2)
        s.text(1032, y + 61, use, 23, c, 600)
    s.save("10-evidence-labels.svg")


def das_system():
    s = SVG()
    s.tag(28, 20, "发射光路", BLUE, PBLUE, 136)
    s.tag(516, 20, "传感介质", TEAL, PTEAL, 136)
    s.tag(794, 20, "接收与解调", ORANGE, PORANGE, 180)
    items = [
        (24, 112, 185, "窄线宽光源", ["相干光"], BLUE, PBLUE),
        (250, 112, 187, "调制 / 放大", ["脉冲或扫频"], BLUE, PBLUE),
        (492, 112, 210, "传感光纤", ["瑞利后向散射"], TEAL, PTEAL),
        (764, 112, 182, "相干接收", ["偏振 / 混频"], ORANGE, PORANGE),
        (983, 112, 190, "PD/TIA/ADC", ["DSP / 事件输出"], ORANGE, PORANGE),
    ]
    for x, y, w, title, sub, c, pale in items:
        s.rect(x, y, w, 178, pale, c, 12, 2)
        s.text(x + w / 2, y + 47, title, 24, c, 700)
        s.text(x + w / 2, y + 139, sub[0], 21, MUTED)
    for a, b in [(209, 250), (437, 492), (702, 764), (946, 983)]:
        s.arrow(a + 4, 195, b - 8, 195, BLUE if a < 437 else TEAL if a < 702 else ORANGE, 4)
    # Optical-path cues, not a paper-specific circuit drawing.
    for yy in (185, 198, 211):
        s.line(66, yy, 150, yy, BLUE, 2)
    s.path("M 303 221 C 315 177 330 257 343 207 C 355 166 370 250 388 201", BLUE, 3)
    for cx, cy in [(548, 210), (583, 183), (611, 220), (647, 191)]:
        s.circle(cx, cy, 6, TEAL, TEAL, 1)
    s.line(801, 202, 896, 202, ORANGE, 3)
    s.line(812, 226, 896, 226, ORANGE, 3)
    s.circle(856, 214, 17, "#FFFFFF", ORANGE, 3)
    # The local-oscillator route returns from the source to the coherent receiver.
    s.path("M 108 298 L 108 379 L 850 379 L 850 297", BLUE, 3, dash="10 8")
    s.text(468, 368, "本振光参考支路", 22, BLUE, 600)
    s.text(602, 94, "沿线散射回波", 21, TEAL, 600)
    s.arrow(694, 315, 771, 315, TEAL, 3)
    s.text(600, 460, "距离、空间分辨率和灵敏度由整条链路及测试条件共同决定", 25, INK, 600)
    s.save("02-das-system.svg")


def das_integration():
    s = SVG()
    s.text(30, 37, "集成边界", 22, MUTED, 600, "start")
    s.text(855, 37, "仍在模块 / 芯片外", 22, MUTED, 600, "start")
    rows = [
        (75, "Jin 2024", BLUE, PBLUE, ["SOI PIC", "调制 + 相干收发"], ["窄线宽激光", "放大 / 采集 / DSP"], "真实 DAS：12.1 / 49 km（作者报告）"),
        (278, "Jin 2026", TEAL, PTEAL, ["InP 激光 + 微光学", "SOI PIC + TEC"], ["EDFA / 环行器", "AWG/TIA/DAQ + DSP"], "真实 DAS：10 km（作者报告）"),
    ]
    for y, name, c, pale, integrated, outside, evidence in rows:
        s.text(24, y + 35, name, 25, c, 700, "start")
        s.rect(168, y, 610, 164, pale, c, 16, 2.5)
        s.text(474, y + 38, integrated[0], 27, c, 700)
        s.text(474, y + 83, integrated[1], 24)
        s.text(474, y + 133, evidence, 21, MUTED)
        s.rect(831, y, 340, 164, PALE, MUTED, 16, 2, "9 7")
        s.lines(1001, y + 65, outside, 23, 42)
        s.arrow(780, y + 82, 824, y + 82, MUTED, 3)
    s.text(600, 495, "2026 年模块纳入激光；两项工作均未将完整 DAS 系统集成在片上", 24, INK, 600)
    s.save("03-das-integration.svg")


def photonic_system():
    s = SVG()
    s.tag(40, 22, "电域输入", BLUE, PBLUE, 132)
    s.tag(420, 22, "光域线性计算", TEAL, PTEAL, 194)
    s.tag(922, 22, "电域输出", ORANGE, PORANGE, 132)
    blocks = [
        (20, 112, 180, "电子输入", "编码 / DAC", BLUE, PBLUE),
        (238, 112, 160, "电光调制", "数据加载", BLUE, PBLUE),
        (440, 95, 320, "光学算子", "MVM / 卷积 / 相关", TEAL, PTEAL),
        (800, 112, 165, "光电探测", "PD / ADC", ORANGE, PORANGE),
        (1005, 112, 175, "电子处理", "非线性 / 输出", ORANGE, PORANGE),
    ]
    for x, y, w, title, sub, c, pale in blocks:
        h = 220 if x == 440 else 188
        s.rect(x, y, w, h, pale, c, 12, 2.2)
        s.text(x + w / 2, y + 52, title, 25, c, 700)
        s.text(x + w / 2, y + h - 38, sub, 22, MUTED)
    for a, b in [(200, 238), (398, 440), (760, 800), (965, 1005)]:
        s.arrow(a + 4, 207, b - 7, 207, TEAL if a >= 398 and a <= 760 else BLUE if a < 398 else ORANGE)
    # Interferometric core glyph: two channels, couplers, programmable phase.
    for yy in (195, 235):
        s.line(480, yy, 715, yy, TEAL, 4)
    s.line(548, 195, 578, 235, TEAL, 3)
    s.line(548, 235, 578, 195, TEAL, 3)
    s.line(648, 195, 678, 235, TEAL, 3)
    s.line(648, 235, 678, 195, TEAL, 3)
    s.circle(612, 195, 12, "#FFFFFF", TEAL, 3)
    s.text(612, 185, "φ", 22, TEAL, 700)
    s.path("M 1080 308 L 1080 415 L 592 415 L 592 339", ORANGE, 3, dash="9 7")
    s.text(826, 402, "权重设置 / 校准 / 控制反馈", 22, ORANGE, 600)
    s.text(600, 482, "完整推理系统还包含激光、转换、存储、控制与数据移动", 24, INK, 600)
    s.save("04-photonic-system.svg")


def photonic_families():
    s = SVG()
    data = [
        (28, BLUE, PBLUE, "MZI / 相干网格", "相位干涉 → 矩阵变换", "片上 PDNN / PACE", "漂移、插损与校准"),
        (418, TEAL, PTEAL, "MRR / WDM / 微梳", "波长并行 → 加权累加", "微梳卷积 / Netcast", "热漂移与光源开销"),
        (808, ORANGE, PORANGE, "衍射 / 芯粒系统", "传播与相位调制", "ACCEL / Taichi", "对准、重构与接口"),
    ]
    for x, c, pale, title, method, works, limit in data:
        s.rect(x, 25, 362, 450, "#FFFFFF", LINE, 14, 2)
        s.rect(x, 25, 362, 63, pale, c, 12, 2)
        s.text(x + 181, 66, title, 25, c, 700)
        s.text(x + 181, 300, method, 23, INK, 600)
        s.tag(x + 34, 330, works, c, pale, 294)
        s.text(x + 181, 438, limit, 22, MUTED)
    # MZI mesh (conceptual crossing of two waveguide channels).
    for yy in (155, 205):
        s.line(75, yy, 330, yy, BLUE, 4)
    for xx in (123, 236):
        s.line(xx, 155, xx + 35, 205, BLUE, 3)
        s.line(xx, 205, xx + 35, 155, BLUE, 3)
    s.circle(204, 155, 11, "#FFFFFF", BLUE, 3)
    # Ring-resonator bank on a bus waveguide.
    s.line(460, 194, 735, 194, TEAL, 4)
    for xx in (505, 592, 679):
        s.circle(xx, 156, 30, "#FFFFFF", TEAL, 4)
        s.circle(xx, 156, 6, TEAL, TEAL, 1)
    # Diffractive planes and fan-out rays.
    for xx in (885, 957, 1029):
        s.rect(xx, 123, 12, 126, PORANGE, ORANGE, 3, 2)
    for yy in (145, 185, 225):
        s.path(f"M 847 185 L 885 {yy} L 963 {185 + (yy-185)*0.65} L 1035 {185 + (yy-185)*0.35} L 1116 {yy}", ORANGE, 2)
    s.save("05-photonic-families.svg")


def capability_matrix():
    s = SVG()
    left = 212
    widths = [205, 205, 205, 205, 165]
    colnames = ["结构化输入", "工具执行", "仿真证据", "评价", "版图 / 规则"]
    for j, (w, name) in enumerate(zip(widths, colnames)):
        x = left + sum(widths[:j])
        s.rect(x, 35, w - 6, 58, NAVY, NAVY, 5, 0)
        s.text(x + (w - 6) / 2, 73, name, 22, "#FFFFFF", 700)
    rows = [
        ("PhIDO", BLUE, PBLUE, ["YAML DSL", "GDS 生成", "SAX 电路", "结构 / DRC", "GDS / DRC"]),
        ("AutoPD", TEAL, PTEAL, ["脚本约束", "Agent 迭代", "真实 solver", "预设 FoM", "局部检查"]),
        ("PICBench", ORANGE, PORANGE, ["JSON netlist", "生成 + 反馈", "SAX 模型", "golden 比较", "未展示"]),
        ("gdsfactory", MUTED, PALE, ["PDK / netlist", "确定性 API", "求解器适配", "调用者决定", "GDS / DRC"]),
    ]
    for i, (name, c, pale, values) in enumerate(rows):
        y = 106 + i * 87
        s.rect(20, y, 178, 72, pale, c, 9, 2)
        s.text(109, y + 45, name, 23, c, 700)
        for j, (w, value) in enumerate(zip(widths, values)):
            x = left + sum(widths[:j])
            is_absent = value == "未展示"
            fill = PALE if is_absent else pale
            stroke = LINE if is_absent else c
            s.rect(x, y, w - 6, 72, fill, stroke, 7, 1.5)
            s.text(x + (w - 6) / 2, y + 44, value, 21, MUTED if is_absent else INK, 600)
    s.text(600, 490, "单元格表示文献 / 源码中可定位的环节；gdsfactory 为工具生态，不是 Agent 验证", 22, MUTED)
    s.save("07-capability-matrix.svg")


def evidence_gaps():
    s = SVG()
    rows = [
        (73, BLUE, PBLUE, "Agentic PIC", "结构链 + solver 在环", "跨工具证据 / 独立评价", "最小工具契约 + 证据账本"),
        (223, TEAL, PTEAL, "DAS 集成", "PIC / 混合模块进入实验", "系统指标→器件 / 封装", "需求—约束追溯图"),
        (373, ORANGE, PORANGE, "光子 AI", "芯片 / 任务级演示", "误差→精度 / 总成本", "统一边界与误差—成本链"),
    ]
    s.text(268, 42, "已有工作实际验证", 22, BLUE, 700)
    s.text(649, 42, "仍缺的连接（推论）", 22, RED, 700)
    s.text(1002, 42, "候选切入点（推论）", 22, ORANGE, 700)
    for y, c, pale, label, validated, gap, cut in rows:
        s.tag(16, y + 33, label, c, pale, 165)
        s.rect(194, y, 298, 105, pale, c, 12, 2)
        s.text(343, y + 61, validated, 22, INK, 600)
        s.arrow(500, y + 52, 559, y + 52, c, 4)
        s.circle(594, y + 52, 27, PRED, RED, 3)
        s.text(594, y + 61, "?", 29, RED, 700)
        s.rect(637, y, 255, 105, PRED, RED, 12, 2, "9 7")
        s.text(764, y + 61, gap, 21, INK, 600)
        s.arrow(898, y + 52, 930, y + 52, ORANGE, 3, "7 6")
        s.rect(942, y, 236, 105, PORANGE, ORANGE, 12, 2)
        s.text(1060, y + 60, cut, 21, INK, 600)
    s.save("08-evidence-gaps.svg")


def route_derivation():
    s = SVG()
    s.text(204, 42, "研究现状", 22, BLUE, 700)
    s.text(618, 42, "证据断点", 22, RED, 700)
    s.text(1010, 42, "候选路线", 22, ORANGE, 700)
    rows = [
        (81, "A", BLUE, PBLUE, "PhIDO + solver 在环", "跨工具证据不可直接互认", "证据优先 Harness"),
        (229, "B", TEAL, PTEAL, "DAS PIC / 混合模块", "系统需求难传到芯片约束", "DAS 约束传播"),
        (377, "C", ORANGE, PORANGE, "光子核 + 任务演示", "精度与总成本口径不一", "光子 AI 证据链"),
    ]
    for y, label, c, pale, status, gap, route in rows:
        s.circle(45, y + 49, 31, c, c, 1)
        s.text(45, y + 60, label, 28, "#FFFFFF", 700)
        s.rect(94, y, 313, 101, pale, c, 12, 2)
        s.text(250, y + 60, status, 23, INK, 600)
        s.arrow(416, y + 50, 485, y + 50, c, 4)
        s.rect(493, y, 316, 101, PRED, RED, 12, 2, "8 7")
        s.text(651, y + 60, gap, 22, INK, 600)
        s.arrow(817, y + 50, 877, y + 50, ORANGE, 4)
        s.rect(887, y, 288, 101, PORANGE, ORANGE, 12, 2)
        s.text(1031, y + 59, route, 24, ORANGE, 700)
    s.save("09-route-derivation.svg")


def cross_direction_matrix():
    s = SVG()
    left = 198
    columns = [
        (left, BLUE, PBLUE, "DAS｜传感系统", "PIC / 混合模块", "真实光纤实验", "需求→器件 / 封装"),
        (left + 330, TEAL, PTEAL, "光子 AI｜任务计算", "干涉 / WDM / 衍射", "芯片与任务演示", "误差→精度 / 成本"),
        (left + 660, ORANGE, PORANGE, "Agentic PIC｜方法", "输入 / 工具 / 验证", "局部工具闭环", "独立评价 / 跨层"),
    ]
    labels = [(142, "主要路径"), (259, "文献已验证"), (376, "待补证据")]
    for y, name in labels:
        s.text(28, y + 37, name, 24, MUTED, 700, "start")
    for x, c, pale, title, path, proven, missing in columns:
        s.rect(x, 24, 315, 86, c, c, 12, 2)
        s.text(x + 157, 76, title, 23, "#FFFFFF", 700)
        for y, value, fill, border in [
            (142, path, pale, c),
            (259, proven, pale, c),
            (376, missing, PRED, RED),
        ]:
            s.rect(x, y, 315, 93, fill, border, 11, 2, "8 6" if y == 376 else None)
            s.text(x + 157, y + 57, value, 23, INK, 600)
        s.arrow(x + 157, 236, x + 157, 257, c, 3)
        s.arrow(x + 157, 353, x + 157, 374, RED, 3)
    s.save("11-cross-direction-matrix.svg")


if __name__ == "__main__":
    for fn in (relation, evidence_labels, das_system, das_integration, photonic_system,
               photonic_families, capability_matrix,
               evidence_gaps, route_derivation, cross_direction_matrix):
        fn()
    print("Built 10 source-linked SVG diagrams")
