#!/usr/bin/env python3
"""The scheduled pull (Build §Schedule), from the vault root: python3 System/scripts/daily.py [--radar]
Runs youtube_analytics.py pull and analytics.py report; on Mondays (or with --radar) radar.py pull and report; then signals.py.
When the weekly OAuth token has expired it writes a banner at the top of Analytics/Report.md instead of failing silently:
the user re-runs `python3 System/scripts/youtube_auth.py` (brand account REDTAIL). Prints one line per step."""
import datetime, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable
REPORT = "Analytics/Report.md"
BANNER = "> **Re-auth needed** ({d}): the YouTube token expired, so these numbers are from the last good pull. Run `python3 System/scripts/youtube_auth.py` and pick REDTAIL.\n\n"


def step(name, *args):
    r = subprocess.run([PY, f"{HERE}/{args[0]}", *args[1:]], capture_output=True, text=True, timeout=1800)
    out = (r.stdout + r.stderr).strip().splitlines()
    print(f"{name}: {'ok' if r.returncode == 0 else 'FAILED'} · {out[-1][:160] if out else ''}")
    return r.returncode, "\n".join(out)


def banner(on):
    if not os.path.exists(REPORT): return
    s = open(REPORT, encoding="utf-8").read()
    s = "\n".join(l for l in s.split("\n") if not l.startswith("> **Re-auth needed**"))
    if on:
        i = s.find("\n# ")
        s = s[:i + 1] + BANNER.format(d=datetime.date.today()) + s[i + 1:] if i >= 0 else BANNER.format(d=datetime.date.today()) + s
    open(REPORT, "w", encoding="utf-8").write(s)


def main():
    rc, out = step("analytics pull", "youtube_analytics.py", "pull")
    expired = rc != 0 and ("HTTP 400" in out or "invalid_grant" in out or "HTTP Error 400" in out)
    if rc == 0:
        step("analytics report", "analytics.py", "report")
        step("comments pull", "comments.py", "pull")
    banner(expired)
    if not expired and (datetime.date.today().weekday() == 0 or "--radar" in sys.argv):
        if step("radar pull", "radar.py", "pull")[0] == 0:
            step("radar report", "radar.py", "report")
    step("signals", "signals.py")
    if expired:
        print("DAILY: re-auth needed (banner written in Analytics/Report.md)")


if __name__ == "__main__":
    main()
