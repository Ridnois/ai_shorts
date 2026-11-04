#!/usr/bin/env python3
"""P8 in one command (stdlib + Pillow). The agent writes ONE small JSON, runs this, and reads a ~10 line result.

    python3 System/scripts/publish.py "Media/Week NN/<Day>/<Video>/upload/publish.json" [--dry-run] [--resume <youtube_id>]

Does, in order: thumbnail check -> description (claim, sources, auto photo credits from stock/_credits.jsonl,
AI line, hashtags; ASCII only) -> upload (youtube_upload.py, private unless the JSON says otherwise) -> waits until YouTube has
processed the video -> sets the thumbnail again -> checks that the thumbnail YouTube serves is ours (pixel compare, no image to
look at) -> Analytics/videos.csv row -> Upload note -> Status stage 8 + index row -> analytics pull + report -> check_vault.
--dry-run stops after the thumbnail and the description. --resume <id> skips the upload (use after a crash).

publish.json (all keys required unless marked):
  media      "Media/Week 01/2026-10-05 Mon/Deep-sea"        render  "render/dn-62s-9x16-r1.mp4"
  video_name "AI invented sources"  (the notes folder, Status and Script names)      title  "..."
  claim      the first two lines of the description (claim and search words)
  sources    [["what it supports", "https://..."], ...]       caveats  "one or two sentences" (optional)
  hashtags   "#a #b #c"            privacy  "private"|"public"|"unlisted" (optional, default private)
  (thumbnail) upload/thumb.jpg must exist: the hf/thumb.html page that hfkit.Short.thumb() writes, snapshotted
             (System/Strategy.md §Package). An old `thumb` key is ignored.
  series     "How AI works"|"Agent at work"|"What's coming"   hook_pattern  a pattern id from System/Strategy.md §Hooks
  medium     the main medium (System/Picture.md §Medium): primitive|figure|capture|manim|generated|drawn
  ai_line    the description's AI line (optional; default from medium)
  pinned     "pinned comment text"           approval  "the user's words"         hook_type (old, optional)
  claims     [["claim", "source", "strength"], ...] (optional)            alt_titles ["...", "..."] (optional)
  tags       "ai, llm, how ai works" (optional, search words; YouTube weighs them little)
  synthetic  true only when the video shows realistic generated people, places or events (optional, default false)
  publish_at "2026-11-02T15:00:00Z" (optional: scheduled release; needs privacy private)
  tiktok     "caption" (optional)     instagram  "caption, at most 5 hashtags" (optional; System/Strategy.md §Package)
The file uploaded is the YouTube master upload/<render stem>-yt.mp4 (2160x3840, master.py); it is made here when missing.
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
        for pl in sc.get("plates", []):                     # HyperFrames plans have no plates
            for f in (pl["file"], pl.get("bg_photo"), (pl.get("inset") or {}).get("file")):
                if f: used.add(os.path.basename(f))
    cc, pd, pages = {}, set(), []
    for cf in (f"{media}/stock/_credits.jsonl", f"{media}/clips/_credits.jsonl"):
        for l in open(cf, encoding="utf-8") if os.path.exists(cf) else []:
            d = json.loads(l); f = os.path.basename(d.get("file") or d.get("dest") or "")
            if f not in used: continue
            pages.append(d.get("page", ""))
            if re.search(r"CC BY", d["license"]): cc.setdefault((d["author"], d["license"]), 0)
            else: pd.add(d["author"])
    parts = [f"{a}, {lic}" for a, lic in cc]
    if pd: parts.append("Public domain and CC0 media: " + ", ".join(sorted(pd)))
    return " | ".join(parts), all("wikimedia.org" in p for p in pages)


def description(cfg, plan):
    src = "\n".join(f"- {a}: {u}" for a, u in cfg["sources"])
    cred, commons = credits(cfg["media"], plan)
    # a video with no photo or footage gets no credits block and never says "the photos are real" (9 Oct 2026: the pc pack did)
    # the AI line says what is real: an ai_line key wins; a capture video's screenshots come from a real recorded run (3 Nov 2026)
    ai = cfg.get("ai_line") or ("The narration is AI-generated; the screenshots and model replies are from a real recorded run, the diagrams were drawn for this video."
                                if cfg.get("medium") == "capture" else "The narration is AI-generated and every animation was drawn for this video.")
    tail = (f"\nPHOTO CREDITS{' (Wikimedia Commons)' if commons else ''}\n{cred}\n\n"
            "The narration is AI-generated and the diagrams were drawn for this video; the photos are real.\n\n") if cred else f"\n{ai}\n\n"
    d = (f"{cfg['claim']}\n\nNext Token: how AI really works, in under a minute. New Shorts Mon to Fri.\n\nSOURCES\n{src}\n"
         + (f"{cfg['caveats']} Figures checked on {datetime.now():%-d %B %Y}.\n" if cfg.get("caveats") else "")
         + tail + cfg["hashtags"] + "\n")
    d = ascii_(d)
    assert len(d) < 5000, f"description is {len(d)} characters (limit 5,000)"
    return d


def token():
    from youtube_auth import access_token  # refuses any channel but Next Token
    return access_token()


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


def write_pack(cfg, plan, up, desc):
    """Publish pack (user, 9 Oct 2026, new vault rule): ONE short note inside the video's upload/ folder with the thumbnail, the title and its alternatives,
    the description, the pinned comment and the TikTok and Instagram captions, each in a plain ```text block to copy. Rewritten on every run; never edited by hand."""
    import shutil
    pre = plan["prefix"]
    shutil.copyfile(f"{up}/thumb.jpg", f"{up}/{pre}-thumb.jpg")         # one thumbnail; the copy has a name no other video's pack shares, so Obsidian embeds the right one
    blk = lambda t: "```text\n" + t.strip() + "\n```"
    L = ["---", "type: publish-pack", f"updated: {datetime.now().strftime('%Y-%m-%d')}", "status: GENERATED by System/scripts/publish.py; do not edit by hand (edit publish.json and rerun with --dry-run)", "---", "",
         f"# Publish pack · {cfg['video_name']}", "", f"Visibility: **{cfg.get('privacy', 'private')}** · approval: {cfg.get('approval', 'pending')} · claims and checklist: the video's Upload note ([[Build]] §Upload). Files: `upload/*-yt.mp4` (YouTube, 2160x3840) · `upload/*-tt.mp4` (TikTok and Instagram, 1080x1920; the Instagram cover is the thumbnail).", "", "## Thumbnail", ""]
    L += [f"`{up}/thumb.jpg`", "", f"![[{pre}-thumb.jpg]]", ""]
    L += ["## Title", "", blk(cfg["title"]), ""]
    if cfg.get("alt_titles"): L += ["Alternatives:", ""] + [f"- {t}" for t in cfg["alt_titles"]] + [""]
    L += ["## Description", "", blk(desc), "", "## Pinned comment", "", blk(ascii_(cfg["pinned"])), ""]
    if cfg.get("tiktok"): L += ["## TikTok caption", "", blk(ascii_(cfg["tiktok"])), ""]
    if cfg.get("instagram"):
        n = len(re.findall(r"#\w+", cfg["instagram"]))
        if n > 5: sys.exit(f"instagram caption has {n} hashtags; Instagram allows 5 (System/Strategy.md §Package)")
        L += ["## Instagram caption", "", blk(ascii_(cfg["instagram"])), ""]
    open(f"{up}/{pre}-publish-pack.md", "w", encoding="utf-8").write("\n".join(L)); return f"{up}/{pre}-publish-pack.md"


def main():
    cfg_path = sys.argv[1]; dry = "--dry-run" in sys.argv
    resume = sys.argv[sys.argv.index("--resume") + 1] if "--resume" in sys.argv else None
    cfg = json.load(open(cfg_path, encoding="utf-8")); media = cfg["media"]; name = cfg["video_name"]
    plan = json.load(open(f"{media}/plan.json", encoding="utf-8")); up = f"{media}/upload"; os.makedirs(up, exist_ok=True)
    privacy = cfg.get("privacy", "private"); out = []
    # 1 thumbnail
    thumb = f"{up}/thumb.jpg"
    if not os.path.exists(thumb):
        raise SystemExit(f"{thumb} missing: build hf/thumb.html (Short.thumb) and snapshot it first")
    # 2 description
    desc = description(cfg, plan); open(f"{up}/desc.txt", "w", encoding="utf-8").write(desc)
    out.append(f"thumbnail {thumb} · description {len(desc)} chars · pack {write_pack(cfg, plan, up, desc)}")
    if dry: print("\n".join(out)); return
    # 3 master and upload
    master = f"{up}/{os.path.splitext(os.path.basename(cfg['render']))[0]}-yt.mp4"
    if not os.path.exists(master):
        rc, o = run(f"{HERE}/master.py", f"{media}/{cfg['render']}")
        if rc: sys.exit("master failed:\n" + o[-400:])
    out.append("master " + run(f"{HERE}/master.py", master, "--probe")[1].strip())
    vid = resume
    if not vid:
        tags = ", ".join(cfg["tags"]) if isinstance(cfg.get("tags"), list) else cfg.get("tags")   # a list or "a, b, c"
        extra = (["--tags", tags] if tags else []) + (["--synthetic"] if cfg.get("synthetic") else []) \
                + (["--publish-at", cfg["publish_at"]] if cfg.get("publish_at") else [])
        for _ in range(2):
            rc, o = run(f"{HERE}/youtube_upload.py", "upload", master, "--title", cfg["title"], "--desc-file", f"{up}/desc.txt", "--privacy", privacy, *extra)
            m = re.search(r"uploaded (\S+)", o)
            if m: vid = m.group(1); break
        if not vid: sys.exit("upload failed:\n" + o[-400:])
    out.append(f"uploaded {vid} ({privacy}) https://youtu.be/{vid}")
    # 4 wait for processing, set the thumbnail, verify it
    t0 = time.time()
    while video(vid)["status"]["uploadStatus"] != "processed" and time.time() - t0 < 1200: time.sleep(10)
    rc, o = run(f"{HERE}/youtube_upload.py", "thumb", "--", vid, thumb)
    ok = "200" in o and thumb_ok(vid, thumb)
    if not ok: time.sleep(20); run(f"{HERE}/youtube_upload.py", "thumb", "--", vid, thumb); ok = thumb_ok(vid, thumb)
    out.append("thumbnail " + ("CONFIRMED (served image is ours)" if ok else "NOT CONFIRMED: check Studio, rerun with --resume " + vid))
    # 5 videos.csv
    texts = plan["texts"]; words = sum(len(t.split()) for t in texts)
    dur = int(re.search(r"-(\d+)s-", cfg["render"]).group(1)); rno = re.search(r"-r(\d+)\.", cfg["render"]).group(1)
    plates = sum(len(s.get("plates", [])) for s in plan["scenes"])
    rows = list(csv.reader(open("Analytics/videos.csv", encoding="utf-8")))
    row = [name, datetime.now(timezone.utc).strftime("%Y-%m-%d"), vid, "", str(words), str(dur), cfg.get("hook_type", ""),
           texts[0].replace("thirteen seventy-seven", "1377"), cfg.get("series", ""), str(plates), plan.get("voice", {}).get("voice_id", "Dennis"),
           cfg.get("hook_pattern", ""), cfg.get("medium", "")]  # columns: Analytics/videos.csv header; patterns: Strategy.md §Hooks
    hook = None
    sc = glob.glob(f"Videos/**/Script - {name}.md", recursive=True)
    if sc:
        lines = open(sc[0], encoding="utf-8").read().splitlines()   # scene 1's cell under the "Voice" header (any column order)
        for i, l in enumerate(lines):
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            col = next((j for j, c in enumerate(cells) if c.startswith("Voice")), None)
            if l.startswith("|") and col is not None:
                r1 = next((r for r in lines[i + 2:i + 4] if r.startswith("|") and r.strip("| ").startswith("1")), None)
                if r1: row[7] = [c.strip() for c in r1.strip().strip("|").split("|")][col]
                break
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
tags: [youtube, upload]
---

# Upload · {name}

← [[{name} - Status]] · [[Script - {name}]] · [[Build]] §Upload

User request: *"{cfg['approval']}"*. Visibility **{privacy}** (default private unless the user names one).

## Upload result

`System/scripts/publish.py`: id **{vid}**, https://studio.youtube.com/video/{vid}/edit, https://youtu.be/{vid}. File `{master}` ({dur} s, the 2160x3840 master of `{cfg['render']}`), `containsSyntheticMedia: {str(bool(cfg.get('synthetic'))).lower()}`. Thumbnail `{up}/thumb.jpg`, set after processing (Shorts take a custom thumbnail only once the channel is in the Partner Program); served image {'confirmed' if ok else 'NOT confirmed'}.

## Title ({len(cfg['title'])} characters)

```text
{cfg['title']}
```

{('Alternatives: ' + alts + '.') if alts else ''}

## Description ({len(desc)} characters, plain ASCII)

Built by `publish.py` into `{up}/desc.txt`: claim, the channel line, sources, caveats, photo credits (from `stock/_credits.jsonl`, only the photos used), the AI line, hashtags.

## Pinned comment (post by hand)

```text
{cfg['pinned']}
```

## Studio settings

Not made for kids. Altered or synthetic content: {'yes' if cfg.get('synthetic') else 'no (drawn animation, stock narrator)'}. Language en. Captions: `{media}/render/` `.srt` (upload by hand if wanted). TikTok: `upload/*-tt.mp4` with the pack's caption, posted by hand.

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
