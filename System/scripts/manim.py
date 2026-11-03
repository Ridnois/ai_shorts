#!/usr/bin/env python3
"""Exact maths as a transparent clip in the paper look (Build: Kit, Manim; Picture §Medium "manim").
    System/.venv/bin/python System/scripts/manim.py "Media/…/<Video>" <scene.py> <SceneClass> [--size 1080] [--preview]
The scene file imports `from manim_paper import *` (palette, thick ink, transparent ground). Output:
hf/assets/<SceneClass>.webm (VP9 with alpha, square, 30 fps), placed in a world with a `clip` item (no frame: give it
"layer": "cam" and set the frame off with css, or an html item <video src=... muted>).
Setup once (needs the cairo and pango headers): sudo apt install libcairo2-dev libpango1.0-dev pkg-config
then: uv venv --python 3.12 System/.venv && uv pip install --python System/.venv/bin/python manim"""
import argparse, glob, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    p = argparse.ArgumentParser(); p.add_argument("root"); p.add_argument("scene"); p.add_argument("cls")
    p.add_argument("--size", type=int, default=1080); p.add_argument("--preview", action="store_true"); a = p.parse_args()
    try:
        import manim  # noqa: F401
    except ImportError:
        sys.exit("manim is not installed in this Python: run with System/.venv/bin/python (setup in this file's header)")
    tmp = tempfile.mkdtemp(prefix="manim-")
    env = dict(os.environ, PYTHONPATH=HERE + os.pathsep + os.environ.get("PYTHONPATH", ""))
    q = ["-ql"] if a.preview else []
    r = subprocess.run([sys.executable, "-m", "manim", "render", *q, "--transparent", "--format", "webm", "-r", f"{a.size},{a.size}",
                        "--fps", "30", "--media_dir", tmp, os.path.abspath(a.scene), a.cls], capture_output=True, text=True, env=env)
    if r.returncode:
        sys.exit(r.stdout[-1500:] + r.stderr[-1500:])
    outs = glob.glob(f"{tmp}/videos/**/{a.cls}.webm", recursive=True)
    if not outs:
        sys.exit("manim wrote no webm")
    dst = f"{os.path.abspath(a.root)}/hf/assets/{a.cls}.webm"
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.move(outs[0], dst); shutil.rmtree(tmp)
    dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", dst], capture_output=True, text=True).stdout.strip()
    print(f"MANIM {dst} {dur} s (transparent)")


if __name__ == "__main__":
    main()
