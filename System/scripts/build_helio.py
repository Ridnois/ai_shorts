"""Monta el video "Helio y poder" (70 s) en el secuenciador de Blender 5.2.

Uso (desde la carpeta del video):
    blender -b --factory-startup --python render/build_helio.py

Salida: render/helio-70s-r1.mp4 y render/helio-70s.blend
El diseño de transiciones y efectos está documentado en
Sistema/Montaje/Transiciones y efectos.md
"""
import array
import os
import wave

import bpy
import numpy as np

# ---------------------------------------------------------------- parámetros
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOZ, AUD, ILU, OUT = (f"{ROOT}/{d}" for d in ("voz", "audio", "ilustraciones", "render"))
FX = f"{OUT}/_fx"
FPS, W, H = 24, 1920, 1080

GAP_ESCENA = 0.30          # silencio entre voces (s)
INICIO_VOZ = 0.40          # la voz de la escena 1 entra a los 0,6 s
COLA = 1.00                # imagen que se queda tras la última palabra, antes del corte a negro
DIP = 0.20                 # mitad de "pasar la hoja": sale y entra, cada una DIP s
CRUCE = 0.30               # fundido cruzado entre tomas de una misma escena
ZOOM = 0.06                # empuje lento de cámara (6 %)
PAPEL = (0.89, 0.83, 0.68)  # color del papel, en lineal
VIGNETA = 0.55             # opacidad de la viñeta
GRANO = 0.10               # opacidad del grano
VOL_VOZ, VOL_ZUMBIDO, VOL_RESONANCIA, VOL_SISEO = 1.0, 0.30, 0.18, 0.22

sc = bpy.context.scene
sc.render.fps = FPS
sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = W, H, 100
sc.sequence_editor_create()
S = sc.sequence_editor.strips
bpy.context.preferences.edit.keyframe_new_interpolation_type = "LINEAR"
fr = lambda t: round(t * FPS)


# ---------------------------------------------------------------- análisis de voz
def analiza(path):
    """Devuelve (inicio_voz, fin_voz) en s del archivo."""
    w = wave.open(path)
    sr = w.getframerate()
    a = array.array("h")
    a.frombytes(w.readframes(w.getnframes()))
    win = int(sr * 0.01)
    env = [sum(abs(x) for x in a[i:i + win]) / win for i in range(0, len(a) - win, win)]
    thr = max(env) * 0.03
    v = [i for i, e in enumerate(env) if e > thr]
    return v[0] * 0.01, (v[-1] + 1) * 0.01


voces = []
t = INICIO_VOZ
for n in range(1, 7):
    f = f"helio-e{n}-voz-qwen-design-v1.wav"
    a, b = analiza(f"{VOZ}/{f}")
    ini, fin = max(0.0, a - 0.08), b + 0.12          # recorte de silencios
    voces.append({"n": n, "f": f, "ini": ini, "fin": fin, "abs": t, "dur": fin - ini})
    t += (fin - ini) + GAP_ESCENA
cue = lambda n, ft: voces[n - 1]["abs"] + (ft - voces[n - 1]["ini"])   # tiempo del archivo -> línea de tiempo

# fronteras de escena: a la mitad del silencio entre voces
B = [0.0] + [v["abs"] + v["dur"] + GAP_ESCENA / 2 for v in voces[:5]] + [voces[5]["abs"] + voces[5]["dur"] + COLA]
T_FIN = B[6]

for v in voces:
    st = S.new_sound(f"voz-e{v['n']}", f"{VOZ}/{v['f']}", 30, fr(v["abs"]))
    st.frame_offset_start = fr(v["ini"])
    st.frame_final_end = fr(v["abs"]) + fr(v["dur"])
    st.volume = VOL_VOZ


# ---------------------------------------------------------------- imagen
# Cada toma: (id, canal, inicio, fin, inicial, final, cambio_empieza, cambio_dura, zoom)
# El cambio de estado es el fundido del fotograma final sobre el inicial, sincronizado con la voz.
CORTE_3, CORTE_5 = cue(3, 5.66), cue(5, 4.85)
tomas = [
    ("e1",  2, B[0], B[1], "e1-inicial-v1", "e1-final-v1", cue(1, 8.51), 0.50, +1),   # la antorcha se apaga en "Se detuvo el gas"
    ("e2",  2, B[1], B[2], "e2-inicial-v2", "e2-final-v1", cue(2, 4.33), 4.00, +1),   # acercamiento a las bobinas
    ("e3a", 2, B[2], CORTE_3, "e3a-inicial-v2", "e3a-final-v1", cue(3, 3.25), 1.20, +1),  # el corchete agrupa a los tres países
    ("e3b", 4, CORTE_3 - CRUCE, B[3], "e3b-inicial-v2", "e3b-final-v1", cue(3, 10.2), 0.80, +1),  # la barrera cierra el paso
    ("e4",  2, B[3], B[4], "e4-inicial-v1", "e4-final-v1", cue(4, 1.70), 3.40, +1),   # el nivel baja mientras se dice que se evapora
    ("e5a", 2, B[4], CORTE_5, "e5a-inicial-v1", "e5a-final-v1", cue(5, 3.20), 1.00, +1),  # la válvula se cierra con candado
    ("e5b", 4, CORTE_5 - CRUCE, B[5], "e5b-inicial-v2", "e5b-final-v1", cue(5, 7.89), 2.00, +1),  # la llave cambia de manos
    ("e6",  2, B[5], B[6], "e6-inicial-v2", "e6-final-v1", cue(6, 5.70), 4.50, -1),   # aparecen las dependencias; la cámara se aleja
]
CRUCE_ENTRADA = {"e3b", "e5b"}      # entran con fundido cruzado sobre la toma anterior (misma escena)
CRUCE_SALIDA = {"e3a", "e5a"}       # ceden el paso: las cubre la toma siguiente
SIN_SALIDA = {"e6"}                 # la última toma termina en corte seco a negro


def img(nombre, fn, canal, t0, t1):
    st = S.new_image(nombre, f"{ILU}/helio-{fn}.png", canal, fr(t0))
    st.frame_final_end = fr(t1)
    w, h = st.elements[0].orig_width, st.elements[0].orig_height
    st.transform.scale_x = st.transform.scale_y = max(W / w, H / h)      # llenar el cuadro
    return st


def alfa(st, puntos):
    """Keyframes de opacidad; los puntos se ordenan y se quitan los repetidos."""
    vistos = {}
    for t_, val in puntos:
        vistos[fr(t_)] = val
    for f_ in sorted(vistos):
        st.blend_alpha = vistos[f_]
        st.keyframe_insert("blend_alpha", frame=f_)


def empuje(st, t0, t1, ts, direccion):
    """Zoom lineal de la toma (t0..t1); la capa que entra tarde (ts) arranca en el valor que ya llevaba la toma."""
    base = st.transform.scale_x
    k = lambda t_: 1.0 + ZOOM * ((t_ - t0) / (t1 - t0) if direccion > 0 else 1 - (t_ - t0) / (t1 - t0))
    for t_ in (ts, t1):
        st.transform.scale_x = st.transform.scale_y = base * k(t_)
        st.transform.keyframe_insert("scale_x", frame=fr(t_))
        st.transform.keyframe_insert("scale_y", frame=fr(t_))


# papel de fondo: se ve en "pasar la hoja"
papel = S.new_effect("papel", "COLOR", 1, 1, length=fr(T_FIN))
papel.color = PAPEL

for tid, canal, t0, t1, ini, fin, c0, cd, dirz in tomas:
    A = img(f"{tid}-inicial", ini, canal, t0, t1)
    Bf = img(f"{tid}-final", fin, canal + 1, c0, t1)
    empuje(A, t0, t1, t0, dirz)
    empuje(Bf, t0, t1, c0, dirz)

    # opacidad de la capa inicial: entrada y salida de la toma
    pa = []
    if tid in CRUCE_ENTRADA:
        pa += [(t0, 0.0), (t0 + CRUCE, 1.0)]            # fundido cruzado sobre la toma anterior
    elif tid != "e1":
        pa += [(t0, 0.0), (t0 + DIP, 1.0)]              # "pasar la hoja": sale del papel
    if tid not in CRUCE_SALIDA and tid not in SIN_SALIDA:
        pa += [(t1 - DIP, 1.0), (t1, 0.0)]              # "pasar la hoja": se va al papel
    if pa:
        alfa(A, pa)

    # opacidad de la capa final: el cambio de estado y la misma salida
    pb = [(c0, 0.0), (min(c0 + cd, t1), 1.0)]
    if tid not in CRUCE_SALIDA and tid not in SIN_SALIDA:
        pb += [(t1 - DIP, 1.0), (t1, 0.0)]
    alfa(Bf, pb)

# ---------------------------------------------------------------- efectos de textura
os.makedirs(FX, exist_ok=True)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
vig = np.clip(1.0 - 0.55 * np.clip(r - 0.35, 0, None) ** 1.6, 0.0, 1.0)
rng = np.random.default_rng(7)
grano = np.clip(0.5 + rng.normal(0, 0.12, (H, W)).astype(np.float32), 0, 1)


def guarda(nombre, gris):
    im = bpy.data.images.new(nombre, W, H, alpha=False)
    rgba = np.dstack([gris, gris, gris, np.ones_like(gris)]).astype(np.float32)
    im.pixels.foreach_set(rgba.ravel())
    im.filepath_raw = f"{FX}/{nombre}.png"
    im.file_format = "PNG"
    im.save()
    return im.filepath_raw


v_path = guarda("viñeta", vig)
g_path = guarda("grano", grano)
dur = fr(T_FIN)
vstrip = S.new_image("viñeta", v_path, 14, 1)
vstrip.frame_final_end = dur
vstrip.blend_type, vstrip.blend_alpha = "MULTIPLY", VIGNETA
gstrip = S.new_image("grano", g_path, 15, 1)
gstrip.frame_final_end = dur
gstrip.blend_type, gstrip.blend_alpha = "OVERLAY", GRANO

# ---------------------------------------------------------------- sonido de ambiente
def rampa(st, prop, puntos):
    """Keyframes de (fotograma, valor) para una propiedad de la tira (volumen)."""
    for f_, val in puntos:
        setattr(st, prop, val)
        st.keyframe_insert(prop, frame=f_)


def sfx(nombre, fn, canal, t0, vol, hasta=None, fade_in=0.3, fade_out=0.4):
    st = S.new_sound(nombre, f"{AUD}/{fn}", canal, fr(t0))
    if hasta is not None and fr(t0) + st.frame_duration > fr(hasta):
        st.frame_final_end = fr(hasta)
    t1 = (st.frame_final_end) / FPS
    st.volume = vol
    if fade_in:
        rampa(st, "volume", [(fr(t0), 0.0), (fr(t0 + fade_in), vol)])
    if fade_out:
        rampa(st, "volume", [(fr(t1 - fade_out), vol), (fr(t1), 0.0)])
    return st


# zumbido de la planta: bajo la voz y CORTE SECO en "Se detuvo el gas"
z = S.new_sound("zumbido", f"{AUD}/helio-e1-zumbido-planta-v1.mp3", 21, 1)
z.frame_final_end = fr(cue(1, 8.51))
z.volume = VOL_ZUMBIDO
rampa(z, "volume", [(1, 0.0), (fr(0.6), VOL_ZUMBIDO)])         # entra suave, corta duro
sfx("resonancia", "helio-e2-resonancia-v1.mp3", 22, B[1] + 0.2, VOL_RESONANCIA, hasta=B[2] - 0.1)
sfx("siseo", "helio-e4-siseo-gas-v1.mp3", 23, B[3] + 0.2, VOL_SISEO, hasta=B[4] - 0.1)

# ---------------------------------------------------------------- render
sc.frame_start, sc.frame_end = 1, dur
rd = sc.render
rd.image_settings.media_type = "VIDEO"
rd.image_settings.file_format = "FFMPEG"
rd.ffmpeg.format, rd.ffmpeg.codec = "MPEG4", "H264"
rd.ffmpeg.constant_rate_factor, rd.ffmpeg.ffmpeg_preset = "HIGH", "GOOD"
rd.ffmpeg.audio_codec, rd.ffmpeg.audio_bitrate, rd.ffmpeg.audio_channels = "AAC", 192, "STEREO"
rd.filepath = f"{OUT}/helio-70s-r1.mp4"
bpy.ops.wm.save_as_mainfile(filepath=f"{OUT}/helio-70s.blend")
print("DURACION", round(T_FIN, 2), "s;", dur, "fotogramas")
for v in voces:
    print("voz", v["n"], round(v["abs"], 2), "->", round(v["abs"] + v["dur"], 2))
print("FRONTERAS", [round(b, 2) for b in B], "corte3", round(CORTE_3, 2), "corte5", round(CORTE_5, 2))
if os.environ.get("SOLO_PROYECTO") != "1":
    bpy.ops.render.render(animation=True)
    print("LISTO", rd.filepath)
