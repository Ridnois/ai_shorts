"""Motion plates: animated, faithful explainers (mechanisms, charts, counters, maps) drawn with cairo and encoded as
1080x1920 H.264 clips that build_video.py places like footage (System/Playbook.md §3, System/Style.md Motion plates).

    VIDEO="Media/<folder>" SOLO_PROYECTO=1 blender -b --factory-startup --python System/scripts/build_video.py   # writes render/_timeline.json
    python3 System/scripts/motion.py "Media/<folder>"                  # renders every `motion` plate of plan.json to its `file`
    python3 System/scripts/motion.py "Media/<folder>" --only m-curve   # plates whose file contains this text
    python3 System/scripts/motion.py "Media/<folder>" --sheet          # also writes <file>.sheet.png (6 frames) to look at

A motion plate in plan.json:  {"type": "motion", "file": "motion/pc-m-curve.mp4", "motion": {"bg": "navy", "els": [...]}}
Each clip lasts exactly as long as its plate (from render/_timeline.json). Every time in a spec is a **cue**: seconds from
the plate start (1.2), a word heard inside the plate ("fade", "fade#2" for its second time, "fade+0.3"), or "end" / "end-0.5".

Elements (coordinates in pixels of the 1080x1920 frame; colours are palette names or hex):
  common   show [in, out] · fade 0.25 · rise px · opacity · keys {"prop": [[cue, value], ...]} (eased; "prop~" = linear)
           · pulse [cue, ...] (a short swell that marks the thing the voice names)
  rect     x y w h r fill stroke lw                     circle  x y r fill stroke lw
  line     pts [[x,y],...] stroke lw dash arrow ("end"|"start"|"both") draw (0..1, keyable: draws on along the path)
  text     x y text size bold align ("left"|"center"|"right") color spaced chip ("paper": a label box behind it)
           value + fmt ("{:.0f} %"): a counting number, keyable through keys {"value": ...}
  label    target [x,y] at [x,y] text: a callout (copper dot, leader, paper box), like the builder's callouts
  image    file x y w (centre; height from the photo) r (corners) — a real photo inside the drawing
  stream   from [x,y] or [[x,y],...] · to [[x,y],...] (one slot per particle) or grid [x0,y0,dx,dy,cols,rows] · via [x,y]
           start every travel r color stop: particles leave `from` one by one and settle in their slots (ions, molecules,
           parcels); vanish: true makes them disappear on arrival (a flow, a current); glow: a soft halo; x y: pulse centre
  bar      x y w h segs [{"v", "color", "label", "show"}] total: a stacked bar whose segments grow when shown
  dots     x y cols rows gap r color n (keyable: dots shown) hi hi_color: a unit chart (1 dot = 1 unit)
  chart    x y w h xr [x0,x1] yr [y0,y1] series [{"pts", "color", "lw", "smooth", "label", "label_at", "label_show",
           "draw" (fraction of length) or "to_x" (data x; keyable, so stages line up)}] bands [{"x0","x1","label","show"}]
           marks [{"x", "label", "show"}] x_label y_label head readout {"series", "fmt", "scale"}
  map      cx cy (screen centre) center [lon,lat] R (globe radius px; keyable: 380 = whole globe, 6000+ = a region)
           highlight [country names] pins [{"lon","lat","label","show"}] arcs [{"from","to","show"}] states (US states etc.)
  camera   (top level, not an element) keys {"zoom": [[cue, 1], ...], "center": [[cue, [x, y]], ...]}: zooms into a detail

The renderer warns when text enters the caption band (y 880 to 1040), the bottom interface zone (y > 1440) or the right
action strip (x > 950), or is smaller than 40 px: fix those before building. Map data: Natural Earth (public domain),
downloaded once into Media/_canal/geo/.
"""
import argparse, io, json, math, os, subprocess, sys, urllib.request

import cairo

W, H, FPS = 1080, 1920, 24
PAL = {"navy": "#101824", "navy2": "#1A2638", "paper": "#F9F6EE", "ink": "#1C1A17", "copper": "#C76B38",
       "copper2": "#E8A06F", "grey": "#8C96A5", "dim": "#3A4658", "white": "#FFFFFF", "cool": "#7FB3D5",
       "land": "#2B3A50", "ocean": "#132033", "border": "#53647C"}
CAP_BAND, UI_BOTTOM, UI_RIGHT, MIN_TEXT = (880, 1040), 1440, 950, 40
F_BOLD, F_REG = "Noto Sans Display", "Noto Sans"
GEO = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "Media", "_canal", "geo")
NE = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/"


def rgb(c, a=1.0):
    h = PAL.get(c, c).lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)) + (a,)


def ease(u):
    u = min(max(u, 0.0), 1.0)
    return 4 * u ** 3 if u < 0.5 else 1 - (-2 * u + 2) ** 3 / 2


def lerp(a, b, u):
    if isinstance(a, (list, tuple)):
        return [lerp(x, y, u) for x, y in zip(a, b)]
    return a + (b - a) * u


# ---------------------------------------------------------------- cues
class Cues:
    """Resolves cue values to seconds from the clip start (the strip's first frame)."""

    def __init__(self, words, ini, fin, label):
        self.words, self.ini, self.dur, self.label = words, ini, fin - ini, label

    def __call__(self, c):
        if c is None:
            return None
        if isinstance(c, (int, float)):
            return float(c)
        s, off = str(c).strip(), 0.0
        for sign in "+-":
            if sign in s[1:]:
                k = s.rfind(sign)
                s, off = s[:k], float(s[k:])
                break
        if s == "end":
            return self.dur + off
        word, nth = (s.split("#") + ["1"])[:2]
        norm = lambda w: "".join(ch for ch in w.lower() if ch.isalnum())
        hits = [w for w in self.words if norm(w[0]) == norm(word) and self.ini - 0.1 <= w[1] < self.ini + self.dur]
        if len(hits) < int(nth):
            heard = " ".join(w[0] for w in self.words if self.ini - 0.1 <= w[1] < self.ini + self.dur)
            raise SystemExit(f"{self.label}: cue '{c}' not heard inside the plate (heard: {heard})")
        return max(0.0, hits[int(nth) - 1][1] - self.ini) + off


def keyed(el, prop, t, cues, default=None):
    """Value of `prop` at time t: from keys (eased, or linear with "prop~"), else the element's own value."""
    for name, f in ((prop, ease), (prop + "~", lambda u: min(max(u, 0.0), 1.0))):
        ks = el.get("keys", {}).get(name)
        if ks:
            pts = sorted(((cues(k[0]), k[1]) for k in ks), key=lambda p: p[0])
            if t <= pts[0][0]:
                return pts[0][1]
            for (t0, v0), (t1, v1) in zip(pts, pts[1:]):
                if t <= t1:
                    return lerp(v0, v1, f((t - t0) / max(t1 - t0, 1e-6)))
            return pts[-1][1]
    return el.get(prop, default)


def visibility(el, t, cues):
    """(alpha, entry progress) of an element at time t."""
    show = el.get("show", [0, "end"])
    t_in, t_out = cues(show[0]), cues(show[1]) if len(show) > 1 else cues("end")
    fd = el.get("fade", 0.25)
    if t < t_in or t > t_out:
        return 0.0, 0.0
    p_in = 1.0 if t_in <= 0.01 else ease((t - t_in) / max(fd, 1e-6))
    p_out = 1.0 if t_out >= cues("end") - 0.01 else ease((t_out - t) / max(fd, 1e-6))
    return min(p_in, p_out) * keyed(el, "opacity", t, cues, 1.0), p_in


# ---------------------------------------------------------------- drawing helpers
def set_font(ctx, size, bold=True):
    ctx.select_font_face(F_BOLD if bold else F_REG, cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD if bold else cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(size)


def text_width(ctx, s, spaced=False):
    if spaced:
        return sum(ctx.text_extents(ch).x_advance + ctx.get_font_matrix().xx * 0.18 for ch in s)
    return ctx.text_extents(s).x_advance


def draw_text(ctx, s, x, y, size, color, bold=True, align="left", spaced=False):
    """y is the vertical centre of the text line. Returns the box (x0, y0, w, h)."""
    set_font(ctx, size, bold)
    if spaced:
        s = s.upper()
    w = text_width(ctx, s, spaced)
    x0 = x - w / 2 if align == "center" else x - w if align == "right" else x
    ctx.set_source_rgba(*color)
    base = y + size * 0.35
    if spaced:
        cx = x0
        for ch in s:
            ctx.move_to(cx, base)
            ctx.show_text(ch)
            cx += ctx.text_extents(ch).x_advance + size * 0.18
    else:
        ctx.move_to(x0, base)
        ctx.show_text(s)
    return (x0, y - size * 0.6, w, size * 1.2)


def rounded(ctx, x, y, w, h, r):
    r = max(0.0, min(r, w / 2, h / 2))
    ctx.new_sub_path()
    ctx.arc(x + w - r, y + r, r, -math.pi / 2, 0)
    ctx.arc(x + w - r, y + h - r, r, 0, math.pi / 2)
    ctx.arc(x + r, y + h - r, r, math.pi / 2, math.pi)
    ctx.arc(x + r, y + r, r, math.pi, 3 * math.pi / 2)
    ctx.close_path()


def chip(ctx, x, y, s, size=40, bold=True, align="left"):
    """A paper label box with a copper bar (the callout style), text centred vertically on y."""
    set_font(ctx, size, bold)
    w = text_width(ctx, s) + 52
    h = size * 1.6
    x0 = x - w / 2 if align == "center" else x - w if align == "right" else x
    ctx.set_source_rgba(0, 0, 0, 0.35)
    rounded(ctx, x0 + 4, y - h / 2 + 8, w, h, 12)
    ctx.fill()
    ctx.set_source_rgba(*rgb("paper", 0.96))
    rounded(ctx, x0, y - h / 2, w, h, 12)
    ctx.fill()
    ctx.set_source_rgba(*rgb("copper"))
    rounded(ctx, x0, y - h / 2, 9, h, 4)
    ctx.fill()
    draw_text(ctx, s, x0 + 30, y, size, rgb("ink"), bold)
    return (x0, y - h / 2, w, h)


def polyline_part(pts, frac):
    """The first `frac` (0..1) of a polyline, by length."""
    if frac >= 1 or len(pts) < 2:
        return pts
    segs = [math.dist(a, b) for a, b in zip(pts, pts[1:])]
    goal, out = sum(segs) * max(frac, 0.0), [pts[0]]
    for (a, b), L in zip(zip(pts, pts[1:]), segs):
        if goal <= L:
            u = goal / L if L else 0
            out.append([a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u])
            return out
        out.append(b)
        goal -= L
    return out


def smooth(pts, n=12):
    """Catmull-Rom through the points (for curves drawn from a few data points)."""
    if len(pts) < 3:
        return pts
    P = [pts[0]] + pts + [pts[-1]]
    out = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for k in range(n):
            t = k / n
            out.append([0.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                               + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t ** 3) for j in (0, 1)])
    out.append(pts[-1])
    return out


def arrow_head(ctx, a, b, size):
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    ctx.move_to(*b)
    ctx.line_to(b[0] - size * math.cos(ang - 0.45), b[1] - size * math.sin(ang - 0.45))
    ctx.line_to(b[0] - size * math.cos(ang + 0.45), b[1] - size * math.sin(ang + 0.45))
    ctx.close_path()
    ctx.fill()


_img_cache = {}


def photo_surface(path, w, h=None):
    """A photo (any format PIL reads) as a cairo surface w px wide (height kept, or cropped to h)."""
    key = (path, round(w), round(h or 0))
    if key not in _img_cache:
        from PIL import Image
        im = Image.open(path).convert("RGBA")
        hh = round(im.height * w / im.width)
        im = im.resize((round(w), hh), Image.LANCZOS)
        if h and hh > h:
            top = (hh - round(h)) // 2
            im = im.crop((0, top, round(w), top + round(h)))
        buf = io.BytesIO()
        im.save(buf, "PNG")
        buf.seek(0)
        _img_cache[key] = cairo.ImageSurface.create_from_png(buf)
    return _img_cache[key]


# ---------------------------------------------------------------- map data (Natural Earth, public domain)
_geo = {}


def geo(name):
    if name not in _geo:
        os.makedirs(GEO, exist_ok=True)
        path = os.path.join(GEO, name + ".geojson")
        if not os.path.exists(path):
            print("downloading", name, "(Natural Earth, public domain)")
            req = urllib.request.Request(NE + name + ".geojson", headers={"User-Agent": "youtube-vault/1.0"})
            open(path, "wb").write(urllib.request.urlopen(req, timeout=120).read())
        polys = []
        for f in json.load(open(path, encoding="utf-8"))["features"]:
            nm = f["properties"].get("NAME") or f["properties"].get("name") or ""
            g = f["geometry"]
            rings = [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"] if g["type"] == "MultiPolygon" else []
            for poly in rings:
                ring = poly[0]
                lon_c = sum(p[0] for p in ring) / len(ring)
                lat_c = sum(p[1] for p in ring) / len(ring)
                rad = max(math.dist((lon_c, lat_c), p) for p in ring)
                polys.append((nm, [(math.radians(p[0]), math.radians(p[1])) for p in ring],
                              (math.radians(lon_c), math.radians(lat_c)), math.radians(min(rad, 180))))
        _geo[name] = polys
    return _geo[name]


def ortho(lon, lat, lon0, lat0):
    x = math.cos(lat) * math.sin(lon - lon0)
    y = math.cos(lat0) * math.sin(lat) - math.sin(lat0) * math.cos(lat) * math.cos(lon - lon0)
    c = math.sin(lat0) * math.sin(lat) + math.cos(lat0) * math.cos(lat) * math.cos(lon - lon0)
    return x, y, c


# ---------------------------------------------------------------- elements
def el_center(el):
    k = el["kind"]
    if k in ("rect", "bar"):
        return el["x"] + el.get("w", 0) / 2, el["y"] + el.get("h", 0) / 2
    if k == "label":
        return tuple(el["target"])
    if k == "line":
        return tuple(el["pts"][-1])
    return el.get("x", W / 2), el.get("y", H / 2)


def draw_el(ctx, el, t, cues, warn):
    k = el["kind"]
    g = lambda p, d=None: keyed(el, p, t, cues, d)
    if k == "rect":
        x, y, w, h = g("x"), g("y"), g("w"), g("h")
        rounded(ctx, x, y, max(w, 0), max(h, 0), g("r", 0))
        if el.get("fill"):
            ctx.set_source_rgba(*rgb(el["fill"]))
            ctx.fill_preserve()
        if el.get("stroke"):
            ctx.set_source_rgba(*rgb(el["stroke"]))
            ctx.set_line_width(g("lw", 4))
            ctx.stroke_preserve()
        ctx.new_path()
    elif k == "circle":
        ctx.arc(g("x"), g("y"), max(g("r", 10), 0), 0, 2 * math.pi)
        if el.get("fill", "copper"):
            ctx.set_source_rgba(*rgb(el.get("fill", "copper")))
            ctx.fill_preserve()
        if el.get("stroke"):
            ctx.set_source_rgba(*rgb(el["stroke"]))
            ctx.set_line_width(g("lw", 4))
            ctx.stroke_preserve()
        ctx.new_path()
    elif k == "line":
        pts = el["pts"] if not el.get("smooth") else smooth(el["pts"])
        part = polyline_part(pts, g("draw", 1.0))
        if len(part) < 2:
            return
        ctx.set_source_rgba(*rgb(el.get("stroke", "paper")))
        ctx.set_line_width(g("lw", 6))
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.set_line_join(cairo.LINE_JOIN_ROUND)
        if el.get("dash"):
            ctx.set_dash(el["dash"])
        ctx.move_to(*part[0])
        for p in part[1:]:
            ctx.line_to(*p)
        ctx.stroke()
        ctx.set_dash([])
        hs = g("lw", 6) * 3.2
        if el.get("arrow") in ("end", "both") and math.dist(part[-2], part[-1]) > 0.5:
            arrow_head(ctx, part[-2], part[-1], hs)
        if el.get("arrow") in ("start", "both"):
            arrow_head(ctx, pts[1], pts[0], hs)
    elif k == "text":
        s = el.get("fmt", "{}").format(g("value")) if "value" in el or "value" in el.get("keys", {}) else el["text"]
        size = g("size", 56)
        if el.get("chip"):
            box = chip(ctx, g("x"), g("y"), s, size, el.get("bold", True), el.get("align", "left"))
        else:
            box = draw_text(ctx, s, g("x"), g("y"), size, rgb(el.get("color", "paper")), el.get("bold", True),
                            el.get("align", "left"), el.get("spaced", False))
        warn(box, size, s)
    elif k == "label":
        tx, ty = g("target")
        lx, ly = g("at")
        set_font(ctx, el.get("size", 40))
        bw = text_width(ctx, el["text"]) + 52
        ex = min(max(tx, lx), lx + bw)
        ctx.set_source_rgba(*rgb("copper"))
        ctx.set_line_width(3)
        ctx.move_to(tx, ty)
        ctx.line_to(ex, ly)
        ctx.stroke()
        ctx.arc(tx, ty, 12, 0, 2 * math.pi)
        ctx.fill()
        ctx.set_line_width(2)
        ctx.arc(tx, ty, 20, 0, 2 * math.pi)
        ctx.stroke()
        warn(chip(ctx, lx, ly, el["text"], el.get("size", 40)), el.get("size", 40), el["text"])
    elif k == "image":
        w = g("w", 600)
        sf = photo_surface(el["file"], w, el.get("h"))
        x0, y0 = g("x") - sf.get_width() / 2, g("y") - sf.get_height() / 2
        ctx.save()
        rounded(ctx, x0, y0, sf.get_width(), sf.get_height(), el.get("r", 20))
        ctx.clip()
        ctx.set_source_surface(sf, x0, y0)
        ctx.paint()
        ctx.restore()
        if el.get("stroke"):
            rounded(ctx, x0, y0, sf.get_width(), sf.get_height(), el.get("r", 20))
            ctx.set_source_rgba(*rgb(el["stroke"]))
            ctx.set_line_width(3)
            ctx.stroke()
    elif k == "stream":
        srcs = el["from"] if isinstance(el["from"][0], (list, tuple)) else [el["from"]]
        if "grid" in el:
            x0, y0, dx, dy, cols, rows = el["grid"]
            slots = [[x0 + c * dx, y0 + r_ * dy] for r_ in range(rows) for c in range(cols)]
        else:
            slots = el["to"]
        t0, every, travel = cues(el.get("start", 0)), el.get("every", 0.12), el.get("travel", 0.7)
        stop = cues(el["stop"]) if "stop" in el else None
        ctx.set_source_rgba(*rgb(el.get("color", "copper")))
        for i, dst in enumerate(slots[: el.get("count", len(slots))]):
            born = t0 + i * every
            if t < born or (stop is not None and born > stop) or (el.get("vanish") and t > born + travel):
                continue
            u = ease((t - born) / travel)
            a = srcs[i % len(srcs)]
            if "via" in el:
                v = el["via"]
                p = [(1 - u) ** 2 * a[j] + 2 * (1 - u) * u * v[j] + u * u * dst[j] for j in (0, 1)]
            else:
                p = lerp(a, dst, u)
            if el.get("glow"):                                      # a soft halo: energy, current, heat
                ctx.set_source_rgba(*rgb(el.get("color", "copper"), 0.22))
                ctx.arc(p[0], p[1], el.get("r", 12) * 2.3, 0, 2 * math.pi)
                ctx.fill()
                ctx.set_source_rgba(*rgb(el.get("color", "copper")))
            ctx.arc(p[0], p[1], el.get("r", 12), 0, 2 * math.pi)
            ctx.fill()
    elif k == "bar":
        x, y, w, h = el["x"], el["y"], el["w"], el["h"]
        total = el.get("total") or sum(s["v"] for s in el["segs"])
        rounded(ctx, x, y, w, h, 14)
        ctx.set_source_rgba(*rgb("dim", 0.6))
        ctx.fill()
        cx = x
        for s in el["segs"]:
            sh = s.get("show", [0])
            t_in = cues(sh[0])
            if t < t_in:
                break
            u = ease((t - t_in) / s.get("grow", 0.8))
            sw = w * s["v"] / total * u
            ctx.save()
            rounded(ctx, x, y, w, h, 14)
            ctx.clip()
            ctx.rectangle(cx, y, sw, h)
            ctx.set_source_rgba(*rgb(s.get("color", "copper")))
            ctx.fill()
            ctx.restore()
            if s.get("label") and u > 0.6:
                ctx.push_group()
                lab_y = y + h + 44 if s.get("below", True) else y - 44
                box = draw_text(ctx, s["label"], cx, lab_y, s.get("size", 40), rgb(s.get("label_color", "paper")), True)
                ctx.pop_group_to_source()
                ctx.paint_with_alpha((u - 0.6) / 0.4)
                warn(box, s.get("size", 40), s["label"])
            cx += sw
    elif k == "dots":
        n_show = round(g("n", el["cols"] * el["rows"]))
        hi = el.get("hi", 0)
        for i in range(el["cols"] * el["rows"]):
            if i >= n_show:
                break
            r_, c_ = divmod(i, el["cols"])
            ctx.arc(el["x"] + c_ * el["gap"], el["y"] + r_ * el["gap"], el.get("r", 6), 0, 2 * math.pi)
            ctx.set_source_rgba(*rgb(el.get("hi_color", "copper") if i < hi else el.get("color", "dim")))
            ctx.fill()
    elif k == "chart":
        draw_chart(ctx, el, t, cues, warn)
    elif k == "map":
        draw_map(ctx, el, t, cues, warn)
    else:
        raise SystemExit(f"unknown element kind: {k}")


def draw_chart(ctx, el, t, cues, warn):
    x, y, w, h = el["x"], el["y"], el["w"], el["h"]
    (x0, x1), (y0, y1) = el.get("xr", [0, 1]), el.get("yr", [0, 1])
    px = lambda p: [x + (p[0] - x0) / (x1 - x0) * w, y + h - (p[1] - y0) / (y1 - y0) * h]
    for b in el.get("bands", []):                                  # shaded stages behind the curves
        a, _ = visibility(b, t, cues)
        if a <= 0:
            continue
        bx0, bx1 = px([b["x0"], y0])[0], px([b["x1"], y0])[0]
        ctx.set_source_rgba(*rgb(b.get("color", "navy2"), 0.85 * a))
        ctx.rectangle(bx0, y, bx1 - bx0, h)
        ctx.fill()
        if b.get("label"):
            ctx.push_group()
            warn(draw_text(ctx, b["label"], (bx0 + bx1) / 2, y + 44, b.get("size", 42), rgb(b.get("label_color", "grey")),
                           True, "center"), b.get("size", 42), b["label"])
            ctx.pop_group_to_source()
            ctx.paint_with_alpha(a)
    ctx.set_source_rgba(*rgb("grey"))
    ctx.set_line_width(4)
    ctx.move_to(x, y)
    ctx.line_to(x, y + h)
    ctx.line_to(x + w, y + h)
    ctx.stroke()
    if el.get("x_label"):
        warn(draw_text(ctx, el["x_label"], x + w, y + h + 50, 40, rgb("grey"), False, "right"), 40, el["x_label"])
    if el.get("y_label"):
        warn(draw_text(ctx, el["y_label"], x + 16, y - 40, 40, rgb("grey"), False), 40, el["y_label"])
    for m in el.get("marks", []):
        a, _ = visibility(m, t, cues)
        if a <= 0:
            continue
        mx = px([m["x"], y0])[0]
        ctx.set_source_rgba(*rgb("paper", 0.7 * a))
        ctx.set_line_width(3)
        ctx.set_dash([14, 12])
        ctx.move_to(mx, y)
        ctx.line_to(mx, y + h)
        ctx.stroke()
        ctx.set_dash([])
    heads = []
    for s in el["series"]:
        a, _ = visibility(s, t, cues)
        if a <= 0:
            continue
        pts = [px(p) for p in s["pts"]]
        pts = smooth(pts) if s.get("smooth") else pts
        if "to_x" in s or "to_x" in s.get("keys", {}):              # drawn up to a data x (stages line up across series)
            xe = px([keyed(s, "to_x", t, cues, x1), y0])[0]
            part = [p for p in pts if p[0] <= xe]
            nxt = next((p for p in pts if p[0] > xe), None)
            if part and nxt:
                a_, b_ = part[-1], nxt
                u = (xe - a_[0]) / max(b_[0] - a_[0], 1e-6)
                part.append([xe, a_[1] + (b_[1] - a_[1]) * u])
            if len(part) < 2:
                continue
        else:
            part = polyline_part(pts, keyed(s, "draw", t, cues, 1.0))
        ctx.set_source_rgba(*rgb(s.get("color", "copper"), a))
        ctx.set_line_width(s.get("lw", 10))
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.set_line_join(cairo.LINE_JOIN_ROUND)
        ctx.move_to(*part[0])
        for p in part[1:]:
            ctx.line_to(*p)
        ctx.stroke()
        if el.get("head", True) and len(part) > 1:
            ctx.arc(part[-1][0], part[-1][1], s.get("lw", 10) * 1.5, 0, 2 * math.pi)
            ctx.fill()
        heads.append((s, part[-1], a))
        if s.get("label") and len(part) > 1 and t >= cues(s.get("label_show", 0)):
            lx, ly = s.get("label_at", [part[-1][0] + 20, part[-1][1] - 50])
            ctx.push_group()
            warn(draw_text(ctx, s["label"], lx, ly, s.get("size", 44), rgb(s.get("color", "copper")), True,
                           s.get("label_align", "left")), s.get("size", 44), s["label"])
            ctx.pop_group_to_source()
            ctx.paint_with_alpha(a)
    ro = el.get("readout")
    if ro and heads:
        s, (hx, hy), a = heads[min(ro.get("series", 0), len(heads) - 1)]
        val = y0 + (y + h - hy) / h * (y1 - y0)
        txt = ro.get("fmt", "{:.0f}").format(val * ro.get("scale", 1))
        warn(draw_text(ctx, txt, hx + ro.get("dx", 0), hy + ro.get("dy", -70), ro.get("size", 56), rgb(ro.get("color", "paper"), a),
                       True, ro.get("align", "center")), ro.get("size", 56), txt)


def draw_map(ctx, el, t, cues, warn):
    g = lambda p, d=None: keyed(el, p, t, cues, d)
    cx, cy, R = g("cx", W / 2), g("cy", 560), g("R", 380)
    lon0, lat0 = (math.radians(v) for v in g("center", [0, 20]))
    hi = set(el.get("highlight", []))
    ctx.save()
    ctx.arc(cx, cy, R, 0, 2 * math.pi)
    ctx.set_source_rgba(*rgb("ocean"))
    ctx.fill_preserve()
    ctx.clip()
    view = math.hypot(W, H) / R                                   # angular radius of the screen, in radians
    layers = [("ne_110m_admin_0_countries" if R < 1500 else "ne_50m_admin_0_countries", True)]
    if el.get("states"):
        layers.append(("ne_50m_admin_1_states_provinces_lakes", False))
    for name, fill in layers:
        for nm, ring, (clon, clat), rad in geo(name):
            _, _, cc = ortho(clon, clat, lon0, lat0)
            ang = math.acos(max(-1.0, min(1.0, cc)))
            if ang - rad > min(math.pi / 2, view):
                continue
            first = True
            for lon, lat in ring:
                x, y, c = ortho(lon, lat, lon0, lat0)
                if c < 0:                                          # behind the globe: pinned to the rim
                    d = math.hypot(x, y) or 1.0
                    x, y = x / d, y / d
                X, Y = cx + R * x, cy - R * y
                ctx.move_to(X, Y) if first else ctx.line_to(X, Y)
                first = False
            ctx.close_path()
            if fill:
                ctx.set_source_rgba(*rgb("copper" if nm in hi else "land"))
                ctx.fill_preserve()
            ctx.set_source_rgba(*rgb("border", 1.0 if fill else 0.8))
            ctx.set_line_width(2 if fill else 1.5)
            ctx.stroke()
    ctx.restore()
    ctx.set_source_rgba(*rgb("grey", 0.5))
    ctx.set_line_width(2)
    ctx.arc(cx, cy, R, 0, 2 * math.pi)
    ctx.stroke()
    proj = lambda lon, lat: (lambda x, y, c: (cx + R * x, cy - R * y, c))(*ortho(math.radians(lon), math.radians(lat), lon0, lat0))
    for arc in el.get("arcs", []):
        a, _ = visibility(arc, t, cues)
        if a <= 0:
            continue
        (lo1, la1), (lo2, la2) = arc["from"], arc["to"]
        pts = []
        for i in range(41):                                        # straight interpolation in lon/lat, lifted in the middle
            u = i / 40
            X, Y, c = proj(lo1 + (lo2 - lo1) * u, la1 + (la2 - la1) * u)
            pts.append([X, Y - math.sin(math.pi * u) * arc.get("lift", 0.12) * R])
        part = polyline_part(pts, min(1.0, a * 1.0) if "draw" not in arc else keyed(arc, "draw", t, cues, 1.0))
        ctx.set_source_rgba(*rgb("copper2"))
        ctx.set_line_width(6)
        ctx.set_dash([18, 12])
        ctx.move_to(*part[0])
        for p in part[1:]:
            ctx.line_to(*p)
        ctx.stroke()
        ctx.set_dash([])
    for pin in el.get("pins", []):
        a, p_in = visibility(pin, t, cues)
        if a <= 0:
            continue
        X, Y, c = proj(pin["lon"], pin["lat"])
        if c < 0:
            continue
        ctx.push_group()
        rr = 16 * (0.6 + 0.4 * p_in)
        ctx.set_source_rgba(*rgb("copper"))
        ctx.arc(X, Y, rr, 0, 2 * math.pi)
        ctx.fill()
        ctx.set_line_width(3)
        ctx.arc(X, Y, rr + 12 + 10 * (1 - p_in), 0, 2 * math.pi)
        ctx.stroke()
        if pin.get("label"):
            lx, ly = X + pin.get("dx", 40), Y + pin.get("dy", -70)
            ctx.set_source_rgba(*rgb("copper"))
            ctx.set_line_width(3)
            ctx.move_to(X, Y)
            ctx.line_to(lx + 10, ly)
            ctx.stroke()
            box = chip(ctx, lx, ly, pin["label"], pin.get("size", 42), True, pin.get("align", "left"))
        ctx.pop_group_to_source()
        ctx.paint_with_alpha(a)
        if pin.get("label"):
            warn(box, pin.get("size", 42), pin["label"])


# ---------------------------------------------------------------- background and frame
def _photo(path, blur=0, dim=1.0):
    from PIL import Image, ImageFilter, ImageEnhance
    im = Image.open(path).convert("RGB")
    if max(im.size) > 2600:
        im.thumbnail((2600, 2600), Image.LANCZOS)
    if blur:
        im = im.filter(ImageFilter.GaussianBlur(blur))
    if dim != 1.0:
        im = ImageEnhance.Brightness(im).enhance(dim)
    buf = io.BytesIO()
    im.convert("RGBA").save(buf, "PNG")
    buf.seek(0)
    return cairo.ImageSurface.create_from_png(buf)


def paint_cover(ctx, sf, fx, fy, z):
    """Paints a surface cover-fitted, with the focus point (fractions) as near the centre as the picture allows."""
    w, h = sf.get_width(), sf.get_height()
    k = max(W / w, H / h) * z
    ox = max(W - w * k, min(0.0, W / 2 - fx * w * k))
    oy = max(H - h * k, min(0.0, H / 2 - fy * h * k))
    ctx.save()
    ctx.translate(ox, oy)
    ctx.scale(k, k)
    ctx.set_source_surface(sf, 0, 0)
    ctx.get_source().set_filter(cairo.FILTER_GOOD)
    ctx.paint()
    ctx.restore()


class Background:
    """navy (gradient and faint drafting grid), {"photo": file, "blur", "dim", "move": {"from": [fx, fy, z], "to": [...]}}
    or {"video": clips/x.mp4, "in": s, "dim"}: real footage under the animation (labels and arrows drawn on the real thing)."""

    def __init__(self, spec, root, dur):
        self.spec, self.dur, self.ff, self.last = spec.get("bg", "navy"), dur, None, None
        bg = self.spec
        if isinstance(bg, dict) and bg.get("video"):
            src = os.path.join(root, bg["video"])
            self.ff = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-ss", str(bg.get("in", 0)), "-i", src, "-an", "-vf",
                                        f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}",
                                        "-f", "rawvideo", "-pix_fmt", "bgra", "-"], stdout=subprocess.PIPE)
        elif isinstance(bg, dict) and bg.get("photo"):
            self.photo = _photo(os.path.join(root, bg["photo"]), bg.get("blur", 0), bg.get("dim", 0.55))
        else:
            self.flat = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
            ctx = cairo.Context(self.flat)
            grad = cairo.LinearGradient(0, 0, 0, H)
            grad.add_color_stop_rgba(0, *rgb("navy"))
            grad.add_color_stop_rgba(1, *rgb("navy2"))
            ctx.set_source(grad)
            ctx.paint()
            if spec.get("grid", True):                             # faint drafting grid: designed, never empty
                ctx.set_source_rgba(1, 1, 1, 0.035)
                ctx.set_line_width(1.5)
                for gx in range(0, W + 1, 60):
                    ctx.move_to(gx, 0)
                    ctx.line_to(gx, H)
                for gy in range(0, H + 1, 60):
                    ctx.move_to(0, gy)
                    ctx.line_to(W, gy)
                ctx.stroke()
        self.vig = cairo.RadialGradient(W / 2, H * 0.45, H * 0.25, W / 2, H * 0.45, H * 0.75)
        self.vig.add_color_stop_rgba(0, 0, 0, 0, 0)
        self.vig.add_color_stop_rgba(1, 0, 0, 0, 0.45)

    def paint(self, ctx, t):
        bg = self.spec
        if self.ff:
            raw = self.ff.stdout.read(W * H * 4)
            if len(raw) == W * H * 4:
                self.last = cairo.ImageSurface.create_for_data(bytearray(raw), cairo.FORMAT_ARGB32, W, H, W * 4)
            if self.last:
                ctx.set_source_surface(self.last, 0, 0)
                ctx.paint()
            if bg.get("dim", 1.0) < 1.0:
                ctx.set_source_rgba(0, 0, 0, 1 - bg["dim"])
                ctx.paint()
        elif isinstance(bg, dict) and bg.get("photo"):
            mv = bg.get("move")
            u = ease(t / max(self.dur, 1e-6))
            fx, fy, z = [a + (b - a) * u for a, b in zip(mv["from"], mv["to"])] if mv else bg.get("focus", [0.5, 0.5]) + [1.02]
            paint_cover(ctx, self.photo, fx, fy, z)
        else:
            ctx.set_source_surface(self.flat, 0, 0)
            ctx.paint()
        ctx.set_source(self.vig)
        ctx.paint()

    def close(self):
        if self.ff:
            self.ff.stdout.close()
            self.ff.wait()


def events(spec, cues):
    """Times at which something on screen changes (entries, exits, key frames, pulses, particles, bar segments)."""
    ts = [0.0, cues("end")]

    def walk(el):
        if "show" in el:
            ts.extend(cues(c) for c in el["show"][:2])
        for ks in el.get("keys", {}).values():
            ts.extend(cues(k[0]) for k in ks)
        ts.extend(cues(c) for c in el.get("pulse", []))
        if el.get("kind") == "stream":
            ts.append(cues(el.get("start", 0)))
            if "stop" in el:
                ts.append(cues(el["stop"]))
        for sub in ("segs", "series", "bands", "marks", "pins", "arcs"):
            for x in el.get(sub, []):
                walk(x)
    for el in spec["els"]:
        walk(el)
    walk(spec.get("camera", {}))
    return sorted(t for t in ts if t is not None)


def render(spec, out, dur, cues, root, label, sheet=False, extra=()):
    els = spec["els"]
    for el in els:
        for key in ("file",):
            if el.get(key) and not os.path.isabs(el[key]):
                el[key] = os.path.join(root, el[key])
    bg = Background(spec, root, dur)
    ev = sorted(min(max(x, 0.0), dur) for x in events(spec, cues) + [cues(c) for c in extra])
    gaps = [(round(a_, 1), round(b_, 1)) for a_, b_ in zip(ev, ev[1:]) if b_ - a_ > 3.5]
    if gaps:
        print(f"  WARN {label}: nothing changes on screen for over 3.5 s in {gaps}: add an event (a label, a pulse, a camera move)")
    warned = set()

    def warn(box, size, s):
        x0, y0, w, h = box
        issues = []
        if y0 < CAP_BAND[1] and y0 + h > CAP_BAND[0]:
            issues.append("in the caption band")
        if y0 + h > UI_BOTTOM:
            issues.append("in the bottom interface zone")
        if x0 + w > UI_RIGHT:
            issues.append("under the right action strip")
        if size < MIN_TEXT:
            issues.append(f"{size} px is below {MIN_TEXT} px")
        for i in issues:
            if (s, i) not in warned:
                warned.add((s, i))
                print(f"  WARN {label}: '{s}' {i}")

    os.makedirs(os.path.dirname(out), exist_ok=True)
    n = max(1, round(dur * FPS))
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "bgra", "-s", f"{W}x{H}",
                           "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16",
                           "-preset", "medium", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
    cam = spec.get("camera", {})
    for f in range(n):
        t = f / FPS
        sf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
        ctx = cairo.Context(sf)
        bg.paint(ctx, t)
        z, (ccx, ccy) = keyed(cam, "zoom", t, cues, 1.0), keyed(cam, "center", t, cues, [W / 2, H / 2])
        ctx.translate(W / 2, H / 2)
        ctx.scale(z, z)
        ctx.translate(-ccx, -ccy)
        for el in els:
            a, p_in = visibility(el, t, cues)
            if a <= 0.001:
                continue
            ctx.save()
            rise = el.get("rise", 18 if el["kind"] in ("text", "label") else 0)
            ctx.translate(0, rise * (1 - p_in))
            for pc in el.get("pulse", []):
                u = (t - cues(pc)) / 0.6
                if 0 <= u <= 1:
                    px_, py_ = el_center(el)
                    s = 1 + 0.10 * math.sin(math.pi * u)
                    ctx.translate(px_, py_)
                    ctx.scale(s, s)
                    ctx.translate(-px_, -py_)
            ctx.push_group()
            draw_el(ctx, el, t, cues, warn)
            ctx.pop_group_to_source()
            ctx.paint_with_alpha(a)
            ctx.restore()
        ff.stdin.write(bytes(sf.get_data()))
    ff.stdin.close()
    ff.wait()
    bg.close()
    print(f"MOTION {os.path.relpath(out, root)}: {dur:.2f} s, {n} frames")
    if sheet:
        png = os.path.splitext(out)[0] + ".sheet.png"
        font = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", out, "-vf",
                        f"setpts=PTS-STARTPTS,fps={6 / max(dur, 0.1):.4f},scale=270:480,drawtext=fontfile={font}:text='%{{pts\\:flt\\:2}} s':"
                        "x=8:y=8:fontsize=20:fontcolor=white:box=1:boxcolor=black@0.6,tile=6x1", "-frames:v", "1", png])
        print("  sheet", os.path.relpath(png, root))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--only", default="")
    ap.add_argument("--sheet", action="store_true")
    a = ap.parse_args()
    root = os.path.abspath(a.video)
    plan = json.load(open(f"{root}/plan.json", encoding="utf-8"))
    tl_path = f"{root}/render/_timeline.json"
    if not os.path.exists(tl_path):
        raise SystemExit("render/_timeline.json missing: run build_video.py with SOLO_PROYECTO=1 first")
    tl = json.load(open(tl_path, encoding="utf-8"))
    slots = {p["file"]: p for p in tl["plates"]}
    done = 0
    for sc in plan["scenes"]:
        for pl in sc["plates"]:
            if pl["type"] != "motion" or a.only not in pl["file"]:
                continue
            p = slots.get(pl["file"])
            if not p:
                raise SystemExit(f"{pl['file']} is not in render/_timeline.json: rebuild with SOLO_PROYECTO=1")
            cues = Cues(tl["words"], p["ini"], p["fin"], pl["file"])
            extra = [c["at"] for c in [pl.get("card") if isinstance(pl.get("card"), dict) else {}] + pl.get("callouts", []) if c.get("at")]
            render(json.loads(json.dumps(pl["motion"])), os.path.join(root, pl["file"]), p["fin"] - p["ini"], cues, root,
                   pl["file"], a.sheet, extra)
            done += 1
    print("MOTION PLATES rendered:", done)


if __name__ == "__main__":
    main()
