#!/usr/bin/env python3
"""The Next Token design system as code: every HyperFrames builder imports it (System/Look.md).

    import sys; sys.path.insert(0, "<vault>/System/scripts"); import hfkit as K
    v = K.Short(__file__, keys={"RAG": K.BLUE})        # plan.json, the take, heard words, scene starts, captions
    W = {"w1": K.hairline("h-cards", 53, 230, 980) + K.card(...), ...}
    v.hairline("h-cards", "riffle"); v.pop("#h-cards", v.S[1]); v.focus("w1", v.cue(1, "card"), (300, 300, 400, 300))
    v.write(W, rev=1, trans={"w2": "whip", "w3": "push"})   # index.html, render/_fx/sound_sfx.wav, render/_timeline.json
    v.thumb(K.hairline(...) + K.big("t", "WRONG CARD", 120, 1100, 840))    # hf/thumb.html -> upload/thumb.jpg

Frame (1080x1920): STAGE x 56..950, y 180..860 holds pictures (to y 1150 when the DECK is empty; below y 310 while the
pipeline rail shows); DECK y 880..1150
holds one card or the comment prompt; captions own the BAND y 1180..1320; nothing below 1440 or right of 950.
Every world is a canvas behind a camera: cam()/focus() move it on a word (wide, medium, close). Worlds change by a
transition with a cause: cut (default; the new world lands slightly large and settles), whip, push, dip or blur.
Sound: sfx() places a kit file (System/assets/sfx) on the timeline; whips, pushes, callouts and chips sound by
themselves; payoff() lays a riser into the reveal word and a hit on it. GSAP, three.js and the fonts are vendored, so
a render needs no network. 3D from Blender: blender3d() renders a scene3d.py spec as glb (model3d) or webm (plate3d).
Self-check: python3 hfkit.py; a demo page: python3 hfkit.py --demo <dir>, then npx hyperframes snapshot <dir>/hf.
ponytail: one class, one file; split only when a second engine needs it.
"""
import difflib, html, json, math, os, re, shutil, subprocess, sys, wave
from array import array

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(os.path.dirname(HERE))
SFX_DIR = f"{VAULT}/System/assets/sfx"
ANATOMY = f"{VAULT}/System/anatomy"                       # Anatomy figures: <name>/<name>.svg .json .css .pose.js (built by the figure's build.mjs)
sys.path.insert(0, HERE)
from captions import html_caps, groups

# ---- tokens (System/Look.md): flat paper. Flat colour survives YouTube's re-encode; no gradients, no grain, no glow.
PAPER, PAPER2, INK, MUTED, WHITE = "#F4EFE4", "#E7E0D1", "#121212", "#6B665C", "#FFFFFF"
YELLOW, YELLOW2 = "#FFD23F", "#FFE68A"     # the hero: a fill or a marker under ink text, never a text colour
BLUE, BLUE2 = "#2C5BEA", "#D3DEFF"         # data and inputs (text-safe on paper)
RED, RED2 = "#D7392B", "#FFD6CF"           # wrong, the error
GREEN, GREEN2 = "#13965A", "#CDEFDB"       # right, the fix
# names used by builders written before 29 Oct 2026 (dark look), mapped to their meaning in the paper look
EMBER = EMBER2 = YELLOW; SIGNAL = SIGNAL2 = BLUE; MINT = MINT2 = GREEN; ROSE = ROSE2 = RED
CREAM, SLATE, HAZE, INK2 = INK, MUTED, PAPER2, WHITE
PAL = {"paper": PAPER, "paper2": PAPER2, "ink": INK, "muted": MUTED, "white": WHITE, "yellow": YELLOW, "yellow2": YELLOW2,
       "blue": BLUE, "blue2": BLUE2, "red": RED, "red2": RED2, "green": GREEN, "green2": GREEN2,
       "ember": YELLOW, "signal": BLUE, "mint": GREEN, "rose": RED, "cream": INK, "slate": MUTED, "haze": PAPER2, "ink2": WHITE}
TEXT_SAFE = {INK, MUTED, BLUE, RED, GREEN}     # colours text may take on paper; yellow only as a marker behind ink
T = {"xs": 44, "s": 60, "m": 84, "l": 128, "xl": 190}          # type scale (px); nothing read is under xs
LINE = 6                                                       # stroke of drawn lines: thick ink survives the encode

# ---- layout: zones and the column grid
FW, FH = 1080, 1920
X0, X1 = 56, 950                       # content edges (right strip x > 950 is the platform's)
STAGE = (X0, 180, X1, 860)             # pictures; the top 180 px is the Shorts title bar
FULL = (X0, 180, X1, 1150)             # the stage when nothing is in the deck
DECK = (X0, 880, X1, 1150)             # one card or the comment prompt
BAND = (1180, 1320)                    # captions only
UI_Y = 1440                            # bottom interface zone
FOCUS = (503, 520)                     # stage centre: where cam() puts the canvas point it looks at
ROW1, ROW2 = 220, 560                  # tops of the two picture rows on the stage
HERO = (73, 330, 933, 1150)            # one hero per beat: 860 px wide (80 % of the frame), centred between the rail and the captions
hero = lambda w, h: (round((HERO[0] + HERO[2] - w) / 2), round((HERO[1] + HERO[3] - h) / 2))   # top-left that centres a w x h hero
colx = lambda k, n: round(X0 + (X1 - X0) * (2 * k + 1) / (2 * n))
rowy = lambda k, n, top=STAGE[1], bottom=STAGE[3]: round(top + (bottom - top) * (2 * k + 1) / (2 * n))


# ---- components (HTML strings; ids drive the motion verbs)
def lbl(id_, text, x, y, w, col=INK):
    col = col if col in TEXT_SAFE else INK              # yellow is a marker, never a text colour
    return f'<div class="lbl ov" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px;color:{col}">{text}</div>'


def big(id_, text, x, y, w, size=T["l"], col=INK, hot=None, hot_col=YELLOW):
    """A display line (a claim, a number) in Inter Display Black; each word is a span id_-w<k> for Short.words().
    hot = index of the one word on the yellow marker (hot_col YELLOW) or, for a text-safe colour, in that colour."""
    if len(text) * size * 0.62 > w and size <= T["m"] and w < 1000:        # a one-line claim; thumbnail lines at 110 px or more wrap on purpose
        print(f"WARN big {id_}: '{text}' needs about {round(len(text) * size * 0.62)} px at {size} px type, the box is {w} px: it will wrap")
    def st(k):
        if k != hot:
            return f'style="color:{col}"'
        return (f'class="hot" style="color:{INK};background:{hot_col}"' if hot_col not in TEXT_SAFE else f'style="color:{hot_col}"')
    ws = "".join(f'<span id="{id_}-w{k}" {st(k)}>{html.escape(t)}</span> ' for k, t in enumerate(text.split()))
    return f'<div class="big ov" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px;font-size:{size}px">{ws.strip()}</div>'


def frame(id_, src, x, y, w, h=None, fit="cover"):
    """A real frame or screenshot (h defaults to 9:16); counts as a picture for the fill check."""
    return (f'<img class="frm art" id="{id_}" src="{src}" style="left:{x}px;top:{y}px;width:{w}px;'
            f'height:{h or round(w * 16 / 9)}px;object-fit:{fit}"/>')


def phone(id_, src, x=90, y=200, w=370, h=660):
    return f'<div class="phone ov box" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><img src="{src}"/></div>'


def code(id_, lines, x=70, y=200, w=870, title=None, size=40):
    """Mono panel; lines are (html, id) with <s>strings</s> in mint and <b>numbers</b> in ember. title = a terminal or
    file bar (real output is labelled as such in it)."""
    rows = "".join(f'<div class="cl" id="{id_}-{i or k}">{c}</div>' for k, (c, i) in enumerate(lines))
    bar = f'<div class="bar"><i></i><i></i><i></i><span>{html.escape(title)}</span></div>' if title else ""
    return (f'<div class="code ov box" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px;font-size:{size}px;'
            f'line-height:{round(size * 1.5)}px">{bar}{rows}</div>')


def counter(id_, prefix, n, x, y, w=420):
    return f'<div class="count ov" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px">{prefix} <b id="{id_}-n">{n}</b></div>'


def arrow(id_, text, x, y, w=290):
    """A labelled arrow: the step between two pictures."""
    return f'<div class="arr ov" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px">{text}</div>'


def strike(id_, x, y, w=200):
    return f'<div class="xx" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px"></div>'


def flash(id_, h=880):
    return f'<div class="flash" id="{id_}" style="height:{h}px"></div>'


def strip(id_, inner, x=70, y=520, w=870, h=310):
    return f'<div class="strip ov box" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><div class="track" id="{id_}-t">{inner}</div></div>'


def hairline(id_, x=53, y=200, w=900):
    """A Hairline isometric line figure (vendor/hairline, MIT): a host box at 5:4; Short.hairline() names the figure and
    Short.point() moves its unseen pointer on words. The drawing fills about 60 % of the box: 900 wide spans the stage."""
    return f'<div class="hl" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px;height:{round(w * 0.8)}px"></div>'


def anatomy(id_, name, x, y, w):
    """An Anatomy figure (System/anatomy/<name>, built with the anatomy skill, MIT): an inline isometric SVG of a real machine.
    Short.anatomy() registers it and Short.pose() moves its parts on words. The host is as tall as the drawing's own box."""
    meta = json.load(open(f"{ANATOMY}/{name}/{name}.json"))
    svg = open(f"{ANATOMY}/{name}/{name}.svg").read()
    # ids inside the drawing (clip paths) are scoped per mount: two mounts of one figure would share url(#id), and a
    # reference that resolves into a hidden world clips the part away
    for sid in set(re.findall(r'\bid="([^"]+)"', svg)):
        svg = svg.replace(f'id="{sid}"', f'id="{id_}-{sid}"').replace(f"url(#{sid})", f"url(#{id_}-{sid})")
    return (f'<div class="an iso art" id="{id_}" data-theme="dark" style="left:{x}px;top:{y}px;width:{w}px;height:{round(w * meta["height"] / meta["width"])}px">'
            f'{svg}</div>')


def anp(name, x, y, w, key):
    """A named point of an anatomy(id, name, x, y, w) figure (its `anchors`, in the drawing's viewBox) in page px: where a callout or the camera goes."""
    m = json.load(open(f"{ANATOMY}/{name}/{name}.json"))
    ax, ay = m["anchors"][key]
    return round(x + ax / m["width"] * w), round(y + ay / m["width"] * w)


def screen(html_):
    """Mark markup as the world's SCREEN layer: text and deck elements (a claim, a number, a card, a tag, the comment prompt)
    that sit on the glass, outside the camera. The camera scales, moves and clips pictures; it never touches these, so
    they cannot be cropped or enlarged by a zoom. Callouts (a leader plus its label) stay in the camera, with the part they name."""
    return f"<!--SCR-->{html_}<!--/SCR-->"


def hlxy(x, y, w, vx, vy):
    """A point of a hairline(x, y, w) figure, from its 400 x 320 viewBox to page px: where a callout anchors."""
    return round(x + vx / 400 * w), round(y + vy / 320 * w * 0.8)


def callout(id_, text, ax, ay, lx, ly, col=INK, side="right", w=440):
    """A technical callout: a dot on the part (ax, ay), a leader to (lx, ly), a rule under the label.
    side = which way the rule and label run from (lx, ly). Enters with Short.callout()."""
    ex = min(lx + w, X1) if side == "right" else max(lx - w, X0)       # the rule and label stay inside the content edges
    w = abs(ex - lx) - 8
    svg = (f'<svg class="co" id="{id_}-s" width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0;overflow:visible">'
           f'<polyline id="{id_}-p" points="{ax},{ay} {lx},{ly} {ex},{ly}" pathLength="1" fill="none" stroke="{col}" stroke-width="{LINE}" '
           f'stroke-linejoin="round" stroke-dasharray="1" stroke-dashoffset="1"/>'
           f'<circle id="{id_}-d" cx="{ax}" cy="{ay}" r="13" fill="{YELLOW}" stroke="{INK}" stroke-width="{LINE}" opacity="0"/></svg>')
    left = lx + 8 if side == "right" else ex
    return svg + (f'<div class="lbl ov col" id="{id_}" style="left:{left}px;top:{ly - 70}px;width:{w}px;color:{col if col in TEXT_SAFE else INK};'
                  f'text-align:{"left" if side == "right" else "right"}">{text}</div>')


SHEET_MIN = 80                          # a capture row under this height is unreadable at Short speed (Look: Readable capture)


def sheet(id_, rows, x, y, w=870, pad=30, gap=12):
    """A white sheet of real capture crops, one phrase a row: rows = [(src, src_w, src_h, display_h)]; a row's img gets the
    id <id_>-<file stem>. Crop two or three words a row so each shows 80 px tall or more. Returns (html, height); put it in screen()."""
    imgs, yy = "", pad
    for k, (src, sw, sh, h) in enumerate(rows):
        ww = round(h * sw / sh)
        if h < SHEET_MIN:
            print(f"WARN sheet {id_} row {k} ({os.path.basename(src)}): {h} px tall, {SHEET_MIN} or more reads on a phone; crop fewer words")
        if ww > w - 2 * pad:
            print(f"WARN sheet {id_} row {k} ({os.path.basename(src)}): {ww} px wide in a {w - 2 * pad} px sheet; crop fewer words")
        imgs += f'<img id="{id_}-{os.path.splitext(os.path.basename(src))[0]}" src="{src}" style="position:absolute;left:{pad}px;top:{yy}px;width:{ww}px;height:{h}px"/>'
        yy += h + gap
    H = yy - gap + pad
    return (f'<div class="art" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px;height:{H}px;background:{WHITE};'
            f'border:{LINE}px solid {INK};border-radius:14px;box-shadow:14px 14px 0 {INK}">{imgs}</div>'), H


def tag(id_, text, x, y, col=BLUE):
    """A line-drawn tag holding a query or a name: the thing that moves between figures."""
    return f'<div class="tag ov" id="{id_}" style="left:{x}px;top:{y}px;color:{col if col in TEXT_SAFE else INK};border-color:{col if col in TEXT_SAFE else INK}">{html.escape(text)}</div>'


RAIL_Y = 196
RAIL_BOTTOM = 310                      # with a rail on screen, world content starts below this line
CLOCK = ((r"performance\.now\(", "__HL.now("), (r"requestAnimationFrame\(", "__HL.raf("), (r"cancelAnimationFrame\(", "__HL.caf("),
         (r"new IntersectionObserver\(", "new __HL.IO("), (r"(window\.)?setTimeout\(", "__HL.st("), (r"clearTimeout\(", "__HL.ct("))


def rail(steps):
    """The pipeline rail: one node per step of the mechanism across the top of the STAGE; Short.step() lights it."""
    n, nodes = len(steps), ""
    for k, t in enumerate(steps):
        nodes += (f'<div class="rn" id="rail-n{k}" style="left:{colx(k, n) - X0 - 110}px"><i id="rail-d{k}"></i>'
                  f'<span id="rail-t{k}">{html.escape(t)}</span></div>')
    return (f'<div id="rail" class="ov" style="position:absolute;left:{X0}px;top:{RAIL_Y}px;width:{X1 - X0}px;height:100px">'
            f'<div class="rl" style="left:{colx(0, n) - X0}px;width:{colx(n - 1, n) - colx(0, n)}px"></div>{nodes}</div>')


def card(id_, label, title, detail, good=False):
    """Context card in the DECK: source label, one title, one detail line. good = the solution's mint card."""
    if len(title) > 26 or len(detail) > 40:
        print(f"WARN card {id_}: title {len(title)} characters (26 or fewer), detail {len(detail)} (40 or fewer): it will wrap and outgrow the deck")
    return (f'<div id="{id_}" class="card ov{" good" if good else ""}"><div class="lab">{label}</div><div class="tit">{html.escape(title)}</div>'
            f'<div class="det">{html.escape(detail)}</div></div>')


def ask(id_, question, answers):
    """Comment prompt (the closing question): a reply box with answer chips, in the DECK."""
    if sum(len(a) * 23 + 70 for a in answers) > 830:      # chips are one row inside the 894 px panel: 40 px type, 52 px padding, 18 px gap
        print(f"WARN ask {id_}: the chips {answers} are wider than the panel; shorten them (about 27 characters in all for three)")
    chips = "".join(f'<span class="chip" id="{id_}-c{k}">{html.escape(a)}</span>' for k, a in enumerate(answers))
    return (f'<div class="ask ov" id="{id_}"><div class="askq"><svg viewBox="0 0 48 48" width="84" height="84"><path d="M8 10h32a4 4 0 0 1 4 4v16a4 4 0 0 1-4 4H22l-9 8v-8H8a4 4 0 0 1-4-4V14a4 4 0 0 1 4-4z" fill="{YELLOW}" stroke="{INK}" stroke-width="3.4" stroke-linejoin="round"/></svg>{html.escape(question)}</div>'
            f'<div class="chips">{chips}</div><div class="askf">reply in the comments</div></div>')


FONTS = [("Inter", 400, "Inter-Regular.otf"), ("Inter", 600, "Inter-SemiBold.otf"), ("Inter", 700, "Inter-Bold.otf"),
         ("Inter", 800, "Inter-ExtraBold.otf"), ("Inter", 900, "Inter-Black.otf"), ("Inter Display", 700, "InterDisplay-Bold.otf"),
         ("Inter Display", 800, "InterDisplay-ExtraBold.otf"), ("Inter Display", 900, "InterDisplay-Black.otf"),
         ("JetBrains Mono", 400, "JetBrainsMono-Regular.ttf"), ("JetBrains Mono", 700, "JetBrainsMono-Bold.ttf")]
FACES = "".join(f'@font-face {{ font-family:"{f}"; font-weight:{w}; src:url("assets/fonts/{n}"); }}\n' for f, w, n in FONTS)
CSS = FACES + f'''
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{ width:1080px; height:1920px; overflow:hidden; background:{PAPER}; }}
#root {{ position:relative; width:1080px; height:1920px; font-family:Inter, sans-serif; color:{INK}; perspective:1600px; }}
/* ground: flat paper and a static dot grid (static texture costs the encoder nothing between frames) */
#ground {{ position:absolute; inset:0; background-color:{PAPER};
  background-image: radial-gradient(circle at 3px 3px, rgba(18,18,18,0.10) 2.6px, transparent 3.2px); background-size:54px 54px; }}
#flood {{ position:absolute; inset:0; background:{GREEN2}; }}
.world, .world .cam, .world .in, .world .scr {{ position:absolute; inset:0; }}
.world {{ clip-path:inset(0 0 {FH - BAND[0] + 10}px 0); }}      /* worlds never paint over the captions: they own the band */
.p3d, #gl {{ position:absolute; left:0; top:0; width:1080px; height:1920px; }}
.art {{ position:absolute; object-fit:contain; }}
.frm {{ position:absolute; border-radius:22px; border:{LINE}px solid {INK}; box-shadow:12px 12px 0 {INK}; background:{WHITE}; }}
.lbl {{ position:absolute; text-align:center; font-size:52px; font-weight:900; letter-spacing:-0.01em; line-height:1.12; }}
.big {{ position:absolute; font-family:"Inter Display"; font-weight:900; line-height:1.04; letter-spacing:-0.03em; color:{INK}; }}
.big span {{ display:inline-block; }}
.hot {{ padding:0 0.10em; margin:0 -0.04em; border-radius:0.12em; box-shadow:0 0 0 0.04em {INK} inset; }}
.phone {{ position:absolute; border-radius:56px; background:{INK}; border:{LINE}px solid {INK}; padding:14px; box-shadow:14px 14px 0 rgba(18,18,18,0.18); }}
.phone img {{ width:100%; height:100%; border-radius:44px; object-fit:cover; }}
.code {{ position:absolute; padding:30px 38px 32px; border-radius:26px; background:#171717; border:{LINE}px solid {INK};
  font-family:"JetBrains Mono", monospace; color:{PAPER}; box-shadow:12px 12px 0 rgba(18,18,18,0.25); }}
.code .bar {{ display:flex; align-items:center; gap:12px; margin:-8px 0 18px; font-size:32px; color:#9A958B; font-weight:700; }}
.code .bar i {{ width:20px; height:20px; border-radius:50%; background:#3A3A3A; }}
.code .bar i:nth-child(1) {{ background:{RED}; }} .code .bar i:nth-child(2) {{ background:{YELLOW}; }} .code .bar i:nth-child(3) {{ background:{GREEN}; }}
.code .bar span {{ margin-left:14px; }}
.cl {{ white-space:pre-wrap; }}
.cl s {{ text-decoration:none; color:#7EE2A8; }}
.cl b {{ color:{YELLOW}; font-weight:700; }}
.cl u {{ text-decoration:none; color:#9A958B; }}
.count {{ position:absolute; text-align:center; font-size:76px; font-weight:900; color:{INK}; }}
.count b {{ color:{INK}; background:{YELLOW}; padding:0 0.12em; border-radius:0.1em; font-size:{T["l"]}px; font-family:"Inter Display"; }}
.flash {{ position:absolute; left:0; top:0; width:1080px; background:{WHITE}; }}
.strip {{ position:absolute; overflow:hidden; border-radius:22px; background:{WHITE}; border:{LINE}px solid {INK}; padding:6px 0; }}
.track {{ position:absolute; left:0; top:8px; }}
.arr {{ position:absolute; text-align:center; font-size:52px; font-weight:900; color:{INK}; border-bottom:10px solid {INK}; padding-bottom:10px; }}
.xx {{ position:absolute; height:18px; border-radius:9px; background:{RED}; transform:rotate(-30deg); }}
.card {{ position:absolute; left:56px; top:{DECK[1] - 8}px; width:894px; min-height:270px; border-radius:26px; background:{WHITE};
  border:{LINE}px solid {INK}; box-shadow:14px 14px 0 {INK}; padding:30px 40px; }}
.card::before {{ content:""; position:absolute; left:40px; top:-6px; width:140px; height:12px; border-radius:6px; background:{YELLOW}; border:3px solid {INK}; }}
.card.good {{ background:{GREEN2}; }}
.card.good::before {{ background:{GREEN}; }}
.card .lab {{ font-family:"JetBrains Mono", monospace; font-size:32px; letter-spacing:0.04em; color:{BLUE}; font-weight:700; }}
.card.good .lab {{ color:{GREEN}; }}
.card .tit {{ font-family:"Inter Display"; font-size:64px; font-weight:900; color:{INK}; margin-top:10px; line-height:1.08; letter-spacing:-0.02em; }}
.card .det {{ font-size:42px; font-weight:600; color:{MUTED}; margin-top:12px; line-height:1.2; }}
.tag {{ position:absolute; padding:14px 32px; border:{LINE}px solid; border-radius:48px; background:{WHITE}; font-size:48px; font-weight:900; white-space:nowrap; box-shadow:8px 8px 0 {INK}; }}
#rail {{ z-index:40; }}
#rail::before {{ content:""; position:absolute; left:-56px; top:-16px; width:1080px; height:130px; background:{PAPER}; }}
.rl {{ position:absolute; top:17px; height:{LINE}px; background:{INK}; }}
.rn {{ position:absolute; top:0; width:220px; text-align:center; }}
.rn i {{ display:block; margin:0 auto; width:40px; height:40px; border-radius:50%; border:{LINE}px solid {INK}; background:{WHITE}; }}
.rn span {{ display:block; margin-top:8px; font-family:"JetBrains Mono", monospace; font-size:40px; font-weight:700; color:{MUTED}; }}
.ask {{ position:absolute; left:56px; top:{DECK[1] - 20}px; width:894px; padding:26px 34px 22px; border-radius:40px; background:{WHITE};
  border:{LINE}px solid {INK}; box-shadow:14px 14px 0 {INK}; }}
.askq {{ display:flex; align-items:center; gap:20px; font-family:"Inter Display"; font-size:60px; font-weight:900; color:{INK}; line-height:1.05; }}
.askq svg {{ flex:none; }}
.chips {{ display:flex; gap:18px; margin-top:20px; }}
.chip {{ padding:10px 28px; border-radius:40px; border:{LINE - 2}px solid {INK}; background:{YELLOW}; color:{INK}; font-size:42px; font-weight:900; white-space:nowrap; }}
.askf {{ margin-top:16px; font-size:40px; font-weight:700; color:{MUTED}; }}
.hl {{ position:absolute; --hairline-plate:{WHITE}; --hairline-hi:{BLUE}; --hairline-edge:{INK}; --hairline-mid:{MUTED};
  --hairline-lo:#CFC7B6; --hairline-stroke:{LINE}; }}
.hl [aria-live], .hl .sr-only {{ display:none; }}
.hl * {{ transition:none !important; }}            /* Hairline fades strokes in real time; frames must follow the timeline only */
.an {{ position:absolute; }}
.an.iso {{ --anatomy-paper:{WHITE}; --anatomy-face:{WHITE}; --anatomy-top:{WHITE};
  --anatomy-shade-0:#C4BAA6; --anatomy-shade-1:#D4CBB9; --anatomy-shade-2:#E3DCCD; --anatomy-shade-3:#F1ECE2;
  --anatomy-hi:{INK}; --anatomy-mid:#3D3932; --anatomy-lo:#5A554B; --anatomy-faint:#B3AA98; --anatomy-lit:{INK};
  --anatomy-lit-top:{YELLOW}; --anatomy-lit-shade:#F0B90F; --anatomy-halo:#6F6552; --anatomy-halo-opacity:.30; --anatomy-dot:{INK};
  --anatomy-weight:3.2px; --anatomy-red:{RED}; --anatomy-green:{GREEN}; --anatomy-blue:{BLUE}; }}
.an * {{ transition:none !important; }}
/* captions: ink capitals on paper, the spoken word on a yellow marker */
.cap {{ position:absolute; left:0; width:1080px; top:{BAND[0] + 2}px; height:140px; line-height:140px; text-align:center;
  font-family:Inter; font-weight:900; color:{INK}; letter-spacing:-0.01em; z-index:50; white-space:nowrap; word-spacing:0; }}
.cap .ci {{ display:inline-block; }}
.cap .ci > span {{ display:inline-block; margin:0 0.10em; padding:0 0.12em; line-height:1.18; border-radius:0.14em; }}
.cap .on {{ background:{YELLOW}; box-shadow:0 0 0 0.05em {INK} inset; transform:scale(1.06); }}
'''
HIDE0 = [".ask", ".hl", ".tag", "#rail", ".card", ".art", ".lbl", ".big", ".code", ".cl", ".count", ".strip", ".frm:not(.track .frm)",
         ".arr", ".xx", ".flash"]
norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
sel = lambda s: json.dumps(s) if isinstance(s, list) else (s if s.startswith("[") else json.dumps(s))


def vendor(dst):
    """Copy GSAP, three.js and the fonts into an hf/assets folder: a render never needs the network."""
    for a, b in (("gsap", "gsap"), ("three", "three"), ("fonts", "fonts")):
        shutil.copytree(f"{HERE}/vendor/{a}", f"{dst}/{b}", dirs_exist_ok=True)


def cam_to(cx, cy, z, to=FOCUS):
    """The camera transform (origin 0 0) that shows canvas point (cx, cy) at `to`, z times larger."""
    return round(to[0] - z * cx, 1), round(to[1] - z * cy, 1)


def fit(box, fill=0.85, area=STAGE):
    """The zoom that makes box (x, y, w, h) fill `fill` of the area's width or height, whichever binds first."""
    return round(min(fill * (area[2] - area[0]) / box[2], fill * (area[3] - area[1]) / box[3]), 3)


def blender3d(spec, out, dur, fmt="glb", preview=False, cue=float):
    """Render a scene3d.py spec (cues: seconds from the plate start, or whatever `cue` resolves) to out (.glb or .webm)."""
    from scene3d import resolve
    job = {"spec": resolve(json.loads(json.dumps(spec)), cue), "dur": dur, "out": os.path.abspath(out), "pal": PAL,
           "preview": preview, "label": os.path.basename(out), "format": fmt}
    jp = os.path.splitext(out)[0] + ".job.json"
    json.dump(job, open(jp, "w"))
    r = subprocess.run(["blender", "-b", "--factory-startup", "--python", f"{HERE}/scene3d.py", "--", os.path.abspath(jp)], capture_output=True, text=True)
    print("\n".join(l for l in r.stdout.splitlines() if l.startswith(("WARN", "  3D"))))
    if r.returncode or not os.path.exists(out):
        raise SystemExit(r.stdout[-1500:] + r.stderr[-1500:] + f"\n{out}: Blender failed")
    os.remove(jp)


def peak(path):
    """Seconds from a sound file's start to its loudest sample (most hits swell first)."""
    pcm = decode(path)
    return max(range(len(pcm)), key=lambda i: abs(pcm[i])) / 48000 if pcm else 0.0


def decode(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-f", "s16le", "-ac", "1", "-ar", "48000", "-"], capture_output=True).stdout
    return array("h", raw[: len(raw) // 2 * 2])


WHOOSH = ["whoosh-air", "whoosh-swipe", "whoosh-stick", "whoosh"]   # rotated: the same whoosh on every cut is the tell


class Short:
    def __init__(self, build_file, keys=None, off=0.15, tail=1.2):
        self.here = os.path.dirname(os.path.abspath(build_file))
        self.root = os.path.dirname(self.here)
        self.plan = plan = json.load(open(f"{self.root}/plan.json"))
        self.take = take = f"{self.root}/{plan['voices'][0]}"
        words = json.load(open(os.path.splitext(take)[0] + ".words.json"))
        err = subprocess.run(["ffmpeg", "-i", take, "-af", "silencedetect=noise=-40dB:d=0.2", "-f", "null", "-"], capture_output=True, text=True).stderr
        sil = [(float(e) - float(d), float(e)) for e, d in re.findall(r"silence_end: ([\d.]+) \| silence_duration: ([\d.]+)", err)]
        self.take_dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", take],
                                             capture_output=True, text=True).stdout)
        for w in words:                               # whisper starts words early, inside the silence before them
            for a, b in sil:
                if a <= w[1] < b:
                    w[1] = b
        for k in range(1, len(words)):
            words[k][1] = max(words[k][1], words[k - 1][1] + 0.067)
        said = " ".join(plan["texts"]).split()        # whisper's homophones ("queues" for cues) take the script's spelling
        sm = difflib.SequenceMatcher(None, [norm(w[0]) for w in words], [norm(x) for x in said], autojunk=False)
        for op, a0, a1, b0, b1 in sm.get_opcodes():
            if op == "replace" and a1 - a0 == b1 - b0:     # one heard word for one said word; merges ("webpage") stay as heard
                for w, x in zip(words[a0:a1], said[b0:b1]):
                    if not re.search(r"\d|%", w[0]):
                        w[0] = x
        self.off, self.words = off, words
        self.DUR = round(off + self.take_dur + tail, 2)
        self.Hw = Hw = [norm(w[0]) for w in words]
        starts, i = [], 0
        for t in plan["texts"]:
            first = [norm(x) for x in t.split()[:4]]
            while Hw[i:i + len(first)] != first:          # a scene may be under 4 words
                i += 1
                if i > len(Hw):
                    raise SystemExit(f"scene start not heard: {first}")
            starts.append(i)
            i += 1
        self.starts = starts + [len(words)]
        self.NS = NS = len(plan["texts"])
        self.S = [None] + [self.T(starts[k]) for k in range(NS)]
        cut = lambda n: 0 if n == 1 else round(self.S[n] - 0.2, 3)
        self.ORDER = [f"w{n}" for n in range(1, NS + 1)]
        self.win = {f"w{n}": (cut(n), cut(n + 1) if n < NS else self.DUR) for n in range(1, NS + 1)}
        self.timed = timed = [(w[0], self.T(k), round(off + w[2], 3)) for k, w in enumerate(words)]
        keys = keys or {}
        self.caps = html_caps(timed, lambda t, s: keys.get(t) if keys.get(t) in TEXT_SAFE else None, end=off + self.take_dur, lit=INK)
        self.J, self.extra, self.models, self.figs, self.sounds = [], [], [], {}, []
        self.anat = {}                                 # Anatomy figures: id -> {name, keys}
        self.beats, self.moves, self.callouts = [], [], {}   # event times (for the frame audit), camera moves, callout windows

    T = lambda self, i: round(self.off + self.words[i][1], 3)

    def cue(self, sc, word, nth=1):
        """Time of the nth heard word starting with `word` in scene sc (1-based)."""
        hits = [k for k in range(self.starts[sc - 1], self.starts[sc]) if self.Hw[k].startswith(norm(word))]
        if len(hits) < nth:
            raise SystemExit(f"cue '{word}' not heard in scene {sc}: {' '.join(self.Hw[self.starts[sc - 1]:self.starts[sc]])}")
        return self.T(hits[nth - 1])

    # ---- motion verbs (Look: Components and verbs). Arrivals land on a long tail; exits are shorter and accelerate.
    # immediateRender:false: a verb never hides its target before its own time (things shown from frame 0 stay shown).
    def at(self, t, js):
        self.J.append("tl." + js.replace("@", str(round(t, 3))))
        self.beats.append(round(t, 2))

    def pop(self, s, t, spring=False):                # labels, frames, cards, figures: rise 24 px
        self.at(t, f'fromTo({sel(s)}, {{opacity:0, y:24, scale:{0.9 if spring else 1}}}, {{immediateRender:false, opacity:1, y:0, scale:1, duration:{0.5 if spring else 0.4}, ease:"{"back.out(1.4)" if spring else "expo.out"}"}}, @);')

    def grow(self, s, t):                             # a picture arrives on its noun: scale up from the middle
        self.at(t, f'fromTo({sel(s)}, {{opacity:0, scale:0.6}}, {{immediateRender:false, opacity:1, scale:1, duration:0.55, ease:"expo.out"}}, @);')

    def blurin(self, s, t, d=0.18):                   # a whole line blurs in: 8 px to 0
        self.at(t, f'fromTo({sel(s)}, {{opacity:0, filter:"blur(8px)"}}, {{immediateRender:false, opacity:1, filter:"blur(0px)", duration:{d}, ease:"power2.out"}}, @);')

    def reveal(self, id_, t, n, step=0.067):          # a big() line of n words, word by word: blur 6 px to 0, no translate
        self.at(t, f'set("#{id_}", {{opacity:1}}, @);')
        for k in range(n):
            self.at(t + step * k, f'fromTo("#{id_}-w{k}", {{opacity:0, filter:"blur(6px)"}}, {{immediateRender:false, opacity:1, filter:"blur(0px)", duration:0.13, ease:"power2.out"}}, @);')

    def hide(self, s, t, d=0.2):
        self.at(t, f'to({sel(s)}, {{opacity:0, filter:"blur(6px)", duration:{d}, ease:"power3.in"}}, @);')

    def rise(self, s, t):                             # panels from the deck: the comment prompt
        self.at(t, f'fromTo({sel(s)}, {{opacity:0, y:60}}, {{immediateRender:false, opacity:1, y:0, duration:0.5, ease:"expo.out"}}, @);')

    def chips(self, id_, n, t, step=0.12):
        for k in range(n):
            self.at(t + step * k, f'fromTo("#{id_}-c{k}", {{opacity:0, scale:0.7}}, {{immediateRender:false, opacity:1, scale:1, duration:0.4, ease:"back.out(1.4)"}}, @);')
            self.sfx(t + step * k, "pop", -30)

    def count(self, s, to, t, d=0.9):
        self.at(t, f'to({sel(s)}, {{textContent:{to}, duration:{d}, snap:{{textContent:1}}, ease:"power2.out"}}, @);')

    def flash(self, s, t):
        self.at(t, f'fromTo({sel(s)}, {{opacity:0.9}}, {{immediateRender:false, opacity:0, duration:0.35, ease:"power2.out"}}, @);')

    def strike(self, s, t):
        self.at(t, f'to({sel(s)}, {{opacity:1, scaleX:1, duration:0.3, ease:"power3.out"}}, @);')

    def light(self, s, t, col=BLUE):                # recolour on the word that names it
        self.at(t, f'to({sel(s)}, {{color:"{col}", duration:0.3}}, @);')

    def slide(self, s, t, x, d):
        self.at(t, f'to({sel(s)}, {{x:{x}, duration:{d}, ease:"none"}}, @);')

    def nudge(self, s, t, rot=12):
        self.at(t, f'to({sel(s)}, {{rotation:{rot}, duration:0.25, ease:"power2.out", yoyo:true, repeat:1}}, @);')

    # ---- the camera: every world is a canvas; moving it is the scale change (wide, medium, close)
    def cam(self, w, t, cx=FOCUS[0], cy=FOCUS[1], z=1.0, d=0.8, ease="power2.inOut", to=None, sound=None):
        """At t the camera of world w moves so canvas point (cx, cy) sits at `to` (default: where it is, a zoom in place),
        z times larger (d=0: a cut)."""
        to = to or (cx, cy)
        self.moves.append((w, round(t, 2), round(t + d, 2)))
        x, y = cam_to(cx, cy, z, to)
        if d:
            self.at(t, f'to("#{w}-cam", {{x:{x}, y:{y}, scale:{z}, duration:{d}, ease:"{ease}"}}, @);')
        else:
            self.at(t, f'set("#{w}-cam", {{x:{x}, y:{y}, scale:{z}}}, @);')
        if sound or (sound is None and 0 < d <= 0.5):  # a fast move is heard
            self.sfx(t + d * 0.5, sound or self._whoosh(), -26, align="peak")

    def focus(self, w, t, box, fill=0.85, d=0.8, area=HERO, **kw):
        """Frame box (x, y, w, h) of world w's canvas: centred in `area`, filling `fill` of it."""
        z = fit(box, fill, area)
        to = ((area[0] + area[2]) / 2, (area[1] + area[3]) / 2)
        self.cam(w, t, box[0] + box[2] / 2, box[1] + box[3] / 2, z, d, to=to, **kw)

    def wide(self, w, t, d=0.8, **kw):                # back to the whole canvas
        self.cam(w, t, d=d, to=FOCUS, **kw)

    def callout(self, id_, t):                        # the leader draws from the part, then the label lands
        self.callouts[id_] = [round(t, 2), None]
        self.at(t, f'fromTo("#{id_}-d", {{opacity:0, scale:0.3, transformOrigin:"50% 50%"}}, {{immediateRender:false, opacity:1, scale:1, duration:0.25, ease:"back.out(1.4)"}}, @);')
        self.at(t + 0.05, f'fromTo("#{id_}-p", {{attr:{{"stroke-dashoffset":1}}}}, {{immediateRender:false, attr:{{"stroke-dashoffset":0}}, duration:0.4, ease:"power3.out"}}, @);')
        self.blurin(f"#{id_}", t + 0.3)
        self.sfx(t, "click", -32)

    def uncallout(self, id_, t):
        self.callouts[id_][1] = round(t, 2)
        self.hide([f"#{id_}", f"#{id_}-s"], t)

    def rail(self, steps, t):
        """The persistent pipeline rail (above the worlds) appears at t, node by node."""
        self.extra.append(f'<div id="railc" class="clip" data-start="0" data-duration="{self.DUR}" data-track-index="40">{rail(steps)}</div>')
        self.at(t, 'set("#rail", {opacity:1}, @);')
        for k in range(len(steps)):
            self.at(t + 0.06 * k, f'fromTo("#rail-n{k}", {{opacity:0, y:16}}, {{immediateRender:false, opacity:1, y:0, duration:0.35, ease:"expo.out"}}, @);')

    def step(self, k, t, state="on"):
        """Rail node k becomes on (ember, the step on screen), done (cream), bad (rose: where it fails) or good (mint)."""
        col = {"on": INK, "done": INK, "bad": RED, "good": GREEN}[state]
        fill = {"on": YELLOW, "done": INK, "bad": RED, "good": GREEN}[state]
        self.at(t, f'to("#rail-d{k}", {{borderColor:"{col}", backgroundColor:"{fill}", scale:1.25, duration:0.25, ease:"back.out(1.4)"}}, @);')
        self.at(t + 0.25, f'to("#rail-d{k}", {{scale:1, duration:0.2}}, @);')
        self.at(t, f'to("#rail-t{k}", {{color:"{col}", duration:0.25}}, @);')

    # ---- sound (Look: Sound kit). Every effect has a cause on screen.
    def sfx(self, t, name, db=-24, align="start"):
        """Place System/assets/sfx/<name>.mp3 at t (align "peak": its loudest sample lands on t), db under full scale."""
        self.sounds.append((round(t, 3), name, db, align))

    def _whoosh(self):
        self._wk = getattr(self, "_wk", -1) + 1
        return WHOOSH[self._wk % len(WHOOSH)]

    def payoff(self, t, rise=True):
        """The reveal: a riser that crests on t (from at most 4 s before) and a hit on t. Once per video."""
        if rise:
            self.sounds.append((round(t, 3), "riser", -27, "end4"))
        self.sfx(t, "impact-bass-2", -20, align="peak")

    # ---- 3D placed on the page
    def plate3d(self, id_, src, t0, dur):
        """An EEVEE plate with alpha (blender3d fmt webm), full frame, under the worlds' text."""
        self.extra.append(f'<video id="{id_}" class="clip p3d" data-start="{t0}" data-duration="{dur}" data-track-index="5" src="{src}" muted playsinline></video>')

    def model3d(self, src, t0, dur):
        """A Blender scene (blender3d fmt glb) played by three.js: its keys and camera follow the timeline."""
        self.models.append({"src": src, "start": t0, "dur": dur})

    # ---- Hairline figures driven on the page clock
    def hairline(self, id_, fn, intensity=0.6, value=None):
        """Mount Hairline's `fn` (drawer, riffle, terrain, sieve, hub, relay, stack, ...) into the hairline() box id_.
        A name in vendor/hairline/custom/ (figures made with /hairline-create, e.g. window) mounts that figure on the
        skill's kernel instead; `value` is its own number (its `range`), default the middle one."""
        custom = os.path.exists(f"{HERE}/vendor/hairline/custom/{fn}.js")
        self.figs[id_] = {"fn": fn, "custom": custom, "value": value, "opts": {"intensity": intensity, "theme": "light"}, "moves": []}

    def point(self, id_, t, x=None, y=None, glide=0):
        """The unseen pointer: at t it moves to (x, y) in the figure's 400 x 320 viewBox (gliding over `glide` s);
        x None = it leaves. Hairline answers the pointer, so this is how a figure acts on a word."""
        self.figs[id_]["moves"].append([round(t, 3), x, y, glide])

    def anatomy(self, id_, name):
        """Mount the Anatomy figure `name` (System/anatomy) into the anatomy() box id_; it starts in its `init` pose."""
        self.anat[id_] = {"name": name, "keys": []}

    def pose(self, id_, t, state, d=0.6, ease="power2.inOut"):
        """At t the figure's parameters move to `state` ({param: value}, only the ones that change) over d seconds.
        The pose function of the figure is a pure map from parameters to part transforms, so every frame is deterministic.
        Keys of one figure must not overlap."""
        f = self.anat[id_]
        if f["keys"] and t < f["keys"][-1][0] + f["keys"][-1][1] - 1e-6:
            raise SystemExit(f"pose {id_}: {round(t, 2)} s overlaps the move that ends at {round(f['keys'][-1][0] + f['keys'][-1][1], 2)} s")
        f["keys"].append([round(t, 3), d, ease, state])
        if d >= 0.2:
            self.sfx(t + d * 0.4, "click", -30)

    def _anatomy(self, end=None):
        """Per figure: its css once, its pose module, and a seek that sets the parameters from the page clock."""
        css, mods = "", ""
        for name in sorted({f["name"] for f in self.anat.values()}):
            d = f"{ANATOMY}/{name}"
            css += open(f"{d}/{name}.css").read() if not css else ""
            mods += f"(() => {{\n{open(f'{d}/{name}.pose.js').read()}\n}})();\n"
        return (f"<style>{css}</style><script>window.__ANP = {{}};\n{mods}"
                "const AN = " + json.dumps(self.anat) + ";\n" + r"""
const anEase = n => gsap.parseEase(n);
function anState(f, init, t) {
  const s = {...init};
  for (const [t0, d, e, st] of f.keys) {
    if (t <= t0) break;
    const p = d > 0 ? Math.min(1, (t - t0) / d) : 1, k = anEase(e)(p);
    for (const key in st) s[key] = s[key] + (st[key] - s[key]) * k;
    if (p < 1) break;
  }
  return s;
}
const anLast = {};
function anSeek(t) {
  for (const [id, f] of Object.entries(AN)) {
    const host = document.getElementById(id); if (!host) continue;
    const tt = __TT__, P = window.__ANP[f.name], s = anState(f, P.init, tt), key = JSON.stringify([s, tt]);
    if (anLast[id] !== key) { anLast[id] = key; P.apply(host.querySelector("svg"), s, tt); }
  }
}
window.__seek.push(anSeek); anSeek(window.__timelines.main.time());
</script>""").replace("__TT__", "t" if end is None else str(end))

    def _hairline(self):
        """Hairline reads performance.now, rAF, timers and IntersectionObserver; the vendored copy is rewritten to read __HL,
        a clock that only moves when the timeline seeks, so every frame is the same on every render (as its parity tests do)."""
        src = open(f"{HERE}/vendor/hairline/hairline-0.5.1.js").read()
        for a, b in CLOCK:
            src = re.sub(a, b, src)
        src = re.sub(r"//# sourceMappingURL=.*", "", src)
        assert "performance.now(" not in src and "requestAnimationFrame(" not in src
        os.makedirs(f"{self.here}/assets", exist_ok=True)
        open(f"{self.here}/assets/hairline.js", "w").write(src)
        custom = sorted({f["fn"] for f in self.figs.values() if f["custom"]})
        if custom:                                      # the skill's kernel, on the same clock, plus each custom figure in its own scope
            k = open(f"{HERE}/vendor/hairline/kernel.js").read()
            for a, b in CLOCK:
                k = re.sub(a, b, k)
            figs = ""
            for n in custom:                            # figures may read performance.now too: same clock
                f = open(f"{HERE}/vendor/hairline/custom/{n}.js").read()
                for a, b in CLOCK:
                    f = re.sub(a, b, f)
                figs += f"(() => {{\n{f}\n}})();\n"
            open(f"{self.here}/assets/hairline-custom.js", "w").write(
                k + "\nwindow.HLK = HL; window.__HLC = {};\nconst hairline = (spec) => { window.__HLC[spec.name] = spec; };\n" + figs)
        return r'''
window.__HL = (() => {
  let now = 0, q = [], tm = [], seq = 0;
  return { now: () => now, raf: cb => (q.push([++seq, cb]), seq), caf: id => { q = q.filter(e => e[0] !== id); },
    st: (cb, ms = 0) => (tm.push([++seq, now + ms, cb]), seq), ct: id => { tm = tm.filter(e => e[0] !== id); },
    IO: class { constructor(cb) { this.cb = cb; } observe(el) { this.cb([{target: el, isIntersecting: true}]); } unobserve() {} disconnect() {} },
    reset() { now = 0; q = []; tm = []; },
    step(to) { while (now < to - 1e-6) { now = Math.min(to, now + 1000 / 60);
      for (const t of tm.filter(t => t[1] <= now)) { tm = tm.filter(x => x !== t); t[2](); }
      const run = q; q = []; for (const [, cb] of run) cb(now); } } };
})();
</script>__CUSTOM__
<script type="module">
import * as HL from "./assets/hairline.js";
const F = __FIGS__;
let figs = [], ev = [], at = 0;
for (const [id, f] of Object.entries(F)) for (const [t, x, y, g] of f.moves) {       // glides become a move every 1/30 s
  const n = g > 0 ? Math.max(1, Math.round(g * 30)) : 0, k0 = ev.filter(e => e.id === id).pop();
  if (n && k0 && k0.x != null && x != null) for (let i = 1; i <= n; i++) ev.push({id, t: t + g * i / n, x: k0.x + (x - k0.x) * i / n, y: k0.y + (y - k0.y) * i / n});
  else ev.push({id, t, x, y});
}
ev.sort((a, b) => a.t - b.t);
function mount() { __HL.reset(); figs.forEach(f => f.destroy()); at = -1;
  figs = Object.entries(F).filter(([id]) => document.getElementById(id))           // a page mounts only the figures it holds
    .map(([id, f]) => f.custom ? custom(document.getElementById(id), f) : HL[f.fn](document.getElementById(id), f.opts)); }
function custom(host, f) {                            // a /hairline-create figure, mounted the way its bench does
  const spec = window.__HLC[f.fn], K = window.HLK;
  K.inject(document); host.setAttribute("data-hairline", spec.name); host.setAttribute("data-hairline-theme", "light");
  const svg = K.mk("svg", {viewBox: "0 0 400 320", "aria-hidden": "true"}, host), read = {textContent: ""};
  const h = spec.mount({stage: host, svg, read}, f.value ?? spec.range[1]);
  return {destroy: () => { h.destroy(); svg.remove(); }};
}
function send(e) {
  const host = document.getElementById(e.id), el = host.querySelector("svg") || host, r = host.getBoundingClientRect();
  if (e.x == null) el.dispatchEvent(new PointerEvent("pointerleave", {pointerType: "mouse", bubbles: true}));
  else el.dispatchEvent(new PointerEvent("pointermove", {pointerType: "mouse", bubbles: true,
    clientX: r.left + e.x / 400 * r.width, clientY: r.top + e.y / 320 * r.height}));
}
function seek(t) {                                   // backwards: remount and replay from 0, so a seek never depends on history
  if (t < at - 1e-6) mount();
  for (const e of ev) if (e.t > at && e.t <= t && document.getElementById(e.id)) { __HL.step(e.t * 1000); send(e); }
  __HL.step(t * 1000); at = t;
}
mount(); window.__seek.push(seek); seek(window.__timelines.main.time());
'''.replace("__FIGS__", json.dumps(self.figs)).replace("__CUSTOM__", '\n<script src="./assets/hairline-custom.js"></script>' if custom else "")

    def _three(self):
        return r'''
import * as THREE from "three";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
const M = __MODELS__, W = 1080, H = 1920;
const canvas = document.getElementById("gl");
const renderer = new THREE.WebGLRenderer({canvas, antialias:true, alpha:true, preserveDrawingBuffer:true});
renderer.setSize(W, H, false); renderer.setPixelRatio(1); renderer.setClearColor(0x000000, 0);
renderer.outputColorSpace = THREE.SRGBColorSpace;
const scene = new THREE.Scene();
scene.add(new THREE.AmbientLight(0xffffff, 0.6));
const keyL = new THREE.DirectionalLight(0xfff4e0, 1.6); keyL.position.set(-4, 6, 8); scene.add(keyL);
const rimL = new THREE.DirectionalLight(0x8ec2f2, 1.0); rimL.position.set(5, 3, -6); scene.add(rimL);
const box3 = new THREE.Box3(), V = new THREE.Vector3();
function screenBox(o, cam) {
  box3.setFromObject(o); if (box3.isEmpty()) return null; let r = [1e9, 1e9, -1e9, -1e9];
  for (let k = 0; k < 8; k++) { V.set(k & 1 ? box3.max.x : box3.min.x, k & 2 ? box3.max.y : box3.min.y, k & 4 ? box3.max.z : box3.min.z).project(cam);
    const x = (V.x + 1) / 2 * W, y = (1 - V.y) / 2 * H; r = [Math.min(r[0], x), Math.min(r[1], y), Math.max(r[2], x), Math.max(r[3], y)]; }
  return r;
}
function render(t) {
  const boxes = []; let cam = null, op = 0;
  for (const m of M) {
    const on = m.root && t >= m.start && t < m.start + m.dur; if (m.root) m.root.visible = on; if (!on) continue;
    for (const a of m.acts) a.time = Math.min(Math.max(t - m.start, 0), a.getClip().duration - 1e-4);   // each clip holds its first and last key: Blender trims every action to its own keys, so looping or mixer time would wrap
    m.mixer.update(0); m.root.updateMatrixWorld(true); cam = m.cam;
    op = Math.min(1, (t - m.start) / 0.25, (m.start + m.dur - t) / 0.2);
    m.root.traverse(o => { if (o.isMesh && o.getWorldScale(V).x > 0.02) { const b = screenBox(o, cam); if (b) boxes.push(b); } });
  }
  canvas.style.opacity = cam ? op : 0;
  if (cam) renderer.render(scene, cam); else renderer.clear();
  window.__boxes3d = boxes;                                   // read by check3d.mjs
}
window.__hf = window.__hf || {}; window.__hf.buildReady = window.__hf.buildReady || {};
window.__hf.buildReady["glb"] = (async () => {
  const loader = new GLTFLoader();
  for (const m of M) {
    const g = await loader.loadAsync(m.src);
    m.root = g.scene; scene.add(m.root); m.mixer = new THREE.AnimationMixer(m.root);
    m.acts = g.animations.map(c => { const a = m.mixer.clipAction(c); a.setLoop(THREE.LoopOnce); a.play(); return a; });
    m.cam = g.cameras[0] || new THREE.PerspectiveCamera(40, W / H, 0.1, 100);
    m.cam.aspect = W / H; m.cam.updateProjectionMatrix();
  }
  const tlm = window.__timelines && window.__timelines["main"];
  render(tlm ? tlm.time() : 0); renderer.getContext().finish();
  window.__seek.push(render);
  window.__render3d = render; window.__ready3d = true;
})();
'''.replace("__MODELS__", json.dumps(self.models))

    # ---- page, sound, timeline
    TRANS = ("cut", "whip", "push", "dip", "blur")

    def _transitions(self, trans):
        """Each world after the first enters by its transition (Look: Camera and transitions); the one before leaves to match."""
        out = []
        for k, w in enumerate(self.ORDER):
            a, b = self.win[w]
            kind = trans.get(w, "cut") if k else None
            nxt = self.ORDER[k + 1] if k + 1 < len(self.ORDER) else None
            leave = trans.get(nxt, "cut") if nxt else None
            if kind and kind not in self.TRANS:
                raise SystemExit(f"{w}: transition '{kind}' is not one of {self.TRANS}")
            if kind in ("cut", "dip"):                 # lands slightly large and settles
                out.append(f'fromTo("#{w}-in", {{scale:1.04}}, {{scale:1, duration:0.5, ease:"expo.out"}}, {a});')
            elif kind == "whip":
                out.append(f'fromTo("#{w}-in", {{x:300, opacity:0, filter:"blur(14px)"}}, {{x:0, opacity:1, filter:"blur(0px)", duration:0.26, ease:"power3.out"}}, {a});')
                self.sfx(a, self._whoosh(), -24, align="peak")
            elif kind == "push":
                out.append(f'fromTo("#{w}-in", {{scale:0.86, opacity:0, filter:"blur(8px)"}}, {{scale:1, opacity:1, filter:"blur(0px)", duration:0.4, ease:"expo.out"}}, {a});')
                self.sfx(a, self._whoosh(), -25, align="peak")
            elif kind == "blur":
                out.append(f'fromTo("#{w}-in", {{opacity:0, filter:"blur(8px)"}}, {{opacity:1, filter:"blur(0px)", duration:0.2, ease:"power2.out"}}, {a});')
            if leave == "whip":
                out.append(f'to("#{w}-in", {{x:-300, opacity:0, filter:"blur(14px)", duration:0.18, ease:"power3.in"}}, {round(b - 0.18, 3)});')
            elif leave == "push":
                out.append(f'to("#{w}-in", {{scale:1.5, opacity:0, filter:"blur(10px)", duration:0.25, ease:"power3.in"}}, {round(b - 0.25, 3)});')
            elif leave == "dip":
                out.append(f'to("#{w}-in", {{filter:"brightness(0.6)", duration:0.1, ease:"none"}}, {round(b - 0.1, 3)});')
            elif leave == "blur":
                out.append(f'to("#{w}-in", {{opacity:0, filter:"blur(8px)", duration:0.15, ease:"power2.in"}}, {round(b - 0.15, 3)});')
        return out

    def _caption_entries(self):
        """Each phrase rises 16 px in 0.15 s on its first word; later words of the phrase only relight."""
        return [f'fromTo("#c{g[0]}i", {{y:16, opacity:0}}, {{y:0, opacity:1, duration:0.15, ease:"expo.out"}}, {self.timed[g[0]][1]});'
                for g in groups(self.timed)]

    def write(self, W, rev, css="", flood=None, trans=None, blur=False, opening=True, first=()):
        """W: {"w1": html, ...}. trans: {"w2": "whip", ...} (default cut; use 3 to 5 kinds, at most a third hard cuts).
        flood: the scene number where the solution's colour flood starts. blur: HyperFrames' render-time motion blur.
        first: selectors on screen from frame 0 (the hook's claim; frame 0 is the thumbnail on social players)."""
        DUR, win, trans = self.DUR, self.win, trans or {}
        if not first:
            print("WARN first=(): nothing is on screen at frame 0. The hook's picture and claim must show at 0 s (frame 0 is the thumbnail)")
        pic = lambda h: re.sub(r"<!--SCR-->.*?<!--/SCR-->", "", h, flags=re.S)
        scr = lambda h: "".join(re.findall(r"<!--SCR-->(.*?)<!--/SCR-->", h, flags=re.S))
        world = lambda wid, z: (f'<div id="{wid}" class="clip world" data-start="{win[wid][0]}" data-duration="{round(win[wid][1] - win[wid][0], 3)}" '
                                f'data-track-index="{z}"><div class="in" id="{wid}-in"><div class="cam" id="{wid}-cam">{pic(W[wid])}</div>'
                                f'<div class="scr" id="{wid}-scr">{scr(W[wid])}</div></div></div>')
        body = (f'<div id="ground" class="clip" data-start="0" data-duration="{DUR}" data-track-index="0"><div id="flood"></div></div>\n'
                + "".join(e + "\n" for e in self.extra)
                + (f'<canvas id="gl" class="clip" width="1080" height="1920" data-start="0" data-duration="{DUR}" data-track-index="6"></canvas>\n' if self.models else "")
                + "\n".join(world(w, 10 + k) for k, w in enumerate(self.ORDER))
                + f'\n<audio id="vo" class="clip" data-start="{self.off}" data-duration="{round(self.take_dur, 3)}" data-track-index="30" data-volume="1" src="assets/{os.path.basename(self.take)}"></audio>'
                + f'\n<div id="caps" data-track-kind="captions">\n{self.caps}\n</div>')
        head = self._transitions(trans) + self._caption_entries()
        if flood:
            head.append(f'to("#flood", {{opacity:1, duration:0.6, ease:"power2.inOut"}}, {round(self.S[flood] - 0.2, 3)});')
        if opening:
            self.sfx(0.12, "impact-bass-2", -24, align="peak")
        J = ["tl." + h for h in head] + self.J
        three = (f'<script type="module">{self._three()}</script>' if self.models else
                 '<script>window.__render3d = () => {}; window.__boxes3d = []; window.__ready3d = true;</script>')   # 2D only; the overlap check still runs
        hl = f'<script>{self._hairline()}</script>' if self.figs else ""
        if self.anat:
            hl += self._anatomy()
        vendor(f"{self.here}/assets")
        if not os.path.exists(f"{self.here}/assets/{os.path.basename(self.take)}"):
            shutil.copy2(self.take, f"{self.here}/assets/")
        page = f'''<!doctype html>
<html lang="en" data-resolution="portrait">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1920" />
<script src="assets/gsap/gsap.min.js"></script>
<script type="importmap">{{"imports": {{"three": "./assets/three/three.module.js", "three/addons/": "./assets/three/addons/"}}}}</script>
<style>{CSS}{css}</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920"{' data-motion-blur="on"' if blur else ''}>
{body}
</div>
<script>
window.__timelines = window.__timelines || {{}};
const q = s => document.querySelectorAll(s);           // initial states outside the timeline: frame 0 renders them
gsap.set(q("#flood, {", ".join(HIDE0)}"), {{opacity:0}});
if (q(".xx").length) gsap.set(q(".xx"), {{scaleX:0, transformOrigin:"0% 50%"}});
gsap.set(q(".world .cam"), {{transformOrigin:"0% 0%"}});
{f'gsap.set(q({json.dumps(", ".join(first))}), {{opacity:1}});' if first else ''}
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(J)}
window.__timelines["main"] = tl;
window.__seek = [];                                     // 3D and Hairline follow every seek of the page clock
tl.eventCallback("onUpdate", () => window.__seek.forEach(f => f(tl.time())));
window.addEventListener("hf-seek", e => {{ if (e && e.detail && typeof e.detail.time === "number") window.__seek.forEach(f => f(e.detail.time)); }});
</script>
{three}{hl}
</body>
</html>
'''
        open(f"{self.here}/index.html", "w").write(page)
        ren = f"{self.root}/render/{self.plan['prefix']}-{round(DUR)}s-9x16-r{rev}.mp4"
        self._sound(ren)
        for cid, (a, b) in self.callouts.items():            # a callout lives in the camera: no move while it shows
            if b is not None and b - a < 0.8:
                print(f"WARN callout {cid} shows at {a} s and hides at {b} s: under 0.8 s on screen (hidden before it lands, or too brief to read)")
            for w, m0, m1 in self.moves:
                if m1 > a and m0 < (b if b is not None else DUR) and not (b is None and m0 >= self.win[w][1]):
                    if self.win[w][0] <= a < self.win[w][1]:
                        print(f"WARN callout {cid} ({a}s) is on screen while the camera of {w} moves ({m0} to {m1} s): it will be scaled, cropped or detached")
        ev = sorted({t for e in self.beats for t in (e, e + 0.45) if 0 <= t < DUR} | {0.1, DUR - 0.2})
        pick, last = [], -9
        for t in ev:
            if t - last >= 0.35:
                pick.append(round(t, 2)); last = t
        open(f"{self.root}/render/_beats.txt", "w").write(",".join(str(t) for t in pick))
        kinds = [trans.get(w, "cut") for w in self.ORDER[1:]]
        print(f"index.html: {DUR} s, {self.caps.count('class=\"clip cap\"')} caption states, {len(J)} tweens, {len(self.models)} models, "
              f"{len(self.sounds)} sounds; transitions {kinds}; render -> {os.path.basename(ren)}")
        if len(kinds) > 2 and kinds.count("cut") > len(kinds) / 3:
            print(f"WARN {kinds.count('cut')} of {len(kinds)} world changes are hard cuts: give the rest a transition with a cause")
        if len(set(kinds)) < min(3, len(kinds)):
            print(f"WARN only {len(set(kinds))} kinds of transition: use 3 to 5")

    def _sound(self, ren):
        """The effects stem from the kit (System/assets/sfx), and the timeline mix_audio.py reads."""
        SR, n = 48000, int((self.DUR + 1) * 48000)
        mix = array("f", bytes(4 * n))
        cache = {}
        for t, name, db, align in sorted(self.sounds):
            if name not in cache:
                f = f"{SFX_DIR}/{name}.mp3"
                if not os.path.exists(f):
                    raise SystemExit(f"sfx '{name}' is not in System/assets/sfx")
                pcm = decode(f)
                cache[name] = (pcm, max(range(len(pcm)), key=lambda i: abs(pcm[i])) if pcm else 0)
            pcm, pk = cache[name]
            g = 10 ** (db / 20) / 32768
            if align == "peak":
                i0 = int(t * SR) - pk
            elif align == "end4":                       # a riser cresting on t, at most its last 4 s
                pcm = pcm[max(0, pk - 4 * SR):pk + 1]
                i0 = int(t * SR) - len(pcm) + 1
            else:
                i0 = int(t * SR)
            for j in range(max(0, -i0), min(len(pcm), n - i0)):
                mix[i0 + j] += pcm[j] * g
        os.makedirs(f"{self.root}/render/_fx", exist_ok=True)
        top = max((abs(x) for x in mix), default=0)
        if top > 0.89:
            print(f"WARN the effects stem peaks at {20 * math.log10(top):.1f} dBFS: it is limited to -1 dBFS")
            mix = array("f", (x * 0.89 / top for x in mix))
        with wave.open(f"{self.root}/render/_fx/sound_sfx.wav", "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
            w.writeframes(array("h", (int(x * 32767) for x in mix)).tobytes())
        json.dump({"render": ren, "duration": self.DUR, "voices": [{"file": self.take, "at": self.off, "in": 0.0, "dur": self.take_dur}],
                   "stems": {"sfx": f"{self.root}/render/_fx/sound_sfx.wav"}, "engine": "hyperframes",
                   "sounds": [list(s) for s in sorted(self.sounds)]},
                  open(f"{self.root}/render/_timeline.json", "w"), indent=1)

    def thumb(self, inner, css="", out=None):
        """The thumbnail as a still page in the video's own look (Growth: Package): `inner` is world markup shown in its
        end state (one focal picture, at most 4 words of 110 px or more inside x 40..1040, y 600..1320). Writes
        hf/thumb.html and, through headless Chrome, upload/thumb.jpg."""
        vendor(f"{self.here}/assets")
        end = max([m[0] for f in self.figs.values() for m in f["moves"]] + [0]) + 3      # every figure in its end state
        hl = (f"<script>window.__seek = []; window.__timelines = {{main: {{time: () => {end}}}}};" + self._hairline() + "</script>") if self.figs else ""
        if self.anat:                                    # Anatomy figures in their last pose
            hl += self._anatomy(end=max([k[0] + k[1] for f in self.anat.values() for k in f["keys"]] + [0]) + 1).replace("<script>window.__ANP", "<script>window.__seek = window.__seek || []; window.__timelines = window.__timelines || {main: {time: () => 0}}; window.__ANP", 1)
        page = (f'<!doctype html><html><head><meta charset="UTF-8"/><style>{CSS}{css} .ov, .hl, .art, .big {{ opacity:1 }}</style>{"<script src=assets/gsap/gsap.min.js></script>" if self.anat else ""}</head>'
                f'<body><div id="root"><div id="ground"></div>{inner}</div>{hl}</body></html>')
        open(f"{self.here}/thumb.html", "w").write(page)
        out = out or f"{self.root}/upload/thumb.jpg"
        os.makedirs(os.path.dirname(out), exist_ok=True)
        png = os.path.splitext(out)[0] + ".png"
        chrome = subprocess.run("ls $HOME/.cache/hyperframes/chrome/chrome-headless-shell/*/chrome-headless-shell-linux64/chrome-headless-shell | head -1",
                                shell=True, capture_output=True, text=True).stdout.strip()
        subprocess.run([chrome, "--no-sandbox", "--hide-scrollbars", "--allow-file-access-from-files", "--window-size=1080,1920", "--virtual-time-budget=5000",
                        f"--screenshot={png}", f"file://{self.here}/thumb.html"], capture_output=True, check=True)
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", png, "-q:v", "2", out], check=True)
        os.remove(png)
        words = len(" ".join(re.sub("<[^>]+>", " ", m) for m in re.findall(r'class="big ov"[^>]*>(.*?)</div>', inner, re.S)).split())
        if words > 4:
            print(f"WARN thumbnail: {words} words, keep it to 3 or 4")
        print("thumbnail", out)


def demo(d):
    """A 4-scene page that uses every verb on a synthetic take (no API): python3 hfkit.py --demo <dir>."""
    os.makedirs(f"{d}/voice", exist_ok=True)
    os.makedirs(f"{d}/hf", exist_ok=True)
    texts = ["One take reads the script.", "Words become times.", "A page becomes frames.", "Checks pass first."]
    t, words = 0.2, []
    for s in texts:
        for w in s.split():
            words.append([w, round(t, 3), round(t + 0.3, 3)]); t += 0.36
        t += 0.6
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", f"sine=f=180:d={t + 0.3:.2f}", "-ar", "48000", f"{d}/voice/dm-take.wav"], check=True)
    json.dump(words, open(f"{d}/voice/dm-take.words.json", "w"))
    json.dump({"prefix": "dm", "voices": ["voice/dm-take.wav"], "texts": texts}, open(f"{d}/plan.json", "w"))
    v = Short(f"{d}/hf/build.py")
    W = {"w1": big("t1", "One take", 70, 300, 880, T["xl"], hot=1) + card("k1", "VOICE · INWORLD TTS-2", "One take, no cuts", "pauses written into the text"),
         "w2": code("c2", [("<u>$</u> word_timings.py", None), ("<s>'words'</s>: <b>118</b>", None)], 70, 300, 870, title="terminal · real output")
               + callout("o2", "times", 600, 420, 760, 640, BLUE, "left", 400),
         "w3": hairline("h3", 53, 220, 900) + tag("g3", "index.html", 80, 760),
         "w4": counter("n4", "OVERLAPS", 0, 330, 380) + ask("a4", "Ship it?", ["yes", "fix", "drop"])}
    v.reveal("t1", v.S[1], n=2); v.pop("#k1", v.cue(1, "script"))
    v.pop("#c2", v.S[2]); v.pop(["#c2-0", "#c2-1"], v.S[2] + 0.1); v.callout("o2", v.cue(2, "times"))
    v.focus("w2", v.cue(2, "times") + 0.2, (70, 300, 870, 260), d=0.6)
    v.hairline("h3", "riffle"); v.grow("#h3", v.S[3]); v.point("h3", v.cue(3, "frames"), 290, 120, glide=0.3); v.pop("#g3", v.cue(3, "page"))
    v.cam("w3", v.cue(3, "frames"), 503, 420, 1.3, d=0.9)
    v.pop("#n4", v.S[4]); v.count("#n4-n", 0, v.S[4]); v.rise("#a4", v.cue(4, "pass")); v.chips("a4", 3, v.cue(4, "pass") + 0.3)
    v.payoff(v.cue(4, "pass"))
    v.write(W, rev=1, trans={"w2": "whip", "w3": "push", "w4": "dip"}, first=("#t1", "#t1-w0", "#t1-w1", "#k1"))
    v.thumb(hairline("h3", 53, 300, 980) + big("tb", "ONE PAGE, MANY FRAMES", 70, 1080, 880, 120, hot=1))
    print(f"demo written: npx hyperframes snapshot {d}/hf --at 0.5,2,4,6")


if __name__ == "__main__":                              # self-check: grid, camera maths, zones
    if "--demo" in sys.argv:
        demo(os.path.abspath(sys.argv[sys.argv.index("--demo") + 1]))
        raise SystemExit
    assert [colx(k, 3) for k in range(3)] == [205, 503, 801], [colx(k, 3) for k in range(3)]
    assert colx(0, 1) == (X0 + X1) // 2 and rowy(0, 2) == 350
    assert cam_to(*FOCUS, 1.0) == (0, 0), "the identity camera must not move the canvas"
    x, y = cam_to(300, 400, 2.0)
    assert (2 * 300 + x, 2 * 400 + y) == FOCUS, "cam() must put the looked-at point on the focus"
    assert fit((0, 0, 447, 100), 1.0) == 2.0 and fit((0, 0, 100, 680), 1.0) == 1.0
    assert hero(860, 820) == (73, 330) and hero(400, 200) == (303, 640), "hero() centres in the HERO box"
    assert STAGE[3] < DECK[1] < DECK[3] < BAND[0] < BAND[1] < UI_Y, "zones must stack: stage, deck, captions, interface"
    assert all(l > 3.9 for l in [LINE]) and min(T.values()) >= 40
    assert "assets/fonts/Inter-Black.otf" in CSS and all(os.path.exists(f"{HERE}/vendor/fonts/{n}") for _, _, n in FONTS)
    assert os.path.exists(f"{HERE}/vendor/gsap/gsap.min.js") and os.path.exists(f"{HERE}/vendor/three/three.module.js")
    assert all(os.path.exists(f"{SFX_DIR}/{n}.mp3") for n in WHOOSH + ["click", "pop", "riser", "impact-bass-2"])
    print("hfkit OK")
