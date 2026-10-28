#!/usr/bin/env python3
"""Ears for the agent: measure what a mastered Short sounds like, so P7 has numbers instead of "not verified".

    python3 System/scripts/listen.py render/<v>.mp4          # or a .wav
    python3 System/scripts/listen.py render/<v>.mp4 --json

Reads only (ffmpeg, local, $0). Reports against the Playbook §5 targets:
  * loudness: integrated LUFS (target -14 +-1), true peak (-1 dBTP or lower), loudness range
  * silences: every gap of 0.3 s or more (start, length), flagged when over 0.9 s (a pause the take should not have)
  * dead air: the longest silence and the share of the runtime that is silent
  * clipping: samples at full scale
Exit 1 when a target fails. It cannot judge voice quality or whether an effect fits: that stays with the user (Workflow listening rubric).
"""
import argparse, json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mix_audio import loudness  # noqa: E402  (two-pass loudnorm measure, EBU R128)


def ff(args):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", args[0]] + args[1:] + ["-f", "null", "-"],
                       capture_output=True, text=True)
    if r.returncode:
        raise SystemExit("ffmpeg failed: " + r.stderr[-800:])
    return r.stderr


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                         capture_output=True, text=True).stdout
    return float(out)


def silences(path, floor=-45, min_len=0.3):
    err = ff([path, "-af", f"silencedetect=n={floor}dB:d={min_len}"])
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", err)]
    ends = [(float(a), float(b)) for a, b in re.findall(r"silence_end: ([\d.]+) \| silence_duration: ([\d.]+)", err)]
    return [(round(e - d, 2), round(d, 2)) for e, d in ends] + ([(round(starts[-1], 2), None)] if len(starts) > len(ends) else [])


def clipped(path):
    err = ff([path, "-af", "astats=metadata=0:measure_perchannel=Number_of_samples+Peak_level"])
    peaks = [float(x) for x in re.findall(r"Peak level dB: (-?[\d.inf]+)", err) if x != "-inf"]
    return max(peaks) if peaks else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    dur, lo = duration(a.file), loudness(a.file)
    gaps = silences(a.file)
    closed = [g for g in gaps if g[1] is not None]
    sil = sum(g[1] for g in closed)
    inner = [g for g in closed if g[0] > 0.3 and g[0] + g[1] < dur - 0.1]   # the lead-in at 0 s and the tail at the end are designed
    odd = [g for g in inner if g[1] > 0.9]
    peak = clipped(a.file)
    fails = []
    if abs(lo["input_i"] + 14) > 1:
        fails.append(f"loudness {lo['input_i']:.1f} LUFS is not -14 +-1")
    if lo["input_tp"] > -1.0:
        fails.append(f"true peak {lo['input_tp']:.1f} dBTP is above -1")
    if peak is not None and peak >= -0.1:
        fails.append(f"sample peak {peak:.2f} dBFS: clipping")
    if inner and max(g[1] for g in inner) > 1.2:
        fails.append(f"dead air of {max(g[1] for g in inner):.2f} s")
    rep = {"duration_s": round(dur, 2), "lufs": lo["input_i"], "true_peak_dbtp": lo["input_tp"], "lra": lo["input_lra"],
           "sample_peak_dbfs": peak, "silent_share": round(sil / dur, 3), "silences": closed, "odd_gaps": odd, "fails": fails}
    if a.json:
        print(json.dumps(rep))
    else:
        print(f"LISTEN {os.path.basename(a.file)}: {dur:.1f} s, {lo['input_i']:.1f} LUFS, true peak {lo['input_tp']:.1f} dBTP, "
              f"LRA {lo['input_lra']:.1f}, sample peak {peak} dBFS, silent {rep['silent_share'] * 100:.0f} %")
        print("  silences (start, length): " + (", ".join(f"{s}s {d}s" for s, d in closed) or "none"))
        if odd:
            print("  OVER 0.9 s: " + ", ".join(f"{s}s {d}s" for s, d in odd))
        print("  " + ("FAIL: " + "; ".join(fails) if fails else "PASS targets (voice quality and effect fit are not measured)"))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
