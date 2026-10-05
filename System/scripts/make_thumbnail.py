#!/usr/bin/env python3
"""Composes Shorts thumbnails (1080x1920, 9:16) from a generated hero image and local text, so the spelling is exact.
    python3 System/scripts/make_thumbnail.py "Media/Week NN/<Video>/upload" [thumb-name ...]   (edit THUMBS below)
Important content stays inside the centre 3:2 band (y 600 to 1320): thumbnails render near 3:2 on channel pages, search and TV
(ppc.land, Shorts thumbnails, July 2026; YouTube's own post gives no sizes). The Redtail mark sits below the band."""
import os, sys
from PIL import Image, ImageDraw, ImageFont
W, H = 1080, 1920
CREAM, ORANGE, INK = (249, 240, 220), (255, 128, 32), (14, 14, 22)
BOLDI = "/usr/share/fonts/truetype/noto/NotoSansDisplay-BoldItalic.ttf"
LOGO = "System/Brand/Redtail/redtail-logo.png"
THUMBS = {  # name: (hero file, lines, index of the orange line, where the text block goes: ("end", y) or ("start", y))
    "thumb-a": ("hero-a.png", ["THE METAL", "THAT FLOATS"], 1, ("end", 1280)),
    "thumb-b": ("hero-b.png", ["NOT RARE.", "STILL A FIGHT."], 1, ("start", 650)),     # the pebble sits lower: keep the text off it
    "thumb-c": ("hero-c.png", ["60% IN", "ONE COUNTRY"], 0, ("end", 1280)),
    "thumb-cu": ("hero-cu.png", ["17 YEARS TO", "OPEN A MINE"], 0, ("end", 1280)),   # Copper and the AI race
}
def cover(im):
    s = max(W / im.width, H / im.height); im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    return im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H))
def compose(folder, name, hero, lines, hot, where):
    im = cover(Image.open(f"{folder}/{hero}").convert("RGB")).convert("RGBA")
    shade = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(shade)
    for y in range(780, H):                                        # dark gradient under the text so it reads on any hero
        d.line([(0, y), (W, y)], fill=(8, 8, 16, min(205, int((y - 780) * 0.5))))
    im.alpha_composite(shade); d = ImageDraw.Draw(im)
    size = 170
    while max(d.textlength(t, font=ImageFont.truetype(BOLDI, size)) for t in lines) > 960: size -= 4
    f = ImageFont.truetype(BOLDI, size); blk = len(lines) * (size + 14)
    y = where[1] - blk if where[0] == "end" else where[1]                    # inside the 3:2 band (y 600 to 1320)
    for i, t in enumerate(lines):
        x = (W - d.textlength(t, font=f)) / 2
        d.text((x + 6, y + 6), t, font=f, fill=(0, 0, 0, 255))     # hard shadow
        d.text((x, y), t, font=f, fill=ORANGE if i == hot else CREAM, stroke_width=7, stroke_fill=INK)
        y += size + 14
    lg = Image.open(LOGO).convert("RGBA"); lg.thumbnail((250, 250)); im.alpha_composite(lg, ((W - lg.width) // 2, 1560))
    out = f"{folder}/{name}.jpg"; im.convert("RGB").save(out, quality=90, optimize=True); return out, os.path.getsize(out)
if __name__ == "__main__":
    for n, (h, l, k, w) in THUMBS.items():
        if len(sys.argv) < 3 or n in sys.argv[2:]: print(compose(sys.argv[1], n, h, l, k, w))
