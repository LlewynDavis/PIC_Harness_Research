"""Author source diagrams and outline for TASK-010. Run with the workspace Python.

The PowerPoint is built by presentation-skill, not by this script.
"""
from __future__ import annotations

import json
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

INK = "#19383b"
TEAL = "#167a73"
MINT = "#d6eee7"
BLUE = "#466a96"
PALE = "#e9f0f8"
ORANGE = "#c8763d"
SAND = "#f8ede3"
GREY = "#58656a"
LIGHT = "#edf1ee"
RED = "#a54d4d"


def svg(name, body, width=1400, height=560):
    p = ASSETS / f"{name}.svg"
    p.write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
        '<defs><marker id="arr" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">'
        f'<path d="M0,0 L10,4 L0,8 Z" fill="{TEAL}"/></marker>'
        '<marker id="back" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">'
        f'<path d="M0,0 L10,4 L0,8 Z" fill="{ORANGE}"/></marker></defs>'
        f'<rect width="{width}" height="{height}" fill="#ffffff"/>{body}</svg>', encoding="utf-8")
    return f"assets/{name}.svg"


def text(x, y, s, size=28, color=INK, anchor="middle", weight="normal"):
    return f'<text x="{x}" y="{y}" fill="{color}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" font-family="Microsoft YaHei,Arial,sans-serif">{escape(s)}</text>'


def rect(x, y, w, h, fill=LIGHT, stroke="none", rx=8, sw=2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def line(x1, y1, x2, y2, color=TEAL, width=4, arrow=True, dash=False):
    marker = (' marker-end="url(#arr)"' if color == TEAL else ' marker-end="url(#back)"') if arrow else ""
    style = ' stroke-dasharray="10 7"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{marker}{style}/>'


def box(x, y, w, h, title, detail="", fill=LIGHT, title_size=27, detail_size=20):
    s = rect(x,y,w,h,fill,stroke="#d5e1dd",rx=4)
    s += text(x+w/2,y+min(42,h*.38),title,title_size,INK,weight="bold")
    if detail:
        for i,t in enumerate(detail.split("|")):
            s += text(x+w/2,y+min(77,h*.65)+i*25,t,detail_size,GREY)
    return s


def diagram_two():
    b = ""
    specs = [
        (60,"DAS 光电混合集成","物理系统 / 感知","光源·调制·接收·光纤","真实传感链路与集成边界",PALE),
        (485,"光子 AI 计算","计算硬件 / 推理","编码·光学线性运算·探测","任务性能与系统成本",MINT),
        (910,"Agentic PIC Design","设计方法 / 工具协同","需求·约束·仿真·验证","面向多类 PIC 设计任务",SAND),
    ]
    for x,a,c,d,e,col in specs:
        b += rect(x,88,370,326,col,stroke="#c6d9d2",rx=4)
        b += text(x+185,145,a,29,INK,weight="bold")+text(x+185,194,c,23,TEAL)
        b += line(x+78,224,x+292,224,TEAL,3,False)
        b += text(x+185,271,d,22)+text(x+185,321,e,21,GREY)
    b += line(420,460,970,460,TEAL,3,False,True)
    b += text(700,508,"可能交叉：以具体器件任务检验设计方法；计算芯片也有设计自动化需求",22,GREY)
    return svg("p02-three-directions",b)


def diagram_three():
    b=""
    stages=[("领域地图","对象与路径"),("代表工作","方法与结果"),("证据核验","原文/代码/数据"),("研究问题","边界与缺口"),("候选路线","可检验问题")]
    for i,(a,c) in enumerate(stages):
        x=28+i*279
        b+=box(x,157,235,188,a,c,fill=[PALE,MINT,SAND,MINT,PALE][i],title_size=26)
        if i<4:b+=line(x+240,252,x+276,252)
    b+=text(700,445,"区分：论文提出 → 论文展示 → 独立核验 → 本项目尚未执行",27,TEAL,weight="bold")
    return svg("p03-evidence-chain",b)


def diagram_das():
    b=""
    b+=box(45,65,215,125,"窄线宽光源","相干光",PALE)
    b+=box(305,65,215,125,"调制/放大","发射脉冲",PALE)
    b+=box(560,65,210,125,"环行/耦合","收发分离",PALE)
    b+=line(260,128,300,128)+line(520,128,555,128)
    b+=f'<path d="M153,193 L153,246 L580,246 L580,274" fill="none" stroke="{BLUE}" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#arr)"/>'
    b+=text(358,235,"本振支路",19,BLUE)
    b+=line(770,128,850,128)
    b+=rect(850,70,470,110,"#eff8f4",stroke=TEAL,rx=55)
    b+=text(1085,117,"传感光纤",29,INK,weight="bold")
    b+=text(1085,153,"沿线扰动 → Rayleigh 后向散射",21,GREY)
    b+=line(850,193,746,278,ORANGE,4)
    b+=box(533,278,240,128,"相干接收","本振 + 90° 混合 + PD",SAND,24,20)
    b+=box(275,278,220,128,"TIA / ADC","电信号采集",LIGHT)
    b+=box(28,278,210,128,"DSP 解调","位置与振动",MINT)
    b+=line(533,342,499,342)+line(275,342,242,342)
    b+=text(700,492,"PIC 可集成发射与接收的部分光学功能；光纤、采集、DSP 等仍可在片外",22,GREY)
    return svg("p04-das-system",b)


def diagram_das_levels():
    b=""
    rows=[(75,"分立系统","激光 | 调制 | 光路 | 相干接收 | ADC/DSP",PALE),
          (205,"SOI 收发 PIC","MZM | 偏振处理 | 90° 混合 | 平衡 PD",MINT),
          (335,"混合集成模块","InP 激光 + 微光学 + SOI PIC + TEC",SAND)]
    for y,t,d,c in rows:
        b+=box(78,y,300,100,t,"",c)
        b+=line(385,y+50,432,y+50)
        b+=box(445,y,875,100,d,"",c,title_size=25)
    b+=text(700,503,"集成层级不同；外部放大、环行、采集和处理需分别核算",24,TEAL,weight="bold")
    return svg("p05-das-levels",b)


def diagram_jin():
    b=""
    b+=rect(72,110,900,285,"#f1f8f5",stroke=TEAL,rx=12,sw=3)
    b+=text(510,152,"40 × 40 × 10 mm 混合集成模块",28,TEAL,weight="bold")
    b+=box(110,195,220,125,"InP ECL","线宽 < 3 kHz",PALE)
    b+=box(395,195,220,125,"微透镜/隔离器","光学耦合",LIGHT)
    b+=box(683,195,230,125,"SOI 收发 PIC","MZM·90°混合·PD",MINT)
    b+=line(335,258,390,258)+line(620,258,678,258)
    b+=text(520,370,"TEC 温控",22,GREY)
    b+=line(975,254,1035,254)
    b+=box(1042,190,270,135,"10 km 光纤演示","外置 EDFA / DAQ / DSP",SAND,25,19)
    b+=text(700,475,"论文报告：约 4 m 空间分辨率；73.27 pε/√Hz（特定统计口径）",23,ORANGE)
    return svg("p06-jin-module",b)


def diagram_ai():
    b=""
    b+=text(700,88,"以 y = W x 的线性层为例",33,TEAL,weight="bold")
    units=[(40,"电子输入","向量 x / 权重 W",PALE),(295,"光学编码","调制幅度/相位",MINT),(550,"光学线性运算","干涉/耦合/传播",MINT),(830,"光电探测","光强 → 电信号",SAND),(1105,"电子后处理","非线性/存储/控制",PALE)]
    for i,(x,t,d,c) in enumerate(units):
        w=225 if i<4 else 255
        b+=box(x,185,w,175,t,d,c,title_size=24,detail_size=19)
        if i<4:b+=line(x+w+5,272,units[i+1][0]-8,272)
    b+=text(700,456,"激光、电光转换、校准、ADC 与控制都影响完整系统的能耗和时延",23,GREY)
    return svg("p07-ai-hybrid",b)


def diagram_ai_arch():
    b=""
    for i,(x,t,c,principle,issue) in enumerate([
        (55,"MZI 干涉网络",PALE,"相位调节 → 矩阵映射","校准/热漂移"),
        (490,"微环 / WDM",MINT,"共振选择 → 波长加权","串扰/温控"),
        (925,"衍射结构",SAND,"传播与相位调制","任务专用/接口")]):
        b+=rect(x,72,380,415,c,stroke="#c6d9d2",rx=4)
        b+=text(x+190,128,t,30,INK,weight="bold")
        if i==0:
            for j in range(3):
                b+=line(x+55,195+j*55,x+315,195+j*55,BLUE,3,False)
            for j in range(2):
                b+=f'<circle cx="{x+145+j*95}" cy="250" r="37" fill="none" stroke="{TEAL}" stroke-width="4"/>'
        elif i==1:
            b+=line(x+55,250,x+325,250,BLUE,5,False)
            for j in range(3):b+=f'<circle cx="{x+115+j*78}" cy="221" r="28" fill="none" stroke="{TEAL}" stroke-width="4"/>'
        else:
            for j in range(5):b+=line(x+55,190+j*25,x+310,260+(j-2)*20,ORANGE,2,False)
            for j in range(3):b+=line(x+150+j*55,175,x+150+j*55,325,BLUE,4,False)
        b+=text(x+190,390,principle,21)+text(x+190,443,issue,20,GREY)
    return svg("p08-ai-architectures",b)


def diagram_mmi():
    b=""
    b+=text(700,65,"1×2 MMI：输入波导 → 多模区 → 两个输出端口",30,TEAL,weight="bold")
    b+=rect(105,165,220,30,PALE,stroke=BLUE,rx=2)+rect(325,125,340,110,MINT,stroke=TEAL,rx=3,sw=3)
    b+=rect(665,139,210,27,PALE,stroke=BLUE,rx=2)+rect(665,194,210,27,PALE,stroke=BLUE,rx=2)
    b+=line(125,180,305,180,BLUE,4,False)
    b+=line(365,183,625,153,TEAL,3,False)+line(365,183,625,207,TEAL,3,False)
    b+=text(490,104,"宽度 W / 长度 L",21,GREY)
    b+=text(795,113,"输出功率与不平衡",21,GREY)
    stages=[("需求","目标/约束"),("建模","W、L、材料"),("仿真","传输/损耗"),("优化","改参数"),("版图/DRC","工艺规则"),("验证","性能复核")]
    for i,(t,d) in enumerate(stages):
        x=26+i*229
        b+=box(x,325,195,135,t,d,fill=SAND if i==0 else LIGHT,title_size=23,detail_size=17)
        if i<5:b+=line(x+197,391,x+227,391)
    return svg("p10-mmi-design",b)


def diagram_agent():
    b=""
    b+=text(360,70,"LLM 生成脚本",30,BLUE,weight="bold")
    b+=box(85,150,225,137,"自然语言需求","1×2 MMI",PALE)
    b+=box(410,150,225,137,"生成 Python","工程师执行/检查",PALE)
    b+=line(315,220,405,220)
    b+=text(1030,70,"Agent 工具循环",30,TEAL,weight="bold")
    nodes=[(740,130,"任务状态","目标/约束"),(1010,130,"工具调用","版图/仿真"),(1010,350,"结果评估","物理输出/错误"),(740,350,"下一步动作","修正或停止")]
    for x,y,t,d in nodes:b+=box(x,y,235,128,t,d,MINT if x==740 else SAND,title_size=23,detail_size=18)
    b+=line(979,195,1004,195)+line(1125,263,1125,344)+line(1005,415,979,415,ORANGE)+line(858,347,858,264,ORANGE)
    return svg("p11-agent-vs-llm",b)


def diagram_harness():
    b=""
    b+=box(35,178,225,160,"需求 / DesignSpec","目标·参数·物理约束",PALE,23,19)
    b+=box(333,141,325,238,"Agent / Harness","计划·状态·工具接口|结果检查·失败处理",MINT,27,20)
    b+=box(742,70,285,125,"设计知识","器件模型 / PDK",LIGHT,23,19)
    b+=box(742,235,285,170,"专业工具","几何/版图·DRC|电路/全波/多物理",SAND,23,19)
    b+=box(1112,178,252,160,"结果 / 证据","GDS·仿真·检查记录",PALE,23,19)
    b+=line(265,255,325,255)+line(662,255,735,312)+line(1035,312,1105,255)
    b+=line(883,196,883,228,TEAL,3)
    b+=line(1100,389,560,440,ORANGE,3)
    b+=text(825,461,"物理结果 / 检查反馈",19,ORANGE)
    b+=text(700,500,"参考架构：多篇工作的技术层级综合；不代表单篇论文完整实现",21,GREY)
    return svg("p12-reference-architecture",b)


def diagram_matrix():
    cols=["结构化需求","物理约束","工具执行","反馈优化","版图/验证","跨任务复用"]
    rows=[("PhIDO",["论文：YAML","论文：部分","论文+代码","论文：有限","论文：GDS/DRC","未明确"]),
          ("PICopilot",["作者：脚本","作者：条件","作者：脚本","作者：评价","作者：脚本","代码未核"]),
          ("AutoPD",["论文：人工设定","论文：人工设定","论文：求解器","论文：迭代","论文：器件","未明确"]),
          ("PICBench",["论文：JSON","论文：任务条件","论文：SAX","论文：重试","未含 GDS","论文：24 题"])]
    b=""
    w0=200; cw=192
    b+=rect(35,58,1330,72,INK,rx=0)
    for j,c in enumerate(["研究工作"]+cols):b+=text(132+j*cw,104,c,20,"#ffffff",weight="bold")
    for i,(name,vals) in enumerate(rows):
        y=130+i*90
        b+=rect(35,y,1330,90,"#f5f8f6" if i%2==0 else "#ffffff",rx=0)
        b+=text(132,y+52,name,24,INK,weight="bold")
        for j,v in enumerate(vals):
            color=TEAL if "代码" in v and "未" not in v else (ORANGE if v.startswith("作者") or "未" in v else GREY)
            b+=text(132+(j+1)*cw,y+52,v,18,color)
    b+=text(700,535,"论文=文中展示｜作者=作者报告｜代码=固定提交只读核验｜未明确/未核 ≠ 领域不存在",18,GREY)
    return svg("p16-capability-matrix",b)


def diagram_compare():
    data=[("DAS 混合集成","传感系统","光电收发前端","真实光纤演示","模块边界/约束传播"),
          ("光子 AI 计算","推理硬件","光学线性运算","任务级演示","误差–精度–系统成本"),
          ("Agentic PIC","设计方法","需求/工具/反馈","结构、脚本、仿真在环","可核验真实物理设计")]
    b=""
    xvals=[35,298,556,816,1070];widths=[260,258,258,250,295]
    for j,h in enumerate(["方向","研究对象","技术核心","已有进展","继续考察"]):
        b+=rect(xvals[j],44,widths[j],66,INK,rx=0)+text(xvals[j]+widths[j]/2,87,h,22,"#ffffff",weight="bold")
    for i,row in enumerate(data):
        y=110+i*94
        for j,v in enumerate(row):
            b+=rect(xvals[j],y,widths[j],94,[PALE,MINT,SAND][i],stroke="#ffffff",rx=0)
            b+=text(xvals[j]+widths[j]/2,y+55,v,20,INK,weight="bold" if j==0 else "normal")
    b+=text(700,440,"候选问题：A Agentic PIC 证据链    B DAS 设计约束传播    C 光子 AI 误差与任务精度",22,TEAL,weight="bold")
    b+=text(700,507,"三条路线均属待讨论候选；个人希望优先深入 Agentic PIC 的真实物理设计问题",20,GREY)
    return svg("p17-cross-direction",b)


def diagram_questions():
    stages=[("1 需求理解","目标、参数、缺失信息","PhIDO: YAML；PICBench: JSON"),
            ("2 物理约束处理","约束是否一致、可检查？","待进一步核验：复杂约束表达"),
            ("3 工具执行","模型、版图、求解器输入","PhIDO: GDS/DRC；AutoPD: solver"),
            ("4 结果验证反馈","实际物理结果决定调整","AutoPD: 仿真迭代；PICopilot: 脚本评价")]
    b=""
    for i,(t,d,e) in enumerate(stages):
        x=30+i*347
        c=SAND if i==1 else (MINT if i==3 else PALE)
        b+=rect(x,94,319,340,c,stroke=ORANGE if i==1 else "#ceddd8",rx=4,sw=4 if i==1 else 2)
        b+=text(x+159,158,t,25,INK,weight="bold")
        b+=text(x+159,244,d,19)
        b+=line(x+42,284,x+277,284,TEAL,2,False)
        for k,s in enumerate(e.split("；")):b+=text(x+159,337+k*30,s,18,GREY)
        if i<3:b+=line(x+324,262,x+341,262)
    b+=text(700,505,"图中“待核验”是研究问题，不是对整个领域能力的否定",21,GREY)
    return svg("p18-four-layers",b)


def diagram_inclination():
    b=""
    b+=box(65,28,1270,93,"总体目标：面向真实 PIC 设计任务的智能设计方法","AI 在物理要求与专业工具支持下参与器件/电路设计",PALE,25,19)
    b+=line(700,124,700,151)
    b+=box(208,159,984,91,"当前优先切入：需求理解 + 物理约束处理","结构化要求 · 识别关键条件 · 一致性检查 · 正确传递",MINT,25,19)
    b+=line(700,252,700,278)
    b+=box(135,285,1130,82,"后续可能扩展：工具执行 → 仿真验证 → 反馈优化 → 跨任务复用","以 1×2 MMI 等真实任务考察价值；具体方案尚未确定",SAND,22,18)
    b+=text(700,410,"尚未确定的三个问题",23,TEAL,weight="bold")
    qs=["已有方法的约束能力到何程度？","重点研究表达、冲突、传递还是保持？","用哪个真实物理任务验证价值与通用性？"]
    for i,q in enumerate(qs):
        x=25+i*461
        b+=rect(x,434,435,83,"#f7f9f8",stroke="#d8e5e0",rx=4)
        b+=text(x+217,485,f"Q{i+1}  {q}",18,INK)
    return svg("p19-research-inclination",b)


def make_diagrams():
    return {2:diagram_two(),3:diagram_three(),4:diagram_das(),5:diagram_das_levels(),
            6:diagram_jin(),7:diagram_ai(),8:diagram_ai_arch(),10:diagram_mmi(),
            11:diagram_agent(),12:diagram_harness(),16:diagram_matrix(),
            17:diagram_compare(),18:diagram_questions(),19:diagram_inclination()}


def flow(n,title,subtitle,message,footer,notes,diagrams):
    return {"type":"content","variant":"flow","slide_intent":"evidence","visual_intent":"flow",
            "title":title,"subtitle":subtitle,"message":message,"assets":{"diagram":diagrams[n]},
            "footer":footer,"notes":notes}


def figure(n,title,subtitle,path,sections,caption,footer,notes):
    return {"type":"content","variant":"image-sidebar","slide_intent":"evidence","visual_intent":"hero",
            "title":title,"subtitle":subtitle,"assets":{"hero_image":path},"image_side":"left",
            "sidebar_sections":[{"title":a,"body":b} for a,b in sections],"caption":caption,
            "footer":footer,"notes":notes}


def build():
    d=make_diagrams()
    slides=[
        {"type":"title","title":"面向光子芯片智能设计的\n国内外研究现状与\n技术路线分析",
         "title_layout":"masthead","kicker":"PIC_HARNESS_RESEARCH · 组会调研",
         "subtitle":"DAS 光电混合集成 · 光子人工智能计算 · Agentic PIC Design\n汇报人：林子涵｜纤维光学与生物光子学课题组｜2026 年 9 月 23 日",
         "notes":"开场说明：本次为三个目标的调研汇报，重点深入 Agentic PIC Design；后半部分提出个人倾向供组内讨论，尚未确定正式课题。"},
        flow(2,"三个研究目标：对象不同，可能交叉","物理系统、计算硬件与设计方法分别建立证据链", "先分别理解三个技术体系，再讨论交叉", "来源：项目 README；TASK-007 正式调研报告 §1", "DAS 关注分布式感知系统的光电集成；光子 AI 关注光学硬件承担推理运算；Agentic PIC 关注智能设计方法与专业工具协同。三者并列，不是既定实施阶段。",d),
        flow(3,"从论文进展走向可讨论的研究问题","既看技术方法，也看实际验证与边界", "证据核验决定候选路线是否成立", "来源：TASK-007 正式调研报告 §方法；全文证据审计", "本轮是结构化范围综述，不是穷尽式系统综述。依次核对研究对象、代表工作、原文证据，再归纳待研究问题；作者主张、本项目核验与未知项分开表述。",d),
        flow(4,"DAS：从光纤后向散射恢复沿线扰动","发射、传感、相干接收与解调是一条完整信号链", "PIC 可承担部分光学收发功能", "依据：TASK-007 正式调研报告 §DAS 原理；Jin 等 2024/2026", "窄线宽光经调制形成探测光进入传感光纤。扰动改变沿线 Rayleigh 后向散射，回波与本振在相干接收端转换为电信号，采集与 DSP 解调得到距离和振动。箭头分别表示发射与返回路径。",d),
        flow(5,"DAS 集成：比较功能边界，而非只比芯片尺寸","器件、PIC、混合模块与系统级演示是不同层级", "集成越高，外部功能边界越要写清", "依据：Jin 等 2024, Photonics Research；Jin 等 2026, OFC W4D.2", "2024 SOI PIC 集成调制、偏振处理、光学混合和平衡探测，激光及采集仍片外。2026 工作进一步把 InP 外腔激光、微光学、SOI PIC 和 TEC 封装在模块中，但并非完整系统片上化。",d),
        flow(6,"Jin 等：混合集成模块进入 10 km DAS 演示","InP 激光 + 微光学 + SOI 收发 PIC + TEC", "真实光纤演示成立；EDFA、采集与 DSP 仍外置", "根据 Jin 等（2026）OFC W4D.2 改绘；doi:10.1364/OFC.2026.W4D.2", "原始 PDF 在当前 Zotero 附件中未找到，因此按已核验会议论文与正式报告重绘。模块约 40×40×10 mm，激光线宽低于 3 kHz；作者在 10 km G.652.D 上报告约 4 m 空间分辨率与 73.27 pε/√Hz 特定统计口径应变分辨率。三页论文缺少完整功耗、良率、长期漂移和重复样本数据。",d),
        flow(7,"光子 AI：把线性运算放进光学路径","以 y = W x 为例，输入和权重需被编码到光场", "电子系统仍承担控制、非线性与结果处理", "依据：TASK-007 正式调研报告 §光子 AI；Wetzstein 等 2020, Nature", "以矩阵向量乘法说明：电子数据编码到光，光学网络实现线性变换，探测转换为电信号。完整推理还涉及激光、调制器、存储、非线性、校准和电子输出；不能只计光学核心能耗。",d),
        flow(8,"三类光学计算架构，限制条件各不相同","MZI、微环/WDM 与衍射传播分别利用不同物理机制", "架构比较要回到任务、接口与系统边界", "依据：TASK-007 正式调研报告 §3；Zhou 等 2021；Feldmann 等 2021", "MZI 用相位和干涉形成可调线性变换；微环与波分复用利用波长选择和加权；衍射结构利用传播与相位调制形成任务相关映射。图是通用机理简化图，并非某篇论文的实际器件版图。",d),
        figure(9,"ACCEL：任务级视觉演示与计算边界","原论文 Fig. 1(b) 展示衍射光学编码与模拟电子计算","assets/accel-fig1b.png",
               [("结构","衍射光学编码 OAC → 光电探测 → 模拟电子计算 EAC"),("实验","作者报告准确率：Fashion-MNIST 85.5%；三类 ImageNet 82.0%；视频 92.6%"),("边界","74.8 Peta-OPS/W 与 72 ns 使用论文定义口径；不可等同通用数字推理")],
               "Chen 等（2023），Nature，Fig. 1(b) 局部；CC BY 4.0。", "doi:10.1038/s41586-023-06558-8；PMC10620079，Fig. 1(b)",
               "原图 Fig. 1(b) 是 ACCEL 的 OAC 加模拟电子 EAC。论文在 Fashion-MNIST、三类 ImageNet 和延时视频识别给出任务级实验；作者报告 85.5%、82.0%、92.6% 准确率。性能数字依论文 operation 和系统定义，不能泛化为完整通用 AI 推理。"),
        flow(10,"以 1×2 MMI 为例：设计需要穿过物理验证链","从性能要求到几何、仿真、优化、版图与检查", "可用工具自动化；物理达标仍须由求解器和验证器判断", "依据：TASK-005 技术地图；TASK-007 §Agentic PIC；概念示意", "用 1×2 MMI 贯穿后续三页。输入目标包括两路功率分配、损耗、波长及工艺边界；宽度 W、长度 L 是可调几何参数。仿真检查传输与不平衡，版图需满足 DRC。此页是教学示例，没有运行仿真。",d),
        flow(11,"从 LLM 脚本生成到 Agent 工具循环","关键差别是能否读取工具结果并决定下一步", "工具调用不等于自动完成物理设计", "依据：TASK-005 能力/验证矩阵；PhIDO、PICopilot、AutoPD 原文", "单次脚本生成由工程师运行和检查。Agent 方法增加任务状态、工具接口、输出检查及下一步决策；是否真正闭环要看工具调用与验证证据。PICopilot 主要评价脚本输出，AutoPhotonicDesign 展示真实仿真迭代。",d),
        flow(12,"Agentic PIC 参考架构：约束必须进入工具链","需求、设计知识、专业工具与物理反馈形成可追溯循环", "这是跨论文参考架构，不是单篇论文完成的系统", "综合 TASK-005 参考架构与 TASK-007 §4 改绘", "1×2 MMI 的要求先形成可检查设计规范；Agent/Harness 管理步骤与工具接口；器件模型和 PDK 提供知识边界；仿真、版图和 DRC 给出可核验输出。反馈不应由模型自评代替物理计算。图为综合参考架构。",d),
        figure(13,"PhIDO：自然语言进入研究级 PIC 设计流程","原论文 Fig. 1 连接解释、设计、版图与电路验证","assets/phido-fig1.png",
               [("输入","自然语言 → 实体/规格 → YAML DSL 与 Pydantic 校验"),("工具","gdsfactory 生成 GDS/DRC；部分任务经 SAX 电路模型"),("验证边界","102 个 prompt；结构/电路级 proof-of-concept，非 foundry signoff")],
               "Sharma 等（2025），APL Machine Learning，Fig. 1 原图；CC BY 4.0。", "doi:10.1063/5.0300741；Fig. 1",
               "解释图中四个角色而非只念 Agent 名称。论文以 102 个 prompt 评价流程，作者报告单器件最高约 91%、≤15 元件电路 pass@5 约 57%。FDTD 分支因兼容性没有进入主发布。GDS/DRC 与 SAX 不等于实际器件性能或代工签核。"),
        figure(14,"PICopilot：多 Agent 协作生成 PIC 设计脚本","原论文 Fig. 2 展示任务分解、检索、合成与静态评价","assets/picopilot-fig2.png",
               [("任务","设计说明拆成版图、DRC、FDTD 等脚本子任务"),("方法","规划 + 工具手册检索 + 程序生成/合成 + 脚本评价"),("证据边界","48 个脚本任务；作者报告全部完成，未核验公开实现和自治执行")],
               "Jiang 等（2026），ICCAD 论文预印本，Fig. 2 原图；学术汇报引用。", "arXiv:2608.01791；Fig. 2",
               "图中 PIC Designer 提供任务；Task Planner 分解，Function-specific Script Generator 经手册检索生成代码，Script Synthesizer 汇总，Script Evaluator 做静态与自定义检查。论文的任务是脚本生成，不可把产出的 FDTD 脚本等同已经运行的物理结果。"),
        figure(15,"AutoPhotonicDesign：真实物理求解器驱动迭代","原论文 Fig. 2 展示被动弯曲器件的 50 次实验过程","assets/autopd-fig2.png",
               [("任务","人类定义目标、约束和评价程序"),("闭环","提出设计 → Tidy3D 求解 → 评价 → 保留/修正"),("边界","器件级仿真在环；专家设置和纠错仍重要")],
               "Kharel 等（2026），arXiv:2606.00915，Fig. 2 原图；学术汇报引用。", "arXiv:2606.00915；Fig. 2",
               "红叉是被丢弃尝试、绿点是保留结果、绿线是迄今最优。论文展示真实物理求解器输出驱动设计迭代，这是较强的仿真在环证据。但人类工程师准备 design.py/program.md 的目标、约束与 evaluator；多物理调制器例子还需要专家修正。图中横轴 50 experiments 不能直接转化为通用成功率。"),
        flow(16,"代表性工作覆盖了不同设计环节","对比的是论文所展示的任务与证据层级", "下一步需细查物理约束如何表达、传递和保持", "依据：TASK-005 能力矩阵；TASK-007 §4.2；四篇原文", "矩阵不是全领域支持/不支持判断。PhIDO 验证结构/电路流程；PICopilot 主要为脚本任务；AutoPhotonicDesign 有真实 solver；PICBench 通过 JSON netlist 与 SAX 评价。待核表示本轮论文证据未足以确定。",d),
        flow(17,"三方向形成不同的候选研究问题","综合比较研究对象、已验证进展和仍待考察的边界", "A/B/C 是调研候选，不是已选课题", "依据：TASK-006 候选路线；TASK-007 候选路线总结", "路线 A 正式名称为证据优先的 Agentic PIC Harness 方法研究，B 是 DAS 系统需求到光电混合集成约束的可追溯传播，C 是光子 AI 的器件误差—任务精度—系统成本联合证据链。图中是压缩后的题眼；三条均不是已选课题，不能用单一成熟度排序。个人更希望进一步研究 Agentic PIC 中真实物理设计问题。",d),
        flow(18,"从需求理解到物理验证：约束能否贯穿设计？","四层技术问题对应不同论文已有能力和待核证据", "优先深入需求理解与物理约束处理", "依据：PhIDO Fig. 1；PICopilot Fig. 2；AutoPD Fig. 2；PICBench；TASK-007 §研究缺口", "PhIDO 与 PICBench 展示结构化表示；AutoPhotonicDesign 展示人类设定约束后的求解器循环；PICopilot 展示脚本评价。值得进一步核验的是复杂物理约束的表达、一致性、跨工具传递与设计过程保持，而不是断言整个领域没有物理约束能力。",d),
        flow(19,"个人倾向：从物理约束理解切入真实 PIC 设计","Agentic PIC Design 是主要方向；具体技术方案尚待讨论", "需求解析是基础能力，不预设为最终创新点", "来源：用户确认的个人倾向；TASK-007 候选路线仅作背景", "总体目标是让 AI 在专业工具与物理要求支持下参与真实器件/电路设计。当前优先研究设计需求理解和物理约束处理，随后可能延伸到工具执行、仿真反馈与跨任务复用。三个未决问题：已有方法做到何种程度；侧重表达、冲突、传递还是保持；选择什么物理任务验证价值与通用性。",d),
        {"type":"content","variant":"comparison-2col","title":"总结与组内讨论","subtitle":"以证据约束判断，以具体设计任务收敛问题",
         "left":{"title":"三点收获","body":["DAS、光子 AI、Agentic PIC 的研究对象与技术体系不同","Agentic PIC 已覆盖结构、脚本、仿真在环等不同能力层级","个人倾向优先关注需求理解与物理约束处理"]},
         "right":{"title":"两个讨论问题","body":["是否适合优先深入 PIC 设计需求与物理约束处理？","下一阶段聚焦哪些具体技术问题和代表工作，才能明确研究贡献？"]},
         "verdict":"当前是研究倾向，不是已确定的课题、算法或实验计划。",
         "footer":"来源：TASK-007 正式报告与候选路线；用户确认的最新研究倾向",
         "notes":"结束时用三个收获复述证据边界，不作完成系统或实验承诺。请导师和师兄师姐优先讨论切入问题是否合适，以及用哪类具体 PIC 器件或电路任务检验其价值。预留问答。"}
    ]
    assert len(slides)==20
    outline={"title":"面向光子芯片智能设计的国内外研究现状与技术路线分析",
             "subtitle":"首次正式组会调研汇报",
             "deck_style":{"font_pair":"system_clean_v1","visual_density":"medium","emoji_mode":"none",
                           "research_visual_mode":True,"header_mode":"stack","title_layout":"masthead",
                           "title_motif":"none","footer_mode":"source-line","footer_page_numbers":True},
             "compliance":{"auto_image_sources":False,"require_attribution":False},"slides":slides}
    (ROOT/"outline.json").write_text(json.dumps(outline,ensure_ascii=False,indent=2),encoding="utf-8")
    (ROOT/"content_plan.json").write_text(json.dumps({"topic":outline["title"],"audience":"课题组师兄师姐及导师",
        "objective":"20 页 / 15–20 分钟，三方向综述后深入 Agentic PIC 并讨论个人倾向",
        "thesis":"Agentic PIC 值得从真实物理设计任务的需求与约束处理进一步研究",
        "narrative_arc":[{"act":"框架","slides":"P1–P3"},{"act":"DAS","slides":"P4–P6"},
                         {"act":"光子 AI","slides":"P7–P9"},{"act":"Agentic PIC","slides":"P10–P16"},
                         {"act":"综合与讨论","slides":"P17–P20"}],
        "slide_plan":[{"slide_id":f"P{i+1}","role":s.get("slide_intent","message"),
                       "message":s.get("message",s["title"]),"variant":s.get("variant","title"),
                       "visual_strategy":"original-figure" if i+1 in [9,13,14,15] else ("technical-diagram" if "diagram" in s.get("assets",{}) else "comparison")}
                      for i,s in enumerate(slides)]},ensure_ascii=False,indent=2),encoding="utf-8")
    (ROOT/"design_brief.json").write_text(json.dumps({"topic":outline["title"],"content_maturity":"technical/educational",
        "audience_posture":"research group","emotional_register":"trustworthy",
        "format_promise":"图示解释技术，原论文 Figure 证明真实工作；中文学术简洁版式",
        "anti_format":["旧版页面结构与布局","大幅装饰性 AI 图","整页 PDF 缩小","连续重复卡片"],
        "canvas_and_grid":{"aspect":"16:9","margin_x_in":0.5,"footer_reserve_in":0.32},
        "title_page_concept":{"chosen_archetype":"editorial masthead","dominant_element":"论文题目","supporting_element":"三个方向"},
        "structure_strategy":{"primary_scaffold":"解释性技术图 + 关键判断","repeated_elements":["来源底注","页码"],
                              "allowed_variations":["flow","image-sidebar","comparison-2col"],
                              "container_policy":"只为模块和证据边界加容器"},
        "design_dna":"editorial academic technical atlas","renderer_treatments":{"header_mode":"stack","title_layout":"masthead","footer_mode":"source-line"}},ensure_ascii=False,indent=2),encoding="utf-8")


if __name__=="__main__":build()
