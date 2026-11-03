#!/usr/bin/env python3
"""Outlier radar on the watchlist (stdlib, read-only on YouTube). Rules: System/Strategy.md §Ideas
  python3 System/scripts/radar.py pull [--pages 2]       # every channel in Research/Channels.md -> Research/radar.csv
  python3 System/scripts/radar.py report [--days 90]     # Research/Radar.md (GENERATED)
  python3 System/scripts/radar.py discover "<query>" ... # search.list: channels not yet on the watchlist (no scoring)
Score: views / median views of the same channel's same-format uploads older than 7 days (a Short is <= 180 s).
Videos 7 days old or younger are scored on views per day against that channel's same-format median views per day
of uploads 7 to 60 days old, and flagged `early` (young Shorts run hot: read them as a lead, not a result).
Cost: about 1 unit per call; channels.list batches 50 ids; a full pull of 25 channels at 2 pages is about 101 units.
Run from the vault root (.env); token: youtube_auth.py."""
import argparse, csv, datetime as dt, os, re, statistics, sys
sys.path.insert(0, os.path.dirname(__file__))
import youtube_auth as ya

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CHANNELS = os.path.join(ROOT, "Research", "Channels.md")
CSV = os.path.join(ROOT, "Research", "radar.csv")
MD = os.path.join(ROOT, "Research", "Radar.md")
API = "https://www.googleapis.com/youtube/v3/"
FIELDS = ["pulled_at", "video_id", "channel", "handle", "kind", "title", "format", "duration_s", "published",
          "age_d", "views", "likes", "comments", "ratio", "early"]
# series keywords (Strategy.md §Series); a title can carry several
SERIES = {
    "How AI works": r"\b(how|why)\b.*\b(ai|llm|gpt|chatgpt|claude|gemini|model|token|neural|transformer|attention)\b|"
                    r"\b(token|embedding|attention|transformer|hallucinat|quantiz|context window|diffusion|neural)",
    "Agent at work": r"\b(agent|agents|claude code|codex|cursor|copilot|automat|mcp|workflow|vibe cod|prompt)",
    "What's coming": r"\b(job|jobs|replace|power|energy|nuclear|data ?cent|chip|nvidia|gpu|agi|future|law|ban|regulat|bubble|cost|expensive|price)",
}
NOW = dt.datetime.now(dt.timezone.utc)


def watchlist():
    rows = []
    for line in open(CHANNELS, encoding="utf-8"):
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) >= 4 and re.fullmatch(r"UC[\w-]{22}", c[1]):
            rows.append({"handle": c[0], "id": c[1], "kind": c[3]})
    return rows


def secs(iso):
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m: return 0
    d, h, mi, s = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + s


def pull(a):
    tok = ya.access_token()
    g = lambda path, **q: ya.get(API + path, tok, **q)
    wl = watchlist(); units = 0; out = []
    info = {}
    for i in range(0, len(wl), 50):
        r = g("channels", part="contentDetails,snippet", id=",".join(c["id"] for c in wl[i:i + 50])); units += 1
        for it in r.get("items", []):
            info[it["id"]] = (it["contentDetails"]["relatedPlaylists"]["uploads"], it["snippet"]["title"])
    stamp = NOW.strftime("%Y-%m-%dT%H:%MZ")
    for c in wl:
        if c["id"] not in info:
            print(f"skip {c['handle']}: channel not found"); continue
        up, title = info[c["id"]]; ids = []; tokn = None
        for _ in range(a.pages):
            q = dict(part="contentDetails", playlistId=up, maxResults=50, **({"pageToken": tokn} if tokn else {}))
            r = g("playlistItems", **q); units += 1
            ids += [x["contentDetails"]["videoId"] for x in r.get("items", [])]
            tokn = r.get("nextPageToken")
            if not tokn: break
        vids = []
        for i in range(0, len(ids), 50):
            r = g("videos", part="snippet,statistics,contentDetails", id=",".join(ids[i:i + 50])); units += 1
            vids += r.get("items", [])
        rows = []
        for v in vids:
            pub = dt.datetime.fromisoformat(v["snippet"]["publishedAt"].replace("Z", "+00:00"))
            age = max((NOW - pub).total_seconds() / 86400, 0.1)
            d = secs(v["contentDetails"].get("duration"))
            if d == 0: continue  # live or premiere placeholder
            st = v.get("statistics", {})
            rows.append(dict(video_id=v["id"], title=v["snippet"]["title"], format="short" if d <= 180 else "long",
                             duration_s=d, published=pub.strftime("%Y-%m-%d"), age_d=round(age, 1),
                             views=int(st.get("viewCount", 0)), likes=int(st.get("likeCount", 0)),
                             comments=int(st.get("commentCount", 0))))
        for fmt in ("short", "long"):
            grp = [r for r in rows if r["format"] == fmt]
            mature = [r["views"] for r in grp if r["age_d"] > 7]
            rate = [r["views"] / r["age_d"] for r in grp if 7 < r["age_d"] <= 60]
            med = statistics.median(mature) if mature else 0
            med_rate = statistics.median(rate) if rate else (med / 30 if med else 0)
            for r in grp:
                if r["age_d"] > 7:
                    r["ratio"] = round(r["views"] / med, 2) if med else ""; r["early"] = ""
                else:
                    r["ratio"] = round(r["views"] / r["age_d"] / med_rate, 2) if med_rate else ""; r["early"] = "early"
        for r in rows:
            r.update(pulled_at=stamp, channel=title, handle=c["handle"], kind=c["kind"])
        out += rows
        print(f"{c['handle']:24} {len(rows):3} uploads")
    new = not os.path.exists(CSV)
    with open(CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if new: w.writeheader()
        w.writerows(out)
    print(f"RADAR pulled {len(out)} videos from {len(info)} channels, about {units} quota units -> {os.path.relpath(CSV, ROOT)}")


def latest():
    if not os.path.exists(CSV): sys.exit("no Research/radar.csv: run `radar.py pull` first")
    rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
    pulls = sorted({r["pulled_at"] for r in rows})
    last = {}
    for r in rows: last[r["video_id"]] = r  # the file is in pull order: the newest row wins
    prev_ids = {r["video_id"] for r in rows if len(pulls) > 1 and r["pulled_at"] == pulls[-2]}
    return list(last.values()), pulls, prev_ids


def tags(title):
    t = title.lower()
    return ", ".join(s for s, rx in SERIES.items() if re.search(rx, t)) or ""


def report(a):
    rows, pulls, prev = latest()
    cut = (NOW - dt.timedelta(days=a.days)).strftime("%Y-%m-%d")
    pick = [r for r in rows if r["ratio"] and float(r["ratio"]) >= a.min_ratio and r["published"] >= cut
            and float(r["age_d"]) >= 1]  # under a day the per-day rate is noise
    pick.sort(key=lambda r: -float(r["ratio"]))
    L = ["---", "type: research", f"updated: {NOW:%Y-%m-%d}",
         "status: GENERATED by System/scripts/radar.py report; do not edit by hand", "---", "",
         "# Radar: outliers on the watchlist", "",
         "← [[Channels]] (the watchlist) · [[Strategy]] §Ideas (how to use it) · [[Signals]]", "",
         f"Pulls: {len(pulls)} (latest {pulls[-1] if pulls else '-'}). {len(rows)} videos tracked. "
         f"Shown: published in the last {a.days} days and {a.min_ratio}x or more their channel's same-format median. "
         "`early` = 7 days old or younger, scored on views per day: a lead, not a result. "
         "Series is a keyword guess; the hook pattern and why people clicked are added when a row becomes an idea.", ""]
    for fmt, head in (("short", "Shorts (180 s or less)"), ("long", "Long videos")):
        g = [r for r in pick if r["format"] == fmt][: a.top]
        L += [f"## {head}", "", "| ratio | views | video | channel | age | series guess | new |",
              "| --- | --- | --- | --- | --- | --- | --- |"]
        for r in g:
            title = r["title"].replace("|", "/")
            L.append(f"| {float(r['ratio']):.1f}x{' early' if r['early'] else ''} | {int(r['views']):,} | "
                     f"[{title}](https://youtu.be/{r['video_id']}) | {r['handle']} | {float(r['age_d']):.0f} d | "
                     f"{tags(r['title'])} | {'new' if prev and r['video_id'] not in prev else ''} |")
        L.append("")
    by = {}
    for r in rows:
        if r["format"] == "short": by.setdefault(r["handle"], []).append(r)
    L += ["## Shorts use per channel (latest pull)", "", "| channel | Shorts | median Short views | best Short ratio |",
          "| --- | --- | --- | --- |"]
    for h, g in sorted(by.items(), key=lambda kv: -len(kv[1])):
        rs = [float(r["ratio"]) for r in g if r["ratio"]]
        L.append(f"| {h} | {len(g)} | {int(statistics.median(int(r['views']) for r in g)):,} | {max(rs) if rs else 0:.1f}x |")
    open(MD, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"RADAR report: {len(pick)} outliers -> {os.path.relpath(MD, ROOT)}")


def discover(a):
    tok = ya.access_token(); known = {c["id"] for c in watchlist()}; seen = {}
    for q in a.q:
        r = ya.get(API + "search", tok, part="snippet", q=q, type="video", maxResults=25, relevanceLanguage="en",
                   **({"videoDuration": "short"} if a.short else {}))
        for it in r.get("items", []):
            ch = it["snippet"]["channelId"]
            if ch not in known: seen.setdefault(ch, [it["snippet"]["channelTitle"], 0])[1] += 1
    if not seen: print("nothing new"); return
    ids = list(seen)[:50]
    st = {i["id"]: i for i in ya.get(API + "channels", tok, part="statistics,snippet", id=",".join(ids)).get("items", [])}
    print("| handle | channel_id | subs | kind | style | why it is here |")
    for ch, (title, n) in sorted(seen.items(), key=lambda kv: -kv[1][1]):
        s = st.get(ch, {})
        print(f"| {s.get('snippet', {}).get('customUrl', title)} | {ch} | {int(s.get('statistics', {}).get('subscriberCount', 0)):,} "
              f"| topic | ? | {n} hits for {a.q!r} |")
    print("(search.list costs 100 units and has its own daily cap: discovery only, never scoring)")


def main():
    p = argparse.ArgumentParser(); sp = p.add_subparsers(dest="cmd", required=True)
    x = sp.add_parser("pull"); x.add_argument("--pages", type=int, default=2)
    x = sp.add_parser("report"); x.add_argument("--days", type=int, default=90); x.add_argument("--min-ratio", type=float, default=3)
    x.add_argument("--top", type=int, default=40)
    x = sp.add_parser("discover"); x.add_argument("q", nargs="+"); x.add_argument("--short", action="store_true")
    a = p.parse_args(); {"pull": pull, "report": report, "discover": discover}[a.cmd](a)


if __name__ == "__main__":
    main()
