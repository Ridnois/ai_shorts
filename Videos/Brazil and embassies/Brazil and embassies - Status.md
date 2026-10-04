---
type: research
created: 2026-10-03
updated: 2026-10-03
status: stages 0–7 done · render r3 · awaiting P7 · narrated in Spanish
tags: [research, youtube, status, brazil, shorts]
---

# Brazil and embassies · status

← [[YouTube Channel]] · [[Fast workflow]]

Third video of the channel and **first vertical Short (9:16, 60 s)**. Made with [[Fast workflow]]: text only until P4. **Narration and on-screen text are in Spanish** (made before the English-only decision of 3 Oct 2026); this note was translated afterwards, so quoted on-screen strings are translations and the original Spanish is in the script note.

## Stage log

| Stage | Status | Approved | Note |
| --- | --- | --- | --- |
| 0 Idea | ✅ P1 | 3 Oct 2026 · implicit ("Script is good") | Request: a 60 s script on Brazil's political situation and the closing of Brazilian embassies. **Feedback v1:** focus on the candidates, their crimes and how the election is sabotaged (suspected coercion). **Premise correction:** Brazil did not close embassies; it *warned it could*. The closures actually carried out are the US's and Australia's in Brazil. The script tells both |
| 1 Research | ✅ P2 | 3 Oct 2026 · implicit; **weak data stays out of the script or is attributed** | [[Research - Brazil and embassies]]: 24 claims; **supported: Jair's and Lula's cases and the rachadinhas; weak: Flávio's investigation (preliminary), the Dark Horse figure, tables in Rio and the R$ 352 M memo** |
| 2 Script | ✅ v3 → v4 | v3 approved on 3 Oct 2026; **v4 was requested by the user** (adapt the script to the voice's pace): 123 words | [[Script - Brazil and embassies (60 seconds)]]: v3 with the user's second feedback (go deeper into the court cases and make people think): final conviction · annulment · dismissal, 153 words, ≈ 59 s |
| 3 Direction | ✅ P4a | 3 Oct 2026 · implicit ("proceed to the next step") | Shots below |
| 4 Prompts and budget | ✅ P4 | **3 Oct 2026** · "Check the API model and proceed to the next step" | Below: **≈ $0.21 with a cap of ≈ $0.30** (v3) |
| 5 Tests | ✅ P5 | **3 Oct 2026** · "1: adapt the script to the pace, 2: image ok, 3: audio ok" | See *P5 test result* |
| 6 Generation | ✅ P6 | 3 Oct 2026 · "I approve the item, continue with the editing" (understood as framing `e6`, no retry) | voice 7/7, image 6/6, sound 2/2. See *P6 generation* |
| 7 Editing | ✅ render r3 · ⏳ P7 | ⏳ | `render/brasil-60s-9x16-r3.mp4`, **63.37 s, 1080×1920**, with the descriptive plates. r1 had cut sentences (fixed in r2); see *Editing r2* and *Plates v3* |
| 8 Publishing | ⏳ not started | — | Title, description with sources and AI disclosure are missing |

## Direction (vertical 9:16 · 1080×1920) · v3

Rules from [[Fast workflow]] §8: one subject, tall composition, nothing key in the bottom third or the top 6 %, **1 image per shot**. Style: technical-sketch visual style (withdrawn) (copper-orange accent = what matters). **No faces or recognisable people: each case is an object**, the same treatment for all three. No words, legible flags or logos. Scene 5's image is the **centre of the video**: it brings the three objects together so the viewer can compare.

| Scene | Seconds | Image | Shot | Emotion | Copper-orange accent |
| --- | --- | --- | --- | --- | --- |
| 1 · Hook | 0–4 | **1** (`e1`) | A cardboard ballot box with a slot, in close foreground on a table; behind it, drawn voter silhouettes; high view | Held suspense | The slot |
| 2 · Jair: final conviction | 4–11 | **1** (`e2`) | A judge's gavel on a sound block, with a thick pile of ribbon-tied pages beside it | Weight, something final | The gavel |
| 3 · Lula: annulment | 11–21 | **1** (`e3`) | A thick case file with **the wax seal broken in two** and loose pages | Something coming undone | The broken wax |
| 4 · Flávio: dismissal | 21–34 | **1** (`e4`) | A closed folder tied with ribbon, a magnifying glass on top, and an open envelope to one side | Something kept, not closed | The ribbon |
| 5 · The question | 34–42 | **1** (`e5`) | **The three objects** (gavel, case file with broken wax, folder with magnifying glass) on three plinths in a row, and a fourth **empty** plinth in front; front and high view | Stillness, question | The empty plinth |
| 6 · Disputed vote | 42–53 | **1** (`e6`) | A school voting booth at the end of a corridor, barricaded with sandbags and a chain across it | Tension | The chain |
| 7 · Close | 53–60 | **0** · reuses `e1` | Fade back to the ballot box | Reflection | — |

**On-screen text (in editing):** "4 Oct" (sc. 1), "27 years · 4 to 1" (sc. 2), "580 days · 2021" (sc. 3), "2022" (sc. 4), "47 detained" (sc. 6). Neutral labels, no names over the drawings.
**Sound (2):** a dry gavel strike on wood (sc. 2) and a school murmur with a chain (sc. 6). Silences and hard cuts, in editing: **a one-second silence before scene 5** (the question).
**Movement (Blender, no video model):** slow push; in scene 5 the push advances toward the empty plinth. Format and steps of [[Blender editing]] with `W, H = 1080, 1920`.

## Prompts (P4, approved)

**Style block (in the positive, pasted at the end of every image prompt):**

```
Detailed industrial design concept sketch on warm off-white paper, vertical 9:16 sheet. Confident black ink and graphite linework with light visible construction lines, cross-hatching for volume, flat cool-grey marker fills in several tones, and a single copper-orange marker accent on the one important element. Technical-drawing feel with blank dimension lines and arrowheads, empty numbered callout circles, and plain unmarked surfaces. A hand-drawn design sheet, with the subject in the upper two thirds and open paper at the bottom.
```

**Images** (model `black-forest-labs/flux-2-klein-4b`, `aspect_ratio` 9:16, one reference from `_canal/estilo/` chosen at P5; `e5` also receives `e2`, `e3` and `e4` as references only if P5 shows the objects are not kept: 3 extra references, ≈ $0.045 more):

| Id | Prompt (before the style block) |
| --- | --- |
| `e1` | A cardboard ballot box with a slot in close foreground on a table, a row of drawn voter silhouettes behind it, seen from slightly above; the slot is the copper-orange accent. |
| `e2` | A judge's gavel resting on a round sound block, a thick stack of bound pages tied with ribbon beside it, seen from a slightly high angle; the gavel is the copper-orange accent. |
| `e3` | A thick case file on a desk with its wax seal broken in two and loose pages fanning out, seen from above; the broken seal is the copper-orange accent. |
| `e4` | A closed folder tied with a ribbon, a magnifying glass resting on it, and an open empty envelope beside it, seen from above; the ribbon is the copper-orange accent. |
| `e5` | Four plinths in a row seen from the front and slightly above: on the first a judge's gavel, on the second a case file with a broken wax seal, on the third a ribbon-tied folder with a magnifying glass, and the fourth plinth empty and in front; the empty plinth is the copper-orange accent. |
| `e6` | A school voting booth at the end of a corridor, a barricade of sandbags and a chain stretched across the foreground, seen from a high angle; the chain is the copper-orange accent. |

**Voice** (`qwen/qwen3-tts`, `voice_clone`, **without designing a new voice**): reference = `helio-e1-voz-qwen-design-v1.wav` (the channel voice, profile B, already approved) with its text as transcript. `style_instruction`: *speak at a brisk, fluent, steady pace in a calm, informative documentary tone*. One prediction per scene (7) with the script's exact text. Files: `brasil-e<n>-voz-qwen-clone-v1.wav`.

**Sound** (`zsxkib/mmaudio`, text to audio, 2 s each; **confirm in *API* that it accepts text only**):
- `brasil-e2-mazo-v1`: *a single wooden gavel strike on a sound block in a large quiet courtroom, dry, short natural echo.*
- `brasil-e6-escuela-v1`: *echoing school corridor with distant voices and footsteps, a metal chain rattling once, steady and tense.*

## Budget in dollars (cap = base × 1.2)

| Category | Model | Base quantity | Unit price | Subtotal | Cap |
| --- | --- | --- | --- | --- | --- |
| Voice | `qwen3-tts` | 7 (≈ 944 characters) | ≈ $0.02 per 1,000 characters | **≈ $0.02** | 8 predictions |
| Sound | `mmaudio` | 2 | ≈ $0.005 | **≈ $0.01** | 2 |
| Image | `flux-2-klein-4b` | 6 | ≈ $0.015 + input reference (≤ $0.015) → **≈ $0.03** | **≈ $0.18** | 7 (≈ $0.21) |
| **Total** | | | | **≈ $0.21** | **≈ $0.30** |

- **P5 test (part of the total, not extra):** voice of scene 1 + image `e1` + sound of scene 5 ≈ **$0.04**.
- Unconfirmed assumptions: klein's price (aggregators, not Replicate) and how much it charges for the reference. If P5 shows another figure, say so before continuing.
- No thumbnail (Shorts) and scenes 6 and 7 reusing images: ≈ $0.09 saved against the earlier flow.
- For comparison: Helium cost ≈ $2 in 32 predictions.

## What awaited your decision (at the time)

1. **P1–P3 + P4a:** the new focus, the v3 text (read it aloud) and the rigor rules (convicted ≠ investigated; do not attribute the coercion)? Brazil *could* close embassies, it did not.
2. **P2:** the two weak data points (R$ 352 M memo; election date). If you want, I verify them with more searches before recording; it costs nothing on Replicate.
3. **P4:** the ≈ $0.21 budget (cap ≈ $0.30) and the prompts. Without your OK I generate nothing.

## Prediction log

Format: `scene · category · model · seed · status · URL`.

| Scene | Category | Model | Status | Prediction |
| --- | --- | --- | --- | --- |
| 1 | voice | `qwen3-tts` clone | ✅ P5 | [smemm5tpc9rmr0d1092at9z238](https://replicate.com/p/smemm5tpc9rmr0d1092at9z238) |
| 1 | image `e1` | `flux-2-klein-4b` (reference `estilo-motor-v1`) | ✅ P5 | [sm9cb1swv9rp60d1092vhzvt5r](https://replicate.com/p/sm9cb1swv9rp60d1092vhzvt5r) |
| 2 | sound | `mmaudio` ×2 | ❌ failed (no audio; probably not charged) | no id (error on text only) |
| 2 | sound | `sepal/audiogen` | ✅ P5 | [34ceyecda9rmr0d1092vf5nng8](https://replicate.com/p/34ceyecda9rmr0d1092vf5nng8) |

**Predictions at P5: 3 useful + 2 failed out of 8 planned in the cap.**

## P5 test result (3 Oct 2026)

Files in `Media/Brasil y embajadas - 60 segundos/` (`voz/`, `ilustraciones/`, `audio/`).

| Test | Result | What I could not check |
| --- | --- | --- |
| **Voice, scene 1** (`brasil-e1-voz-qwen-clone-v1.wav`) | 5.68 s; useful voice 4.91 s; **≈ 122 words per minute** on this 10-word sentence (with 1 pause between sentences) | **The timbre** and whether it sounds like Helium's |
| **Image `e1`** (`brasil-e1-v1.png`, 768×1360) | **Style and vertical OK**: cream paper, ink and marker, copper accent on the ballot box slot, faceless silhouettes. **Defects:** unreadable dimension figures (scribbles), an empty box at the bottom (title block), and the composition fills the whole frame (box in the centre, voters above) | Whether you accept it visually |
| **Sound, scene 2** (`brasil-e2-mazo-v1.wav`) | 2.0 s, **a single strike at 0.76 s with a fast decay**, matching "a gavel strike". 16 kHz mono (low quality) | **How it sounds** |
| **`mmaudio`** | **Failed on text only** ("Input Tensor has to be 2D"); it is no use without video | |

### Three decisions for you (P5)

1. **Voice pace:** if the whole script comes out at ≈ 122 to 136 words per minute, **the 153 words last 68 to 75 s, not 59**. In Helium it was 156. Options: (a) generate the whole script (≈ $0.02) and measure before deciding; (b) ask for a faster pace (`style_instruction`) and measure again; (c) cut the script (approved: P3 would have to reopen). **I recommend (a) and then (b).**
2. **Image look:** do you approve it? The dimension scribbles and the empty title block can be covered in editing (a slightly tighter frame and a paper veil); they are not regenerated.
3. **Sound:** `mmaudio` is discarded; `audiogen` comes out at 16 kHz. If it does not convince you, the alternative would be another model (to test only with your OK).

**Test spend (estimated):** voice ≈ $0.002 · image ≈ $0.03 (klein + 1 reference; **price unconfirmed on Replicate**) · sound ≈ $0.011 · **≈ $0.04**, as planned.

## P6 generation (3 Oct 2026)

**Script v4 (123 words, 765 characters)** adapted to the voice's pace, at the user's request: see [[Script - Brazil and embassies (60 seconds)]].

| Category | Files | Result |
| --- | --- | --- |
| **Voice 7/7** | `brasil-e1..e7-voz-qwen-clone-v1.wav` | Useful voice **55.8 s**; with ≈ 3 s of silences between scenes the cut lands at **≈ 58–59 s**. Pace per scene: 122, 116, 99, 156, 137, 139 and 153 words per minute (scenes 2 and 3 are slow because of the colons; **I could not hear the timbre**) |
| **Image 6/6** | `brasil-e1..e6-v1.png` and `brasil-e5-v2.png` (use v2) | `e1`, `e2`, `e3` fine. `e4` ✅ with reservations: it looks like a gift with a bow. `e5-v2` ✅: four plinths, the fourth with a copper block (not empty) and small in the frame. **`e6` ⚠️:** at the bottom, sandbags with a copper chain (good); at the top, **machine parts in a corridor** (contamination from the style reference). The 768×1360 px are scaled to 1080×1920 |
| **Sound 2/2** | `brasil-e2-mazo-v1.wav`, `brasil-e6-escuela-v1.wav` | Gavel: one strike at 0.76 s. School: 4 s (I asked for 2, raised to 4) |

### Predictions and cost (estimated)

| Category | Predictions | Cost |
| --- | --- | --- |
| Voice | 7 (1 from P5 + 6) | ≈ $0.02 |
| Image | 7 (6 + 1 retry of `e5`) | ≈ $0.21 (with reference, ≈ $0.03 each, **unconfirmed**) |
| Sound | 2 (+ 2 failed `mmaudio`) | ≈ $0.02 |
| **Total** | **16 useful** | **≈ $0.25**; cap ≈ $0.30 (image: 7 of 7) |

**The image cap (7) was reached.** Redoing `e6` goes over the cap and needs your OK (≈ +$0.03). Free alternative: in editing only the lower half of `e6` is framed (sandbags and chain).

## Editing (3 Oct 2026)

**Render r1:** `Media/Brasil y embajadas - 60 segundos/render/brasil-60s-9x16-r1.mp4`, **59.17 s**, 1080×1920, 24 fps, H.264 and AAC (with audio track). Script: `System/scripts/build_brasil.py`.

| What | How |
| --- | --- |
| Voice | 7 takes with 0.2 s of silence between scenes and **0.7 s before scene 5** (the question) |
| Image | One per scene, "page turn" between scenes and slow 6 % push. Scene 7 returns to `e1` |
| Crops | The secondary drawing (book, envelope) is removed from the bottom of `e2`, `e3`, `e4`, `e5`; paper fills the gap. `e6`: only the sandbag-and-chain strip, raised out of the caption zone |
| On-screen text | `27 years · 4 to 1` (sc. 2), `580 days · 2021` (sc. 3), `2020 → 2022` (sc. 4), `47 detained` (sc. 6), in DejaVu Sans Bold on the paper, at 30 % height from the bottom. **"4 Oct" was removed**: it fell on the ballot box |
| Sound | Gavel at second 3.0 of voice 2 (**estimated, not measured**: it may not land exactly on "convicted"); school with chain under scene 6 |
| Texture | Soft vignette and grain, as in Helium |

### What I verified and what I did not

- ✅ Duration (59.17 s), resolution and tracks (video and audio), from the mp4 headers.
- ✅ Seven key frames reviewed: crops with no visible edge except `e6` (faint), legible text outside the caption zone.
- ❌ **I cannot watch or hear the whole video.** Unchecked: timbre and pace of the voice, volume of the gavel and school against the voice, whether the strike lands on "convicted", and the fades between scenes.

### What awaits your decision (P7)

1. **Watch and listen** to the mp4. Pace, voice and sound OK?
2. **Image defects worth your judgement:** `e4` looks like a gift with a bow; `e5` has the fourth plinth with a copper block (not empty); `e6` has a faint crop edge.
3. **Before publishing (P8):** confirm the first-round date at the TSE, the original source of the R$ 352 M memo (no longer in the script) and whether the US and Australia reopened; title, description with sources and AI disclosure.

## Editing r2 (3 Oct 2026): cut sentences, fixed

**Feedback:** "phrases cut mid sentence, voice clip cut before they end, adjust the render, you can make it longer".

- **Cause (my error, not the audio's):** in Blender, `frame_offset_start` also advances the strip's visible start. The voice takes have ≈ 0.5 to 0.7 s of initial silence, so each voice started late and ended ≈ 0.6 s early. The voice files **end in silence** (checked: energy 0 in the last 80 ms).
- **Fix:** the strip is created `ini` seconds earlier, so the audible part starts at `abs` and ends at `abs + dur`, and an `assert` checks it. The tail went from 0.08 to 0.25 s.
- **Pace, longer:** silences between scenes 0.45 to 0.5 s (before 0.2), **1.2 s before the question** (before 0.7), 0.5 s of intro and 1.2 s of tail. It lasts **63.37 s** (before 59.17), still a Short.
- **Verified:** each strip covers the whole useful voice of its file, plus 0.25 s of tail (e.g. voice 2: 0.62–8.71 s is heard and the useful voice is 0.69–8.45 s). **I could not measure the mixed audio** (the background mix comes out empty): you confirm it by listening.
- The text is still v4's; recovering v3 sentences ("4 to 1", "580 days", "film financing") requires generating those voices again (≈ $0.02).

## More descriptive illustrations (v2 proposal · was pending approval)

**Feedback:** "rework on the illustrations, make them more descriptive".

**What failed:** each image was an isolated object (gavel, seal, folder). They told the *topic*, not the *mechanism*. The channel's style (industrial-designer plates) is exactly right to show how something works: here, each image explains **what happened and how**, with arrows and empty numbered circles. Secondary drawings are also avoided ("a single large plate" is requested) and so is contamination from the `estilo-motor` reference: **the reference becomes `brasil-e2-v1.png`** (the gavel, which did come out well).

| Scene | What the plate (v2) explains | Prompt (before the style block) | Accent |
| --- | --- | --- | --- |
| 1 | **Three cases, three endings** | One single large drawing filling the sheet: a cardboard ballot box in the foreground; behind it a single thick case folder from which three numbered arrows diverge to three small objects: a judge's gavel, a broken wax seal, and a closed archive box with a lid. | The ballot box |
| 2 | **Final conviction, 4 to 1** | One single large drawing filling the sheet: a long courtroom bench seen from the front with five identical high-backed chairs behind it; four chairs have a copper seat cushion and one chair has a grey cushion; on the bench a gavel on a sound block and a thick bound dossier tied with ribbon; numbered callout circles on the chairs. | The four cushions |
| 3 | **580 days and an annulment** | One single large drawing filling the sheet: on the left a small prison cell with a barred door standing open and a wall covered in tally marks grouped in fives; on the right a thick case file on a desk with its wax seal broken in two; a long curved arrow from the file to the open door. | The broken seal |
| 4 | **How the scheme worked and why it was dismissed** | One single large drawing filling the sheet: on the left five small desks in a row, each with an envelope, and dotted arrows carrying the envelopes into one open drawer of a larger desk; on the right a magnifying glass over a torn page, and a closed archive box with its lid half shut. | The drawer |
| 5 | **The question** | One single large drawing filling the sheet: four identical stone plinths in a row; on the first a gavel, on the second a case file with a broken wax seal, on the third a closed archive box with a magnifying glass, and the fourth plinth topped by a large hand-drawn question mark. | The question mark |
| 6 | **Votes under pressure: change of venue** | One single large drawing filling the sheet: an isometric view of a small neighbourhood block; on one side a school with a sandbag barricade and a chain across its entrance, on the other side a second school across the street; a large curved arrow carries a cardboard ballot box from the barricaded school to the second school. | The chain |

**Rigor rules:** no faces, no flags or letters; numbers and years still go in editing.

**Budget (in dollars):** 6 images × ≈ $0.03 (klein + 1 reference, **price unconfirmed**) = **≈ $0.18**; **cap: 7 images (≈ $0.21)** with a single retry. Accumulated spend of the video: ≈ $0.25 + $0.21 = **≈ $0.46** (the initial cap was $0.30: **over the cap, needed your approval**).

**Approved by the user ("go ahead") and executed: see *Plates v3*.** (Original plan: generate in series, look at the sheet of the six together, redo at most one, move the v1s to `_descartes/`, update the editing crops (with full plates no cropping is needed) and render r3.)

## Plates v3 (3 Oct 2026): more descriptive illustrations

**Approved:** "go ahead" (≈ $0.21, cap of 7 images). Generated in series with `brasil-e2-v1.png` as style reference: `brasil-e1-v3`, `e2-v4`, `e3-v3`, `e4-v3`, `e5-v3`, `e6-v3` (7 predictions: 6 + 1 retry of `e2`).

| Scene | What it shows | Result |
| --- | --- | --- |
| 1 | Ballot box and a case file with gavel, seal and archive box | ✅ but **the numbered arrows did not come out**: the three objects sit on the case file |
| 2 | Courtroom bench with 5 chairs | ✅ on the **retry**: **4 copper cushions and 1 grey** (the first came out 3 and 2) |
| 3 | Open cell with day marks, arrow to the broken-seal file | ✅ |
| 4 | Desks with envelopes toward a drawer, magnifying glass over a torn page and archive box | ✅ |
| 5 | Gavel, case file, box with magnifying glass and plinth with a question mark | ✅ |
| 6 | Two schools, barricade with chain and an arrow carrying the ballot box | ✅ |

**Spend of the video: ≈ $0.25 + 7 × $0.03 ≈ $0.46** (original cap $0.30; the excess was approved by the user). The earlier versions are in `ilustraciones/_descartes/`.

**Editing r3:** no crops (the v3 plates carry no secondary drawings), base push between 0.96 and 1.0 so edges are not cut, drawing raised 90 px and on-screen text at 27 % of the height. Background paper measured again. **I have not watched the whole video**; I reviewed five key frames.
