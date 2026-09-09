#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
items = [
    ("monastic-bowl.png", "法会因由、乞食、回到树园敷座；把宏大经义放回日常动作。"),
    ("open-hand.png", "无住布施与不受福德；手有行动而不把功劳握成身份。"),
    ("reflection.png", "凡所有相、诸相非相；形影可见而不固定。"),
    ("empty-sky.png", "虚空、微尘、三世心不可得；保留空间感与不占有。"),
    ("quiet-garden.png", "庄严净土与清净心；安静场景不替经文作宗教证明。"),
    ("boat-crossing.png", "筏喻、无住、如如不动与结尾渡行；小舟只作记忆类比。"),
]
manifest = []
for name, purpose in items:
    p = ROOT / "assets/images" / name
    manifest.append({
        "file": f"assets/images/{name}",
        "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
        "width": 1536,
        "height": 1024,
        "purpose": purpose,
        "prompt_constraints": "无文字、无水印、无 logo；低干扰水彩/水墨教学类比。",
    })
(ROOT / "assets/images/manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"illustrations": len(manifest)}, ensure_ascii=False))
