# 原文与源码证据索引

日期：2026-10-14。定位来自本对话此前定向核读与既有证据包；本次整理期间补核官方 HTML、固定版本源码及本地文件哈希。所有作者指标未复现；`CODE INSPECTED` 仅静态检查。没有全库扫描、没有新增实验。

## 一手来源与定位

| ID | 来源 / 定位 | 支持的具体判断 | 不支持的外推 |
|---|---|---|---|
| E1 | [PhIDO 论文](https://doi.org/10.1063/5.0300741)，Fig.1、Table II、§II.E；[既有核读](../task-016-evidence/agentic-pic-comparison.md)；[仓库](https://github.com/JPPhotonics/PhIDO-Release) | `FACT`：NL、DSL/组件、版图、SAX；主 benchmark 的成功口径为有效 schematic/GDS | 光学目标性能达标、通用全波闭环、LVS 或流片签核 |
| E2 | [Lumi / DOI](https://doi.org/10.1145/3787109.3816402)，用户供给 6 页 PDF，p.3 Fig.1 / §3.1–3.2，p.4 §3.4 | `FACT`：约束工具、lumapi、执行反馈、反思重试；任务产物归档 | 类型检查已确保物理正确；反思置信度已校准；可直接复现的开源代码 |
| E3 | 同一 Lumi PDF，p.5 Fig.2 E1、Table 2，§4.3–4.4 | `FACT`：执行、setup、result 分开评价；E1 要求与生成衬底高度不符。`AUTHOR CLAIM`：闭环执行可成功而 setup 仍有失败 | 执行成功率即需求/物理正确率；全部失败都能自动修复 |
| E4 | [HALO v2 官方全文](https://arxiv.org/html/2608.28877v2)，Method / Planner Configurations，PDF p.3–4、Fig.2 | `FACT`：固定 LangGraph、自主结构化 LangChain DeepAgent、自主编码三配置；typed design 和 RCWA 接口；诊断反馈 | typed validation 能排除全部材料/数值错误；周期纳米结构证据可直接推广到导波 PIC |
| E5 | 同一 HALO v2，Common Evaluation Protocol / Experimental Setup / Failure Analysis；PDF p.4–7，Table 3/5 | `AUTHOR CLAIM`：固定工作流 token 效率好；自主配置有额外运行失败。`FACT`：单模型/配置/案例一次运行，评价生成与规划配置等存在混杂 | 同预算隔离证明“自主结构化总是更好”；失败类别比例是所有任务的发生率 |
| E6 | [Kharel 等：Autonomous agentic design for photonics v1](https://arxiv.org/html/2606.00915v1)，§2、§3.1/3.3、§S2.1、§S4.2–3、§S6 | `AUTHOR CLAIM`：给定约束下 SiN 弯曲优化、RF 多家族切换；MZM 有人机纠错。`FACT`：工程师给定初始脚本和评价器 | 全流程无人、全局最优、诊断机制被独立验证；RF 路由 DRC 下降证明波导优化的因果机理 |
| E7 | [RF 分支 tools/journal.py](https://github.com/flexcompute/autophotonicdesign/blob/6d0e257b73579a331cc994b6973085ff512396c4/tools/journal.py)，`archive_run`、`_save_rf_traces_npz`、`promote_best`、`revert_to_best`；[program.md](https://github.com/flexcompute/autophotonicdesign/blob/6d0e257b73579a331cc994b6973085ff512396c4/program.md) | `CODE INSPECTED`：设计快照、results.json、TSV、条件满足时保存原始 trace；数值 FOM 保留/回退；指令含异常处理和最终评价条件要求 | 源码存在即所有运行产物齐全；日志解释经物理验证；现行 RF 分支与论文案例条件完全相同 |
| E8 | [bend 固定版本 journal.md](https://github.com/flexcompute/autophotonicdesign/blob/280973d197643054ba0ab414e6a5e62b1ee8256d/output/journal.md)，Experiment 6–8、28–31、38；[program.md](https://github.com/flexcompute/autophotonicdesign/blob/280973d197643054ba0ab414e6a5e62b1ee8256d/program.md) | `FACT / 作者公开记录`：局部宽度尝试与后期联合参数方案不同；探索允许额外求解器调用 | 每个外层迭代只调用一次 solver；早期经验为跨条件定律；轨迹已经由本项目重算 |
| E9 | [HiLAB 官方开放全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC12641366/)，方法：部分拓扑优化、VAE 与贝叶斯优化 | `FACT`：非 Agent 方法也能搜索自由形状及物理超参数，构成“传统方法只会固定参数”反例 | 同器件/预算下必定胜过 Agent；直接证明本候选方法无价值 |

不复刻版权尚未明确的论文图，本轮覆盖图为分析性原创改绘。论文/源码的外部链接是出处，不是部署或模型调用入口。

## 版本与源码范围

AutoPhotonicDesign 在此前本轮只读审查中核对的版本：

- main：`3b265056586a2923b58f60fd9efe73530a03b1d4`，`program.md` / `orchestrate.py`。
- bend：`280973d197643054ba0ab414e6a5e62b1ee8256d`，`program.md` / `output/journal.md`。
- rf_transmission_lines：`6d0e257b73579a331cc994b6973085ff512396c4`，`program.md` / `tools/journal.py`。

首轮文件整理重新读取 RF `tools/journal.py`；本次继续流程又定向读取 RF `program.md`、晋升/历史最好值函数及 bend `output/journal.md` 的局部与联合参数记录，均未执行。新定位见[决策证据卡](feedback-decision-evidence-cards.md)。未在本次重新读取的其他细节沿用前序审查；不假定三个固定提交一直是远端最新 HEAD。代码来自 `flexcompute/autophotonicdesign`，不是本项目实现。

PhIDO 沿用 TASK-005 固定版本 `6a8b8d695f0af9247db1a9bbe0511307a8301b4d` 及当时根 MIT 记录；本次未重新审计整个仓库。Lumi/HALO 的公开实现和许可证尚未核实，不能称为已开源或断言没有公开代码。商业求解器依赖可纳入候选，但费用与授权条件未评估。

## 用户供给 PDF 的身份

本次 `Get-FileHash` 只读核对 SHA-256，PDF 原件未写入或公开发布。页码为 PDF 物理页码。

- Lumi：`Chen 2026 - Lumi Agent Autonomous Lumerical FDTD Simulation for Photonic Waveguide Experiments.pdf`；SHA-256 `6fa6a2cda8ee08bd5284c9cdf28b2dfeb7c0c6527f316d600bdf8646e9fd3657`。原件位于用户此前指定微信文件目录。
- HALO：`Zhang 2026 - HALO A Physics-Aware LLM Agent Framework for Nanophotonic Design.pdf`；SHA-256 `02303c04644f6249f41af054b779866c7edbc0dbd22c6ba79883a67d0f727d0a`。核读版本为 arXiv:2608.28877v2，2026-09-07。
- PhIDO 等旧原件的 item key / 哈希 / 页数见[旧 source manifest](../task-016-evidence/source-manifest.md)。未改 Zotero 或附件。

## 影响路线判断的证据链

1. **运行不等于正确**：E3 的需求偏差 + E5 的无效结果/设置失败 → 需要分离执行、需求、数值与器件性能。结论是 `INFERENCE`，不是已实现判定器。
2. **诊断和切换已有先例**：E4、E6、E7 → H1 的宽泛缺失说不成立；需要转向决策可靠性问题。
3. **存在结构化产物与规则**：E7 → 不沿用“现有项目只有文本、没有 RESULT”或“完全没有设置恢复”的宽泛判断。
4. **经验有条件**：E8 → 失败必须保留，但局部趋势不能自动泛化；不据此证明长期学习。
5. **更简单替代不可遗漏**：E9 + E7 的确定性规则 → 自主动作选择的必要性与价值仍需论证，不能把搜索迭代本身当创新。

## 审查方法说明

本工作稿使用 `nature-reader` 的源定位规则，以及 K-Dense `scientific-critical-thinking` 的主张—证据—反例与混杂审查。未套用临床 GRADE 评分，没有让工具替代物理判断。

方法工具引用：Kassis, T., Agarwal, V., He, Y., Patel, D., & Brueckner, A. M. (2026). [Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents](https://doi.org/10.48550/arXiv.2609.00065). 官方 arXiv 当前 v2（2026-09-02 修订），2026-10-14 核对，2026-10-15 撰写第三章时再次核对作者、年份与版本；它是辅助审查工具出处，不是本候选方法有效性的科研证据。章节初版同时使用 `literature-review` 的主题综合方法，不宣称完成系统检索或穷尽性综述。

## 尚待补齐

- Lumi / HALO 公开源码与可运行原始轨迹；HALO 的补充材料未完整取得。
- 诊断解释、具体动作及后续独立证据之间的对应，不以最终 FOM 改善代替。
- 真实求解器总调用与额外探索预算；不能只读“50 iterations”作成本比较。
- 分支条件与论文平台差异；不将当前 RF README 当论文原始全部条件。
- 跨器件、制造约束与签核证据；本轮不声称已经补齐。
