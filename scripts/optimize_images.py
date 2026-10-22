#!/usr/bin/env python3
"""Resize and compress images in assets/images.

- Caps width at 1920px (keeps aspect ratio; never upscales).
- Re-encodes JPG (quality 82, progressive) and WebP (quality 80); optimizes PNG.
- Applies camera rotation and strips metadata (including GPS location).
- Keeps file names and formats, so links in Markdown never break.
- Records each optimized file's hash in scripts/.optimized-images.json so a
  file is only processed once (no repeated quality loss).

This runs automatically via GitHub Actions (.github/workflows/optimize-images.yml)
whenever images are pushed. To run it yourself: pip install pillow && python3 scripts/optimize_images.py
"""
import hashlib
import json
import sys
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
IMAGE_DIR = ROOT / "assets" / "images"
MANIFEST = ROOT / "scripts" / ".optimized-images.json"
MAX_WIDTH = 1920
EXTS = {".jpg", ".jpeg", ".png", ".webp"}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def optimize(path):
    before = path.stat().st_size
    with Image.open(path) as im:
        im = ImageOps.exif_transpose(im)
        resized = im.width > MAX_WIDTH
        if resized:
            im = im.resize((MAX_WIDTH, round(im.height * MAX_WIDTH / im.width)), Image.LANCZOS)
        ext = path.suffix.lower()
        tmp = path.with_name(path.name + ".tmp")
        if ext in (".jpg", ".jpeg"):
            im.convert("RGB").save(tmp, "JPEG", quality=82, optimize=True, progressive=True)
        elif ext == ".webp":
            im.save(tmp, "WEBP", quality=80, method=6)
        else:
            im.save(tmp, "PNG", optimize=True)
    after = tmp.stat().st_size
    # Keep the original if re-encoding didn't help and no resize was needed.
    if resized or after < before:
        tmp.replace(path)
    else:
        tmp.unlink()
        after = before
    if ext == ".png" and after > 1_000_000:
        print(f"  ! {path.relative_to(ROOT)} is a large PNG ({after // 1024} KB). "
              "Photos are much smaller saved as .jpg or .webp.")
    return before, after


def main():
    manifest = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    changed = 0
    for path in sorted(IMAGE_DIR.rglob("*")):
        if path.suffix.lower() not in EXTS or not path.is_file():
            continue
        key = path.relative_to(ROOT).as_posix()
        if manifest.get(key) == sha(path):
            continue
        before, after = optimize(path)
        manifest[key] = sha(path)
        changed += 1
        print(f"{key}: {before // 1024} KB -> {after // 1024} KB")
    # Forget files that were deleted
    manifest = {k: v for k, v in sorted(manifest.items()) if (ROOT / k).exists()}
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Optimized {changed} image(s).")


if __name__ == "__main__":
    sys.exit(main())
