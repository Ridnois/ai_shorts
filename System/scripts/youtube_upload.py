#!/usr/bin/env python3
"""YouTube Data API v3 uploader (stdlib only). Setup and gotchas: System/Publish.md
  python3 System/scripts/youtube_upload.py auth                      # once: browser consent, prints YT_REFRESH_TOKEN
  python3 System/scripts/youtube_upload.py upload VIDEO.mp4 --title T --desc-file D.txt [--thumb T.jpg] [--privacy private]
Reads YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN from .env (vault root) or the environment."""
import argparse, http.server, json, os, sys, urllib.parse, urllib.request, urllib.error, webbrowser

for l in open(".env") if os.path.exists(".env") else []:
    k, _, v = l.strip().partition("=")
    if k and not k.startswith("#"): os.environ.setdefault(k, v)
CID, SEC = os.environ.get("YT_CLIENT_ID"), os.environ.get("YT_CLIENT_SECRET")
SCOPE = "https://www.googleapis.com/auth/youtube.upload"  # upload + thumbnails.set; cannot read or delete anything
PORT = 8765  # loopback redirect; the OAuth client type must be "Desktop app"
TOKEN = "https://oauth2.googleapis.com/token"


def post_form(url, data):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, urllib.parse.urlencode(data).encode())))


def auth():
    redirect = f"http://127.0.0.1:{PORT}"
    got = {}

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            got.update(urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query))
            self.send_response(200); self.end_headers(); self.wfile.write(b"Done, close this tab.")
        log_message = lambda *a: None

    url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode(dict(
        client_id=CID, redirect_uri=redirect, response_type="code", scope=SCOPE,
        access_type="offline", prompt="consent"))
    print("Open (pick the Redtail channel's Google account):\n" + url)
    webbrowser.open(url)
    http.server.HTTPServer(("127.0.0.1", PORT), H).handle_request()
    r = post_form(TOKEN, dict(code=got["code"][0], client_id=CID, client_secret=SEC,
                              redirect_uri=redirect, grant_type="authorization_code"))
    print("\nAdd to .env:\nYT_REFRESH_TOKEN=" + r["refresh_token"])


def access_token():
    return post_form(TOKEN, dict(client_id=CID, client_secret=SEC, grant_type="refresh_token",
                                 refresh_token=os.environ["YT_REFRESH_TOKEN"]))["access_token"]


def upload(a):
    tok = access_token()
    desc = open(a.desc_file).read() if a.desc_file else a.desc
    meta = dict(snippet=dict(title=a.title, description=desc, categoryId=a.category),
                status=dict(privacyStatus=a.privacy, selfDeclaredMadeForKids=False,
                            containsSyntheticMedia=True))  # AI-assisted channel: YouTube's altered/synthetic disclosure
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
        vid = json.load(urllib.request.urlopen(put, timeout=3600))["id"]
    print("uploaded", vid, f"https://studio.youtube.com/video/{vid}/edit", flush=True)
    if a.thumb:
        t = urllib.request.Request(
            f"https://www.googleapis.com/upload/youtube/v3/thumbnails/set?videoId={vid}", open(a.thumb, "rb").read(),
            {"Authorization": "Bearer " + tok, "Content-Type": "image/jpeg" if a.thumb.endswith("jpg") else "image/png"})
        try: urllib.request.urlopen(t); print("thumbnail set")
        except urllib.error.HTTPError as e: print("thumbnail failed (Shorts thumbnails need Partner Program):", e.code)


p = argparse.ArgumentParser()
s = p.add_subparsers(dest="cmd", required=True)
s.add_parser("auth")
u = s.add_parser("upload")
u.add_argument("video"); u.add_argument("--title", required=True)
u.add_argument("--desc", default=""); u.add_argument("--desc-file")
u.add_argument("--thumb"); u.add_argument("--privacy", default="private", choices=["private", "unlisted", "public"])
u.add_argument("--publish-at"); u.add_argument("--category", default="28")  # 28 = Science & Technology
a = p.parse_args()
if not CID or not SEC: sys.exit("Set YT_CLIENT_ID and YT_CLIENT_SECRET in .env (System/Publish.md)")
try:
    auth() if a.cmd == "auth" else upload(a)
except urllib.error.HTTPError as e:
    sys.exit(f"HTTP {e.code}: {e.read().decode()[:600]}")
