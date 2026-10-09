"""Read existing Zotero PDFs, verify versions and crop figures without changing data."""
import argparse
import hashlib
import json
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("--storage-root", required=True, type=Path)
args = parser.parse_args()
out = ROOT / "assets" / "papers"
out.mkdir(exist_ok=True)
versions = {
    "KGSYYKEY":"f7063ef2dd4c1f37267684e809276897577b5a00f21da605ce52c3422cc17cd2",
    "QDKDF8UH":"d749fdc9d9ceb5ea62d14756a715a0769d5db33ae70f5585fbfaa50885f499cd",
    "CLTWB7PW":"daef5a9de80fc3dd72286ccd63e8a36362dba31328549ba24dedb30fdd2ab683",
}
docs={}
for key,sha in versions.items():
    candidates=list((args.storage_root/key).glob("*.pdf"))
    assert len(candidates)==1, key
    pdf=candidates[0]
    assert hashlib.sha256(pdf.read_bytes()).hexdigest()==sha, f"PDF version changed: {key}"
    docs[key]=pymupdf.open(pdf)
specs=[
    ("phido-fig5-panel","KGSYYKEY",8,[410,79,540,185],"Fig.5, Gemini-2.5-pro/GPT-4o panel"),
    ("phido-fig5-legend","KGSYYKEY",8,[182,287,415,311],"Fig.5, original outcome-code legend"),
    ("kharel-fig1b","CLTWB7PW",3,[290,313,548,452],"Fig.1(b), original Agent loop"),
    ("kharel-fig2a","CLTWB7PW",5,[78,75,551,309],"Fig.2(a), original bend-loss iteration"),
]
manifest=[]
for name,key,page,coords,label in specs:
    docs[key][page-1].get_pixmap(matrix=pymupdf.Matrix(4,4),clip=pymupdf.Rect(coords)).save(out/f"{name}.png")
    manifest.append({"file":f"assets/papers/{name}.png","attachment_key":key,"pdf_sha256":versions[key],"pdf_page":page,"crop_pt":coords,"locator":label,"edit":"crop only; original axes/data/legend unchanged"})
(ROOT/"paper-figure-manifest.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
print("Verified 3 Zotero PDF versions and extracted 4 crops.")
