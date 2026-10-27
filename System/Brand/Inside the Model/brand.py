#!/usr/bin/env python3
"""Inside the Model: avatar (800x800) and banner (2560x1440), drawn in the house look (ink ground, ember hero).
Mark: a cut-away core. Nested rings are the model's layers; a quarter is cut out so you see the ember core inside.
    python3 "System/Brand/Inside the Model/brand.py"      (writes itm-avatar.png, itm-avatar-small.png, itm-banner.png here)"""
import math, os, random, sys
import cairo
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "scripts"))
from motion import rgb, draw_text

OUT = os.path.dirname(os.path.abspath(__file__))
CUT = (-math.pi / 2, 0)                                        # the cut-away quarter: top right


def ground(w, h):
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
    c = cairo.Context(s)
    lin = cairo.LinearGradient(0, 0, 0, h)
    lin.add_color_stop_rgba(0, *rgb("ink2"))
    lin.add_color_stop_rgba(1, *rgb("ink"))
    c.set_source(lin)
    c.paint()
    for cx, cy, r, col, a in ((w * 0.15, h * 0.85, max(w, h) * 0.5, "ember", 0.10), (w * 0.9, h * 0.12, max(w, h) * 0.45, "signal", 0.09)):
        rg = cairo.RadialGradient(cx, cy, 0, cx, cy, r)
        rg.add_color_stop_rgba(0, *rgb(col, a))
        rg.add_color_stop_rgba(1, *rgb(col, 0))
        c.set_source(rg)
        c.paint()
    rnd = random.Random(7)
    for _ in range(w * h // 40):
        v = rnd.random()
        c.set_source_rgba(v, v, v, 0.035)
        c.rectangle(rnd.random() * w, rnd.random() * h, 2, 2)
        c.fill()
    return s, c


def arc(c, x, y, r, a0, a1, col, lw, alpha=1.0):
    c.set_line_cap(cairo.LINE_CAP_ROUND)
    c.set_source_rgba(*rgb(col, alpha))
    c.set_line_width(lw)
    c.new_path()
    c.arc(x, y, r, a0, a1)
    c.stroke()


def mark(c, x, y, R):
    """Three layer rings with the top-right quarter cut away; an ember core with glow; input dots entering through the cut."""
    gap = 0.16                                                  # angular gap at the cut edges, so the cut reads at 48 px
    for i, (k, col) in enumerate(((1.0, "slate"), (0.74, "cream"), (0.48, "slate"))):
        arc(c, x, y, R * k, CUT[1] + gap, CUT[0] + 2 * math.pi - gap, col, R * 0.11)
        arc(c, x, y, R * k, CUT[0] + gap, CUT[1] - gap, col, R * 0.03, 0.35)   # the removed quarter, as a faint ghost
    for k_r, a in ((0.42, 0.10), (0.30, 0.20)):
        c.arc(x, y, R * k_r, 0, 2 * math.pi)
        c.set_source_rgba(*rgb("ember", a))
        c.fill()
    c.arc(x, y, R * 0.2, 0, 2 * math.pi)
    c.set_source_rgba(*rgb("ember"))
    c.fill()
    c.arc(x, y, R * 0.09, 0, 2 * math.pi)
    c.set_source_rgba(*rgb("ember2"))
    c.fill()
    for k in (0.87, 0.61):                                     # signal dots (inputs) travelling into the cut
        a = -math.pi / 4
        c.arc(x + R * k * math.cos(a), y + R * k * math.sin(a), R * 0.045, 0, 2 * math.pi)
        c.set_source_rgba(*rgb("signal2"))
        c.fill()


def avatar():
    s, c = ground(800, 800)
    mark(c, 400, 410, 270)                                     # YouTube crops to a circle: the mark stays inside r 340
    s.write_to_png(f"{OUT}/itm-avatar.png")
    small = cairo.ImageSurface(cairo.FORMAT_ARGB32, 98, 98)
    sc = cairo.Context(small)
    sc.scale(98 / 800, 98 / 800)
    sc.set_source_surface(s)
    sc.paint()
    small.write_to_png(f"{OUT}/itm-avatar-small.png")         # what the feed shows: check the mark still reads


def banner():
    w, h = 2560, 1440                                          # safe area for every device: 1546x423 centred (x 507-2053, y 508-931)
    s, c = ground(w, h)
    mx, my = 720, 720
    for k in range(2, 9):                                      # the same layers, continued faint across the TV-only area
        arc(c, mx, my, 180 * (1 + 0.5 * (k - 1)), CUT[1] + 0.05, CUT[0] + 2 * math.pi - 0.05, "slate", 3, 0.16 - k * 0.015)
    mark(c, mx, my, 180)
    draw_text(c, "Inside the Model", 965, 650, 128, rgb("cream"))
    draw_text(c, "How AI works  ·  Agents at work  ·  What's coming", 969, 770, 40, rgb("slate"), bold=False)
    draw_text(c, "NEW SHORTS MON TO FRI", 969, 855, 34, rgb("ember2"), spaced=True)
    s.write_to_png(f"{OUT}/itm-banner.png")


if __name__ == "__main__":
    avatar()
    banner()
    print("written:", ", ".join(f for f in sorted(os.listdir(OUT)) if f.endswith(".png")))
