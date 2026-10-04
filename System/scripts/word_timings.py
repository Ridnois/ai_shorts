#!/usr/bin/env python3
"""Word-level timings for the voice takes, so the builder can show word-by-word captions.

    python3 System/scripts/word_timings.py Media/<Video>            # every voice in plan.json that has no .words.json yet

Writes voice/<take>.words.json = [[word, start_s, end_s], ...] (seconds in the ORIGINAL mp3; the builder adds the padding).
Model: vaibhavs10/incredibly-fast-whisper with timestamp=word (≈ $0.01 per take; the price is logged, not assumed).
Without these files the builder still captions the video from an estimate (characters and pauses), see build_video.py.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from replicate_helper import call, datauri, log, run  # noqa: E402  (needs REPLICATE_API_TOKEN)

MODEL = "vaibhavs10/incredibly-fast-whisper"


def words_of(output):
    chunks = output.get("chunks") or []
    return [[c["text"].strip(), c["timestamp"][0], c["timestamp"][1] if c["timestamp"][1] is not None else c["timestamp"][0] + 0.3]
            for c in chunks if c["text"].strip()]


def main(root):
    plan = json.load(open(f"{root}/plan.json", encoding="utf-8"))
    for src in plan["voices"]:
        dst = f"{root}/{os.path.splitext(src)[0]}.words.json"
        if os.path.exists(dst):
            continue
        p = run(MODEL, {"audio": datauri(f"{root}/{src}", "audio/mpeg"), "timestamp": "word", "language": "english", "task": "transcribe"})
        log(p)
        w = words_of(p["output"])
        json.dump(w, open(dst, "w"), ensure_ascii=False)
        print(dst, len(w), "words:", " ".join(x[0] for x in w)[:100])


if __name__ == "__main__":
    main(sys.argv[1])
