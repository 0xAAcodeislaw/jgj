#!/usr/bin/env python3
from pathlib import Path
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
TMP = Path("/tmp/diamond-sutra-preview")
(ROOT / "assets/cards").mkdir(parents=True, exist_ok=True)
for d in ["card-ledgers", "card-sources", "classic-slices", "previews"]:
    (ROOT / "verification" / d).mkdir(parents=True, exist_ok=True)
for p in (TMP / "render").iterdir():
    if p.suffix in {".png", ".html"}:
        shutil.copy2(p, ROOT / "assets/cards" / p.name)
    elif p.name.endswith(".ledger.json"):
        shutil.copy2(p, ROOT / "verification/card-ledgers" / p.name)
    elif p.suffix == ".txt":
        shutil.copy2(p, ROOT / "verification/card-sources" / p.name)
# The official capture uses an absolute file URI so Chromium can resolve the
# image while rendering. Exported HTML stays portable inside a cloned repo.
for p in (ROOT / "assets/cards").glob("*.html"):
    text = p.read_text(encoding="utf-8")
    text = text.replace(f"file://{ROOT}/assets/images/", "../images/")
    p.write_text(text, encoding="utf-8")
shutil.copy2(TMP / "classic.png", ROOT / "assets/cards/classic.png")
shutil.copy2(TMP / "classic.html", ROOT / "assets/cards/classic.html")
for p in (TMP / "classic-slices").glob("*.png"):
    shutil.copy2(p, ROOT / "verification/classic-slices" / p.name)
m = json.loads((TMP / "classic.manifest.json").read_text())
for k, rel in {
    "inputPath": "data/classic.json",
    "htmlPath": "assets/cards/classic.html",
    "pngPath": "assets/cards/classic.png",
    "manifestPath": "verification/classic.manifest.json",
    "heroImagePath": "assets/images/boat-crossing.png",
}.items():
    m[k] = str(ROOT / rel)
m["qaSlices"] = [str(ROOT / "verification/classic-slices" / Path(p).name) for p in m["qaSlices"]]
for d in m["qaSliceDetails"]:
    d["path"] = str(ROOT / "verification/classic-slices" / Path(d["path"]).name)
(ROOT / "verification/classic.manifest.json").write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n")
shutil.copy2(TMP / "render-result.json", ROOT / "verification/render-result.json")
print(json.dumps({"cards": len(list((ROOT / "assets/cards").glob("*.png"))), "slices": len(list((ROOT / "verification/classic-slices").glob("*.png")))}, ensure_ascii=False))
