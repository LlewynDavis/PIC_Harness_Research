"""Author native PowerPoint primitives in outline.json, preserving evidence and notes."""
import json
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parent
outline=json.loads((ROOT/"outline.json").read_text(encoding="utf-8"))
INK="18364A"; TEAL="167B78"; MUTED="536570"
PALE="EAF0F7"; MINT="E6F3EF"; SAND="FBEFE3"
items=[]

def text(s,x,y,w,h,size=14,bold=False,color=INK,align="left"):
    items.append({"kind":"text","text":s,"x":x,"y":y,"w":w,"h":h,"fontSize":size,"bold":bold,"color":color,"align":align})
def rect(x,y,w,h,fill=PALE):
    items.append({"kind":"rect","x":x,"y":y,"w":w,"h":h,"fill":fill,"stroke":"CBD9DF"})
def line(x1,y1,x2,y2,arrow=False):
    items.append({"kind":"line","x1":x1,"y1":y1,"x2":x2,"y2":y2,"color":TEAL,"arrow":arrow})
def card(x,y,w,h,title,body,fill=PALE):
    rect(x,y,w,h,fill)
    text(title,x+.10,y+.10,w-.20,.44,16,True,align="center")
    text("\n".join(body),x+.10,y+.70,w-.20,h-.77,12.7,color=MUTED,align="center")
def image(path,x,y,w,h,name):
    path=Path(path)
    actual=ROOT/path
    with Image.open(actual) as im:iw,ih=im.size
    scale=min(w/iw,h/ih);ww,hh=iw*scale,ih*scale
    items.append({"kind":"image","path":path.as_posix(),"x":x+(w-ww)/2,"y":y+(h-hh)/2,"w":ww,"h":hh,"name":name})
def sidebar(sections):
    for i,(title,body) in enumerate(sections):
        x,y,w,h=6.95,[1.36,2.60,4.04][i],2.55,[1.14,1.34,1.14][i]
        rect(x,y,w,h,[MINT,PALE,SAND][i])
        text(title,x+.12,y+.06,w-.24,.32,14,True)
        text("\n".join(body),x+.12,y+.48,w-.24,.78 if len(body)==3 else .60,12.1,color=MUTED)

for index,s in enumerate(outline["slides"]):
    items=[]
    if index==0:
        rect(.5,1.35,9,.58,MINT)
        text("Harness：围绕 Agent 组织工具执行、状态保存和验证检查",.7,1.42,8.6,.44,17,True,color=TEAL,align="center")
        for x,title,body,fill in [
            (.5,"需求与约束",["目标指标","工艺 / 几何条件"],PALE),
            (2.85,"Agent",["规划设计","解释结果 / 选动作"],MINT),
            (5.2,"专业工具",["CAD / 仿真器","产生结构与数值结果"],PALE),
            (7.55,"确定性评价",["计算指标","检查约束与达标"],PALE)]:
            card(x,2.17,1.95,1.45,title,body,fill)
        for x in [2.45,4.8,7.15]:line(x+.04,2.91,x+.34,2.91,True)
        line(8.525,3.69,8.525,4.16)
        line(8.525,4.16,3.825,4.16)
        line(3.825,4.16,3.825,3.69,True)
        text("反馈：指标 + 条件 + 检查结果",4.4,4.35,4.5,.31,15,True,color=TEAL,align="center")
        text("版本与轨迹持续记录",.5,4.38,2.65,.3,12,color=MUTED,align="center")
    elif index==1:
        text("候选研究问题：如何利用物理知识与真实反馈选择下一步？",.5,1.38,9,.33,17,True,color=TEAL,align="center")
        for x,title,body,fill in [
            (.5,"仿真结果",["功率 / 光谱 / 场分布","模型与求解条件"],PALE),
            (3.58,"物理诊断",["哪里偏离目标？","提出原因假设"],SAND),
            (6.65,"设计决策",["改参数 / 换策略","或补充验证"],MINT)]:
            card(x,2.12,2.85,1.45,title,body,fill)
        line(3.39,2.85,3.53,2.85,True)
        line(6.47,2.85,6.61,2.85,True)
        rect(3.58,4.05,5.92,.98,MINT)
        text("把诊断写成可检验预测",3.78,4.11,5.52,.42,16,True,color=TEAL,align="center")
        text("下一轮仿真是否支持预测？",3.78,4.65,5.52,.36,13,color=MUTED,align="center")
        line(8.075,3.65,8.075,3.99,True)
        line(3.53,4.54,1.925,4.54)
        line(1.925,4.54,1.925,3.65,True)
        text("新证据可修正原假设",.5,4.84,2.85,.32,12,color=MUTED,align="center")
    elif index==2:
        image("../task-010-group-meeting-rebuild/assets/phido-fig1.png",.5,1.47,6.15,3.68,"PaperOriginal_PhIDO_Fig1")
        sidebar([
            ("自然语言进入设计流程",["解释需求 → 选器件","结构化 DSL → 版图"]),
            ("四段职责",["前两段：LLM Agent","后两段：CAD / 电路工具"]),
            ("验证边界",["主基准检验结构有效","FDTD 非主发布分支"])])
    elif index==3:
        image("assets/papers/phido-fig5-panel.png",.5,1.4,6.15,3.0,"PaperOriginal_PhIDO_Fig5Panel")
        image("assets/papers/phido-fig5-legend.png",1.2,4.45,4.8,.48,"PaperOriginal_PhIDO_Fig5Legend")
        text("Fig. 5 局部：Gemini-2.5-pro/GPT-4o；保留原始颜色图例",.5,5.03,6.15,.19,8.8,color=MUTED,align="center")
        sidebar([
            ("102 个设计描述",["Level 1/2/3/4","任务数：23/10/60/9"]),
            ("左柱 @1，右柱 @5",["图中蓝色 S 为成功","复杂任务的成功仍有限"]),
            ("“成功”是什么？",["有效 schematic 与 GDS","不等同光学性能达标"])])
    elif index==4:
        image("../task-010-group-meeting-rebuild/assets/picopilot-fig2.png",.5,1.47,6.15,3.68,"PaperOriginal_PICopilot_Fig2")
        sidebar([
            ("任务 → 脚本",["规划 → 检索增强生成","合成脚本 → 静态评价"]),
            ("48 项脚本任务（作者）",["Basic 12 / Medium 12","Advanced 24；15 次/任务","Solved：48/48（≥3/15）"]),
            ("内部与外部评价不同",["内部：静态检查 + LLM","外部：运行脚本并评分"])])
    elif index==5:
        image("assets/papers/kharel-fig1b.png",.5,1.47,5.95,3.68,"PaperOriginal_Kharel_Fig1b")
        sidebar([
            ("人类提供起点",["目标、约束、仿真初设","评价器与可编辑参数"]),
            ("真实求解器在环",["设计 → 规则检查 → 仿真","数值结果决定保留 / 回退"]),
            ("关键能力与边界",["显式规则 + 定量验收","多物理初设曾由专家纠错"])])
    elif index==6:
        image("assets/papers/kharel-fig2a.png",.5,1.47,6.15,3.68,"PaperOriginal_Kharel_Fig2a")
        sidebar([
            ("弯曲损耗：作者仿真",["0.460 → 0.109 dB","50 次仿真预算"]),
            ("案例条件",["400 nm SiN；1550 nm","12 µm 半径","150 nm 最小特征"]),
            ("如何读这张图？",["绿色：保留 / 最优值","红色：丢弃；不是实测"])])
    else:
        for i,(title,body,fill) in enumerate([
            ("PhIDO","自然语言 → 结构化设计与版图",PALE),
            ("PICopilot","自然语言 → PIC 脚本与功能评价",MINT),
            ("Kharel","显式规则 → 仿真反馈 → 定量迭代",SAND)]):
            y=1.43+.72*i
            rect(.5,y,9,.58,fill)
            text(title,.65,y+.08,2.0,.44,17,True,align="center")
            text(body,2.9,y+.08,6.2,.44,17,align="center")
        text("已有项目构成方法基础，成功定义与验证层级需要区分",.5,3.83,9,.44,17,True,color=TEAL,align="center")
        text("我的切入点：让仿真后的诊断与动作选择得到证据检验",.5,4.38,9,.44,17,True,align="center")
        text("方法增益待验证；DAS 可作为后续复杂应用场景",.5,4.88,9,.40,13,color=MUTED,align="center")
    s["assets"]={}
    s["native_elements"]=items
    s["variant"]="flow"
outline["native_renderer_version"]=1
outline["deck_style"]["font_body"]="Microsoft YaHei"
outline["deck_style"]["font_heading"]="Microsoft YaHei"
(ROOT/"outline.json").write_text(json.dumps(outline,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
plan=json.loads((ROOT/"content_plan.json").read_text(encoding="utf-8"))
for i,s in enumerate(plan["slide_plan"]):
    s["visual_strategy"]="native-shapes" if i in [0,1,7] else "independent-paper-image-and-native-text"
(ROOT/"content_plan.json").write_text(json.dumps(plan,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("Authored native elements: no composite slide images; independent original figures.")
