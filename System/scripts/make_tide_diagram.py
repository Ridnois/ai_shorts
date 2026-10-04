#!/usr/bin/env python3
"""Draws the tidal-bulge schematic used by the Moon video (exact geometry, no model): python3 System/scripts/make_tide_diagram.py <out.png>
Seen from above the north pole: Earth spins and the Moon orbits counter-clockwise; the ocean bulges are carried AHEAD of the Earth-Moon
line, so the near bulge pulls the Moon forward along its orbit. Not to scale (bulge and Moon exaggerated)."""
import math, sys
from PIL import Image, ImageDraw
SS, W, H = 3, 1024, 1536
im = Image.new("RGB", (W * SS, H * SS), (230, 230, 232))
d = ImageDraw.Draw(im)
S = lambda v: v * SS
cx, cy, R = 380, 780, 150                      # Earth
mx, my, mr = 840, 780, 46                      # Moon
tilt = math.radians(24)                        # the bulge axis leads the Earth-Moon line (counter-clockwise on the page = upward on the right)
a, b = 205, 158                                # ocean ellipse semi-axes
def rot(x, y, t): return (x * math.cos(t) - y * math.sin(t), x * math.sin(t) + y * math.cos(t))
pts = [rot(a * math.cos(u / 100 * 2 * math.pi), b * math.sin(u / 100 * 2 * math.pi), -tilt) for u in range(100)]   # -tilt: counter-clockwise on a y-down page
d.polygon([(S(cx + x), S(cy + y)) for x, y in pts], fill=(48, 112, 190), outline=(25, 70, 130))
d.ellipse([S(cx - R), S(cy - R), S(cx + R), S(cy + R)], fill=(122, 104, 82), outline=(80, 66, 50), width=S(3))
d.ellipse([S(mx - mr), S(my - mr), S(mx + mr), S(my + mr)], fill=(150, 150, 154), outline=(95, 95, 100), width=S(3))
# dashed line between the centres
n = 34
for k in range(n):
    if k % 2 == 0:
        x0 = cx + R + (mx - mr - cx - R) * k / n
        x1 = cx + R + (mx - mr - cx - R) * (k + 1) / n
        d.line([S(x0), S(cy), S(x1), S(cy)], fill=(70, 70, 76), width=S(3))
def arrow(p0, p1, col=(28, 26, 23), w=7, head=26):
    d.line([(S(p0[0]), S(p0[1])), (S(p1[0]), S(p1[1]))], fill=col, width=S(w))
    ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    for s in (-1, 1):
        q = (p1[0] - head * math.cos(ang) + s * head * 0.55 * math.sin(ang), p1[1] - head * math.sin(ang) - s * head * 0.55 * math.cos(ang))
        d.polygon([(S(p1[0]), S(p1[1])), (S(q[0]), S(q[1])), (S(p1[0] - head * 0.6 * math.cos(ang)), S(p1[1] - head * 0.6 * math.sin(ang)))], fill=col)
# Earth's spin: a counter-clockwise arc below-left of Earth, ending with an arrowhead
arc = [(cx + 255 * math.cos(math.radians(t)), cy - 255 * math.sin(math.radians(t))) for t in range(200, 340, 4)]   # t degrees counter-clockwise (page y flipped)
arc = [(cx + 255 * math.cos(math.radians(t)), cy - 255 * math.sin(math.radians(t))) for t in range(120, 240, 3)]
d.line([(S(x), S(y)) for x, y in arc], fill=(28, 26, 23), width=S(7))
arrow(arc[-4], arc[-1])
# Moon's orbit direction: straight up (tangent, counter-clockwise)
arrow((mx, my - mr - 12), (mx, my - mr - 150))
# the pull of the near bulge on the Moon: from the Moon toward the bulge tip, which sits above the line
tipx, tipy = rot(a, 0, -tilt)
arrow((mx - mr - 8, my - 30), (cx + tipx + 24, cy + tipy - 4), col=(190, 90, 40), w=6, head=24)
im = im.resize((W, H), Image.LANCZOS)
im.save(sys.argv[1] if len(sys.argv) > 1 else "tide.png")
print("tip", cx + tipx, cy + tipy)
