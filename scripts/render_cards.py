#!/usr/bin/env python3
"""Prepare source-faithful card HTML/ledgers for the official ljg-card capture."""
from __future__ import annotations

import base64
import hashlib
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = Path("/tmp/tengwang-preview/ljg-skills/skills/ljg-card")
TEMPLATE = (SKILL / "assets/full_template.html").read_text(encoding="utf-8")
TEMPLATE_DIR = Path("/tmp/diamond-sutra-preview/render")
TEMPLATE_DIR.mkdir(parents=True, exist_ok=True)


def block(tag: str, bid: str, text: str) -> str:
    return f"<{tag} data-source-block=\"{bid}\">{html.escape(text)}</{tag}>"


def main() -> None:
    cards = json.loads((ROOT / "data/cards.json").read_text(encoding="utf-8"))["cards"]
    # Reuse the official template's existing local brand asset without adding a
    # new project dependency or remote resource.
    old = Path("/Users/coben/Documents/Codex/2026-09-09/new-chat/outputs/heart-sutra-study/assets/cards/s01.html")
    old_html = old.read_text(encoding="utf-8")
    marker = 'class="avatar" src="data:image/png;base64,'
    start = old_html.index(marker) + len(marker)
    end = old_html.index('" alt=""', start)
    logo = "data:image/png;base64," + old_html[start:end]
    results = []
    for card in cards:
        blocks = []
        n = 1
        blocks.append({"id": f"b{n:03d}", "text": card["title"]}); n += 1
        blocks.append({"id": f"b{n:03d}", "text": card["front"]}); n += 1
        doc = [block("h1", blocks[0]["id"], blocks[0]["text"]), block("p", blocks[1]["id"], blocks[1]["text"])]
        for field in card["fields"]:
            blocks.append({"id": f"b{n:03d}", "text": field["label"]}); n += 1
            blocks.append({"id": f"b{n:03d}", "text": field["text"]}); n += 1
            doc.append(block("h2", blocks[-2]["id"], blocks[-2]["text"]))
            doc.append(block("p", blocks[-1]["id"], blocks[-1]["text"]))
        if card.get("image"):
            caption = "记忆插画：仅作教学类比，不是经文历史事件或宗教实相图。"
            blocks.append({"id": f"b{n:03d}", "text": caption}); n += 1
            src = (ROOT / card["image"]).resolve().as_uri()
            doc.append(f'<figure class="source-figure"><img src="{html.escape(src)}" alt="记忆插画"><figcaption data-source-block="{blocks[-1]["id"]}">{html.escape(caption)}</figcaption></figure>')
        document = "\n".join(doc)
        source = "\n\n".join(b["text"] for b in blocks) + "\n"
        ledger = {"version": 1, "source_sha256": hashlib.sha256(source.encode()).hexdigest(), "blocks": blocks}
        source_name = f"{card['id']}.txt"
        ledger_name = f"{card['id']}.ledger.json"
        html_name = f"{card['id']}.html"
        (TEMPLATE_DIR / source_name).write_text(source, encoding="utf-8")
        (TEMPLATE_DIR / ledger_name).write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        source_line = '<span class="info-source">LJG 官方 ljg-card -f · 姚秦鸠摩罗什译通行本<br>本项目编注 · v0.1.0-preview</span>'
        rendered = TEMPLATE.replace("{{DOCUMENT_HTML}}", document).replace("{{LOGO}}", logo).replace("{{SOURCE_LINE}}", source_line).replace("{{CUSTOM_CSS}}", "")
        (TEMPLATE_DIR / html_name).write_text(rendered, encoding="utf-8")
        results.append(card["id"])
    print(json.dumps({"cards": len(results), "render_dir": str(TEMPLATE_DIR)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
