"""Author SVG diagrams and outline; presentation-skill builds the PowerPoint."""
import json
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent
A = ROOT / "assets"
A.mkdir(exist_ok=True)
INK, TEAL, BLUE, ORANGE, MUTED = "#18364a", "#167b78", "#466a96", "#b76b32", "#536570"
PALE, MINT, SAND = "#eaf0f7", "#e6f3ef", "#fbefe3"

def txt(x, y, s, size=27, color=INK, bold=False, anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Microsoft YaHei,Arial" font-size="{size}" fill="{color}" font-weight="{700 if bold else 400}">{escape(s)}</text>'

def rect(x,y,w,h,fill=PALE,stroke="#c9d8df",dash=False):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" stroke="{stroke}" stroke-width="2"'+(' stroke-dasharray="8 6"' if dash else '')+'/>'

def arrow(x1,y1,x2,y2,color=TEAL,dash=False):
    return f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="{color}" stroke-width="3" marker-end="url(#arr)"'+(' stroke-dasharray="8 6"' if dash else '')+'/>'

def path(d,color=TEAL,dash=False):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="3" marker-end="url(#arr)"'+(' stroke-dasharray="8 6"' if dash else '')+'/>'

def box(x,y,w,h,title,lines=(),fill=PALE):
    out=rect(x,y,w,h,fill)+txt(x+w/2,y+40,title,28,bold=True)
    for i,s in enumerate(lines): out+=txt(x+w/2,y+78+31*i,s,23,MUTED)
    return out

def save(name,b):
    defs='<defs><marker id="arr" markerWidth="9" markerHeight="8" refX="8" refY="4" orient="auto"><path d="M0,0 L9,4 L0,8Z" fill="#167b78"/></marker></defs>'
    (A/f"{name}.svg").write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="520" viewBox="0 0 1400 520">{defs}<rect width="1400" height="520" fill="white"/>{b}</svg>',encoding="utf-8")
    return f"assets/{name}.svg"

# 1: the application hands requirements to the design loop, not to a finished chip.
b=box(25,175,230,150,"应用需求",["功能 · 损耗 · 约束"],MINT)
b+=arrow(260,250,325,250)
for i,(t,detail) in enumerate([("设计","结构 / 参数"),("仿真","模型 / 求解"),("分析","指标 / 原因"),("修改","动作 / 复核")]):
    x=335+i*265
    b+=box(x,175,225,150,t,[detail])
    if i<3:b+=arrow(x+230,250,x+263,250)
b+=path("M1242,333 L1242,388 L446,388 L446,335")
b+=txt(850,425,"重复迭代：下一步该改哪里？为什么这样改？",28,TEAL,True)
b+=rect(335,65,1020,67,MINT)+txt(845,108,"拟用 Harness 组织设计工具、反馈与迭代状态",29,TEAL,True)
b+=txt(145,364,"与 DAS 模块的接口",21,MUTED)
p1=save("p01-design-loop",b)

# 2: information flow and responsibilities.
b=rect(35,35,1330,70,MINT)+txt(700,79,"Harness：围绕 Agent 组织工具执行、状态保存和验证检查",30,TEAL,True)
for x,t,ls,fill in [(40,"需求与约束",["目标指标","工艺 / 几何条件"],PALE),(370,"Agent",["规划设计","解释结果 / 选动作"],MINT),(700,"专业工具",["CAD / 仿真器","产生结构与数值结果"],PALE),(1030,"确定性评价",["计算指标","检查约束与达标"],PALE)]:
    b+=box(x,165,290,180,t,ls,fill)
for x in [335,665,995]:b+=arrow(x,255,x+30,255)
b+=path("M1175,355 L1175,420 L515,420 L515,355")
b+=txt(840,462,"反馈：指标 + 条件 + 检查结果",26,TEAL,True)
b+=txt(185,457,"版本与轨迹持续记录",23,MUTED)
p2=save("p02-harness-roles",b)

# 4: a diagnosis becomes useful when it predicts a testable next step.
b=txt(700,50,"候选研究问题：如何利用物理知识与真实反馈选择下一步？",30,TEAL,True)
stages=[(40,"仿真结果",["功率 / 光谱 / 场分布","模型与求解条件"],PALE),(490,"物理诊断",["哪里偏离目标？","提出原因假设"],SAND),(940,"设计决策",["改参数 / 换策略","或补充验证"],MINT)]
for x,t,ls,col in stages:b+=box(x,145,420,180,t,ls,col)
b+=arrow(465,235,485,235)+arrow(915,235,935,235)
b+=rect(490,375,870,90,MINT)+txt(925,412,"把诊断写成可检验预测",27,TEAL,True)+txt(925,447,"下一轮仿真是否支持预测？",25,MUTED)
b+=path("M1150,333 L1150,368")+path("M485,420 L245,420 L245,333")
b+=txt(245,467,"新证据可修正原假设",22,MUTED)
p4=save("p04-research-focus",b)

# 5: rule gate, solver, diagnosis, action and independent check.
b=rect(25,32,355,65,PALE)+txt(202,74,"输入：目标 · 变量 · 约束",25,bold=True)
b+=rect(430,32,935,65,SAND)+txt(897,74,"研究集中区域：结果解释、原因诊断、动作选择",27,ORANGE,True)
b+=box(30,140,310,155,"候选设计与规则检查",["生成参数 / 结构","几何、工艺条件"],PALE)
b+=box(425,140,310,155,"执行数值仿真",["明确模型与求解条件","返回指标及场 / 谱"],PALE)
b+=box(820,140,545,155,"诊断 → 选择下一步动作",["结合知识与反馈提出假设","给出可由后续仿真检验的预测"],SAND)
b+=arrow(345,220,420,220)+arrow(740,220,815,220)
b+=box(820,350,545,120,"独立检查：指标与约束是否满足",["达标则输出；未达标则继续 / 转人工"],MINT)
b+=arrow(1090,302,1090,345)
b+=path("M815,410 L185,410 L185,302")
b+=txt(490,385,"更新设计 / 补充验证 / 回退",25,TEAL,True)
b+=txt(470,470,"保存：输入条件 · 设计版本 · 动作理由 · 后续结果",22,MUTED)
p5=save("p05-proposed-loop",b)

# 6: schematic only, no invented numerical curves or physical diagnosis.
b=txt(405,43,"1×2 MMI 示意：多模干涉分光器",28,bold=True)
b+=rect(65,170,155,26,MINT,TEAL)+rect(220,118,400,135,PALE,BLUE)
b+=rect(620,142,155,26,MINT,TEAL)+rect(620,205,155,26,MINT,TEAL)
b+=txt(110,147,"输入",22,MUTED)+txt(420,183,"多模区",31,bold=True)
b+=txt(420,292,"可编辑参数：长度、宽度、输出位置等",24,MUTED)
b+=txt(820,162,"P₁",28,TEAL,True)+txt(820,227,"P₂",28,TEAL,True)
b+=rect(920,90,430,200,SAND)+txt(1135,135,"假设观察到分光不均衡",27,ORANGE,True)
b+=txt(1135,185,"先检查模型与仿真条件",25)+txt(1135,233,"再提出设计参数相关假设",25)
for i,(t,ls) in enumerate([("提出假设",["预测参数改变的影响"]),("检验假设",["扫描 / 复算，核对趋势"]),("修改与复核",["同时检查均衡与损耗"])]):
    x=65+i*440
    b+=box(x,345,380,125,t,ls,[SAND,PALE,MINT][i])
    if i<2:b+=arrow(x+386,405,x+434,405)
p6=save("p06-mmi-example",b)

# 7: questions and candidate evaluation, not a study specification.
b=txt(700,50,"拟在相同任务、工具与预算下比较方法价值",30,TEAL,True)
for i,(t,ls) in enumerate([("设计结果",["目标是否达成","约束是否满足"]),("执行成本",["求解器调用次数","迭代与时间成本"]),("决策可靠性",["预测与新结果是否一致","错误动作能否被发现"])]):
    b+=box(40+i*450,120,420,165,t,ls,[PALE,MINT,SAND][i])
b+=txt(700,330,"候选对照：普通工具调用 Agent · 物理引导 Agent · 适用的数值优化",25,MUTED)
for i,(t,ls) in enumerate([("基础器件",["MMI 等"]),("仿真在环验证",["方法与对照"]),("复杂 PIC / DAS",["后续应用候选"])]):
    x=70+i*450
    b+=box(x,380,360,120,t,ls,[PALE,MINT,PALE][i])
    if i<2:b+=arrow(x+365,440,x+442,440)
p7=save("p07-evaluation-route",b)

titles=["从应用需求到芯片设计：为什么需要 Harness？","Harness 如何连接 AI 与专业工具？","已有 PIC Agent 做到了哪一步？","我的研究问题：仿真之后如何决定下一步？","拟议方法：建立可验证的设计闭环","MMI 示例：分光不均衡时怎么办？","如何验证价值，并对接 DAS？"]
subtitles=["课题方向：面向光子芯片自主设计的 Agent Harness","模型提出方案，专业工具与评价器提供可核验依据","输出、反馈来源和成功定义必须一起看","关注仿真结果 → 物理诊断 → 设计决策","物理反馈驱动的诊断与决策｜拟议架构，尚未实现","结构与诊断过程示意｜未运行实验，无性能数据","验证思路为候选；任务、预算和判据待后续明确"]
times=[45,60,65,60,90,75,55]
notes=[
"前面同学介绍的是 DAS 系统的组成和需求。我的部分关注这些需求进入芯片设计流程之后，如何借助 AI 组织设计、仿真和修改。以一个器件为例，工程师先选择结构和参数，运行仿真，分析结果，再决定怎么修改。这一循环需要反复执行。我的课题方向是研究 Agent Harness，让模型能够通过专业工具获得反馈，并组织后续动作。这里汇报的是候选方向。",
"Harness 可以理解为围绕智能体运行的执行框架。它接收设计目标与约束，把设计动作交给 CAD 或仿真工具，同时保存当前设计版本和执行过程。Agent 负责规划、解释和动作选择；仿真器返回数值结果，评价器计算指标并检查条件。评价反馈再进入下一轮。模型的解释不能直接作为物理正确性的依据，数值结果也要连同模型和仿真设置一起检查。",
"已有工作证明了不同环节的可行性。PhIDO 将自然语言转成结构化设计和版图，主要基准评价结构有效性。PICopilot 面向脚本生成，内部反馈主要是静态代码和自定义检查，外部基准执行脚本并评分。Kharel 的工作已经有显式规则、真实数值求解器、定量验收和迭代，所以不能认为已有方法都只会写代码。但其多物理初设曾需要专家纠正。三项工作的成功定义不同，不能拿单一成功率排序。",
"我的兴趣集中在仿真之后。结果不理想时，智能体能否定位性能瓶颈，提出原因假设，再选择修改参数、改变策略或补充验证？诊断需要形成可检验的预测，例如某个参数的变化应影响哪类指标。下一轮结果才能检验这个解释是否有用。这是当前拟研究的问题；既有仿真闭环是否已经具备足够的诊断能力，以及该方法是否有额外价值，都还需要核验。",
"拟议闭环从明确目标、变量与约束开始。生成候选结构后先检查几何和工艺条件，再运行数值仿真，并保存材料、模型和求解条件。Agent 根据反馈与器件知识提出诊断假设，选择下一步动作。动作可以是修改参数、做补充扫描，或回退到上一个设计。确定性评价器重新检查指标与约束；满足条件时输出，不满足时继续或转人工。研究重点在图中的结果诊断与动作选择，而 Harness 保存执行状态和证据，使整个过程可追溯。图是研究设想，没有表示我们已经实现这一系统。",
"用一个一进二出 MMI 分光器说明。图中只是简化结构，不是具体论文器件或实验数据。假设仿真返回两路输出功率不均衡，首先要确认输入、模型和求解设置是否适用。随后提出可检验的候选原因，例如某些几何参数的变化是否会影响均衡。通过参数扫描或复算核对趋势，证据支持时才进行修改，再同时检查均衡和损耗。如果新结果不支持假设，就修正诊断，而不是继续沿着错误解释修改。这说明一次物理诊断应如何落到工具动作和后续验证。",
"方法的价值需要比较来证明。未来拟在相同任务、工具和预算下，对比普通工具调用 Agent、物理引导 Agent，以及适用的数值优化方法。关注三类问题：设计是否达标，执行花了多少成本，诊断和动作是否可靠。先在基础器件上建立证据，再讨论复杂 PIC。DAS 可以作为后续复杂应用场景之一，与同学的系统方向形成接口。具体任务和指标尚未确定；目前没有方法优越性的实验证据。"
]
source="来源：候选方向材料 §2–6；拟议概念，非已实现系统"
slides=[]
for i in range(7):
    s={"id":f"s{i+1}","type":"content","variant":"flow","slide_intent":"process","title":titles[i],"subtitle":subtitles[i],"notes":f"计划用时：{times[i]} 秒。\n\n{notes[i]}","footer":source,"sources":[source]}
    if i==2:
        s.update(variant="table",slide_intent="evidence",headers=["工作","主要输出","反馈来源","成功 / 验证边界"],rows=[
            ["PhIDO","结构化设计 / GDS","Schema、DRC；部分 SAX","主基准：结构有效\n不能推出光学性能达标"],
            ["PICopilot","PIC 设计脚本","内部静态检查\n外部执行评分","脚本功能正确\n内部非物理仿真闭环"],
            ["Kharel 2026","设计与迭代日志","规则 + 数值仿真\n定量验收","仿真闭环已展示\n初设与评价依赖专家"]
        ],column_weights=[0.15,0.22,0.26,0.37],caption="研究切入点：诊断与动作选择能否带来可证明的增益？",footer="依据：PhIDO Fig.1/Table II；PICopilot §3.6/4；Kharel Fig.1/Table S2（详细 DOI 见备注）")
        s["sources"]=[s["footer"]]
        s["notes"]+="\n\n来源：Sharma et al., PhIDO, DOI:10.1063/5.0300741；Jiang et al., PICopilot, DOI:10.48550/arXiv.2608.01791；Kharel et al., Autonomous agentic design for photonics, DOI:10.48550/arXiv.2606.00915。论文能力与结果来自既有核读记录，不是本项目复现。"
    else:
        s["assets"]={"diagram":[p1,p2,None,p4,p5,p6,p7][i]}
    if i==5:s["footer"]="来源：候选方向材料 §4、§6；MMI 简化结构与假设情境，非论文原图或实验结果";s["sources"]=[s["footer"]]
    if i==2:
        s["header_style"]={"fontSize":18}
        s["row_styles"]=[{"fontSize":16,"fill":"FFFFFF","border_color":"D1DDE3"},{"fontSize":16,"fill":"F0F5F6","border_color":"D1DDE3"},{"fontSize":16,"fill":"FFFFFF","border_color":"D1DDE3"}]
        s.pop("caption",None)
        s.pop("footer",None)
    else:
        s["footer"]+=f"｜{i+1}/7"
    slides.append(s)

def write(name,obj): (ROOT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
write("design_brief.json",{"topic":"Harness 课堂课题方向汇报","content_maturity":"technical/educational","audience_posture":"students/learners","format_promise":"白底、少修饰、图示解释机制、可与 DAS 拼接","anti_format":["独立封面/目录/附录","通用科技插图","捏造实验曲线","重复三卡片"],"canvas_and_grid":{"aspect":"16:9","margin_x_in":0.4,"footer_reserve_in":0.4},"structure_strategy":{"primary_scaffold":"核心判断与一张主要图示","allowed_variations":["flow","table"],"container_policy":"仅用于实际模块、状态与对照字段"},"design_dna":"custom classroom research explanation"})
write("content_plan.json",{"topic":"Agent Harness","audience":"课堂同学与教师","objective":"在7–8分钟内解释课题问题、方法、验证与DAS关系","thesis":"物理反馈驱动的诊断与决策是当前候选研究主线","narrative_arc":[{"act":"problem","slides":["s1","s2"]},{"act":"evidence and question","slides":["s3","s4"]},{"act":"method and example","slides":["s5","s6"]},{"act":"evaluation","slides":["s7"]}],"slide_plan":[{"slide_id":s["id"],"role":"evidence" if i==2 else "mechanism","message":subtitles[i],"variant":s["variant"],"visual_strategy":"table" if i==2 else "vector-diagram","planned_seconds":times[i]} for i,s in enumerate(slides)]})
write("evidence_plan.json",{"sources":["../../references/task-007/candidate-research-direction.md","../../references/task-016-evidence/agentic-pic-comparison.md","../../references/task-016-evidence/evidence-log.md"],"claims":[{"slide":"s3","level":"FACT / AUTHOR CLAIM","scope":"既有论文方法与验证层级","locator":"三项目比较与原文定位"},{"slides":["s1","s2","s4","s5","s7"],"level":"USER RESEARCH PREFERENCE / INFERENCE","scope":"拟议概念与候选评价"},{"slide":"s6","level":"INFERENCE","scope":"MMI 结构与假设观察，仅示意，未运行实验"}],"unknown":["相对已有仿真闭环的创新性","相同预算下的净增益","诊断预测与结果一致性","跨器件泛化"]})
write("outline.json",{"title":"面向光子芯片自主设计的 Agent Harness","subtitle":"课堂汇报｜Harness 模块｜初版","deck_style":{"font_pair":"system_clean_v1","visual_density":"medium","emoji_mode":"none","research_visual_mode":False,"header_mode":"stack","footer_mode":"source-line","footer_page_numbers":True},"compliance":{"auto_image_sources":False,"require_attribution":False},"slides":slides})
(ROOT/"speaker-notes.md").write_text("# Harness 课堂讲稿｜初版\n\n计划总时长 7 分 30 秒；未经实际试讲。\n\n"+"\n\n".join(f"## P{i+1}｜{titles[i]}（{times[i]} 秒）\n\n{notes[i]}" for i in range(7))+"\n",encoding="utf-8")
(ROOT/"notes.md").write_text("# 制作与证据边界\n\n7 页、16:9、无附录。时间为规划，尚未试讲。仅使用已核验项目资料。P3 是文献方法比较；其他图为依据候选方向材料绘制的概念图，非已实现架构。P6 无数值数据或已确认的原因。标题、说明、表格和备注可编辑；技术图为 SVG 矢量，可通过源文件修改或在 PowerPoint 中转换为形状。拼接时统一字体、页码，推荐保留当前浅色背景。\n",encoding="utf-8")
brief=json.loads((ROOT/"design_brief.json").read_text(encoding="utf-8"))
brief["title_page_concept"]={"chosen_archetype":"content opener for concatenation","dominant_element":"应用到设计循环；不设置独立封面"}
write("design_brief.json",brief)
evidence=json.loads((ROOT/"evidence_plan.json").read_text(encoding="utf-8"))
evidence["items"]=[
    {"id":"ev1","claim":"PhIDO 主基准评价结构有效性","source_url":"https://doi.org/10.1063/5.0300741","source_note":"Fig.1/Table II；既有核读记录","used_on_slides":["s3"],"visual_use":"table"},
    {"id":"ev2","claim":"PICopilot 内部静态检查与外部执行评分不同","source_url":"https://doi.org/10.48550/arXiv.2608.01791","source_note":"§3.6/4；既有核读记录","used_on_slides":["s3"],"visual_use":"table"},
    {"id":"ev3","claim":"Kharel 展示规则、求解器、定量验收闭环，初设曾需专家修正","source_url":"https://doi.org/10.48550/arXiv.2606.00915","source_note":"Fig.1/Table S2","used_on_slides":["s3"],"visual_use":"table"},
    {"id":"ev4","claim":"拟议物理诊断与决策主线及MMI示意","source_note":"references/task-007/candidate-research-direction.md §2–6；未验证设想","used_on_slides":["s1","s2","s4","s5","s6","s7"],"visual_use":"footer-source"}
]
write("evidence_plan.json",evidence)
print("Authored 7 slides; planned 450 seconds.")
