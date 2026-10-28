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
| How RAG works r1 (27 Oct) | *"Way better, i think those icon-like illustrations can be removed, use hairlines. redesign the way info is showed on the screen"* | Hairline figures replace emoji; callouts, the pipeline rail and line panels (below) |
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

- **Columns:** `colx(k, n)` is the centre of column k of n across the stage (n = 2: 280, 726; n = 3: 205, 503, 801). Everything in a row sits on one column set.
- **Rows:** `ROW1` (top 220) and `ROW2` (top 560); a figure on ROW2 ends above the band. `rowy(k, n)` divides the stage evenly when a row is not a picture row.
- **Figure:** a Hairline host `hairline(id, x, y, w)` is the unit. The drawing fills about 60 % of its 5:4 box, so hosts are 780 to 900 wide and may overhang the STAGE edges; place them so the **drawing** spans 60 to 65 % of the width and ends above the band (riffle: `(53, 187, 900)` under the rail). `hlxy(x, y, w, vx, vy)` turns a viewBox point into page px for callout anchors; find a figure's parts by tiling it over a 20-unit grid once. (`fig` with Fluent Emoji is retired.)
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

## Information on screen (since 27 Oct 2026)

Four layers of text, each with one job, so nothing floats unexplained:

| Layer | Component | Job | Place |
| --- | --- | --- | --- |
| Where we are | **pipeline rail** `rail(steps)` via `v.rail(steps, t)`, `v.step(k, t, state)` | the mechanism's steps as nodes on a line (mono 40 px); `on` ember = the step on screen, `done` cream, `bad` rose = where it fails, `good` mint = where the fix acts. Shown from the hook's "here is how" to the end; one per video with a process | top of the STAGE, y 200 to 292, above the worlds |
| What this part is | **callout** `callout(id, text, ax, ay, lx, ly, col, side, w)` via `v.callout(id, t)` | a dot on the part, a hairline leader, the label on a rule (46 px heavy); the dot lands on the word, the leader draws in 0.35 s, the label follows; ≤ 2 at once; label in empty space, leader never across the drawing's middle | beside or under the figure, inside x 56 to 950 |
| What moves | **tag** `tag(id, text, x, y, col)` | the query or name that travels between figures (a line-drawn pill, 44 px) | moves in 2D only |
| What it means | **line panel** `card(...)` and the comment prompt | source, one claim, one detail: ink panel, 3.2 px cream line, ember tick, mono label | DECK |

Captions stay the voice's layer (band). A world shows at most: rail, one figure, two callouts or one tag, one panel, captions.

## Figure library (Hairline, reusable)

Every figure mounts by name: `K.hairline("id", x, y, w)` in a world, `v.hairline("id", "<name>")`, then `v.point("id", t, vx, vy, glide=s)`. Points are viewBox units (400 × 320) on the figure as drawn; a host's drawing fills about 60 % of the box. The **33 packaged figures** are listed in `vendor/hairline/README.upstream`; tile `point` positions over a 20-unit grid once to map one. **Custom figures** live in `System/scripts/vendor/hairline/custom/<name>.js` (made with `/hairline-create`, each passed its `look.mjs`); `hfkit` loads them on the skill's kernel (`vendor/hairline/kernel.js`) on the same page clock. `value=` sets a custom figure's own number (its `range`, the middle one by default).

| Figure | Concept ([[Audience]] *Plain-words map*) | The pointer | Key points (viewBox) | `value` (range) | First used |
| --- | --- | --- | --- | --- | --- |
| `riffle` (package) | passages, the library, a pick | a card stands up | y 120, x 140 to 320 pulls a card | intensity | [[How RAG works - Status]] |
| `terrain` (package) | embedding, a map of meaning | pillars rise round it | (200, 165) centre | intensity | [[How RAG works - Status]] |
| `drawer` (package) | looking up, a skill opened on demand | height picks a drawer | (200, 60) top, (200, 250) bottom | intensity | [[How RAG works - Status]] |
| `window` | context window, what the model reads | slides the frame along the tape | tape from block 1 (87, 134) to block 16 (313, 247); centre (192, 186) | frame length in blocks: 4, 6, 9 | [[How RAG works - Status]] r3 |
| `balance` | RLHF, people choosing the better answer | left of the post: A rises; right: B | A (120, 150), B (330, 120), level (200, 120) | tip in degrees: 8, 14, 22 | |
| `temperature` | sampling temperature, why answers vary | height: top hot, bottom cold | any x; y 60 hot to 260 cold | hottest temperature: 1.2, 2, 3 | |
| `splitter` | tokens, word pieces | nearest seam: a blade drops in, pieces part | seams (141, 185), (211, 194), (244, 198) | gap: 3, 6, 10 | |
| `loop` | an agent's loop: plan, act, check | picks a station; the carriage rides forward to it | plan (220, 214), act (30, 94), check (305, 88) | station lift: 10, 16, 22 | |

A new custom figure: `/hairline-create <idea>` writes `<name>.js`; move it into `custom/`, pass `look.mjs` there (Playwright's Chromium is installed in `~/.cache/ms-playwright`), then add its row here and its concept to the plain-words map. Never edit `kernel.js` or a packaged figure.

## Components (`hfkit.py`)

| Component | Function | Spec | Enters with |
| --- | --- | --- | --- |
| Caption | `Short(keys=…)` (`captions.py`) | phrase of 1 to 3 words, ≤ 16 characters, centred at 50 % of the height, 88 px bold capitals, white with dark outline; spoken word lit, the others 45 %; `keys` colours up to 6 key words | its word |
| Illustration (retired 27 Oct 2026) | `art`, `fig` | Fluent Emoji 3D, kept for old builders only; new videos use Hairline figures | `grow` |
| Label | `lbl` | 46 px heavy, centred, one line (`nowrap`), cream or one semantic colour | `pop` 0.1 s after its picture |
| Real frame | `frame` | 9:16 screenshot or video still, 14 px corners, slate border | `pop` |
| Device | `phone`, `code` | phone 370 × 660 around a real screen; code panel 870 wide, JetBrains Mono 42 px, strings mint, numbers ember | `settle` (hook) or `pop` |
| Counter | `counter` | 76 px word and a 96 px ember number | `count` |
| Arrow | `arrow` | slate word on an 8 px rule: the step between two pictures | `pop` |
| Strike | `strike` | 16 px `rose2` bar at −30° across a picture | `strike` on the word that negates |
| Flash | `flash` | white radial light over the stage | `flash` on the shot |
| Strip | `strip` | dark film strip holding real frames | `pop`, then `slide` |
| Context card (line panel) | `card` | 894 × 280 in the DECK (top 1127), `ink2` 94 %, 3.2 px cream line, 120 px ember tick on the top edge; label JetBrains Mono 30 px ember, title 56 px cream, detail 34 px; `good=True`: mint line and tick | `pop` |
| Number card | `card` with the figure as title | same box; one number with its source | `pop` |
| Comment prompt | `ask` | the closing question as a reply box (DECK top 1110, `ink2` 94 %, 4 px `mint2` border, 40 px corners): line-drawn reply bubble 88 px and question 56 px (≤ 26 characters), two or three answer chips 40 px (≤ 14 characters, `signal2` outline), "reply in the comments" 40 px slate | `rise` on the question; `chips` on "Tell me" |
| Solution flood | `write(flood=n)` | mint and signal light pools fade in over 0.6 s from scene n ([[Style]] Solution scenes) | automatic |
| Hairline figure | `hairline(id, x, y, w)` + `v.hairline(id, fn)` | an isometric line figure from `vendor/hairline` (MIT, 0.5.1), 5:4 at `w` (800 wide = 640 tall fills the STAGE); colours from [[Style]] *Hairline figures*; it acts only through `point`; colours switch on the frame the pointer arrives (`hfkit` turns Hairline's real-time stroke fades off, 27 Oct 2026: they lagged behind the captured frames) | `pop`, then `point` |
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
| `point` | moves a Hairline figure's unseen pointer to a viewBox point (optionally gliding); the figure answers on its own springs (a card stands up, pillars rise, layers lift) | the verb of a mechanism step, on its word |
| world cut | out: blur 8 px and fade 0.2 s; in: blur and fade 0.25 s | automatic, 0.2 s before the scene's first word |

**Timing laws:** a picture lands on the first syllable of its word; its label follows 0.1 s later; items in a list are 0.1 to 0.18 s apart; anything replaced leaves 0.25 s before its successor arrives; an event every 1.5 to 2 s and one scale change per world, nothing unchanged over 3.5 s ([[Playbook]] §3).

**Hairline under the hood:** Hairline animates on `performance.now`, rAF, timers and an IntersectionObserver, which HyperFrames does not seek. `Short._hairline()` copies the vendored build into `hf/assets/hairline.js` with those calls rewritten to `__HL`, a clock moved only by the page's seek (`window.__seek`, shared with three.js); a backward seek remounts and replays from 0, so every frame is the same on every render (first used on [[How RAG works - Status]]).

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
