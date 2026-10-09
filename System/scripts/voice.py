"""The narration as ONE continuous take (System/Playbook.md §5): no stitched scenes, no cut-in silences.

    python3 System/scripts/voice.py "Media/Week NN/<Day>/<Video>" --dry     # prints the request text, spends nothing
    python3 System/scripts/voice.py "Media/Week NN/<Day>/<Video>"           # generates voice/<prefix>-take-v<n>.wav

Reads plan.json: `texts` (one voiced string per scene) and `voice`:
  "voice": {"model": "inworld/realtime-tts-2", "voice_id": "Dennis", "speaking_rate": 1.0, "temperature": 0,
            "direction": "[say calmly and warmly, like a curious specialist explaining something to a friend]"}
and per scene (optional): "beat": seconds of pause after the scene (a deliberate beat, ≤ 0.8 s; omit for the natural
paragraph pause), "pauses": [["word", seconds], ...] (a break after that word, for a planned pause inside the scene) and
"delivery": a bracketed direction placed before that scene ("[say this more slowly, with quiet gravity]").

Pauses are written into the text as SSML breaks (<break time="0.3s" />), which the model renders as part of the
performance, so the timing and breathing stay continuous. Measured on Inworld TTS-2 (9 Oct 2026): a break ADDS to the
model's own sentence pause (about 0.5 s) and is digital silence, so write the extra, not the total (0.3 gives a beat of
about 0.8 s, the research ceiling). Use one or two: many breaks destabilise a voice (Analytics/Reports/2026-10-09 Audio
research.md). The take is logged at once (voice/_log.txt: prediction id), saved as
48 kHz WAV, and plan.json `voices` is set to [that take]; then run word_timings.py and the builder (one-take mode).
"""
import argparse, json, os, re, sys

sys.path.insert(0, os.path.dirname(__file__))

DEFAULT = {"model": "inworld/realtime-tts-2", "voice_id": "Dennis", "speaking_rate": 1.0, "temperature": 0,
           "direction": "[say calmly and warmly, like a curious specialist explaining something to a friend]"}


def norm(w):
    return "".join(c for c in w.lower() if c.isalnum())


def request_text(plan):
    vc = {**DEFAULT, **plan.get("voice", {})}
    parts = [vc["direction"]] if vc.get("direction") else []
    for sc, text in zip(plan["scenes"], plan["texts"]):
        words = text.split()
        for spec in sc.get("pauses", []):                     # a planned pause inside the scene, after the nth heard word
            word, secs, nth = spec[0], float(spec[1]), (spec[2] if len(spec) > 2 else 1)
            hits = [i for i, w in enumerate(words) if norm(w) == norm(word)]
            if len(hits) < nth:
                raise SystemExit(f"pause anchor '{word}' (occurrence {nth}) not in: {text}")
            words[hits[nth - 1]] += f' <break time="{secs:.1f}s" />'
        chunk = " ".join(words)
        if sc.get("delivery"):
            chunk = sc["delivery"] + " " + chunk
        if sc.get("beat"):
            chunk += f' <break time="{min(float(sc["beat"]), 1.5):.1f}s" />'
        parts.append(chunk)
    return "\n\n".join(parts), vc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    root = os.path.abspath(a.video)
    pp = f"{root}/plan.json"
    plan = json.load(open(pp, encoding="utf-8"))
    text, vc = request_text(plan)
    breaks = len(re.findall("<break", text))
    print(f"REQUEST ({len(text)} characters, {breaks} breaks, voice {vc['voice_id']} on {vc['model']}):\n{text}\n")
    if len(text) > 2000:
        raise SystemExit("over the model's 2,000 characters: shorten the script or split at a paragraph")
    if breaks > 2:
        print("WARN more than 2 breaks: many breaks destabilise the voice; keep the deliberate ones")
    if any(float(x) > 0.5 for x in re.findall(r'<break time="([0-9.]+)s"', text)):
        print("WARN a break over 0.5 s: it adds to the model's own pause (about 0.5 s), so the silence will pass 1 s")
    if a.dry:
        return
    from replicate_helper import download, log, run                       # needs REPLICATE_API_TOKEN
    os.makedirs(f"{root}/voice", exist_ok=True)
    n = 1
    while any(os.path.exists(f"{root}/voice/{d}{plan['prefix']}-take-v{n}.wav") for d in ("", "_descartes/")):
        n += 1
    dst = f"{root}/voice/{plan['prefix']}-take-v{n}.wav"
    inp = {"text": text, "voice_id": vc["voice_id"], "language": "en", "audio_format": "wav", "sample_rate": 48000,
           "speaking_rate": vc["speaking_rate"], "temperature": vc["temperature"]}
    p = run(vc["model"], inp)
    with open(f"{root}/voice/_log.txt", "a") as f:
        f.write(f"take v{n} {p['id']} {vc['model']} {vc['voice_id']} {len(text)} chars\n")
    log(p)
    download(p, dst)
    plan["voices"] = [os.path.relpath(dst, root)]
    json.dump(plan, open(pp, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("TAKE", os.path.relpath(dst, root), "| plan.json voices set; next: word_timings.py, then the builder")


if __name__ == "__main__":
    main()
