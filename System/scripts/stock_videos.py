"""Free stock footage: search, download with the license recorded, look at it as frames, cut it to a 9:16 clip.

Sources (research 9 Oct 2026, Analytics/Reports/2026-10-09 Visual research.md):
  commons   Wikimedia Commons, no key. Per-file license: PD, CC0, CC BY, CC BY-SA kept; NC, ND and fair use dropped.
  pexels    needs PEXELS_API_KEY in .env (free). Pexels license: commercial use, no credit required (we credit anyway).
  pixabay   needs PIXABAY_API_KEY in .env (free). Content License: commercial use, no visible trademarks used commercially.
  nasa      images-api.nasa.gov, no key. Generally public domain; no NASA insignia, no implied endorsement.
  archive   Internet Archive, no key; only items whose licenseurl is public domain, CC BY or CC BY-SA (claims unverified).

    python3 System/scripts/stock_videos.py search "copper mine" [--source commons|pexels|pixabay|nasa|archive] [--n 8] [--vertical]
    python3 System/scripts/stock_videos.py get <url> <clips/_src/x-src-name.webm> --title ... --author ... --license ... --page ...
    python3 System/scripts/stock_videos.py look <clips/_src/file> [--n 8]          # frames with timestamps -> <file>.look.png
    python3 System/scripts/stock_videos.py cut <src> <clips/x-c01-name.mp4> --start 2.0 --dur 3.5 --focus 0.35 [--fps 24]

`cut` crops a 9:16 window centred on `--focus` (fraction of the source width; `--focus-y` for vertical sources wider
than 9:16 is not needed), scales to 1080x1920, drops the audio and encodes H.264 at the plan's fps (24). A 1080p landscape
source gives a 608 px wide crop (soft, fine for 3 to 4 s of b-roll, never for text); 4K gives full quality; never use
720p or lower except as an element inside a motion plate. Every download is appended to <dest folder>/_credits.jsonl.
"""
import argparse, hashlib, json, os, re, subprocess, sys, time, urllib.parse, urllib.request

UA = {"User-Agent": "youtube-vault-research/1.0 (personal project)"}
OK_LICENSES = ("public domain", "pd", "cc0", "cc by", "cc-by", "nasa")
ENV = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), ".env")


def key(name):
    if os.environ.get(name):
        return os.environ[name]
    if os.path.exists(ENV):
        for line in open(ENV):
            if line.startswith(name + "="):
                return line.split("=", 1)[1].strip()
    raise SystemExit(f"{name} is not in .env: it is a free key the user creates (see the docstring); ask before using this source")


def _get(url, headers=None, timeout=40, tries=3):
    err = None
    for a in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers={**UA, **(headers or {})}), timeout=timeout).read()
        except Exception as e:  # throttling and hiccups: back off
            err = e
            time.sleep(3 * (a + 1))
    raise RuntimeError(f"{url}: {err}")


def licensed(lic):
    l = (lic or "").lower()
    return any(k in l for k in OK_LICENSES) and not any(k in l for k in ("nc", "nd", "fair use", "non-commercial"))


def commons(q, n, vertical):
    s = f"{q} filetype:video" + (" fileh:>1900 filew:<1100" if vertical else "")
    u = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(
        {"action": "query", "generator": "search", "gsrsearch": s, "gsrnamespace": 6, "gsrlimit": n * 2, "prop": "videoinfo",
         "viprop": "url|size|mime|derivatives|extmetadata", "format": "json", "formatversion": 2})
    out = []
    for p in sorted(json.loads(_get(u)).get("query", {}).get("pages", []), key=lambda p: p.get("index", 0)):
        vi = p["videoinfo"][0]
        md = vi.get("extmetadata", {})
        lic = md.get("LicenseShortName", {}).get("value", "")
        if not licensed(lic):
            continue
        best = (vi.get("width", 0), vi.get("height", 0), vi["url"])           # the original, unless it is huge
        ders = sorted((d for d in vi.get("derivatives", []) if d.get("height")), key=lambda d: d["height"])
        if max(best[0], best[1]) > 2200 or vi.get("size", 0) > 250e6:
            fit = [d for d in ders if max(d["width"], d["height"]) <= 2200]
            if fit:
                best = (fit[-1]["width"], fit[-1]["height"], fit[-1]["src"])
        out.append({"source": "commons", "title": p["title"].replace("File:", ""), "author": re.sub("<[^>]+>", "", md.get("Artist", {}).get("value", ""))[:80],
                    "license": lic, "url": best[2], "page": vi["descriptionurl"], "size": best[:2], "duration": round(vi.get("duration", 0), 1)})
    return out[:n]


def pexels(q, n, vertical):
    u = "https://api.pexels.com/videos/search?" + urllib.parse.urlencode(
        {"query": q, "per_page": n, "size": "medium", **({"orientation": "portrait"} if vertical else {})})
    out = []
    for v in json.loads(_get(u, {"Authorization": key("PEXELS_API_KEY")}))["videos"]:
        fs = sorted((f for f in v["video_files"] if f.get("height") and max(f["width"], f["height"]) <= 4096), key=lambda f: f["height"])
        if not fs:
            continue
        f = fs[-1]
        out.append({"source": "pexels", "title": v["url"].rstrip("/").split("/")[-1], "author": v["user"]["name"],
                    "license": "Pexels License", "url": f["link"], "page": v["url"], "size": (f["width"], f["height"]), "duration": v["duration"]})
    return out


def pixabay(q, n, vertical):
    u = "https://pixabay.com/api/videos/?" + urllib.parse.urlencode({"key": key("PIXABAY_API_KEY"), "q": q, "per_page": max(3, n)})
    out = []
    for v in json.loads(_get(u))["hits"]:
        f = v["videos"].get("large") or v["videos"]["medium"]
        if not f.get("url"):
            f = v["videos"]["medium"]
        if vertical and f["height"] < f["width"]:
            continue
        out.append({"source": "pixabay", "title": v.get("tags", ""), "author": v["user"], "license": "Pixabay Content License",
                    "url": f["url"], "page": v["pageURL"], "size": (f["width"], f["height"]), "duration": v["duration"]})
    return out[:n]


def nasa(q, n, vertical):
    u = "https://images-api.nasa.gov/search?" + urllib.parse.urlencode({"q": q, "media_type": "video", "page_size": n})
    out = []
    for it in json.loads(_get(u))["collection"]["items"][:n]:
        d = it["data"][0]
        files = json.loads(_get(it["href"].replace("http://", "https://").replace(" ", "%20")))
        mp4 = [f for f in files if f.endswith("~large.mp4")] or [f for f in files if f.endswith("~orig.mp4")] or [f for f in files if f.endswith(".mp4")]
        if not mp4:
            continue
        out.append({"source": "nasa", "title": d["title"], "author": d.get("center") or "NASA",
                    "license": "NASA media (public domain; no insignia or endorsement)", "url": mp4[0].replace("http://", "https://").replace(" ", "%20"),
                    "page": "https://images.nasa.gov/details/" + urllib.parse.quote(d["nasa_id"]), "size": None, "duration": None})
    return out


def archive(q, n, vertical):
    lic = r"(licenseurl:*publicdomain* OR licenseurl:*\/by\/* OR licenseurl:*\/by-sa\/*)"
    u = "https://archive.org/advancedsearch.php?" + urllib.parse.urlencode(
        {"q": f"({q}) AND mediatype:movies AND {lic}", "fl[]": ["identifier", "title", "licenseurl"], "rows": n, "output": "json"}, doseq=True)
    out = []
    for d in json.loads(_get(u))["response"]["docs"]:
        if d["identifier"].startswith("youtube-"):
            continue
        md = json.loads(_get(f"https://archive.org/metadata/{d['identifier']}"))
        vids = [f for f in md.get("files", []) if f["name"].lower().endswith((".mp4", ".webm", ".mov", ".mpeg", ".ogv"))]
        if not vids:
            continue
        f = max(vids, key=lambda f: int(f.get("height") or 0) * 10 ** 6 + int(float(f.get("size") or 0) // 1000))
        out.append({"source": "archive", "title": d.get("title", ""), "author": md["metadata"].get("creator") or md["metadata"].get("uploader", ""),
                    "license": d.get("licenseurl", ""), "url": f"https://archive.org/download/{d['identifier']}/{urllib.parse.quote(f['name'])}",
                    "page": f"https://archive.org/details/{d['identifier']}", "size": (f.get("width"), f.get("height")), "duration": f.get("length")})
    return out


SOURCES = {"commons": commons, "pexels": pexels, "pixabay": pixabay, "nasa": nasa, "archive": archive}


def cmd_search(a):
    res = SOURCES[a.source](a.q, a.n, a.vertical)
    for i, r in enumerate(res, 1):
        sz = "x".join(str(x) for x in r["size"]) if r.get("size") and r["size"][0] else "?"
        print(f"{i}. [{r['source']}] {r['title'][:70]} | {sz} | {r.get('duration') or '?'} s | {r['license']} | {r['author'][:40]}")
        print(f"   {r['url']}\n   {r['page']}")
    if not res:
        print("no licensed results")


def cmd_get(a):
    if not licensed(a.license) and not a.license.lower().startswith(("pexels", "pixabay")):
        raise SystemExit(f"license '{a.license}' is not one we use (PD, CC0, CC BY, CC BY-SA, Pexels, Pixabay)")
    os.makedirs(os.path.dirname(os.path.abspath(a.dest)), exist_ok=True)
    req = urllib.request.Request(a.url, headers=UA)
    h = hashlib.sha256()
    with urllib.request.urlopen(req, timeout=120) as r, open(a.dest, "wb") as f:
        while True:
            b = r.read(1 << 20)
            if not b:
                break
            f.write(b)
            h.update(b)
    info = probe(a.dest)
    rec = {"file": os.path.basename(a.dest), "title": a.title, "author": a.author, "license": a.license, "page": a.page,
           "url": a.url, "sha256": h.hexdigest(), "downloaded": time.strftime("%Y-%m-%d"), **info}
    with open(os.path.join(os.path.dirname(os.path.abspath(a.dest)), "_credits.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print("saved", a.dest, info, "| credit logged" + (" | CC BY-SA: credit with the license link" if "sa" in a.license.lower() else ""))


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate:format=duration",
                          "-of", "json", path], capture_output=True, text=True).stdout
    j = json.loads(out or "{}")
    st = (j.get("streams") or [{}])[0]
    return {"width": st.get("width"), "height": st.get("height"), "fps": st.get("r_frame_rate"),
            "duration": round(float(j.get("format", {}).get("duration", 0) or 0), 2)}


def cmd_look(a):
    info = probe(a.src)
    dur = info["duration"] or 1
    font = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
    dst = os.path.splitext(a.src)[0] + ".look.png"
    vf = (f"setpts=PTS-STARTPTS,fps={a.n / dur:.5f},scale=480:-2,drawtext=fontfile={font}:text='%{{pts\\:hms}}':x=10:y=10:fontsize=26:"
          f"fontcolor=white:box=1:boxcolor=black@0.6,tile={min(a.n, 4)}x{-(-a.n // 4)}")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", a.src, "-vf", vf, "-frames:v", "1", dst], check=True)
    print("frames", dst, info)


def cmd_cut(a):
    info = probe(a.src)
    w, h = info["width"], info["height"]
    if w / h > 9 / 16:                      # landscape (or square): a 9:16 window at the focus point
        crop = f"crop=w=trunc(ih*9/32)*2:h=ih:x=min(max(0\\,{a.focus}*iw-ow/2)\\,iw-ow):y=0,"
        width = 2 * int(h * 9 / 32)
    else:                                   # already vertical or taller: cover-fit
        crop, width = "", w
    vf = f"{crop}scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,setsar=1,fps={a.fps},format=yuv420p"
    os.makedirs(os.path.dirname(os.path.abspath(a.dest)), exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(a.start), "-t", str(a.dur), "-i", a.src, "-an", "-vf", vf,
                    "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-movflags", "+faststart", a.dest], check=True)
    print("cut", a.dest, f"{a.dur} s from {a.start} s, crop {width}px wide from {w}x{h}" + (" (SOFT: under 900 px)" if width < 900 else ""))


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("search")
    s.add_argument("q")
    s.add_argument("--source", default="commons", choices=SOURCES)
    s.add_argument("--n", type=int, default=8)
    s.add_argument("--vertical", action="store_true")
    g = sp.add_parser("get")
    g.add_argument("url")
    g.add_argument("dest")
    for k in ("title", "author", "license", "page"):
        g.add_argument("--" + k, required=k != "author", default="")
    lk = sp.add_parser("look")
    lk.add_argument("src")
    lk.add_argument("--n", type=int, default=8)
    c = sp.add_parser("cut")
    c.add_argument("src")
    c.add_argument("dest")
    c.add_argument("--start", type=float, default=0.0)
    c.add_argument("--dur", type=float, default=4.0)
    c.add_argument("--focus", type=float, default=0.5)
    c.add_argument("--fps", type=int, default=24)
    a = ap.parse_args()
    {"search": cmd_search, "get": cmd_get, "look": cmd_look, "cut": cmd_cut}[a.cmd](a)


if __name__ == "__main__":
    main()
