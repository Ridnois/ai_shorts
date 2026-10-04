"""Free stock photo search and download, with the license and attribution recorded.

Sources that work without an API key (checked 4 Oct 2026):
  - Openverse  (api.openverse.org): aggregates Flickr, Wikimedia, museums; has a license filter.
  - NASA images (images-api.nasa.gov): mostly public domain.
  - Wikimedia Commons: originals fetched directly from upload.wikimedia.org (the thumbnail API throttles).
Sources that need a free API key (ask the user before using): Pexels, Pixabay, Unsplash API.

    python3 System/scripts/stock_photos.py search "superconducting magnet" [--source openverse|nasa|commons] [--n 8]
    python3 System/scripts/stock_photos.py get <url> <dest.jpg> --title "..." --author "..." --license "CC BY 4.0" --page <url>

Every downloaded photo is appended to <dest folder>/_credits.jsonl (title, author, license, page): the video's
Status note copies it into its attribution table. Photos are resized to <= 1920 px.
"""
import argparse, hashlib, json, os, sys, time, urllib.parse, urllib.request

H = {"User-Agent": "youtube-vault-research/1.0 (personal project)"}


def _get(url, timeout=30, tries=3):
    for a in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=H), timeout=timeout).read()
        except Exception as e:  # network hiccups and throttling: back off and retry
            err = e
            time.sleep(3 * (a + 1))
    raise RuntimeError(f"{url}: {err}")


def openverse(q, n=8, commercial=True):
    u = "https://api.openverse.org/v1/images/?" + urllib.parse.urlencode(
        {"q": q, "page_size": n, "license_type": "commercial" if commercial else "all"})
    out = []
    for r in json.loads(_get(u))["results"]:
        out.append({"source": "openverse/" + r["source"], "title": r["title"], "author": r.get("creator") or "",
                    "license": f'{r["license"].upper()} {r.get("license_version") or ""}'.strip(), "url": r["url"],
                    "page": r.get("foreign_landing_url") or "", "size": (r.get("width"), r.get("height"))})
    return out


def nasa(q, n=8):
    u = "https://images-api.nasa.gov/search?" + urllib.parse.urlencode({"q": q, "media_type": "image"})
    out = []
    for it in json.loads(_get(u))["collection"]["items"][:n]:
        d = it["data"][0]
        big = it["links"][0]["href"].replace("~thumb", "~large").replace("~medium", "~large")
        out.append({"source": "nasa", "title": d["title"], "author": d.get("photographer") or d.get("center") or "NASA",
                    "license": "NASA media (generally public domain; check usage guidelines)", "url": big,
                    "page": "https://images.nasa.gov/details/" + d["nasa_id"], "size": None})
    return out


def commons(q, n=8):
    u = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(
        {"action": "query", "generator": "search", "gsrnamespace": 6, "gsrlimit": n, "gsrsearch": q, "prop": "imageinfo",
         "iiprop": "url|size|mime|extmetadata", "iiextmetadatafilter": "Artist|LicenseShortName", "format": "json"})
    out = []
    for p in sorted(json.loads(_get(u)).get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 0)):
        i = p["imageinfo"][0]
        if i["mime"] != "image/jpeg":
            continue
        em = i["extmetadata"]
        out.append({"source": "commons", "title": p["title"], "author": "", "license": em.get("LicenseShortName", {}).get("value", ""),
                    "url": i["url"], "page": "https://commons.wikimedia.org/wiki/" + p["title"].replace(" ", "_"),
                    "size": (i["width"], i["height"])})
    return out


def get(url, dest, **credit):
    """Downloads, resizes to <= 1920 px, saves as JPEG and records the credit."""
    from PIL import Image
    data = _get(url, timeout=60)
    tmp = dest + ".tmp"
    open(tmp, "wb").write(data)
    im = Image.open(tmp).convert("RGB")
    im.thumbnail((1920, 1920))
    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    im.save(dest, quality=92)
    os.remove(tmp)
    credit.update(file=os.path.basename(dest), url=url)
    with open(os.path.join(os.path.dirname(dest) or ".", "_credits.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps(credit, ensure_ascii=False) + "\n")
    return im.size


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(required=True)
    s = sub.add_parser("search"); s.add_argument("q"); s.add_argument("--source", default="openverse"); s.add_argument("--n", type=int, default=8)
    g = sub.add_parser("get"); g.add_argument("url"); g.add_argument("dest")
    for k in ("title", "author", "license", "page"):
        g.add_argument("--" + k, default="")
    a = ap.parse_args()
    if hasattr(a, "q"):
        for r in {"openverse": openverse, "nasa": nasa, "commons": commons}[a.source](a.q, a.n):
            print(f'{r["license"]:<28} {r["title"][:60]:<60} {r["author"][:24]:<24} {r["url"]}')
    else:
        print(get(a.url, a.dest, title=a.title, author=a.author, license=a.license, page=a.page))
