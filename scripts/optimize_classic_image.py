#!/usr/bin/env python3
"""Write a smaller palette PNG for mobile and GitHub image viewers.

The official ljg-classic render remains the source of the layout and text.
This post-processing step keeps the same pixel dimensions while reducing the
colour table; it does not resize, crop, or rewrite any annotation content.
"""

from pathlib import Path
import hashlib
import os
import tempfile

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
IMAGE = ROOT / "assets/cards/classic.png"
COLORS = 256


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    with Image.open(IMAGE) as image:
        original_size = image.size
        if image.mode not in {"RGB", "RGBA"}:
            raise SystemExit(f"unexpected source mode: {image.mode}")
        optimized = image.quantize(
            colors=COLORS,
            method=Image.Quantize.MEDIANCUT,
            dither=Image.Dither.NONE,
        )

    fd, temporary_name = tempfile.mkstemp(prefix="classic-", suffix=".png", dir=IMAGE.parent)
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        optimized.save(temporary, format="PNG", optimize=True)
        temporary.replace(IMAGE)
    finally:
        temporary.unlink(missing_ok=True)

    print(
        {
            "path": str(IMAGE.relative_to(ROOT)),
            "width": original_size[0],
            "height": original_size[1],
            "colors": COLORS,
            "bytes": IMAGE.stat().st_size,
            "sha256": sha256(IMAGE),
        }
    )


if __name__ == "__main__":
    main()
