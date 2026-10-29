---
type: rules
created: 2026-10-27
updated: 2026-10-28
status: v2 · 27 Oct 2026: look tokens moved in from Style; camera on a canvas, transitions with a cause, type scale, vendored fonts and libraries, grain, the sound kit, captions in the low band; code in System/scripts/hfkit.py
tags: [rules, design, motion, hyperframes]
---

# Design system: look, layout, camera, motion, sound

← [[Playbook]] §3 (what a visual must do) · [[Style]] (brand, persona, words) · [[Workflow]] (commands)

The system is code first: **`System/scripts/hfkit.py`** holds every token, zone, component, verb and sound below, and a video's `hf/build.py` only places and times them. Change a rule here and in `hfkit.py` together; never fork it inside a video's builder. The HyperFrames skills in `.claude/skills/` (`hyperframes`, `hyperframes-cli`, `hyperframes-registry`, `media-use`) are the craft reference: read `hyperframes/references/motion.md` and `types/explainer.md` before a new kind of scene, and search the registry (`npx hyperframes catalog --tag <camera|transition|caption-style>`) before hand-writing an effect.

## What the renders taught (user verdicts, 5 to 27 Oct 2026)

One picture per spoken noun, entering on its word, on a grid, with a real thing as proof, was approved; ideas typeset as text, decorative 3D, emoji art and elements placed by eye were rejected. The r5 contact sheet of *How RAG works* (27 Oct) still read as slides: a small figure in the top third, an empty lower half, the same figure on most tiles and the same blur crossfade at every cut. v2 answers each: the camera, transitions with a cause, bigger subjects, captions low.

## Look

| Token | Value |
| --- | --- |
| **Ground** | `ink` `#0B0D17` with three radial pools (ember low left 16 %, signal high right 15 %, ink2 centre), a vignette and a fixed grain overlay (7 %, against banding; no full-screen linear gradient: it bands under H.264) |
| **Semantic colours** (one meaning each, in every video) | **ember** `#E36927` / `ember2` `#FF9A5C`: the hero, the one thing being explained · **signal** `#418AD1` / `#8EC2F2`: data and inputs · **mint** `#00AE7B` / `#5FD6A8`: right, the fix · **rose** `#B83255` / `#E8708F`: wrong, error |
| Neutrals | `cream` `#F3EDE2` text · `slate` `#6B7590` structure · `haze` `#262D42` inactive |
| Colour rules | the hero is the only ember thing on screen; colour never decorates; three semantic colours on one frame at most; a new colour passes the dataviz validator first ([[Workflow]] §Commands) |
| **Solution scenes** | from the fix to the close: the mint and signal flood (`flood=n`), mint becomes the hero, entrances may spring; the picture shows *why* the fix works, never only a green end state |
| **Lines** | `LINE` 4.4 px everywhere (under 4 px smears after YouTube's encode), rounded caps; dashed only for predicted or removed |
| **Type** (vendored in `vendor/fonts`, loaded by `@font-face`) | **Inter Display** 800 to 900 for display lines, numbers and titles · **Inter** 700 to 900 for labels and captions · **JetBrains Mono** for anything a model reads or writes. Scale `T`: 40 · 56 · 80 · 120 · 180 px; nothing read under 40 px; display tracking −0.025 em |

## Layout: zones (1080 × 1920)

| Zone | Area (px) | Holds |
| --- | --- | --- |
| Title bar | y < 180 | nothing (platform) |
| **STAGE** | x 56 to 950, y 180 to 860 | pictures; extends to y 1150 (**FULL**) when the deck is empty |
| **DECK** | x 56 to 950, y 880 to 1150 | one card or the comment prompt |
| **BAND** | y 1180 to 1320 | captions only; worlds are clipped at y 1170, so a close-up never paints over them |
| Interface | y > 1440, x > 950 | nothing (platform buttons, title) |

**One hero per beat** (user, 28 Oct 2026): one element at a time fills about 80 % of the frame width (`HERO` x 73 to 933, y 330 to 1150, `hero(w, h)` centres it), and the next beat's hero replaces it; at most one support line under it or one deck element, never small things in corners. Content centres on x 503, not 540: the right strip belongs to the buttons. **While the pipeline rail shows (y 196 to 296), world content starts below y 310.** `colx(k, n)` gives column centres (n = 3: 205, 503, 801); `ROW1` 220 and `ROW2` 560 are picture rows. A Hairline host draws in about 60 % of its 5:4 box: a 900 to 1000 px host spans the stage; bigger hosts may overhang the edges. **Density:** one dominant element per moment; a world shows at most the rail, one figure, two callouts or one tag, one deck element, captions.

## Camera and transitions

- **Every world is a canvas** behind a camera (`#wN-cam`). `v.cam(w, t, cx, cy, z, d)` zooms z times about canvas point (cx, cy) (or moves it to `to=`), easing `power2.inOut`; `v.focus(w, t, (x, y, w, h), fill)` frames a box; `v.wide(w, t)` returns. A move of 0.5 s or less is heard (a whoosh). Use the camera for scale changes: **wide** (the whole figure), **medium** (one part), **close** (the detail the voice names). Captions and the rail sit outside the camera. A close-up may crop text past the frame edges on purpose: `check3d.mjs` exempts content under a camera scale over 1.02 from the interface-zone check.
- **Transitions** (`v.write(..., trans={"w2": "whip"})`), each with a cause:

  | Kind | Built | Use when |
  | --- | --- | --- |
  | `cut` (default) | the new world lands 4 % large and settles in 0.5 s | a new step of the same idea |
  | `whip` | out 0.18 s left with 14 px blur, in 0.26 s from the right; whoosh | moving along a pipeline or to the next thing |
  | `push` | out scales 1.5 with blur, in from 0.86; whoosh | going inside something (zoom through) |
  | `dip` | the old world darkens 40 % for 0.1 s, then a cut | a turn: "but", the catch |
  | `blur` | blur swap 0.15 to 0.2 s | a quiet change on the same ground |

  3 to 5 kinds per video, at most a third hard cuts (`hfkit` warns). `write(blur=True)` turns on HyperFrames' render-time motion blur for fast movers.

## Components (`hfkit.py`)

| Component | Function | Spec |
| --- | --- | --- |
| Caption | automatic | phrase of 1 to 3 words, 84 px Inter Black capitals fitted to 860 px, white with a 4 px ink stroke and drop shadow, an explicit 0.28 em gap between words (a heavy stroke swallows plain spaces); the spoken word in ember (or its key colour) and 6 % larger, the others white at 55 %; each phrase rises 16 px in 0.15 s; band y 1186 |
| Display line | `big(id, text, x, y, w, size, hot=k)` | Inter Display Black, tracking −0.025 em, one hot word in ember; enters with `reveal` |
| Real frame | `frame(id, src, x, y, w, h)` | screenshot or still, 18 px corners, 4 px slate border, deep shadow |
| Terminal / code | `code(id, lines, x, y, w, title=)` | JetBrains Mono 40 px, a title bar ("terminal · real output"); `<s>` strings mint, `<b>` numbers ember, `<u>` prompt slate |
| Device | `phone` | 370 × 660 around a real screen |
| Counter | `counter` | label and an ember Inter Display number that counts |
| Hairline figure | `hairline(id, x, y, w)` + `v.hairline(id, fn)` | isometric line figure (MIT); acts only through `v.point` |
| Callout | `callout(id, text, ax, ay, lx, ly, col, side, w)` | dot on the part, leader, label 48 px; dot on the word, leader draws 0.4 s, label blurs in |
| Tag | `tag` | the query or name that travels between figures (46 px pill) |
| Pipeline rail | `v.rail(steps, t)`, `v.step(k, t, state)` | the mechanism's steps (mono 40 px) at the top of the stage: `on` ember, `done` cream, `bad` rose, `good` mint |
| Card | `card(id, label, title, detail, good=)` | DECK, ink2 94 %, 4.4 px cream line with an ember tick; label mono 32 px, title Inter Display 60 px, detail 40 px |
| Comment prompt | `ask(id, question, answers)` | DECK, mint border, question 58 px, 2 or 3 answer chips that pop with a sound |
| Arrow, strike, flash, strip | `arrow`, `strike`, `flash`, `strip` | the step between two pictures · a rose bar on "no" · a capture flash · real frames sliding |
| 3D | `model3d`, `plate3d` | below |
| Thumbnail | `v.thumb(inner)` | a still page in the video's look → `upload/thumb.jpg` ([[Workflow]] §Thumbnail) |

**Layers, bottom to top:** ground and flood, 3D plate, 3D canvas, worlds, rail, grain, captions. Cards and labels never cover captions.

## Motion verbs

Every verb fires on a word (`v.cue(scene, "word")`). Arrivals land on long tails; exits are 40 to 50 % shorter and accelerate; landed things hold still.

| Verb | Motion | Use |
| --- | --- | --- |
| `pop` | rise 24 px, 0.4 s `expo.out` (`spring=True`: `back.out(1.4)`, solution scenes) | labels, frames, cards, figures |
| `grow` | scale 0.6 → 1, 0.55 s `expo.out` | a picture arriving on its noun |
| `reveal` | a `big` line word by word: blur 6 → 0 px, 0.13 s each, 67 ms apart | display lines, numbers |
| `blurin` | a line blurs in, 8 → 0 px | callout labels, quiet text |
| `hide` | fade and 6 px blur, 0.2 s `power3.in` | clearing room 0.25 s before the next picture |
| `rise` | rise 60 px, 0.5 s | the comment prompt |
| `chips` | scale 0.7 → 1, 120 ms apart, a pop each | answer chips, list items |
| `count` | a number counts to its value, 0.9 s | a number that builds |
| `light`, `strike`, `flash`, `slide`, `nudge` | recolour · a bar draws · light flash · linear move · a 12° turn and back | a part named · "no" · a capture · time passing · a picture reacting |
| `pose` | moves an Anatomy figure's parameters (a part slides, a gas starts, a glow rises) | the verb of a physical step |
| `point` | moves a Hairline figure's pointer (optionally gliding) | the verb of a mechanism step |
| `cam`, `focus`, `wide` | the camera | scale change inside a world |

## Sound kit (`System/assets/sfx/`, credits in its `CREDITS.md`)

`whoosh-air`, `whoosh-swipe`, `whoosh-stick`, `whoosh` (rotated on whips, pushes and fast camera moves) · `click` (callouts, −32 dB) · `pop` (chips, −30 dB) · `impact-bass-2` (the opening hit and the payoff hit, aligned on its peak) · `riser` (the last 4 s crest on the payoff word) · `ping`, `key-press`, `typing` (on demand with `v.sfx(t, name, db)`). `v.payoff(t)` lays the riser and hit once per video. `hfkit` writes them into `render/_fx/sound_sfx.wav`; `mix_audio.py` keeps them at their designed level under the voice. New sounds: CC0 or Pixabay only, credited in `CREDITS.md`.

## Hairline figure library

Mount by name: `K.hairline("id", x, y, w)` in a world, `v.hairline("id", "<name>")`, then `v.point("id", t, vx, vy, glide=s)` (viewBox 400 × 320). The 33 packaged figures are listed in `vendor/hairline/README.upstream`; tile `point` positions over a 20-unit grid once to map one. Custom figures (made with `/hairline-create`) live in `vendor/hairline/custom/`.

| Figure | Concept ([[Audience]] *Plain-words map*) | Pointer | Key points (viewBox) | `value` |
| --- | --- | --- | --- | --- |
| `riffle` | passages, the library, a pick | a card stands up | y 120, x 140 to 320 | intensity |
| `terrain` | embedding, a map of meaning | pillars rise round it | (200, 165) centre | intensity |
| `drawer` | looking up, a skill opened on demand | height picks a drawer | (200, 60) top, (200, 250) bottom | intensity |
| `window` | context window | slides the frame along the tape | block 1 (87, 134) to block 16 (313, 247) | 4, 6, 9 |
| `balance` | RLHF, choosing the better answer | left raises A, right B | A (120, 150), B (330, 120) | 8, 14, 22 |
| `temperature` | sampling temperature | top hot, bottom cold | y 60 hot to 260 cold | 1.2, 2, 3 |
| `splitter` | tokens, word pieces | nearest seam splits | (141, 185), (211, 194), (244, 198) | 3, 6, 10 |
| `loop` | an agent's plan, act, check | picks a station | plan (220, 214), act (30, 94), check (305, 88) | 10, 16, 22 |

Hairline animates on its own clock; `hfkit` rewrites the vendored build so it follows the page's seek (deterministic frames), and a page mounts only the figures it holds.

## Anatomy figures

Made with the `anatomy` skill (`.claude/skills/anatomy`, MIT, installed with `npx skills add wheresryan22/anatomy -a claude-code`); each figure is a folder `System/anatomy/<name>/` with `build.mjs` (imports the skill's `kit/iso-kit.mjs`) that writes `<name>.svg` (the drawing), `<name>.json` (viewBox size, parameters), `<name>.css` (the kit's styles) and `<name>.pose.js` (`init` and `apply(svg, state, t)`: a pure map from parameters and the page clock to part transforms, helium dots and the like). `hfkit` places it: `K.anatomy(id, name, x, y, w)` in a world, `v.anatomy(id, name)` and `v.pose(id, t, {param: value}, d=0.6, ease)` on a word (moves of one figure never overlap). Frames are deterministic: no CSS animation, no `requestAnimationFrame`, positions come from the state and `t`. The look is mapped to the tokens in `.an.iso` (paper `ink2`, parts in slate and cream, **the one lit part and heat in ember**, gas and data in signal, line 2.2 px so it survives the encode); words stay out of the drawing apart from one engraved label, labels are `callout`s. A figure drawn once is reused only as the anchor of one video; a second video needs its own object (variety guard). Direction of draw: `azimuth 40`, `elevation 30`; a host of 860 to 940 px spans the stage (x 20 to 960, never cropped by the screen edge; in a world with a deck element or the comment prompt the host ends above y 870). Answer chips of the comment prompt total about 27 characters for three (`hfkit.ask` warns).

| Figure | Concept ([[Audience]] *Plain-words map*) | Parameters | Used in |
| --- | --- | --- | --- |
| `wafer-chuck` | a chip chamber: helium cools the wafer (compute, chips, supply) | `lift` 0 clamped, 0.3 raised on pins, 1 slid out · `plasma` 0 to 1 · `he` 0 to 1 (flow, gauge, rim, cooling) | *Helium and AI chips* |

## 3D routes

3D only where depth itself explains; text never moves in 3D. `hfkit.blender3d(spec, "assets/x.glb", dur, "glb")` then `v.model3d(...)` (three.js on the page clock, boxes reach `check3d.mjs`), or `"webm"` then `v.plate3d(...)` (full EEVEE look with alpha, invisible to the overlap check). Spec vocabulary: `scene3d.py` header. Frame the subject inside the STAGE and look at a snapshot before building on it.

## Build and check

1. `hf/build.py`: `v = K.Short(__file__, keys=…)`; worlds `W["w1"] … W["wN"]`; verbs on cues; `v.write(W, rev=n, trans=…, flood=…)` writes `index.html` (libraries and fonts copied into `hf/assets`), the effects stem and `render/_timeline.json`; `v.thumb(...)` writes the thumbnail.
2. `npx hyperframes check --json`: no errors. Accepted warnings: `nested_structure_needs_subcomposition` and `timeline_track_too_dense` (the vault does not edit in Studio). Read every `craft` warning.
3. `node System/scripts/check3d.mjs hf/index.html`: `OVERLAPS 0`; every `WARN SPARSE` or `WARN SMALL TEXT` fixed or explained in Status.
4. `npx hyperframes snapshot --at <cue moments>`: look at the contact sheet, then render and mix ([[Workflow]]).
