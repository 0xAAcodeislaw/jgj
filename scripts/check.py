#!/usr/bin/env python3
"""Offline structural checks for the Diamond Sutra study project."""
from pathlib import Path
import hashlib
import json
import re
import struct
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

R = Path(__file__).resolve().parents[1]
errors = []


def check(ok, message):
    if not ok:
        errors.append(message)


def read_json(path):
    return json.loads((R / path).read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


for path in R.rglob("*.json"):
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"JSON {path.relative_to(R)}: {exc}")

cards = read_json("data/cards.json")["cards"]
sections = read_json("data/sections.json")
classic = read_json("data/classic.json")
manifest = read_json("data/manifest.json")

check(len(cards) == 160, "expected 160 cards")
check(len(sections) == 32, "expected 32 sections")
check(len({card["id"] for card in cards}) == len(cards), "card IDs are unique")
check(len({section["id"] for section in sections}) == len(sections), "section IDs are unique")

original = "".join(section["original"] for section in sections)
check(original == classic["original"], "classic original differs from sections")
token_text = "".join(
    token["text"] for passage in classic["passages"] for token in passage["tokens"]
)
check(token_text == original, "classic token readback differs from original")
source_text = (R / "data/source-text.txt").read_text(encoding="utf-8")
check(sha(R / "data/source-text.txt") == read_json("verification/source-lock.json")["source_text_sha256"], "source hash mismatch")
check(re.sub(r"\s", "", source_text) == original, "locked source differs from section join")
check(original.endswith("佛说是经已，长老须菩提及诸比丘、比丘尼、优婆塞、优婆夷、一切世间天、人、阿修罗，闻佛所说，皆大欢喜，信受奉行。"), "complete ending is missing")
check(len(re.findall(r"[\u4e00-\u9fff]", original)) == 5179, "expected 5179 Chinese characters")
check(manifest.get("text_chars") == 5179, "manifest character count")
check(len(read_json("data/pronunciation.json")) == 42, "42 pronunciation entries")
check(len(read_json("data/allusions.json")) == 23, "23 allusion entries")
check(len(read_json("data/idioms.json")) == 22, "22 idiom entries")
check(len(read_json("data/learning.json")) == 8, "8 memory entries")
check(len(list((R / "notes").glob("*.org"))) == 7, "7 Org notes")

comparison = read_json("verification/version-comparison.json")
check(comparison.get("base"), "chosen edition is recorded")
check(comparison.get("cbeta"), "reference edition is recorded")
check((R / "data/cbeta-comparison.txt").is_file(), "CBETA comparison text is missing")
app_js = (R / "preview/app.js").read_text(encoding="utf-8")
check("tengwang-learned" not in app_js, "old local storage key leaked")
check("heart-sutra" not in app_js, "心经 local storage key leaked")
check("diamond-sutra-learned-v1" in app_js, "diamond storage key missing")

full_text_md = (R / "content/full-text.md").read_text(encoding="utf-8")
check(all(section["original"] in full_text_md for section in sections), "full-text Markdown misses a section")
check(all(section.get("reading") for section in sections), "section reading fields missing")
tokens = [token for passage in classic["passages"] for token in passage["tokens"] if not token.get("punctuation")]
check(len(tokens) >= 196, "expected sentence-level annotated tokens")
check(not any(token.get("note") == "本段语境中的连续语义单位；结合整句理解。" for token in tokens), "placeholder annotation remains")
check(all(token.get("note") for token in tokens), "an annotated token has no note")


class HtmlBlocks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.blocks = []
        self.active = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ("href", "src"):
            if key in attrs:
                self.links.append(attrs[key])
        if "data-source-block" in attrs:
            self.active = [attrs["data-source-block"], ""]

    def handle_data(self, data):
        if self.active is not None:
            self.active[1] += data

    def handle_endtag(self, tag):
        if self.active is not None:
            self.blocks.append(self.active)
            self.active = None


for card in cards:
    for key in ("markdown", "png", "html"):
        check((R / card[key]).is_file(), f"{card['id']} {key} is missing")
    check(card.get("fields") and all(field.get("label") and field.get("text") for field in card["fields"]), f"{card['id']} fields are incomplete")
    ledger_path = R / f"verification/card-ledgers/{card['id']}.ledger.json"
    source_path = R / f"verification/card-sources/{card['id']}.txt"
    check(ledger_path.is_file() and source_path.is_file(), f"{card['id']} ledger or source is missing")
    if ledger_path.is_file() and source_path.is_file():
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        check(sha(source_path) == ledger["source_sha256"], f"{card['id']} source hash")
        parser = HtmlBlocks()
        parser.feed((R / card["html"]).read_text(encoding="utf-8"))
        expected_blocks = [[block["id"], block["text"]] for block in ledger["blocks"]]
        check(parser.blocks == expected_blocks, f"{card['id']} HTML block readback")
        markdown = (R / card["markdown"]).read_text(encoding="utf-8")
        for field in card["fields"]:
            check(field["text"] in markdown, f"{card['id']} Markdown field")
    if card.get("image"):
        check((R / card["image"]).is_file(), f"{card['id']} image is missing")


for path in R.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    refs = []
    if path.suffix == ".html":
        parser = HtmlBlocks()
        parser.feed(path.read_text(encoding="utf-8"))
        refs = parser.links
    elif path.suffix == ".md":
        refs = re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8"))
    for ref in refs:
        url = urlsplit(ref)
        if url.scheme or not url.path or url.path.startswith("#"):
            continue
        check((path.parent / unquote(url.path)).exists(), f"broken link {path.relative_to(R)} -> {ref}")
    if path.suffix == ".png":
        data = path.read_bytes()
        check(data[:8] == b"\x89PNG\r\n\x1a\n", f"PNG signature {path.relative_to(R)}")
        if len(data) >= 24:
            width, height = struct.unpack(">II", data[16:24])
            check(width > 0 and height > 0, f"PNG size {path.relative_to(R)}")
            if path.parent == R / "assets/cards":
                check(width == 1080, f"card width {path.name}")

check(len(list((R / "assets/cards").glob("*.png"))) == 161, "expected 161 rendered PNGs including classic")
check(len(list((R / "assets/cards").glob("*.html"))) == 161, "expected 161 rendered HTML files including classic")
images = read_json("assets/images/manifest.json")
check(len(images) == 6, "expected 6 illustrations")
for image in images:
    image_path = R / image["file"]
    check(image_path.is_file(), f"image missing {image['file']}")
    if image_path.is_file():
        check(sha(image_path) == image["sha256"], f"image hash {image['file']}")

classic_manifest = read_json("verification/classic.manifest.json")
check((R / "assets/cards/classic.png").stat().st_size < 10 * 1024 * 1024, "classic PNG should stay below 10 MiB for mobile viewers")
check(classic_manifest.get("pngOptimization", {}).get("sameDimensions") is True, "classic PNG optimization record is missing")
for key, relative in (("input", "data/classic.json"), ("html", "assets/cards/classic.html"), ("png", "assets/cards/classic.png")):
    check(sha(R / relative) == classic_manifest["sha256"][key], f"classic {key} hash")
for detail in classic_manifest.get("qaSliceDetails", []):
    slice_path = R / "verification/classic-slices" / Path(detail["path"]).name
    check(slice_path.is_file(), f"classic slice missing {slice_path.name}")
    if slice_path.is_file():
        check(sha(slice_path) == detail["sha256"], f"classic slice hash {slice_path.name}")
render_result = read_json("verification/render-result.json")
check(len(render_result) == 160, "render result card count")
check(all(item.get("ok") for item in render_result), "a card was not verified and captured")

result = {
    "status": "pass" if not errors else "fail",
    "cards": len(cards),
    "sections": len(sections),
    "annotations": len(tokens),
    "rendered_cards": 161,
    "illustrations": len(images),
    "chars": len(re.findall(r"[\u4e00-\u9fff]", original)),
    "errors": errors,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
