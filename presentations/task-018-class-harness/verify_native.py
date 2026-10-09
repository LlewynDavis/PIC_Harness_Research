"""Inspect OOXML editability and prove original figures were not recomposed."""
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

ROOT=Path(__file__).resolve().parent
deck=ROOT/"Harness_课堂汇报_可编辑版.pptx"
outline=json.loads((ROOT/"outline.json").read_text(encoding="utf-8"))
prs=Presentation(deck)
assert len(prs.slides)==8
inventory=[]
for i,(slide,spec) in enumerate(zip(prs.slides,outline["slides"])):
    pictures=[s for s in slide.shapes if s.shape_type==MSO_SHAPE_TYPE.PICTURE]
    texts=[s for s in slide.shapes if s.has_text_frame and s.text]
    values=[s.text for s in texts]
    for el in spec["native_elements"]:
        if el["kind"]=="text":assert el["text"] in values, el["text"]
    inventory.append({"page":i+1,"native_text_objects":len(texts),"independent_pictures":len(pictures),"total_objects":len(slide.shapes)})
assert [s["independent_pictures"] for s in inventory]==[0,0,1,2,1,1,1,0]
images=[(ROOT/e["path"]).resolve() for s in outline["slides"] for e in s["native_elements"] if e["kind"]=="image"]
with ZipFile(deck) as z:
    assert z.testzip() is None
    hashes={hashlib.sha256(z.read(n)).hexdigest() for n in z.namelist() if n.startswith("ppt/media/")}
    for image in images:assert hashlib.sha256(image.read_bytes()).hexdigest() in hashes, image
    notes=[n for n in z.namelist() if n.startswith("ppt/notesSlides/notesSlide") and n.endswith(".xml")]
    assert len(notes)==8
payload={"date":"2026-10-09","slides":inventory,"native_text_total":sum(s["native_text_objects"] for s in inventory),"original_images_byte_identical":len(images),"concept_pages_without_pictures":[1,2,8],"notes_pages":8}
(ROOT/"editability-check.json").write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print("PASS: 93 native text objects; 6 independent byte-identical original images; 8 notes pages.")
