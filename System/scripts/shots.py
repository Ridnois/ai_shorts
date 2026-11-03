#!/usr/bin/env python3
"""Study material for a reference shot (Picture §Before each beat sheet; Research/Shots): no video file is downloaded.
    python3 System/scripts/shots.py <youtube id or url> [...]
For each video, into Media/_research/<id>/ (local, gitignored): the YouTube storyboard (the low-res frames the player shows
when scrubbing, format sb0) tiled into sheet.jpg with each tile's time, the auto captions as transcript.txt with times,
and meta.json (title, channel, views, duration). The agent reads sheet.jpg and transcript.txt and writes a note in
Research/Shots/ from Research/Shots/_template.md. Needs yt-dlp (`uv tool install yt-dlp`)."""
import glob, json, os, re, shutil, subprocess, sys, urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
YT = shutil.which("yt-dlp") or os.path.expanduser("~/.local/bin/yt-dlp")


def vid(x):
    m = re.search(r"(?:youtu\.be/|v=|shorts/)([\w-]{11})", x)
    return m.group(1) if m else x


def study(v):
    out = f"{ROOT}/Media/_research/{v}"; os.makedirs(out, exist_ok=True)
    url = f"https://www.youtube.com/watch?v={v}"
    meta = json.loads(subprocess.run([YT, "-q", "--skip-download", "--dump-json", url], capture_output=True, text=True).stdout or "{}")
    keep = {k: meta.get(k) for k in ("title", "channel", "uploader_id", "view_count", "duration", "upload_date", "like_count")}
    json.dump(keep, open(f"{out}/meta.json", "w"), indent=1)
    # storyboard: the sb0 format lists its sprite sheets (grids of frames) as fragments with direct URLs
    sb = next((x for x in meta.get("formats", []) if x.get("format_id") == "sb0"), {})
    sprites = []
    for k, fr in enumerate(sb.get("fragments", [])):
        u = fr.get("url") or (sb.get("fragment_base_url", "") + fr.get("path", ""))
        path = f"{out}/sprite-{k:03d}.webp"
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
            open(path, "wb").write(urllib.request.urlopen(req, timeout=30).read()); sprites.append(path)
        except Exception as e:
            print(f"sprite {k}: {e}")
    w, h = sb.get("width", 101), sb.get("height", 180)
    frames = []
    from PIL import Image, ImageDraw               # sprites are WebP grids; the last one is often a partial grid
    for sp in sorted(sprites):
        try: im = Image.open(sp).convert("RGB")        # WebP; ffmpeg's WebP decoder garbles these sprites, Pillow reads them
        except OSError: continue
        for r in range(im.height // h):
            for c in range(im.width // w):
                frames.append(im.crop((c * w, r * h, (c + 1) * w, (r + 1) * h)))
    for sp in sprites: os.remove(sp)
    dur = keep["duration"] or 60
    frames = [f for f in frames if f.getbbox()]       # drop the blank cells of a partial last grid
    if frames:
        step, n = dur / len(frames), 10
        sheet = Image.new("RGB", (n * w, -(-len(frames) // n) * h), "black")
        d = ImageDraw.Draw(sheet)
        for k, f in enumerate(frames):
            x, y = (k % n) * w, (k // n) * h
            sheet.paste(f, (x, y)); d.rectangle((x, y, x + 34, y + 13), fill="black"); d.text((x + 2, y + 1), f"{k * step:.0f}s", fill="white")
        sheet = sheet.resize((sheet.width * 2, sheet.height * 2))
        sheet.save(f"{out}/sheet.jpg", quality=88)
    tiles = len(frames)
    subprocess.run([YT, "-q", "--skip-download", "--write-auto-subs", "--sub-langs", "en.*", "--sub-format", "vtt", "-o", f"{out}/subs", url],
                   capture_output=True, text=True)
    lines, last = [], ""
    for f in glob.glob(f"{out}/subs*.vtt")[:1]:
        for blk in open(f, encoding="utf-8").read().split("\n\n"):
            m = re.search(r"(\d+):(\d+):([\d.]+) -->", blk)
            txt = re.sub(r"<[^>]+>", "", " ".join(l for l in blk.splitlines()[1:] if "-->" not in l)).strip()
            if m and txt and txt != last:
                t = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
                lines.append(f"{t:5.1f}  {txt}"); last = txt
        os.remove(f)
    open(f"{out}/transcript.txt", "w").write("\n".join(lines))
    print(f"SHOTS {v}: {keep['title']!r} ({keep['channel']}, {keep['view_count']:,} views, {keep['duration']} s) · "
          f"{tiles} storyboard frames · {len(lines)} caption lines{' (captions refused, often HTTP 429: retry later)' if not lines else ''} -> {os.path.relpath(out, ROOT)}")


if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(__doc__)
    for x in sys.argv[1:]: study(vid(x))
