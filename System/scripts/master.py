#!/usr/bin/env python3
"""Platform masters from a mixed render: the encode is the last step before upload (System/Production.md §Master).

    python3 System/scripts/master.py "Media/…/<Video>/render/<v>-r<n>.mp4"            # writes upload/<v>-yt.mp4 and upload/<v>-tt.mp4
    python3 System/scripts/master.py <mp4> --only yt                                     # one of them
    python3 System/scripts/master.py <mp4> --probe                                       # print codec, size, bitrate, colour tags only

Why: YouTube re-encodes everything. A 1080x1920 upload on a small channel is usually served as H.264 at a low
bitrate (soft, blocky, banded). A 2160x3840 upload is processed into the VP9/AV1 ladder, whose 1080p rung is cleaner.
So the YouTube master is a lanczos upscale to 2160x3840 at a high bitrate, BT.709-tagged, closed GOP of half the frame
rate, AAC 48 kHz 384 kb/s, faststart (YouTube's own upload spec: support.google.com/youtube/answer/1722171).
TikTok downsizes anything above 1080p, so its master stays 1080x1920 at a high bitrate.
aq-mode 3 spends bits in dark areas (against banding); a light unsharp helps text survive the re-encode.
Verify after a private upload: "Stats for nerds" shows vp09 or av01 (not avc1) on the 1080p rung.
"""
import argparse, json, os, subprocess, sys

COLOR = ["-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709", "-color_range", "tv"]
TARGETS = {
    "yt": dict(vf="scale=2160:3840:flags=lanczos+accurate_rnd+full_chroma_int,unsharp=5:5:0.35:3:3:0,format=yuv420p",
               x264=["-preset", "slow", "-crf", "14", "-profile:v", "high", "-level", "5.1", "-maxrate", "60M", "-bufsize", "120M",
                     "-x264-params", "aq-mode=3:aq-strength=1.1:bframes=2:keyint=15:min-keyint=15:scenecut=0:open-gop=0:deblock=-1,-1"],
               audio=["-c:a", "aac", "-ar", "48000", "-b:a", "384k"]),
    "tt": dict(vf="unsharp=5:5:0.3:3:3:0,format=yuv420p",
               x264=["-preset", "slow", "-crf", "16", "-profile:v", "high", "-level", "4.1", "-maxrate", "15M", "-bufsize", "30M",
                     "-x264-params", "aq-mode=3:bframes=2:keyint=30:open-gop=0"],
               audio=["-c:a", "aac", "-ar", "48000", "-b:a", "192k"]),
}


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                          "stream=codec_type,codec_name,profile,width,height,r_frame_rate,pix_fmt,color_space,color_range,bit_rate,sample_rate",
                          "-show_entries", "format=duration,size", "-of", "json", path], capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def line(path):
    p = probe(path)
    v = next(s for s in p["streams"] if s["codec_type"] == "video")
    a = next((s for s in p["streams"] if s["codec_type"] == "audio"), {})
    mb = round(int(p["format"]["size"]) * 8 / float(p["format"]["duration"]) / 1e6, 1)
    return (f"{os.path.basename(path)}: {v['codec_name']} {v['width']}x{v['height']} {v['r_frame_rate']} {v['pix_fmt']} "
            f"{v.get('color_space', '?')}/{v.get('color_range', '?')} · {mb} Mb/s · audio {a.get('codec_name', 'none')} {a.get('sample_rate', '')}")


def master(src, kind):
    t = TARGETS[kind]
    vid = os.path.dirname(os.path.dirname(os.path.abspath(src)))
    stem = os.path.splitext(os.path.basename(src))[0]
    os.makedirs(f"{vid}/upload", exist_ok=True)
    out = f"{vid}/upload/{stem}-{kind}.mp4"
    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", src, "-vf", t["vf"], "-c:v", "libx264", *t["x264"],
           "-pix_fmt", "yuv420p", *COLOR, *t["audio"], "-movflags", "+faststart", out]
    subprocess.run(cmd, check=True)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--only", choices=list(TARGETS))
    ap.add_argument("--probe", action="store_true")
    a = ap.parse_args()
    if not os.path.exists(a.src):
        sys.exit(f"no such file: {a.src}")
    if a.probe:
        print(line(a.src)); sys.exit()
    for k in ([a.only] if a.only else list(TARGETS)):
        print("MASTER", k, line(master(a.src, k)))
