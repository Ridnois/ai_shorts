#!/usr/bin/env python3
"""Eyes on the pace: find where the picture of a render holds still, so "the pace in motion" has numbers instead of "not checked".

    python3 System/scripts/pace.py render/<v>.mp4          # world labels from ../hf/index.html when it is there
    python3 System/scripts/pace.py render/<v>.mp4 --json

Reads only (ffmpeg freezedetect, local, $0). Watches the picture zones above the captions (stage and deck, y 0 to BAND top,
from hfkit): captions change on every word and would hide a frozen picture. Against Format §4 "an event every 1.5 to 2 s,
nothing holds still over 3 s" and the swipe decision in the first seconds:
  FAIL  a still over 3 s anywhere, or over 1.5 s inside the first 3 s (the hook)
  WARN  a still of 2 to 3 s
Exit 1 on a FAIL. Calibrated on 30 Oct 2026 against the frame audits of four renders (it found every dead stretch they
named, plus frozen openings they missed). It cannot judge whether a motion means anything: that stays with the frame audit.
"""
import argparse, json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hfkit import BAND  # noqa: E402  (captions own y BAND[0]..BAND[1])

NOISE, MIN = 0.002, 1.5      # freezedetect: difference under -54 dB at 270 px wide counts as still; report stills of 1.5 s or more
HOOK, WARN, FAIL = 3.0, 2.0, 3.0


def duration(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                                capture_output=True, text=True).stdout)


def stills(path):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-an", "-vf",
                        f"crop=iw:{BAND[0]}:0:0,scale=270:-2,freezedetect=n={NOISE}:d={MIN}", "-f", "null", "-"], capture_output=True, text=True)
    if r.returncode:
        raise SystemExit("ffmpeg failed: " + r.stderr[-800:])
    starts = [float(x) for x in re.findall(r"freeze_start: ([\d.]+)", r.stderr)]
    ends = [float(x) for x in re.findall(r"freeze_end: ([\d.]+)", r.stderr)]
    end = duration(path)
    return [(s, (ends[i] if i < len(ends) else end) - s) for i, s in enumerate(starts)]  # a still running into the end has no freeze_end


def worlds(path):
    """[(start, id)] from the build's hf/index.html (render/ and hf/ are siblings)."""
    page = os.path.join(os.path.dirname(os.path.abspath(path)), "..", "hf", "index.html")
    if not os.path.exists(page):
        return []
    return sorted((float(s), w) for w, s in re.findall(r'id="(w\d+)"[^>]*class="[^"]*\bworld\b[^"]*"[^>]*data-start="([\d.]+)"', open(page).read()))


def judge(path):
    ws, out = worlds(path), []
    for s, d in stills(path):
        w = next((w for t, w in reversed(ws) if t <= s + 0.05), "")
        level = "FAIL" if d > FAIL or (s < HOOK and d > MIN) else "WARN" if d >= WARN else "ok"
        out.append(dict(start=round(s, 1), seconds=round(d, 1), world=w, level=level, hook=s < HOOK))
    return out


if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("video"); p.add_argument("--json", action="store_true")
    a = p.parse_args()
    res = judge(a.video)
    if a.json:
        print(json.dumps(res, indent=1))
    else:
        for r in res:
            print(f"{r['level']:4}  still {r['seconds']:.1f} s at {r['start']:.1f} s" + (f" ({r['world']})" if r["world"] else "") + ("  <- the hook" if r["hook"] else ""))
        bad = [r for r in res if r["level"] == "FAIL"]
        print(f"PACE {'FAIL' if bad else 'PASS'}: {len(res)} still(s) of {MIN} s or more, {len(bad)} over the bar"
              + ("" if bad else ", none over 3 s or in the first 3 s over 1.5 s"))
    sys.exit(1 if any(r["level"] == "FAIL" for r in res) else 0)
