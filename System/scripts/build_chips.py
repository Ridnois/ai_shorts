"""Assembles "Chips and lithography" (vertical 9:16 Short, ≈ 93 s) in Blender 5.2's sequencer.

    SOLO_PROYECTO=1 blender -b --factory-startup --python System/scripts/build_chips.py   # assembles and measures
    blender -b --factory-startup --python System/scripts/build_chips.py                  # assembles and renders
Base: build_queque.py. 7 voices, 8 plates (2 in scene 5), label cards on scenes 1 to 6. Narration and on-screen
text are Spanish (made before the English-only decision); for English videos change `TEXTOS` and the voice files.
Media folder: Media/Legacy/Chips - 85 segundos/ (voz/, ilustraciones/, render/).
"""
import os

import aud
import bpy
import numpy as np

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "Media", "Legacy", "Chips - 85 segundos")
VOZ, ILU, OUT = (f"{ROOT}/{d}" for d in ("voz", "ilustraciones", "render"))
FX = f"{OUT}/_fx"
FPS, W, H = 24, 1080, 1920

GAPS = [0.45, 0.45, 0.45, 0.45, 0.45, 1.20]     # silence between voices; longer before the close
INICIO_VOZ, COLA = 0.50, 1.20
PAD_INI, PAD_FIN = 0.08, 0.25
DIP, XF, ZOOM = 0.20, 0.30, 0.05
PAPEL = (0.945, 0.935, 0.86)
VIGNETA, GRANO = 0.20, 0.08
VOL_VOZ = 1.0

# image -> file ; plates per scene (add up to 8)
ARCH = {1: "chips-i01-v1.png", 2: "chips-i02-v1.png", 3: "chips-i03-v1.png", 4: "chips-i04-v2.png",
        5: "chips-i05-v1.png", 6: "chips-i06-v1.png", 7: "chips-i07-v1.png", 8: "chips-i08-v1.png"}
POR_ESCENA = [1, 1, 1, 1, 2, 1, 1]
OFF_X = {2: -300}            # the photo is landscape: it is shifted so the machine and the figure stay in
ZOOM_IMG = {2: 0.0}          # no push: the side crop is already tight
# (label, title): see "On-screen text style"
TEXTOS = {1: ("Canon · Texas", "Septiembre de 2024"), 2: ("ASML", "Único proveedor de EUV"),
          3: ("TSMC · est. 2.º trim. 2026", "72,5 % del mercado"), 4: ("EE. UU. · China · Japón", "Una disputa por máquinas"),
          5: ("Según Canon", "5 nm hoy · 2 nm meta"), 6: ("2 nm", "Meta, no logro")}

sc = bpy.context.scene
sc.render.fps = FPS
sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = W, H, 100
sc.view_settings.view_transform = "Standard"
sc.sequence_editor_create()
S = sc.sequence_editor.strips
bpy.context.preferences.edit.keyframe_new_interpolation_type = "LINEAR"
fr = lambda t: round(t * FPS)


def analiza(path):
    s = aud.Sound.file(path)
    rate = s.specs[0]
    a = np.abs(np.asarray(s.data(), dtype=np.float32))
    a = a.mean(axis=1) if a.ndim > 1 else a
    win = int(rate * 0.01)
    n = len(a) // win
    env = a[: n * win].reshape(n, win).mean(axis=1)
    v = np.nonzero(env > env.max() * 0.03)[0]
    return v[0] * 0.01, (v[-1] + 1) * 0.01, len(a) / rate


voces, t = [], INICIO_VOZ
for n in range(1, 8):
    f = f"chips-e{n}-voz-v1.mp3"
    a, b, total = analiza(f"{VOZ}/{f}")
    ini, fin = max(0.0, a - PAD_INI), min(total, b + PAD_FIN)
    voces.append({"n": n, "f": f, "ini": ini, "fin": fin, "abs": t, "dur": fin - ini})
    t += (fin - ini) + (GAPS[n - 1] if n < 7 else 0)
B = [0.0] + [v["abs"] + v["dur"] + GAPS[i] / 2 for i, v in enumerate(voces[:6])] + [voces[6]["abs"] + voces[6]["dur"] + COLA]
T_FIN = B[7]

for v in voces:
    # the strip is created `ini` earlier: frame_offset_start also advances the visible start
    st = S.new_sound(f"voz-e{v['n']}", f"{VOZ}/{v['f']}", 30, fr(v["abs"]) - fr(v["ini"]))
    st.frame_offset_start = fr(v["ini"])
    st.frame_final_end = fr(v["abs"]) + fr(v["dur"])
    st.volume = VOL_VOZ
    assert st.frame_final_start == fr(v["abs"]), (v["n"], st.frame_final_start, fr(v["abs"]))
    v["strip"] = st

papel = S.new_effect("papel", "COLOR", 1, 1, length=fr(T_FIN))
papel.color = PAPEL


def alfa(st, puntos):
    vistos = {}
    for t_, val in puntos:
        vistos[fr(t_)] = val
    for f_ in sorted(vistos):
        st.blend_alpha = vistos[f_]
        st.keyframe_insert("blend_alpha", frame=f_)


# ---------------------------------------------------------------- plates
idx, esc_img = 1, []
for e, n in enumerate(POR_ESCENA, start=1):
    t0, t1 = B[e - 1], B[e]
    seg = (t1 - t0) / n
    for j in range(n):
        esc_img.append((idx, e, j, n, t0 + j * seg, t0 + (j + 1) * seg))
        idx += 1

for i, e, j, n, a, b in esc_img:
    ini = a - (XF / 2 if j > 0 else 0)
    fin = b + (XF / 2 if j < n - 1 else 0)
    st = S.new_image(f"i{i:02d}", f"{ILU}/{ARCH[i]}", 2 + (j % 2), fr(ini))
    st.frame_final_end = fr(fin)
    w, h = st.elements[0].orig_width, st.elements[0].orig_height
    k = max(W / w, H / h) * 1.07                                   # leaves room to raise the drawing without leaving gaps
    st.transform.scale_x = st.transform.scale_y = k
    st.transform.offset_x = OFF_X.get(i, 0)
    st.transform.offset_y = 60                                      # raises the drawing: the card does not cover the subject
    for t_ in (ini, fin):                                           # slow push
        z = 1.0 + ZOOM_IMG.get(i, ZOOM) * (t_ - ini) / (fin - ini)
        st.transform.scale_x = st.transform.scale_y = k * z
        st.transform.keyframe_insert("scale_x", frame=fr(t_))
        st.transform.keyframe_insert("scale_y", frame=fr(t_))
    pa = []
    if j > 0:
        pa += [(ini, 0.0), (ini + XF, 1.0)]                         # cross-fade within the scene
    elif e > 1:
        pa += [(ini, 0.0), (ini + DIP, 1.0)]                        # "page turn"
    if j == n - 1 and e < 7:
        pa += [(fin - DIP, 1.0), (fin, 0.0)]
    if pa:
        alfa(st, pa)

# ---------------------------------------------------------------- label card (On-screen text style)
os.makedirs(FX, exist_ok=True)
CX0, CX1 = 56, 56 + 894                                   # 56 px left margin; 130 px free on the right (Shorts buttons)
CY = H * (1 - 0.275)                                      # centre between 22 and 33 % of the height from the bottom
CY0, CY1 = CY - 105, CY + 105
RAD = 16
COBRE = (0.78, 0.42, 0.22)
yy_, xx_ = np.mgrid[0:H, 0:W].astype(np.float32)
dx = np.maximum(np.maximum(CX0 + RAD - xx_, xx_ - (CX1 - RAD)), 0)
dy = np.maximum(np.maximum(CY0 + RAD - yy_, yy_ - (CY1 - RAD)), 0)
dist = np.sqrt(dx ** 2 + dy ** 2) - RAD                   # <0 inside the rounded card
dentro = np.clip(0.5 - dist, 0, 1)
borde = np.clip(1.0 - np.abs(dist + 0.5), 0, 1) * 0.25
barra = ((xx_ >= CX0) & (xx_ < CX0 + 8)).astype(np.float32) * dentro
rgba = np.zeros((H, W, 4), dtype=np.float32)
papel = np.array([0.976, 0.965, 0.933], dtype=np.float32)
graf = np.array([0.20, 0.19, 0.18], dtype=np.float32)
for c in range(3):
    base = papel[c] * (1 - borde) + graf[c] * borde
    rgba[..., c] = base * (1 - barra) + COBRE[c] * barra
rgba[..., 3] = np.maximum(dentro * 0.94, borde * dentro)
tarjeta = bpy.data.images.new("tarjeta", W, H, alpha=True)
tarjeta.pixels.foreach_set(rgba[::-1].ravel())            # Blender stores bottom to top
tarjeta.filepath_raw = f"{FX}/tarjeta.png"
tarjeta.file_format = "PNG"
tarjeta.save()

F_TIT = bpy.data.fonts.load("/usr/share/fonts/truetype/noto/NotoSansDisplay-Bold.ttf")
F_ETQ = bpy.data.fonts.load("/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf")
TINTA = (0.11, 0.10, 0.09, 1.0)
HAIR = "\u200a"
espaciado = lambda t: HAIR.join(t.upper().replace(" ", "  "))    # label in capitals with wide spacing


def entra(st, prop_alfa, t0, t1):
    alfa(st, [(t0, 0.0), (t0 + 0.25, 1.0), (t1 - 0.20, 1.0), (t1, 0.0)])


for e, (etq, tit) in TEXTOS.items():
    t0, t1 = B[e - 1] + 0.5, B[e] - 0.15
    cd = S.new_image(f"tarjeta-{e}", f"{FX}/tarjeta.png", 5, fr(t0))
    cd.frame_final_end = fr(t1)
    entra(cd, "blend_alpha", t0, t1)
    for t_, off in ((t0, -24), (t0 + 0.25, 0)):                    # 24 px rise on entering
        cd.transform.offset_y = off
        cd.transform.keyframe_insert("offset_y", frame=fr(t_))
    for nombre, txt, font, size, col, y in ((f"etq-{e}", espaciado(etq), F_ETQ, 34, COBRE + (1.0,), 0.307),
                                            (f"tit-{e}", tit, F_TIT, 58, TINTA, 0.250)):
        tx = S.new_effect(nombre, "TEXT", 6 if "etq" in nombre else 7, fr(t0), length=fr(t1 - t0))
        tx.text, tx.font_size, tx.font, tx.color = txt, size, font, col
        tx.anchor_x, tx.anchor_y = "LEFT", "CENTER"
        x_txt = (CX0 + 8 + 36) / W
        for t_, dy_ in ((t0, -24 / H), (t0 + 0.25, 0.0)):
            tx.location = (x_txt, y + dy_)
            tx.keyframe_insert("location", frame=fr(t_))
        entra(tx, "blend_alpha", t0, t1)

# ---------------------------------------------------------------- vignette and grain
yy2, xx2 = np.mgrid[0:H, 0:W].astype(np.float32)
r = np.sqrt(((xx2 - W / 2) / (W / 2)) ** 2 + ((yy2 - H / 2) / (H / 2)) ** 2)
vig = np.clip(1.0 - 0.45 * np.clip(r - 0.55, 0, None) ** 1.6, 0.0, 1.0)
grano = np.clip(0.5 + np.random.default_rng(7).normal(0, 0.12, (H, W)).astype(np.float32), 0, 1)


def guarda(nombre, gris):
    im = bpy.data.images.new(nombre, W, H, alpha=False)
    im.pixels.foreach_set(np.dstack([gris, gris, gris, np.ones_like(gris)]).astype(np.float32).ravel())
    im.filepath_raw = f"{FX}/{nombre}.png"
    im.file_format = "PNG"
    im.save()
    return im.filepath_raw


dur = fr(T_FIN)
vs = S.new_image("viñeta", guarda("viñeta", vig), 14, 1)
vs.frame_final_end = dur
vs.blend_type, vs.blend_alpha = "MULTIPLY", VIGNETA
gs = S.new_image("grano", guarda("grano", grano), 15, 1)
gs.frame_final_end = dur
gs.blend_type, gs.blend_alpha = "OVERLAY", GRANO

# ---------------------------------------------------------------- render
sc.frame_start, sc.frame_end = 1, dur
rd = sc.render
rd.image_settings.media_type = "VIDEO"
rd.image_settings.file_format = "FFMPEG"
rd.ffmpeg.format, rd.ffmpeg.codec = "MPEG4", "H264"
rd.ffmpeg.constant_rate_factor, rd.ffmpeg.ffmpeg_preset = "HIGH", "GOOD"
rd.ffmpeg.audio_codec, rd.ffmpeg.audio_bitrate, rd.ffmpeg.audio_channels = "AAC", 192, "STEREO"
rd.filepath = f"{OUT}/chips-93s-9x16-r1.mp4"
bpy.ops.wm.save_as_mainfile(filepath=f"{OUT}/chips-93s.blend")
print("DURACION", round(T_FIN, 2), "s;", dur, "fotogramas")
for v in voces:
    st = v["strip"]
    print("voz", v["n"], round(v["abs"], 2), "->", round(v["abs"] + v["dur"], 2),
          f"| se oye {(st.frame_final_start - st.frame_start) / FPS:.2f}-{(st.frame_final_end - st.frame_start) / FPS:.2f} s del archivo; útil {v['ini'] + PAD_INI:.2f}-{v['fin'] - PAD_FIN:.2f}")
print("FRONTERAS", [round(b, 2) for b in B])
if os.environ.get("SOLO_PROYECTO") != "1":
    bpy.ops.render.render(animation=True)
    print("LISTO", rd.filepath)
