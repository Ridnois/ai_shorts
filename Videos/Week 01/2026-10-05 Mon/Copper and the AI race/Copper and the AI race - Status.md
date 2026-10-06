---
type: research
created: 2026-10-05
updated: 2026-10-06
status: r1 rendered and uploaded (5 Oct) · REDO r2 written to Playbook v3, waiting at P4 for the user's yes (6 Oct 2026)
tags: [research, youtube, status, copper, ai, shorts, week-01]
---

# Copper and the AI race · status (Week 01)

← [[YouTube Channel]] · [[Script - Copper and the AI race]] · [[Workflow]] · [[Playbook]]

Short 9:16, English, **160 words**, Austin at `speed` 1.0, **Week 01** (the same calendar week as [[Battery and lithium - Status]]: both were made on Monday 5 Oct 2026; [[Workflow]]). Question: why can't the AI race just make more copper? Media in `Media/Week 01/2026-10-05 Mon/Copper-AI/` (prefix `cu-`). First video with **the new caption layout** (captions centred, cards below) and **the new image model** (`gpt-image-2`, one plate).

## Redo r2 (6 Oct 2026)

User: *"I really like [this video], i want you to redo this reel with all our new guidelines"*. No spend delegation was given, so the run **stops at P4** ([[Workflow]]). Same Status note, same Media folder (`Media/Week 01/2026-10-05 Mon/Copper-AI/`, prefix `cu`, voice files `v2`, render `r2`; r1 stays on disk as `plan-r1.json` and its render).

**Changed from r1:** hook (stakes: *"AI could run short of copper, and a new mine takes seventeen years."*); scene 3 is the turn (AI is not the only buyer; the 4 % share was dropped by the user); scene 5 explains why a mine is slow; pause plan (`gaps` [0.55, 0.25, 0.45, 0.30, 0.90, 1.00] plus inner pauses); 20 plates, immersive layouts (blur, insets, three drawn plates, the real USGS porphyry diagram instead of a generated plate); a derived number (found 2026, open about 2043, after the 2040 gap).

| Stage | Status | Approved | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research · 2 Script · 3 Visual plan | ✅ r2 text | agent | hook type **stakes**; street-lamp: stated mechanism, **needs the user's yes**; demand check done (crowded topic, earned by the turn and the 2043 sum); [[Script - Copper and the AI race]] |
| 4 Prompts, stock, budget | ✅ | **user, 6 Oct 2026**: *"the ore's speed is good, the date is good too, continue"* (street-lamp yes; run to the render, **no upload**) | base $0.41, expected $0.16, cap $0.49 (below) |
| 6 Generation | ✅ | delegation | 7 voice takes (832 characters), 1 generated plate (porphyry, no retry), 7 word-timing runs, 3 drawn plates (Pillow), 4 new stock photos |
| 7 Edit | ✅ built · render r2 running · ⏳ **P7 is yours** | | `Media/Week 01/2026-10-05 Mon/Copper-AI/render/cu-74s-9x16-r2.mp4` (73.9 s, 1772 frames, + `cu.srt`) |
| 8 Publish | r1 uploaded private (id YRX0VfpPMtU); r2 replaces it only if the user chooses | | [[Upload - Copper and the AI race]] |

## r2 prediction log

- Voice · `elevenlabs/v3` Austin `en` 1.0, 7 takes · ✅ `voice/cu-s1…s7-voice-v2.mp3` · ids in `voice/_log.jsonl`. **A first attempt failed at once ("Providing previous_text or next_text is not yet supported with the 'eleven_v3' model"), nothing charged; the takes carry no context text.**
- G1 porphyry · `openai/gpt-image-2` 4:3 high, USGS diagram as the only reference · ✅ `plates/cu-p09-porphyry-v2.png` · [ahgyz6dp…](https://replicate.com/p/ahgyz6dpsxrmw0d12cja2b02c8) · 79 s · used (the real USGS diagram was 600 px and unreadable, so the reserve was spent)
- Word timings · 7 runs ✅. **Spent about $0.40 of the $0.49 cap** (voice about $0.08, timings about $0.07, image about $0.25 if `gpt-image-2` high is that price).
- Schematic: one fluid path and a tree of veins stand for the stockwork; marked "schematic", not to scale.

## r2 budget (dollars)

Voice 7 takes about $0.09 · word timings about $0.07 · stock, drawn plates, sound $0 · reserve for one generated porphyry plate (`gpt-image-2` high, only if the USGS diagram is unreadable) about $0.25. **Base $0.41, expected $0.16, cap $0.49.**

## r1 record (5 Oct 2026, kept short)

Rendered `render/cu-61s-9x16-r1.mp4` (60.8 s, 160 words, 18 plates, 17 stock and 1 generated), 15 predictions, about $0.41 of a $0.49 cap, delegated by the user (*"do it all for yourself"*). Uploaded private as YRX0VfpPMtU; the user later made it public. r1 faults against Playbook v3: hook was a number with no stake, flat 0.45 s gaps, several one-photo-one-label plates, only 10 photos (five reused), generated plate was a simplified schematic. `gpt-image-2` price still unmeasured: read the Replicate dashboard once.

## Checks done by the agent

`PLATES 20`, durations 2.6 to 4.8 s, `LONG PLATE: none`, `EMPTY PLATE: none`; `CAPTIONS 161 words, timed by whisper`; all 7 voices complete; 73.9 s with the gaps. 21 stills looked at: no overlap between cards, callouts and captions; fixed after the stills: cathode label under the caption (now a framed plate), drawn charts enlarged. **The voice runs slow without context text (about 130 words per minute with gaps, against 160 planned): the video is 74 s, not about 60.** Added 0.12 s inner pauses after words whisper stretched (so, hot, but, someone, it, copper, not, of).

## Not verified by the agent

- **I did not hear audio or watch any video.** Voice, pace, pauses, sound mix and motion are for the user's P7 rubric ([[Workflow]]).
- Facts to recheck are listed in [[Script - Copper and the AI race]] §6 (rack figure, generic mining steps, 2043 sum).
- Not yet seen: the USGS diagram and the new photos (nothing is downloaded before P4).

## Feedback

(none yet for r2)
