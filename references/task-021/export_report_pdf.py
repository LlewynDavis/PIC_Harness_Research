"""Export the current Markdown report without modifying its source text.

Run with the bundled Python runtime (ReportLab and Pillow required).
"""
from __future__ import annotations

import hashlib
import html
import re
from pathlib import Path
from urllib.parse import unquote

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Flowable, Paragraph, Spacer, Table,
    TableStyle, Image,
)

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).parent / "chapters/完整调研报告.md"
OUTPUT = ROOT / "output/pdf/TASK-021_完整调研报告_2026-10-15.pdf"
WIDTH = A4[0] - 88
TEAL = colors.HexColor("#194954")
pdfmetrics.registerFont(TTFont("ReportSong", "C:/Windows/Fonts/simsun.ttc", subfontIndex=0))
pdfmetrics.registerFont(TTFont("ReportHei", "C:/Windows/Fonts/simhei.ttf"))
pdfmetrics.registerFontFamily("ReportSong", normal="ReportSong", bold="ReportHei", italic="ReportSong", boldItalic="ReportHei")

BODY = ParagraphStyle("Body", fontName="ReportSong", fontSize=10.5,
                      leading=18, firstLineIndent=21, spaceBefore=0,
                      spaceAfter=0, wordWrap="CJK", allowWidows=0,
                      allowOrphans=0, textColor=colors.HexColor("#222A30"))
CELL = ParagraphStyle("Cell", parent=BODY, fontSize=9, leading=13.5,
                      firstLineIndent=0, spaceAfter=0)
CAPTION = ParagraphStyle("Caption", parent=BODY, fontSize=9, leading=14,
                         firstLineIndent=0, textColor=colors.HexColor("#465A62"),
                         spaceAfter=0)
META = ParagraphStyle("Meta", parent=BODY, firstLineIndent=0, keepWithNext=True)
REFERENCE = ParagraphStyle("Reference", parent=BODY, fontSize=9.5,
                           leading=15, firstLineIndent=19)
HEADINGS = {
    1: ParagraphStyle("Chapter", parent=BODY, fontName="ReportHei", fontSize=19,
                      firstLineIndent=0, leading=28, textColor=TEAL,
                      spaceBefore=12, spaceAfter=8, keepWithNext=True),
    2: ParagraphStyle("Section", parent=BODY, fontName="ReportHei", fontSize=13,
                      firstLineIndent=0, leading=20, textColor=TEAL,
                      spaceBefore=10, spaceAfter=6, keepWithNext=True),
    3: ParagraphStyle("Subsection", parent=BODY, fontName="ReportHei", fontSize=11,
                      firstLineIndent=0, leading=18, textColor=TEAL,
                      spaceBefore=8, spaceAfter=4, keepWithNext=True),
}


class BottomFigure(Flowable):
    """Leave the figure near its source, but reserve its space below page text."""
    _ZEROSIZE = True

    def __init__(self, items):
        super().__init__()
        self.items = items
        self.layout = [(item, *item.wrap(WIDTH, 740)) for item in items]
        self.figure_height = sum(h for _, _, h in self.layout)

    def wrap(self, available_width, available_height):
        return 0, 0

    def draw(self):
        self.canv._doctemplate.register_figure(self)

    def draw_bottom(self, canvas, bottom):
        y = bottom + self.figure_height
        for item, width, height in self.layout:
            y -= height
            item.drawOn(canvas, 44 + (WIDTH - width) / 2, y)


class FlushFigures(Flowable):
    _ZEROSIZE = True

    def wrap(self, available_width, available_height):
        if self.canv._doctemplate.pending_figures:
            return 0, available_height + 1
        return 0, 0

    def split(self, available_width, available_height):
        return []

    def draw(self):
        pass


class ReportDocument(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        super().__init__(filename, pagesize=A4, **kwargs)
        self.pending_figures = []
        self.page_figures = []
        self.figure_pages = []
        self.full_height = A4[1] - 43 - 50
        frame = Frame(44, 50, WIDTH, self.full_height, leftPadding=0,
                      rightPadding=0, topPadding=0, bottomPadding=0, id="body")
        self.addPageTemplates(PageTemplate(id="report", frames=[frame],
                                          onPage=footer,
                                          onPageEnd=self.draw_page_figures))

    def beforePage(self):
        frame = self.pageTemplate.frames[0]
        frame._y1p = 50
        frame._aH = self.full_height
        self.page_figures = []
        if self.pending_figures:
            self.reserve_figure(self.pending_figures.pop(0), frame)

    def reserve_figure(self, figure, frame):
        reserve = figure.figure_height + 12
        frame._y1p += reserve
        frame._aH -= reserve
        self.page_figures.append(figure)

    def register_figure(self, figure):
        remaining = self.frame._y - self.frame._y1p
        if not self.page_figures and remaining >= figure.figure_height + 12:
            self.reserve_figure(figure, self.frame)
        else:
            self.pending_figures.append(figure)

    def draw_page_figures(self, canvas, doc):
        for figure in self.page_figures:
            figure.draw_bottom(canvas, 50)
            self.figure_pages.append(self.page)


def inline(text: str) -> str:
    """Convert the report's inline Markdown while keeping all visible words."""
    pieces = re.split(r"(\[[^\]]+\]\([^)]+\)|`[^`]+`|\*\*[^*]+\*\*)", text)
    result = []
    for piece in pieces:
        match = re.fullmatch(r"\[([^\]]+)\]\(([^)]+)\)", piece)
        if match:
            label, target = match.groups()
            if not re.match(r"https?://", target):
                filename, _, fragment = target.partition("#")
                target = (SOURCE.parent / unquote(filename)).resolve().as_uri()
                if fragment:
                    target += "#" + fragment
            result.append(f'<link href="{html.escape(target, quote=True)}" color="#176C73">{html.escape(label)}</link>')
        elif piece.startswith("**"):
            result.append("<b>" + html.escape(piece[2:-2]) + "</b>")
        elif piece.startswith("`"):
            result.append(html.escape(piece[1:-1]))
        else:
            result.append(html.escape(piece))
    return "".join(result)


def make_table(lines: list[str]) -> Table:
    rows = []
    for line in lines:
        values = [s.strip() for s in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-+:?", s) for s in values):
            continue
        rows.append([Paragraph(inline(s), CELL) for s in values])
    n = len(rows[0])
    ratios = {3: [.22, .39, .39], 4: [.16, .28, .28, .28]}.get(n, [1 / n] * n)
    table = Table(rows, colWidths=[WIDTH * r for r in ratios], repeatRows=1,
                  hAlign="LEFT", splitByRow=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E5EFF1")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F6F8F9")]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOX", (0, 0), (-1, -1), .45, colors.HexColor("#C8D7DC")),
        ("INNERGRID", (0, 0), (-1, -1), .35, colors.HexColor("#D8E2E6")),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return table


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#C8D7DC"))
    canvas.line(44, 37, A4[0] - 44, 37)
    canvas.setFont("ReportSong", 8)
    canvas.setFillColor(colors.HexColor("#61747D"))
    canvas.drawString(44, 25, "TASK-021 | 完整调研报告")
    canvas.drawRightString(A4[0] - 44, 25, str(doc.page))
    canvas.restoreState()


def main():
    source_bytes = SOURCE.read_bytes()
    lines = source_bytes.decode("utf-8-sig").splitlines()
    story = []
    table_count = image_count = 0
    in_references = False
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            story.extend([make_table(table_lines), Spacer(1, 5)])
            table_count += 1
            continue
        heading = re.match(r"^(#{1,3})\s+(.+)", line)
        if heading:
            level, title = len(heading[1]), heading[2]
            if level == 1 and story and title == "参考文献与来源":
                story.append(FlushFigures())
                in_references = True
            story.append(Paragraph(inline(title), HEADINGS[level]))
            i += 1
            continue
        img = re.fullmatch(r"!\[([^\]]*)\]\(([^)]+)\)", line)
        if img:
            path = (SOURCE.parent / img[2]).resolve()
            if path.suffix.lower() == ".svg":
                path = path.with_suffix(".png")
            with PILImage.open(path) as bitmap:
                iw, ih = bitmap.size
            max_height = 350 if "fig2-original" in path.name else 310
            scale = min(WIDTH / iw, max_height / ih)
            pic = Image(str(path), width=iw * scale, height=ih * scale)
            pic.hAlign = "CENTER"
            block = [pic, Spacer(1, 5)]
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and re.match(r"图\s*\d", lines[j].strip()):
                block.append(Paragraph(inline(lines[j].strip()), CAPTION))
                i = j
            story.append(BottomFigure(block))
            image_count += 1
            i += 1
            continue
        # Repair only presentation of number/emoji markers in the export.
        line = re.sub(r"^([1-9])[\ufe0f\u20e3]+", r"\1. ", line)
        line = re.sub(r"^([1-9])\.(?=\S)", r"\1. ", line)
        if line.startswith("> "):
            line = line[2:]
        style = (REFERENCE if in_references else
                 META if re.match(r"^2026-\d\d-\d\d", line) else BODY)
        story.append(Paragraph(inline(line), style))
        i += 1
    story.append(FlushFigures())
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = ReportDocument(str(OUTPUT), title="完整调研报告：Agent 反馈驱动的器件与电路设计",
                         author="PIC_Harness_Research", pageCompression=1)
    doc.build(story)
    assert not doc.pending_figures, "Some figures were not rendered"
    assert SOURCE.read_bytes() == source_bytes, "Source was unexpectedly modified"
    print(f"PDF: {OUTPUT}")
    print(f"Tables: {table_count}; images: {image_count}")
    print("Bottom figure pages:", doc.figure_pages)
    print("Source SHA256:", hashlib.sha256(source_bytes).hexdigest())


if __name__ == "__main__":
    main()
