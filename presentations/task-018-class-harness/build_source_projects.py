"""Author the project-focused revision using original paper figures."""
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from xml.sax.saxutils import escape

ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[1]
A=ROOT/"assets"
INK="#18364a"; TEAL="#167b78"; MUTED="#536570"
FONT=Path("C:/Windows/Fonts/msyh.ttc")

def write(name,obj):
    (ROOT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

def composition(name,image_path,sections,legend=None,annotation=None):
    canvas=Image.new("RGB",(1400,560),"white")
    im=Image.open(image_path).convert("RGB")
    image_box=(15,15,955,430 if legend else 535)
    im.thumbnail((image_box[2]-image_box[0],image_box[3]-image_box[1]),Image.Resampling.LANCZOS)
    canvas.paste(im,(image_box[0]+(image_box[2]-image_box[0]-im.width)//2,image_box[1]+(image_box[3]-image_box[1]-im.height)//2))
    draw=ImageDraw.Draw(canvas)
    if legend:
        lg=Image.open(legend).convert("RGB");lg.thumbnail((740,85),Image.Resampling.LANCZOS)
        canvas.paste(lg,(130,440))
    if annotation:
        draw.text((45,527),annotation,font=ImageFont.truetype(str(FONT),21),fill=MUTED)
    for i,(title,lines) in enumerate(sections):
        y=20+i*175
        draw.rounded_rectangle((985,y,1380,y+150),radius=4,fill=["#e6f3ef","#eaf0f7","#fbefe3"][i],outline="#cbd9df",width=2)
        draw.text((1005,y+13),title,font=ImageFont.truetype(str(FONT),27),fill=INK)
        for j,s in enumerate(lines):
            draw.text((1005,y+56+30*j),s,font=ImageFont.truetype(str(FONT),23),fill=MUTED)
    dest=A/f"{name}.png";canvas.save(dest)
    return f"assets/{name}.png"

old=REPO/"presentations/task-010-group-meeting-rebuild/assets"
p3=composition("project-phido-architecture",old/"phido-fig1.png",[
    ("自然语言进入设计流程",["解释需求 → 选器件","结构化 DSL → 版图"]),
    ("四段职责",["前两段：LLM Agent","后两段：CAD / 电路工具"]),
    ("验证边界",["主基准检验结构有效","FDTD 非主发布分支"]),
])
p4=composition("project-phido-benchmark",A/"papers/phido-fig5-panel.png",[
    ("102 个设计描述",["Level 1/2/3/4","任务数：23/10/60/9"]),
    ("左柱 @1，右柱 @5",["图中蓝色 S 为成功","复杂任务的成功仍有限"]),
    ("“成功”是什么？",["有效 schematic 与 GDS","不等同光学性能达标"]),
],legend=A/"papers/phido-fig5-legend.png",annotation="Fig. 5 局部：Gemini-2.5-pro/GPT-4o；保留原始颜色图例")
p5=composition("project-picopilot",old/"picopilot-fig2.png",[
    ("任务 → 脚本",["规划 → 检索增强生成","合成脚本 → 静态评价"]),
    ("48 项脚本任务（作者）",["Basic 12 / Medium 12","Advanced 24；15 次/任务","Solved：48/48（≥3/15）"]),
    ("内部与外部评价不同",["内部：静态检查 + LLM","外部：运行脚本并评分"]),
])
p6=composition("project-kharel-loop",A/"papers/kharel-fig1b.png",[
    ("人类提供起点",["目标、约束、仿真初设","评价器与可编辑参数"]),
    ("真实求解器在环",["Design → Verify → Simulate","数值结果决定保留 / 回退"]),
    ("关键能力与边界",["显式规则 + 定量验收","多物理初设曾由专家纠错"]),
])
p7=composition("project-kharel-result",A/"papers/kharel-fig2a.png",[
    ("弯曲损耗：作者仿真",["0.460 → 0.109 dB","50 次仿真预算"]),
    ("案例条件",["400 nm SiN；1550 nm","12 µm 半径；150 nm 最小特征"]),
    ("如何读这张图？",["绿色：保留 / 最优值","红色：丢弃；不是实测"]),
])

def text(x,y,s,size=28,color=INK,bold=False):
    return f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Microsoft YaHei,Arial" font-size="{size}" fill="{color}" font-weight="{700 if bold else 400}">{escape(s)}</text>'
b=""
for i,(title,desc,fill) in enumerate([
    ("PhIDO","自然语言 → 结构化设计与版图","#eaf0f7"),
    ("PICopilot","自然语言 → PIC 脚本与功能评价","#e6f3ef"),
    ("Kharel","显式规则 → 仿真反馈 → 定量迭代","#fbefe3")]):
    y=30+i*105
    b+=f'<rect x="30" y="{y}" width="1340" height="88" rx="4" fill="{fill}"/>'
    b+=text(190,y+53,title,30,bold=True)+text(860,y+53,desc,29)
b+=text(700,394,"已有项目构成方法基础，成功定义与验证层级需要区分",29,TEAL,True)
b+=text(700,455,"我的切入点：让仿真后的诊断与动作选择得到证据检验",30,INK,True)
b+=text(700,505,"方法增益待验证；DAS 可作为后续复杂应用场景",25,MUTED)
(A/"project-summary.svg").write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="540" viewBox="0 0 1400 540"><rect width="1400" height="540" fill="white"/>{b}</svg>',encoding="utf-8")

titles=[
    "课题方向：面向光子芯片设计的 Agent Harness",
    "研究切入点：仿真后的物理诊断与设计决策",
    "PhIDO：自然语言到结构化设计与版图",
    "PhIDO：102 个任务怎样评价“设计成功”？",
    "PICopilot：领域 RAG 与多 Agent 生成设计脚本",
    "Kharel：规则与数值仿真驱动的设计闭环",
    "Kharel 案例：在求解器反馈中优化波导弯曲",
    "总结：已有方法基础与我的研究切入点",
]
subtitles=[
    "Harness 组织模型、专业工具、状态与验证；与 DAS 需求模块衔接",
    "拟研究方向：诊断形成可检验预测，动作由后续结果验证",
    "原文 Fig. 1｜Interpreter → Designer → Layout → Circuit Verification",
    "原文 Fig. 5 局部｜用复杂度与失败阶段理解 benchmark",
    "原文 Fig. 2｜脚本生成反馈与 benchmark 执行评分分开理解",
    "原文 Fig. 1(b)｜目标、显式规则、求解器与验收条件共同作用",
    "原文 Fig. 2(a)｜数值仿真案例，不是流片测量结果",
    "从结构生成、脚本生成走向可检验的设计诊断与决策",
]
times=[55,55,60,50,65,65,70,40]
paths=["assets/p02-harness-roles.svg","assets/p04-research-focus.svg",p3,p4,p5,p6,p7,"assets/project-summary.svg"]
footers=[
    "依据：候选方向材料 §2–4；概念职责分工",
    "依据：候选方向材料 §2–4；拟研究问题，尚未验证",
    "Sharma et al., 2025, Fig. 1 (PDF p.3), DOI: 10.1063/5.0300741",
    "Sharma et al., 2025, Fig. 5 / Table II (PDF p.8–9), DOI: 10.1063/5.0300741",
    "Jiang et al., 2026, Fig. 2 / §3.6 / Table 3, DOI: 10.48550/arXiv.2608.01791",
    "Kharel et al., 2026, Fig. 1(b) / Table S2, DOI: 10.48550/arXiv.2606.00915",
    "Kharel et al., 2026, Fig. 2(a) / §S2.1 (PDF p.5/12–14), DOI: 10.48550/arXiv.2606.00915",
    "依据：TASK-016 三项目比较；候选方向材料 §2–8",
]
notes=[
    "前面同学介绍了 DAS 系统，我的课题关注这些需求进入芯片设计之后，AI 如何组织设计工具。Harness 是围绕 Agent 的执行框架，接收目标和约束，组织 CAD、仿真与确定性检查，保存版本和轨迹。Agent 负责规划与动作选择，专业工具提供数值结果，评价器复核目标。这个分工是理解后面三个现成项目的共同入口。我们当前汇报的是候选研究方向。",
    "课题重点放在仿真后的结果分析和决策。性能偏离目标时，Agent 能否提出有依据的原因假设，并决定修改参数、换策略或补充验证？诊断需要形成下一轮可检验的预测。反馈不支持预测时，就修正假设。现有 Agent 是否已经具备足够能力，以及这种方法能否带来额外价值，都需要核验。下面用三个现成项目说明已有工作到哪一层。",
    "先看 PhIDO。原图把流程分为四段：Interpreter 解析自然语言并检索模板，Designer 选择组件、配置参数并产生结构化设计，Layout 用版图工具布局、路由和检查，Circuit Verification 使用 SAX 电路模型。前两段由 LLM Agent 承担，后两段主要是算法和专业工具。输出中间表示后可以人工检查。原图出现 FDTD，但既有核读记录显示该分支没有进入主发布；不能把原图中的所有模块都理解为正式基准已验证的能力。",
    "这页引用 PhIDO Fig.5 中 Gemini-2.5-pro/GPT-4o 的局部和原图图例。benchmark 一共有102个描述，四级分别23、10、60、9个；同级左柱是pass@1，右柱是pass@5。蓝色S表示无致命错误且得到有效 schematic 与 GDS；其余颜色定位不同阶段失败。可以看出更复杂任务仍有困难，但不从柱形目测推导精确百分比。这里的成功是结构层成功，不是目标光学性能已经满足。",
    "PICopilot 的目标是生成可用的 PIC 设计脚本。原图中 Planner 分解任务，功能专用生成器从工具手册中检索，Synthesizer 合成脚本，Evaluator 提供检查反馈。需要特别区分：内部反馈主要是静态代码、自定义检查和 LLM 评价；原文因工具运行成本较高，没有把逐次真实执行作为内部循环。48个benchmark任务分Basic12、Medium12、Advanced24，每任务15次生成，外部另运行脚本并比较参考输出，至少3次成功计为Solved。作者报告48项均Solved，这不表示单次都成功，也不表示器件性能达标。",
    "Kharel 的工作更接近真实数值仿真在环。原图左边由人提供目标、约束和初始设计文件；Agent 修改设计，先做预览和DRC，再调用Tidy3D等求解器。评价器判断候选是否更好，选择保留或丢弃，同时记录设计日志。论文展示显式几何、工艺与物理一致性规则，结果按给定定量标准验收。所以不能说现有方法都没有物理反馈。但在多物理案例中，模态识别和电容处理初设曾由专家纠正，说明正确仿真设置和评价条件仍是重要边界。",
    "这一页用作者原始Fig.2(a)说明反馈怎样影响迭代。在400nm SiN、1550nm、12微米半径和150nm最小特征约束下，作者以50次仿真为预算，圆弧基线损耗约0.460dB，最优约0.109dB。原图纵轴使用负的dB传输值，绿色最优线更接近0表示损耗更小；文字报告的是正值损耗幅度。绿色点是被保留的候选，红叉是被丢弃的候选，不应把红叉当作全部实验失败。结果说明显式约束和数值反馈可以支持有效探索；它仍是论文仿真案例，并没有由我们复现或通过流片测量验证。",
    "三个项目分别提供结构生成、脚本生成和数值仿真闭环的基础，其成功标准需要分开理解。我的切入点是仿真后的物理诊断与动作选择：使诊断形成能由后续结果检验的预测，进一步考察方法是否提高可靠性。这仍是候选问题，不能提前宣称创新或性能优势。DAS 可以作为后续复杂应用场景，与小组系统方向衔接。",
]
papers={
    2:"Sharma et al., 2025, AI agents for photonic integrated circuit design automation, Fig. 1, DOI:10.1063/5.0300741",
    3:"Sharma et al., 2025, AI agents for photonic integrated circuit design automation, Fig. 5/Table II, DOI:10.1063/5.0300741",
    4:"Jiang et al., 2026, PICopilot: An LLM-based Agentic Framework for Assisting Photonic Integrated Circuit Design via Script Generation, Fig. 2/Table 2–3/§3.6, DOI:10.48550/arXiv.2608.01791",
    5:"Kharel et al., 2026, Autonomous agentic design for photonics, Fig. 1(b)/Table S2, DOI:10.48550/arXiv.2606.00915",
    6:"Kharel et al., 2026, Autonomous agentic design for photonics, Fig. 2(a)/§S2.1, DOI:10.48550/arXiv.2606.00915",
}
slides=[]
for i in range(8):
    note=f"计划用时：{times[i]} 秒。\n\n{notes[i]}"
    if i in papers:note+="\n\n原图来源："+papers[i]+"。裁剪/缩放和中文说明仅用于课堂解释，原始数据、坐标与图例未修改。"
    slides.append({"id":f"s{i+1}","type":"content","variant":"flow","slide_intent":"evidence" if 2<=i<=6 else "message","title":titles[i],"subtitle":subtitles[i],"assets":{"diagram":paths[i]},"footer":footers[i]+f"｜{i+1}/8","sources":[footers[i]],"notes":note})
write("outline.json",{"title":"面向光子芯片设计的 Agent Harness：课题与现成项目","subtitle":"课堂汇报｜项目重点版","deck_style":{"font_pair":"system_clean_v1","visual_density":"medium","emoji_mode":"none","research_visual_mode":True,"header_mode":"stack","footer_mode":"source-line","footer_page_numbers":True},"compliance":{"auto_image_sources":False,"require_attribution":False},"slides":slides})
write("content_plan.json",{"topic":"Harness 课堂项目重点版","audience":"课堂同学与教师","objective":"两页课题、五页现成项目、一页总结，计划460秒","thesis":"从原文架构与结果理解已有能力，再定位物理诊断与决策问题","narrative_arc":[{"act":"topic","slides":["s1","s2"]},{"act":"existing projects","slides":["s3","s4","s5","s6","s7"]},{"act":"summary","slides":["s8"]}],"slide_plan":[{"slide_id":s["id"],"role":"evidence" if 2<=i<=6 else "context","message":subtitles[i],"variant":"flow","visual_strategy":"original-paper-figure" if 2<=i<=6 else "concept-diagram","planned_seconds":times[i]} for i,s in enumerate(slides)]})
write("design_brief.json",{"topic":"课堂 Harness 项目重点版","format_promise":"原图为主，中文短注解释；白底、16:9、便于拼接","title_page_concept":{"chosen_archetype":"content opener for concatenation"},"structure_strategy":{"container_policy":"原图不加框遮挡数据；右侧短注与原图明显分开"},"design_dna":"classroom research explanation"})
write("evidence_plan.json",{"topic":"既有核读证据","items":[{"id":f"ev{i}","claim":titles[i],"source_note":papers.get(i,"候选方向材料 §2–8，未验证设想"),"used_on_slides":[f"s{i+1}"],"visual_use":"footer-source"} for i in range(8)],"open_questions":["诊断与动作选择的额外增益","仿真初设与评价器正确性","原图再分发许可：PICopilot/Kharel未核实，未远程发布"]})
(ROOT/"speaker-notes.md").write_text("# Harness 课堂汇报｜项目重点版\n\n8页：两页课题、五页现成项目、最后一页总结。计划7分40秒，尚未试讲。\n\n"+"\n\n".join(f"## P{i+1}｜{titles[i]}（{times[i]}秒）\n\n{notes[i]}"+("\n\n来源："+papers[i] if i in papers else "") for i in range(8))+"\n",encoding="utf-8")
print("Authored 8 slides; topic 110s, projects 310s, summary 40s.")
