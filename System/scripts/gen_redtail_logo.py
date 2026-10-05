#!/usr/bin/env python3
"""Redtail logo: style 2 (the user's winner) with the new wordmark, gpt-image-1.5, one prediction. python3 System/scripts/gen_redtail_logo.py [n]
Cap $0.06 (5 Oct 2026). Output Media/Brand redtail/<n>.png (transparent); id logged in _log.jsonl."""
import sys, json, os
sys.path.insert(0, "System/scripts")
os.environ.setdefault("REPLICATE_API_TOKEN", next(l.split("=", 1)[1].strip() for l in open(".env") if l.startswith("REPLICATE_API_TOKEN")))
import replicate_helper as R
OUT = "Media/Brand redtail"; os.makedirs(OUT, exist_ok=True)
REFS = ["System/Brand/Redtail/redtail-style-reference.png"]
PROMPT = ("Redesign this sports-team logo for a science explainer channel renamed REDTAIL. Keep the same style: the aggressive side-profile orange fox head in a round ring, "
          "sharp angular planes, thick dark outline, American football (NFL) look. Replace the lettering: the only text is the word REDTAIL, spelled exactly R-E-D-T-A-I-L, "
          "in the same heavy slanted italic block-letter wordmark below the head. Add one new element: the fox's big bushy red-orange tail with a cream tip sweeps in a curve "
          "around the lower part of the ring behind the wordmark. Flat vector illustration, bold clean outlines, oranges, cream white and one dark navy for outlines. "
          "No other text, no tagline, no real team marks. Transparent background; no glow, no shadow, no gradient background, no texture.")
n = sys.argv[1] if len(sys.argv) > 1 else "1"
p = R.run("openai/gpt-image-1.5", {"prompt": PROMPT, "aspect_ratio": "1:1", "quality": "medium", "input_fidelity": "high", "number_of_images": 1,
                                   "output_format": "png", "background": "transparent", "input_images": [R.datauri(r, "image/png") for r in REFS]})
R.download(p, f"{OUT}/{n}.png"); R.log(p)
open(f"{OUT}/_log.jsonl", "a").write(json.dumps({"n": n, "id": p["id"], "status": p["status"], "metrics": p.get("metrics")}) + "\n")
