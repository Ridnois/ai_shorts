#!/usr/bin/env python3
"""YouTube OAuth for the vault (stdlib only). Every YouTube script gets its token here, and every token is checked to belong
to the Next Token channel before it is used: a token for any other channel (the owner's personal one) stops the script.
  python3 System/scripts/youtube_auth.py        # browser consent (weekly while the OAuth app is in Testing); saves YT_REFRESH_TOKEN to .env
  python3 System/scripts/youtube_auth.py check  # prints the channel the saved token reaches
Reads YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN from .env (vault root, gitignored). Tokens are never printed."""
import http.server, json, os, sys, urllib.error, urllib.parse, urllib.request, webbrowser

CHANNEL_ID = "UCCZX7-YPNPntwPKI1hdv2hQ"  # NextToken, @yournexttoken (the Redtail channel renamed); public, safe to commit
SCOPE = " ".join("https://www.googleapis.com/auth/" + s for s in (
    "youtube.upload",           # videos.insert, thumbnails.set
    "youtube.readonly",         # channel check, uploads list, outlier search
    "yt-analytics.readonly"))   # retention and engaged views
PORT, TOKEN = 8765, "https://oauth2.googleapis.com/token"  # loopback redirect: the OAuth client type must be "Desktop app"
ENV = ".env"

for l in open(ENV) if os.path.exists(ENV) else []:
    k, _, v = l.strip().partition("=")
    if k and not k.startswith("#"): os.environ.setdefault(k, v)
CID, SEC = os.environ.get("YT_CLIENT_ID"), os.environ.get("YT_CLIENT_SECRET")


def post_form(url, data):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, urllib.parse.urlencode(data).encode())))


def get(url, tok, **q):
    return json.load(urllib.request.urlopen(urllib.request.Request(url + "?" + urllib.parse.urlencode(q), headers={"Authorization": "Bearer " + tok})))


def channel(tok):
    items = get("https://www.googleapis.com/youtube/v3/channels", tok, part="snippet", mine="true").get("items", [])
    return (items[0]["id"], items[0]["snippet"]["title"]) if items else (None, "no channel")


def require_channel(tok):
    cid, title = channel(tok)
    if cid != CHANNEL_ID:
        sys.exit(f"Wrong YouTube channel: the token reaches '{title}' ({cid}), not Next Token ({CHANNEL_ID}). "
                 "Run python3 System/scripts/youtube_auth.py and pick the NextToken brand channel at the account step.")


def set_env(key, value):
    """Replace or add one line of .env, kept owner-only (0600)."""
    lines = [l for l in (open(ENV).read().splitlines() if os.path.exists(ENV) else []) if not l.startswith(key + "=")]
    fd = os.open(ENV + ".tmp", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f: f.write("\n".join(lines + [f"{key}={value}"]) + "\n")
    os.replace(ENV + ".tmp", ENV)


_tok = None
def access_token():
    """A fresh access token, checked once per run against CHANNEL_ID."""
    global _tok
    if not _tok:
        if not CID or not SEC: sys.exit("Set YT_CLIENT_ID and YT_CLIENT_SECRET in .env (System/Growth.md §Publish)")
        if not os.environ.get("YT_REFRESH_TOKEN"): sys.exit("No YT_REFRESH_TOKEN in .env: run python3 System/scripts/youtube_auth.py")
        try:
            _tok = post_form(TOKEN, dict(client_id=CID, client_secret=SEC, grant_type="refresh_token",
                                         refresh_token=os.environ["YT_REFRESH_TOKEN"]))["access_token"]
        except urllib.error.HTTPError as e:  # 400 invalid_grant: the weekly expiry, or a token from before the scopes changed
            sys.exit(f"Token refresh failed (HTTP {e.code}): run python3 System/scripts/youtube_auth.py")
        require_channel(_tok)
    return _tok


def auth():
    redirect, got = f"http://127.0.0.1:{PORT}", {}

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            got.update(urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query))
            self.send_response(200); self.end_headers(); self.wfile.write(b"Done, close this tab.")
        log_message = lambda *a: None

    url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode(dict(
        client_id=CID, redirect_uri=redirect, response_type="code", scope=SCOPE, access_type="offline", prompt="consent"))
    print("Open, and at 'Choose an account or brand account' pick NextToken (not the personal channel):\n" + url, flush=True)
    webbrowser.open(url)
    http.server.HTTPServer(("127.0.0.1", PORT), H).handle_request()
    if "code" not in got: sys.exit(f"Consent not given: {got.get('error', ['no code'])[0]}")
    r = post_form(TOKEN, dict(code=got["code"][0], client_id=CID, client_secret=SEC, redirect_uri=redirect, grant_type="authorization_code"))
    require_channel(r["access_token"])  # a wrong pick is refused before anything is saved
    set_env("YT_REFRESH_TOKEN", r["refresh_token"])
    print("saved YT_REFRESH_TOKEN to .env (Next Token channel)")


if __name__ == "__main__":
    if not CID or not SEC: sys.exit("Set YT_CLIENT_ID and YT_CLIENT_SECRET in .env (System/Growth.md §Publish)")
    try:
        if sys.argv[1:] == ["check"]: print("ok:", *channel(access_token()))
        else: auth()
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read().decode()[:600]}")
