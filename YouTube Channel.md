---
type: research
created: 2026-10-03
updated: 2026-10-04
aliases: [Canal YouTube, YouTube Channel]
tags: [research, youtube, hub]
---

# 🎬 YouTube Channel

(vault index)

A narrated-learning channel made with AI, built on the criteria in [[YouTube with AI - quality content guide]]. This vault is the **process for producing videos iteratively**: fixed steps, and media generated only after the user approves.

> **Language rule (3 Oct 2026): everything is in English.** Notes, scripts, narration, on-screen text, video descriptions, prompts and pipeline states. Voice: `elevenlabs/v3`, `language_code: en` ([[Channel voice]]). Videos 1 to 6 were made in Spanish and stay as a historical record; their notes were translated, but their narration was not.

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
│   ├── Process/    Fast workflow · Production process · Media convention · YouTube upload · Feedback loop · Post-render feedback template
│   ├── Content/    Idea and hook quality · Channel identity · Narration guide · Channel voice · Shorts quality bar · Channel strategy · Channel playbook · YouTube with AI (quality guide)
│   ├── Visual/     Illustration pipeline · On-screen text style · Per-scene prompt
│   ├── Editing/    Blender editing · Transitions and effects
│   ├── Models/     Channel models (prices)
│   ├── Brand/      Redtail logo and banner, brand register and archive: [[Brand options]] · [[Logo references]] · decision in [[Channel playbook]] §4 · voice candidates: [[Voice samples]]
│   └── scripts/    build_video.py (the builder) · stock_photos.py · replicate_helper.py · check_vault.py · legacy build_*.py
├── Research/       general notes on models and styles, unrelated to a script
└── Videos/         Week 01 (current) and Legacy; one folder per video: Status, scripts, research, upload note
```

A new video = a folder in `Videos/Week NN/` (the current week) with its `<Topic> - Status` note, copied from the template in [[Production process]]; Week 01 (5 to 11 Oct 2026) holds the Battery and lithium and the Copper and the AI race videos.

## Reference by topic

| Topic | Note |
| --- | --- |
| Stages and gates | [[Production process]] |
| Where media is stored | [[Media convention]] |
| Uploading to YouTube (API setup, script, gotchas) | [[YouTube upload]] |
| Is the idea worth it? | [[Idea and hook quality]] |
| How to write | [[Narration guide]] · [[Channel voice]] · voice candidates: [[Voice samples]] |
| What makes a Short top tier (hook, captions, rhythm, checklist) | [[Shorts quality bar]] |
| Monetization, policies, multi-platform plan | [[Channel strategy]] |
| Engagement, on-screen design system, brand and mission | [[Channel playbook]] |
| How it looks | [[Illustration pipeline]] · [[On-screen text style]] · [[Channel identity]] |
| How to call Replicate | [[Prompt - per-scene generation guide]] · [[Channel models]] |
| How to edit | [[Blender editing]] · [[Transitions and effects]] |
| Model research | [[Research - Flux Kontext Pro with references (power)]] |
| Free resource directories (sound, references, data) | [[Research - Free resource directories (FMHY)]] |
| Other agents' workflows (Moltbook) | [[Research - Moltbook (agent creators)]] |

## Videos

Videos are grouped by publishing week: **Week 01 is the first video made under the full process**; everything before it is **Legacy** (user, 5 Oct 2026). Notes live in `Videos/Week NN/<Topic>/`, media in `Media/Week NN/<Video>/` ([[Media convention]]).

### Week 01

| Video | Stage | Status | Note |
| --- | --- | --- | --- |
| Battery and lithium (Short 9:16, **200 words** by the user's request, **English**, ≈ 72 s, first with the **Austin** voice at speed 1.0) | 7 · r1 rendered (the user: "perfect"); 8 · upload package ready | delegated by the user: 9 voice takes, 3 `gpt-image-1.5` plates, 8 word-timing runs (≈ $0.35 of a ≈ $0.41 cap); 21 plates, 14 free photos | [[Battery and lithium - Status]] · [[Script - Battery and lithium]] · [[Upload - Battery and lithium]] |
| Copper and the AI race (Short 9:16, **160 words**, **English**, ≈ 61 s, **Austin** at speed 1.0, new caption layout, `gpt-image-2`) | 7 · r1 rendered; 8 · **uploaded private** (YRX0VfpPMtU), awaiting the user | delegated by the user: 7 voice takes, 1 `gpt-image-2` plate, 7 word-timing runs (≈ $0.41 of a ≈ $0.49 cap, price of the image unconfirmed); 18 plates, 10 free photos | [[Copper and the AI race - Status]] · [[Script - Copper and the AI race]] · [[Upload - Copper and the AI race]] |

### Legacy

| Video | Stage | Status | Note |
| --- | --- | --- | --- |
| Magnets and geopolitics (38 s) | 7 · provisional cut | First video; made before the process existed | [[Magnets and geopolitics - Status]] |
| Helium and power (70 s) | 7 · r1, awaiting P7 | Voice, sound, image and editing | [[Helium and power - Status]] |
| Brazil and embassies (Short 9:16, 63 s) | 7 · r3, awaiting P7 | ≈ $0.46 | [[Brazil and embassies - Status]] |
| Lemon cake (Short 9:16, 81 s) | 7 · r2, awaiting P7 | `elevenlabs/v3` and 20 `gpt-image-1.5` plates (≈ $1.57) | [[Lemon cake - Status]] |
| Bike stems (Short 9:16, 63 s) | 7 · r2, awaiting P7 | `elevenlabs/v3` and 8 `wan-2.7-image` plates (≈ $0.26) | [[Bike stems - Status]] |
| Chips and lithography (Short 9:16, ≈ 93 s) | 7 · r1, awaiting P7 | `elevenlabs/v3`, 8 `flux-kontext-pro` images (≈ $0.48) | [[Chips and lithography - Status]] |
| Twisted carbon (Short 9:16, ≈ 85 s, **English**) | 7 · r1, awaiting P7 | First video built with the idea-quality rules; `elevenlabs/v3` `en`, 13 `flux-kontext-pro` plates (≈ $0.64) | [[Twisted carbon - Status]] |
| Helium - why it cannot be made (Short 9:16, ≈ 76 s, **English**) | 7 · r1, awaiting P7 | `elevenlabs/v3` `en`, 13 `flux-kontext-pro` plates (≈ $0.70) | [[Helium - why it cannot be made - Status]] |
| Magnetar (Short 9:16, 61 s, **English**) | 7 · r3, awaiting P7; **post-render feedback applied to the vault, video not reworked yet** | `elevenlabs/v3` `en`, 3 `gpt-image-1.5` plates + 5 NASA/CC0 stock photos (≈ $0.24) | [[Magnetar - Status]] |
| Moon (Short 9:16, 137 words, **English**) | 7 · built by the agent on the user's delegation (option C of [[The Moon is leaving us]]), awaiting P7 | first video with all the Superconductors-feedback rules: plain hook, theme line, 18 plates, no branding; 2 `gpt-image-1.5` plates + a drawn diagram + 13 NASA and Commons photos (≈ $0.24) | [[Moon - Status]] |
| Superconductors (Short 9:16, 162 words, **English**) | 7 · built by the agent on the user's delegation, awaiting P7 | first video with the Magnetar-feedback rules: need-to-know opener, faithful schematics, real backdrops, word-by-word captions; 4 `gpt-image-1.5` plates + 5 Commons photos | [[Superconductors - Status]] |
| Asteroid mining (Short 9:16, 162 words, **English**) | 7 · built by the agent on the user's delegation, awaiting P7 | the chain of a real mine in four steps (127 g brought home so far, ball-pit landing, no zero-gravity refining, the platinum market); 19 plates, 17 NASA or JAXA or Commons photos and 2 schematics; [[Asteroid mining - Status]] |
