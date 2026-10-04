---
type: research
created: 2026-10-03
updated: 2026-10-03
status: stages 0–7 done · render r2 · awaiting P7 · narrated in Spanish
tags: [research, youtube, status, lemon-cake, shorts]
---

# Lemon cake · status

← [[YouTube Channel]] · [[Fast workflow]]

Fourth video of the channel, **second vertical Short (9:16)**. Made with [[Fast workflow]]: text only until P4. **Narration and on-screen text are in Spanish** (made before the English-only decision of 3 Oct 2026). The original Spanish name of the video was "Queque" (a Chilean word for a loaf cake); this note was translated afterwards, so on-screen strings quoted below are translations.

## Stage log

| Stage | Status | Approved | Note |
| --- | --- | --- | --- |
| 0 Idea | ✅ P1 | **3 Oct 2026** · "I approve the approach" | Request: "a script on how to make a lemon cake"; **up to 20 images** and **a voice model that sounds better and is cheap** (3 Oct 2026) |
| 1 Research | ✅ P2 | **3 Oct 2026** · "we publish it as a base recipe" (not baked beforehand) | [[Research - Lemon cake]]: 15 claims; **quantities contradict each other across sources** (eggs 2 or 4; baking powder 1 or 2 teaspoons; oven 30 to 60 min). **The recipe was not tested** |
| 2 Script | ✅ P3 | 3 Oct 2026 · implicit on approving the approach | [[Script - Lemon cake (80 seconds)]]: 179 words, ≈ 80 s, 8 scenes |
| 3 Direction | ✅ P4a | 3 Oct 2026 · implicit | 20 plates, below |
| 4 Prompts and budget | ✅ P4 | **3 Oct 2026** · "I approve the budget" | **≈ $0.70, cap ≈ $0.90** |
| 5 Tests | ✅ P5 | 3 Oct 2026 · "Horrible illustration… elevenlabs is better, no batidora sound" | `elevenlabs/v3` chosen; the image was redone |
| 6 Generation | ✅ P6 | 3 Oct 2026 · **delegated**: "follow the rest yourself till the render… make all decisions" | 8 voices, 20 plates, 0 sounds. See *Generation and editing* |
| 7 Editing | ✅ render r2 · ⏳ P7 | ⏳ | `render/queque-80s-9x16-r2.mp4`, **81.22 s, 1080×1920**, with `gpt-image-1.5` and the new text style. r1 used the old plates |
| 8 Publishing | ⏳ not started | — | Title, description with sources (**declare "base recipe from several sources"**) and AI disclosure are missing |

## Voice: more natural and cheap (proposal, decided at P5)

**Why change:** the `qwen3-tts` voice came out at ≈ 122 words per minute, with no speed control and long pauses ([[Brazil and embassies - Status]]). A model with `speed` allows adjusting the voice to the script and avoids cutting the text or regenerating.

| Model | Price (Replicate, 3 Oct 2026, from [[Channel models]]) | Cost of this script (≈ 1,010 characters) | Why |
| --- | --- | --- | --- |
| **`minimax/speech-2.8-turbo`** (recommended) | ≈ $0.06 per 1,000 tokens (≈ 1 token per character) | **≈ $0.06** | Multilingual, with speed and emotion control; more natural than an open TTS according to the comparisons I read. **The name of `speed` and of the Spanish voices must be confirmed in the API tab** |
| `elevenlabs/v3` | $0.10 per 1,000 characters | ≈ $0.10 | The most expressive voice, at a still small cost |
| `qwen/qwen3-tts` (current) | $0.02 per 1,000 characters | ≈ $0.02 | Baseline: already known, slower |

- **P5 voice test:** only scene 1 (≈ 100 characters) in `minimax/speech-2.8-turbo` and in `elevenlabs/v3`: **≈ $0.02 in total**. **I cannot hear the difference: you choose.** One is chosen and not changed again.
- Chilean or neutral Spanish: a voice is chosen in the test.
- **Limitation:** "sounds better" is an impression only you can judge.

## Direction: 20 plates (vertical 9:16 · 1080×1920)

Rules from [[Fast workflow]] §8 and §9: **a single large plate per image, explaining the mechanism** (arrows, empty numbered circles, cutaway views), focus between 15 and 60 % of the height, nothing key in the bottom third or the top 6 %. Style: technical-sketch visual style (withdrawn); **copper-orange accent = what matters in each step**. No faces, words or figures inside the drawing (they go in editing). The quantities that matter are **checked by eye**.

| # | Scene | What the plate explains | Accent |
| --- | --- | --- | --- |
| 1 | 1 Hook | **The result**: two cake cross-sections side by side, one low and dense (the brick) and one tall with many bubbles | The tall crumb |
| 2 | 1 Hook | **The six steps**: a path of six numbered stones from a bowl to an oven, each with its icon | The path's arrow |
| 3 | 2 Ingredients | **The ingredients**: 2 cups of flour, 1 of sugar, 1 of milk, half a cup of butter, 2 eggs, teaspoons and vanilla, in a row | The butter |
| 4 | 2 Ingredients | **At room temperature**: a stick of butter with a finger denting it; two eggs beside it; an arrow from the fridge to the table | The finger dent |
| 5 | 2 Ingredients | **Why**: a bowl with butter and eggs and a magnifying circle showing the emulsion with trapped air bubbles | The bubbles |
| 6 | 3 Creaming | **Beating**: a hand-held electric mixer over a bowl of butter and sugar, with arrows on the beaters | The beaters |
| 7 | 3 Creaming | **The why, in cross-section**: sugar crystals opening air pockets inside the butter | The air pockets |
| 8 | 3 Creaming | **Before and after**: two bowls, one with a dense yellow mix and one with pale, fluffy cream, with an arrow | The arrow |
| 9 | 4 Eggs | **One at a time**: a hand cracks an egg over the bowl while another egg waits aside | The falling egg |
| 10 | 4 Eggs | **If it splits**: two bowls, one with a curdled, lumpy mix (cold egg) and one smooth and glossy | The curdled mix |
| 11 | 5 Dry and milk | **Sifting**: a sieve over a bowl with flour and baking powder falling | The falling powder |
| 12 | 5 Dry and milk | **Alternating**: a bowl with three arrows in sequence, flour, milk, flour | The arrows |
| 13 | 5 Dry and milk | **The gluten**: on the left a spatula mixing gently; on the right a hard beating with elastic strands in a magnifying circle | The strands |
| 14 | 6 Oven | **The pan**: a brush with butter and flour dusted in a long pan | The brush |
| 15 | 6 Oven | **Pouring**: the batter falling from a bowl into the pan with a spatula | The batter |
| 16 | 6 Oven | **Why it rises**: an oven in cross-section with the pan inside, heat arrows and bubbles expanding in the batter | The heat arrows |
| 17 | 7 The test | **The toothpick**: a cake with a toothpick stuck in the centre and another clean toothpick aside | The clean toothpick |
| 18 | 7 The test | **Resting**: the pan on a rack with an hourglass and an arrow toward unmoulding | The hourglass |
| 19 | 8 Close | **The result**: a cut cake with a lifted slice showing the crumb with bubbles | The slice |
| 20 | 8 Close | **The six steps**: six objects on a shelf (butter, egg, sieve, spatula, pan, toothpick) with **an empty slot** | The empty slot |

**On-screen text (in editing):** `Step 1` to `Step 6` (scenes 2 to 7), `180 °C` (sc. 6), `35–40 min` (sc. 7). Step numbers go at 27 % height from the bottom, as in [[Brazil and embassies - Status]].
**Sound (2 effects, optional):** short electric mixer (sc. 3) and the oven alert (sc. 7), with `sepal/audiogen`.
**Editing (Blender):** `build_brasil.py` as the base; one image every ≈ 4 s, "page turn" between scenes, cross-fade within a scene. Change `W, H = 1080, 1920`, done.

## Prompts (P4, approved)

**Style block (in the positive, at the end of each prompt):**

```
Detailed industrial design concept sketch on warm off-white paper, vertical 9:16 sheet. Confident black ink and graphite linework with light visible construction lines, cross-hatching for volume, flat cool-grey marker fills in several tones, and a single copper-orange marker accent on the one important element. Technical-drawing feel with blank dimension lines and arrowheads, empty numbered callout circles, and plain unmarked surfaces. A hand-drawn design sheet.
```

**Images:** `black-forest-labs/flux-2-klein-4b`, `aspect_ratio` 9:16, PNG format, **one reference**: `brasil-e4-v3.png` (the plate that best explains a mechanism). Every prompt starts with *"One single large drawing filling the sheet:"* and ends with *"<X> is the copper-orange accent."*

| # | Prompt (before the style block) |
| --- | --- |
| 1 | two cross-sections of baked cakes side by side: on the left a low flat dense loaf with tiny holes, on the right a tall domed loaf full of round air bubbles; numbered callouts on both. The tall loaf's golden crust |
| 2 | six numbered stepping stones forming a winding path from a mixing bowl at the bottom to an oven at the top; on the stones a butter block, an egg, a sieve, a spatula, a loaf pan and a toothpick. The path's arrow |
| 3 | a flat-lay of baking ingredients in a row: two measuring cups of flour, one measuring cup of sugar, one measuring cup of milk, half a cup of butter, two eggs, two measuring spoons and a small vanilla bottle. The butter |
| 4 | a block of butter on a counter with a finger pressing a dent into it, two eggs beside it, and a curved arrow from an open refrigerator to the counter. The dent in the butter |
| 5 | a mixing bowl with soft butter and two eggs inside, and a large magnifying circle showing a smooth emulsion with tiny trapped air bubbles. The air bubbles |
| 6 | a handheld electric mixer with two beaters over a bowl of butter and sugar, curved arrows around the beaters. The beaters |
| 7 | a cutaway of a block of butter with sugar crystals cutting small round air pockets inside it, with an enlarged circle and arrows. The air pockets |
| 8 | two bowls side by side with an arrow between them: on the left a dense yellow mixture, on the right pale fluffy cream. The arrow |
| 9 | a hand cracking an egg over a mixing bowl while a second egg waits on the counter beside it. The falling egg |
| 10 | two bowls side by side: on the left a curdled lumpy mixture with a cold egg and an ice cube beside it, on the right a smooth glossy mixture. The curdled lumps |
| 11 | a sieve held over a bowl with flour and baking powder falling in a fine cloud. The falling powder |
| 12 | a mixing bowl with three arrows in sequence around it: a scoop of flour, a jug of milk, a scoop of flour. The three arrows |
| 13 | two panels: on the left a spatula gently folding batter, on the right a whisk beating hard with elastic gluten strands shown in an enlarged circle. The gluten strands |
| 14 | a brush spreading butter inside a long loaf pan while flour is dusted over it. The brush |
| 15 | batter pouring from a bowl into a loaf pan with a spatula scraping the bowl. The pouring batter |
| 16 | a cutaway of an oven with a loaf pan inside, heat arrows rising from below, and the batter in the pan showing expanding round bubbles and a rising dome. The heat arrows |
| 17 | a baked loaf with a toothpick stuck in the centre and a second clean toothpick lying beside it. The clean toothpick |
| 18 | a baked loaf in its pan on a wire cooling rack with a large sand timer beside it and a curved arrow toward an unmoulding. The sand timer |
| 19 | a sliced loaf with one slice lifted to show a crumb full of small air holes. The lifted slice |
| 20 | a wooden shelf with six objects in a row (a butter block, an egg, a sieve, a spatula, a loaf pan, a toothpick) and one empty slot in the row. The empty slot |

**Voice:** `minimax/speech-2.8-turbo` (and `elevenlabs/v3` only in the test), 8 takes, one per scene, with the script's exact text; speed fixed in the P5 test. The API tab's schema is copied before calling.
**Sound:** `sepal/audiogen`, 2 s each: *"an electric hand mixer whirring briefly over a metal bowl, close microphone, steady"* and *"a kitchen oven timer bell ringing twice, quiet kitchen"*.

## Budget in dollars (cap = base × 1.2)

| Category | Model | Base quantity | Unit price | Subtotal | Cap |
| --- | --- | --- | --- | --- | --- |
| Image | `flux-2-klein-4b` | **20** | ≈ $0.03 (klein + 1 reference, **unconfirmed**) | **≈ $0.60** | 24 images (≈ $0.72) |
| Voice | `minimax/speech-2.8-turbo` | 8 takes (≈ 1,010 characters) | ≈ $0.06 per 1,000 | **≈ $0.06** | 10 predictions |
| Voice · test | the two candidates, scene 1 | 2 | ≈ $0.01 each | **≈ $0.02** | |
| Sound | `sepal/audiogen` | 2 | ≈ $0.011 | **≈ $0.02** | 2 |
| **Total** | | | | **≈ $0.70** | **≈ $0.90** |

- **P5 test (inside the total):** one image (#1), the scene 1 voice in both models and one sound: **≈ $0.06**.
- Retries: **only once** per image, only if the prompt changes; the images most prone to fail by counting are 3, 20 and 1.
- For comparison: the Brazil Short cost ≈ $0.46 with 7 images; here 20 images are ≈ $0.60.

## What awaited your decision (at the time)

1. **P1–P3 + P4a:** the approach ("six steps, each with its why"), the text (read it aloud) and the 20 plates?
2. **P2:** quantities contradict each other across sources and **the recipe was not tested**: do you bake once before publishing, or do we publish as a "base recipe"?
3. **P4:** the ≈ $0.70 budget (cap ≈ $0.90) and the prompts. **Without your OK I generate nothing.**

## Prediction log

Format: `scene · category · model · status · prediction`.

| Scene | Category | Model | Status | Prediction |
| --- | --- | --- | --- | --- |
| 1 | voice | `minimax/speech-2.8-turbo` (voice `Casual_Guy`, `language_boost: Spanish`) | ✅ P5 | [w657yw5gmxrmy0d10a3vszb1ww](https://replicate.com/p/w657yw5gmxrmy0d10a3vszb1ww) |
| 1 | voice | `elevenlabs/v3` (voice `Roger`, `es`) | ✅ P5 | [qbdbkrpbt5rmr0d10a3rq3m3sw](https://replicate.com/p/qbdbkrpbt5rmr0d10a3rq3m3sw) |
| 1 | image #1 | `flux-2-klein-4b` (reference `brasil-e4-v3`) | ✅ P5 | [mmczstr0enrzy0d10a4859yx8c](https://replicate.com/p/mmczstr0enrzy0d10a4859yx8c) |
| 3 | sound | `sepal/audiogen` | ✅ P5 | [7axfrz9jdhrmr0d10a4a44xvam](https://replicate.com/p/7axfrz9jdhrmr0d10a4a44xvam) |

**Predictions: 4 of the 4 in the test.**

## P5 test result (3 Oct 2026)

Files in `Media/Queque - 80 segundos/` (`voz/`, `ilustraciones/`, `audio/`).

| Test | Result | What I could not check |
| --- | --- | --- |
| **Voice `minimax/speech-2.8-turbo`** (`queque-e1-voz-minimax-turbo-v1.wav`) | 7.98 s for 19 words (≈ 143 words per minute with pauses), 32 kHz mono. Built-in voice `Casual_Guy`, with `language_boost: Spanish` | **Whether it sounds natural, the accent and whether it reads "queque" well** |
| **Voice `elevenlabs/v3`** (`queque-e1-voz-eleven-v3-v1.mp3`) | 6.73 s for the same 19 words (≈ 169 words per minute with pauses), 44.1 kHz. Voice `Roger`, `es` | The same |
| **Image #1** (`queque-i01-v1.png`, 768×1344) | Conveys the idea: **a low, dense cut on the left and a tall piece with bubbles on the right**; style and copper fine. **Reservations:** the tall piece looks more like a long loaf of bread than a cake; illegible dimension figures (scribbles); the drawing fills only the middle band | Whether you accept it |
| **Sound** (`queque-e3-batidora-v1.wav`) | 2.0 s, 16 kHz mono | How it sounds |

### Decisions for you (P5)

1. **Voice:** listen to both and choose. Pace estimate with 179 words: `minimax` ≈ 80 to 85 s; `elevenlabs` ≈ 65 to 70 s. **With `speed` either can be adjusted.** `qwen` is out. Cost of the voice tests ≈ $0.02.
2. **Image:** do you approve the look? If not, what would you change (for example, the tall piece shaped like a cake pan).
3. **Sound:** is it useful?

**Test spend (estimated):** voice ≈ $0.02 · image ≈ $0.03 (klein price unconfirmed) · sound ≈ $0.011 · **≈ $0.06**, as planned.

## Feedback after the test and decisions (3 Oct 2026)

> *"Horrible illustration, look for home queque, no nuts on them, no circles, search on the internet homemade queque so you understand, transparent rectangular oven dish, lemon zest queque. Readjust the script. Elevenlabs is better, no batidora sound."* (the user's words mixed English and Spanish; the Spanish part is translated) and *"follow the rest yourself till the render, you can make all decisions and wait for me with the render ready."*

| Feedback | What I did |
| --- | --- |
| "Horrible" illustration: home-made cake, no nuts, **no circles** | The earlier plate copied numbered circles from the `brasil-e4-v3` reference. **The reference, the numbered circles and the round bubbles were removed** from the style (new block in the positive: straight lines, arrowheaded arrows, angular and irregular shapes) |
| **Transparent rectangular dish** and **lemon** | Every plate with oven or batter shows the rectangular glass dish; lemon zest in the batter and a grater among the ingredients. Search for home lemon cake: zest in the batter, 180 °C, rectangular dish and a clean toothpick were confirmed |
| Readjust the script | Script v2: **lemon** cake, glass dish, zest at the end of the batter, no vanilla; 197 words. See [[Script - Lemon cake (80 seconds)]] |
| `elevenlabs/v3` is better | Voice `Roger`, `es`, speed 0.95; `previous_text` and `next_text` for intonation |
| No mixer sound | **No sound effects** in the whole video (I cannot judge `audiogen` and the first one was rejected) |

## Generation and editing (3 Oct 2026)

| Category | Predictions | Cost (estimated) |
| --- | --- | --- |
| Voice | 2 from the test (P5) + 8 (`elevenlabs/v3`, 1,107 characters) | ≈ $0.12 |
| Image | 1 test v1 (with reference) + 1 test v2 + 19 plates + 2 retries (#18 and #20) = **23** (cap 24) | ≈ $0.36 (without reference ≈ $0.015 each; **price unconfirmed**) |
| Sound | 1 from the test (discarded) | ≈ $0.01 |
| **Total** | **34** | **≈ $0.50**; approved cap ≈ $0.90 |

**Render r1:** `Media/Queque - 80 segundos/render/queque-80s-9x16-r1.mp4`, **81.22 s**, 1080×1920, video and audio (checked in the mp4 headers). Script: `System/scripts/build_queque.py`.

- **Voice:** 8 takes; each strip covers its full voice plus 0.25 s of tail (checked against the file's times); 0.4 s silence between scenes and 0.9 s before the close.
- **Plates:** 20, spread per scene (2, 3, 3, 2, 3, 3, 2, 2) in equal parts, with a 0.3 s cross-fade within each scene and "page turn" between scenes; slow 6 % push. **Plate changes are not synced to each word**, only to the scene.
- **Text:** `6 steps`, `Step 1` to `Step 4`, `Step 5 · 180 °C` and `Step 6 · ≈ 40 min`, on a paper band at 20–34 % from the bottom.
- No sound effects, no music.

### What I checked and what I did not

- ✅ Duration and tracks of the mp4; eight key frames (framing, band and legible texts).
- ❌ **I did not hear the audio or watch the whole video:** voice, pace (the 8 takes add up to 77.6 s raw for 197 words, ≈ 150 words per minute with pauses), fades and whether the band covers anything important.
- **Plates that deviate:** #2 (the six-stone path shows only four cards with legible icons), #5 (an insert with orange dots), #12 (the three arrows look like spoons), #20 (five objects instead of six, no toothpick, and the slot is not clear). The rest are fine.
- **Recipe:** still not baked; the quantities come from several sources that do not match.

### What awaits your decision (P7)

1. **Watch and listen** to the mp4: voice and pace OK? Do the plate changes land where they should?
2. Do I redo #2, #12 and #20 (≈ $0.05, 1 image of margin in the cap)?
3. **Before publishing (P8):** title, description as a *base recipe from several sources* (the time depends on the oven) and AI disclosure.

## v3 illustrations with `nano-banana-2` (3 Oct 2026) · spend pending approval (superseded by the next section)

> *"Improve the estilo visual dataset, use nano-banana-2 for images and provide them more context, redo the prompts for the images adding more context of the scene they are representing, make this with the queque video and rerender it."*

**Done (text only and one test image):**
- **Style dataset v2** in the technical-sketch visual style (withdrawn): style block v3, scene-context template, real-object sheets, error catalogue and 5 references in `_canal/estilo/v2/`.
- **20 prompts with scene context** (≈ 200 to 270 words each: what the video is about, what the narration says at that moment, the subject with real details, composition and accent): Lemon cake image prompts (withdrawn).
- **Test of image #1** with `google/nano-banana-2` (2 dataset references and `image_search`): `ilustraciones/queque-i01-nb1.png`. Result: glass dishes with handles, a golden cake with a crack, half a lemon, no circles. **It is a clear improvement over `flux-2-klein-4b`.**

**Budget to finish (in dollars):**

| Item | Quantity | Price | Subtotal |
| --- | --- | --- | --- |
| `nano-banana-2` (1K, 9:16), images #2 to #20 | 19 | ≈ $0.067 (**unconfirmed whether references or `image_search` are charged separately**) | **≈ $1.27** |
| Test already done (#1) | 1 | ≈ $0.067 | ≈ $0.07 |
| Retries (at most one per image and up to the 24-image cap) | up to 4 | ≈ $0.067 | up to ≈ $0.27 |
| Voice, editing | reuses what is done | $0 | $0 |
| **Total of this round** | | | **≈ $1.34**; cap **≈ $1.61** |

- Previous spend of the video: ≈ $0.50; with this round the video reaches **≈ $1.85** (cap ≈ $2.10). **It exceeds the approved cap ($0.90).**
- It is ≈ 4.5 times what the `flux-2-klein-4b` round cost (≈ $0.29 for the 19 plates).
- **If you approve:** I generate #2 to #20 in series (batches of ≤ 10), look at the 20 together, redo at most the ones that fail, adapt `build_queque.py` to the new plates and render `queque-80s-9x16-r2.mp4`. The voice does not change.
- **If you prefer to spend less:** only the 10 most important plates could be generated with `nano-banana-2` (#1, 5, 7, 10, 13, 16, 17, 19, 20 and 2) and the rest left with those of `flux-2-klein-4b`; ≈ $0.60.

## `gpt-image-1.5` round + text style + render r2 (3 Oct 2026)

> *"Design a style for text, it must be sober, professional and modern, then proceed with the next steps, remove the old photos and proceed with gpt-image-1.5."*

| What | How |
| --- | --- |
| **Text style** | New label card (copper bar, spaced label and bold title): [[On-screen text style]]. Scenes 1 to 7; scene 8 stays without a card |
| **Images** | All 20 with `openai/gpt-image-1.5` (medium quality, 2:3, 3 references from a technical-sketch reference library (withdrawn) depending on the plate type, **no own references**). The paper was extended top and bottom to 9:16 with each plate's real edge colour (`queque-iNN-gpt-v.png`) so the sides are not cropped |
| **Old photos** | **Deleted:** the 20 `flux-2-klein-4b` plates, the retries (#18 and #20), the `nano-banana-2` test (#1) and the `_descartes` folder; in `_canal/estilo/`, `v2/` was deleted (copies of old plates). **Kept:** the 20 `gpt-image-1.5` originals and, in `_canal/estilo/`, `v1`, `v3-externas` and `v4-gpt`. *(The model research images are no longer in this folder: they live in `_canal/investigacion/`.)* |
| **Retries** | None: all 20 came out and are accepted (see reservations) |

**Spend of this round (estimated):** 20 images × ≈ $0.05 (OpenAI's rate for 1024×1536 at medium quality, **not confirmed on Replicate**) ≈ **$1.00**. With the `nano-banana-2` test plate (≈ $0.07), the video accumulates **≈ $1.57**. *(Image model research is kept separate and does not count in the video's cost.)*

**Render r2:** `render/queque-80s-9x16-r2.mp4`, 81.22 s, 1080×1920, video and audio. The voice is the same as in r1 (`elevenlabs/v3`).

### Reservations

- **Empty labelling boxes** (I asked for "blank boxes" to avoid text): they appear on almost every plate and read as unfilled placeholders. If they bother, v4 of the prompt asks for them as *guide lines ending in a small arrow*, with no boxes (it would cost to regenerate).
- **#1 and #20**: lots of empty paper; #20 shows a highlighted orange gap and not exactly five objects.
- **I did not hear the audio or watch the whole video**; I saw eight key frames of the edit (cards, framing).
- The recipe is still **not baked**; publish as a *base recipe from several sources*.

### What awaits your decision (P7)

1. Watch and listen to the mp4. Text style and plates OK?
2. Do we regenerate the plates without empty boxes (≈ $1.00 with `gpt-image-1.5` at medium quality; ≈ $0.26 at low quality, untested)?
3. To publish: title, description as a *base recipe*, AI disclosure.
