#!/usr/bin/env python3
"""Draws the channel's brand assets into System/Brand/ (run from the vault root): python3 System/scripts/make_brand.py
  avatar.png   800 px profile picture (the copper fox)
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


FOX = [  # (polygon, colour) in a -1..1 box: head, white cheeks, inner ears, nose; the right eye is the callout ring-and-dot
    ([(-1, -.95), (-.45, -.45), (.45, -.45), (1, -.95), (.95, .1), (0, 1), (-.95, .1)], COPPER),
    ([(-.95, .1), (0, .25), (.95, .1), (0, 1)], PAPER),
    ([(-.82, -.7), (-.55, -.4), (-.8, -.2)], INK), ([(.82, -.7), (.55, -.4), (.8, -.2)], INK),
    ([(-.12, .78), (.12, .78), (0, .93)], INK),
]


def draw_fox(d, cx, cy, s):
    """s = half-width in px. A fox that is also an annotation: its right eye is the channel's ring-and-dot."""
    for pts, col in FOX:
        d.polygon([(cx + x * s, cy + y * s) for x, y in pts], fill=col)
    e = lambda x, y, r, **k: d.ellipse([cx + (x - r) * s, cy + (y - r) * s, cx + (x + r) * s, cy + (y + r) * s], **k)
    e(-.38, -.02, .09, fill=INK)
    e(.38, -.02, .2, outline=PAPER, width=max(2, round(s * 0.05)))
    e(.38, -.02, .09, fill=INK)


def small(img, w, h):
    return img.resize((w, h), Image.LANCZOS)


# avatar 800: the fox centred inside the circular crop
A = ground(800 * SS, 800 * SS)
draw_fox(ImageDraw.Draw(A), 400 * SS, 410 * SS, 250 * SS)
small(A, 800, 800).save(f"{OUT}/avatar.png")
if os.path.exists(f"{OUT}/avatar.svg"):
    os.remove(f"{OUT}/avatar.svg")                # the vector twin was the old mark; PNG is what Studio takes

# banner 2560 x 1440: fox, wordmark and tagline inside the centre safe area (1546 x 423)
Wb, Hb = 2560, 1440
B = ground(Wb, Hb)
bs = Image.new("RGB", (Wb * 2, Hb * 2), (0, 0, 0))
mask = Image.new("L", bs.size, 0)
big = Image.new("RGBA", bs.size, (0, 0, 0, 0))
draw_fox(ImageDraw.Draw(big), 880 * 2, 720 * 2, 130 * 2)
big = big.resize((Wb, Hb), Image.LANCZOS)
B = B.convert("RGBA"); B.alpha_composite(big)
d = ImageDraw.Draw(B)
f1, f2 = ImageFont.truetype(BOLD, 170), ImageFont.truetype(REG, 50)
d.text((1050, 690), "Cutaway", font=f1, fill=PAPER, anchor="lm")
d.text((1058, 830), "SCIENCE, CUT OPEN.  WITH SOURCES.", font=f2, fill=COPPER, anchor="lm")
B.convert("RGB").save(f"{OUT}/banner.png")
print("ok", os.listdir(OUT))
