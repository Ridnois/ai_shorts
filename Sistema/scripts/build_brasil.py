"""Monta "Brasil y embajadas" (Short vertical 9:16, ~60 s) en el secuenciador de Blender 5.2.

Uso (desde la carpeta del video):
    SOLO_PROYECTO=1 blender -b --factory-startup --python render/build_brasil.py   # solo arma y mide
    blender -b --factory-startup --python render/build_brasil.py                  # arma y renderiza
Salida: render/brasil-60s-9x16-r3.mp4 y render/brasil-60s.blend
Base: build_helio.py (mismas transiciones: "pasar la hoja", empuje lento, viñeta y grano).
"""
import array
import os
import wave

import bpy
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOZ, AUD, ILU, OUT = (f"{ROOT}/{d}" for d in ("voz", "audio", "ilustraciones", "render"))
FX = f"{OUT}/_fx"
FPS, W, H = 24, 1080, 1920                      # vertical, Shorts

GAPS = [0.45, 0.45, 0.50, 1.20, 0.50, 0.50]     # silencio entre voces; 0,7 s antes de la escena 5 (la pregunta)
INICIO_VOZ, COLA = 0.50, 1.20
PAD_INI, PAD_FIN = 0.08, 0.25                   # recorte de silencios de cada toma de voz
DIP, ZOOM = 0.20, 0.06
PAPEL = (0.914, 0.913, 0.876)    # papel de las láminas v3 medido en sRGB; el efecto COLOR lo toma tal cual
VIGNETA, GRANO = 0.22, 0.08
VOL_VOZ, VOL_MAZO, VOL_ESCUELA = 1.0, 0.55, 0.22
MAZO_EN = 3.0                                    # s dentro de la voz 2 ("condenado"), estimado sin tiempos por palabra

sc = bpy.context.scene
sc.render.fps = FPS
sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = W, H, 100
sc.view_settings.view_transform = "Standard"      # AgX (por defecto) apaga el color del papel
sc.sequence_editor_create()
S = sc.sequence_editor.strips
bpy.context.preferences.edit.keyframe_new_interpolation_type = "LINEAR"
fr = lambda t: round(t * FPS)


def analiza(path):
    w = wave.open(path)
    sr = w.getframerate()
    a = array.array("h")
    a.frombytes(w.readframes(w.getnframes()))
    win = int(sr * 0.01)
    env = [sum(abs(x) for x in a[i:i + win]) / win for i in range(0, len(a) - win, win)]
    v = [i for i, e in enumerate(env) if e > max(env) * 0.03]
    return v[0] * 0.01, (v[-1] + 1) * 0.01


voces, t = [], INICIO_VOZ
for n in range(1, 8):
    f = f"brasil-e{n}-voz-qwen-clone-v1.wav"
    a, b = analiza(f"{VOZ}/{f}")
    ini, fin = max(0.0, a - PAD_INI), b + PAD_FIN
    voces.append({"n": n, "f": f, "ini": ini, "fin": fin, "abs": t, "dur": fin - ini})
    t += (fin - ini) + (GAPS[n - 1] if n < 7 else 0)
B = [0.0] + [v["abs"] + v["dur"] + GAPS[i] / 2 for i, v in enumerate(voces[:6])] + [voces[6]["abs"] + voces[6]["dur"] + COLA]
T_FIN = B[7]

for v in voces:
    # frame_offset_start también adelanta el inicio visible: la tira se crea `ini` antes para que
    # lo audible empiece en `abs` y termine en `abs + dur` (si no, se corta el final de la frase)
    st = S.new_sound(f"voz-e{v['n']}", f"{VOZ}/{v['f']}", 30, fr(v["abs"]) - fr(v["ini"]))
    st.frame_offset_start = fr(v["ini"])
    st.frame_final_end = fr(v["abs"]) + fr(v["dur"])
    st.volume = VOL_VOZ
    assert st.frame_final_start == fr(v["abs"]), (v["n"], st.frame_final_start, fr(v["abs"]))
    v["strip"] = st

# papel de fondo (se ve en "pasar la hoja" y donde se recorta la imagen)
papel = S.new_effect("papel", "COLOR", 1, 1, length=fr(T_FIN))
papel.color = PAPEL

# (id, archivo, inicio, fin, acercamiento base, dirección del empuje)
# Láminas v3: una sola lámina por escena, sin dibujos secundarios; el acercamiento llena mejor el cuadro.
tomas = [
    ("e1", "brasil-e1-v3.png", B[0], B[1], 1.00, +1),
    ("e2", "brasil-e2-v4.png", B[1], B[2], 0.96, +1),
    ("e3", "brasil-e3-v3.png", B[2], B[3], 1.00, +1),
    ("e4", "brasil-e4-v3.png", B[3], B[4], 1.00, +1),
    ("e5", "brasil-e5-v3.png", B[4], B[5], 0.96, +1),
    ("e6", "brasil-e6-v3.png", B[5], B[6], 0.98, +1),
    ("e1b", "brasil-e1-v3.png", B[6], B[7], 1.00, -1),         # cierre: vuelve a la urna
]


def alfa(st, puntos):
    vistos = {}
    for t_, val in puntos:
        vistos[fr(t_)] = val
    for f_ in sorted(vistos):
        st.blend_alpha = vistos[f_]
        st.keyframe_insert("blend_alpha", frame=f_)


def img(nombre, fn, canal, t0, t1, zoom):
    st = S.new_image(nombre, f"{ILU}/{fn}", canal, fr(t0))
    st.frame_final_end = fr(t1)
    w, h = st.elements[0].orig_width, st.elements[0].orig_height
    k = max(W / w, H / h) * zoom
    st.transform.scale_x = st.transform.scale_y = k
    if nombre not in ("e1", "e1b"):
        st.transform.offset_y = 90                  # sube el dibujo: foco entre el 15 y el 60 % de la altura
    return st, k


def empuje(st, k, t0, t1, d):
    f = lambda t_: 1.0 + ZOOM * ((t_ - t0) / (t1 - t0) if d > 0 else 1 - (t_ - t0) / (t1 - t0))
    for t_ in (t0, t1):
        st.transform.scale_x = st.transform.scale_y = k * f(t_)
        st.transform.keyframe_insert("scale_x", frame=fr(t_))
        st.transform.keyframe_insert("scale_y", frame=fr(t_))


for tid, fn, t0, t1, arriba, d in tomas:
    st, k = img(tid, fn, 2, t0, t1, arriba)
    empuje(st, k, t0, t1, d)
    pa = []
    if tid != "e1":
        pa += [(t0, 0.0), (t0 + DIP, 1.0)]
    if tid != "e1b":
        pa += [(t1 - DIP, 1.0), (t1, 0.0)]
    if pa:
        alfa(st, pa)

# texto en pantalla (cifras que salieron del guion); arriba de la zona de subtítulos
FUENTE = bpy.data.fonts.load("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")


def texto(nombre, s, t0, t1, y=0.27):
    tx = S.new_effect(nombre, "TEXT", 6, fr(t0), length=fr(t1 - t0))
    tx.text, tx.font_size, tx.font = s, 96, FUENTE
    tx.color = (0.10, 0.09, 0.08, 1.0)
    tx.location = (0.5, y)
    tx.anchor_x, tx.anchor_y = "CENTER", "CENTER"
    tx.use_shadow, tx.shadow_color = True, (0.95, 0.92, 0.84, 0.6)
    alfa(tx, [(t0, 0.0), (t0 + 0.25, 1.0), (t1 - 0.25, 1.0), (t1, 0.0)])


texto("tx-2", "27 años · 4 a 1", B[1] + 0.8, B[2] - 0.2)
texto("tx-3", "580 días · 2021", B[2] + 0.8, B[3] - 0.2)
texto("tx-4", "2020 → 2022", B[3] + 0.8, B[4] - 0.2)
texto("tx-6", "47 detenidos", B[5] + 1.0, B[6] - 0.2)

# viñeta y grano
os.makedirs(FX, exist_ok=True)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
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


def rampa(st, puntos):
    for f_, val in puntos:
        st.volume = val
        st.keyframe_insert("volume", frame=f_)


def sfx(nombre, fn, canal, t0, vol, hasta=None, fade_in=0.15, fade_out=0.4):
    st = S.new_sound(nombre, f"{AUD}/{fn}", canal, fr(t0))
    if hasta is not None and fr(t0) + st.frame_duration > fr(hasta):
        st.frame_final_end = fr(hasta)
    t1 = st.frame_final_end / FPS
    st.volume = vol
    rampa(st, [(fr(t0), 0.0), (fr(t0 + fade_in), vol), (fr(t1 - fade_out), vol), (fr(t1), 0.0)])


sfx("mazo", "brasil-e2-mazo-v1.wav", 21, voces[1]["abs"] + MAZO_EN, VOL_MAZO, fade_in=0.01, fade_out=0.5)
sfx("escuela", "brasil-e6-escuela-v1.wav", 22, B[5] + 0.3, VOL_ESCUELA, hasta=B[6] - 0.1)

sc.frame_start, sc.frame_end = 1, dur
rd = sc.render
rd.image_settings.media_type = "VIDEO"
rd.image_settings.file_format = "FFMPEG"
rd.ffmpeg.format, rd.ffmpeg.codec = "MPEG4", "H264"
rd.ffmpeg.constant_rate_factor, rd.ffmpeg.ffmpeg_preset = "HIGH", "GOOD"
rd.ffmpeg.audio_codec, rd.ffmpeg.audio_bitrate, rd.ffmpeg.audio_channels = "AAC", 192, "STEREO"
rd.filepath = f"{OUT}/brasil-60s-9x16-r3.mp4"
bpy.ops.wm.save_as_mainfile(filepath=f"{OUT}/brasil-60s.blend")
print("DURACION", round(T_FIN, 2), "s;", dur, "fotogramas")
for v in voces:
    print("voz", v["n"], round(v["abs"], 2), "->", round(v["abs"] + v["dur"], 2))
for v in voces:
    st = v["strip"]
    print("fuente", v["n"], f"se oye {(st.frame_final_start - st.frame_start) / FPS:.2f}-{(st.frame_final_end - st.frame_start) / FPS:.2f} s del archivo; voz útil {v['ini'] + PAD_INI:.2f}-{v['fin'] - PAD_FIN:.2f}")
print("FRONTERAS", [round(b, 2) for b in B])
if os.environ.get("SOLO_PROYECTO") != "1":
    bpy.ops.render.render(animation=True)
    print("LISTO", rd.filepath)
