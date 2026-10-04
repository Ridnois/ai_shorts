#!/usr/bin/env python3
"""Draws the channel's brand assets into System/Brand/ (run from the vault root): python3 System/scripts/make_brand.py
  avatar.png   800 px profile picture; avatar.svg the vector source
  banner.png   2560 x 1440 channel banner (the text sits in the 1546 x 423 centre safe area)
Colours and fonts are the tokens of System/Content/Channel playbook.md §3.1."""
from PIL import Image, ImageDraw, ImageFont
import os

INK, INK2, PAPER, COPPER = (28, 26, 23), (11, 26, 43), (249, 246, 238), (199, 107, 56)
OUT = "System/Brand"
BOLD = "/usr/share/fonts/truetype/noto/NotoSansDisplay-Bold.ttf"
REG = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
SS = 4                                            # supersampling for smooth edges


def ground(w, h):
    im = Image.new("RGB", (w, h), INK)
    px = im.load()
    for y in range(h):                            # a slow vertical gradient from ink to the cryogenic navy
        t = y / (h - 1)
        c = tuple(round(INK[i] * (1 - 0.55 * t) + INK2[i] * 0.55 * t) for i in range(3))
        for x in range(w):
            px[x, y] = c
    return im


def draw_mark(d, cx, cy, s, label=True):
    """ring + dot + leader line + label bar, s = ring radius in output px (all scaled by SS by the caller)."""
    d.ellipse([cx - s, cy - s, cx + s, cy + s], outline=COPPER, width=max(2, round(s * 0.14)))
    r = s * 0.52
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=COPPER)
    if label:
        k = 0.7071
        x1, y1 = cx + s * k, cy - s * k
        x2, y2 = cx + s * 2.6, cy - s * 2.4
        d.line([x1, y1, x2, y2], fill=COPPER, width=max(2, round(s * 0.09)))
        bw, bh = s * 3.2, s * 0.9
        d.rounded_rectangle([x2, y2 - bh / 2, x2 + bw, y2 + bh / 2], radius=bh * 0.2, fill=PAPER)
        d.rectangle([x2, y2 - bh / 2, x2 + bh * 0.16, y2 + bh / 2], fill=COPPER)
        for k_, wfrac in ((0.27, 0.70), (0.58, 0.45)):                    # two ink lines: it reads as a label with text
            d.rounded_rectangle([x2 + bh * 0.42, y2 - bh / 2 + bh * k_ - bh * 0.07, x2 + bh * 0.42 + (bw - bh * 0.8) * wfrac, y2 - bh / 2 + bh * k_ + bh * 0.07], radius=bh * 0.07, fill=INK)


def small(img, w, h):
    return img.resize((w, h), Image.LANCZOS)


# avatar 800: the whole annotation (ring, dot, leader, label) inside the circular crop (radius 400)
A = ground(800 * SS, 800 * SS)
draw_mark(ImageDraw.Draw(A), 213 * SS, 472 * SS, 78 * SS)
small(A, 800, 800).save(f"{OUT}/avatar.png")
svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800">
<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c1a17"/><stop offset="1" stop-color="#0b1a2b"/></linearGradient></defs>
<rect width="800" height="800" fill="url(#g)"/>
<g transform="translate(-87 -28)">
<circle cx="300" cy="500" r="78" fill="none" stroke="#c76b38" stroke-width="11"/>
<circle cx="300" cy="500" r="40.6" fill="#c76b38"/>
<line x1="355.2" y1="444.8" x2="502.8" y2="313" stroke="#c76b38" stroke-width="7"/>
<rect x="502.8" y="278" width="249.6" height="70" rx="14" fill="#f9f6ee"/>
<rect x="502.8" y="278" width="11" height="70" fill="#c76b38"/>
<rect x="532" y="291" width="154" height="10" rx="5" fill="#1c1a17"/>
<rect x="532" y="318" width="99" height="10" rx="5" fill="#1c1a17"/>
</g>
</svg>
'''
open(f"{OUT}/avatar.svg", "w").write(svg)

# banner 2560 x 1440: wordmark, tagline and mark inside the centre safe area (1546 x 423)
Wb, Hb = 2560, 1440
B = ground(Wb * 1, Hb * 1).convert("RGBA")
bs = Image.new("RGBA", (Wb * 2, Hb * 2), (0, 0, 0, 0))
d = ImageDraw.Draw(bs)
draw_mark(d, 851 * 2, 720 * 2, 62 * 2, label=False)
bs = bs.resize((Wb, Hb), Image.LANCZOS)
B = Image.alpha_composite(B, bs)
d = ImageDraw.Draw(B)
f1, f2 = ImageFont.truetype(BOLD, 190), ImageFont.truetype(REG, 54)
d.text((981, 700), "Cutaway", font=f1, fill=PAPER, anchor="lm")
d.text((991, 850), "HOW IT WORKS.  WITH SOURCES.", font=f2, fill=COPPER, anchor="lm")
B.convert("RGB").save(f"{OUT}/banner.png")
print("ok", os.listdir(OUT))
