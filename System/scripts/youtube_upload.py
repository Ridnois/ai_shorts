#!/usr/bin/env python3
"""YouTube Data API v3 uploader (stdlib only). Setup and gotchas: System/Growth.md §Publish
  python3 System/scripts/youtube_upload.py upload VIDEO.mp4 --title T --desc-file D.txt [--thumb T.jpg] [--privacy private]
  python3 System/scripts/youtube_upload.py thumb VIDEO_ID THUMB.jpg   # set or re-set a thumbnail later (one set right after upload can be overwritten while YouTube is still processing)
Token and channel check: youtube_auth.py (refuses any channel but Next Token)."""
import argparse, json, os, sys, urllib.parse, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(__file__))
from youtube_auth import CHANNEL_ID, access_token  # loads .env


def upload(a):
    tok = access_token()
    desc = open(a.desc_file).read() if a.desc_file else a.desc
    meta = dict(snippet=dict(title=a.title, description=desc, categoryId=a.category, defaultLanguage="en", defaultAudioLanguage="en",
                             tags=[t.strip() for t in a.tags.split(",") if t.strip()][:15]),
                # the label is for realistic altered or generated people, places or events; drawn animation with a stock
                # TTS narrator needs none (System/Growth.md §Policy); --synthetic sets it when a video shows realistic generated media
                status=dict(privacyStatus=a.privacy, selfDeclaredMadeForKids=False, containsSyntheticMedia=a.synthetic))
    if a.publish_at:  # RFC 3339 UTC, e.g. 2026-10-12T15:00:00Z; requires privacy=private
        meta["status"]["publishAt"] = a.publish_at
    size = os.path.getsize(a.video)
    req = urllib.request.Request(
        "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status",
        json.dumps(meta).encode(), {"Authorization": "Bearer " + tok, "Content-Type": "application/json",
                                    "X-Upload-Content-Length": str(size), "X-Upload-Content-Type": "video/mp4"})
    session = urllib.request.urlopen(req).headers["Location"]
    with open(a.video, "rb") as f:  # one streamed PUT; ponytail: no resume on a dropped connection, rerun re-uploads
        put = urllib.request.Request(session, f, {"Content-Length": str(size), "Content-Type": "video/mp4"}, method="PUT")
        res = json.load(urllib.request.urlopen(put, timeout=3600))
    vid = res["id"]
    print("uploaded", vid, f"https://studio.youtube.com/video/{vid}/edit", flush=True)
    if res["snippet"]["channelId"] != CHANNEL_ID:  # cannot happen after access_token's check; caught loudly if it ever does
        sys.exit(f"Uploaded to the wrong channel {res['snippet']['channelId']}: delete {vid} in YouTube Studio")
    if a.thumb:
        t = urllib.request.Request(
            f"https://www.googleapis.com/upload/youtube/v3/thumbnails/set?videoId={vid}", open(a.thumb, "rb").read(),
            {"Authorization": "Bearer " + tok, "Content-Type": "image/jpeg" if a.thumb.endswith("jpg") else "image/png"})
        try: urllib.request.urlopen(t); print("thumbnail set")
        except urllib.error.HTTPError as e: print("thumbnail failed (Shorts thumbnails need Partner Program):", e.code)


def thumb(a):
    r = urllib.request.urlopen(urllib.request.Request(
        f"https://www.googleapis.com/upload/youtube/v3/thumbnails/set?videoId={a.video_id}", open(a.file, "rb").read(),
        {"Authorization": "Bearer " + access_token(), "Content-Type": "image/jpeg" if a.file.endswith("jpg") else "image/png"}))
    print("thumbnail set", a.video_id, r.status)


p = argparse.ArgumentParser()
s = p.add_subparsers(dest="cmd", required=True)
th = s.add_parser("thumb"); th.add_argument("video_id"); th.add_argument("file")
u = s.add_parser("upload")
u.add_argument("video"); u.add_argument("--title", required=True)
u.add_argument("--desc", default=""); u.add_argument("--desc-file")
u.add_argument("--thumb"); u.add_argument("--privacy", default="private", choices=["private", "unlisted", "public"])
u.add_argument("--publish-at"); u.add_argument("--category", default="28")  # 28 = Science & Technology
u.add_argument("--tags", default=""); u.add_argument("--synthetic", action="store_true")
a = p.parse_args()
try:
    thumb(a) if a.cmd == "thumb" else upload(a)
except urllib.error.HTTPError as e:
    sys.exit(f"HTTP {e.code}: {e.read().decode()[:600]}")
