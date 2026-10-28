#!/usr/bin/env python3
"""The Redtail design system as code: one module every HyperFrames builder imports (System/Design system.md).

    import sys; sys.path.insert(0, "<vault>/System/scripts"); import hfkit as K
    v = K.Short(__file__, keys={"RAG": K.EMBER2})        # plan.json, the take, heard words, scene starts, captions
    W = {"w1": K.fig("h-doc", "page_facing_up", 0, 3, K.ROW1, label="the page") + K.card(...), ...}
    v.grow("#h-doc", v.cue(1, "page")); v.pop("#h-doc-l", v.cue(1, "page") + 0.1)
    v.write(W, rev=1, css="...")                       # index.html, render/_fx/sound_sfx.wav, render/_timeline.json

Layout (px on the 1080x1920 frame): STAGE x 56..950, y 192..860 is where pictures live; the caption band y 880..1040
belongs to captions; DECK y 1080..1420 holds one card or the comment prompt; nothing below 1440 or right of 950.
Columns: colx(k, n) is the centre of column k of n across the stage (n = 3: 205, 503, 801); fig() centres an
illustration and its label on a column, sized by sz(n). Motion verbs are methods (pop, grow, hide, rise, chips, count,
flash, strike, light, settle, slide, nudge); worlds enter and leave on their own (blur 0.25 s in, 0.2 s out).
3D from Blender: blender3d() renders a scene3d.py spec as `webm` (EEVEE, alpha; placed with plate3d) or `glb`
(placed with model3d: three.js plays the baked keys and camera on the page's clock, boxes reach check3d.mjs).
ponytail: one class, one file; split only when a second engine needs it.
"""
import html, json, math, os, random, re, struct, subprocess, sys, wave

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from captions import html_caps

# ---- tokens (Style: Redtail look v2)
INK, INK2, EMBER, EMBER2, SIGNAL, SIGNAL2, MINT, MINT2, ROSE, ROSE2 = ("#0B0D17", "#151A2B", "#E36927", "#FF9A5C", "#418AD1",
                                                                         "#8EC2F2", "#00AE7B", "#5FD6A8", "#B83255", "#E8708F")
CREAM, SLATE, HAZE = "#F3EDE2", "#6B7590", "#262D42"

# ---- layout: zones and the column grid
FW, FH = 1080, 1920
X0, X1 = 56, 950                       # content edges (right strip x > 950 is the platform's)
STAGE = (X0, 192, X1, 860)             # pictures; top 192 px is the Shorts title bar
BAND = (880, 1040)                     # captions only
DECK = (X0, 1080, X1, 1420)            # one card or the comment prompt
ROW1, ROW2 = 220, 560                  # tops of the two picture rows on the stage (a figure is about 300 px tall)
GAP = 14                               # illustration to its label
colx = lambda k, n: round(X0 + (X1 - X0) * (2 * k + 1) / (2 * n))
rowy = lambda k, n, top=STAGE[1], bottom=STAGE[3]: round(top + (bottom - top) * (2 * k + 1) / (2 * n))
sz = lambda n: min(280, round(0.72 * (X1 - X0) / n))           # illustration size in a row of n (Fluent Emoji blur above 280)


# ---- components (HTML strings; ids drive the motion verbs)
def art(id_, name, x, y, size):
    return f'<img class="art" id="{id_}" src="assets/fe-{name}_3d.png" style="left:{x}px;top:{y}px;width:{size}px;height:{size}px"/>'


def lbl(id_, text, x, y, w, col=CREAM):
    return f'<div class="lbl ov" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px;color:{col}">{text}</div>'


def fig(id_, name, k, n, y, size=None, label=None, col=CREAM):
    """An illustration centred on column k of n, its label under it (id_-l). The unit of every row."""
    s, cx, w = size or sz(n), colx(k, n), round((X1 - X0) / n) - 8
    return art(id_, name, cx - s // 2, y, s) + (lbl(f"{id_}-l", label, cx - w // 2, y + s + GAP, w, col) if label else "")


def frame(id_, src, x, y, w):
    """A real 9:16 frame or screenshot (counts as a picture for the fill check)."""
    return f'<img class="frm art" id="{id_}" src="{src}" style="left:{x}px;top:{y}px;width:{w}px;height:{round(w * 16 / 9)}px"/>'


def phone(id_, src, x=90, y=200, w=370, h=660):
    return f'<div class="phone ov box" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><img src="{src}"/></div>'


def code(id_, lines, x=70, y=200, w=870):
    """Mono panel; lines are (html, id) with <s>strings</s> in mint and <b>numbers</b> in ember."""
    rows = "".join(f'<div class="cl" id="{id_}-{i or k}">{c}</div>' for k, (c, i) in enumerate(lines))
    return f'<div class="code ov" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px">{rows}</div>'


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


def hairline(id_, x=103, y=205, w=800):
    """A Hairline isometric line figure (vendor/hairline, MIT): a host box at 5:4; Short.hairline() names the figure and
    Short.point() moves its unseen pointer on words. 800 wide = 640 tall, inside the STAGE."""
    return f'<div class="hl" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px;height:{round(w * 0.8)}px"></div>'


def hlxy(x, y, w, vx, vy):
    """A point of a hairline(x, y, w) figure, from its 400 x 320 viewBox to page px: where a callout anchors."""
    return round(x + vx / 400 * w), round(y + vy / 320 * w * 0.8)


def callout(id_, text, ax, ay, lx, ly, col=CREAM, side="right", w=440):
    """A technical callout: a dot on the part (ax, ay), a hairline leader to (lx, ly), a rule under the label.
    side = which way the rule and label run from (lx, ly). Enters with Short.callout()."""
    ex = min(lx + w, X1) if side == "right" else max(lx - w, X0)       # the rule and label stay inside the content edges
    w = abs(ex - lx) - 8
    svg = (f'<svg class="co" id="{id_}-s" width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0;overflow:visible">'
           f'<polyline id="{id_}-p" points="{ax},{ay} {lx},{ly} {ex},{ly}" pathLength="1" fill="none" stroke="{col}" stroke-width="3.2" '
           f'stroke-linejoin="round" stroke-dasharray="1" stroke-dashoffset="1"/>'
           f'<circle id="{id_}-d" cx="{ax}" cy="{ay}" r="9" fill="{INK}" stroke="{col}" stroke-width="3.2" opacity="0"/></svg>')
    left = lx + 8 if side == "right" else ex
    return svg + (f'<div class="lbl ov col" id="{id_}" style="left:{left}px;top:{ly - 64}px;width:{w}px;color:{col};'
                  f'text-align:{"left" if side == "right" else "right"}">{text}</div>')


def tag(id_, text, x, y, col=SIGNAL2):
    """A line-drawn tag holding a query or a name: the thing that moves between figures."""
    return f'<div class="tag ov" id="{id_}" style="left:{x}px;top:{y}px;color:{col};border-color:{col}">{html.escape(text)}</div>'


RAIL_Y = 200
CLOCK = ((r"performance\.now\(", "__HL.now("), (r"requestAnimationFrame\(", "__HL.raf("), (r"cancelAnimationFrame\(", "__HL.caf("),
         (r"new IntersectionObserver\(", "new __HL.IO("), (r"(window\.)?setTimeout\(", "__HL.st("), (r"clearTimeout\(", "__HL.ct("))


def rail(steps):
    """The pipeline rail: one node per step of the mechanism across the top of the STAGE (y 200 to 290); Short.step() lights it."""
    n, nodes = len(steps), ""
    for k, t in enumerate(steps):
        nodes += (f'<div class="rn" id="rail-n{k}" style="left:{colx(k, n) - X0 - 110}px"><i id="rail-d{k}"></i>'
                  f'<span id="rail-t{k}">{html.escape(t)}</span></div>')
    return (f'<div id="rail" class="ov" style="position:absolute;left:{X0}px;top:{RAIL_Y}px;width:{X1 - X0}px;height:92px">'
            f'<div class="rl" style="left:{colx(0, n) - X0}px;width:{colx(n - 1, n) - colx(0, n)}px"></div>{nodes}</div>')


def card(id_, label, title, detail, good=False):
    """Context card in the DECK: source label, one title, one detail line. good = the solution's mint card."""
    return (f'<div id="{id_}" class="card ov{" good" if good else ""}"><div class="lab">{label}</div><div class="tit">{html.escape(title)}</div>'
            f'<div class="det">{html.escape(detail)}</div></div>')


def ask(id_, question, answers):
    """Comment prompt (the closing question): a reply box with answer chips, in the DECK."""
    chips = "".join(f'<span class="chip" id="{id_}-c{k}">{html.escape(a)}</span>' for k, a in enumerate(answers))
    return (f'<div class="ask ov" id="{id_}"><div class="askq"><svg viewBox="0 0 48 48" width="88" height="88"><path d="M8 10h32a4 4 0 0 1 4 4v16a4 4 0 0 1-4 4H22l-9 8v-8H8a4 4 0 0 1-4-4V14a4 4 0 0 1 4-4z" fill="none" stroke="{MINT2}" stroke-width="2.6" stroke-linejoin="round"/></svg>{html.escape(question)}</div>'
            f'<div class="chips">{chips}</div><div class="askf">reply in the comments</div></div>')


CSS = f'''
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{ width:1080px; height:1920px; overflow:hidden; background:{INK}; }}
#root {{ position:relative; width:1080px; height:1920px; font-family:Inter, sans-serif; color:{CREAM}; perspective:1600px; }}
#ground {{ position:absolute; inset:0;
  background: radial-gradient(900px 700px at 15% 85%, rgba(227,105,39,0.10), transparent 70%),
              radial-gradient(800px 700px at 85% 15%, rgba(65,138,209,0.09), transparent 70%),
              linear-gradient(180deg, {INK} 0%, {INK2} 100%); }}
#ground::after {{ content:""; position:absolute; inset:0; background: radial-gradient(ellipse at 50% 45%, transparent 55%, rgba(0,0,0,0.45) 100%); }}
#flood {{ position:absolute; inset:0;
  background: radial-gradient(900px 800px at 20% 30%, rgba(0,174,123,0.26), transparent 70%),
              radial-gradient(800px 800px at 85% 75%, rgba(65,138,209,0.22), transparent 70%); }}
.world, .world > .in {{ position:absolute; inset:0; }}
.p3d, #gl {{ position:absolute; left:0; top:0; width:1080px; height:1920px; }}
.art {{ position:absolute; object-fit:contain; filter:drop-shadow(0 18px 30px rgba(0,0,0,0.55)); }}
.frm {{ position:absolute; border-radius:14px; border:3px solid {SLATE}; object-fit:cover; box-shadow:0 12px 30px rgba(0,0,0,0.5); }}
.lbl {{ position:absolute; text-align:center; font-size:46px; font-weight:900; white-space:nowrap; }}
.phone {{ position:absolute; border-radius:50px; background:#05070D; border:4px solid {SLATE}; padding:12px; box-shadow:0 30px 80px rgba(0,0,0,0.6); }}
.phone img {{ width:100%; height:100%; border-radius:40px; object-fit:cover; }}
.code {{ position:absolute; padding:30px 36px; border-radius:26px; background:#0E1220; border:4px solid {SLATE};
  font-family:"JetBrains Mono", monospace; font-size:42px; line-height:64px; color:{CREAM}; }}
.cl {{ white-space:pre; }}
.cl s {{ text-decoration:none; color:{MINT2}; }}
.cl b {{ color:{EMBER2}; }}
.count {{ position:absolute; text-align:center; font-size:76px; font-weight:900; }}
.count b {{ color:{EMBER2}; font-size:96px; }}
.flash {{ position:absolute; left:0; top:0; width:1080px; background:radial-gradient(600px 400px at 80% 25%, rgba(255,255,255,0.75), transparent 70%); }}
.strip {{ position:absolute; overflow:hidden; border-radius:18px; background:#05070D; border:4px solid {SLATE}; padding:6px 0; }}
.track {{ position:absolute; left:0; top:8px; }}
.arr {{ position:absolute; text-align:center; font-size:46px; font-weight:900; color:{SLATE}; border-bottom:8px solid {SLATE}; padding-bottom:10px; }}
.xx {{ position:absolute; height:16px; border-radius:8px; background:{ROSE2}; transform:rotate(-30deg); }}
.card {{ position:absolute; left:56px; top:1127px; width:894px; height:280px; border-radius:22px; background:rgba(21,26,43,0.94);
  border:3.2px solid rgba(243,237,226,0.85); padding:30px 40px; }}
.card::before {{ content:""; position:absolute; left:40px; top:-3px; width:120px; height:6px; background:{EMBER2}; }}
.card.good {{ border-color:{MINT2}; box-shadow:0 0 50px rgba(95,214,168,0.25); }}
.card.good::before {{ background:{MINT2}; }}
.card .lab {{ font-family:"JetBrains Mono", monospace; font-size:30px; letter-spacing:0.08em; color:{EMBER2}; font-weight:700; }}
.card.good .lab {{ color:{MINT2}; }}
.card .tit {{ font-size:56px; font-weight:800; color:{CREAM}; margin-top:10px; white-space:nowrap; }}
.card .det {{ font-size:34px; color:#A9B0C4; margin-top:12px; }}
.col {{ white-space:nowrap; }}
.tag {{ position:absolute; padding:14px 30px; border:3.2px solid; border-radius:44px; background:rgba(21,26,43,0.94); font-size:44px; font-weight:800; white-space:nowrap; }}
#rail {{ z-index:40; }}
.rl {{ position:absolute; top:16px; height:3.2px; background:{SLATE}; }}
.rn {{ position:absolute; top:0; width:220px; text-align:center; }}
.rn i {{ display:block; margin:0 auto; width:34px; height:34px; border-radius:50%; border:3.2px solid {SLATE}; background:{INK}; }}
.rn span {{ display:block; margin-top:6px; font-family:"JetBrains Mono", monospace; font-size:40px; font-weight:700; color:{SLATE}; letter-spacing:0.04em; }}
.ask {{ position:absolute; left:56px; top:1110px; width:894px; padding:26px 32px 22px; border-radius:40px; background:rgba(21,26,43,0.94);
  border:4px solid {MINT2}; box-shadow:0 0 50px rgba(95,214,168,0.30); }}
.askq {{ display:flex; align-items:center; gap:20px; font-size:56px; font-weight:900; color:{CREAM}; }}
.askq svg {{ flex:none; }}
.chips {{ display:flex; gap:18px; margin-top:22px; }}
.chip {{ padding:10px 26px; border-radius:40px; border:4px solid {SIGNAL2}; color:{SIGNAL2}; font-size:40px; font-weight:800; white-space:nowrap; }}
.askf {{ margin-top:18px; font-size:40px; font-weight:700; color:{SLATE}; }}
.hl {{ position:absolute; --hairline-plate:{INK2}; --hairline-hi:{EMBER2}; --hairline-edge:{CREAM}; --hairline-mid:{SLATE};
  --hairline-lo:{HAZE}; --hairline-stroke:3.2; }}
.hl [aria-live], .hl .sr-only {{ display:none; }}
.cap {{ position:absolute; left:0; width:1080px; top:905px; text-align:center; font-family:Inter; font-weight:900; color:#fff;
  line-height:110px; height:110px; -webkit-text-stroke:10px #0A0907; paint-order:stroke fill; text-shadow:0 6px 18px rgba(0,0,0,0.55); z-index:50; white-space:nowrap; }}
'''
HIDE0 = [".ask", ".hl", ".tag", "#rail", ".card", ".art", ".lbl", ".code", ".cl", ".count", ".strip", ".frm:not(.track .frm)", ".arr", ".xx", ".flash"]
norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
sel = lambda s: json.dumps(s) if isinstance(s, list) else (s if s.startswith("[") else json.dumps(s))


def blender3d(spec, out, dur, fmt="glb", preview=False, cue=float):
    """Render a scene3d.py spec (cues: seconds from the plate start, or whatever `cue` resolves) to out (.glb or .webm)."""
    from scene3d import resolve
    from motion import PAL
    job = {"spec": resolve(json.loads(json.dumps(spec)), cue), "dur": dur, "out": os.path.abspath(out), "pal": PAL,
           "preview": preview, "label": os.path.basename(out), "ground": None, "format": fmt}
    jp = os.path.splitext(out)[0] + ".job.json"
    json.dump(job, open(jp, "w"))
    r = subprocess.run(["blender", "-b", "--factory-startup", "--python", f"{HERE}/scene3d.py", "--", os.path.abspath(jp)], capture_output=True, text=True)
    print("\n".join(l for l in r.stdout.splitlines() if l.startswith(("WARN", "  3D"))))
    if r.returncode or not os.path.exists(out):
        raise SystemExit(r.stdout[-1500:] + r.stderr[-1500:] + f"\n{out}: Blender failed")
    os.remove(jp)


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
        self.off, self.words = off, words
        self.DUR = round(off + self.take_dur + tail, 2)
        self.Hw = Hw = [norm(w[0]) for w in words]
        starts, i = [], 0
        for t in plan["texts"]:
            first = [norm(x) for x in t.split()[:4]]
            while Hw[i:i + 4] != first:
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
        timed = [(w[0], self.T(k), round(off + w[2], 3)) for k, w in enumerate(words)]
        keys = keys or {}
        self.caps = html_caps(timed, lambda t, s: keys.get(t, "#FFFFFF"), end=off + self.take_dur)
        self.J, self.extra, self.models, self.figs = [], [], [], {}

    T = lambda self, i: round(self.off + self.words[i][1], 3)

    def cue(self, sc, word, nth=1):
        """Time of the nth heard word starting with `word` in scene sc (1-based)."""
        hits = [k for k in range(self.starts[sc - 1], self.starts[sc]) if self.Hw[k].startswith(norm(word))]
        if len(hits) < nth:
            raise SystemExit(f"cue '{word}' not heard in scene {sc}: {' '.join(self.Hw[self.starts[sc - 1]:self.starts[sc]])}")
        return self.T(hits[nth - 1])

    # ---- motion verbs (Design system: Motion)
    def at(self, t, js):
        self.J.append("tl." + js.replace("@", str(round(t, 3))))

    def pop(self, s, t, spring=False):                # text, labels, cards: rise 24 px
        self.at(t, f'fromTo({sel(s)}, {{opacity:0, y:24, scale:{0.9 if spring else 1}}}, {{opacity:1, y:0, scale:1, duration:{0.5 if spring else 0.35}, ease:"{"back.out(1.7)" if spring else "expo.out"}"}}, @);')

    def grow(self, s, t):                             # illustrations: grow and turn into place
        self.at(t, f'fromTo({sel(s)}, {{opacity:0, scale:0.4, rotation:-12}}, {{opacity:1, scale:1, rotation:0, duration:0.5, ease:"back.out(1.9)"}}, @);')

    def hide(self, s, t):
        self.at(t, f'to({sel(s)}, {{opacity:0, duration:0.2, ease:"power2.in"}}, @);')

    def rise(self, s, t):                             # panels from the deck: the comment prompt
        self.at(t, f'fromTo({sel(s)}, {{opacity:0, y:60}}, {{opacity:1, y:0, duration:0.45, ease:"expo.out"}}, @);')

    def chips(self, id_, n, t, step=0.18):
        for k in range(n):
            self.at(t + step * k, f'fromTo("#{id_}-c{k}", {{opacity:0, scale:0.6}}, {{opacity:1, scale:1, duration:0.35, ease:"back.out(2)"}}, @);')

    def count(self, s, to, t, d=0.9):
        self.at(t, f'to({sel(s)}, {{textContent:{to}, duration:{d}, snap:{{textContent:1}}, ease:"power1.in"}}, @);')

    def flash(self, s, t):
        self.at(t, f'fromTo({sel(s)}, {{opacity:0.9}}, {{opacity:0, duration:0.35, ease:"power2.out"}}, @);')

    def strike(self, s, t):
        self.at(t, f'to({sel(s)}, {{opacity:1, scaleX:1, duration:0.3, ease:"power2.out"}}, @);')

    def light(self, s, t, col=EMBER2):                # recolour on the word that names it
        self.at(t, f'to({sel(s)}, {{color:"{col}", duration:0.3}}, @);')

    def settle(self, s, t=0, k=1.06):                 # frame 1: the hook picture settles in, never static
        self.at(t, f'fromTo({sel(s)}, {{scale:{k}}}, {{scale:1, duration:1.2, ease:"power2.out"}}, @);')

    def slide(self, s, t, x, d):
        self.at(t, f'to({sel(s)}, {{x:{x}, duration:{d}, ease:"none"}}, @);')

    def nudge(self, s, t, rot=20):
        self.at(t, f'to({sel(s)}, {{rotation:{rot}, duration:0.3, yoyo:true, repeat:1}}, @);')

    def callout(self, id_, t):                        # the leader draws from the part, then the label lands
        self.at(t, f'fromTo("#{id_}-d", {{opacity:0, scale:0.3, transformOrigin:"50% 50%"}}, {{opacity:1, scale:1, duration:0.2, ease:"back.out(2)"}}, @);')
        self.at(t + 0.05, f'fromTo("#{id_}-p", {{attr:{{"stroke-dashoffset":1}}}}, {{attr:{{"stroke-dashoffset":0}}, duration:0.35, ease:"power2.out"}}, @);')
        self.pop(f"#{id_}", t + 0.3)

    def uncallout(self, id_, t):
        self.hide([f"#{id_}", f"#{id_}-s"], t)

    def rail(self, steps, t):
        """The persistent pipeline rail (above the worlds) appears at t, node by node."""
        self.extra.append(f'<div id="railc" class="clip" data-start="0" data-duration="{self.DUR}" data-track-index="40">{rail(steps)}</div>')
        self.at(t, 'set("#rail", {opacity:1}, @);')
        for k in range(len(steps)):
            self.at(t + 0.12 * k, f'fromTo("#rail-n{k}", {{opacity:0, y:16}}, {{opacity:1, y:0, duration:0.3, ease:"back.out(2)"}}, @);')

    def step(self, k, t, state="on"):
        """Rail node k becomes on (ember, the step on screen), done (cream), bad (rose: where it fails) or good (mint)."""
        col = {"on": EMBER2, "done": CREAM, "bad": ROSE2, "good": MINT2}[state]
        fill = {"on": EMBER2, "done": INK, "bad": ROSE2, "good": MINT2}[state]
        self.at(t, f'to("#rail-d{k}", {{borderColor:"{col}", backgroundColor:"{fill}", scale:1.25, duration:0.25, ease:"back.out(2)"}}, @);')
        self.at(t + 0.25, f'to("#rail-d{k}", {{scale:1, duration:0.2}}, @);')
        self.at(t, f'to("#rail-t{k}", {{color:"{col}", duration:0.25}}, @);')

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
        self.figs[id_] = {"fn": fn, "custom": custom, "value": value, "opts": {"intensity": intensity, "theme": "dark"}, "moves": []}

    def point(self, id_, t, x=None, y=None, glide=0):
        """The unseen pointer: at t it moves to (x, y) in the figure's 400 x 320 viewBox (gliding over `glide` s);
        x None = it leaves. Hairline answers the pointer, so this is how a figure acts on a word."""
        self.figs[id_]["moves"].append([round(t, 3), x, y, glide])

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
  figs = Object.entries(F).map(([id, f]) => f.custom ? custom(document.getElementById(id), f) : HL[f.fn](document.getElementById(id), f.opts)); }
function custom(host, f) {                            // a /hairline-create figure, mounted the way its bench does
  const spec = window.__HLC[f.fn], K = window.HLK;
  K.inject(document); host.setAttribute("data-hairline", spec.name); host.setAttribute("data-hairline-theme", "dark");
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
  for (const e of ev) if (e.t > at && e.t <= t) { __HL.step(e.t * 1000); send(e); }
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
const keyL = new THREE.DirectionalLight(0xffe2c8, 1.5); keyL.position.set(-4, 6, 8); scene.add(keyL);
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
    def write(self, W, rev, css="", flood=None):
        """W: {"w1": html, ...}. flood: the scene number where the solution's colour flood starts (Style: solution scenes)."""
        DUR, win = self.DUR, self.win
        world = lambda wid, z: (f'<div id="{wid}" class="clip world" data-start="{win[wid][0]}" data-duration="{round(win[wid][1] - win[wid][0], 3)}" '
                                f'data-track-index="{z}"><div class="in" id="{wid}-in">{W[wid]}</div></div>')
        body = (f'<div id="ground" class="clip" data-start="0" data-duration="{DUR}" data-track-index="0"><div id="flood"></div></div>\n'
                + "".join(e + "\n" for e in self.extra)
                + (f'<canvas id="gl" class="clip" width="1080" height="1920" data-start="0" data-duration="{DUR}" data-track-index="6"></canvas>\n' if self.models else "")
                + "\n".join(world(w, 10 + k) for k, w in enumerate(self.ORDER))
                + f'\n<audio id="vo" class="clip" data-start="{self.off}" data-duration="{round(self.take_dur, 3)}" data-track-index="30" data-volume="1" src="assets/{os.path.basename(self.take)}"></audio>'
                + f'\n<div id="caps" data-track-kind="captions">\n{self.caps}\n</div>')
        head = [f'set("#flood", {{opacity:0}}, 0);', f'set({json.dumps(HIDE0)}, {{opacity:0}}, 0);', 'set(".xx", {scaleX:0, transformOrigin:"0% 50%"}, 0);']
        for k, w in enumerate(self.ORDER):
            a, b = win[w]
            if k:
                head.append(f'fromTo("#{w}-in", {{opacity:0, filter:"blur(8px)"}}, {{opacity:1, filter:"blur(0px)", duration:0.25, ease:"power2.out"}}, {a});')
            if b < DUR:
                head.append(f'to("#{w}-in", {{opacity:0, filter:"blur(8px)", duration:0.2, ease:"power2.in"}}, {round(b - 0.2, 3)});')
        if flood:
            head.append(f'to("#flood", {{opacity:1, duration:0.6, ease:"power2.inOut"}}, {round(self.S[flood] - 0.2, 3)});')
        J = ["tl." + h for h in head] + self.J
        three = (f'<script type="module">{self._three()}</script>' if self.models else
                 '<script>window.__render3d = () => {}; window.__boxes3d = []; window.__ready3d = true;</script>')   # 2D only; the overlap check still runs
        hl = f'<script>{self._hairline()}</script>' if self.figs else ""
        page = f'''<!doctype html>
<html lang="en" data-resolution="portrait">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1920" />
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<script type="importmap">{{"imports": {{"three": "https://cdn.jsdelivr.net/npm/three@0.181.2/build/three.module.js", "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.181.2/examples/jsm/"}}}}</script>
<style>{CSS}{css}</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
{body}
</div>
<script>
window.__timelines = window.__timelines || {{}};
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
        print(f"index.html: {DUR} s, {self.caps.count('class=\"clip cap\"')} caption states, {len(J)} tweens, {len(self.models)} models; "
              f"render -> {os.path.basename(ren)}; worlds {win}")

    def _sound(self, ren):
        """The opening thump and a whoosh ending on each cut (stdlib port of build_video.synth_sound), and the timeline for mix_audio.py."""
        SR, DUR = 48000, self.DUR
        cuts = [self.win[w][0] for w in self.ORDER[1:]]
        sfx = [0.0] * int((DUR + 1) * SR)

        def put(t0, xs):
            i0 = max(0, int(t0 * SR))
            for j, x in enumerate(xs[: len(sfx) - i0]):
                sfx[i0 + j] += x
        L = int(0.55 * SR)
        put(0.0, [math.sin(2 * math.pi * (58 - 18 * j / SR) * j / SR) * min(j / SR / 0.004, 1) * math.exp(-j / SR / 0.16) * 0.22 for j in range(L)])
        rnd = random.Random(11)
        for c in cuts:
            L = int(0.42 * SR); z = [rnd.gauss(0, 1) for _ in range(L)]
            acc, low = 0.0, []
            for j, x in enumerate(z):                 # 60-sample moving average: the soft low part of the sweep
                acc += x - (z[j - 60] if j >= 60 else 0); low.append(acc / 60)
            put(c - L / SR * 0.7, [(low[j] * (1 - j / L) * 4.0 + (z[j] - low[j]) * (j / L) * 0.9) * math.sin(math.pi * j / L) ** 2 * 0.075 for j in range(L)])
        os.makedirs(f"{self.root}/render/_fx", exist_ok=True)
        with wave.open(f"{self.root}/render/_fx/sound_sfx.wav", "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
            w.writeframes(b"".join(struct.pack("<h", int(max(-0.9, min(0.9, x)) * 32767)) for x in sfx))
        json.dump({"render": ren, "duration": DUR, "voices": [{"file": self.take, "at": self.off, "in": 0.0, "dur": self.take_dur}],
                   "stems": {"sfx": f"{self.root}/render/_fx/sound_sfx.wav"}, "engine": "hyperframes", "whooshes": cuts},
                  open(f"{self.root}/render/_timeline.json", "w"), indent=1)


if __name__ == "__main__":                              # self-check: the grid stays symmetric and inside the stage
    assert [colx(k, 3) for k in range(3)] == [205, 503, 801], [colx(k, 3) for k in range(3)]
    assert colx(0, 1) == (X0 + X1) // 2 and sz(1) == 280 and sz(3) == 215 and sz(4) == 161
    assert rowy(0, 2) == 359 and rowy(1, 2) == 693
    for n in (1, 2, 3, 4):
        f = fig("a", "x", n - 1, n, ROW2, label="y")
        x, w = map(int, re.findall(r'class="lbl ov" id="a-l" style="left:(-?\d+)px;top:\d+px;width:(\d+)px', f)[0])
        assert X0 <= x and x + w <= X1, (n, x, w)
    assert ROW2 + sz(3) + GAP + 56 < BAND[0], "a figure on row 2 must clear the caption band"
    print("hfkit OK")
