"""Assembles the 38 s video in Blender's sequencer.
Usage: blender -b --factory-startup --python render/build_38s.py   (from the version's folder)
Output: render/imanes-38s-r1.mp4 and render/imanes-38s.blend
"""
import bpy, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) if "__file__" in globals() else os.getcwd()
VOZ, ILU, OUT = f"{ROOT}/voz", f"{ROOT}/ilustraciones", f"{ROOT}/render"
FPS, W, H = 24, 1920, 1080
CORTAR_ENVIOS = True   # scene 3: "Los envíos cayeron" ("Shipments fell") is cut

sc = bpy.context.scene
sc.render.fps = FPS
sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = W, H, 100
sc.sequence_editor_create()
S = sc.sequence_editor.strips
f = lambda t: round(t * FPS)

# --- Voice: (file, initial trim s, final trim s, start on the timeline s)
voz = [
    ("e1-voz-qwen-design-v3.wav", 0.14, 7.70, 3.00),
    ("e2-voz-qwen-design-v3.wav", 0.00, 9.40, 10.96),
    ("e3-voz-qwen-design-v3.wav", 0.06, 8.90 if CORTAR_ENVIOS else 10.44, 20.76),
    ("e4-voz-qwen-design-v3.wav", 0.10, 8.42, 30.00),
]
end_audio = 0
for i, (fn, a, b, t0) in enumerate(voz, 1):
    st = S.new_sound(f"voz-e{i}", f"{VOZ}/{fn}", 5, f(t0))
    st.frame_offset_start = f(a)                       # trim at the start
    st.frame_final_end = f(t0) + f(b - a)              # trim at the end
    end_audio = max(end_audio, st.frame_final_end)

# --- Image: shots (start s, end s, initial image, final image)
tomas = [
    ("e1",  0.00, 10.76, "e1-inicial-v3.png",  "e1-final-v1.png"),
    ("e2", 10.76, 20.56, "e2-inicial-v2.png",  "e2-final-v1.png"),
    ("e3a", 20.56, 25.20, "e3a-inicial-v4.png", "e3a-final-v1.png"),
    ("e3b", 25.20, 29.80, "e3b-inicial-v3.png", "e3b-final-v1.png"),
    ("e4a", 29.80, 32.80, "e4a-inicial-v1.png", "e4a-final-v1.png"),
    ("e4b", 32.80, 38.80, "e4b-inicial-v3.png", "e4b-final-v1.png"),
]
def add_img(name, fn, ch, t0, t1):
    st = S.new_image(name, f"{ILU}/{fn}", ch, f(t0))
    st.frame_final_end = f(t1)
    st.transform.scale_x = st.transform.scale_y = W / st.elements[0].orig_width if hasattr(st.elements[0], "orig_width") else 1.0
    return st
for name, t0, t1, ini, fin in tomas:
    d = t1 - t0
    a = add_img(f"{name}-inicial", ini, 1, t0, t1)
    b = add_img(f"{name}-final", fin, 2, t0 + 0.35 * d, t1)
    # fade of the final image over the initial
    b.blend_alpha = 0.0
    b.keyframe_insert("blend_alpha", frame=f(t0 + 0.35 * d))
    b.blend_alpha = 1.0
    b.keyframe_insert("blend_alpha", frame=f(t0 + 0.35 * d + 0.55 * d))

sc.frame_start, sc.frame_end = 1, f(38.80)
r = sc.render
r.image_settings.media_type = "VIDEO"
r.image_settings.file_format = "FFMPEG"
r.ffmpeg.format, r.ffmpeg.codec = "MPEG4", "H264"
r.ffmpeg.constant_rate_factor, r.ffmpeg.ffmpeg_preset = "HIGH", "GOOD"
r.ffmpeg.audio_codec, r.ffmpeg.audio_bitrate, r.ffmpeg.audio_channels = "AAC", 192, "STEREO"
r.filepath = f"{OUT}/imanes-38s-r1.mp4"
bpy.ops.wm.save_as_mainfile(filepath=f"{OUT}/imanes-38s.blend")
bpy.ops.render.render(animation=True)
print("LISTO", r.filepath, "fin audio s:", end_audio / FPS)
