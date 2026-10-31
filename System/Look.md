---
type: rules
updated: 2026-10-29
status: v1 · 29 Oct 2026: Next Token brand and the flat paper look. Replaces Design system and Style (dark navy, grain and gradients broke under YouTube's re-encode). Code: System/scripts/hfkit.py
---

# Look: brand, design system, motion, sound

What a picture must do: [[Format]] §4. Commands: [[Production]].

The system is code first: **`System/scripts/hfkit.py`** holds every token, zone, component, verb and sound below; a video's `hf/beats.json` only places and times them (`System/scripts/beats.py` reads it). Change a rule here and in `hfkit.py` together; never fork a component inside a video's builder.

## Brand

- **Next Token** (renamed 29 Oct 2026 from Inside the Model; the user claims the handle in Studio and TikTok). Line: "How AI works · Agents at work · What's coming". Kit: `System/Brand/Next Token/` (`brand.py` writes `nt-avatar.png`, `nt-banner.png`, `nt-mascot.png`).
- **Mascot, Tok:** a yellow token tile with a thick ink outline, two eyes and a cursor: the next token a model is about to say. It lives on the channel page, the banner and thumbnails, **not inside the video** (the look is the brand inside the video).
- **Persona:** an engineer who uses AI every day and explains it to a smart friend: precise, dry, calm, never hype or doom. Specific beats general ("Claude Opus 5.5, October 2026", not "AI").
- **Banned words** (voice, screen, description): did you know, game-changing, revolutionary, mind-blowing, insane, unlock, supercharge, journey, this changes everything, in this video, like and subscribe; exclamation marks.

## Look: flat paper

Why: flat colour and still texture compress cleanly; a bright frame stands out in a dark feed; thick ink survives the 1080p rung. **Never:** full-frame gradients, animated grain or noise, glows, thin lines, small text.

| Token | Value | Job |
| --- | --- | --- |
| `PAPER` | `#F4EFE4` with a still dot grid | the ground |
| `INK` | `#121212` | lines (6 px), text, hard shadows |
| `YELLOW` | `#FFD23F` | **the hero**: the one thing being explained, as a fill or a marker under ink text; never a text colour |
| `BLUE` | `#2C5BEA` (`BLUE2` `#D3DEFF`) | data, inputs, a figure's lit stroke |
| `RED` | `#D7392B` (`RED2`) | wrong, the error |
| `GREEN` | `#13965A` (`GREEN2`) | right, the fix; `flood=` turns the ground `GREEN2` from the fix on |
| `MUTED`, `PAPER2`, `WHITE` | `#6B665C`, `#E7E0D1`, `#FFFFFF` | secondary text · inactive · panels |

- Text takes only `INK`, `MUTED`, `BLUE`, `RED`, `GREEN` (`hfkit.TEXT_SAFE`); a "hot" word sits on a yellow marker.
- **Type:** Inter Display Black for display lines and numbers (tracking −0.03 em), Inter Black for captions and labels, JetBrains Mono for anything a model reads or writes. Scale `T`: 44 · 60 · 84 · 128 · 190 px; nothing read is under 44 px.
- **Panels** (cards, tags, the comment prompt, frames): white, 6 px ink border, a hard 12 to 14 px ink offset shadow. Terminal and code panels are the one dark block (`#171717`).
- Old names (`EMBER`, `SIGNAL`, `MINT`, `ROSE`, `CREAM`, `SLATE`) still resolve to their meaning in this look, so older builders run.

## Layout (1080 × 1920)

| Zone | Area (px) | Holds |
| --- | --- | --- |
| Top bar | y < 180 | nothing (platform) |
| **STAGE** | x 56 to 950, y 180 to 860 (to 1150 when the deck is empty) | pictures; `HERO` x 73 to 933, y 330 to 1150 is one hero filling about 80 % of the width |
| **DECK** | x 56 to 950, y 880 to 1150 | one card or the comment prompt |
| **BAND** | y 1180 to 1320 | captions only; worlds are clipped above it |
| Interface | y > 1440, x > 950 | nothing (title, buttons) |

- **One hero per beat**, centred on x 503 (the right strip belongs to the buttons); the next beat's hero replaces it.
- **Two layers:** pictures live in the camera; everything read on the glass (a claim, a number, a card, the prompt) goes through `K.screen(...)`, so a zoom never crops it. A callout (dot, leader, label) stays in the camera, shows only while the camera is still and for 0.8 s or more, its label in free space.
- **Captions:** 1 to 3 words, Inter Black capitals up to 96 px, ink on paper, the spoken word on a yellow marker and 6 % larger; in the band (`captions.py`).

## Camera and transitions

Every world is a canvas behind a camera: `v.cam`, `v.focus(w, t, box)`, `v.wide`. Scale changes happen through the camera (wide, medium, close), never a new slide. A move of 0.5 s or less is heard (a whoosh).

| Transition | Use when |
| --- | --- |
| `cut` (lands 4 % large and settles) | a new step of the same idea |
| `whip` | moving along a pipeline, to the next thing |
| `push` | going inside something |
| `dip` | a turn: "but", the catch |
| `blur` | a quiet change on the same ground |

3 to 5 kinds per video, at most a third hard cuts (`hfkit` warns). Keep full-frame motion short: fast whole-frame movement costs the most bits after upload.

## Components and verbs (`hfkit.py`)

| Component | Function |
| --- | --- |
| Display line | `big(id, text, x, y, w, size, hot=k)` with `v.reveal` |
| Real frame, phone | `frame(...)`, `phone(...)`: screenshots and recorded runs, ink border and hard shadow |
| Readable capture | a capture is read at Short speed on a phone: `sheet(id, rows, x, y)` holds real crops of two or three words each, every row 80 px tall or more (`hfkit` warns), so body type lands near 70 px; sheets go in `screen()`; a whole page or table appears only as a brief establishing shot under a big line (user, 30 Oct 2026: "make sure captures are readable on the short speed and format") |
| Terminal | `code(id, lines, x, y, w, title=)`: `<s>` strings, `<b>` numbers, `<u>` prompt |
| Counter | `counter` with `v.count` |
| Callout | `callout(id, text, ax, ay, lx, ly, col)` with `v.callout` |
| Tag, card, comment prompt | `tag`, `card(id, label, title, detail, good=)`, `ask(id, question, answers)` |
| Pipeline rail | `v.rail(steps, t)`, `v.step(k, t, "on"/"done"/"bad"/"good")` |
| Hairline figure | `hairline(id, x, y, w)` + `v.hairline(id, name)` + `v.point` |
| Anatomy figure | `anatomy(id, name, x, y, w)` + `v.anatomy(id, name)` + `v.pose` |
| 3D | `blender3d(spec, out, dur)` then `v.model3d` or `v.plate3d` (only where depth explains) |
| Thumbnail | `v.thumb(inner)` → `upload/thumb.jpg` |

Verbs fire on a heard word (`v.cue(scene, "word")`): `pop`, `grow`, `reveal`, `blurin`, `hide`, `rise`, `chips`, `count`, `light`, `strike`, `flash`, `slide`, `nudge`, `pose`, `point`, `cam`, `focus`, `wide`. Arrivals land on a long tail, exits are shorter, landed things hold still. Words stagger 60 to 120 ms.

## Figures

- **Hairline** (isometric line figures, MIT, light theme): `riffle` (cards, a pick), `terrain` (a map of meaning), `drawer` (look-up on demand), `window` (context window), `balance` (RLHF), `temperature` (sampling), `splitter` (tokens), `loop` (plan, act, check), `doubling` (pointer x = puzzle size: columns double with each switch; value 1 adds a slower claim row, shape only), `quantize` (pointer height = bits: pins snap to 16, 4 or 2-bit rails; 16-bit y 60, 4-bit y 165, 2-bit y 245); the 33 packaged ones are in `vendor/hairline/README.upstream`; new ones with `/hairline-create` into `vendor/hairline/custom/`.
- **Anatomy** (the `anatomy` skill, isometric machines of 40 to 80 parts): for a physical machine (a chip chamber, a cooling loop, a rack). Each lives in `System/anatomy/<name>/` with a pose contract (parameters in, part transforms out, no page clock of its own). The lit part fills yellow. Built so far: `wafer-chuck` (helium cools the wafer: `lift`, `plasma`, `he`), `gut-carrier` (a pill floods gut and body; carriers open only at the infection: `pill`, `spread`, `kill`, `resist`, `carrier`, `open`), `citator` (a citation card looked up in a drawer cabinet and stamped: `feed`, `search`, `found`, `ok`, `bad`), `ram-stick` (weights on a RAM module: 16-bit overflows, 4-bit fits: `load`, `bits`, `bad`, `ok`), `rater` (the thumbs-up tuner: rated reply cards tune a model's dial toward agreeing; a green clamp holds it at centre: `feed`, `up`, `down`, `tune`, `ok`, `bad`), `switchboard` (the k-SAT puzzle: eight toggle switches, three rule lamps: `s0`..`s7`, `more`, `r0`..`r2`), `compile-gate` (the compiler as an inspection gate: a press stamps a code block, a feeler checks it, green rides to the done tray, red is kicked to a return chute back to the press: `feed`, `check`, `ok`, `bad`, `count`, `part`), `context-reader` (the context window: message slips land in a tray, a reading head sweeps all of them each turn, a yellow memory note drops in first, middle slips fade: `msgs`, `scan`, `read`, `note`, `lit`, `mid`), `effort-meter` (the effort knob: LOW to MAX turns a pointer, thinking tokens stack in a cage, a printer pushes out the answer card green or red: `effort`, `think`, `out`, `ok`, `bad`). `hfkit.anatomy()` scopes a drawing's ids (clip paths) per mount, so one figure can appear in several worlds.
- A figure is the anchor of one video; the next video needs a different main picture.

## Sound kit (`System/assets/sfx/`, credits in its `CREDITS.md`)

`whoosh-air`, `whoosh-swipe`, `whoosh-stick`, `whoosh` (rotated on whips, pushes, fast moves) · `click` (callouts) · `pop` (chips) · `impact-bass-2` (opening and payoff hit) · `riser` (into the payoff) · `ping`, `key-press`, `typing` (on demand, `v.sfx`). `v.payoff(t)` once per video. New sounds: CC0 (Openverse) or the `media-use` skill, credited.
