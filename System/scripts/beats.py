#!/usr/bin/env python3
"""The beat sheet as data: hf/beats.json -> index.html, the sound timeline and the thumbnail, through hfkit (System/Production.md).
A video no longer needs a hand-written hf/build.py: one world per scene, its items (hfkit components) and its events
(motion verbs on spoken words).

    python3 System/scripts/beats.py "Media/…/<Video>" --new      # writes hf/beats.json: one empty world per scene of plan.json
    python3 System/scripts/beats.py "Media/…/<Video>" [--rev N] [--no-thumb]

beats.json:
  {"keys": {"16": "red"},                      caption words in a colour (text-safe names: blue, red, green, ink, muted)
   "defs": {"T1": [["<u>$</u> free -h", null]]},   any string "$T1" in the file is replaced by defs["T1"]
   "trans": {"w2": "push"},                    optional; default: push, whip, cut, blur, dip in turn (3+ kinds, cuts under a third)
   "flood": 7, "rev": 1, "first": [...],       first defaults to every item of w1 (an item with "late": true is left out)
   "worlds": [{"say": "the scene's text (a note, not read)",
               "items": [{"big": "t1", "text": "8B MODEL", "at": [70, 196, 880], "size": "l", "hot": 0}, ...],
               "do": [["reveal", "t2", "needs-0.1"], ["pose", "a2", "16-0.1", {"load": 1}, 1.4], ...]}],
   "thumb": {"items": [...], "do": [["pose", "at", 0.1, {"ok": 1}, 0.1]]},
   "py": "extra.py"}                           (full example: beats-example.json) escape hatch: exec'd with v, K, W, t() before write; never fork hfkit

Items (one key names the type and the id; "at" is x, y, w; colours by name): big (text, size: xs|s|m|l|xl or px, hot, hot_col),
lbl, tag, code (lines, title, size), card (label, title, detail, good), ask (question, answers), counter (prefix, n), arrow,
sheet (rows), anatomy (name), hairline (fn, intensity, value), frame (src, px: [source w, h], fit), phone (src),
box (rect in page px, or on: a frame id and rect in that capture's px), callout (text, anchor: [x, y] | "a2:key" | "h3@vx,vy",
label: [x, y], side, w), html (markup). Text items sit on the SCREEN layer, pictures in the camera; "layer" overrides.

Times: a number (s), "@in" (the world's first frame), "@S" (the scene's first word), "word", "word#2" (its 2nd hearing),
"s3:word" (in scene 3), each with an offset: "needs-0.1", "@in+0.2".
Events: pop|grow|blurin|hide|rise|flash|strike|nudge|light|callout|uncallout [target, t, ...] · reveal [id, t, n?] ·
chips [id, t] · count [sel, to, t, d?] · pose [id, t, state, d?, ease?] · point [id, t, x, y, glide?] ·
cam [t, cx, cy, z, d?] · zoom ["a2:key" | "h3@vx,vy", t, z, d?] · focus [t, [x, y, w, h], fill?, d?] · wide [t, d?] ·
mark [row id, t, db?] (lights a code row, a click) · sfx [name, t, db?, align?] · payoff [t] · rail [steps, t] · step [k, t, state?]
"""
import argparse, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hfkit as K

COL = lambda c: K.PAL.get(c, c) if isinstance(c, str) else c
SCREEN = {"big", "lbl", "tag", "code", "card", "ask", "counter", "arrow", "sheet"}
TYPES = SCREEN | {"anatomy", "hairline", "frame", "phone", "box", "callout", "html"}
AUTO_TRANS = ["push", "whip", "cut", "blur", "dip"]
TIME = re.compile(r"^(?:s(\d+):)?(.+?)(?:#(\d+))?([+-]\d*\.?\d+)?$")


def subst(x, defs):
    if isinstance(x, str) and x.startswith("$") and x[1:] in defs:
        return defs[x[1:]]
    if isinstance(x, list):
        return [subst(y, defs) for y in x]
    if isinstance(x, dict):
        return {k: subst(y, defs) for k, y in x.items()}
    return x


class Beats:
    def __init__(self, root, spec):
        self.root, self.spec = root, spec
        self.v = K.Short(f"{root}/hf/build.py", keys={w: COL(c) for w, c in spec.get("keys", {}).items()})
        self.items = {}                              # id -> (kind, item): what verbs look up (word counts, anchors, frames)

    # ---- times
    def t(self, x, n):
        """A time token of scene n to seconds."""
        if isinstance(x, (int, float)):
            return x
        m = TIME.match(str(x))
        if not m:
            raise SystemExit(f"time '{x}' (scene {n}): use a number, @in, @S or word[#k][+-s]")
        sc, word, nth, off = int(m.group(1) or n), m.group(2), int(m.group(3) or 1), float(m.group(4) or 0)
        if word == "@in":
            base = self.v.win[f"w{sc}"][0]
        elif word == "@S":
            base = self.v.S[sc]
        else:
            base = self.v.cue(sc, word, nth)
        return round(base + off, 3)

    # ---- items
    def kind(self, it):
        ks = [k for k in it if k in TYPES]
        if len(ks) != 1:
            raise SystemExit(f"item {it}: name exactly one type of {sorted(TYPES)}")
        return ks[0]

    def point(self, ref):
        """'a2:key' (an Anatomy anchor), 'h3@vx,vy' (a Hairline viewBox point) or [x, y] to page px."""
        if isinstance(ref, list):
            return tuple(ref)
        if ":" in ref:
            fid, key = ref.split(":")
            it = self.items[fid][1]
            return K.anp(it["name"], *it["at"], key)
        fid, xy = ref.split("@")
        return K.hlxy(*self.items[fid][1]["at"], *map(float, xy.split(",")))

    def html(self, it):
        k = self.kind(it)
        id_, at, col = it[k], it.get("at"), COL(it.get("col", K.INK))
        self.items[id_] = (k, it)
        if k == "big":
            size = K.T.get(it.get("size", "l"), it.get("size"))
            h = K.big(id_, it["text"], *(at or (70, 196, 880)), size, col, it.get("hot"), COL(it.get("hot_col", K.YELLOW)))
        elif k == "lbl":
            h = K.lbl(id_, it["text"], *at, col)
        elif k == "tag":
            h = K.tag(id_, it["text"], *at, COL(it.get("col", K.BLUE)))
        elif k == "code":
            h = K.code(id_, [tuple(r) for r in it["lines"]], *(at or (70, 330, 880)), title=it.get("title"), size=it.get("size", 40))
        elif k == "card":
            h = K.card(id_, it["label"], it["title"], it["detail"], it.get("good", False))
        elif k == "ask":
            h = K.ask(id_, it["question"], it["answers"])
        elif k == "counter":
            h = K.counter(id_, it["prefix"], it["n"], *at)
        elif k == "arrow":
            h = K.arrow(id_, it["text"], *at)
        elif k == "sheet":
            h, _ = K.sheet(id_, [tuple(r) for r in it["rows"]], *at)
        elif k == "anatomy":
            h = K.anatomy(id_, it["name"], *(at or (73, 420, 860)))
            self.v.anatomy(id_, it["name"])
        elif k == "hairline":
            it.setdefault("at", [53, 200, 900])
            h = K.hairline(id_, *it["at"])
            self.v.hairline(id_, it["fn"], it.get("intensity", 0.6), it.get("value"))
        elif k == "frame":
            x, y, w = at
            hh = round(w * it["px"][1] / it["px"][0]) if "px" in it else it.get("h")
            h = K.frame(id_, it["src"], x, y, w, hh, it.get("fit", "fill" if "px" in it else "cover"))
        elif k == "phone":
            h = K.phone(id_, it["src"], *(at or (90, 200, 370)))
        elif k == "box":                              # a ring round a region: page px, or a rect of a frame's source capture
            x, y, w, hh = it["rect"]
            if "on" in it:
                f = self.items[it["on"]][1]
                fx, fy, fw = f["at"]
                s, pad = fw / f["px"][0], it.get("pad", 8)
                x, y, w, hh = round(fx + x * s) - pad, round(fy + y * s) - pad, round(w * s) + 2 * pad, round(hh * s) + 2 * pad
            h = (f'<div class="art" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px;height:{hh}px;'
                 f'border:{K.LINE}px solid {COL(it.get("col", K.RED))};border-radius:12px"></div>')
        elif k == "callout":
            h = K.callout(id_, it["text"], *self.point(it["anchor"]), *it["label"], col, it.get("side", "right"), it.get("w", 440))
        else:
            h = it["html"]
        return K.screen(h) if it.get("layer", "screen" if k in SCREEN else "cam") == "screen" else h

    def world(self, items):
        return "".join(self.html(it) for it in items)

    def first_of(self, items):
        """Every w1 item and its parts (words, code rows) on screen at frame 0: the hook is the thumbnail."""
        out = []
        for it in items:
            k = self.kind(it)
            if it.get("late") or k in ("callout",):
                continue
            id_ = it[k]
            out.append(f"#{id_}")
            if k == "big":
                out += [f"#{id_}-w{j}" for j in range(len(it["text"].split()))]
            elif k == "code":
                out += [f"#{id_}-{r[1] or j}" for j, r in enumerate(it["lines"])]
            elif k == "ask":
                out += [f"#{id_}-c{j}" for j in range(len(it["answers"]))]
        return out

    # ---- events
    def event(self, e, n):
        v, w, verb, a = self.v, f"w{n}", e[0], list(e[1:])
        T = lambda x: self.t(x, n)
        if verb in ("pop", "grow", "blurin", "hide", "rise", "flash", "strike", "nudge", "light", "callout", "uncallout"):
            a[1] = T(a[1])
            if verb == "light" and len(a) > 2:
                a[2] = COL(a[2])
            getattr(v, verb)(*a)
        elif verb == "reveal":
            n_words = a[2] if len(a) > 2 else len(self.items[a[0]][1]["text"].split())
            v.reveal(a[0], T(a[1]), n_words)
        elif verb == "chips":
            v.chips(a[0], len(self.items[a[0]][1]["answers"]), T(a[1]))
        elif verb == "count":
            v.count(a[0], a[1], T(a[2]), *a[3:])
        elif verb == "pose":
            v.pose(a[0], T(a[1]), *a[2:])
        elif verb == "point":
            v.point(a[0], T(a[1]), *a[2:])
        elif verb == "cam":
            v.cam(w, T(a[0]), *a[1:])
        elif verb == "zoom":
            v.cam(w, T(a[1]), *self.point(a[0]), *a[2:])
        elif verb == "focus":
            v.focus(w, T(a[0]), tuple(a[1]), *a[2:])
        elif verb == "wide":
            v.wide(w, T(a[0]), *a[1:])
        elif verb == "mark":
            t = T(a[1])
            v.at(t, f'to("#{a[0]}", {{backgroundColor:"#3A3A3A", boxShadow:"inset 10px 0 0 {K.YELLOW}", duration:0.25}}, @);')
            v.sfx(t + 0.1, "click", a[2] if len(a) > 2 else -28)
        elif verb == "sfx":
            v.sfx(T(a[1]), a[0], *a[2:])
        elif verb == "payoff":
            v.payoff(T(a[0]), *a[1:])
        elif verb == "rail":
            v.rail(a[0], T(a[1]))
        elif verb == "step":
            v.step(a[0], T(a[1]), *a[2:])
        else:
            raise SystemExit(f"scene {n}: unknown event '{verb}' (see beats.py's docstring)")

    def build(self, rev=None, thumb=True):
        s, v = self.spec, self.v
        ws = s["worlds"]
        if len(ws) != v.NS:
            raise SystemExit(f"beats.json has {len(ws)} worlds, plan.json {v.NS} scenes: one world per scene")
        W = {f"w{n}": self.world(wd.get("items", [])) for n, wd in enumerate(ws, 1)}
        for n, wd in enumerate(ws, 1):
            for e in wd.get("do", []):
                self.event(e, n)
        if s.get("py"):
            exec(open(os.path.join(self.root, "hf", s["py"])).read(), {"v": v, "K": K, "W": W, "t": self.t, "items": self.items})
        trans = s.get("trans") or {f"w{n}": AUTO_TRANS[(n - 2) % len(AUTO_TRANS)] for n in range(2, v.NS + 1)}
        first = s.get("first") or self.first_of(ws[0].get("items", []))
        v.write(W, rev=rev or s.get("rev", 1), trans=trans, flood=s.get("flood"), first=first, css=s.get("css", ""))
        if thumb and s.get("thumb"):
            th = s["thumb"]
            inner = re.sub(r"<!--/?SCR-->", "", self.world(th["items"]))     # a still has no camera: no layers
            for e in th.get("do", []):
                self.event(e, 1)
            v.thumb(inner)


def new(root):
    """A skeleton: one world per scene, its text as a note; the agent fills items and events from the beat sheet."""
    plan = json.load(open(f"{root}/plan.json"))
    out = f"{root}/hf/beats.json"
    if os.path.exists(out):
        raise SystemExit(f"{out} exists; edit it")
    os.makedirs(f"{root}/hf", exist_ok=True)
    json.dump({"keys": {}, "defs": {}, "worlds": [{"say": t, "items": [], "do": []} for t in plan["texts"]],
               "thumb": {"items": [], "do": []}}, open(out, "w"), indent=1)
    print("wrote", out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("root", help="the video's Media folder (holds plan.json and hf/)")
    ap.add_argument("--new", action="store_true", help="write a skeleton hf/beats.json from plan.json")
    ap.add_argument("--rev", type=int)
    ap.add_argument("--no-thumb", action="store_true")
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    if a.new:
        new(root)
        raise SystemExit
    spec = json.load(open(f"{root}/hf/beats.json"))
    Beats(root, subst(spec, spec.get("defs", {}))).build(a.rev, not a.no_thumb)
