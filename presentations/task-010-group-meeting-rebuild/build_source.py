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
    b=rect(52,70,800,310,MINT,stroke=TEAL,rx=5,sw=3)
    b+=text(452,112,"Jin 2024 SOI PIC 功能清单（据 Fig. 1(b)）",24,TEAL,weight="bold")
    for x,title,detail in [(82,"发射","MZM"),(275,"辅助光路","PC + BS"),(488,"相干混合","PBRS + 90° hybrid"),(690,"探测","4×BPD")]:
        b+=box(x,175,160,130,title,detail,PALE,21,17)
    b+=box(900,72,420,120,"片外光学","窄线宽激光 · EDFA · 环行器",SAND,24,19)
    b+=box(900,255,420,120,"片外电子与处理","AWG · TIA · DAQ · DSP",SAND,24,19)
    b+=line(853,180,892,135,ORANGE,3,False,True)+line(853,275,892,310,ORANGE,3,False,True)
    b+=text(700,483,"12.1 km：1.14 m / 59 pε/√Hz；49.0 km：3.78 m / 81 pε/√Hz",22,INK,weight="bold")
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


def diagram_ahmed():
    b=text(700,69,"Ahmed 2025：光电混合张量核与数字系统协同",29,TEAL,weight="bold")
    units=[(35,"Host / PCIe","模型与数据"),(282,"DCI / SRAM","权重·调度·接口"),(575,"DAC → PTC","128×128 MVP"),(878,"ADC / 输出流水","量化·累加"),(1160,"模型任务","分类/语言")]
    for i,(x,a,c) in enumerate(units):
        w=215 if i in (0,4) else 245
        b+=box(x,154,w,160,a,c,PALE if i in (0,1,4) else MINT,23,18)
        if i<4:b+=line(x+w+4,234,[277,570,873,1155][i],234)
    b+=rect(272,350,840,95,SAND,stroke="#dfc8b6",rx=3)
    b+=text(690,388,"电子：编译、控制、存储、非线性、累加、校准",22,INK,weight="bold")
    b+=text(690,424,"光电混合：矩阵向量乘法；4 个 PTC + 2 个 DCI",20,GREY)
    b+=text(700,481,"CIFAR-10：86.4% vs FP32 88.3%；SQuAD F1：12.0 vs 43.5",19,INK)
    b+=text(700,526,"65.5×10¹² ABFP16 ops/s ≠ 任务吞吐；功耗口径需含外围",19,ORANGE)
    return svg("p09-ahmed-system",b)


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
    b+=text(1030,70,"求解器在环的设计循环",30,TEAL,weight="bold")
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
    cols=["核心输入","Agent / 知识","工具或反馈","输出与判据","物理约束边界"]
    rows=[("PhIDO",["NL 设计需求","两 Agent + RAG","GDS/DRC/SAX","有效图/版图","PDK 组件/规则"]),
          ("PICopilot",["NL 脚本任务","多 Agent + 手册 RAG","内部静态检查","脚本/外部评分","非内部仿真反馈"]),
          ("Kharel",["人定目标/约束","编码 Agent + 日志","DRC + 真求解器","数值达标/迭代","显式规则；专家初设"])]
    b=""
    cw=218
    b+=rect(35,58,1330,72,INK,rx=0)
    for j,c in enumerate(["研究工作"]+cols):b+=text(145+j*cw,104,c,20,"#ffffff",weight="bold")
    for i,(name,vals) in enumerate(rows):
        y=130+i*118
        b+=rect(35,y,1330,118,"#f5f8f6" if i%2==0 else "#ffffff",rx=0)
        b+=text(145,y+66,name,24,INK,weight="bold")
        for j,v in enumerate(vals):
            color=ORANGE if "非内部" in v or "专家" in v else GREY
            b+=text(145+(j+1)*cw,y+66,v,18,color)
    b+=text(700,535,"验证层级不同：结构/GDS、脚本功能、数值求解；不能用单一成功率排序",19,TEAL,weight="bold")
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
            7:diagram_ai(),8:diagram_ai_arch(),9:diagram_ahmed(),10:diagram_mmi(),
            11:diagram_agent(),12:diagram_harness(),16:diagram_matrix(),
            17:diagram_compare(),18:diagram_questions(),19:diagram_inclination()}


def flow(n,title,subtitle,message,footer,notes,diagrams):
    return {"type":"content","variant":"flow","slide_intent":"evidence","visual_intent":"flow",
            "title":title,"subtitle":subtitle,"message":message,"assets":{"diagram":diagrams[n]},
            "footer":footer,"sources":[footer],"notes":notes}


def figure(n,title,subtitle,path,sections,caption,footer,notes):
    return {"type":"content","variant":"image-sidebar","slide_intent":"evidence","visual_intent":"hero",
            "title":title,"subtitle":subtitle,"assets":{"hero_image":path},"image_side":"left",
            "sidebar_sections":[{"title":a,"body":b} for a,b in sections],"caption":caption,
            "footer":footer,"sources":[footer],"notes":notes}


def build():
    d=make_diagrams()
    slides=[
        {"type":"title","title":"面向光子芯片智能设计的\n国内外研究现状与\n技术路线分析",
         "title_layout":"masthead","kicker":"PIC_HARNESS_RESEARCH · 组会调研",
         "subtitle":"DAS 光电混合集成 · 光子人工智能计算 · Agentic PIC Design\n汇报人：林子涵｜纤维光学与生物光子学课题组｜2026 年 9 月 29 日（证据增强版）",
         "notes":"开场说明：本次为三个目标的调研汇报，重点深入 Agentic PIC Design；后半部分提出个人倾向供组内讨论，尚未确定正式课题。"},
        flow(2,"三个研究目标：对象不同，可能交叉","物理系统、计算硬件与设计方法分别建立证据链", "先分别理解三个技术体系，再讨论交叉", "来源：项目 README；TASK-007 正式调研报告 §1", "DAS 关注分布式感知系统的光电集成；光子 AI 关注光学硬件承担推理运算；Agentic PIC 关注智能设计方法与专业工具协同。三者并列，不是既定实施阶段。",d),
        flow(3,"从论文进展走向可讨论的研究问题","既看技术方法，也看实际验证与边界", "证据核验决定候选路线是否成立", "来源：TASK-007 正式调研报告 §方法；全文证据审计", "本轮是结构化范围综述，不是穷尽式系统综述。依次核对研究对象、代表工作、原文证据，再归纳待研究问题；作者主张、本项目核验与未知项分开表述。",d),
        flow(4,"DAS：从光纤后向散射恢复沿线扰动","发射、传感、相干接收与解调是一条完整信号链", "PIC 可承担部分光学收发功能", "依据：TASK-007 正式调研报告 §DAS 原理；Jin 等 2024/2026", "窄线宽光经调制形成探测光进入传感光纤。扰动改变沿线 Rayleigh 后向散射，回波与本振在相干接收端转换为电信号，采集与 DSP 解调得到距离和振动。箭头分别表示发射与返回路径。",d),
        flow(5,"Jin 2024：SOI 芯片进入真实 DAS 收发链路","片上 MZM、偏振处理、相干混合与探测；片外模块另列", "系统指标必须连同光纤长度和测量条件报告", "根据 Jin 等（2024）Fig. 1(b)/3/5/6 改绘；doi:10.1364/PRJ.512298", "图依据 Jin 2024 Fig. 1(b) 和 Fig. 3 改绘，不是论文原图。Fig. 5：12.1 km、100 Hz PZT、0.819 m gauge length 下为 1.14 m 与 59 pε/√Hz；Fig. 6：49.0 km、4.01 m gauge length 下为 3.78 m 与 81 pε/√Hz。均为作者报告。窄线宽激光、EDFA、环行器、AWG、TIA、DAQ 和 DSP 仍片外；论文原始数据未公开。Sandmann 2023 Fig. 2/5 另展示通信 IC-TROSA 复用于 20 km 后 200 Hz 声学实验，是不同路线，不能用指标直接比较。",d),
        figure(6,"Cheng 2023：四微环结构针对 DAS 发射脉冲","原论文 Fig. 1 显示耦合微环、透射谱与脉冲响应","assets/cheng-fig1-device-spectrum.png",
               [("结构","4 个 10 µm 微环 + PIN 注入；通带与带外抑制"),("器件","动态 ER 68 dB；3.60 mW；上升/下降 6.54/0.40 ns"),("系统边界","2 km DAS 为 EOM 子模块替换；激光/EDFA/接收仍片外")],
               "Cheng 等（2023），Nature Communications，Fig. 1(a–f) 原图；CC BY 4.0。", "doi:10.1038/s41467-023-43244-9；Fig. 1/2/4/5",
               "Fig. 1(a) 是四微环结构，(d) 是不同 DC 偏压的原始透射谱，(f) 是脉冲响应。Fig. 2(a) 静态 71 dB、Fig. 2(c) self-heterodyne 动态 68 dB，不能混为一个测量。3.60 mW 是高占空比驱动下 EOM 本体功耗，非全系统。Fig. 4/5 的 2 km Φ-OTDR 台架报告 4 pε/√Hz，与商用 AOM 替换对照。作者指出温漂、硅非线性和约 6.5 ns 响应限制。"),
        flow(7,"光子 AI：把线性运算放进光学路径","以 y = W x 为例，输入和权重需被编码到光场", "电子系统仍承担控制、非线性与结果处理", "依据：TASK-007 正式调研报告 §光子 AI；Wetzstein 等 2020, Nature", "以矩阵向量乘法说明：电子数据编码到光，光学网络实现线性变换，探测转换为电信号。完整推理还涉及激光、调制器、存储、非线性、校准和电子输出；不能只计光学核心能耗。",d),
        flow(8,"三类光学计算架构，限制条件各不相同","MZI、微环/WDM 与衍射传播分别利用不同物理机制", "架构比较要回到任务、接口与系统边界", "依据：TASK-007 正式调研报告 §3；Zhou 等 2021；Feldmann 等 2021", "MZI 用相位和干涉形成可调线性变换；微环与波分复用利用波长选择和加权；衍射结构利用传播与相位调制形成任务相关映射。图是通用机理简化图，并非某篇论文的实际器件版图。",d),
        flow(9,"Ahmed 2025：光子核心与电子系统共同运行 AI","根据原论文 Fig. 2 改绘；任务准确率见 Table 1", "光电混合矩阵乘法与完整推理性能要分别报告", "根据 Ahmed 等（2025）Fig. 1/2、Table 1 改绘；doi:10.1038/s41586-025-08854-x", "原论文 Fig. 2(a–c) 把 host、DCI、PTC 和 ABFP 计算链分开。本图是根据原文改绘，不是论文原图。4 个 128×128 PTC 与 2 个 DCI；作者报告 65.5×10¹² ABFP16 ops/s、78 W 电子功率和 1.6 W 光功率。Table 1：ResNet18 CIFAR-10 86.4% 对 FP32 88.3%；BERT-Tiny IMDb 83.2% 对 86.2%，但 SQuAD F1 12.0 对 43.5。ImageWoof 结果经过专门重新训练。主文未给完整统一墙插和各任务能耗；Methods 另列八只激光器每只 1.25 W 电功率。",d),
        flow(10,"以 1×2 MMI 为例：设计需要穿过物理验证链","从性能要求到几何、仿真、优化、版图与检查", "可用工具自动化；物理达标仍须由求解器和验证器判断", "依据：TASK-005 技术地图；TASK-007 §Agentic PIC；概念示意", "用 1×2 MMI 贯穿后续三页。输入目标包括两路功率分配、损耗、波长及工艺边界；宽度 W、长度 L 是可调几何参数。仿真检查传输与不平衡，版图需满足 DRC。此页是教学示例，没有运行仿真。",d),
        flow(11,"脚本生成与物理求解器循环的验证层级不同","左：生成代码；右：规则闸门、求解器数值、评价与迭代", "要核对反馈实际来自静态检查还是物理仿真", "依据：PICopilot §3.6/§4.1.4；Kharel §2/Fig. 1", "此图右侧是 Kharel 等 Fig. 1 和 §2 支持的通用求解器在环路径，不代表 PICopilot 已实现。PICopilot 内部 Script Evaluator 用静态代码检查、自定义检查库和 LLM，benchmark 才在外部执行脚本并比对参考输出；因此其 48/48 不是 Agent 内部电磁仿真迭代证据。Kharel 的 acceptance criteria 由工程师给定。",d),
        flow(12,"Agentic PIC 参考架构：约束必须进入工具链","需求、设计知识、专业工具与物理反馈形成可追溯循环", "这是跨论文参考架构，不是单篇论文完成的系统", "综合 TASK-005 参考架构与 TASK-007 §4 改绘", "1×2 MMI 的要求先形成可检查设计规范；Agent/Harness 管理步骤与工具接口；器件模型和 PDK 提供知识边界；仿真、版图和 DRC 给出可核验输出。反馈不应由模型自评代替物理计算。图为综合参考架构。",d),
        figure(13,"PhIDO：自然语言进入研究级 PIC 设计流程","原论文 Fig. 1 连接解释、设计、版图与电路验证","assets/phido-fig1.png",
               [("输入","自然语言 → 实体/规格 → YAML DSL 与 Pydantic 校验"),("工具","gdsfactory 生成 GDS/DRC；部分任务经 SAX 电路模型"),("验证边界","102 个 prompt；结构/电路级 proof-of-concept，非 foundry signoff")],
               "Sharma 等（2025），APL Machine Learning，Fig. 1 原图；CC BY 4.0。", "doi:10.1063/5.0300741；Fig. 1",
               "解释图中四段：interpreter、designer、layout、circuit verification；前两段是 LLM Agent，后两段主要是算法模块。102 个 prompt 中 level 1/2/3/4 为 23/10/60/9，7 模型每题各 5 次。Fig. 5 显示复杂度升高后成功率下降；正文报告单器件最高约 91%、levels 1–3 汇总 pass@5 最高 58%。Table II 的 S 仅要求有效 schematic 与 GDSII。FDTD 分支未进入主发布；结构成功不等于性能达标或 foundry signoff。"),
        figure(14,"PICopilot：多 Agent 协作生成 PIC 设计脚本","原论文 Fig. 2 展示任务分解、检索、合成与静态评价","assets/picopilot-fig2.png",
               [("任务","48 个脚本任务：基础 12 / 中等 12 / 高级 24"),("内部反馈","静态检查 + 自定义检查库 + LLM；并非求解器反馈"),("外部评分","脚本运行结果与参考输出相符；≥3/15 次才计 solved")],
               "Jiang 等（2026），ICCAD 论文预印本，Fig. 2 原图；学术汇报引用。", "arXiv:2608.01791；Fig. 2",
               "图中 PIC Designer 提供任务；Task Planner 分解，Function-specific Script Generator 经手册 RAG 生成代码，Script Synthesizer 汇总。§3.6 明确 Script Evaluator 内部用静态代码检查、自定义检查库和 LLM，不直接运行耗时的 PIC 工具。§4.1.4 的 benchmark 另运行脚本，功能结果与参考一致算 trial 成功，至少 3/15 次计 task solved。作者报告 48/48、总 pass@1 93.9%、pass@5 99.9%；都不是物理性能资格验证。本项目未核实公开实现。"),
        figure(15,"AutoPhotonicDesign：真实物理求解器驱动迭代","原论文 Fig. 2 展示被动弯曲器件的 50 次实验过程","assets/autopd-fig2.png",
               [("规则与反馈","人类定目标；显式 DRC → Tidy3D 等求解器 → 定量验收"),("原图案例","12 µm SiN 弯曲：0.460 → 0.109 dB，50 次预算"),("边界","多物理 MZM 初始设置由专家纠错；结果是数值仿真")],
               "Kharel 等（2026），arXiv:2606.00915，Fig. 2 原图；学术汇报引用。", "arXiv:2606.00915；Fig. 2",
               "红叉为丢弃尝试、绿点为保留结果、绿线为迄今最优。弯曲器件是 400 nm SiN、1550 nm、150 nm 最小特征、12 µm 半径的仿真；50 是预算，最优在第 38 次。Fig. 3 另有 39 次 PN 结迭代、Fig. 5 有 192→0 DRC violations。多物理 MZM 首次在 30 GHz 得到约 15 Ω，参考值 48 Ω；Table S2 记录专家修正 mode 识别及 junction shunt 等设置，之后才进入九设计的自治循环。故不应宣称无条件独立理解物理。"),
        flow(16,"PhIDO、PICopilot、Kharel：成功定义不同","结构/GDS、脚本功能、数值验收分别位于不同层级", "比较 Agent 能力时先写清输入、反馈和约束来源", "依据：PhIDO Fig. 1/Table II；PICopilot Fig. 2/Table 2–3；Kharel Fig. 1/Table S2", "完整八列比较表在 references/task-016-evidence/agentic-pic-comparison.md。PhIDO 的 S 是有效 schematic/GDSII；PICopilot 的 #Solved 是脚本外部运行后参考输出相符、至少 3/15 次；Kharel 是人类提供规则和定量目标后以求解器数值通过验收。它们不能按 91%、48/48 和器件损耗作单一能力排名。",d),
        flow(17,"三方向形成不同的候选研究问题","综合比较研究对象、已验证进展和仍待考察的边界", "A/B/C 是调研候选，不是已选课题", "依据：TASK-006 候选路线；TASK-007 候选路线总结", "路线 A 正式名称为证据优先的 Agentic PIC Harness 方法研究，B 是 DAS 系统需求到光电混合集成约束的可追溯传播，C 是光子 AI 的器件误差—任务精度—系统成本联合证据链。图中是压缩后的题眼；三条均不是已选课题，不能用单一成熟度排序。个人更希望进一步研究 Agentic PIC 中真实物理设计问题。",d),
        flow(18,"从需求理解到物理验证：约束能否贯穿设计？","四层技术问题对应不同论文已有能力和待核证据", "优先深入需求理解与物理约束处理", "依据：PhIDO Fig. 1；PICopilot Fig. 2；AutoPD Fig. 2；PICBench；TASK-007 §研究缺口", "PhIDO 与 PICBench 展示结构化表示；AutoPhotonicDesign 展示人类设定约束后的求解器循环；PICopilot 展示脚本评价。值得进一步核验的是复杂物理约束的表达、一致性、跨工具传递与设计过程保持，而不是断言整个领域没有物理约束能力。",d),
        flow(19,"个人倾向：从物理约束理解切入真实 PIC 设计","Agentic PIC Design 是主要方向；具体技术方案尚待讨论", "需求解析是基础能力，不预设为最终创新点", "来源：用户确认的个人倾向；TASK-007 候选路线仅作背景", "总体目标是让 AI 在专业工具与物理要求支持下参与真实器件/电路设计。当前优先研究设计需求理解和物理约束处理，随后可能延伸到工具执行、仿真反馈与跨任务复用。三个未决问题：已有方法做到何种程度；侧重表达、冲突、传递还是保持；选择什么物理任务验证价值与通用性。",d),
        {"type":"content","variant":"comparison-2col","title":"总结与组内讨论","subtitle":"以证据约束判断，以具体设计任务收敛问题",
         "left":{"title":"三点收获","body":["DAS、光子 AI、Agentic PIC 的研究对象与技术体系不同","Agentic PIC 已覆盖结构、脚本、仿真在环等不同能力层级","个人倾向优先关注需求理解与物理约束处理"]},
         "right":{"title":"两个讨论问题","body":["是否适合优先深入 PIC 设计需求与物理约束处理？","下一阶段聚焦哪些具体技术问题和代表工作，才能明确研究贡献？"]},
         "verdict":"当前是研究倾向，不是已确定的课题、算法或实验计划。",
         "footer":"来源：TASK-007 正式报告与候选路线；用户确认的最新研究倾向",
         "sources":["TASK-007 正式报告与候选路线；用户确认的最新研究倾向"],
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
                       "visual_strategy":"original-figure" if i+1 in [6,13,14,15] else ("technical-diagram" if "diagram" in s.get("assets",{}) else "comparison")}
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
