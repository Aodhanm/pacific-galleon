#!/usr/bin/env python3
"""Set a line of display type as SVG OUTLINE PATHS.

Why: the arcade's marquees are drawn in Trattatello, which is a macOS system
font. Set as live <text> it falls back to a plain serif on every other machine
and the whole look goes. The doghole marquee solves this by carrying the
letterforms in the file itself; this does the same, programmatically.

  python3 text_to_paths.py "PACIFIC GALLEON" --size 54 --x 34 --y 86
"""
import argparse, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

FONTS = {
    "trattatello": "/System/Library/Fonts/Supplemental/Trattatello.ttf",
    "luminari":    "/System/Library/Fonts/Supplemental/Luminari.ttf",
    "academy":     "/System/Library/Fonts/Supplemental/Academy Engraved LET Fonts.ttf",
}

def layout(text, font_key="trattatello", size=54.0, x=0.0, y=0.0, tracking=0.0):
    """Return (list of <path> strings, total advance width)."""
    f = TTFont(FONTS[font_key])
    upem = f["head"].unitsPerEm
    cmap = f.getBestCmap()
    gs = f.getGlyphSet()
    hmtx = f["hmtx"]
    s = size / upem
    out, pen_x = [], x
    for ch in text:
        if ch == " ":
            pen_x += (hmtx[cmap[ord(" ")]][0] if ord(" ") in cmap else upem * .3) * s + tracking
            continue
        gname = cmap.get(ord(ch))
        if gname is None:
            print(f"  !! no glyph for {ch!r}", file=sys.stderr); continue
        pen = SVGPathPen(gs)
        gs[gname].draw(pen)
        d = pen.getCommands()
        if d:
            out.append(f'<path transform="translate({pen_x:.2f},{y:.2f}) '
                       f'scale({s:.6f},{-s:.6f})" d="{d}"/>')
        pen_x += hmtx[gname][0] * s + tracking
    return out, pen_x - x

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("text")
    p.add_argument("--font", default="trattatello", choices=list(FONTS))
    p.add_argument("--size", type=float, default=54.0)
    p.add_argument("--x", type=float, default=0.0)
    p.add_argument("--y", type=float, default=0.0)
    p.add_argument("--tracking", type=float, default=0.0)
    a = p.parse_args()
    paths, w = layout(a.text, a.font, a.size, a.x, a.y, a.tracking)
    print(f"<!-- {a.text!r} in {a.font} {a.size}px, advance {w:.1f} -->", file=sys.stderr)
    print("\n".join(paths))
