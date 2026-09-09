#!/usr/bin/env python3
from pathlib import Path
import concurrent.futures
import json
import subprocess

TMP = Path("/tmp/diamond-sutra-preview/render")
SKILL = Path("/tmp/tengwang-preview/ljg-skills/skills/ljg-card")
ids = sorted(p.stem for p in TMP.glob("*.html"))


def run(cid: str):
    commands = [
        ["bun", "assets/verify-full-text.ts", str(TMP / f"{cid}.ledger.json"), str(TMP / f"{cid}.html"), str(TMP / f"{cid}.txt")],
        ["bun", "assets/capture.ts", str(TMP / f"{cid}.html"), str(TMP / f"{cid}.png"), "1080", "1600", "fullpage"],
    ]
    for cmd in commands:
        p = subprocess.run(cmd, cwd=SKILL, text=True, capture_output=True)
        if p.returncode:
            return {"id": cid, "ok": False, "error": (p.stdout + p.stderr)[-4000:]}
    return {"id": cid, "ok": True}


def main():
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(run, ids):
            results.append(result)
            if not result["ok"]:
                print(json.dumps(result, ensure_ascii=False), flush=True)
            elif len(results) % 20 == 0:
                print(f"{len(results)}/{len(ids)} verified and captured", flush=True)
    (Path("/tmp/diamond-sutra-preview") / "render-result.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n")
    print(f"DONE {sum(x['ok'] for x in results)} of {len(results)}")
    raise SystemExit(0 if all(x["ok"] for x in results) else 1)


if __name__ == "__main__":
    main()
