#!/usr/bin/env python3
"""P8 in one command (stdlib + Pillow). The agent writes ONE small JSON, runs this, and reads a ~10 line result.

    python3 System/scripts/publish.py "Media/Week NN/<Day>/<Video>/upload/publish.json" [--dry-run] [--resume <youtube_id>]

Does, in order: thumbnail (make_thumbnail.compose) -> description (claim, sources, auto photo credits from stock/_credits.jsonl,
AI line, hashtags; ASCII only) -> upload (youtube_upload.py, private unless the JSON says otherwise) -> waits until YouTube has
processed the video -> sets the thumbnail again -> checks that the thumbnail YouTube serves is ours (pixel compare, no image to
look at) -> Analytics/videos.csv row -> Upload note -> Status stage 8 + index row -> analytics pull + report -> check_vault.
--dry-run stops after the thumbnail and the description. --resume <id> skips the upload (use after a crash).

publish.json (all keys required unless marked):
  media      "Media/Week 01/2026-10-05 Mon/Deep-sea"        render  "render/dn-62s-9x16-r1.mp4"
  video_name "Deep-sea nodules"  (the notes folder, Status and Script names)      title  "..."
  claim      the first two lines of the description (claim and search words)
  sources    [["what it supports", "https://..."], ...]       caveats  "one or two sentences" (optional)
  hashtags   "#a #b #c"            privacy  "private"|"public"|"unlisted" (optional, default private)
  thumb      {"hero": "stock/x.jpg", "lines": ["TOP", "BOTTOM"], "hot": 1, "kicker": "TOPIC TAG", "chips": ["FACT ONE", "FACT TWO", "FACT THREE"]}
             (kicker and up to 3 chips are the "more info" layer, 6 Oct 2026: each chip a sourced figure or the video's three key terms, <= 26 characters)
  hook_type  "stakes"             pinned  "pinned comment text"           approval  "the user's words"
  claims     [["claim", "source", "strength"], ...] (optional)            alt_titles ["...", "..."] (optional)
"""
import csv, glob, json, os, re, subprocess, sys, time, unicodedata, urllib.parse, urllib.request
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
for l in open(".env") if os.path.exists(".env") else []:
    k, _, v = l.strip().partition("=")
    if k and not k.startswith("#"): os.environ.setdefault(k, v)
PY = sys.executable


def run(*a):
    r = subprocess.run([PY, *a], capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr)


def ascii_(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().replace("<", "").replace(">", "")


def credits(media, plan):
    used = set()
    for sc in plan["scenes"]:
        for pl in sc["plates"]:
            for f in (pl["file"], pl.get("bg_photo"), (pl.get("inset") or {}).get("file")):
                if f: used.add(os.path.basename(f))
    cc, pd = {}, set()
    for l in open(f"{media}/stock/_credits.jsonl", encoding="utf-8"):
        d = json.loads(l); f = os.path.basename(d.get("file") or d.get("dest") or "")
        if f not in used: continue
        if re.search(r"CC BY", d["license"]): cc.setdefault((d["author"], d["license"]), 0)
        else: pd.add(d["author"])
    parts = [f"{a}, {lic}" for a, lic in cc]
    if pd: parts.append("Public domain and CC0 photos: " + ", ".join(sorted(pd)))
    return " | ".join(parts)


def description(cfg, plan):
    src = "\n".join(f"- {a}: {u}" for a, u in cfg["sources"])
    d = (f"{cfg['claim']}\n\nNew Shorts every day.\n\nSOURCES\n{src}\n"
         + (f"{cfg['caveats']} Figures checked on {datetime.now():%-d %B %Y}.\n" if cfg.get("caveats") else "")
         + f"\nPHOTO CREDITS (Wikimedia Commons)\n{credits(cfg['media'], plan)}\n\n"
         "The narration is AI-generated and the diagrams were drawn for this video; the photos are real.\n\n" + cfg["hashtags"] + "\n")
    d = ascii_(d)
    assert len(d) < 5000, f"description is {len(d)} characters (limit 5,000)"
    return d


def token():
    r = json.load(urllib.request.urlopen(urllib.request.Request("https://oauth2.googleapis.com/token", urllib.parse.urlencode(dict(
        client_id=os.environ["YT_CLIENT_ID"], client_secret=os.environ["YT_CLIENT_SECRET"], grant_type="refresh_token",
        refresh_token=os.environ["YT_ANALYTICS_REFRESH_TOKEN"])).encode())))
    return r["access_token"]


def video(vid):
    u = f"https://www.googleapis.com/youtube/v3/videos?part=status,snippet&id={vid}"
    return json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"Authorization": "Bearer " + token()})))["items"][0]


def thumb_ok(vid, local):
    """True when the thumbnail YouTube serves (signed URL, works for private videos) is our 9:16 art, centred in a 16:9 frame."""
    from PIL import Image, ImageChops, ImageStat
    url = video(vid)["snippet"]["thumbnails"]["maxres"]["url"]
    served = Image.open(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=30)).convert("L")
    w, h = served.size; cw = round(h * 9 / 16)
    a = served.crop(((w - cw) // 2 + 6, 6, (w + cw) // 2 - 6, h - 6)).resize((72, 128))
    b = Image.open(local).convert("L").resize((cw, h)).crop((6, 6, cw - 6, h - 6)).resize((72, 128))
    return ImageStat.Stat(ImageChops.difference(a, b)).mean[0] < 14


def sub_line(path, pat, new):
    t = open(path, encoding="utf-8").read(); t2 = re.sub(pat, lambda m: new, t, count=1, flags=re.M)
    open(path, "w", encoding="utf-8").write(t2); return t2 != t


def main():
    cfg_path = sys.argv[1]; dry = "--dry-run" in sys.argv
    resume = sys.argv[sys.argv.index("--resume") + 1] if "--resume" in sys.argv else None
    cfg = json.load(open(cfg_path, encoding="utf-8")); media = cfg["media"]; name = cfg["video_name"]
    plan = json.load(open(f"{media}/plan.json", encoding="utf-8")); up = f"{media}/upload"; os.makedirs(up, exist_ok=True)
    privacy = cfg.get("privacy", "private"); out = []
    # 1 thumbnail
    from make_thumbnail import compose
    th = cfg["thumb"]; shutil_hero = f"{up}/hero-pub.jpg"
    from PIL import Image
    Image.open(f"{media}/{th['hero']}").convert("RGB").save(shutil_hero, quality=95)
    compose(up, "thumb", "hero-pub.jpg", th["lines"], th.get("hot", 1), ("end", 1280), th.get("kicker"), th.get("chips")); thumb = f"{up}/thumb.jpg"
    # 2 description
    desc = description(cfg, plan); open(f"{up}/desc.txt", "w", encoding="utf-8").write(desc)
    out.append(f"thumbnail {thumb} · description {len(desc)} chars")
    if dry: print("\n".join(out)); return
    # 3 upload
    vid = resume
    if not vid:
        for _ in range(2):
            rc, o = run(f"{HERE}/youtube_upload.py", "upload", f"{media}/{cfg['render']}", "--title", cfg["title"], "--desc-file", f"{up}/desc.txt", "--privacy", privacy)
            m = re.search(r"uploaded (\S+)", o)
            if m: vid = m.group(1); break
        if not vid: sys.exit("upload failed:\n" + o[-400:])
    out.append(f"uploaded {vid} ({privacy}) https://youtu.be/{vid}")
    # 4 wait for processing, set the thumbnail, verify it
    t0 = time.time()
    while video(vid)["status"]["uploadStatus"] != "processed" and time.time() - t0 < 1200: time.sleep(10)
    rc, o = run(f"{HERE}/youtube_upload.py", "thumb", vid, thumb)
    ok = "200" in o and thumb_ok(vid, thumb)
    if not ok: time.sleep(20); run(f"{HERE}/youtube_upload.py", "thumb", vid, thumb); ok = thumb_ok(vid, thumb)
    out.append("thumbnail " + ("CONFIRMED (served image is ours)" if ok else "NOT CONFIRMED: check Studio, rerun with --resume " + vid))
    # 5 videos.csv
    texts = plan["texts"]; words = sum(len(t.split()) for t in texts)
    dur = int(re.search(r"-(\d+)s-", cfg["render"]).group(1)); rno = re.search(r"-r(\d+)\.", cfg["render"]).group(1)
    plates = sum(len(s["plates"]) for s in plan["scenes"])
    rows = list(csv.reader(open("Analytics/videos.csv", encoding="utf-8")))
    row = [name, datetime.now(timezone.utc).strftime("%Y-%m-%d"), vid, "", str(words), str(dur), cfg["hook_type"], texts[0].replace("thirteen seventy-seven", "1377"), "", str(plates), "Austin"]
    hook = None
    sc = glob.glob(f"Videos/**/Script - {name}.md", recursive=True)
    if sc:
        m = re.search(r"Voice \(exact text\).*?\n\|[^\n]*\n\|\s*1\s*\|\s*([^|]+?)\s*\|", open(sc[0], encoding="utf-8").read(), re.S)
        if m: row[7] = m.group(1)
    rows = [r for r in rows if not (r and r[0] == name)] + [row]
    csv.writer(open("Analytics/videos.csv", "w", newline="", encoding="utf-8"), lineterminator="\n").writerows(rows)
    # 6 Upload note
    nd = os.path.dirname(sc[0]) if sc else os.path.dirname(glob.glob(f"Videos/**/{name} - Status.md", recursive=True)[0])
    today = datetime.now().strftime("%Y-%m-%d")
    claims = "".join(f"| {a} | {b} | {c} |\n" for a, b, c in cfg.get("claims", []))
    alts = "; ".join(cfg.get("alt_titles", []))
    note = f"""---
type: research
created: {today}
updated: {today}
status: UPLOADED {privacy} (video id {vid}); thumbnail {'confirmed' if ok else 'NOT confirmed'}; pinned comment and TikTok are the user's
tags: [youtube, upload, week-01]
---

# Upload · {name}

← [[{name} - Status]] · [[Script - {name}]] · [[Publish]]

User request: *"{cfg['approval']}"*. Visibility **{privacy}** (default private unless the user names one).

## Upload result

`System/scripts/publish.py`: id **{vid}**, https://studio.youtube.com/video/{vid}/edit, https://youtu.be/{vid}. File `{media}/{cfg['render']}` ({dur} s), `containsSyntheticMedia: true`. Thumbnail `{up}/thumb.jpg` (text **{' / '.join(th['lines'])}**), set after processing; served image {'confirmed' if ok else 'NOT confirmed'}.

## Title ({len(cfg['title'])} characters)

```text
{cfg['title']}
```

{('Alternatives: ' + alts + '.') if alts else ''}

## Description ({len(desc)} characters, plain ASCII)

Built by `publish.py` into `{up}/desc.txt`: claim, "New Shorts every day.", sources, caveats, photo credits (from `stock/_credits.jsonl`, only the photos used), the AI line, hashtags.

## Pinned comment (post by hand)

```text
{cfg['pinned']}
```

## Studio settings

Not made for kids. Altered or synthetic content: the script sent "yes". Captions: `{media}/render/` `.srt` (upload by hand if wanted). TikTok: not prepared.

## Claims to recheck

| Claim | Source | Strength |
| --- | --- | --- |
{claims}
"""
    open(f"{nd}/Upload - {name}.md", "w", encoding="utf-8").write(note)
    # 7 Status and index
    st = f"{nd}/{name} - Status.md"
    sub_line(st, r"^status:.*$", f"status: rendered r{rno} ({dur} s) and uploaded {privacy} ({vid}) on the user's word")
    sub_line(st, r"^\| 8 Publish.*$", f"| 8 Publish | ✅ uploaded {privacy} | **user**: *\"{cfg['approval']}\"* | see [[Upload - {name}]]; `videos.csv` row added |")
    idx = open("YouTube Channel.md", encoding="utf-8").read()
    def fix(m):
        c = m.group(0).split(" | ")
        if len(c) >= 4:
            c[2] = f"r{rno} ({dur} s) uploaded {privacy} ({vid}) with thumbnail"
            if "Upload - " + name not in c[3]: c[3] = c[3].rstrip(" |") + f" · [[Upload - {name}]] |"
        return " | ".join(c)
    open("YouTube Channel.md", "w", encoding="utf-8").write(re.sub(rf"^\| {re.escape(name)} \|.*$", fix, idx, count=1, flags=re.M))
    # 8 analytics and check
    run(f"{HERE}/youtube_analytics.py", "pull"); run(f"{HERE}/analytics.py", "report")
    rc, o = run(f"{HERE}/check_vault.py")
    out.append("vault: " + o.strip().splitlines()[-1])
    print("\n".join(out))


if __name__ == "__main__":
    main()
