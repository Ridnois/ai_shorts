#!/usr/bin/env python3
"""Proof footage from a real web page (Build: Kit, Captures): a scripted browser session recorded at 1080x1920.
    python3 System/scripts/capture.py "Media/…/<Video>" <name> <script.json> [--speed 1.0]
Writes hf/assets/<name>.webm (VP9, real timing; --speed 2 plays it twice as fast and the Script note must say so) and
stock/<name>-capture.json (url, steps, date) for the credit line. Script format: the header of capture.mjs.
Record only tools whose licence allows it (Picture §Medium) and never a page showing keys or personal data."""
import argparse, datetime, json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    p = argparse.ArgumentParser(); p.add_argument("root"); p.add_argument("name"); p.add_argument("script")
    p.add_argument("--speed", type=float, default=1.0); a = p.parse_args()
    root = os.path.abspath(a.root); spec = json.load(open(a.script))
    tmp = tempfile.mkdtemp(prefix="cap-")
    r = subprocess.run(["node", f"{HERE}/capture.mjs", os.path.abspath(a.script), tmp], capture_output=True, text=True)
    print(r.stdout.strip() or r.stderr[-1500:])
    if r.returncode: sys.exit("capture failed")
    fr = json.load(open(f"{tmp}/frames.json"))
    lst = f"{tmp}/list.txt"
    with open(lst, "w") as f:                       # each frame held until the next one was taken: real timing
        for (name, t), (_, t2) in zip(fr, fr[1:]):
            f.write(f"file '{tmp}/{name}'\nduration {max(0.02, (t2 - t) / a.speed):.3f}\n")
        f.write(f"file '{tmp}/{fr[-2][0]}'\nduration 0.04\n")
    os.makedirs(f"{root}/hf/assets", exist_ok=True); os.makedirs(f"{root}/stock", exist_ok=True)
    out = f"{root}/hf/assets/{a.name}.webm"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-vf",
                    "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=white,fps=30",
                    "-c:v", "libvpx-vp9", "-b:v", "0", "-crf", "28", "-row-mt", "1", "-an", out], check=True)
    json.dump({"url": spec.get("url"), "steps": spec.get("steps"), "speed": a.speed,
               "recorded": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")},
              open(f"{root}/stock/{a.name}-capture.json", "w"), indent=1)
    dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", out], capture_output=True, text=True).stdout.strip()
    shutil.rmtree(tmp)
    print(f"CAPTURE {os.path.relpath(out, root)} {dur} s" + (f" (played at {a.speed}x: say so on screen)" if a.speed != 1 else ""))


if __name__ == "__main__":
    main()
