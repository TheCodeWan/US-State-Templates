#!/usr/bin/env python3
"""
Generate high-resolution PNGs from the US State map HTML files.

Usage:
    python scripts/generate-pngs.py                 # regenerate all
    python scripts/generate-pngs.py --file path/to/file.html
    python scripts/generate-pngs.py --check         # verify that PNGs match (for CI)

Requirements:
    - rsvg-convert (librsvg) must be installed:
        macOS:   brew install librsvg
        Ubuntu:  sudo apt install librsvg2-bin
        Windows: Use WSL or install via MSYS2 / vcpkg
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Optional

# All maps use the same canvas size
SVG_WIDTH = 1019
SVG_HEIGHT = 972
# 4x resolution as used in the repository
PNG_WIDTH = 4076
PNG_HEIGHT = 3888

# White background rect that matches the viewBox
BG_RECT = f'<rect x="-30" y="-74" width="{SVG_WIDTH}" height="{SVG_HEIGHT}" fill="white"/>'

ROOT = Path(__file__).parent.parent
MAPS_DIR = ROOT / "Maps of the entire US"


def extract_svg(html_path: Path) -> str:
    """Extract the main <svg> element from an HTML file and ensure white background."""
    text = html_path.read_text(encoding="utf-8")

    # Grab the first (and only) top-level SVG
    match = re.search(r"<svg[^>]*>.*?</svg>", text, re.DOTALL)
    if not match:
        raise RuntimeError(f"No <svg> found in {html_path}")

    svg = match.group(0)

    # Make sure we have a white background rect right after the opening <svg> tag.
    # This ensures consistent output even if the SVG was edited without the rect.
    if not re.search(r"<rect[^>]*fill=[\"']white", svg, re.IGNORECASE):
        svg = re.sub(r"(<svg[^>]*>)", r"\1" + BG_RECT, svg, count=1)

    return svg


def render_png(svg_content: str, output_png: Path) -> None:
    """Render SVG content to PNG using rsvg-convert at 4x resolution."""
    tmp_svg = output_png.with_suffix(".tmp.svg")
    tmp_svg.write_text(svg_content, encoding="utf-8")

    try:
        cmd = [
            "rsvg-convert",
            "--width", str(PNG_WIDTH),
            "--height", str(PNG_HEIGHT),
            "--background-color", "white",
            str(tmp_svg),
            "-o", str(output_png),
        ]
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"  ✓ Generated {output_png.relative_to(ROOT)}")
    finally:
        tmp_svg.unlink(missing_ok=True)


def find_html_files() -> List[Path]:
    """Find all map HTML files under Maps of the entire US/."""
    if not MAPS_DIR.exists():
        print(f"Error: {MAPS_DIR} not found", file=sys.stderr)
        sys.exit(1)

    htmls = sorted(MAPS_DIR.rglob("*.html"))
    # Only keep files that actually contain an SVG (skip any other HTML)
    return [h for h in htmls if "<svg" in h.read_text(encoding="utf-8", errors="ignore")]


def generate_for_file(html_path: Path) -> None:
    png_path = html_path.with_suffix(".png")
    svg = extract_svg(html_path)
    render_png(svg, png_path)


def main():
    parser = argparse.ArgumentParser(description="Generate 4x PNGs from state map HTML files.")
    parser.add_argument("--file", type=Path, help="Render only this specific HTML file")
    parser.add_argument("--check", action="store_true",
                        help="Check that PNGs are up-to-date instead of overwriting them")
    args = parser.parse_args()

    if args.file:
        files = [args.file.resolve()]
    else:
        files = find_html_files()

    if not files:
        print("No HTML map files found.")
        return

    print(f"Processing {len(files)} map(s)...\n")

    any_change = False

    for html_path in files:
        html_path = html_path.resolve()
        png_path = html_path.with_suffix(".png")

        try:
            svg = extract_svg(html_path)
        except Exception as e:
            print(f"  ✗ Failed to extract SVG from {html_path.name}: {e}")
            continue

        if args.check:
            # In check mode we just render to a temp file and compare
            tmp_png = png_path.with_suffix(".check.png")
            try:
                render_png(svg, tmp_png)
                if not png_path.exists():
                    print(f"  ✗ Missing PNG: {png_path.relative_to(ROOT)}")
                    any_change = True
                else:
                    # Simple byte compare is good enough here
                    if tmp_png.read_bytes() != png_path.read_bytes():
                        print(f"  ✗ PNG is out of date: {png_path.relative_to(ROOT)}")
                        any_change = True
                    else:
                        print(f"  ✓ {png_path.relative_to(ROOT)} is up to date")
            finally:
                tmp_png.unlink(missing_ok=True)
        else:
            render_png(svg, png_path)

    if args.check and any_change:
        print("\nSome PNGs are out of date. Run the script without --check to update them.")
        sys.exit(1)

    if not args.check:
        print("\nAll done.")


if __name__ == "__main__":
    main()
