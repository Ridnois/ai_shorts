"""3D plates: tokens, embedding spaces, layered networks, links and solids, lit and rendered by Blender EEVEE as
1080x1920 H.264 clips that build_video.py places like any motion plate (System/Playbook.md §3, System/Style.md 3D plates).

    VIDEO="Media/<folder>" SOLO_PROYECTO=1 blender -b --factory-startup --python System/scripts/build_video.py   # writes render/_timeline.json
    python3 System/scripts/scene3d.py "Media/<folder>"                  # renders every `scene3d` plate of plan.json
    python3 System/scripts/scene3d.py "Media/<folder>" --only 3d-net    # plates whose file contains this text
    python3 System/scripts/scene3d.py "Media/<folder>" --sheet          # also writes <file>.sheet.png (6 frames) to look at
    python3 System/scripts/scene3d.py "Media/<folder>" --preview        # half size, 4 samples: fast drafts while staging

A 3D plate in plan.json is a motion plate with a `scene3d` spec instead of a `motion` one (motion.py skips it):
    {"type": "motion", "file": "motion/ai-3d-net.mp4", "scene3d": {"camera": {...}, "els": [...]}}
Cues are motion.py's (seconds, a heard word "token", "token#2", "token+0.3", "end", "end-0.5"); this script resolves
them with the plate's timeline, then runs itself inside Blender. Units are metres; the camera looks along +y by default.

Spec (top level):  camera {"lens": 50, "keys": {"pos": [[cue, [x,y,z]], ...], "target": [[cue, [x,y,z]], ...]}}
                   ground "navy" (world colour) · bloom 0.6 (glare strength; 0 = off) · dof [target distance m, f-stop]
Elements (`els`), colours are motion.py palette names or hex:
  common   pos [x,y,z] · color · emit (emission strength; keyable) · show [in, out] (pops in and out by scale)
           · keys {"pos"|"rot"|"scale"|"emit": [[cue, value], ...]} (rot in degrees) · pulse [cue, ...] (emission swell)
  box      size [x,y,z] bevel             sphere  r              text  text size (height m) extrude
  tokens   words [...] gap stagger (s between pops) size: a row of rounded tiles, one word on each (what a model reads)
  cloud    clusters [[x,y,z, spread, n, color], ...] r seed: an embedding space (points near each other mean similar)
  net      layers [4,6,6,3] gap spread r · fire [cue, ...]: a forward pass lights each layer in turn (0.12 s apart)
  link     from [x,y,z] to [x,y,z] r · draw [cue, cue]: a tube that grows from `from` to `to` (attention, a call, data)
  surface  size [w,d] res base bowl tilt [tx,ty] wells [[x,y,depth,width], ...] wire (grid colour) · rise [cue, cue]: a
           loss landscape z = base + tilt·xy + bowl·r² - Σ depth·exp(-d²/width²), drawn as a solid with a grid on it
           balls [{start [x,y], lr, steps, run [cue, cue], r, color, emit, trail, arrow cue}]: real gradient descent on
           that function (x -= lr·gradient), one keyed hop per step; `arrow` shows the downhill direction at the start

Text warnings match motion.py: text entering the caption band (y 880 to 1040), the bottom interface zone (y > 1440)
or the right action strip (x > 950) is reported at sampled frames. Look at the --sheet frames before the build.
"""
import json, math, os, subprocess, sys

W, H, FPS = 1080, 1920, 24
CAP_BAND, UI_BOTTOM, UI_RIGHT = (880, 1040), 1440, 950
HERE = os.path.dirname(os.path.abspath(__file__))
FONT = "/usr/share/fonts/truetype/noto/NotoSansDisplay-Bold.ttf"


# ---------------------------------------------------------------- outside Blender: resolve cues, then call Blender
def resolve(spec, cues):
    """Every cue in the spec becomes seconds from the plate start."""
    def keys(k):
        return {p: [[cues(c), v] for c, v in pts] for p, pts in k.items()}
    cam = spec.setdefault("camera", {})
    cam["keys"] = keys(cam.get("keys", {}))
    for el in spec.get("els", []):
        el["show"] = [cues(c) for c in el.get("show", [0, "end"])]
        el["keys"] = keys(el.get("keys", {}))
        for f in ("pulse", "fire", "draw", "rise"):
            if f in el:
                el[f] = [cues(c) for c in el[f]]
        for b in el.get("balls", []):
            b["run"] = [cues(c) for c in b["run"]]
            if "arrow" in b:
                b["arrow"] = cues(b["arrow"])
    return spec


def outside():
    import argparse
    sys.path.insert(0, HERE)
    from motion import PAL, Cues
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--only", default="")
    ap.add_argument("--sheet", action="store_true")
    ap.add_argument("--preview", action="store_true")
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
            if "scene3d" not in pl or a.only not in pl["file"]:
                continue
            p = slots.get(pl["file"])
            if not p:
                raise SystemExit(f"{pl['file']} is not in render/_timeline.json: rebuild with SOLO_PROYECTO=1")
            out = os.path.join(root, pl["file"])
            os.makedirs(os.path.dirname(out), exist_ok=True)
            job = {"spec": resolve(json.loads(json.dumps(pl["scene3d"])), Cues(tl["words"], p["ini"], p["fin"], pl["file"])),
                   "dur": p["fin"] - p["ini"], "out": out, "pal": PAL, "preview": a.preview, "label": pl["file"]}
            jp = os.path.splitext(out)[0] + ".job.json"
            json.dump(job, open(jp, "w"), indent=1)
            r = subprocess.run(["blender", "-b", "--factory-startup", "--python", __file__, "--", jp],
                               capture_output=True, text=True)
            for line in r.stdout.splitlines():
                if line.startswith(("WARN", "  3D")):
                    print(line)
            if r.returncode or not os.path.exists(out):
                sys.stderr.write(r.stdout[-2000:] + r.stderr[-2000:])
                raise SystemExit(f"{pl['file']}: Blender failed")
            os.remove(jp)
            if a.sheet:                                   # same contact sheet as motion.py: 6 frames in a row
                png = os.path.splitext(out)[0] + ".sheet.png"
                step = max(job["dur"] / 6, 0.1)
                subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", out, "-vf",
                                f"fps=1/{step:.3f},scale=270:-1,tile=6x1", "-frames:v", "1", png], check=True)
                print("  sheet", os.path.relpath(png, root))
            done += 1
    print("3D PLATES rendered:", done)


# ---------------------------------------------------------------- inside Blender
def inside(jp):
    import bpy
    from bpy_extras.object_utils import world_to_camera_view
    from mathutils import Vector

    job = json.load(open(jp))
    spec, dur, pal = job["spec"], job["dur"], job["pal"]
    sc = bpy.context.scene
    n_frames = max(1, round(dur * FPS))
    sc.frame_start, sc.frame_end = 1, n_frames
    sc.render.fps = FPS
    k = 0.5 if job["preview"] else 1.0
    sc.render.resolution_x, sc.render.resolution_y = int(W * k), int(H * k)
    sc.render.engine = "BLENDER_EEVEE"
    sc.eevee.taa_render_samples = 4 if job["preview"] else 16
    sc.view_settings.view_transform = "AgX"
    for o in list(bpy.data.objects):
        bpy.data.objects.remove(o)

    def rgb(c):
        h = pal.get(c, c).lstrip("#")
        return tuple((int(h[i:i + 2], 16) / 255) ** 2.2 for i in (0, 2, 4)) + (1.0,)   # sRGB hex to linear

    fr = lambda t: 1 + t * FPS

    world = bpy.data.worlds.new("w")
    sc.world = world
    world.use_nodes = True
    world.node_tree.nodes["Background"].inputs[0].default_value = rgb(spec.get("ground", "navy"))
    world.node_tree.nodes["Background"].inputs[1].default_value = 1.0
    for rot, e in (((50, 0, 30), 3.0), ((60, 0, -140), 1.2)):                         # key and rim light
        ld = bpy.data.lights.new("l", "SUN")
        ld.energy = e
        lo = bpy.data.objects.new("l", ld)
        lo.rotation_euler = [math.radians(v) for v in rot]
        sc.collection.objects.link(lo)

    mats = {}

    def material(color, emit, own=False, rough=0.35):
        key = (color, emit, rough)
        if key in mats and not own:
            return mats[key]
        m = bpy.data.materials.new("m")
        bsdf = m.node_tree.nodes["Principled BSDF"]
        bsdf.inputs["Base Color"].default_value = rgb(color)
        bsdf.inputs["Roughness"].default_value = rough
        bsdf.inputs["Emission Color"].default_value = rgb(color)
        bsdf.inputs["Emission Strength"].default_value = emit
        mats[key] = m
        return m

    def emit_socket(m):
        return m.node_tree.nodes["Principled BSDF"].inputs["Emission Strength"]

    def key_socket(sock, pts):
        for t, v in pts:
            sock.default_value = v
            sock.keyframe_insert("default_value", frame=fr(t))

    def add(obj_data, name, pos, mat):
        o = bpy.data.objects.new(name, obj_data)
        sc.collection.objects.link(o)
        o.location = pos
        if mat and hasattr(obj_data, "materials"):
            if not obj_data.materials:
                obj_data.materials.append(None)
            o.material_slots[0].link = "OBJECT"                     # meshes are shared; the colour belongs to the object
            o.material_slots[0].material = mat
        return o

    meshes = {}

    def mesh(kind, **kw):
        key = (kind, tuple(sorted(kw.items())))
        if key in meshes:
            return meshes[key]
        import bmesh
        bm = bmesh.new()
        if kind == "sphere":
            bmesh.ops.create_uvsphere(bm, u_segments=24, v_segments=16, radius=kw["r"])
        else:
            bmesh.ops.create_cube(bm, size=1.0)
        me = bpy.data.meshes.new(kind)
        bm.to_mesh(me)
        bm.free()
        if kind == "sphere":
            for p in me.polygons:
                p.use_smooth = True
        meshes[key] = me
        return me

    def show(o, t_in, t_out, base=(1, 1, 1)):
        """Pop in by scale at t_in (0.3 s) and out at t_out unless it stays to the end."""
        b = Vector(base)
        if t_in > 0.01:
            o.scale = b * 0.001
            o.keyframe_insert("scale", frame=fr(max(t_in - 0.001, 0)))
            o.scale = b
            o.keyframe_insert("scale", frame=fr(t_in + 0.3))
        if t_out < dur - 0.01:
            o.scale = b
            o.keyframe_insert("scale", frame=fr(max(t_out - 0.3, 0)))
            o.scale = b * 0.001
            o.keyframe_insert("scale", frame=fr(t_out))
        o.scale = b * 0.001 if t_in > 0.01 else b

    def keys(o, el, m):
        for prop, pts in el.get("keys", {}).items():
            for t, v in pts:
                if prop == "pos":
                    o.location = v
                    o.keyframe_insert("location", frame=fr(t))
                elif prop == "rot":
                    o.rotation_euler = [math.radians(x) for x in v]
                    o.keyframe_insert("rotation_euler", frame=fr(t))
                elif prop == "scale":
                    o.scale = v if isinstance(v, list) else [v] * 3
                    o.keyframe_insert("scale", frame=fr(t))
            if prop == "emit" and m:
                key_socket(emit_socket(m), pts)

    def pulse(m, cues, base):
        pts = []
        for t in cues:
            pts += [(max(t - 0.05, 0), base), (t + 0.12, base * 4 + 4), (t + 0.6, base)]
        if pts:
            key_socket(emit_socket(m), pts)

    def text_obj(s, size, color, emit, pos, extrude=0.02):
        cu = bpy.data.curves.new("t", "FONT")
        cu.body = s
        cu.font = bpy.data.fonts.load(FONT, check_existing=True)
        cu.size = size
        cu.extrude = extrude
        cu.align_x, cu.align_y = "CENTER", "CENTER"
        o = add(cu, "text", pos, material(color, emit))
        o.rotation_euler = (math.radians(90), 0, 0)                 # faces the default camera (looking along +y)
        return o

    def surface(el, pos, m, t_in, t_out):
        wells, base, bowl = el.get("wells", []), el.get("base", 0.0), el.get("bowl", 0.0)
        tx, ty = el.get("tilt", [0, 0])

        def h(x, y):
            z = base + tx * x + ty * y + bowl * (x * x + y * y)
            for wx, wy, d, w in wells:
                z -= d * math.exp(-((x - wx) ** 2 + (y - wy) ** 2) / w ** 2)
            return z

        def grad(x, y):
            gx, gy = tx + 2 * bowl * x, ty + 2 * bowl * y
            for wx, wy, d, w in wells:
                e = d * math.exp(-((x - wx) ** 2 + (y - wy) ** 2) / w ** 2)
                gx, gy = gx + e * 2 * (x - wx) / w ** 2, gy + e * 2 * (y - wy) / w ** 2
            return gx, gy

        sx, sy = el.get("size", [10, 10])
        objs = []
        zs = [h(-sx / 2 + sx * i / 40, -sy / 2 + sy * j / 40) for i in range(41) for j in range(41)]
        for res, mat, wire in ((el.get("res", 72), height_material(min(zs), max(zs), el.get("ramp", ["ink2", "signal", "signal2"]),
                                                                   el.get("emit", 0.35)), False),
                               (el.get("res", 72) // 3, material(el.get("wire", "slate"), el.get("wire_emit", 0.5)), True)):
            n = res + 1
            verts = [(-sx / 2 + sx * i / res, -sy / 2 + sy * j / res, 0) for j in range(n) for i in range(n)]
            verts = [(x, y, h(x, y)) for x, y, _ in verts]
            faces = [(j * n + i, j * n + i + 1, (j + 1) * n + i + 1, (j + 1) * n + i) for j in range(res) for i in range(res)]
            me = bpy.data.meshes.new("surface")
            me.from_pydata(verts, [], faces)
            for f in me.polygons:
                f.use_smooth = True
            o = add(me, "surface", pos, mat)
            if wire:
                wm = o.modifiers.new("w", "WIREFRAME")
                wm.thickness, wm.use_replace = 0.018, True
                o.location.z += 0.01
            objs.append(o)
        a, b = el.get("rise") or [t_in, t_in + 0.6]
        for o in objs:                                    # rises from flat: the error appears as height
            if a > 0.01 or el.get("rise"):
                o.scale = (1, 1, 0.001)
                o.keyframe_insert("scale", frame=fr(a))
            o.scale = (1, 1, 1)
            o.keyframe_insert("scale", frame=fr(b))
        p0 = Vector(pos)
        for bspec in el.get("balls", []):
            r = bspec.get("r", 0.2)
            bm = material(bspec.get("color", "copper"), bspec.get("emit", 3.0))
            x, y = bspec["start"]
            pts = []
            for _ in range(bspec.get("steps", 20) + 1):
                pts.append((x, y))
                gx, gy = grad(x, y)
                x, y = x - bspec["lr"] * gx, y - bspec["lr"] * gy
            r0, r1 = bspec["run"]
            ball = add(mesh("sphere", r=r), "ball", p0 + Vector((pts[0][0], pts[0][1], h(*pts[0]) + r)), bm)
            show(ball, max(t_in, b if el.get("rise") else t_in), t_out)
            dt = (r1 - r0) / max(len(pts) - 1, 1)
            for i, (x, y) in enumerate(pts):
                ball.location = p0 + Vector((x, y, h(x, y) + r))
                ball.keyframe_insert("location", frame=fr(r0 + i * dt))
                if bspec.get("trail", True) and i:
                    dot = add(mesh("sphere", r=r * 0.35), "trail", p0 + Vector((x, y, h(x, y) + r * 0.35)), bm)
                    show(dot, r0 + i * dt, t_out)
            if "arrow" in bspec:
                gx, gy = grad(*pts[0])
                d = Vector((-gx, -gy, -(gx * gx + gy * gy))).normalized() * bspec.get("arrow_len", 1.6)
                start = p0 + Vector((pts[0][0], pts[0][1], h(*pts[0]) + r))
                ar = add(mesh("box"), "arrow", start, material(bspec.get("arrow_color", "copper2"), 4.0))
                ar.data = ar.data.copy()
                for v in ar.data.vertices:
                    v.co.x += 0.5
                ar.rotation_mode = "QUATERNION"
                ar.rotation_quaternion = Vector((1, 0, 0)).rotation_difference(d)
                ar.scale = (0.001, 0.05, 0.05)
                ar.keyframe_insert("scale", frame=fr(bspec["arrow"]))
                ar.scale = (d.length, 0.05, 0.05)
                ar.keyframe_insert("scale", frame=fr(bspec["arrow"] + 0.4))
                ar.keyframe_insert("scale", frame=fr(max(r0, bspec["arrow"] + 0.5)))
                ar.scale = (0.001, 0.05, 0.05)
                ar.keyframe_insert("scale", frame=fr(max(r0, bspec["arrow"] + 0.5) + 0.3))

    texts = []
    for el in spec.get("els", []):
        kind, pos = el["kind"], el.get("pos", [0, 0, 0])
        t_in, t_out = (el["show"] + [dur])[:2]
        color, emit = el.get("color", "copper"), el.get("emit", 0.0)
        own = bool(el.get("pulse") or "emit" in el.get("keys", {}) or el.get("fire"))
        m = material(color, emit, own)
        if kind in ("box", "sphere"):
            me = mesh("sphere", r=el.get("r", 0.5)) if kind == "sphere" else mesh("box")
            o = add(me, kind, pos, m)
            base = el.get("size", [1, 1, 1]) if kind == "box" else [1, 1, 1]
            if kind == "box" and el.get("bevel", 0.06):
                bv = o.modifiers.new("b", "BEVEL")
                bv.width, bv.segments = el.get("bevel", 0.06) / max(min(base), 1e-3), 3
            show(o, t_in, t_out, base)
            keys(o, el, m)
            pulse(m, el.get("pulse", []), emit)
        elif kind == "text":
            o = text_obj(el["text"], el.get("size", 0.5), color, emit, pos, el.get("extrude", 0.02))
            texts.append((o, t_in, t_out))
            show(o, t_in, t_out)
            keys(o, el, m)
        elif kind == "tokens":
            words, gap, size = el["words"], el.get("gap", 1.4), el.get("size", 1.0)
            x0 = pos[0] - gap * (len(words) - 1) / 2
            for i, w in enumerate(words):
                ti = t_in + i * el.get("stagger", 0.12)
                tile = add(mesh("box"), "token", [x0 + i * gap, pos[1], pos[2]], m)
                bv = tile.modifiers.new("b", "BEVEL")
                bv.width, bv.segments = 0.12, 3
                base = [size * 1.2, size * 0.3, size * 0.7]
                show(tile, ti, t_out, base)
                label = text_obj(w, size * 0.32, el.get("text_color", "paper"), 0.6,
                                 [x0 + i * gap, pos[1] - size * 0.16, pos[2]], 0.0)
                texts.append((label, ti, t_out))
                show(label, ti, t_out)
            pulse(m, el.get("pulse", []), emit)
        elif kind == "cloud":
            import random
            rnd = random.Random(el.get("seed", 1))
            for i, (cx, cy, cz, spread, n, ccol) in enumerate(el["clusters"]):
                cm = material(ccol, el.get("emit", 1.5))
                for j in range(int(n)):
                    p = [cx + rnd.gauss(0, spread), cy + rnd.gauss(0, spread), cz + rnd.gauss(0, spread)]
                    o = add(mesh("sphere", r=el.get("r", 0.06)), "pt", p, cm)
                    show(o, t_in + i * el.get("stagger", 0.3) + rnd.random() * 0.4, t_out)
        elif kind == "net":
            layers, gap, spread, r = el["layers"], el.get("gap", 2.0), el.get("spread", 0.9), el.get("r", 0.18)
            x0 = pos[0] - gap * (len(layers) - 1) / 2
            nodes, lm = [], material(el.get("link_color", "dim"), 0.3)
            for li, n in enumerate(layers):
                layer_m = material(color, emit, True)
                col = []
                for j in range(n):
                    p = Vector((x0 + li * gap, pos[1], pos[2] + (j - (n - 1) / 2) * spread))
                    o = add(mesh("sphere", r=r), "node", p, layer_m)
                    show(o, t_in + li * 0.15, t_out)
                    col.append(p)
                pulse(layer_m, [t + li * 0.12 for t in el.get("fire", [])], emit)
                nodes.append(col)
            for li in range(len(nodes) - 1):
                for a in nodes[li]:
                    for b in nodes[li + 1]:
                        o = add(mesh("box"), "edge", (a + b) / 2, lm)
                        d = b - a
                        o.rotation_mode = "QUATERNION"
                        o.rotation_quaternion = Vector((1, 0, 0)).rotation_difference(d)
                        show(o, t_in + li * 0.15 + 0.1, t_out, [d.length, 0.012, 0.012])
        elif kind == "link":
            a, b = Vector(el["from"]), Vector(el["to"])
            d = b - a
            o = add(mesh("box"), "link", a, m)
            o.rotation_mode = "QUATERNION"
            o.rotation_quaternion = Vector((1, 0, 0)).rotation_difference(d)
            r = el.get("r", 0.03)
            o.data = o.data.copy()                        # a unit cube shifted so its origin is one end: it grows along x
            for v in o.data.vertices:
                v.co.x += 0.5
            t0, t1 = (el.get("draw") or [t_in, t_in + 0.6])[:2]
            o.scale = (0.001, r, r)
            o.keyframe_insert("scale", frame=fr(t0))
            o.scale = (d.length, r, r)
            o.keyframe_insert("scale", frame=fr(t1))
            if t_out < dur - 0.01:
                o.keyframe_insert("scale", frame=fr(max(t_out - 0.3, t1)))
                o.scale = (0.001, r, r)
                o.keyframe_insert("scale", frame=fr(t_out))
            pulse(m, el.get("pulse", []), emit)
        elif kind == "surface":
            surface(el, pos, m, t_in, t_out)
        else:
            raise SystemExit(f"{job['label']}: unknown element kind {kind}")

    cam_spec = spec.get("camera", {})
    cd = bpy.data.cameras.new("cam")
    cd.lens = cam_spec.get("lens", 50)
    cam = add(cd, "cam", [0, -12, 0], None)
    sc.camera = cam
    tgt = bpy.data.objects.new("target", None)
    sc.collection.objects.link(tgt)
    tc = cam.constraints.new("TRACK_TO")
    tc.target, tc.track_axis, tc.up_axis = tgt, "TRACK_NEGATIVE_Z", "UP_Y"
    for prop, o in (("pos", cam), ("target", tgt)):
        for t, v in cam_spec.get("keys", {}).get(prop, []):
            o.location = v
            o.keyframe_insert("location", frame=fr(t))
    if spec.get("dof"):
        cd.dof.use_dof = True
        cd.dof.focus_distance, cd.dof.aperture_fstop = spec["dof"]

    bloom = spec.get("bloom", 0.6)
    if bloom:
        tree = bpy.data.node_groups.new("comp", "CompositorNodeTree")
        tree.interface.new_socket("Image", in_out="OUTPUT", socket_type="NodeSocketColor")
        rl = tree.nodes.new("CompositorNodeRLayers")
        gl = tree.nodes.new("CompositorNodeGlare")
        gl.inputs["Type"].default_value = "Bloom"
        gl.inputs["Strength"].default_value = bloom
        gl.inputs["Threshold"].default_value = 0.8
        out = tree.nodes.new("NodeGroupOutput")
        tree.links.new(rl.outputs["Image"], gl.inputs["Image"])
        tree.links.new(gl.outputs["Image"], out.inputs[0])
        sc.compositing_node_group = tree

    # text safety, sampled every 0.5 s (projected bounding boxes against the caption band and interface zones)
    warned = set()
    for i in range(0, n_frames + 1, FPS // 2):
        sc.frame_set(max(i, 1))
        t = (max(i, 1) - 1) / FPS
        for o, a_, b_ in texts:
            if not (a_ + 0.3 <= t <= b_) or o.name in warned:
                continue
            pts = [world_to_camera_view(sc, cam, o.matrix_world @ Vector(c)) for c in o.bound_box]
            xs = [p.x * W for p in pts]
            ys = [(1 - p.y) * H for p in pts]
            body = o.data.body
            if max(ys) > CAP_BAND[0] and min(ys) < CAP_BAND[1]:
                print(f"WARN {job['label']}: text '{body}' crosses the caption band at {t:.1f} s")
            elif max(ys) > UI_BOTTOM or max(xs) > UI_RIGHT or min(xs) < 0:
                print(f"WARN {job['label']}: text '{body}' enters an interface zone or leaves the frame at {t:.1f} s")
            else:
                continue
            warned.add(o.name)

    rd = sc.render
    rd.filepath = job["out"]
    rd.image_settings.media_type = "VIDEO"
    rd.image_settings.file_format = "FFMPEG"
    rd.ffmpeg.format, rd.ffmpeg.codec = "MPEG4", "H264"
    rd.ffmpeg.constant_rate_factor, rd.ffmpeg.ffmpeg_preset = "HIGH", "GOOD"
    rd.use_file_extension = False
    import time
    t0 = time.time()
    bpy.ops.render.render(animation=True)
    print(f"  3D {job['label']}: {n_frames} frames in {time.time() - t0:.0f} s")


if __name__ == "__main__":
    if "--" in sys.argv:
        inside(sys.argv[sys.argv.index("--") + 1])
    else:
        outside()
