#!/usr/bin/env python3
"""Composes Shorts thumbnails (1080x1920, 9:16) from a generated hero image and local text, so the spelling is exact.
    python3 System/scripts/make_thumbnail.py "Media/Week NN/<Day>/<Video>/upload" [thumb-name ...]   (edit THUMBS below; `publish.py` calls `compose` directly from publish.json, so new videos need no THUMBS entry)
Important content stays inside the centre 3:2 band (y 600 to 1320): thumbnails render near 3:2 on channel pages, search and TV
(ppc.land, Shorts thumbnails, July 2026; YouTube's own post gives no sizes). The Redtail mark sits below the band."""
import os, sys
from PIL import Image, ImageDraw, ImageFont
W, H = 1080, 1920
CREAM, ORANGE, INK = (249, 240, 220), (255, 128, 32), (14, 14, 22)
BOLDI = "/usr/share/fonts/truetype/noto/NotoSansDisplay-BoldItalic.ttf"
LOGO = "System/Brand/Redtail/redtail-logo-dark-small.png"   # logo on its own dark badge (user, 7 Oct 2026)
THUMBS = {  # name: (hero file, lines, index of the orange line, where the text block goes: ("end", y) or ("start", y))
    "thumb-a": ("hero-a.png", ["THE METAL", "THAT FLOATS"], 1, ("end", 1280)),
    "thumb-b": ("hero-b.png", ["NOT RARE.", "STILL A FIGHT."], 1, ("start", 650)),     # the pebble sits lower: keep the text off it
    "thumb-c": ("hero-c.png", ["60% IN", "ONE COUNTRY"], 0, ("end", 1280)),
    "thumb-jk": ("hero-jk.jpg", ["BEFORE", "GUTENBERG"], 1, ("end", 1280)),          # Jikji and Gutenberg (free stock hero, no generation)
    "thumb-sp": ("hero-sp.jpg", ["CHIPS DEPEND", "ON ONE TOWN"], 1, ("end", 1280)),          # Spruce Pine quartz (free stock hero)
    "thumb-tf": ("hero-tf.jpg", ["NO MOVING PARTS", "2.5-YEAR WAIT"], 1, ("end", 1280)),     # Transformer shortage (free stock hero)
    "thumb-dn": ("hero-dn.jpg", ["MINING THE", "DEEP SEABED"], 1, ("end", 1280)),          # Deep-sea nodules (free stock hero)
    "thumb-ev": ("hero-ev.jpg", ["BATTERY WEAR:", "ABOUT 2% A YEAR"], 1, ("end", 1280)),     # EV battery tech (free stock hero)
    "thumb-cu": ("hero-cu.png", ["17 YEARS TO", "OPEN A MINE"], 0, ("end", 1280)),   # Copper and the AI race
}
def cover(im):
    s = max(W / im.width, H / im.height); im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    return im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H))
def compose(folder, name, hero, lines, hot, where, kicker=None, chips=None):
    """Hero + big two-line title (the structure the user likes) + optional **kicker** (a topic tag above the title) and up to
    three **fact chips** under it (user, 6 Oct 2026: "add a little bit more info so the thumbnail creates a good impression
    of what the content is about"). Everything stays inside the 3:2 band (y 600 to 1320)."""
    im = cover(Image.open(f"{folder}/{hero}").convert("RGB")).convert("RGBA")
    info = bool(kicker or chips)
    top = 540 if info else 780
    shade = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(shade)
    for y in range(top, H):                                        # dark gradient under the text so it reads on any hero
        d.line([(0, y), (W, y)], fill=(8, 8, 16, min(190 if info else 205, int((y - top) * (0.55 if info else 0.5)))))
    im.alpha_composite(shade); d = ImageDraw.Draw(im)
    chips = (chips or [])[:3]
    chip_h, chip_gap, kick_h = 64, 12, 62
    size = 150 if info else 170
    while max(d.textlength(t, font=ImageFont.truetype(BOLDI, size)) for t in lines) > 960: size -= 4
    f = ImageFont.truetype(BOLDI, size); blk = len(lines) * (size + 14)
    if info:
        need = (kick_h + 22 if kicker else 0) + blk + (24 + len(chips) * (chip_h + chip_gap) if chips else 0)
        while 610 + need > 1318 and size > 90:                     # shrink the title until everything fits the band
            size -= 6; f = ImageFont.truetype(BOLDI, size); blk = len(lines) * (size + 14)
            need = (kick_h + 22 if kicker else 0) + blk + (24 + len(chips) * (chip_h + chip_gap) if chips else 0)
        y = 610
        if kicker:
            kf = ImageFont.truetype(BOLDI, 38); k = kicker.upper(); kw = d.textlength(k, font=kf) + 56
            d.rounded_rectangle([(W - kw) / 2, y, (W + kw) / 2, y + kick_h], 14, fill=ORANGE)
            d.text(((W - kw) / 2 + 28, y + 8), k, font=kf, fill=INK); y += kick_h + 22
    else:
        y = where[1] - blk if where[0] == "end" else where[1]                    # inside the 3:2 band (y 600 to 1320)
    for i, t in enumerate(lines):
        x = (W - d.textlength(t, font=f)) / 2
        d.text((x + 6, y + 6), t, font=f, fill=(0, 0, 0, 255))     # hard shadow
        d.text((x, y), t, font=f, fill=ORANGE if i == hot else CREAM, stroke_width=7, stroke_fill=INK)
        y += size + 14
    if chips:
        y += 10; cf = ImageFont.truetype(BOLDI, 40)
        for c in chips:
            c = c.upper(); cw = d.textlength(c, font=cf) + 64
            d.rounded_rectangle([(W - cw) / 2, y, (W + cw) / 2, y + chip_h], 12, fill=(14, 14, 22, 225))
            d.rounded_rectangle([(W - cw) / 2, y, (W - cw) / 2 + 10, y + chip_h], 5, fill=ORANGE)
            d.text(((W - cw) / 2 + 34, y + 9), c, font=cf, fill=CREAM); y += chip_h + chip_gap
    lg = Image.open(LOGO).convert("RGBA"); lg.thumbnail((302, 302)); im.alpha_composite(lg, ((W - lg.width) // 2, 1534))
    out = f"{folder}/{name}.jpg"; im.convert("RGB").save(out, quality=90, optimize=True); return out, os.path.getsize(out)
def drawn(folder, spec, name="thumb"):
    """Thumbnail v2 (research 9 Oct 2026, Workflow §Thumbnail): ONE focal image drawn with motion.py elements as a still (every
    element in its final state), at most 3 to 4 words, text 110 px or more (a phone tile is about 168 px wide), everything that
    matters inside the safe band x 40 to 1040, y 600 to 1320 (Shorts thumbnails render near 3:2). No kicker, chips or logo.
    spec = {"bg": "navy", "els": [...]} as in a motion plate; warnings are printed, the file is written anyway."""
    import io, cairo
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import motion
    end = 10.0
    cues = lambda c: end if str(c).startswith("end") else 0.0
    sf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    ctx = cairo.Context(sf)
    motion.Background(spec, folder, end).paint(ctx, end)
    issues, words = [], 0

    def warn(box, size, s):
        x0, y0, w, h = box
        if size < 110:
            issues.append(f"'{s}' at {size} px is unreadable on a phone tile (use 110 px or more)")
        if x0 < 40 or x0 + w > 1040 or y0 < 600 or y0 + h > 1320:
            issues.append(f"'{s}' leaves the safe band (x 40 to 1040, y 600 to 1320)")
    for el in spec["els"]:
        a, _ = motion.visibility(el, end, cues)
        ctx.save()
        ctx.push_group()
        motion.draw_el(ctx, el, end, cues, warn)
        ctx.pop_group_to_source()
        ctx.paint_with_alpha(a)
        ctx.restore()
        if el.get("kind") in ("text", "label"):
            words += len(str(el.get("text", "0")).split())
    if words > 4:
        issues.append(f"{words} words: keep it to 3 or 4")
    for i in issues:
        print("  WARN thumbnail:", i)
    buf = io.BytesIO()
    sf.write_to_png(buf)
    buf.seek(0)
    out = f"{folder}/{name}.jpg"
    Image.open(buf).convert("RGB").save(out, quality=92, optimize=True)
    return out, os.path.getsize(out)


if __name__ == "__main__":
    for n, (h, l, k, w) in THUMBS.items():
        if len(sys.argv) < 3 or n in sys.argv[2:]: print(compose(sys.argv[1], n, h, l, k, w))
