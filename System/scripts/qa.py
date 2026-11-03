#!/usr/bin/env python3
"""Every check of a Short in one command and one table (Build §Checks).
    python3 System/scripts/qa.py "Media/…/<Video>"                       # before the render: kit, build, lint, layout, frames
    python3 System/scripts/qa.py "Media/…/<Video>" --render <mixed mp4>  # after the mix: adds pace, sound, master
    --skip frames,lint   leaves rows out (say so in Status)
Exit 1 when a row fails. WARN lines are printed under the table; the agent reads the frames' contact sheets once.
What no row checks: how the voice and effects sound, and whether the motion means something."""
import argparse, glob, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable
HF = "hyperframes@0.8.209"


def run(cmd, cwd=None, timeout=900):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout,
                           env=dict(os.environ, HYPERFRAMES_NO_TELEMETRY="1"))
        return r.returncode, r.stdout + r.stderr
    except subprocess.TimeoutExpired:
        return 124, "timed out"


def main():
    p = argparse.ArgumentParser(); p.add_argument("root"); p.add_argument("--render"); p.add_argument("--skip", default="")
    a = p.parse_args()
    root, skip = os.path.abspath(a.root), set(filter(None, a.skip.split(",")))
    hf = f"{root}/hf"
    rows, warns = [], []

    def row(name, ok, detail, out=""):
        rows.append((name, "PASS" if ok else "FAIL", detail))
        warns.extend(f"{name}: {l.strip()}" for l in out.splitlines() if l.strip().startswith("WARN"))

    if "kit" not in skip:
        rc, o = run([PY, f"{HERE}/hfkit.py"]); row("kit", rc == 0 and "hfkit OK" in o, "hfkit OK" if rc == 0 else o[-200:])
    if "build" not in skip and os.path.exists(f"{hf}/beats.json"):
        rc, o = run([PY, f"{HERE}/beats.py", root])
        n = sum(1 for l in o.splitlines() if l.startswith("WARN"))
        row("build", rc == 0, f"{n} WARN (explain or fix each)" if rc == 0 else o[-300:], o)
    if "lint" not in skip:
        rc, o = run(["npx", "--yes", HF, "check", "--json"], cwd=hf)
        try:
            j = json.loads(o[o.index("{"):])
            errs = sum(v.get("errorCount", 0) for v in j.values() if isinstance(v, dict))
            ok = bool(j.get("ok")) and errs == 0
        except ValueError:
            errs, ok = "?", False
        row("lint", ok, f"{errs} errors (nested-structure and dense-track warnings accepted)")
    if "layout" not in skip:
        rc, o = run(["node", f"{HERE}/check3d.mjs", f"{hf}/index.html"])
        bad = [k for k in ("CLIPPED", "OVERFLOW", "TEXT OVER PICTURE") if k in o]
        m = re.search(r"OVERLAPS\s+(\d+)", o)
        row("layout", rc == 0 and not bad, f"OVERLAPS {m.group(1) if m else '?'}" + (f"; {', '.join(bad)}" if bad else ""), o)
    if "frames" not in skip and os.path.exists(f"{root}/render/_beats.txt"):
        at = open(f"{root}/render/_beats.txt").read().strip()
        rc, o = run(["npx", "--yes", HF, "snapshot", ".", "--at", at], cwd=hf, timeout=1200)
        sheets = re.findall(r"(\S+contact-sheet\.jpg)", o)
        row("frames", rc == 0 and bool(sheets), (sheets[-1] if sheets else o[-200:]) + "  <- read it once, every frame")
    if a.render:
        mix = os.path.abspath(a.render)
        if "pace" not in skip:
            rc, o = run([PY, f"{HERE}/pace.py", mix])
            row("pace", rc == 0, " · ".join(l for l in o.splitlines() if l.startswith(("PACE", "COMPOSITION"))), o)
        if "sound" not in skip:
            rc, o = run([PY, f"{HERE}/listen.py", mix])
            row("sound", rc == 0 and "LISTEN PASS" in o, next((l for l in o.splitlines() if l.startswith("LISTEN")), o[-200:]), o)
        if "master" not in skip:
            rc, o = run([PY, f"{HERE}/master.py", mix], timeout=1800)
            ms = [l for l in o.splitlines() if l.startswith("MASTER")]
            row("master", rc == 0 and len(ms) >= 2, " · ".join(ms) or o[-200:], o)
    w = max(len(r[0]) for r in rows) if rows else 5
    print("| check | result | detail |\n| --- | --- | --- |")
    for n, r, d in rows:
        print(f"| {n:<{w}} | {r} | {d} |")
    if warns:
        print("\n" + "\n".join(warns[:40]))
    if skip:
        print(f"\nskipped: {', '.join(sorted(skip))} (say so in Status)")
    print("\nnot checked: how the voice and effects sound; whether the motion means something (read the frames)")
    fails = [r for r in rows if r[1] == "FAIL"]
    print(f"QA {'FAIL' if fails else 'PASS'}: {len(rows) - len(fails)} of {len(rows)} rows pass")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
