---
type: research
created: 2026-10-03
updated: 2026-10-03
status: v2 · feedback from the first 5 videos compressed into rules; English-only since 3 Oct 2026
tags: [research, youtube, script, guidelines, feedback]
---

# Guidelines for new scripts

← [[YouTube Channel]] · [[Fast workflow]]

**Read it whole before writing a script.** It is the feedback from the videos ([[Magnets and geopolitics - Status]], [[Helium and power - Status]], [[Brazil and embassies - Status]], [[Lemon cake - Status]]) reduced to rules. Each rule says where it comes from. Production details (models, prices, budget) are in [[Fast workflow]].

> **Language (user decision, 3 Oct 2026): every new script is written and narrated in English**, with English on-screen text, English prompts and an English description. Research, status notes and budgets are also in English. The earlier videos (Spanish narration) are a record and are not redone unless the user asks. Voice: [[Channel voice]].

> **What good content is (user's definition):** the kind you can enjoy and keep watching *even knowing it is AI*; informative or absurd, but it delivers its message. Channel goal: **narrated learning**, educate and entertain. References: *Sleep on Physics*, *Sleep on Science*. Detail: [[YouTube with AI - quality content guide]].

## 1. Script

**Craft and structure of a Short: [[Narration guide]]** (source of truth). This table is the feedback that originated it.

| # | Rule | Comes from |
| --- | --- | --- |
| 1.1 | **Tension comes from context, not from waiting.** A concrete fact that shows what is at stake builds more tension than a pause. | Magnets: "slow, as if forcing curiosity" |
| 1.2 | **Every hook is resolved within its scene or the next**, and answers all three: **what it is**, **why it happened**, **what it means**. | Magnets: "was a magnet missing? why? what does it mean?" |
| 1.3 | **Simplifying is not removing the why.** If you must cut, sacrifice the side detail (dates, names, secondary figures), not the cause → effect chain. | Magnets |
| 1.4 | **Make them think.** Deliver an idea the viewer closes alone (e.g. "a case that falls on procedure never gets to judge the facts"; "if it goes wrong, it is not the recipe: it is a step"). A list of facts is not enough. | Brazil (feedback 2) |
| 1.5 | **Focus on causes, not lists.** Every step or case carries its why in the same sentence. | Lemon cake |
| 1.6 | **Brisk pace:** short sentences full of information, no filler pauses. Silence is used **once, on purpose** (e.g. 1.2 s before the central question). | Magnets, Brazil |
| 1.7 | **One new idea per scene.** If a scene explains two things, split it. | Magnets |
| 1.8 | **Write for the ear and read it aloud.** Whatever sounds forced or dramatic gets rewritten. | Magnets |
| 1.9 | **Figures and dates go on screen, not in the voice** (`180 °C`, `27 years · 4 to 1`). | Brazil, Lemon cake |

### Rigor

- **Every figure with source and date**; weak material stays out of the script or is attributed ("according to…"). Use "can" / "could" when the source is weak. Check the premise of the request: Brazil *warned it could* close embassies, it did not close them.
- **Convicted ≠ accused ≠ investigated ≠ dismissed.** Use the exact words of the ruling; same treatment for every character; nobody gets adjectives.
- **If sources contradict each other** (recipe quantities), publish it as "a base recipe from several sources" and say so in the description.
- **Focus of the request:** if the user fixes a focus ("candidates, their crimes and how the election is sabotaged"), respect it; do not widen it.

### Duration and pace

- A Short (9:16) fits ≈ 60 s, but **"longer is fine"** if needed (63 to 93 s worked). Do not speed up the voice to make it fit.
- **Adapt the script to the pace of the voice, or use a model with `speed`**; do not cut blindly or regenerate. Planning: ≈ 150 words per minute with `elevenlabs/v3` at `speed` 0.95 (Lemon cake: 197 words → 77.6 s; Chips: 211 words → 88 s). **Measure with the complete script**, not one sentence (a single sentence gave 122; the whole script, 156). **The English pace is still to be measured** ([[Channel voice]]).
- Hook in the **first 3 s**, with the strongest image.

### Checklist before P3

- [ ] Does every hook answer what it is, why and what it means?
- [ ] Is there a pause or sentence that exists only to create suspense?
- [ ] Does someone who knows nothing understand the cause → effect chain **without seeing the images**?
- [ ] Does it leave an idea that makes you think, without reproach or sermon?
- [ ] Read aloud: where does it drag?
- [ ] Is every claim supported or attributed?

## 2. Illustrations: `flux-kontext-pro` + real photo

Style, method and prompt template: [[Visual style - plasticine miniatures]]. Source feedback: Brazil ("there is no relation between the illustrations and the content… the prompt became generic and forgot the research"); Lemon cake ("Horrible illustration… look up a homemade lemon cake so you understand").

| # | Rule |
| --- | --- |
| 2.1 | **Each image shows a concrete state of the story** (what happened, who, where to), not a loose object. Before and after are two images. |
| 2.2 | **The prompt inherits the research:** it carries the narration sentence, the object with its real parts and the single copper-orange accent ([[Prompt - per-scene generation guide]]). |
| 2.3 | **Real-object sheet and reference photo before writing prompts.** "Baking dish" generates a bread tin; the real photo, cropped and in the orientation of the result, fixes the shape. A single `input_image`; license and attribution in the Status note. |
| 2.4 | **One large focal point;** the rest barely hinted. |
| 2.5 | **No text, figures or faces inside the image** (they are added in editing). Prompts **in the positive**. |
| 2.6 | **Counts and parts are checked by eye** (3 chairs instead of 4). Simple shot; name parts and quantities. |
| 2.7 | **An "almost right" image is accepted.** What can be fixed in editing is not regenerated. One retry per image; if it fails twice, accept it, reframe it or drop the shot. |
| 2.8 | **Vertical 9:16, safe zone:** subject between 15 % and 60 % of the height; nothing key in the bottom third or the top 6 %. |
| 2.9 | **The result has to be worth watching:** if the images are not understood without the voice, they are not ready. |
| 2.10 | **Check the reference for text and brands** before using it: a photo with a legible brand ("PRADO BRAZIL" on a padlock) leaks it into the image; the prompt asks for a blank, unmarked surface. |

## 3. Voice and sound

- **Voice: `elevenlabs/v3`, `Roger`, `language_code: en`, `speed` 0.95**, `previous_text` / `next_text` for intonation. "Elevenlabs is better." (`qwen3-tts` only as a cheap alternative, no speed control.) **I cannot hear the difference: the voice is the user's choice** at P5, and it is not changed afterwards. Details and alternative (`Bradford`): [[Channel voice]].
- **One take per scene, with the exact script text.** Sentences are never cut (see §4).
- **No sound effects by default.** `audiogen` sounds at 16 kHz and the user rejected the first one ("no blender sound"); ask for them only if the script requires it. Pending from Brazil's feedback: "the audio is fine, the quality could improve a lot and add dynamism" → try another sound model **only with approval**.
- `mmaudio` does not work with text only. `stable-audio-2.5` is out because of price.

## 4. Editing

- **A voice sentence is never cut.** In Blender, `frame_offset_start` also advances the visible start; the strip is created `ini` seconds earlier and an `assert` checks that the audible part starts and ends complete, with a 0.25 s tail (Brazil r1 error).
- **Silences:** 0.45 to 0.5 s between scenes; 1.2 s before the central question; 0.5 s of intro and 1.2 s of tail.
- **On-screen text:** sober label card (copper bar, spaced label, bold title), max. 4 words: [[On-screen text style]]. Between 22 % and 33 % from the bottom.
- **Plates:** one every ≈ 4 s, cross-fade within the scene and "page turn" between scenes; zoom 0.96 to 1.0, slow 6 % push. Plate changes should land on the word they explain (not yet synced to each word). With only 8 images in a 90 s Short (Chips) each plate stays ≈ 10 s: prefer 12 or more.
- **Say what was not verified:** the full video is not watched or heard, only frames and headers; gate P7 is the user's.
- **Before putting a symbol on screen** (→, ≈), check that the typeface has it: Noto Sans Display Bold has no "→" and it showed as a box (Stems, r1). Use "·" or "to".
- Details: [[Blender editing]], [[Transitions and effects]].

## 5. Process, costs and files

- **Master rule: no media is generated before P4** (prompts + budget approved, in dollars). Every approval is written in the video's Status. If the user **delegates** ("carry on until the render"), note it and run without stopping, but respect the cap.
- **Cost:** it worries the user ("it is getting expensive, too much testing"). Cap per category = base × 1.2; a minimal test at P5; series of ≤ 10 calls, **in series**, never in parallel; fix the prompt before retrying. Going over the cap needs approval.
- **The images that are generated are the ones in the cut**, 1 per shot by default.
- **Research goes separate from scripts** (models, styles, references): notes in `Research/`, tests in `Media/_canal/investigacion/`, cost accounted separately. A video note only links the conclusion.
- **Do not move other videos' folders.** Files carry their video's prefix (Obsidian resolves embeds by name). Discards go to `_descartes/`.
- **Notes in the vault, never artifacts or Claude Docs.**
- **No thumbnail on Shorts.** Description with sources, cut-off date and AI disclosure, in English.

## 6. Open items

- [ ] **Sound quality and dynamism** (Brazil feedback): no proven solution.
- [ ] **Plate changes synced to the word**, not only to the scene.
- [ ] Try the text style on a political topic (figure + source) and define 16:9.
- [ ] Confirm the `flux-kontext-pro` price on Replicate (≈ $0.04 from memory); test `match_input_image` and a scene with no object ([[Visual style - plasticine miniatures]]).
- [ ] **Measure the English pace and the English voice** with the first English script ([[Channel voice]]).
