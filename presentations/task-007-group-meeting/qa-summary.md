# TASK-007 组会 PPT 质量检查

检查日期：2026-09-21

## 自动检查

- 页数：25。
- presentation-skill preflight：通过，无 blocking issue。
- overflow：0。
- overlap：0。
- placeholder：0。
- geometry error：0；warning：3（两页轻微留白、一页卡片密度提示，不阻断）。
- design error / warning：0 / 0。
- 叙事资产引用：全部解析成功。

## 渲染检查

- 本机未安装 LibreOffice `soffice`，因此 skill 内置渲染器不能使用。
- 改用本机 Microsoft PowerPoint 只读打开最终 PPTX，并导出 25/25 张 1600×900 PNG 进行视觉检查。
- 第一轮发现 Mermaid PNG 的中文字体缺失、末页左右失衡。
- 修复：流程图改用英文短标签，保留中文页标题/解释；末页改为“当前结论 / 下一步讨论”双栏。
- 第二轮重新构建并导出 25/25 张 PNG；抽查流程图、宽表格、对抗性矩阵和结论页，未发现截断、乱码或明显不可读内容。

## 已知限制

- 幻灯片使用本地生成的 Mermaid 流程图和原生可编辑表格，没有外部图片。
- 页脚来源在投影环境下接近最小字号，适合追溯，不适合作为口头讲解正文。
- 自动 QA 不能替代不同投影设备和字体环境下的现场预演。

