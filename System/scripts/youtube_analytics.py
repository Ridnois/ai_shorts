#!/usr/bin/env python3
"""YouTube Analytics puller (stdlib only, read-only). Rules: System/Growth.md §Analytics
  python3 System/scripts/youtube_analytics.py pull [--age 24h|7d|28d]   # all channel videos -> Analytics/snapshots.csv + Analytics/exports/<date>/*.json
Needs the YouTube Analytics API enabled in the same Google Cloud project. Token and channel check: youtube_auth.py."""
import argparse, csv, datetime, json, os, sys, urllib.error, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(__file__))
import analytics  # same folder: add() appends a snapshot row
from youtube_auth import access_token, get  # loads .env; refuses any channel but Next Token

METRICS = "views,engagedViews,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,likes,comments,shares,subscribersGained,subscribersLost"


def report(tok, **q):
    return get("https://youtubeanalytics.googleapis.com/v2/reports", tok, ids="channel==MINE", **q)


def hours_age(pub):
    h = int((datetime.datetime.now(datetime.timezone.utc) - datetime.datetime.fromisoformat(pub.replace("Z", "+00:00"))).total_seconds() // 3600)
    return f"{h}h" if h < 48 else f"{h // 24}d"


def pull(a):
    tok = access_token()
    today = datetime.date.today().isoformat()
    out = f"Analytics/exports/{today}"; os.makedirs(out, exist_ok=True)
    tbl = report(tok, startDate="2020-01-01", endDate=today, metrics=METRICS, dimensions="video", sort="-views", maxResults=200)
    json.dump(tbl, open(f"{out}/videos.json", "w"), indent=1)
    cols = [c["name"] for c in tbl["columnHeaders"]]
    rows = {r[0]: dict(zip(cols, r)) for r in tbl.get("rows", [])}  # empty for videos still inside Analytics' reporting lag
    up = get("https://www.googleapis.com/youtube/v3/channels", tok, part="contentDetails", mine="true")["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    ids = [i["snippet"]["resourceId"]["videoId"] for i in get("https://www.googleapis.com/youtube/v3/playlistItems", tok, part="snippet", playlistId=up, maxResults=50)["items"]]
    meta = get("https://www.googleapis.com/youtube/v3/videos", tok, part="snippet,status,statistics", id=",".join(ids))["items"]
    json.dump(meta, open(f"{out}/data-api.json", "w"), indent=1)
    names = {r["youtube_id"]: r["video"] for r in csv.DictReader(open(analytics.VID)) if r["youtube_id"]}
    for m in meta:
        vid, pub = m["id"], m["snippet"]["publishedAt"]
        age = a.age or hours_age(pub)
        name = names.get(vid, f"{m['snippet']['title']} [{vid}]")
        note = f"published={pub[:16]}Z; privacy={m['status']['privacyStatus']}"
        if vid in rows:  # full Analytics API row
            d = rows[vid]
            src = report(tok, startDate="2020-01-01", endDate=today, metrics="views", dimensions="insightTrafficSourceType", filters=f"video=={vid}")
            json.dump(src, open(f"{out}/sources-{vid}.json", "w"))
            total = sum(r[1] for r in src.get("rows", [])) or 1
            feed = sum(r[1] for r in src.get("rows", []) if r[0] == "SHORTS") * 100 / total
            try:  # retention curve: 100 points over the video's length, kept raw
                json.dump(report(tok, startDate="2020-01-01", endDate=today, metrics="audienceWatchRatio", dimensions="elapsedVideoTimeRatio",
                                 filters=f"video=={vid}"), open(f"{out}/retention-{vid}.json", "w"))
            except urllib.error.HTTPError as e: print("retention not available:", vid, e.code)
            analytics.add([name, "youtube", age, f"views={d['views']}", f"engaged_views={d['engagedViews']}", f"avg_view_s={d['averageViewDuration']}",
                           f"avg_pct_viewed={d['averageViewPercentage']:.1f}", f"likes={d['likes']}", f"comments={d['comments']}", f"shares={d['shares']}",
                           f"subs_gained={d['subscribersGained']}", f"feed_pct={feed:.0f}", f"notes=analytics api {today}; {note}; subs lost={d['subscribersLost']}"])
        else:  # Data API public counts only (instant, no retention or shares)
            st = m["statistics"]
            analytics.add([name, "youtube", age, f"views={st.get('viewCount', 0)}", f"likes={st.get('likeCount', 0)}",
                           f"comments={st.get('commentCount', 0)}", f"notes=data api counts {today} (analytics api had no row yet); {note}"])
    print(f"{len(meta)} video(s), {len(rows)} with Analytics rows; raw JSON in {out}/. Next: python3 System/scripts/analytics.py report")


def main():
    p = argparse.ArgumentParser(); s = p.add_subparsers(dest="cmd", required=True)
    q = s.add_parser("pull"); q.add_argument("--age")
    a = p.parse_args()
    try:
        pull(a)
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read().decode()[:700]}")


if __name__ == "__main__":
    main()
