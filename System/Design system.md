---
type: rules
created: 2026-10-27
updated: 2026-10-27
status: v1 · layout grid, components, motion verbs, 3D routes (Blender to HyperFrames); code in System/scripts/hfkit.py
tags: [rules, design, motion, hyperframes, blender]
---

# Design system: layout, components, motion

← [[Style]] (brand, persona, colour tokens) · [[Playbook]] §3 (what a visual must do) · [[Workflow]] (commands)

User (27 Oct 2026): *"build a design system for components and animation styles. combine all the techniques you used before … analyze the strong results. maybe you could use blender better, export it and uploaded it on hyperframes. and design a way to distribute elements on the viewport."* The system is code first: **`System/scripts/hfkit.py`** holds every token, zone, component and motion verb below, and a HyperFrames `hf/build.py` only places and times them (HyperFrames r2 dropped from 314 to 117 lines and rebuilt pixel for pixel, checked at 15 moments). Change a component here and in `hfkit.py` together; never fork it inside a video's builder.

## What the results say (27 Oct 2026)

Audience numbers cannot rank anything yet: 7 old-niche Shorts (5 to 6 Oct 2026) with 0 to 172 views at ≤ 9 h, counts only, and no AI-niche video published. So the evidence is the user's verdict on each render (git history of the Status notes); every rule below is [H] until [[Publish]] §Analytics loop has 10 videos.

| Render | User verdict | What it keeps or bans |
| --- | --- | --- |
| HyperFrames r2 (27 Oct) | *"the rest is good"* (after the comment prompt and spacing fix) | **the reference:** illustrations on a column grid, real frames as proof, one deck element, cuts on the word, comment prompt |
| Look v1 (5 Oct) | *"good and appealing, keep improving"* | caption and card layout |
| RAG explained r1 | *"100% text"* | every step is a picture; text only labels it |
| Prompt injection r1 | *"no 3d movement on text element"* | text stays flat; depth belongs to objects |
| Prompt injection r2 | *"Content overlaps"* | `check3d.mjs` before every render |
| Free or paid r2 | *"Horrible, unnecesary 3d models … go simpler"* | 3D is the exception |
| Chatbot vs agent r1 | *"Timing is a little too fast … position of the elements is not quite right"* | the grid below; room between phrases |
| Look v1 (23 Oct) | *"color, background and line style feel too generic"* | look v2 tokens ([[Style]]) |
| Prompt injection r3 | *"solution could be more colorful and meaingful"* | the solution flood and mint hero |

The common thread of the approved work: **one picture per spoken noun, entering on its word, on a fixed grid, with a real thing (frame, screenshot, photo) as proof**. The rejected work typeset ideas, decorated with 3D, or placed by eye.

## Layout: zones and grid

The frame is 1080 × 1920. Zones (`hfkit` names):

| Zone | Area (px) | Holds |
| --- | --- | --- |
| Title bar | y < 192 | nothing (platform) |
| **STAGE** | x 56 to 950, y 192 to 860 | pictures: illustrations, frames, devices, 3D |
| **BAND** | y 880 to 1040 | captions only (top layer, 50 % of the height) |
| **DECK** | x 56 to 950, y 1080 to 1420 | one card or the comment prompt, never both at once |
| Interface | y > 1440, x > 950 | nothing (platform buttons and title) |

Content is centred on x 503 (the middle of 56 to 950), not on the frame's 540: the right strip belongs to the buttons.

- **Columns:** `colx(k, n)` is the centre of column k of n across the stage (n = 2: 280, 727; n = 3: 205, 503, 801). Everything in a row sits on one column set.
- **Rows:** `ROW1` (top 220) and `ROW2` (top 560); a figure on ROW2 ends above the band. `rowy(k, n)` divides the stage evenly when a row is not a picture row.
- **Figure:** `fig(id, emoji, k, n, y, label=…)` is the unit: an illustration of size `sz(n)` (n = 1, 2: 280; 3: 215; 4: 161) centred on its column with its label 14 px under it (`id-l`).
- **Density:** at most one row of figures and one deck element at once, plus the captions; one dominant element per moment (the newest word's picture). A world holds up to six pictures over its life, never more than four at the same time [H].
- **Fill:** the stage is never three-quarters empty for over 3 s (`WARN SPARSE`).

**Arrangements** (choose one per world; the voice's sentence decides):

| Arrangement | When the sentence… | Placement |
| --- | --- | --- |
| hero | names one thing | one `fig` n = 1 (280 px) on ROW1, or a phone or code panel filling the stage |
| sequence | lists steps or parts | `fig` k = 0, 1, 2 of 3 on ROW2, popping in order |
| pair | turns A into B | `fig` columns 0 and 2 of 3 plus an `arrow` on column 1 |
| device + parts | shows an interface and what is in it | `phone` at x 90 (370 × 660) and figures on column 2 of 3 |
| board | compares | two rows of frames or figures on the same columns ([[Playbook]] §3 *Comparisons live on one board*) |
| strip | shows time passing | `strip` of real frames sliding (`slide`) |

## Components (`hfkit.py`)

| Component | Function | Spec | Enters with |
| --- | --- | --- | --- |
| Caption | `Short(keys=…)` (`captions.py`) | phrase of 1 to 3 words, ≤ 16 characters, centred at 50 % of the height, 88 px bold capitals, white with dark outline; spoken word lit, the others 45 %; `keys` colours up to 6 key words | its word |
| Illustration | `art`, `fig` | Fluent Emoji 3D ([[Style]] Illustrations), ≤ 280 px, soft shadow; the concept picture is fixed per idea ([[Audience]] *Plain-words map*) | `grow` |
| Label | `lbl` | 46 px heavy, centred, one line (`nowrap`), cream or one semantic colour | `pop` 0.1 s after its picture |
| Real frame | `frame` | 9:16 screenshot or video still, 14 px corners, slate border | `pop` |
| Device | `phone`, `code` | phone 370 × 660 around a real screen; code panel 870 wide, JetBrains Mono 42 px, strings mint, numbers ember | `settle` (hook) or `pop` |
| Counter | `counter` | 76 px word and a 96 px ember number | `count` |
| Arrow | `arrow` | slate word on an 8 px rule: the step between two pictures | `pop` |
| Strike | `strike` | 16 px `rose2` bar at −30° across a picture | `strike` on the word that negates |
| Flash | `flash` | white radial light over the stage | `flash` on the shot |
| Strip | `strip` | dark film strip holding real frames | `pop`, then `slide` |
| Context card | `card` | 894 × 280 in the DECK (top 1127), paper 94 %, 8 px ember bar; label 32 px spaced capitals, title 56 px, detail 34 px; `good=True` is the solution's mint card | `pop` |
| Number card | `card` with the figure as title | same box; one number with its source | `pop` |
| Comment prompt | `ask` | the closing question as a reply box (DECK top 1110, `ink2` 94 %, 4 px `mint2` border, 40 px corners): balloon 96 px and question 56 px (≤ 26 characters), two or three answer chips 40 px (≤ 14 characters, `signal2` outline), "reply in the comments" 40 px slate | `rise` on the question; `chips` on "Tell me" |
| Solution flood | `write(flood=n)` | mint and signal light pools fade in over 0.6 s from scene n ([[Style]] Solution scenes) | automatic |
| 3D model | `model3d` | a Blender scene as glb, played by three.js on the page clock | world window |
| 3D plate | `plate3d` | an EEVEE render with alpha (webm) under the text | world window |

**Layers, bottom to top:** ground and flood, 3D plate, 3D canvas, worlds (pictures, labels, cards), captions. Cards and labels never cover captions (user, 5 Oct 2026).

## Motion vocabulary

Every motion is a verb on `Short`; each fires on a word with `v.cue(scene, "word")`. No idle wobble, no shakes, no zoom punches.

| Verb | Motion | Use |
| --- | --- | --- |
| `grow` | scale 0.4 → 1, turn −12° → 0°, 0.5 s `back.out(1.9)` | a picture arrives on its noun |
| `pop` | rise 24 px and fade, 0.35 s `expo.out`; `spring=True`: 0.5 s `back.out(1.7)` (solution scenes) | labels, frames, cards, panels |
| `hide` | fade 0.2 s `power2.in` | clear room 0.25 s before the next picture lands |
| `rise` | rise 60 px, 0.45 s `expo.out` | panels from the deck (comment prompt) |
| `chips` | scale 0.6 → 1, 0.35 s `back.out(2)`, 0.18 s apart | answer chips, list items |
| `count` | number counts to its value, 0.9 s `power1.in` | a number that builds |
| `light` | text recolours in 0.3 s | the word that names a part |
| `nudge` | 20° turn and back, 0.6 s | a picture reacting to its verb ("moves") |
| `flash` | white light 0.9 → 0 in 0.35 s | a capture, a shot |
| `strike` | bar draws from the left in 0.3 s | "no", "without", "wrong" |
| `settle` | 1.06 → 1 over 1.2 s | frame 1: the hook picture is never static |
| `slide` | linear move | strips, time passing |
| world cut | out: blur 8 px and fade 0.2 s; in: blur and fade 0.25 s | automatic, 0.2 s before the scene's first word |

**Timing laws:** a picture lands on the first syllable of its word; its label follows 0.1 s later; items in a list are 0.1 to 0.18 s apart; anything replaced leaves 0.25 s before its successor arrives; an event every 2 to 3 s, nothing unchanged over 3.5 s ([[Playbook]] §3).

## 3D: three routes into HyperFrames

3D only where depth explains ([[Style]] 3D plates); text is never 3D. Pick the cheapest route that shows the point:

| Route | How | Gives | Costs |
| --- | --- | --- | --- |
| three.js primitives | a module in the page (as in [[Prompt injection - Status]]) | full control, labels pinned to projected boxes | hand-written JS per scene |
| **Blender glb → `model3d`** | `hfkit.blender3d(spec, "assets/x.glb", dur, "glb")`, then `v.model3d("assets/x.glb", t0, dur)` | `scene3d.py` vocabulary (net, cloud, link, surface, tokens) with its bevels, colours, show pops and camera path; seeks exactly; boxes reach `check3d.mjs` | about 2 s to export; three.js light (no bloom); emission keys (`pulse`, `fire`) are not exported |
| **Blender webm → `plate3d`** | `hfkit.blender3d(spec, "assets/x.webm", dur, "webm")`, then `v.plate3d("p", "assets/x.webm", t0, dur)` | the full EEVEE look (bloom, depth of field, glow pulses) with alpha over the page ground | about 0.85 s a frame at half size (82 s for 4 s), more at full size; invisible to the overlap check (frame its camera inside the STAGE by spec) |

Spec cues for `blender3d` are seconds from the 3D clip's start (or pass `cue=` a resolver). Blender trims each object's action to its own keys; `model3d` clamps every clip at its first and last key instead of looping (fixed 27 Oct 2026, the cause of nodes vanishing mid-shot). Frame the subject inside the STAGE with the spec's camera and look at a snapshot before building on it.

## Build and check

1. `hf/build.py`: `v = K.Short(__file__, keys=…)`; a dict of worlds `W["w1"] … W["wN"]` built from components; verbs on cues; `v.write(W, rev=n, flood=<solution scene>)` writes `index.html`, `render/_fx/sound_sfx.wav` and `render/_timeline.json`.
2. `node System/scripts/check3d.mjs hf/index.html` (serves the folder over local HTTP, so glb pages load): `OVERLAPS 0`, every WARN fixed or explained in Status.
3. `npx hyperframes snapshot` at the cue moments, look at the sheet, then render and mix ([[Workflow]]).
