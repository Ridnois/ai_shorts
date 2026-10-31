#!/usr/bin/env python3
"""Deep-first search helper (stdlib, read-only). Rules: System/Growth.md §Ideas
  python3 System/scripts/youtube_search.py "<query>" [more queries] [--days 365] [--short] [--min-ratio 3]
Per query: search.list (100 quota units), then each result's channel: median views of its last 10 uploads.
Prints outliers (views / channel median >= min-ratio) as Niche map rows. Token: youtube_auth.py (youtube.readonly)."""
import argparse, datetime, json, os, statistics, sys, urllib.parse, urllib.request
sys.path.insert(0, os.path.dirname(__file__))
import youtube_auth as ya  # loads .env, access_token, get

def main():
    p = argparse.ArgumentParser(); p.add_argument("q", nargs="+"); p.add_argument("--days", type=int, default=365)
    p.add_argument("--short", action="store_true"); p.add_argument("--min-ratio", type=float, default=3)
    a = p.parse_args()
    tok = ya.access_token()
    g = lambda path, **q: ya.get("https://www.googleapis.com/youtube/v3/" + path, tok, **q)
    after = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=a.days)).strftime("%Y-%m-%dT%H:%M:%SZ")
    med = {}  # channel -> median views of last 10 uploads (cache)
    for q in a.q:
        r = g("search", part="snippet", q=q, type="video", maxResults=25, publishedAfter=after, relevanceLanguage="en",
              **({"videoDuration": "short"} if a.short else {}))
        ids = [i["id"]["videoId"] for i in r["items"]]
        vs = g("videos", part="snippet,statistics,contentDetails", id=",".join(ids))["items"]
        print(f"\n## {q}")
        for v in vs:
            ch = v["snippet"]["channelId"]
            if ch not in med:
                up = "UU" + ch[2:]
                last = g("playlistItems", part="contentDetails", playlistId=up, maxResults=10)["items"]
                st = g("videos", part="statistics", id=",".join(i["contentDetails"]["videoId"] for i in last))["items"]
                med[ch] = statistics.median(int(s["statistics"].get("viewCount", 0)) for s in st) or 1
            views = int(v["statistics"].get("viewCount", 0)); ratio = views / med[ch]
            if ratio >= a.min_ratio:
                print(f"| https://youtu.be/{v['id']} | {views:,} ({ratio:.1f}x of {int(med[ch]):,}) | | {v['snippet']['title']} | {v['snippet']['channelTitle']} | |")

main()
