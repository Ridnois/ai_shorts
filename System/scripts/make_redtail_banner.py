#!/usr/bin/env python3
"""The Redtail channel banner (the user's winner, banner B, 5 Oct 2026). Free, local (PIL), no model call.
2560x1440; crest + slogan sit inside the 1546x423 centre safe area (size from memory, check the Studio preview). python3 System/scripts/make_redtail_banner.py
Writes System/Brand/Redtail/redtail-banner.png and a preview with the safe-area guide in Media/_canal/brand-redtail/."""
import os
from PIL import Image, ImageDraw, ImageFont
OUT = "Media/_canal/brand-redtail"; os.makedirs(OUT, exist_ok=True)
NAVY, INK, CREAM, ORANGE = (11, 26, 43), (20, 22, 38), (249, 240, 220), (240, 110, 30)
BOLDI = "/usr/share/fonts/truetype/noto/NotoSansDisplay-BoldItalic.ttf"
LOGO = "System/Brand/Redtail/redtail-logo.png"
HEAD, SUB = "SCIENCE AT FULL SPEED.", "STRANGE, FAST AND TRUE."
def trim(path):
    im = Image.open(path).convert("RGBA"); return im.crop(im.getchannel("A").point(lambda v: 255 if v > 20 else 0).getbbox())
def field():
    im = Image.new("RGB", (2560, 1440)); px = im.load()
    for y in range(1440):
        t = y / 1439; c = tuple(round(NAVY[i] * (1 - t) + INK[i] * t) for i in range(3))
        for x in range(2560): px[x, y] = c
    d = ImageDraw.Draw(im, "RGBA")
    for x in range(0, 2560, 160): d.rectangle([x, 0, x + 6, 1440], fill=(255, 255, 255, 22))
    for x in range(80, 2560, 160):
        for y in range(0, 1440, 90): d.rectangle([x, y, x + 3, y + 28], fill=(255, 255, 255, 30))
    d.rectangle([0, 1380, 2560, 1440], fill=ORANGE); return im
def banner(head, sub):
    A = field(); d = ImageDraw.Draw(A); lg = trim(LOGO); s = 400 / max(lg.size); lg = lg.resize((round(lg.width * s), round(lg.height * s)), Image.LANCZOS)
    gap, room = 60, 1500 - lg.width - 60                              # keep logo + text inside ~1500 px, centred
    hs = 92
    while d.textlength(head, font=ImageFont.truetype(BOLDI, hs)) > room or d.textlength(sub, font=ImageFont.truetype(BOLDI, round(hs * .48))) > room: hs -= 2
    f1, f2 = ImageFont.truetype(BOLDI, hs), ImageFont.truetype(BOLDI, round(hs * .48))
    tw = max(d.textlength(head, font=f1), d.textlength(sub, font=f2)); x0 = 1280 - (lg.width + gap + tw) / 2
    A.paste(lg, (round(x0), round(720 - lg.height / 2)), lg)
    tx = x0 + lg.width + gap; d.text((tx, 690), head, font=f1, fill=CREAM, anchor="ls"); d.text((tx, 690 + hs * .8), sub, font=f2, fill=ORANGE, anchor="ls")
    return A
if __name__ == "__main__":
    b = banner(HEAD, SUB); b.save("System/Brand/Redtail/redtail-banner.png", optimize=True)
    g = b.copy(); ImageDraw.Draw(g).rectangle([1280 - 773, 720 - 211, 1280 + 773, 720 + 211], outline=(255, 255, 255), width=4); g.resize((1280, 720)).save(f"{OUT}/preview.png")
    print("ok")
