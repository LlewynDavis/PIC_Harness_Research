# Harness 课题介绍两页模块

用户指定桌面Harness PPT为内容源，采用工程光学格式模板。交付为同名PPTX/PDF：Harness_课题介绍_原理与案例_模板版。

- P1：Agent Harness原理，需求、模型、工具、评价与数值反馈。
- P2：Kharel 2026波导弯曲案例，论文原图、0.460→0.109dB作者仿真结果与完整条件。
- 原理框图、说明、箭头和导航为原生对象，曲线为独立原图。没有封面、目录或致谢，方便直接插入。

复制两页到课题组PPT时选择“保留源格式”；画布为13.3333×7.5英寸（16:9）。顶部导航先用“课题方向/技术原理/代表案例/研究展望”，都是可编辑标签，可按目标PPT章节改名。源文件与模板未修改。

完整课题组PPT未提供，本次只交付两页模块，尚未实际合并。

重建：使用bundled Python运行build_excerpt.py --source <桌面源PPT路径>，随后在PowerShell运行export_preview.ps1。默认模板引用来自个人技能artifact-template-engineering-optics，模板内容不复制进仓库。outline.json为两页内容源，source-manifest.json记录输入版本；verification.json记录结构/原图/母版主题检查。verify_editability.ps1仅在build中的临时副本测试编辑并保存重开。
