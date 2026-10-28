"""Mix and master the audio of a rendered Short with ffmpeg, then put it back into the mp4 (System/Playbook.md §5).

    python3 System/scripts/mix_audio.py "Media/Week NN/<Day>/<Video>"          # after the HyperFrames render
    python3 System/scripts/mix_audio.py "Media/..." --report                   # measure only

Keeps the picture and replaces the sound. Reads render/_timeline.json (voice placement, stems, render path, written by
hfkit.Short.write) and plan.json `sound`:

  "sound": {"music": {"file": "music/pc-music.mp3", "start": 12.0, "lu": -15, "duck": 0.063},  # optional bed
            "sfx_db": 0, "bed": false, "lufs": -14, "tp": -1.0}

  * voice stem: the takes as placed by the builder, through a speech chain for phone speakers (high-pass 80 Hz, a small cut
    at 250 Hz, presence +2.5 dB at 3.2 kHz, de-esser, 2.5:1 compression), then levelled to `lufs` + 1 LU.
  * music: looped or trimmed to the video, levelled `lu` under the voice (default −15 LU), ducked about 8 dB while the voice
    speaks (sidechain 3:1, threshold `duck`; measured 9 Oct 2026), so it sits about 23 LU under speech and fills the pauses.
  * sfx: the effects stem hfkit lays from System/assets/sfx (render/_fx/sound_sfx.wav), at its designed level relative to the voice
    plus `sfx_db`; the old sine bed only if "bed": true and there is no music.
  * master: two-pass loudnorm to `lufs` (−14 LUFS integrated, YouTube's reference) and `tp` (−1 dBTP), 48 kHz stereo AAC.
The silent render is kept as render/_fx/<name>-picture.mp4. The script prints the final loudness: P7 belongs to the user.
"""
import argparse, json, os, re, shutil, subprocess, sys

SR = 48000
VOICE_CHAIN = ("highpass=f=80,equalizer=f=250:t=q:w=1.2:g=-2,equalizer=f=3200:t=q:w=1.0:g=2.5,deesser=i=0.35,"
               "acompressor=threshold=-20dB:ratio=2.5:attack=8:release=160:makeup=1")


def ff(args, quiet=True):
    r = subprocess.run(["ffmpeg", "-y", "-hide_banner", "-nostats"] + args, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit("ffmpeg failed: " + r.stderr[-1500:])
    return r.stderr


def loudness(path):
    """Integrated loudness, true peak and range (EBU R128) of a file, from loudnorm's measuring pass."""
    err = ff(["-i", path, "-af", "loudnorm=print_format=json", "-f", "null", "-"])
    j = json.loads(err[err.rindex("{"):err.rindex("}") + 1])
    return {k: float(j[k]) for k in ("input_i", "input_tp", "input_lra", "input_thresh", "target_offset")}


def gain_to(path, out, target):
    m = loudness(path)
    ff(["-i", path, "-af", f"volume={target - m['input_i']:.2f}dB", "-ar", str(SR), out])
    return target - m["input_i"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args()
    root = os.path.abspath(a.video)
    plan = json.load(open(f"{root}/plan.json", encoding="utf-8"))
    tl = json.load(open(f"{root}/render/_timeline.json", encoding="utf-8"))
    render = tl["render"]
    if a.report:
        print("LOUDNESS", render, loudness(render))
        return
    sn = plan.get("sound", {})
    lufs, tp = sn.get("lufs", -14.0), sn.get("tp", -1.0)
    work = os.path.join(root, "render", "_fx", "mix")
    os.makedirs(work, exist_ok=True)
    dur = tl["duration"]

    # voice stem: every take where the builder placed it
    ins, chains = [], []
    for k, v in enumerate(tl["voices"]):
        ins += ["-i", v["file"]]
        ms = round(v["at"] * 1000)
        chains.append(f"[{k}:a]aresample={SR},aformat=channel_layouts=mono,atrim=start={v['in']:.3f}:duration={v['dur']:.3f},"
                      f"asetpts=PTS-STARTPTS,adelay={ms}|{ms},aresample=async=1:first_pts=0[v{k}]")   # adelay alone only shifts timestamps (measured: voice 0.44 s early); this writes the silence
    n = len(tl["voices"])
    mix = "".join(f"[v{k}]" for k in range(n)) + f"amix=inputs={n}:normalize=0,apad,atrim=0:{dur:.3f},{VOICE_CHAIN}[vo]"
    raw_voice = f"{work}/voice_raw.wav"
    ff(ins + ["-filter_complex", ";".join(chains + [mix]), "-map", "[vo]", "-ar", str(SR), raw_voice])
    voice = f"{work}/voice.wav"
    vgain = gain_to(raw_voice, voice, lufs + 1.0)          # the voice carries the loudness; the master adds the rest

    stems = [voice]
    # music bed, ducked by the voice
    mu = sn.get("music")
    if mu:
        src = os.path.join(root, mu["file"])
        cut = f"{work}/music_cut.wav"
        ff(["-stream_loop", "-1", "-ss", str(mu.get("start", 0)), "-i", src, "-t", f"{dur:.3f}", "-af",
            f"aresample={SR},aformat=channel_layouts=stereo,afade=t=in:d={mu.get('fade_in', 0.3)},"
            f"afade=t=out:st={max(0, dur - mu.get('fade_out', 1.6)):.3f}:d={mu.get('fade_out', 1.6)}", cut])
        lev = f"{work}/music_lev.wav"
        gain_to(cut, lev, lufs + 1.0 + mu.get("lu", -15))
        duck = f"{work}/music.wav"
        ff(["-i", lev, "-i", voice, "-filter_complex",
            f"[1:a]aformat=channel_layouts=stereo[key];[0:a][key]sidechaincompress=threshold={mu.get('duck', 0.063)}:"
            f"ratio=3:attack=40:release=450:knee=3[m]", "-map", "[m]", duck])
        stems.append(duck)
    # the effects stem from the builder, kept at its designed level relative to the voice
    for name in ("sfx", "bed"):
        p = tl.get("stems", {}).get(name)
        if not p or not os.path.exists(p) or (name == "bed" and (mu or not sn.get("bed", False))):
            continue
        out = f"{work}/{name}.wav"
        ff(["-i", p, "-af", f"aresample={SR},volume={vgain + sn.get('sfx_db', 0) if name == 'sfx' else vgain:.2f}dB", out])
        stems.append(out)

    pre = f"{work}/premaster.wav"
    ins = sum((["-i", s] for s in stems), [])
    ff(ins + ["-filter_complex", "".join(f"[{k}:a]aformat=channel_layouts=stereo[s{k}];" for k in range(len(stems)))
              + "".join(f"[s{k}]" for k in range(len(stems))) + f"amix=inputs={len(stems)}:normalize=0[o]", "-map", "[o]", pre])
    m = loudness(pre)
    master = f"{work}/master.wav"
    ff(["-i", pre, "-af", f"loudnorm=I={lufs}:TP={tp}:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
        f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,"
        f"aresample={SR}", "-ar", str(SR), master])

    keep = os.path.join(root, "render", "_fx", os.path.basename(render).replace(".mp4", "-picture.mp4"))
    stamp = keep + ".mixed"                              # mtime of the last mixed output: anything else is a new render
    mixed = open(stamp).read().strip() if os.path.exists(stamp) else ""
    if not os.path.exists(keep) or str(os.path.getmtime(render)) != mixed:
        shutil.copy2(render, keep)                       # a re-render under the same name replaces the kept picture
    tmp = render.replace(".mp4", ".mixing.mp4")
    ff(["-i", keep, "-i", master, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-ar", str(SR), "-ac", "2", "-shortest", "-movflags", "+faststart", tmp])
    os.replace(tmp, render)
    open(stamp, "w").write(str(os.path.getmtime(render)))
    f = loudness(render)
    vm = (loudness(voice)["input_i"] - loudness(stems[1])["input_i"]) if mu else None
    print(f"MIX {os.path.basename(render)}: {f['input_i']:.1f} LUFS, true peak {f['input_tp']:.1f} dBTP, range {f['input_lra']:.1f} LU"
          + (f", music {vm:.1f} LU under the voice (after ducking)" if vm is not None else ", no music")
          + f" | stems: {', '.join(os.path.basename(s) for s in stems)}")


if __name__ == "__main__":
    main()
