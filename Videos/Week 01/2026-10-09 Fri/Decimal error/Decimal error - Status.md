---
type: process
created: 2026-10-06
updated: 2026-10-09
status: v2 redo (Vancouver index), delegated run to the render; v1 (Patriot) parked 6 Oct and replaced
tags: [status, week-01]
---

# Decimal error · Status

← [[Script - Decimal error]] · [[YouTube Channel]] · [[Workflow]]

**Delegation (user, 9 Oct 2026):** *"Redo the decimal error video entirely, from idea to render. you're free to rethink how to make it engaging, viral-like"*. The agent runs P1 to P7 without stopping and stops at the render.

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research · 2 Script · 3 Visual plan | done (agent) | delegated 9 Oct 2026 | Vancouver Stock Exchange index, 1982 to 1983. Hook type: **contradiction** ("A stock index doubled over one weekend, while the market was closed."). Theme line: *a tiny cut, always in the same direction, can halve a number*. Demand: low direct (1.7k), adjacent 200k to 227k; bridged to the money outcome. Street-lamp: pass (truncation's bias against rounding's cancelling). 161 words, 7 scenes, 10 motion plates |
| 4 Prompts, stock, budget | approved by delegation | 9 Oct 2026 | voice one take about 0.95k characters ≈ $0.03, timings ≈ $0.01, reserve for one retake ≈ $0.03, 1 Commons photo $0, 0 generated media: **base ≈ $0.07, cap ≈ $0.08** |
| 6 Generation | done | within the cap | Voice: take v1 `jt8yh0q571rmy0d13zdamvs6j0` discarded (whisper heard "can halve a number" as "have": a homophone a half-listening viewer would mishear; reworded to "can cut a number in half"); **take v2 `05x4qzd301rmt0d13zdr8s9nsr`** (Dennis, rate 0.95, 2 breaks: 0.3 before the turn, 0.2 before the question): 55.7 s, 163 of 163 words heard, 176 wpm, every silence on punctuation (0.21 to 0.82 s, none inside a clause). Timings: v1 `a16py0a5z9rmy0d13zdtgnykar`, v2 (id not captured in the trimmed output). 10 motion plates (`motion.py`, $0), every sheet looked at; fixes after the first sheets: CLOSED label off its box, trade dots no longer cross the number, the dropped 7 lands in its bin, the hairline cut stands out at 9x zoom, pulses added to the last plate. **No photo or footage:** the only free VSE photo shows its 1929 to 1946 building (it was at 609 Granville in 1982), so it was deleted. Spend ≈ $0.05 voice (2 018 characters) + ≈ $0.02 timings = **≈ $0.07** against the cap of ≈ $0.08 (prices from model pages, unconfirmed by a bill) |
| 7 Edit | done, **waiting for the user (P7)** | | `Media/Week 01/2026-10-09 Fri/Decimal-error/render/de-57s-9x16-r1.mp4` (56.8 s). Build: `MOTION SHARE` 100 %, no `REPEAT`, no `LONG PLATE`, `CHECK` all voices complete, speech starts 0.20 s, 163 words in 136 caption strips (short words pair up), `render/de.srt`. `motion.py` warnings: only the falling 7 crossing the caption band for 0.7 s (on purpose). Mix: **−14.1 LUFS, true peak −3.1 dBTP**, no music. Stills checked at 20 moments: captions clear of drawings, cards in the lower lane, frame 1 shows the board counting |
| 8 Publish · 9 Measure | pack ready, **waiting for the user's approval** | | `upload/de-publish-pack.md` and `upload/de-thumb-a.jpg` from `publish.py --dry-run` (9 Oct 2026); claims and checklist in [[Upload - Decimal error]]; private proposed; this machine has no YouTube keys |

**Learned from v1 (6 Oct 2026, user):** *"Good, for not enough. this video doesnt make the cut into yt."* and, on its voice, words that the model clipped ("harmless", "one hundred", "target") are reworded, not re-rolled. v1's notes and render were replaced by this version.

*Schematics:* the chart draws straight lines between sourced end points; the trades, the 1000.4567 update and the error bars are illustrative values ([[Script - Decimal error]] §4). *Not verified:* §5 there, plus how the take sounds, caption timing in motion, the pace of the animations in real time (only 6-frame sheets and stills seen), the sound levels on a phone.

## Feedback

User, 9 Oct 2026, on the r1 summary: *"Perfect"*. The listening rubric below is not answered yet.

User, 9 Oct 2026, on the first pack: *"rethink how do you do the thumbnail, forget about what i told you and make a fast and efficient research about youtube thumbnails, and the redo it"*. **Action:** thumbnail v2 (one drawn focal image, 2 words, no chips or logo), rules rewritten in [[Workflow]] §Thumbnail, [[Playbook]] §2b and [[Audience]]; recommended title changed to the cause (*The Rounding Error That Halved a Stock Index*) so it complements the picture.

## P7 listening rubric (answer in chat; words go under Feedback)

1. Voice natural? 2. Pace right? 3. Pauses misplaced or missing (scene, word)? 4. Sound mix right (opening hit and whooshes against the voice)? 5. Any screen empty (scene)? 6. Did any picture fail to show what was said, or arrive late (scene, word)? 7. Is the story more engaging than v1 (the Patriot version)? 8. Music: none, or a Pixabay track you pick? 9. Build the thumbnail and publish pack?
