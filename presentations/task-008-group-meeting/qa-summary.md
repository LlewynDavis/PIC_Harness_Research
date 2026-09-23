# TASK-008 组会调研 PPT 图示化修订检查

日期：2026-09-23。修订基线提交：`4d5f06099e86431dba6ec08ce5c3241a5b54f69a`。原 TASK-007 研究报告与 PPT workspace 保持不变。

## 交付内容

- 最终版仅有 14 页主讲，未保留附录；14/14 页含讲稿备注，面向 15–20 分钟组会。
- 第 2–13 页的 12 张技术/综合分析页均使用承担解释任务的图示、论文 Figure 或可视化矩阵。比例是本次内容适用的结果，不以填满页面为目标；封面与讨论页保持简洁。
- 新绘或重绘：三目标关系、证据标签、DAS 信号链与集成边界、光子 AI 推理链与架构对比、代表工作能力矩阵、三方向比较、研究缺口及 A/B/C 路线推导。各图的解释问题、原始依据和限制逐条列于 `diagram-sources.md`。
- 原论文图片：从 Zotero 本地 PDF 只读裁剪 AutoPhotonicDesign Fig. 1(b) 与 PhIDO Fig. 1。页脚标明作者、年份、图号与论文来源。PhIDO 图内的 FDTD 支路已注明不代表主发布已验证。
- DAS 与光子 AI 代表论文 PDF 未在本次查到的 Zotero 附件目录中；Zotero API 恢复后再次查询相关条目，仍未找到这些 PDF 附件。对应页面使用有明确证据来源的重绘图，未冒充原始论文图或本项目实物成果。

## 已执行的验证

- 运行 `build_explanatory_svgs.py`、`compose_outline.py`、`build_workspace.py --qa --skip-render --overwrite`，均成功；12/12 张技术/综合分析页的图示路径在 `outline.json` 中解析成功。
- Microsoft PowerPoint 打开最终 PPTX，导出 14/14 张 1600×900 PNG 与 14 页 PDF；检查整套页面缩略图，并放大检查证据标签、DAS、两页原论文 Figure、能力矩阵、三方向比较、路线与讨论页。修复证据页和跨方向比较页原先过大的无效留白，并缩短原论文案例页标题。
- 对最终 PPTX 运行严格几何 QA，退出码 0：文字溢出 0、对象重叠 0、占位符 0、视觉警告 0、设计错误/警告 0/0。保留 10 条非阻断 `density_too_high` 提示，均来自高占比整幅图示；人工查看未发现裁剪、遮挡或无法阅读的关键标注。
- 使用 `python-pptx` 读回 14 页与 14/14 页备注；PPTX 包含 10 个 SVG 媒体对象及高分辨率论文裁剪图。使用 `pypdf` 读回 PDF 为 14 页。
- Zotero API 重连后，本地 API、Connector 均返回 200；两张 PDF 的图号、页码、裁剪范围、条目/附件定位和使用许可检查见 `diagram-sources.md`。未改动 Zotero 库。论文指标仍为作者报告，本项目未复算或运行物理实验。

## 编辑与使用边界

- PPTX 中标题、页脚和备注可直接编辑；概念 SVG 为矢量媒体，精确修改节点/箭头应编辑 `assets/diagrams/build_explanatory_svgs.py` 并重建。原论文 Figure 是高分辨率裁剪 PNG，不能作为原生形状逐节点编辑。
- PhIDO PDF 明示文章内容除另有注明外为 CC BY 4.0；AutoPhotonicDesign 附件未找到明确许可声明。当前用于带完整来源标注的组会讲解；对外公开前应核查该图的传播许可。
- 未在实际投影设备或会议时长条件下预演。图示阐释的是文献和调研判断，不是本项目已实现的 PIC Harness、DAS 模块或光子 AI 芯片。
