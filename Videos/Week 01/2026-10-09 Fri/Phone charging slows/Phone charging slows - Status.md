---
type: process
created: 2026-10-09
updated: 2026-10-09
status: r3 (new voice and master) rendered; waiting for the user (P7)
tags: [status, week-01]
---

# Phone charging slows · Status

← [[Script - Phone charging slows]] · [[YouTube Channel]] · [[Workflow]]

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research | done | user asked 9 Oct 2026 | Source: `Analytics/Generated ideas/Takeaways - youtube.md`. Y: fast charge and a long-lived battery. X: lithium plating near full forces the taper. Hook type: contradiction. **Surprise scored 3 (needs 4): the user's yes needed.** Demand check not run (no YouTube token here). Street-lamp: pass only with the plating step |
| 2 Script · 3 Visual plan | done (agent) | | 112 words, 5 scenes, 14 plates ([[Script - Phone charging slows]]); written to the low-attention rule |
| 4 Prompts, stock, budget | approved by delegation | 9 Oct 2026 (user: "go for the render", surprise-3 idea accepted) | nothing downloaded or generated; estimate about $0.15 (voice 5 takes 0.07, timings 0.05, 0 generated plates; prices unconfirmed), cap about $0.18 |
| 6 Generation · 7 Edit | done, **waiting for the user (P7)** | | voice 5 takes turbo-v2.5 (about 610 characters), 5 timings, 0 generated plates, 5 drawn plates (charge curve in 2 states, graphite in 2 states, stage bar), 5 stock photos (credits in `stock/_credits.jsonl`). Render `Media/Week 01/2026-10-09 Fri/Phone-charging-slows/render/pc-42s-9x16-r1.mp4` (42.4 s, 14 plates 2.7 to 3.4 s, `CHECK` all voices complete, no `EMPTY PLATE`, 112 words captioned). Spend about $0.07 voice + 0.05 timings = about $0.12 against the cap of about $0.18 (prices unconfirmed). **Not verified:** voice, mix, caption timing in motion, pace; the engagement rules are [H] |

**r2, visual redesign test (9 Oct 2026, $0):** same voice, words and pauses; visuals rebuilt with the new [[Playbook]] §3 (research: [[2026-10-09 Visual research]]): 8 motion plates cut on the word (hook counter and speed bar, current into the phone, zoom into the cell, graphite filling then lithium plating, the two-stage charge curve, overnight charging, the phone again with the conclusion card, the speed-or-battery switch with the question). `MOTION SHARE` 100 %, no `REPEAT`, no `motion.py` warnings, `CHECK` all voices complete. Render `Media/Week 01/2026-10-09 Fri/Phone-charging-slows/render/pc-42s-9x16-r2.mp4` (r1 kept for comparison; r1 plan in `plan-r1.json`). No footage: Commons has none for phone charging and Pexels/Pixabay need the user's free keys. The only Commons clip found (USB chargers) failed the swap test (shaky, Samsung logo, shows chargers not current) and was deleted. **Not verified:** motion in real time (only 6-frame sheets and 2 s stills seen), whether the calm lower third reads as empty, the Apple overnight curve (shape from a search summary, schematic).

**r3, audio redesign test (9 Oct 2026):** same script and pictures (motion plates re-timed to the new take); voice = one Inworld TTS-2 take (`Dennis`, rate 0.95, one 0.3 s break before the conclusion; `voice/pc-take-v2.wav`, prediction `244kpkqsp5rmr0d13yrs3a72r4`; take v1 discarded: its 0.7 and 0.6 s breaks became 1.2 s silences). 37.9 s of speech, 112 of 112 words heard, silences 0.34 to 0.64 s and one 0.86 s beat. Captions snapped to the speech onsets. Sound: opening hit and scene whooshes only, no drone, no music (Pixabay music needs a manual pick). Mix: −14.0 LUFS, true peak −2.8 dBTP, mix-to-picture lag 20 ms. Render `Media/Week 01/2026-10-09 Fri/Phone-charging-slows/render/pc-39s-9x16-r3.mp4` (39.5 s); r2 plan in `plan-r2.json`. Spend for r3 about $0.05 (two takes about $0.04, one timing call about $0.01): video total about $0.17 against the cap of about $0.18 (prices from model pages, unconfirmed by a bill). **Not verified:** how the new voice sounds, whether Dennis suits the persona, the voice chain's EQ on a phone.

*Not verified:* see the Script note §5.

## Feedback (user, 9 Oct 2026, on r2)

*"I see a significant visual improvement, content is way appealing this way. voice and audio feels broken now, i want you to redesign that segment of the process, also lets use pixabay"*; on a listening test: *"lets skip the test and go for a higher tier model"*. **Rubric:** visuals better (r2 over r1); voice and audio broken. **Measured on r2** (the voice track is identical in r1 and r2): master −20.8 LUFS (YouTube's reference is −14); take levels drift 1.6 LU (scene 1 −19.7, scene 5 −21.3); whisper word starts sit at the start of the preceding silence, so captions and cuts run up to 1 s early ("Tell" shows 0.94 s before it is heard); the pause cutter made a 0.35 s gap inside "Should … phones" that is not in the raw take (its quiet threshold, 10 % of the peak, catches soft consonants); the takes' own pauses are digital silence (−90 dBFS) under a 110 Hz sine bed phones barely play. **Actions:** audio segment redesigned ([[Playbook]] §5, [[2026-10-09 Audio research]]); Pixabay key stored in `.env`.

## P7 listening rubric (answer in chat; words go under Feedback)

1. Voice natural? 2. Pace right? 3. Pauses misplaced or missing (scene, word)? 4. Sound mix right? 5. Any screen empty (scene)? 6. Did any picture fail to show what was being said, or arrive late (scene, word)? 7. r2 against r3: does the new voice sound continuous and calm, and is the loudness right on a phone? 8. Music: none, or a Pixabay track you pick? 9. Build the thumbnail and package?
