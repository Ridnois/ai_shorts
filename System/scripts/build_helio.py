"""Assembles the video "Helium and power" (70 s) in Blender 5.2's sequencer.

Usage (from the video's folder):
    blender -b --factory-startup --python render/build_helio.py

Output: render/helio-70s-r1.mp4 and render/helio-70s.blend
The design of transitions and effects is documented in
System/Editing/Transitions and effects.md (Spanish narration)
"""
import array
import os
import wave

import bpy
import numpy as np

# ---------------------------------------------------------------- parameters
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOZ, AUD, ILU, OUT = (f"{ROOT}/{d}" for d in ("voz", "audio", "ilustraciones", "render"))
FX = f"{OUT}/_fx"
FPS, W, H = 24, 1920, 1080

GAP_ESCENA = 0.30          # silence between voices (s)
INICIO_VOZ = 0.40          # the scene 1 voice enters at 0.6 s
COLA = 1.00                # image that stays after the last word, before the cut to black
DIP = 0.20                 # half of the "page turn": exits and enters, each DIP s
CRUCE = 0.30               # cross-fade between shots of the same scene
ZOOM = 0.06                # slow camera push (6 %)
PAPEL = (0.89, 0.83, 0.68)  # paper colour, in linear
VIGNETA = 0.55             # vignette opacity
GRANO = 0.10               # grain opacity
VOL_VOZ, VOL_ZUMBIDO, VOL_RESONANCIA, VOL_SISEO = 1.0, 0.30, 0.18, 0.22

sc = bpy.context.scene
sc.render.fps = FPS
sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = W, H, 100
sc.sequence_editor_create()
S = sc.sequence_editor.strips
bpy.context.preferences.edit.keyframe_new_interpolation_type = "LINEAR"
fr = lambda t: round(t * FPS)


# ---------------------------------------------------------------- voice analysis
def analiza(path):
    """Returns (voice_start, voice_end) in s of the file."""
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
    ini, fin = max(0.0, a - 0.08), b + 0.12          # trimming of silences
    voces.append({"n": n, "f": f, "ini": ini, "fin": fin, "abs": t, "dur": fin - ini})
    t += (fin - ini) + GAP_ESCENA
cue = lambda n, ft: voces[n - 1]["abs"] + (ft - voces[n - 1]["ini"])   # file time -> timeline

# scene boundaries: halfway through the silence between voices
B = [0.0] + [v["abs"] + v["dur"] + GAP_ESCENA / 2 for v in voces[:5]] + [voces[5]["abs"] + voces[5]["dur"] + COLA]
T_FIN = B[6]

for v in voces:
    st = S.new_sound(f"voz-e{v['n']}", f"{VOZ}/{v['f']}", 30, fr(v["abs"]))
    st.frame_offset_start = fr(v["ini"])
    st.frame_final_end = fr(v["abs"]) + fr(v["dur"])
    st.volume = VOL_VOZ


# ---------------------------------------------------------------- imagen
# Cada toma: (id, canal, inicio, fin, inicial, final, cambio_empieza, cambio_dura, zoom)
# The state change is the fade of the final frame over the initial one, synced with the voice.
CORTE_3, CORTE_5 = cue(3, 5.66), cue(5, 4.85)
tomas = [
    ("e1",  2, B[0], B[1], "e1-inicial-v1", "e1-final-v1", cue(1, 8.51), 0.50, +1),   # the flare goes out at "Se detuvo el gas" ("the gas stopped")
    ("e2",  2, B[1], B[2], "e2-inicial-v2", "e2-final-v1", cue(2, 4.33), 4.00, +1),   # zoom to the coils
    ("e3a", 2, B[2], CORTE_3, "e3a-inicial-v2", "e3a-final-v1", cue(3, 3.25), 1.20, +1),  # the bracket groups the three countries
    ("e3b", 4, CORTE_3 - CRUCE, B[3], "e3b-inicial-v2", "e3b-final-v1", cue(3, 10.2), 0.80, +1),  # the barrier closes the passage
    ("e4",  2, B[3], B[4], "e4-inicial-v1", "e4-final-v1", cue(4, 1.70), 3.40, +1),   # the level drops while it is said that it evaporates
    ("e5a", 2, B[4], CORTE_5, "e5a-inicial-v1", "e5a-final-v1", cue(5, 3.20), 1.00, +1),  # the valve closes with a padlock
    ("e5b", 4, CORTE_5 - CRUCE, B[5], "e5b-inicial-v2", "e5b-final-v1", cue(5, 7.89), 2.00, +1),  # the key changes hands
    ("e6",  2, B[5], B[6], "e6-inicial-v2", "e6-final-v1", cue(6, 5.70), 4.50, -1),   # the dependencies appear; the camera pulls back
]
CRUCE_ENTRADA = {"e3b", "e5b"}      # they enter with a cross-fade over the previous shot (same scene)
CRUCE_SALIDA = {"e3a", "e5a"}       # they give way: the next shot covers them
SIN_SALIDA = {"e6"}                 # the last shot ends in a hard cut to black


def img(nombre, fn, canal, t0, t1):
    st = S.new_image(nombre, f"{ILU}/helio-{fn}.png", canal, fr(t0))
    st.frame_final_end = fr(t1)
    w, h = st.elements[0].orig_width, st.elements[0].orig_height
    st.transform.scale_x = st.transform.scale_y = max(W / w, H / h)      # fill the frame
    return st


def alfa(st, puntos):
    """Opacity keyframes; the points are sorted and repeats removed."""
    vistos = {}
    for t_, val in puntos:
        vistos[fr(t_)] = val
    for f_ in sorted(vistos):
        st.blend_alpha = vistos[f_]
        st.keyframe_insert("blend_alpha", frame=f_)


def empuje(st, t0, t1, ts, direccion):
    """Linear zoom of the shot (t0..t1); the layer that enters late (ts) starts at the value the shot already had."""
    base = st.transform.scale_x
    k = lambda t_: 1.0 + ZOOM * ((t_ - t0) / (t1 - t0) if direccion > 0 else 1 - (t_ - t0) / (t1 - t0))
    for t_ in (ts, t1):
        st.transform.scale_x = st.transform.scale_y = base * k(t_)
        st.transform.keyframe_insert("scale_x", frame=fr(t_))
        st.transform.keyframe_insert("scale_y", frame=fr(t_))


# background paper: shows in the "page turn"
papel = S.new_effect("papel", "COLOR", 1, 1, length=fr(T_FIN))
papel.color = PAPEL

for tid, canal, t0, t1, ini, fin, c0, cd, dirz in tomas:
    A = img(f"{tid}-inicial", ini, canal, t0, t1)
    Bf = img(f"{tid}-final", fin, canal + 1, c0, t1)
    empuje(A, t0, t1, t0, dirz)
    empuje(Bf, t0, t1, c0, dirz)

    # opacity of the initial layer: entry and exit of the shot
    pa = []
    if tid in CRUCE_ENTRADA:
        pa += [(t0, 0.0), (t0 + CRUCE, 1.0)]            # cross-fade over the previous shot
    elif tid != "e1":
        pa += [(t0, 0.0), (t0 + DIP, 1.0)]              # "page turn": comes out of the paper
    if tid not in CRUCE_SALIDA and tid not in SIN_SALIDA:
        pa += [(t1 - DIP, 1.0), (t1, 0.0)]              # "page turn": goes into the paper
    if pa:
        alfa(A, pa)

    # opacity of the final layer: the state change and the same exit
    pb = [(c0, 0.0), (min(c0 + cd, t1), 1.0)]
    if tid not in CRUCE_SALIDA and tid not in SIN_SALIDA:
        pb += [(t1 - DIP, 1.0), (t1, 0.0)]
    alfa(Bf, pb)

# ---------------------------------------------------------------- texture effects
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

# ---------------------------------------------------------------- ambient sound
def rampa(st, prop, puntos):
    """Keyframes of (frame, value) for a strip property (volume)."""
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


# plant hum: under the voice and HARD CUT at "Se detuvo el gas"
z = S.new_sound("zumbido", f"{AUD}/helio-e1-zumbido-planta-v1.mp3", 21, 1)
z.frame_final_end = fr(cue(1, 8.51))
z.volume = VOL_ZUMBIDO
rampa(z, "volume", [(1, 0.0), (fr(0.6), VOL_ZUMBIDO)])         # enters softly, cuts hard
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
