#!/usr/bin/env python3
"""Inside the Model: avatar (800x800) and banner (2560x1440), drawn in the house look (ink ground, ember hero).
Mascot (27 Oct 2026, user: "Avatar is quite boring, no soul"): the model is a box; a curious ember creature, the thing
inside the model, lifts the lid and peeks out at you, with two tokens floating up out of the box.
    python3 "System/Brand/Inside the Model/brand.py"      (writes itm-avatar.png, itm-avatar-small.png, itm-banner.png here)"""
import math, os, random, sys
import cairo
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "scripts"))
from motion import rgb, draw_text

OUT = os.path.dirname(os.path.abspath(__file__))


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


def poly(c, pts, col, a=1.0):
    c.new_path()
    c.move_to(*pts[0])
    for p in pts[1:]:
        c.line_to(*p)
    c.close_path()
    c.set_source_rgba(*rgb(col, a))
    c.fill()


def peek(c, cx, cy, s, look=(0.12, 0.08)):
    """The mascot: the model as a box, lid lifted, and a curious ember creature peeking out at you from inside.
    (cx, cy) is the box's front-top corner; s the edge length; look the pupils' direction."""
    k = math.cos(math.pi / 6) * s
    F1, L1, R1, K1 = (cx, cy), (cx - k, cy - s / 2), (cx + k, cy - s / 2), (cx, cy - s)
    F0, L0, R0 = (cx, cy + s), (cx - k, cy + s / 2), (cx + k, cy + s / 2)
    up = s * 0.62                                              # the lid hinges on the back-left edge and stands open behind
    Lt, Kt = (L1[0] - s * 0.16, L1[1] - up), (K1[0] - s * 0.16, K1[1] - up)
    ox, oy = cx, cy - s / 2                                    # centre of the opening
    rg = cairo.RadialGradient(ox, oy, 0, ox, oy, s * 1.6)      # the light spilling out, behind everything
    rg.add_color_stop_rgba(0, *rgb("ember", 0.40))
    rg.add_color_stop_rgba(1, *rgb("ember", 0))
    c.set_source(rg)
    c.paint()
    poly(c, (L1, K1, Kt, Lt), "slate")                         # the open lid; its inner face catches the glow
    lg = cairo.LinearGradient(0, L1[1], 0, Lt[1])
    lg.add_color_stop_rgba(0, *rgb("ember2", 0.55))
    lg.add_color_stop_rgba(1, *rgb("ember2", 0))
    c.move_to(*L1); c.line_to(*K1); c.line_to(*Kt); c.line_to(*Lt); c.close_path()
    c.set_source(lg)
    c.fill()
    poly(c, (L1, F1, R1, K1), "ink")                           # the inside: dark, lit from deep below
    ig = cairo.RadialGradient(ox, oy + s * 0.15, 0, ox, oy, k)
    ig.add_color_stop_rgba(0, *rgb("ember2", 0.9))
    ig.add_color_stop_rgba(1, *rgb("ember", 0.15))
    c.move_to(*L1); c.line_to(*F1); c.line_to(*R1); c.line_to(*K1); c.close_path()
    c.set_source(ig)
    c.fill()
    hx, hy, hr = ox, oy - s * 0.12, s * 0.46                   # the creature: a soft ember head rising out, two big eyes
    c.save()
    c.translate(hx, hy)
    c.scale(1, 0.9)
    c.arc(0, 0, hr, 0, 2 * math.pi)
    c.restore()
    hg = cairo.RadialGradient(hx - hr * 0.35, hy - hr * 0.45, 0, hx, hy, hr * 1.1)
    hg.add_color_stop_rgba(0, *rgb("ember2"))
    hg.add_color_stop_rgba(0.75, *rgb("ember"))
    hg.add_color_stop_rgba(1, *rgb("#A8441A"))
    c.set_source(hg)
    c.fill()
    for ex in (-0.4, 0.4):
        x, y, r = hx + ex * hr, hy - hr * 0.15, hr * 0.29
        c.arc(x, y, r, 0, 2 * math.pi)
        c.set_source_rgba(*rgb("cream"))
        c.fill()
        px, py = x + look[0] * r * 0.9, y + look[1] * r * 0.9
        c.arc(px, py, r * 0.55, 0, 2 * math.pi)
        c.set_source_rgba(*rgb("ink"))
        c.fill()
        c.arc(px + r * 0.2, py - r * 0.22, r * 0.17, 0, 2 * math.pi)  # catch-light: what gives the eyes life
        c.set_source_rgba(1, 1, 1, 0.95)
        c.fill()
    for ex in (-1, 1):                                         # two small hands gripping the front rims
        t = 0.45
        hx2 = F1[0] + ex * k * t
        c.arc(hx2, F1[1] - s / 2 * t - s * 0.03, s * 0.075, 0, 2 * math.pi)
        c.set_source_rgba(*rgb("ember2"))
        c.fill()
    poly(c, (L0, F0, F1, L1), "haze")                          # the box walls, over the creature's body so it sits inside
    poly(c, (F0, R0, R1, F1), "ink2")
    for ex in (-1, 1):                                         # fingers over the rim
        hx2 = F1[0] + ex * k * 0.45
        for f in (-1, 0, 1):
            c.arc(hx2 + f * s * 0.045, F1[1] - s / 2 * 0.45 + s * 0.04 - ex * f * s * 0.026, s * 0.03, 0, 2 * math.pi)
            c.set_source_rgba(*rgb("ember2"))
            c.fill()
    c.set_line_cap(cairo.LINE_CAP_ROUND)
    for a, b in ((L1, F1), (F1, R1)):                          # rim light where the glow touches
        c.set_source_rgba(*rgb("ember2", 0.9))
        c.set_line_width(s * 0.025)
        c.move_to(*a); c.line_to(*b); c.stroke()
    for a, b in ((L1, L0), (L0, F0), (F0, R0), (R0, R1), (F1, F0)):
        c.set_source_rgba(*rgb("slate", 0.5))
        c.set_line_width(s * 0.015)
        c.move_to(*a); c.line_to(*b); c.stroke()
    # two tokens floating up out of the gap
    for dx, dy, r in ((0.62, -1.25, 0.06), (0.85, -1.0, 0.045)):
        c.rectangle(cx + dx * s - r * s, cy + dy * s - r * s, 2 * r * s, 2 * r * s)
        c.set_source_rgba(*rgb("signal2"))
        c.fill()


def avatar():
    s, c = ground(800, 800)
    peek(c, 400, 470, 220)                                     # YouTube crops to a circle: the mascot stays inside r 340
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
    peek(c, 720, 760, 150)
    draw_text(c, "Inside the Model", 965, 650, 128, rgb("cream"))
    draw_text(c, "How AI works  ·  Agents at work  ·  What's coming", 969, 770, 40, rgb("slate"), bold=False)
    draw_text(c, "NEW SHORTS MON TO FRI", 969, 855, 34, rgb("ember2"), spaced=True)
    s.write_to_png(f"{OUT}/itm-banner.png")


if __name__ == "__main__":
    avatar()
    banner()
    print("written:", ", ".join(f for f in sorted(os.listdir(OUT)) if f.endswith(".png")))
