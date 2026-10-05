---
type: research
created: 2026-10-05
updated: 2026-10-05
status: stages 0 to 3 done · delegated by the user (5 Oct 2026): P4 to P6 run by the agent within the cap, stop at the render (P7)
tags: [research, youtube, status, battery, lithium, shorts]
---

# Battery and lithium · status

← [[YouTube Channel]] · [[Script - Battery and lithium]] · [[Fast workflow]] · [[Guidelines for new scripts]] · [[Channel voice]]

Short 9:16, English, **200 words** (the user's number, above the 130 to 190 range), first video with the **Austin** voice at **`speed` 1.0** ("pace 1"). Question: why did a metal that is not rare become something countries compete for? Media in `Media/Battery-lithium/` (prefix `bt-`). The Short itself carries no branding ([[Channel playbook]] §4).

## Stage log

| Stage | Status | Approved | Note |
| --- | --- | --- | --- |
| 0 Idea | ✅ | agent | 19-fact bank, scoring of six threads, five hooks in [[Script - Battery and lithium]]; street-lamp test **borderline** (swap candidate: the Big Bang lithium problem) |
| 1 Research | ✅ | agent | USGS MCS 2026 and IEA GCMO 2025 read; the rest from search summaries; see "not verified" in the script note |
| 2 Script | ✅ | agent | 200 words, 8 scenes, 5 facts, 3 spoken figures |
| 3 Direction | ✅ | agent | 21-plate visual plan, 18 stock and 3 generated; on-screen text plan |
| 4 Prompts and budget | ✅ | **delegated by the user** (5 Oct 2026: *"Follow the steps until the render, use the date atemporally, keep the 200 words"*), cap ≈ $0.41 | prompts in the script note §5, budget below |
| 5 Test | ⏳ | | scene 1 voice twice (default and the expressive variant), one generated plate and one stock photo composed |
| 6 Generation | ⏳ | | |
| 7 Editing | ⏳ | | |
| 8 Publishing | ⏳ | | |

Stock photos (free) were downloaded **before** P4 as part of package B: 13 of 14 in `Media/Battery-lithium/stock/` (credits in `_credits.jsonl`); `bt-sodium2` (Faradion) was rate-limited by Wikimedia and is still to fetch. **Weak points to decide:** five photos are small (345 to 722 px), no photo shows lithium clearly floating, one phone photo shows a Samsung logo, and one NASA image carries a date stamp (to crop). They are listed in the script note §4.

## P4 budget (dollars; Replicate is not called before your approval)

| Category | Model | Quantity | Unit price | Subtotal | Cap (×1.2) |
| --- | --- | --- | --- | --- | --- |
| Voice | `elevenlabs/v3`, `Austin`, `en`, `speed` 1.0 | 8 takes, 1,099 characters + a 41-character alternative of scene 1 for the A/B | ≈ $0.10 per 1,000 characters | ≈ $0.115 | ≈ $0.14 |
| Image (generated) | `gpt-image-1.5`, 2:3, medium | 3 plates (G1, G2, G3) | ≈ $0.05 (unconfirmed) | ≈ $0.15 | ≈ $0.18 |
| Image (stock) | free sources | 18 plates | $0 | $0 | n/a |
| Word timings | `incredibly-fast-whisper` | 8 takes | ≈ $0.01 (unconfirmed) | ≈ $0.08 | ≈ $0.10 |
| Sound | built by `build_video.py` | | $0 | $0 | n/a |
| P5 test | scene 1 voice twice, one plate | (inside the lines above) | | | |
| **Total and cap** | | | | **≈ $0.345** | **≈ $0.41** |

One retry of one plate fits inside the total cap; going over needs your approval. Prices are rates read in [[Channel models]], not confirmed on Replicate's pages; the real charge is not in the API's `metrics`, so I will report the dashboard check as unverified.

**Decisions taken with the delegation:** the borderline thread stays (no answer given, so the agent keeps the chosen one); the pause sentence is **atemporal** (scene 6 now says "for one year… a pause is not a repeal", no end date); the 200 words are kept; Zimbabwe stays cut.

## Prediction log

(empty: nothing is called before P4)

## Attribution table

Filled from `Media/Battery-lithium/stock/_credits.jsonl` when the photos are final (13 photos so far: Wikimedia Commons, NASA, ESA; CC BY, CC BY-SA, public domain: CC BY and CC BY-SA need the credit line in the description).
