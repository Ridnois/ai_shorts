"""Generic builder for vertical Shorts in Blender 5.2's sequencer, driven by a plan file (`plan.json`).

    VIDEO="Media/<folder>" SOLO_PROYECTO=1 blender -b --factory-startup --python System/scripts/build_video.py   # assemble and measure
    VIDEO="Media/<folder>" blender -b --factory-startup --python System/scripts/build_video.py                  # assemble and render
    VIDEO=... CHECK=1 ...        # also mixes the audio down and checks that every voice starts and ends complete

What it does (see System/Playbook.md §3 and §6):
  * Voices: each take is padded (0.30 s of silence before, 0.40 s after, 20 ms fade-in) into voice/_padded/*.wav and
    placed so the whole clip is audible. The TTS files often start abruptly; the padding and fades remove the "cut" at the start.
  * Plates of five types:
      video    real footage (clips/*.mp4 cut to 9:16 by stock_videos.py, muted), cover-fitted, `in` = seconds into the clip
      motion   an animated explainer rendered by System/scripts/motion.py from the plate's `motion` spec (1080x1920)
      full     a photo or generated image that fills the frame (cover, with a focus point and a slow push, or a
               `move` {"from": [fx, fy, zoom], "to": [fx, fy, zoom]}: a pan from one detail to the one the voice names)
      contain  a photo or diagram fitted inside the frame on a gradient, with rounded corners and a soft shadow
      cutout   a PNG with a transparent background (generated or cut out) over the gradient, with a soft shadow
  * Cuts on the word: a plate with `"at": "token"` ("token#2", "token+0.2") starts just before that word is heard
    in its scene; plates without `at` share the time left evenly. Callouts and cards take `at` too (they appear on the word).
  * render/_timeline.json: every plate's start and end and every heard word (absolute seconds), read by motion.py.
  * Callouts: a dot on a part of the image, a leader line and a short label (explains machines and processes).
  * One card per plate: context (label, title, detail), number (big figure, caption, source) or margin note; vignette and grain.
  * Word-by-word captions (plan `texts`, one narration string per voice, plus optional `captions`: the same takes spelled for the eye, an empty string falls back to `texts`; timings from voice/<take>.words.json made by
    System/scripts/word_timings.py, else estimated): one big word at a time in the lower caption zone, so the video follows with the sound off.
  * Sound design (plan `sound`): synthesized here with numpy (no model, no cost): scene whooshes, plate ticks, card pings,
    callout ticks, an opening thump and a very quiet drone bed, as one WAV mixed under the voice.
  * No bare backdrops: a plate whose file is a blank placeholder is refused (a number card sits on a real photo or explainer).

plan.json: see the docstring of `load_plan` and `System/Playbook.md` §6.
"""
import glob
import json
import os

import aud
import bpy
import numpy as np

ROOT = os.path.abspath(os.environ.get("VIDEO") or sorted(glob.glob("Media/*"))[-1])
PLAN = json.load(open(f"{ROOT}/plan.json", encoding="utf-8"))
_bad = [c for c in "≈≥≤→" if c in json.dumps(PLAN["scenes"], ensure_ascii=False)]
if _bad:                                                          # Noto Sans Display Bold has none of these: they render as boxes
    raise SystemExit(f"plan.json uses {_bad}, which the card font lacks: write about / or more / to / ·")
OUT = f"{ROOT}/render"
FX = f"{OUT}/_fx"
os.makedirs(FX, exist_ok=True)
os.makedirs(f"{ROOT}/voice/_padded", exist_ok=True)
W, H = PLAN.get("size", [1080, 1920])
FPS = PLAN.get("fps", 24)
GAPS = PLAN.get("gaps", [])
START, TAIL = PLAN.get("start", 0.5), PLAN.get("tail", 1.2)
PAD_LEAD, PAD_TAIL, FADE_IN, FADE_OUT = 0.30, 0.40, 0.02, 0.05      # voice padding and fades (s)
LEAD_KEEP, TAIL_KEEP = 0.12, 0.30                                    # silence kept around the speech in the timeline (s)
DIP, XF, ZOOM = 0.20, 0.20, 0.08            # zoom pushes in on odd plates and out on even ones (more movement)
PAPER = (0.945, 0.935, 0.86)
VIGNETTE, GRAIN = 0.20, 0.08
COPPER = (0.78, 0.42, 0.22)
INK = (0.11, 0.10, 0.09, 1.0)
INK_SOFT = (0.30, 0.28, 0.26, 1.0)
HAIR = " "
CAP_Y = 0.50                        # caption centre (fraction of the height from the top): the middle of the frame, clear of the Shorts interface (user, 5 Oct 2026: the old 0.835 sat under the channel name, title and sound ticker)
CAP_CH = 40                         # captions are the top layer: above cards (channels 7 to 10), callouts (20 to 27) and their text (user, 5 Oct 2026)
CAP_SIZE, CAP_GAP = 88, 0.55        # caption font size (px) and the longest pause (s) a word stays on screen

sc = bpy.context.scene
sc.render.fps = FPS
sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = W, H, 100
sc.view_settings.view_transform = "Standard"
sc.sequence_editor_create()
S = sc.sequence_editor.strips
bpy.context.preferences.edit.keyframe_new_interpolation_type = "LINEAR"
fr = lambda t: round(t * FPS)
hexrgb = lambda h: tuple(int(h.lstrip("#")[i:i + 2], 16) / 255 for i in (0, 2, 4))


# ---------------------------------------------------------------- voices
def norm(w):
    return "".join(c for c in w.lower() if c.isalnum())


def pause_cuts(src, pauses, env_of):
    """Inner pauses (user, 5 Oct 2026: "pauses should be paired with the intention and emotion of the phrase").
    `pauses` = [[word, seconds] or [word, seconds, nth]]: the silence after the nth heard `word` becomes exactly `seconds`
    (shorter or longer than the voice made it). Returns [(gap_start, gap_end, seconds)] in the take's own seconds: the gap is the
    quiet run of the take's envelope nearest the word boundary (a zero-length cut at its quietest point if there is none)."""
    wp = f"{ROOT}/{os.path.splitext(src)[0]}.words.json"
    if not pauses:
        return []
    if not os.path.exists(wp):
        raise SystemExit(f"pauses need {wp} (run word_timings.py first)")
    ws, (env, total) = json.load(open(wp)), env_of
    thr, cuts = env.max() * 0.10, []
    for spec in pauses:
        word, secs, nth = spec[0], float(spec[1]), (spec[2] if len(spec) > 2 else 1)
        hits = [i for i, w in enumerate(ws) if norm(w[0]) == norm(word)]
        if len(hits) < nth or hits[nth - 1] + 1 >= len(ws):
            raise SystemExit(f"pause anchor '{word}' (occurrence {nth}) not found before the last heard word in {src}: heard {' '.join(w[0] for w in ws)}")
        i = hits[nth - 1]
        mid = (ws[i][2] + ws[i + 1][1]) / 2
        lo, hi = max(0, int((mid - 0.35) * 100)), min(len(env), int((mid + 0.35) * 100) + 1)
        quiet = [k for k in range(lo, hi) if env[k] < thr]
        if quiet:
            runs, run = [], [quiet[0]]
            for k in quiet[1:]:
                if k == run[-1] + 1:
                    run.append(k)
                else:
                    runs.append(run); run = [k]
            runs.append(run)
            best = min(runs, key=lambda r: abs((r[0] + r[-1]) / 200 - mid) - 0.01 * len(r))
            gs, ge = best[0] / 100 + 0.01, (best[-1] + 1) / 100 - 0.01
        else:
            k = min(range(lo, hi), key=lambda k: env[k]); gs = ge = k / 100 + 0.005
        cuts.append((gs, max(ge, gs), secs))
    return sorted(cuts)


def remap_time(t, cuts):
    """Original take time -> time in the take after its inner pauses were reshaped."""
    shift = 0.0
    for gs, ge, secs in cuts:
        if t >= ge:
            shift += secs - (ge - gs)
        elif t > gs:
            return gs + shift + (t - gs) * secs / max(ge - gs, 1e-6)
    return t + shift


def pad_voice(src, pauses=None):
    """Writes voice/_padded/<name>.wav = lead silence + 20 ms fade-in + voice + 50 ms fade-out + tail silence.
    With `pauses` the inner pauses of the take are reshaped first (see pause_cuts). Returns (path, cuts)."""
    dst = f"{ROOT}/voice/_padded/{os.path.splitext(os.path.basename(src))[0]}.wav"
    cuts = pause_cuts(src, pauses, envelope(f"{ROOT}/{src}")) if pauses else []
    if not cuts and os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(f"{ROOT}/{src}"):
        return dst, cuts
    v = aud.Sound.file(f"{ROOT}/{src}")
    rate, ch = int(v.specs[0]), int(v.specs[1])
    n = len(np.asarray(v.data()))
    if cuts:
        pieces, prev = [], 0.0
        for gs, ge, secs in cuts:
            pieces.append(v.limit(prev, gs).fadein(0, 0.005).fadeout(max(0.0, gs - prev - 0.005), 0.005))
            pieces.append(aud.Sound.silence(rate).limit(0, secs))
            prev = ge
        pieces.append(v.limit(prev, n / rate).fadein(0, 0.005))
        v = pieces[0]
        for pc in pieces[1:]:
            v = v.join(pc)
        n = int(round(sum(len(np.asarray(pc.data())) for pc in pieces)))
    body = v.fadein(0, FADE_IN).fadeout(max(0.0, n / rate - FADE_OUT), FADE_OUT)
    out = aud.Sound.silence(rate).limit(0, PAD_LEAD).join(body).join(aud.Sound.silence(rate).limit(0, PAD_TAIL))
    out.write(dst, rate, ch, aud.FORMAT_S16, aud.CONTAINER_WAV, aud.CODEC_PCM)
    return dst, cuts


def envelope(path):
    s = aud.Sound.file(path)
    rate = s.specs[0]
    a = np.abs(np.asarray(s.data(), dtype=np.float32))
    a = a.mean(axis=1) if a.ndim > 1 else a
    win = int(rate * 0.01)
    n = len(a) // win
    return a[: n * win].reshape(n, win).mean(axis=1), len(a) / rate


def analyse(path):
    env, total = envelope(path)
    v = np.nonzero(env > env.max() * 0.01)[0]
    return v[0] * 0.01, (v[-1] + 1) * 0.01, total


# One take (Playbook §5, 9 Oct 2026): a single voice file reads every scene; its pauses were written into the text by
# voice.py, so nothing is cut or padded inside it and the scene boundaries come from the heard words (set after PLACED).
# Legacy plans (one take per scene) keep the stitched path with `gaps` and `pauses`.
TAKE = len(PLAN["voices"]) == 1 and len(PLAN.get("texts", [])) > 1
voices, t = [], START
NV = len(PLAN["voices"])
for n, src in enumerate(PLAN["voices"], start=1):
    wav, cuts = pad_voice(src, None if TAKE else PLAN["scenes"][n - 1].get("pauses"))
    a, b, total = analyse(wav)
    ini, fin = max(0.0, a - LEAD_KEEP), min(total, b + TAIL_KEEP)
    voices.append({"n": n, "f": wav, "a": a, "b": b, "ini": ini, "fin": fin, "abs": t, "dur": fin - ini, "cuts": cuts})
    t += (fin - ini) + (0 if TAKE else GAPS[n - 1] if n < NV else 0)
if TAKE:
    B = [0.0] + [None] * (len(PLAN["scenes"]) - 1) + [voices[0]["abs"] + voices[0]["dur"] + TAIL]
else:
    B = [0.0] + [v["abs"] + v["dur"] + GAPS[i] / 2 for i, v in enumerate(voices[:-1])] + [voices[-1]["abs"] + voices[-1]["dur"] + TAIL]
T_END = B[-1]
CUE_LEAD = 0.15                     # a plate anchored on a word lands this much before the word (the picture arrives with it)

for v in voices:
    # the strip is created `ini` earlier: frame_offset_start also advances the visible start
    st = S.new_sound(f"voice-{v['n']}", v["f"], 30, fr(v["abs"]) - fr(v["ini"]))
    st.frame_offset_start = fr(v["ini"])
    st.frame_final_end = fr(v["abs"]) + fr(v["dur"])
    assert st.frame_final_start == fr(v["abs"]), (v["n"], st.frame_final_start, fr(v["abs"]))
    v["strip"] = st

paper = S.new_effect("paper", "COLOR", 1, 1, length=fr(T_END))
paper.color = PAPER


def alpha(st, pts):
    seen = {}
    for t_, val in pts:
        seen[fr(t_)] = val
    for f_ in sorted(seen):
        st.blend_alpha = seen[f_]
        st.keyframe_insert("blend_alpha", frame=f_)


# ---------------------------------------------------------------- image helpers (numpy on Blender images)
def load_rgba(path, max_side=None):
    im = bpy.data.images.load(path, check_existing=False)
    if max_side and max(im.size) > max_side:
        k = max_side / max(im.size)
        im.scale(max(1, round(im.size[0] * k)), max(1, round(im.size[1] * k)))
    w, h = im.size
    px = np.empty(w * h * 4, dtype=np.float32)
    im.pixels.foreach_get(px)
    bpy.data.images.remove(im)
    return px.reshape(h, w, 4)[::-1].copy()          # top row first


def resize(arr, nw, nh):
    h, w = arr.shape[:2]
    im = bpy.data.images.new("tmp", w, h, alpha=True)
    im.pixels.foreach_set(arr[::-1].ravel())
    im.scale(nw, nh)
    px = np.empty(nw * nh * 4, dtype=np.float32)
    im.pixels.foreach_get(px)
    bpy.data.images.remove(im)
    return px.reshape(nh, nw, 4)[::-1].copy()


def save_rgba(arr, name):
    path = f"{FX}/{name}.png"
    im = bpy.data.images.new(name, arr.shape[1], arr.shape[0], alpha=True)
    im.pixels.foreach_set(arr[::-1].ravel().astype(np.float32))
    im.filepath_raw = path
    im.file_format = "PNG"
    im.save()
    bpy.data.images.remove(im)
    return path


def box_blur(a, r):
    """Separable box blur (r px, two passes) of a 2D array."""
    k = 2 * r + 1
    for ax in (0, 1):
        for _ in range(2):
            c = np.cumsum(np.pad(a, [(r + 1, r) if i == ax else (0, 0) for i in range(2)], mode="edge"), axis=ax)
            a = (np.take(c, range(k, c.shape[ax]), axis=ax) - np.take(c, range(0, c.shape[ax] - k), axis=ax)) / k
    return a


def rounded_mask(w, h, rad):
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    dx = np.maximum(np.maximum(rad - xx, xx - (w - 1 - rad)), 0)
    dy = np.maximum(np.maximum(rad - yy, yy - (h - 1 - rad)), 0)
    return np.clip(0.5 - (np.sqrt(dx ** 2 + dy ** 2) - rad), 0, 1)


_bg_cache = {}


def blur_bg(plate, idx):
    """Immersive background for `contain` photos (user, 5 Oct 2026: "screen feels empty, only with a picture and a note"):
    the same photo, cover-fitted, strongly blurred and darkened, so the frame is never an empty gradient."""
    src = load_rgba(f"{ROOT}/{plate.get('bg_photo', plate['file'])}", 600)    # `bg_photo`: blur another photo (for a diagram plate)
    h0, w0 = src.shape[:2]
    s = max(W / 4 / w0, H / 4 / h0)
    big = resize(src, max(W // 4, round(w0 * s)), max(H // 4, round(h0 * s)))
    y0, x0 = (big.shape[0] - H // 4) // 2, (big.shape[1] - W // 4) // 2
    small = big[y0:y0 + H // 4, x0:x0 + W // 4, :3]
    small = np.stack([box_blur(small[..., c], 14) for c in range(3)], axis=2)
    tint = np.array(hexrgb(plate.get("tint", "#10161c")), np.float32)
    small = small * 0.38 + tint * 0.22
    rgba = np.concatenate([small, np.ones(small.shape[:2] + (1,), np.float32)], axis=2)
    return save_rgba(resize(rgba, W, H), f"blurbg{idx}")


def gradient(c0, c1, angle):
    key = (c0, c1, angle)
    if key not in _bg_cache:
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        th = np.radians(angle)
        d = (xx - W / 2) * np.cos(th) + (yy - H / 2) * np.sin(th)
        u = np.clip(d / (abs(W * np.cos(th)) + abs(H * np.sin(th))) + 0.5, 0, 1)[..., None]
        a, b = np.array(hexrgb(c0), np.float32), np.array(hexrgb(c1), np.float32)
        rgb = a * (1 - u) + b * u
        rgba = np.concatenate([rgb, np.ones((H, W, 1), np.float32)], axis=2)
        _bg_cache[key] = save_rgba(rgba, f"bg{len(_bg_cache)}")
    return _bg_cache[key]


def compose_layer(plate, idx):
    """Builds the RGBA layer for `contain` and `cutout` plates: placed, masked, with a soft shadow. Returns (path, bbox)."""
    src = load_rgba(f"{ROOT}/{plate['file']}", 2200)
    h0, w0 = src.shape[:2]
    pos = plate.get("pos", [0.5, 0.40])
    if plate["type"] == "contain":
        fw = round(W * plate.get("width", 0.90))
        fh = round(fw * h0 / w0)
        if fh > H * 0.60:                                  # tall images: limit the height
            fh = round(H * 0.60)
            fw = round(fh * w0 / h0)
    else:                                                  # cutout: `size` is the fraction of the frame height
        fh = round(H * plate.get("size", 0.45))
        fw = round(fh * w0 / h0)
        if fw > W * 0.92:
            fw = round(W * 0.92)
            fh = round(fw * h0 / w0)
    img = resize(src, fw, fh)
    if plate["type"] == "contain":
        img[..., 3] = img[..., 3] * rounded_mask(fw, fh, plate.get("radius", 28))
    x0 = round(pos[0] * W - fw / 2)
    y0 = round(pos[1] * H - fh / 2)
    layer = np.zeros((H, W, 4), np.float32)
    # soft shadow from the alpha, offset down
    sh = np.zeros((H, W), np.float32)
    ys, xs = max(0, y0 + 26), max(0, x0)
    ye, xe = min(H, y0 + 26 + fh), min(W, x0 + fw)
    sub = img[..., 3][max(0, -(y0 + 26)):max(0, -(y0 + 26)) + (ye - ys), max(0, -x0):max(0, -x0) + (xe - xs)]
    sh[ys:ye, xs:xe] = sub
    sh = box_blur(sh, 18) * 0.38
    layer[..., 3] = sh
    # image on top (alpha over the shadow)
    iy0, ix0 = max(0, y0), max(0, x0)
    iy1, ix1 = min(H, y0 + fh), min(W, x0 + fw)
    piece = img[iy0 - y0:iy1 - y0, ix0 - x0:ix1 - x0]
    base = layer[iy0:iy1, ix0:ix1]
    a_i = piece[..., 3:4]
    a_b = base[..., 3:4]
    out_a = a_i + a_b * (1 - a_i)
    rgb = np.where(out_a > 1e-5, (piece[..., :3] * a_i + 0.0 * a_b * (1 - a_i)) / np.maximum(out_a, 1e-5), 0)
    layer[iy0:iy1, ix0:ix1, :3] = rgb
    layer[iy0:iy1, ix0:ix1, 3:4] = out_a
    return save_rgba(layer, f"layer{idx}"), (x0, y0, fw, fh)


# ---------------------------------------------------------------- label card (three lines) and callouts
CX0, CX1 = 56, 56 + 894
CY = round(H * 0.66)                  # card centre: below the captions, above the Shorts bottom text (last ≈ 25 %), left of the action buttons (card spans x 56 to 950)
CY0, CY1 = CY - 140, CY + 140
RAD = 16


def card_image():
    m = rounded_mask(CX1 - CX0, CY1 - CY0, RAD)
    yy, xx = np.mgrid[0:CY1 - CY0, 0:CX1 - CX0].astype(np.float32)
    edge = np.clip(1.0 - np.abs((np.sqrt(np.maximum(np.maximum(RAD - xx, xx - (CX1 - CX0 - 1 - RAD)), 0) ** 2 + np.maximum(np.maximum(RAD - yy, yy - (CY1 - CY0 - 1 - RAD)), 0) ** 2) - RAD) + 0.5), 0, 1) * 0.25
    bar = (xx < 8).astype(np.float32) * m
    paper_rgb = np.array([0.976, 0.965, 0.933], np.float32)
    graph = np.array([0.20, 0.19, 0.18], np.float32)
    rgba = np.zeros((CY1 - CY0, CX1 - CX0, 4), np.float32)
    for c in range(3):
        base = paper_rgb[c] * (1 - edge) + graph[c] * edge
        rgba[..., c] = base * (1 - bar) + COPPER[c] * bar
    rgba[..., 3] = np.maximum(m * 0.94, edge * m)
    full = np.zeros((H, W, 4), np.float32)
    full[int(CY0):int(CY1), CX0:CX1] = rgba
    return save_rgba(full, "card")


def callout_image(target, label_xy, box_w, box_h, idx):
    """Dot at `target`, leader line to the label box, and the box (paper, copper bar). Coordinates in pixels."""
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    tx, ty = target
    lx, ly = label_xy
    # nearest point of the box to the target, so the line meets the box edge
    ex = min(max(tx, lx), lx + box_w)
    ey = min(max(ty, ly), ly + box_h)
    vx, vy = ex - tx, ey - ty
    L2 = max(vx * vx + vy * vy, 1e-6)
    u = np.clip(((xx - tx) * vx + (yy - ty) * vy) / L2, 0, 1)
    d = np.sqrt((xx - (tx + u * vx)) ** 2 + (yy - (ty + u * vy)) ** 2)
    line = np.clip(2.2 - d, 0, 1)
    dot = np.clip(13 - np.sqrt((xx - tx) ** 2 + (yy - ty) ** 2), 0, 1)
    ring = np.clip(1.5 - np.abs(np.sqrt((xx - tx) ** 2 + (yy - ty) ** 2) - 20), 0, 1)
    ink = np.maximum(np.maximum(line, dot), ring)
    rgba = np.zeros((H, W, 4), np.float32)
    rgba[..., 0], rgba[..., 1], rgba[..., 2] = COPPER
    rgba[..., 3] = ink
    bw, bh = int(box_w), int(box_h)
    m = rounded_mask(bw, bh, 10)
    bx0, by0 = int(lx), int(ly)
    y1, x1 = min(H, by0 + bh), min(W, bx0 + bw)
    mm = m[: y1 - by0, : x1 - bx0, None]
    sub = rgba[by0:y1, bx0:x1]
    paper_rgb = np.array([0.976, 0.965, 0.933], np.float32)
    sub[..., :3] = sub[..., :3] * (1 - mm) + paper_rgb * mm
    sub[..., 3:4] = np.maximum(sub[..., 3:4], mm * 0.95)
    sub[: , :6, :3] = np.where(mm[:, :6] > 0.5, np.array(COPPER, np.float32), sub[:, :6, :3])
    return save_rgba(rgba, f"callout{idx}")


def spaced(t):
    return HAIR.join(t.upper().replace(" ", "  "))


F_TITLE = bpy.data.fonts.load("/usr/share/fonts/truetype/noto/NotoSansDisplay-Bold.ttf")
F_BODY = bpy.data.fonts.load("/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf")
CARD_PNG = card_image()


def fade(st, t0, t1):
    alpha(st, [(t0, 0.0), (t0 + 0.25, 1.0), (t1 - 0.20, 1.0), (t1, 0.0)])


def add_text(name, txt, font, size, col, ch, t0, t1, xpx, ypx, rise=True):
    tx = S.new_effect(name, "TEXT", ch, fr(t0), length=fr(t1 - t0))
    tx.text, tx.font_size, tx.font, tx.color = txt, size, font, col
    tx.anchor_x, tx.anchor_y = "LEFT", "CENTER"
    for t_, dy in ((t0, -24 / H if rise else 0), (t0 + 0.25, 0.0)):
        tx.location = (xpx / W, 1 - ypx / H + dy)
        tx.keyframe_insert("location", frame=fr(t_))
    fade(tx, t0, t1)
    return tx


# ---------------------------------------------------------------- heard words (captions, cuts on the word, motion cues)
def estimate_words(text, a, b, env):
    """Fallback: split [a, b] (the speech) among the words by characters, adding weight after commas and full stops."""
    ws = text.split()
    wt = [len(w.strip(".,;:!?")) + 1 + (4 if w[-1] in ".!?" else 2 if w[-1] in ",;:" else 0) for w in ws]
    k, t_ = (b - a) / sum(wt), a
    out = []
    for w, x in zip(ws, wt):
        out.append([w, t_, t_ + x * k])
        t_ += x * k
    return out


def align_words(ws, heard):
    """Maps the script words `ws` onto the heard words [[w, s, e], ...]: identical words (letters and digits only) anchor, and the script
    words between two anchors share the heard span between them by characters ("1911." heard for "nineteen eleven" still lands right)."""
    import difflib
    norm = lambda w: "".join(c for c in w.lower() if c.isalnum())
    sm = difflib.SequenceMatcher(None, [norm(w) for w in ws], [norm(h[0]) for h in heard], autojunk=False)
    out, i0, j0 = [], 0, 0
    for i, j, n in sm.get_matching_blocks() + [difflib.Match(len(ws), len(heard), 0)]:
        gap_w, gap_h = ws[i0:i], heard[j0:j]
        if gap_w:
            if gap_h:
                a_, b_ = gap_h[0][1], gap_h[-1][2]
            else:                                             # words nobody heard: borrow a sliver after the previous word
                a_ = out[-1][2] if out else (heard[0][1] if heard else 0.0)
                b_ = a_ + 0.18 * len(gap_w)
            wt = [len(w.strip(".,;:!?")) + 1 for w in gap_w]
            k, t_ = (b_ - a_) / sum(wt), a_
            for w, x in zip(gap_w, wt):
                out.append([w, t_, t_ + x * k])
                t_ += x * k
        for q in range(n):
            out.append([ws[i + q], heard[j + q][1], heard[j + q][2]])
        i0, j0 = i + n, j + n
    return out


def take_words(v, text):
    """[[word, start, end]] in seconds of the padded file (original time + PAD_LEAD), using the script's own spelling."""
    ws = text.split()
    path = os.path.splitext(v["f"])[0].replace("/_padded", "") + ".words.json"
    if os.path.exists(path):
        raw = [[w, remap_time(s, v["cuts"]) + PAD_LEAD, remap_time(e, v["cuts"]) + PAD_LEAD] for w, s, e in json.load(open(path))]
        return snap_onsets(align_words(ws, raw), v["f"])
    return estimate_words(text, v["a"], v["b"], None)


def snap_onsets(words, wav):
    """Whisper often starts a word at the beginning of the silence before it, so its caption (and any cut anchored on it) came
    up to 1 s early (measured 9 Oct 2026: "Tell" shown 0.94 s before it was heard). A start inside a silent run moves to where
    the speech resumes; an end that runs into a silence moves back. Silent = 40 dB under the take's peak (soft consonants stay)."""
    env, _ = envelope(wav)
    quiet = env < env.max() * 0.01
    n = len(quiet)
    out = []
    for w, s, e in words:
        i0, i1 = int(s * 100), min(int(e * 100), n)
        start, k = None, i0
        while k < i1:                                    # silent runs inside the word's span
            if quiet[k]:
                r = k
                while r < i1 and quiet[r]:
                    r += 1
                if r < i1 and (k == i0 or r - k >= 20):  # leading quiet, or a pause of 0.2 s or more: the word starts after it
                    start = r
                k = r
            else:
                k += 1
        j = i1 - 1
        while j > (start or i0) and quiet[j]:
            j -= 1
        out.append([w, start / 100 if start is not None else s, (j + 1) / 100 + 0.02 if j > (start or i0) else e])
    return out


KEYWORDS = {"".join(c for c in k.lower() if c.isalnum()) for k in PLAN.get("keywords", [])}   # up to ~6 key terms per video, shown in copper


def heard_words():
    """[(word, start, end, scene)] in absolute seconds, in the caption spelling (plan `captions` over `texts`)."""
    texts = PLAN.get("texts")
    if not texts:
        return []
    caps = PLAN.get("captions") or [""] * len(texts)
    assert len(caps) == len(texts), "plan.captions needs one string per scene (\"\" keeps the voiced text)"
    if TAKE:                                             # one take: align the whole script, then tag each word with its scene
        shown = [c or t for c, t in zip(caps, texts)]
        v = voices[0]
        scene_of = [k + 1 for k, t in enumerate(shown) for _ in t.split()]
        return [(w, v["abs"] + s_ - v["ini"], v["abs"] + e_ - v["ini"], n)
                for (w, s_, e_), n in zip(take_words(v, " ".join(shown)), scene_of)]
    assert len(texts) == len(voices), "plan.texts needs one narration string per voice"
    out = []
    for v, c, t in zip(voices, caps, texts):   # display spelling ("250 K") over voiced spelling; align_words maps it onto the heard words
        for w, s_, e_ in take_words(v, c or t):
            out.append((w, v["abs"] + s_ - v["ini"], v["abs"] + e_ - v["ini"], v["n"]))
    return out


PLACED = heard_words()
if TAKE:                                                 # scene k ends halfway through the silence before scene k + 1
    for k in range(1, len(PLAN["scenes"])):
        B[k] = (max(w[2] for w in PLACED if w[3] == k) + min(w[1] for w in PLACED if w[3] == k + 1)) / 2


def cue_time(spec, scene, label):
    """Absolute time of a word cue inside a scene: \"token\", \"token#2\" (its second time), \"token+0.3\"."""
    s, off = str(spec), 0.0
    for sign in "+-":
        if sign in s[1:]:
            k = s.rfind(sign)
            s, off = s[:k], float(s[k:])
            break
    word, nth = (s.split("#") + ["1"])[:2]
    hits = [w for w in PLACED if w[3] == scene and norm(w[0]) == norm(word)]
    if len(hits) < int(nth):
        raise SystemExit(f"{label}: cue '{spec}' not heard in scene {scene} (heard: {' '.join(w[0] for w in PLACED if w[3] == scene)})")
    return hits[int(nth) - 1][1] + off


# ---------------------------------------------------------------- plates
for _sc in PLAN["scenes"]:
    for _pl in _sc["plates"]:
        if "blank" in os.path.basename(_pl["file"]).lower() and not PLAN.get("allow_bare"):
            raise SystemExit(f"bare backdrop refused: {_pl['file']} (feedback 4 Oct 2026: put the figure on a photo or explainer; "
                             "set allow_bare only if the user asked for it)")
        if not os.path.exists(f"{ROOT}/{_pl['file']}") and _pl["type"] != "motion":
            raise SystemExit(f"missing plate file: {_pl['file']}")
PENDING = [pl["file"] for sc_ in PLAN["scenes"] for pl in sc_["plates"] if pl["type"] == "motion" and not os.path.exists(f"{ROOT}/{pl['file']}")]
if PENDING and os.environ.get("SOLO_PROYECTO") != "1":
    raise SystemExit(f"motion plates not rendered yet: {PENDING} (run System/scripts/motion.py on this folder first)")
EVENTS = [(0.0, "thump")]                       # (time, kind) for the sound design
SFX_FULL = PLAN.get("sound", {}).get("events") == "full"   # default: the opening hit and scene whooshes only (sounds under speech compete with it; audio research 9 Oct 2026)
idx = 0
flat = []
for e, scene in enumerate(PLAN["scenes"], start=1):
    n = len(scene["plates"])
    t0, t1 = B[e - 1], B[e]
    starts = [t0] + [cue_time(pl["at"], e, pl["file"]) - CUE_LEAD if pl.get("at") else None for pl in scene["plates"][1:]] + [t1]
    k0 = 0                                               # plates without `at` share the time between their anchored neighbours
    for k1 in range(1, n + 1):
        if starts[k1] is not None:
            for q in range(k0 + 1, k1):
                starts[q] = starts[k0] + (starts[k1] - starts[k0]) * (q - k0) / (k1 - k0)
            k0 = k1
    if any(b_ - a_ < 0.8 for a_, b_ in zip(starts, starts[1:])):
        raise SystemExit(f"scene {e}: plate cues out of order or under 0.8 s apart: {[round(x, 2) for x in starts]}")
    for j, pl in enumerate(scene["plates"]):
        idx += 1
        flat.append((idx, e, j, n, starts[j], starts[j + 1], pl))

LONG = [(i, round(float(b - a), 1)) for i, e, j, n, a, b, pl in flat
        if b - a > {"motion": 1e9, "video": 6.0}.get(pl["type"], 4.0 if not pl.get("move") else 5.0)]
print("PLATES", len(flat), "| durations", [round(float(b - a), 1) for i, e, j, n, a, b, pl in flat])
print("LONG PLATE (a still over 4 s, footage over 6 s: add an event or a plate; motion plates are checked by motion.py):", LONG if LONG else "none")
EMPTY = [i for i, e, j, n, a, b, pl in flat if pl["type"] in ("contain", "cutout") and pl.get("bg") != "blur" and not pl.get("inset")]
print("EMPTY PLATE (contain or cutout on a flat gradient: use bg \"blur\" or an inset, user 5 Oct 2026):", EMPTY if EMPTY else "none")
_uses = {}
for i, e, j, n, a, b, pl in flat:
    _uses.setdefault(pl["file"], []).append(i)
REPEAT = {f_: v_ for f_, v_ in _uses.items() if len(v_) > 2}
print("REPEAT (one source on more than 2 plates; a recurring anchor must change state each time):", REPEAT if REPEAT else "none")
MOVING = sum(b - a for i, e, j, n, a, b, pl in flat if pl["type"] in ("video", "motion") or pl.get("move"))
print(f"MOTION SHARE {MOVING / T_END:.0%} of the runtime is footage, animation or a purposeful camera move")
if PENDING:
    print("MOTION PENDING (placeholder only; run motion.py, then build again):", PENDING)
TIMELINE = {"fps": FPS, "duration": T_END, "plates": [], "words": [list(w) for w in PLACED]}


def cover(w, h, fx, fy, k):
    """Offsets that put the focus point (fractions of the picture) at the frame centre, clamped to the picture."""
    ox = max(-(w * k - W) / 2, min((w * k - W) / 2, (0.5 - fx) * w * k))
    oy = max(-(h * k - H) / 2, min((h * k - H) / 2, (fy - 0.5) * h * k + 60))
    return ox, oy


def camera(st, pl, i, ini, fin, w, h, k, push):
    """Cover-fit with either a `move` (pan and zoom from one detail to another) or a gentle push in or out."""
    mv = pl.get("move")
    for t_ in (ini, fin):
        u_ = (t_ - ini) / (fin - ini)
        if mv:
            fx, fy, z = [a_ + (b_ - a_) * u_ for a_, b_ in zip(mv["from"], mv["to"])]
        else:
            fx, fy = pl.get("focus", [0.5, 0.5])
            z = 1.0 + pl.get("zoom", push) * (u_ if i % 2 else 1.0 - u_)
        st.transform.offset_x, st.transform.offset_y = cover(w, h, fx, fy, k * z)
        st.transform.scale_x = st.transform.scale_y = k * z
        for prop in ("scale_x", "scale_y", "offset_x", "offset_y"):
            st.transform.keyframe_insert(prop, frame=fr(t_))


for i, e, j, n, a, b, pl in flat:
    ini = a - (XF / 2 if j > 0 else 0)
    fin = b + (XF / 2 if j < n - 1 else 0)
    TIMELINE["plates"].append({"i": i, "scene": e, "file": pl["file"], "type": pl["type"], "a": a, "b": b, "ini": ini, "fin": fin})
    ch = 3 + 2 * (j % 2)                                 # plate channel: 3 or 5; its gradient sits right below it (2 or 4)
    strips = []
    if pl["type"] in ("video", "motion") and pl["file"] not in PENDING:
        cin = pl.get("in", 0.0)                          # seconds into the clip
        st = S.new_movie(f"plate{i:02d}", f"{ROOT}/{pl['file']}", ch, fr(ini) - fr(cin))
        st.frame_offset_start = fr(cin)
        st.frame_final_end = fr(fin)                     # past the clip's end Blender holds its last frame
        if abs(st.fps - FPS) > 0.01:
            print(f"CLIP FPS {pl['file']}: {st.fps} fps, plan is {FPS} (recut it with stock_videos.py cut)")
        if st.frame_duration - fr(cin) < fr(fin - ini) - 1:
            print(f"SHORT CLIP {pl['file']}: {(st.frame_duration - fr(cin)) / FPS:.1f} s for a {fin - ini:.1f} s plate (last frame held)")
        w, h = st.elements[0].orig_width, st.elements[0].orig_height
        k = max(W / w, H / h) * (1.0 if pl["type"] == "motion" else 1.02)
        camera(st, pl, i, ini, fin, w, h, k, 0.0 if pl["type"] == "motion" else 0.04)
        strips = [st]
    elif pl["type"] == "motion":                         # not rendered yet: a dark stand-in keeps the timing
        st = S.new_image(f"plate{i:02d}", gradient("#101824", "#1a2638", 90), ch, fr(ini))
        st.frame_final_end = fr(fin)
        strips = [st]
    elif pl["type"] == "full":
        st = S.new_image(f"plate{i:02d}", f"{ROOT}/{pl['file']}", ch, fr(ini))
        st.frame_final_end = fr(fin)
        w, h = st.elements[0].orig_width, st.elements[0].orig_height
        camera(st, pl, i, ini, fin, w, h, max(W / w, H / h) * 1.07, ZOOM)
        strips = [st]
    else:
        c0, c1 = ("#10243a", "#27507a") if pl.get("bg") in (None, "blur") else pl["bg"]
        bgpath = blur_bg(pl, i) if pl.get("bg") == "blur" else gradient(c0, c1, pl.get("bg_angle", 70))
        bgs = S.new_image(f"bg{i:02d}", bgpath, ch - 1, fr(ini))
        bgs.frame_final_end = fr(fin)
        path, _ = compose_layer(pl, i)
        st = S.new_image(f"plate{i:02d}", path, ch, fr(ini))
        st.frame_final_end = fr(fin)
        st.blend_type = "ALPHA_OVER"
        for t_ in (ini, fin):
            u_ = (t_ - ini) / (fin - ini)
            z = 1.0 + pl.get("zoom", ZOOM) * (u_ if i % 2 else 1.0 - u_)
            st.transform.scale_x = st.transform.scale_y = z
            st.transform.keyframe_insert("scale_x", frame=fr(t_))
            st.transform.keyframe_insert("scale_y", frame=fr(t_))
        strips = [bgs, st]
    pa = []
    if j > 0:
        pa += [(ini, 0.0), (ini + XF, 1.0)]
    elif e > 1:
        pa += [(ini, 0.0), (ini + DIP, 1.0)]
    if j == n - 1 and e < len(PLAN["scenes"]):
        pa += [(fin - DIP, 1.0), (fin, 0.0)]
    if pa:
        for s_ in strips:
            alpha(s_, pa)

    if j > 0 or e > 1:
        if j == 0 or SFX_FULL:
            EVENTS.append((ini, "whoosh" if j == 0 else "tick2"))

    # inset: a second picture on the plate (a locator, a detail, a comparison), so a plate is never one photo and one label
    #   "inset": {"file": "stock/x.jpg", "pos": [0.5, 0.27], "width": 0.5}
    ins = pl.get("inset")
    if ins:
        ipath, _ = compose_layer({"type": "contain", "radius": 22, **ins}, f"i{i}")
        i0, i1 = a + 0.7, b - 0.15
        if i1 - i0 > 0.8:
            ist = S.new_image(f"inset{i:02d}", ipath, 12 + (i % 2), fr(i0))
            ist.frame_final_end = fr(i1)
            ist.blend_type = "ALPHA_OVER"
            fade(ist, i0, i1)
            if SFX_FULL:
                EVENTS.append((i0, "tick"))

    # callouts (they appear after the card is in, one after another)
    for ci, co in enumerate(pl.get("callouts", [])):
        tgt = (co["target"][0] * W, co["target"][1] * H)
        txt = co["text"]
        size = 40                                        # legible on a phone (Style: text >= 40 px)
        bw = int(len(txt) * size * 0.56 + 44)
        bh = 72
        lxy = (co["label"][0] * W - bw / 2, co["label"][1] * H - bh / 2)
        lxy = (min(max(lxy[0], 24), W - bw - 24), min(max(lxy[1], 24), round(H * CAP_Y) - 90 - bh))      # never in the caption zone (the card sits below the captions, so labels above them never meet it)
        c0t = cue_time(co["at"], e, pl["file"]) if co.get("at") else a + 1.0 + 0.6 * ci   # `at`: on the word that names the part
        c1t = b - 0.15
        if c1t - c0t < 1.0:
            continue
        cs = S.new_image(f"callout{i:02d}-{ci}", callout_image(tgt, lxy, bw, bh, f"{i}_{ci}"), 20 + ci, fr(c0t))   # own channel: overlapping strips on one channel get bumped into the card's channels
        cs.frame_final_end = fr(c1t)
        if SFX_FULL:
            EVENTS.append((c0t, "tick"))
        cs.blend_type = "ALPHA_OVER"
        fade(cs, c0t, c1t)
        add_text(f"co{i}-{ci}", txt, F_BODY, size, INK, 24 + ci, c0t, c1t, lxy[0] + 22, lxy[1] + bh / 2, rise=False)

    # card: three kinds (see System/Style.md)
    #   context (list or {"kind": "context", "card": [label, title, detail]}): label, title, detail
    #   number  {"kind": "number", "value": "1.1°", "caption": "twist angle", "source": "Nature, 2018"}
    #   note    {"kind": "note", "text": "Yes, the stuff in your pencil."}   (a short aside in the narrator's voice)
    card = pl.get("card")
    if card:
        kind = card.get("kind", "context") if isinstance(card, dict) else "context"
        t0, t1 = (cue_time(card["at"], e, pl["file"]) if isinstance(card, dict) and card.get("at") else a + 0.45), b - 0.15
        if SFX_FULL:
            EVENTS.append((t0, "ping"))
        cd = S.new_image(f"card{i:02d}", CARD_PNG, 7, fr(t0))
        cd.frame_final_end = fr(t1)
        cd.blend_type = "ALPHA_OVER"
        fade(cd, t0, t1)
        for t_, off in ((t0, -24), (t0 + 0.25, 0)):
            cd.transform.offset_y = off
            cd.transform.keyframe_insert("offset_y", frame=fr(t_))
        x = CX0 + 8 + 36
        if kind == "context":
            etq, tit, det = card if isinstance(card, list) else card["card"]
            add_text(f"etq{i}", spaced(etq), F_BODY, 32, COPPER + (1.0,), 8, t0, t1, x, CY - 0.050 * H)
            add_text(f"tit{i}", tit, F_TITLE, 56, INK, 9, t0, t1, x, CY - 0.001 * H)
            add_text(f"det{i}", det, F_BODY, 34, INK_SOFT, 10, t0, t1, x, CY + 0.047 * H)
        elif kind == "number":
            add_text(f"val{i}", card["value"], F_TITLE, 124, COPPER + (1.0,), 8, t0, t1, x, CY - 0.036 * H)
            add_text(f"cap{i}", card["caption"], F_TITLE, 44, INK, 9, t0, t1, x, CY + 0.021 * H)
            add_text(f"src{i}", card.get("source", ""), F_BODY, 30, INK_SOFT, 10, t0, t1, x, CY + 0.056 * H)
        elif kind == "note":
            words, lines = card["text"].split(), [""]
            for w_ in words:                                   # wrap to two lines of about 30 characters
                if len(lines[-1]) + len(w_) > 30 and len(lines) < 2:
                    lines.append("")
                lines[-1] = (lines[-1] + " " + w_).strip()
            add_text(f"etq{i}", spaced("Margin note"), F_BODY, 30, COPPER + (1.0,), 8, t0, t1, x, CY - 0.050 * H)
            add_text(f"nt{i}a", lines[0], F_TITLE, 46, INK, 9, t0, t1, x, CY - 0.002 * H)
            add_text(f"nt{i}b", lines[1] if len(lines) > 1 else "", F_TITLE, 46, INK, 10, t0, t1, x, CY + 0.048 * H)


# ---------------------------------------------------------------- word-by-word captions
def write_srt(placed, per_cue=5):
    """render/<prefix>.srt: the same words in cues of `per_cue` words, to upload as a caption track (search, translation, accessibility)."""
    ts = lambda t: f"{int(t // 3600):02d}:{int(t % 3600 // 60):02d}:{int(t % 60):02d},{int(t % 1 * 1000):03d}"
    out = []
    for k in range(0, len(placed), per_cue):
        c = placed[k:k + per_cue]
        end = min(c[-1][2], placed[k + per_cue][1]) if k + per_cue < len(placed) else c[-1][2]
        out.append(f"{k // per_cue + 1}\n{ts(c[0][1])} --> {ts(max(end, c[0][1] + 0.3))}\n{' '.join(x[0] for x in c)}\n")
    open(f"{OUT}/{PLAN['prefix']}.srt", "w", encoding="utf-8").write("\n".join(out))


def add_captions():
    if not PLACED:
        return
    placed = [w[:3] for w in PLACED]
    write_srt(placed)
    shown = []                                           # a word on screen for under 0.09 s (2 frames) shares its caption with the next ("IT IS")
    for i_, (w, s, e) in enumerate(placed):
        short = i_ + 1 < len(placed) and placed[i_ + 1][1] - s < 0.09
        if shown and shown[-1][3] and len(shown[-1][0]) + len(w) <= 14:
            shown[-1] = [shown[-1][0] + " " + w, shown[-1][1], e, short]
        else:
            shown.append([w, s, e, short])
    placed = [x[:3] for x in shown]
    n = 0
    for i_, (w, s, e) in enumerate(placed):
        nxt = placed[i_ + 1][1] if i_ + 1 < len(placed) else T_END
        end = min(nxt, e + CAP_GAP, T_END)                 # hold until the next word, but not across a long pause
        if fr(end) <= fr(s):
            continue
        tx = S.new_effect(f"cap{n:03d}", "TEXT", CAP_CH, fr(s), length=fr(end) - fr(s))
        tx.text = w.upper()
        tx.font, tx.font_size = F_TITLE, min(CAP_SIZE, int(1300 / max(len(w), 1)))   # long words shrink to fit the frame
        key = any(c.isdigit() for c in w) or "".join(c for c in w.lower() if c.isalnum()) in KEYWORDS   # figures and plan.keywords are copper
        tx.color = COPPER + (1.0,) if key else (1.0, 1.0, 1.0, 1.0)
        tx.anchor_x, tx.anchor_y = "CENTER", "CENTER"
        tx.location = (0.5, 1 - CAP_Y)
        tx.use_outline, tx.outline_color, tx.outline_width = True, (0.04, 0.035, 0.03, 1.0), 0.14
        tx.use_shadow, tx.shadow_color, tx.shadow_offset, tx.shadow_blur = True, (0, 0, 0, 0.55), 0.04, 0.03
        n += 1
    print("CAPTIONS", n, "words,", "timed by whisper" if any(os.path.exists(os.path.splitext(v["f"])[0].replace("/_padded", "") + ".words.json") for v in voices) else "estimated")

add_captions()


# ---------------------------------------------------------------- sound design (synthesized, deterministic)
def synth_sound(sr=48000):
    """Returns (sfx, bed) float arrays: events from EVENTS, and a quiet drone. Everything is numpy; levels are low and unheard by the agent."""
    n = int((T_END + 1.0) * sr)
    sfx, bed = np.zeros(n, np.float32), np.zeros(n, np.float32)
    rng = np.random.default_rng(11)
    sn = PLAN.get("sound", {})

    def put(t0, x):
        i0 = max(0, int(t0 * sr))
        x = x[: max(0, n - i0)]
        sfx[i0:i0 + len(x)] += x

    def env(L, a, tau):
        t = np.arange(L) / sr
        return np.minimum(t / max(a, 1e-4), 1.0) * np.exp(-t / tau)

    def lowpass(x, k):
        c = np.cumsum(np.pad(x, (k, 0)))
        return (c[k:] - c[:-k]) / k

    for t_, kind in EVENTS:
        if kind == "thump":                                       # opening hit: a short sub tone
            L = int(0.55 * sr); t = np.arange(L) / sr
            put(max(0.0, t_ - 0.02), (np.sin(2 * np.pi * (58 - 18 * t) * t) * env(L, 0.004, 0.16) * 0.22).astype(np.float32))
        elif kind in ("whoosh", "tick2"):                         # a soft filtered-noise sweep that ends on the cut
            L = int((0.42 if kind == "whoosh" else 0.22) * sr)
            z = rng.standard_normal(L).astype(np.float32)
            low, hp = lowpass(z, 60), z - lowpass(z, 12)
            u = np.linspace(0, 1, L, dtype=np.float32)
            sweep = low * (1 - u) * 4.0 + hp * u * 0.9
            sh = np.sin(np.pi * u) ** 2
            put(t_ - L / sr * 0.7, (sweep * sh * (0.075 if kind == "whoosh" else 0.04)).astype(np.float32))
        elif kind == "ping":                                      # a card arrives: two soft partials
            L = int(0.7 * sr); t = np.arange(L) / sr
            x = (np.sin(2 * np.pi * 880 * t) + 0.6 * np.sin(2 * np.pi * 1320 * t)) * env(L, 0.006, 0.17)
            put(t_, (x * 0.055).astype(np.float32))
        elif kind == "tick":                                      # a callout arrives: a tiny click
            L = int(0.06 * sr); t = np.arange(L) / sr
            x = np.sin(2 * np.pi * 2600 * t) * np.exp(-t / 0.007) + 0.3 * rng.standard_normal(L) * np.exp(-t / 0.002)
            put(t_, (x * 0.05).astype(np.float32))
    if sn.get("bed", False):                                      # legacy drone bed (A minor sine; phones barely play it): opt-in only
        t = np.arange(n) / sr
        for f_, a_, ph in ((110.0, 1.0, 0.0), (164.81, 0.6, 1.3), (220.0, 0.5, 2.1), (329.63, 0.25, 0.7)):
            lfo = 0.75 + 0.25 * np.sin(2 * np.pi * (0.07 + 0.013 * f_ / 110) * t + ph)
            bed += (a_ * lfo * (np.sin(2 * np.pi * f_ * t) + 0.18 * np.sin(2 * np.pi * 2 * f_ * t))).astype(np.float32)
        bed *= 0.012
        bed *= np.minimum(t / 1.2, 1.0) * np.clip((T_END + 0.8 - t) / 1.6, 0.0, 1.0)
    return sfx * sn.get("sfx_gain", 1.0), bed * sn.get("bed_gain", 1.0)


def add_sound():
    sn = PLAN.get("sound")
    if not sn:
        return
    import wave
    sfx, bed = synth_sound()
    for name, arr, ch in (("sfx", sfx, 31), ("bed", bed, 32)):
        path = f"{FX}/sound_{name}.wav"
        if not np.any(arr) or (name == "sfx" and not sn.get("sfx", True)):
            if os.path.exists(path):
                os.remove(path)                              # a stale stem must not reach mix_audio.py
            continue
        a = np.clip(arr, -0.9, 0.9)
        with wave.open(path, "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(48000)
            w.writeframes((a * 32767).astype("<i2").tobytes())
        S.new_sound(f"sound-{name}", path, ch, 1)
        print(f"SOUND {name}: {len(a) / 48000:.1f} s, peak {np.abs(a).max():.3f}, rms {np.sqrt((a ** 2).mean()):.4f}")


add_sound()

# ---------------------------------------------------------------- vignette and grain
yy2, xx2 = np.mgrid[0:H, 0:W].astype(np.float32)
r = np.sqrt(((xx2 - W / 2) / (W / 2)) ** 2 + ((yy2 - H / 2) / (H / 2)) ** 2)
vig = np.clip(1.0 - 0.45 * np.clip(r - 0.55, 0, None) ** 1.6, 0.0, 1.0)
grain = np.clip(0.5 + np.random.default_rng(7).normal(0, 0.12, (H, W)).astype(np.float32), 0, 1)


def gray_png(name, g):
    return save_rgba(np.dstack([g, g, g, np.ones_like(g)]).astype(np.float32), name)


dur = fr(T_END)
vs = S.new_image("vignette", gray_png("vignette", vig), 14, 1)
vs.frame_final_end = dur
vs.blend_type, vs.blend_alpha = "MULTIPLY", VIGNETTE
gs = S.new_image("grain", gray_png("grain", grain), 15, 1)
gs.frame_final_end = dur
gs.blend_type, gs.blend_alpha = "OVERLAY", GRAIN

# ---------------------------------------------------------------- render
sc.frame_start, sc.frame_end = 1, dur
rd = sc.render
rd.image_settings.media_type = "VIDEO"
rd.image_settings.file_format = "FFMPEG"
rd.ffmpeg.format, rd.ffmpeg.codec = "MPEG4", "H264"
rd.ffmpeg.constant_rate_factor, rd.ffmpeg.ffmpeg_preset = "HIGH", "GOOD"
rd.ffmpeg.audio_codec, rd.ffmpeg.audio_bitrate, rd.ffmpeg.audio_channels = "AAC", 192, "STEREO"
name = f"{PLAN['prefix']}-{round(T_END)}s-9x16-r{PLAN.get('render', 1)}"
rd.filepath = f"{OUT}/{name}.mp4"
bpy.ops.wm.save_as_mainfile(filepath=f"{OUT}/{PLAN['prefix']}-{round(T_END)}s.blend")
TIMELINE["voices"] = [{"file": v["f"], "in": v["ini"], "at": v["abs"], "dur": v["dur"]} for v in voices]   # read by mix_audio.py
TIMELINE["events"] = sorted([round(float(t_), 3), k_] for t_, k_ in EVENTS)
TIMELINE["stems"] = {n_: f"{FX}/sound_{n_}.wav" for n_ in ("sfx", "bed") if os.path.exists(f"{FX}/sound_{n_}.wav") and PLAN.get("sound")}
TIMELINE["render"] = rd.filepath
json.dump(TIMELINE, open(f"{OUT}/_timeline.json", "w", encoding="utf-8"), indent=1)   # read by motion.py and mix_audio.py
print("DURATION", round(T_END, 2), "s;", dur, "frames;", name)
for v in voices:
    print("voice", v["n"], f"timeline {v['abs']:.2f} -> {v['abs'] + v['dur']:.2f}",
          f"| speech starts {v['abs'] + v['a'] - v['ini']:.2f}, ends {v['abs'] + v['b'] - v['ini']:.2f}")
print("BOUNDARIES", [round(float(b), 2) for b in B])


def check_voices():
    """Checks that every voice is placed complete (Blender's background mixdown is silent, so the strips are checked directly):
    the strip covers the whole speech plus the silence kept around it, nothing overlaps, and the padded file really has a silent lead-in."""
    bad = 0
    prev_end = 0.0
    for v in voices:
        st = v["strip"]
        c0 = st.frame_offset_start / FPS                                  # first second of the file that is played
        c1 = c0 + (st.frame_final_end - st.frame_final_start) / FPS       # last second of the file that is played
        env, _ = envelope(v["f"])
        lead_silent = env[: max(1, int(v["a"] * 100) - 1)].max() < 0.01 * env.max()
        covers = c0 <= v["a"] - 0.09 and c1 >= v["b"] + 0.24
        starts_ok = abs(st.frame_final_start / FPS - v["abs"]) < 1.0 / FPS
        no_overlap = v["abs"] >= prev_end - 1e-6
        prev_end = v["abs"] + v["dur"]
        ok = lead_silent and covers and starts_ok and no_overlap
        bad += not ok
        print(f"CHECK voice {v['n']}: plays file {c0:.2f}-{c1:.2f} s, speech {v['a']:.2f}-{v['b']:.2f} s | "
              f"lead-in {'ok' if v['a'] - c0 >= 0.09 else 'TOO SHORT'}, tail {'ok' if c1 - v['b'] >= 0.24 else 'TOO SHORT'}, "
              f"padded file lead {'silent' if lead_silent else 'NOT silent'}, order {'ok' if no_overlap else 'OVERLAP'}")
    print("CHECK RESULT", "all voices complete" if not bad else f"{bad} voice(s) need attention")


if os.environ.get("CHECK") == "1":
    check_voices()
if os.environ.get("SOLO_PROYECTO") != "1":
    bpy.ops.render.render(animation=True)
    print("DONE", rd.filepath)
