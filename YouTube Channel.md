---
type: research
created: 2026-10-03
updated: 2026-10-03
aliases: [Canal YouTube, YouTube Channel]
tags: [research, youtube, hub]
---

# 🎬 YouTube Channel

(vault index)

A narrated-learning channel made with AI, built on the criteria in [[YouTube with AI - quality content guide]]. This vault is the **process for producing videos iteratively**: fixed steps, and media generated only after the user approves.

> **Language rule (3 Oct 2026): everything is in English.** Notes, scripts, narration, on-screen text, video descriptions, prompts and pipeline states. Voice: `elevenlabs/v3`, `language_code: en` ([[Channel voice]]). Videos 1 to 5 were made in Spanish and stay as a historical record; their notes were translated, but their narration was not.

> **Master rule:** no media is generated until gate P4 ([[Production process]]).

**Idea queue and states: [[Pipeline]].**

## To produce a video, read only two notes

1. **[[Guidelines for new scripts]]**: which quality rules apply (script, illustration, voice, editing, costs). It is the feedback from every video, compressed.
2. **[[Fast workflow]]**: how a video is produced (packages, models, prices, budget, Shorts format).

Plus the video's `<Topic> - Status` note and its script. Everything else is reference.

## Map

```
YouTube Channel.md
├── System/
│   ├── Guidelines for new scripts.md   ← main entry point
│   ├── Process/    Fast workflow · Production process · Media convention
│   ├── Content/    Narration guide · Channel voice · YouTube with AI (quality guide)
│   ├── Visual/     Visual style · On-screen text style · Per-scene prompt
│   ├── Editing/    Blender editing · Transitions and effects
│   ├── Models/     Channel models (prices)
│   └── scripts/    build_*.py · replicate_helper.py
├── Research/       general notes on models and styles, unrelated to a script
└── Videos/         one folder per video: Status, scripts, research
```

A new video = a folder in `Videos/` with its `<Topic> - Status` note, copied from the template in [[Production process]].

## Reference by topic

| Topic | Note |
| --- | --- |
| Stages and gates | [[Production process]] |
| Where media is stored | [[Media convention]] |
| How to write | [[Narration guide]] · [[Channel voice]] |
| How it looks | [[Visual style - plasticine miniatures]] · [[On-screen text style]] |
| How to call Replicate | [[Prompt - per-scene generation guide]] · [[Channel models]] |
| How to edit | [[Blender editing]] · [[Transitions and effects]] |
| Model research | [[Research - Flux Kontext Pro with references (power)]] |

## Videos

| Video | Stage | Status | Note |
| --- | --- | --- | --- |
| Magnets and geopolitics (38 s) | 7 · provisional cut | First video; made before the process existed | [[Magnets and geopolitics - Status]] |
| Helium and power (70 s) | 7 · r1, awaiting P7 | Voice, sound, image and editing | [[Helium and power - Status]] |
| Brazil and embassies (Short 9:16, 63 s) | 7 · r3, awaiting P7 | ≈ $0.46 | [[Brazil and embassies - Status]] |
| Lemon cake (Short 9:16, 81 s) | 7 · r2, awaiting P7 | `elevenlabs/v3` and 20 `gpt-image-1.5` plates (≈ $1.57) | [[Lemon cake - Status]] |
| Bike stems (Short 9:16, 63 s) | 7 · r2, awaiting P7 | `elevenlabs/v3` and 8 `wan-2.7-image` plates (≈ $0.26) | [[Bike stems - Status]] |
| Chips and lithography (Short 9:16, ≈ 93 s) | 7 · r1, awaiting P7 | `elevenlabs/v3`, 8 `flux-kontext-pro` images (≈ $0.48) | [[Chips and lithography - Status]] |
