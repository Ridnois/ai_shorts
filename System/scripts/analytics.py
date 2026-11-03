#!/usr/bin/env python3
"""Channel metrics log.  From the vault root:
  python3 System/scripts/analytics.py add <video> youtube <24h|7d|28d> views=1200 viewed_pct=71 ...
  python3 System/scripts/analytics.py report          # rewrites Analytics/Report.md
  python3 System/scripts/analytics.py beats <video>   # where viewers left: the retention curve on the spoken words
Data: Analytics/videos.csv (what each video IS) and Analytics/snapshots.csv (what it DID); retention curves in
Analytics/exports/<date>/retention-<id>.json (youtube_analytics.py pull). viewed_pct (viewed vs swiped) is not in any
API: it is typed from Studio (Content > Shorts) at 24 h and 7 d. Rules: System/Data.md"""
import csv, datetime, glob, json, os, re, statistics, subprocess, sys

D = "Analytics"
SNAP, VID, REP = f"{D}/snapshots.csv", f"{D}/videos.csv", f"{D}/Report.md"
SCOLS = ["video", "platform", "age", "date", "views", "engaged_views", "viewed_pct", "avg_view_s", "avg_pct_viewed",
         "completion_pct", "likes", "comments", "shares", "saves", "subs_gained", "new_viewers_pct", "feed_pct", "notes"]
NUM = SCOLS[4:-1]
KEY = ["viewed_pct", "avg_pct_viewed", "engaged_views", "shares", "subs_gained"]  # the five that drive decisions


def rows(path):
    return list(csv.DictReader(open(path))) if os.path.exists(path) else []


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def med(vals):
    vals = [v for v in vals if v is not None]
    return statistics.median(vals) if vals else None


def fmt(v):
    return "" if v is None else (str(int(v)) if v == int(v) else f"{v:.1f}")


def add(argv):
    video, platform, age, *kv = argv
    r = dict.fromkeys(SCOLS, "")
    r.update(video=video, platform=platform, age=age, date=datetime.date.today().isoformat())
    for a in kv:
        k, _, v = a.partition("=")
        if k not in SCOLS:
            sys.exit(f"unknown column {k!r}; allowed: {', '.join(SCOLS)}")
        r[k] = v
    key = lambda x: (x["video"], x["platform"], x["date"])  # one snapshot per video, platform and day
    rows = [x for x in csv.DictReader(open(SNAP, newline="")) if key(x) != key(r)] if os.path.exists(SNAP) else []  # a re-pull replaces, never doubles
    with open(SNAP, "w", newline="") as f:
        w = csv.DictWriter(f, SCOLS)
        w.writeheader()
        w.writerows(rows + [r])
    print("added", video, platform, age)


def curve(yt_id):
    """Newest retention export for a video: [(ratio 0.01..1, audienceWatchRatio, relativeRetentionPerformance|None)]."""
    fs = sorted(glob.glob(f"{D}/exports/*/retention-{yt_id}.json"))
    if not fs: return None, None
    d = json.load(open(fs[-1])); cols = [c["name"] for c in d.get("columnHeaders", [])]
    pts = [(r[0], r[cols.index("audienceWatchRatio")],
            r[cols.index("relativeRetentionPerformance")] if "relativeRetentionPerformance" in cols else None) for r in d.get("rows", [])]
    return pts or None, fs[-1].split("/")[-2]


def media_dir(video):
    g = [p for p in glob.glob(f"Media/Week */*/{video}") if os.path.isdir(p)]
    return sorted(g)[-1] if g else None


def spoken(video):
    """Word timings of the newest take, shifted by the take's offset in the render (render/_timeline.json)."""
    m = media_dir(video)
    if not m: return []
    takes = sorted(glob.glob(f"{m}/voice/*.words.json"), key=os.path.getmtime)
    if not takes: return []
    off = 0.0
    try: off = json.load(open(f"{m}/render/_timeline.json"))["voices"][0]["at"]
    except Exception: pass
    return [(w, s + off, e + off) for w, s, e in json.load(open(takes[-1]))]


def scenes(video):
    """Scene starts from hf/beats.json when the video was built with beats.py: [(t, scene id)]; else []."""
    m = media_dir(video); b = f"{m}/hf/beats.json" if m else ""
    if not b or not os.path.exists(b): return []
    try:
        d = json.load(open(b)); ws = spoken(video); out = []
        for w in d.get("worlds", d.get("scenes", [])):
            at = w.get("at") or w.get("start")
            if isinstance(at, (int, float)): out.append((float(at), w.get("id", "?")))
        return sorted(out) if out else []
    except Exception:
        return []


def words_at(ws, t0, t1):
    return " ".join(w for w, s, e in ws if e >= t0 and s <= t1).strip()


def read_curve(video, dur, yt_id, frames=False):
    """hold at 3 s, the two biggest drops (time, words, scene), end value; None when no curve."""
    pts, date = curve(yt_id)
    if not pts or not dur: return None
    ws = spoken(video); sc = scenes(video)
    at = lambda t: min(pts, key=lambda p: abs(p[0] * dur - t))[1]
    start = pts[0][1] or 1
    # drop over a 2-point window (2 % of the length), non-overlapping, after the first second
    drops = sorted(((pts[i][1] - pts[i + 2][1], pts[i][0] * dur) for i in range(len(pts) - 2) if pts[i][0] * dur > 1),
                   reverse=True)
    pick = []
    for d, t in drops:
        if d <= 0: break
        if all(abs(t - u) > 4 for _, u in pick): pick.append((d, t))
        if len(pick) == 2: break
    rel = [p[2] for p in pts if p[2] is not None]
    def scene_at(t):
        cur = ""
        for s, i in sc:
            if s <= t: cur = i
        return cur
    out = dict(date=date, start=start, hold3=at(3), hold3_rel=at(3) / start, mid=at(dur / 2), end=pts[-1][1],
               rel=statistics.mean(rel) if rel else None,
               drops=[dict(t=t, size=d, words=words_at(ws, t - 0.8, t + 1.2), scene=scene_at(t)) for d, t in pick])
    if frames:
        m = media_dir(video); rs = sorted(glob.glob(f"{m}/render/*-9x16-r*.mp4"), key=os.path.getmtime) if m else []
        if rs:
            os.makedirs(f"{m}/render/_drops", exist_ok=True)
            for dr in out["drops"]:
                jpg = f"{m}/render/_drops/drop-{dr['t']:05.1f}s.jpg"
                subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{dr['t']:.2f}", "-i", rs[-1], "-frames:v", "1",
                                "-vf", "scale=360:-1", jpg])
                dr["frame"] = jpg
    return out


def beats(video):
    v = {r["video"]: r for r in rows(VID)}.get(video)
    if not v or not v["youtube_id"]: sys.exit(f"{video!r} has no youtube_id in {VID}")
    dur = num(v["duration_s"]); r = read_curve(video, dur, v["youtube_id"], frames=True)
    if not r: sys.exit(f"no retention curve for {video} ({v['youtube_id']}): run youtube_analytics.py pull (curves need ~100 views)")
    print(f"{video} ({dur:.0f} s), curve of {r['date']}")
    print(f"  start {r['start']:.2f} · at 3 s {r['hold3']:.2f} ({r['hold3_rel'] * 100:.0f} % of start) · at half {r['mid']:.2f} · end {r['end']:.2f}"
          + (f" · relative to similar videos {r['rel']:.2f} (0.5 = median)" if r["rel"] is not None else ""))
    print("  (audienceWatchRatio counts replays, so it can exceed 1 on Shorts; read the shape, not the level)")
    for k, d in enumerate(r["drops"], 1):
        print(f"  drop {k}: {d['t']:.1f} s, -{d['size']:.2f}{' in ' + d['scene'] if d['scene'] else ''}: \"{d['words']}\""
              + (f" · frame {d['frame']}" if d.get("frame") else ""))


WINDOWS = ["24h", "7d", "28d"]  # Data.md: pulls at about 24 h, 7 d and 28 d; any age lands in the nearest one


def window(age):
    h = int(age[:-1] or 0) * (24 if age.endswith("d") else 1)
    return "24h" if h < 72 else "7d" if h < 14 * 24 else "28d"


def report():
    vids = {v["video"]: v for v in rows(VID)}
    latest, legacy = {}, {}  # (video, platform, window) -> newest snapshot; legacy: uploads with no videos.csv row (Redtail era, strays)
    for r in rows(SNAP):
        (latest if r["video"] in vids else legacy)[(r["video"], r["platform"], window(r["age"]))] = r
    out = ["---", "type: research", f"created: {datetime.date.today()}", f"updated: {datetime.date.today()}",
           "status: GENERATED by System/scripts/analytics.py report; do not edit by hand", "tags: [analytics, metrics, report]",
           "---", "", "# Metrics report", "", "← [[YouTube Channel]] · [[Data]] (rules) · data: `Analytics/snapshots.csv`, `Analytics/videos.csv`", ""]
    n = len({k[0] for k in latest})
    out += [f"**{n} video(s) with data.** The channel's own medians below replace the third-party benchmarks once there are 10 ([[Data]]).",
            "views, likes and comments are live (Data API); every other column comes from the Analytics API, which lags a day or two: under 3 days old, compare views only.", ""]
    for plat in sorted({k[1] for k in latest}):
        for age in [w for w in WINDOWS if any(k[1] == plat and k[2] == w for k in latest)]:
            snaps = [r for k, r in latest.items() if k[1] == plat and k[2] == age]
            med_row = {c: med([num(r[c]) for r in snaps]) for c in NUM}
            out += [f"## {plat} at about {age} ({len(snaps)} videos)", "", "| video | age | " + " | ".join(NUM) + " |", "| --- | --- |" + " --- |" * len(NUM)]
            for r in sorted(snaps, key=lambda r: -(num(r["views"]) or 0)):
                out.append(f"| [[{r['video']} - Status]] | {r['age']} | " + " | ".join(fmt(num(r[c])) for c in NUM) + " |")
            out.append("| **median** | | " + " | ".join(fmt(med_row[c]) for c in NUM) + " |")
            small = [r["video"] for r in snaps if (num(r["views"]) or 0) < 100]
            if small:
                out += ["", "**Too few views to read percentages (< 100): " + ", ".join(small) + ".** Counts only; do not act on rates ([[Data]])."]
            low = [f"{r['video']}: {c} {fmt(num(r[c]))} < median {fmt(med_row[c])}" for r in snaps if len(snaps) >= 3
                   for c in KEY if num(r[c]) is not None and med_row[c] is not None and num(r[c]) < med_row[c]]
            out += ["", "Below the median (needs 3+ videos): " + ("; ".join(low) if low else "none"), ""]
            groups = {}
            for r in snaps:
                h = vids.get(r["video"], {}).get("hook_type", "")
                if h and num(r["viewed_pct"]) is not None:
                    groups.setdefault(h, []).append(num(r["viewed_pct"]))
            by_len = {}
            for r in snaps:                              # length test (Format §3): 45 s and under against longer cuts
                d = num(vids.get(r["video"], {}).get("duration_s", ""))
                if d is not None and num(r["avg_pct_viewed"]) is not None:
                    by_len.setdefault("45 s or less" if d <= 45 else "over 45 s", []).append(num(r["avg_pct_viewed"]))
            if len(by_len) > 1:
                out += ["By length (median avg_pct_viewed): " + "; ".join(f"{h} {fmt(med(v))} (n={len(v)})" for h, v in sorted(by_len.items())), ""]
            if len(groups) > 1:
                out += ["By hook type (median viewed_pct): " + "; ".join(f"{h} {fmt(med(v))} (n={len(v)})" for h, v in sorted(groups.items())), ""]
    if not latest:
        out.append("No snapshots yet. Add one with `analytics.py add` ([[Data]]).")
    # newest snapshot per video (any window), for the cross-video cuts
    newest = {}
    for (v, p, w), r in latest.items():
        if p == "youtube" and (v not in newest or r["date"] >= newest[v]["date"]): newest[v] = r
    readable = {v: r for v, r in newest.items() if (num(r["views"]) or 0) >= 100}
    if readable:
        out += ["## What each kind of video did (newest snapshot, 100+ views)", "",
                "Median engaged views and average % viewed per group. Groups of 1 are anecdotes. "
                "Series, hook pattern and main medium come from `videos.csv` (publish.json writes them).", "",
                "| cut | group | n | engaged_views | avg_pct_viewed | feed_pct |", "| --- | --- | --- | --- | --- | --- |"]
        for cut in ("series", "hook_pattern", "medium"):
            grp = {}
            for v, r in readable.items():
                grp.setdefault(vids.get(v, {}).get(cut) or "(not set)", []).append(r)
            for gname, rs in sorted(grp.items(), key=lambda kv: -(med([num(r["engaged_views"]) for r in kv[1]]) or 0)):
                out.append(f"| {cut} | {gname} | {len(rs)} | " + " | ".join(fmt(med([num(r[c]) for r in rs])) for c in ("engaged_views", "avg_pct_viewed", "feed_pct")) + " |")
        out.append("")
    reads = []
    for v, meta in sorted(vids.items()):
        if not meta.get("youtube_id") or v not in readable: continue
        r = read_curve(v, num(meta.get("duration_s")), meta["youtube_id"])
        if r: reads.append((v, r))
    if reads:
        out += ["## Where viewers leave (retention curve on the spoken words)", "",
                "`hold 3 s` = the curve at 3 s as a share of its start (the hook); drops = the two steepest falls, with the words "
                "spoken there. `rel` = relativeRetentionPerformance, 0.5 is the median of similar-length videos. "
                "Detail and frames: `analytics.py beats \"<video>\"`.", "",
                "| video | hold 3 s | end | rel | drop 1 | drop 2 |", "| --- | --- | --- | --- | --- | --- |"]
        for v, r in sorted(reads, key=lambda x: x[1]["hold3_rel"]):
            ds = [f"{d['t']:.0f} s \"{d['words'][:40]}\"" for d in r["drops"]] + ["", ""]
            out.append(f"| [[{v} - Status]] | {r['hold3_rel'] * 100:.0f} % | {r['end']:.2f} | {fmt(r['rel']) if r['rel'] is not None else ''} | {ds[0]} | {ds[1]} |")
        hs = [r["hold3_rel"] for _, r in reads]
        out += ["", f"Median hold at 3 s: {statistics.median(hs) * 100:.0f} % (n={len(hs)}).", ""]
    if legacy:  # kept out of every median above
        last = {}
        for k, r in legacy.items(): last[k[0]] = r if k[0] not in last or r["date"] >= last[k[0]]["date"] else last[k[0]]
        out += ["## Not in videos.csv (left out of the medians)", "",
                "Redtail-era uploads before the AI relaunch, and uploads the vault has no notes for. Newest snapshot each.", "",
                "| video | age | views | engaged_views | avg_pct_viewed | feed_pct |", "| --- | --- | --- | --- | --- | --- |"]
        for r in sorted(last.values(), key=lambda r: -(num(r["views"]) or 0)):
            out.append(f"| {r['video']} | {r['age']} | " + " | ".join(fmt(num(r[c])) for c in ("views", "engaged_views", "avg_pct_viewed", "feed_pct")) + " |")
        out.append("")
    open(REP, "w").write("\n".join(out) + "\n")
    print("wrote", REP)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "add" and len(sys.argv) >= 5:
        add(sys.argv[2:])
    elif cmd == "report":
        report()
    elif cmd == "beats" and len(sys.argv) == 3:
        beats(sys.argv[2])
    else:
        sys.exit(__doc__)
