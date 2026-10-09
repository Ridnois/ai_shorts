---
type: process
created: 2026-10-09
updated: 2026-10-09
status: A (text) done; stopped at P4; waiting for the user
tags: [status, week-01]
---

# Neon for chips · Status

← [[Script - Neon for chips]] · [[YouTube Channel]] · [[Workflow]]

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research | done | user asked 9 Oct 2026 | Source: `Analytics/Generated ideas/Youtube idea #4.md`. Y: chips keep being made. X: neon is a by-product of steel-plant air separation. Hook type: surprising fact. Street-lamp: pass with limit. Demand check **not run** (no YouTube token on this machine). Compact-test video |
| 2 Script · 3 Visual plan | done (agent) | | 114 words, 5 scenes ([[Script - Neon for chips]] §3); 12 plates |
| 4 Prompts, stock, budget | approved by delegation | 9 Oct 2026 (user: "go for it") | base about $0.40 (voice 5 takes 0.07, timings 0.05, 1 generated plate 0.25; prices unconfirmed), **cap about $0.48**; run stops at the render (P7) |
| 6 Generation · 7 Edit | render r1 running | | Blender 5.1.2 at `~/software/blender-5.1.2-linux-x64/blender` (not on PATH; vault says 5.2); `Media/` created 9 Oct 2026; no numpy in system Python |

*Not verified:* see the Script note §5. *Feedback:* none yet.

## Prediction log (9 Oct 2026)

| Scene | Category | Model | Result | URL |
| --- | --- | --- | --- | --- |
| 1 to 5 | voice | elevenlabs/turbo-v2.5, Austin, stability 0.45, similarity 0.75, style 0, speed 1.0, prev/next text | used v1 (607 characters) | ids in `voice/_log.txt` |
| 1 to 5 | word timings | incredibly-fast-whisper | used | replicate.com/p/pap3atk0hxrmy0d13x3sc89cq4 (scene 2) and four more |
| plate 4 | generated | openai/gpt-image-2, high, 3:2 | used v1, cropped; checked: neon, argon, fluorine dots, one beam, no extras (schematic; mixture proportions drawn as mostly neon, unsourced) | replicate.com/p/940j49tyrnrmt0d13x2rqdtge4 |

Stock photos (credits in `stock/_credits.jsonl`): steel plant at night (CC BY-SA 4.0), Air Liquide ASU plant cropped to hide the logo (CC BY-SA 4.0, N2e), 12-inch wafer (CC BY-SA 3.0, Peellden), ASML headquarters (public domain), neon discharge tube (CC BY 3.0, Jurii), IC die AD580 (CC BY-SA 4.0, Mister rf). Built with Blender 5.1.2 (vault says 5.2; no errors). Drawn plates: 55,000 dots, air separation flow, supply bar.
