"""Generate the Research Portal reading layer from TASK-007/016 sources.

The research Markdown under references/ remains the source of truth. This
script only adapts relative links for MkDocs and copies permitted figures.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "references/task-007/formal-research-report.md"
EVIDENCE = ROOT / "references/task-016-evidence"
PORTAL = ROOT / "portal/docs"
OUT = PORTAL / "task-016-evidence"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "figures").mkdir(exist_ok=True)

    report = REPORT.read_text(encoding="utf-8")
    report = report.replace("../task-016-evidence/", "task-016-evidence/")
    preface = (
        "---\ntitle: 正式技术调研报告\n---\n\n"
        "<div class=\"sot-note\">事实源（Source of Truth）："
        "<code>references/task-007/formal-research-report.md</code>。"
        "本页由 <code>scripts/sync_task016_portal.py</code> 生成，只调整站内链接。</div>\n\n"
    )
    (PORTAL / "task-007-report.md").write_text(preface + report, encoding="utf-8")

    names = (
        "README.md",
        "agentic-pic-comparison.md",
        "evidence-log.md",
        "figure-sources.md",
        "source-manifest.md",
    )
    for name in names:
        content = (EVIDENCE / name).read_text(encoding="utf-8")
        if name == "README.md":
            # The public reading layer does not re-embed images whose
            # redistribution rights remain unverified.
            content = re.sub(
                r"^!\[PICopilot 原始架构图\]\([^\n]+\)$",
                "*PICopilot Fig. 2 原图请由 DOI 或本地 Zotero PDF p.3 查看；本网页不再分发该图。*",
                content,
                flags=re.MULTILINE,
            )
            content = re.sub(
                r"^!\[Kharel 被动弯曲器件原始结果图\]\([^\n]+\)$",
                "*Kharel Fig. 2 原图请由 DOI 或本地 Zotero PDF p.5 查看；本网页不再分发该图。*",
                content,
                flags=re.MULTILINE,
            )
            content = content.replace(
                "PDF p.3；沿用既有局部裁图。预印本未核实可公开再分发的图片许可，公开发布前需另核权利。",
                "PDF p.3；网页仅保留原文定位，图片再分发许可未核实。",
            ).replace(
                "PDF p.5；沿用既有局部裁图。预印本图片再分发许可未核实。",
                "PDF p.5；网页仅保留原文定位，图片再分发许可未核实。",
            )
        preface = (
            "<div class=\"sot-note\">事实源："
            f"<code>references/task-016-evidence/{name}</code>。"
            "本页为构建时阅读副本。</div>\n\n"
        )
        (OUT / name).write_text(preface + content, encoding="utf-8")
    shutil.copy2(EVIDENCE / "key-data.csv", OUT / "key-data.csv")
    for path in (EVIDENCE / "figures").glob("*.png"):
        shutil.copy2(path, OUT / "figures" / path.name)
    print(f"synced report and {len(names)} evidence pages; 3 figures")


if __name__ == "__main__":
    main()
