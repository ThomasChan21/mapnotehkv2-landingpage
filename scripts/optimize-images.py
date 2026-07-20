#!/usr/bin/env python3
"""
Resize landing page screenshots and export WebP + PNG variants for responsive srcset.
Also generates og-image.jpg for social link previews.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ASSETS = Path(__file__).resolve().parent.parent / "assets"

# Source file -> list of (suffix, width, height)
SCREENSHOTS: dict[str, list[tuple[str, int, int]]] = {
    "hero-screenshot.png": [
        ("-300", 300, 650),
        ("-560", 560, 1213),
        ("-600", 600, 1300),
    ],
    "feature-map.png": [
        ("-280", 280, 607),
        ("-560", 560, 1213),
    ],
    "feature-media.png": [
        ("-280", 280, 607),
        ("-560", 560, 1213),
    ],
    "feature-ai.png": [
        ("-280", 280, 607),
        ("-560", 560, 1213),
    ],
    "feature-planning.png": [
        ("-280", 280, 628),
        ("-560", 560, 1256),
    ],
    # Two-page A4 PDF stack (feature-pdf.png generated from source PDF)
    "feature-pdf.png": [
        ("-280", 280, 0),
        ("-560", 560, 0),
    ],
}

LOGO_SIZES = [
    ("logo-140", 140, 70),
    ("logo-180", 180, 90),
    ("logo-220", 220, 110),
]


def resize_cover(img: Image.Image, width: int, height: int) -> Image.Image:
    """Scale image to exact width x height (phone screenshots)."""
    return img.resize((width, height), Image.Resampling.LANCZOS)


def resize_fit_width(img: Image.Image, width: int) -> Image.Image:
    """Scale image to target width, preserving aspect ratio (PDF stacks)."""
    ratio = width / img.width
    height = max(1, round(img.height * ratio))
    return img.resize((width, height), Image.Resampling.LANCZOS)


def export_variants(stem: str, variants: list[tuple[str, int, int]]) -> None:
    """Export WebP and PNG for each size variant of a source screenshot."""
    src = ASSETS / stem
    if not src.exists():
        print(f"skip missing: {src}")
        return

    base = stem.replace(".png", "")
    img = Image.open(src).convert("RGB")
    fit_width_only = stem == "feature-pdf.png"

    for suffix, w, h in variants:
        out = resize_fit_width(img, w) if fit_width_only else resize_cover(img, w, h)
        webp_path = ASSETS / f"{base}{suffix}.webp"
        png_path = ASSETS / f"{base}{suffix}.png"
        out.save(webp_path, "WEBP", quality=82, method=6)
        out.save(png_path, "PNG", optimize=True)
        print(f"  {webp_path.name} ({webp_path.stat().st_size // 1024} KB)")
        print(f"  {png_path.name} ({png_path.stat().st_size // 1024} KB)")


def export_logo() -> None:
    """Export resized logo PNG for header."""
    src = ASSETS / "logo.png"
    if not src.exists():
        return
    img = Image.open(src).convert("RGBA")
    for name, w, h in LOGO_SIZES:
        out = img.resize((w, h), Image.Resampling.LANCZOS)
        path = ASSETS / f"{name}.png"
        out.save(path, "PNG", optimize=True)
        print(f"  {path.name} ({path.stat().st_size // 1024} KB)")


def create_og_image() -> None:
    """Create 1200x630 OG share image with hero screenshot and branding."""
    hero_src = ASSETS / "hero-screenshot-600.png"
    if not hero_src.exists():
        hero_src = ASSETS / "hero-screenshot.png"

    canvas = Image.new("RGB", (1200, 630), (245, 247, 251))
    draw = ImageDraw.Draw(canvas)

    # Teal accent bar
    draw.rectangle([(0, 0), (1200, 6)], fill=(15, 118, 110))

    # Title text
    try:
        font_lg = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 42)
        font_sm = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 24)
    except OSError:
        font_lg = ImageFont.load_default()
        font_sm = ImageFont.load_default()

    draw.text((60, 80), "MapNoteHK", fill=(15, 23, 42), font=font_lg)
    draw.text(
        (60, 150),
        "香港地產代理專用的地圖筆記工具",
        fill=(71, 85, 105),
        font=font_sm,
    )
    draw.text(
        (60, 200),
        "規劃申請地圖 · 五類筆記 · 分享 PDF · AI 整理",
        fill=(15, 118, 110),
        font=font_sm,
    )

    # Phone mockup on right
    phone = Image.open(hero_src).convert("RGB")
    phone_h = 520
    ratio = phone_h / phone.height
    phone_w = int(phone.width * ratio)
    phone = phone.resize((phone_w, phone_h), Image.Resampling.LANCZOS)
    x = 1200 - phone_w - 80
    y = (630 - phone_h) // 2
    canvas.paste(phone, (x, y))

    out = ASSETS / "og-image.jpg"
    canvas.save(out, "JPEG", quality=85, optimize=True)
    print(f"  {out.name} ({out.stat().st_size // 1024} KB)")


def main() -> None:
    print("Exporting screenshot variants...")
    for stem, variants in SCREENSHOTS.items():
        print(stem)
        export_variants(stem, variants)

    print("Exporting logo...")
    export_logo()

    print("Creating OG image...")
    create_og_image()
    print("Done.")


if __name__ == "__main__":
    main()
