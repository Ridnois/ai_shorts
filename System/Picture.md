---
type: rules
updated: 2026-11-03
status: v2 · 3 Nov 2026 vault rebuild. Owns what the viewer sees: the medium of each beat, the quality bar, the pace, motion, camera and sound use. Replaces Format §4–5 and the motion half of Look; built on how 3Blue1Brown, Kurzgesagt, Welch Labs, Two Minute Papers, Fireship and ByteByteGo make their pictures (research of 3 Nov 2026)
---

# Picture: what the viewer sees

The words it serves: [[Story]]. The components, tokens and commands: [[Build]]. Reference shots from other channels: [[Shots]].

## What the best channels do (research, 3 Nov 2026)

- **They own their primitives.** 3Blue1Brown animates every video with his own library (Manim), Kurzgesagt with a rigged library of drawn parts, Welch Labs with paper plus Manim. A new video is new arrangements of known pieces, so each piece can be polished once. Our pieces: `hfkit`'s components, the ML primitives, the Anatomy and Hairline figures ([[Build]] §Kit).
- **The proof is real.** Two Minute Papers shows the paper's own output; Fireship shows real code; ByteByteGo draws the real system. Our two best curves (Effort level and ETH, [[Data]] §Review) both showed a real output inside the mechanism.
- **Generated video is only metaphor.** Creators who use Veo, Kling or Hailuo use them for an establishing shot or a metaphor, never for the mechanism, and keep each shot short.
- Sources: 3blue1brown.com/faq; aperiodical.com (Welch Labs interview); the Kurzgesagt "How to make a Kurzgesagt video in 1200 hours" video; [[Channels]].

## Medium: each beat picks its medium by its job

| Beat job | Medium (`medium` in publish.json) | Tool |
| --- | --- | --- |
| an ML mechanism: tokens, next-token odds, attention, embeddings, layers, a matrix, an agent loop | **primitive** | `hfkit` ML primitives ([[Build]] §Kit) |
| a machine or a physical process (a chip, a rack, a cooling loop) | **figure** | Anatomy (`/anatomy`) or Hairline (`/hairline-create`) |
| a real product, a real run, a real model's output | **capture** | `capture.py` (scripted browser recording), a recorded terminal run, real page crops in `sheet` |
| exact math: a vector sum, a matrix product, a curve, a proof step | **manim** | `manim.py` (transparent clip in the paper palette) |
| metaphor, establishing shot, a real place or scale (a data-centre hall, a river) | **generated** | a still in our style, then image-to-video ([[Build]] §Budget); 1.5 to 3 s a shot, at most 3 a video |
| a named effect: a chart, kinetic type, a transition | registry block | `hyperframes-registry`: look it up before building one by hand |

- **Every video shows one real run or real model output** (a capture, a recorded run, a real attention map) inside the mechanism, not only as a page to cite.
- **The main medium** (the one with the most screen time) is written in Status and `publish.json` so [[Data]] can compare media.
- Open-source tools that may be recorded (licence checked at build time, credit in the description): Transformer Explainer (Polo Club, MIT), bbycroft LLM visualisation (MIT), TensorFlow Playground and the Embedding Projector (Apache-2.0). Jay Alammar's illustrations are non-commercial: redraw the idea, never reuse the image.

## Bar

| Rule | Test |
| --- | --- |
| **Frame 0 is the thumbnail** | the hook's picture and its claim text are on screen at 0 s, readable at 170 px wide |
| **Show the verb** | every beat: "the viewer sees ___ happen, so they understand ___"; a picture any other video could use is cut |
| **The subject fills the frame** | the hero spans 70 to 90 % of the width; no area over a third of the frame stays empty for 2 s |
| **Real over drawn** | a real product is shown as itself; a machine is drawn as a figure; never a fake UI (a `chat` primitive is labelled as a recreation of a real log) |
| **Source on screen, not in the voice** | the 4 to 7 s window ([[Story]] §Beats) shows the real page or a tag while the voice raises the stakes |
| **Three shot sizes** | wide, medium and close inside the same world, through the camera |
| **The point is spent, not spread** | each beat is marked 1 (connective: fast, small), 2 (supporting) or 3 (the point: larger, slower, its own sound); at most a quarter are 3 |
| **Act out one word** | the one word that carries the video does what it means, once ("split" splits) |
| **Mute test** | the picture alone, sound off, tells the same story as the voice |
| **No AI clichés** | no glowing brains, robots, circuit faces, binary rain, handshakes |
| **Varied from the last video** | a new main figure, primitive arrangement or capture; the inauthentic-content policy punishes interchangeable videos ([[Strategy]] §Policy) |

## Pace: three tiers (`pace.py` measures the first two)

| Tier | Every | What counts |
| --- | --- | --- |
| **Motion** | 2 s or less (1.5 s in the hook) | a part moves, a number counts, the camera pushes, a word lands; nothing holds still over 3 s |
| **Composition** | 5 s or less | the hero is replaced, or the shot size changes (wide to close) |
| **Scene** | 8 to 12 s | a new world on a re-hook ([[Story]] §Beats); this is where the transition kinds are spent |

These replace the single "event every 1.5 to 2 s" rule. Faster than about 1.2 s between changes reads as noise (third-party retention guides, direction only).

## Motion (measured)

From motionmaxxing (Tejas Makwana, Apache-2.0, read 31 Oct 2026): about 4,300 moves read frame by frame from 53 professional pieces. Durations are a floor, because a phone viewer also has to read.

- **Things arrive by moving:** the move runs 0.4 to 0.5 s; opacity is only a 0.15 s helper under it.
- **Down from oversize, never up from small:** a picture settles from 1.25x, a chip from 1.3x, a callout dot from 2.2x.
- **Land slows, leave speeds up:** `expo.out` in, `power3.in` out, exits shorter than entries.
- **One spring a video** (the payoff). **Early by two frames:** an event lands 0.05 s before its word. **Siblings overlap:** the gap is under half the move.

## Camera and transitions

Every world is a canvas behind a camera (wide, medium, close); scale changes happen through the camera, never a new slide. A move of 0.5 s or less is heard (a whoosh).

| Transition | Use when |
| --- | --- |
| `cut` (lands 4 % large and settles) | a new step of the same idea |
| `whip` | moving along a pipeline, to the next thing |
| `push` | going inside something |
| `dip` | a turn: "but", the catch |
| `blur` | a quiet change on the same ground |

3 to 5 kinds per video, at most a third hard cuts. Keep full-frame motion short: fast whole-frame movement costs the most bits after upload.

## Sound

One continuous voice take. Effects go only on a visible action that matters (a whoosh on a camera move, a click on a callout, a pop on a chip, one hit on the payoff): a sound on every event makes the few that count indistinguishable. Silence before the payoff hit. A quiet licensed music bed is allowed, ducked under the voice. Master at −14 LUFS, true peak −1 dBTP.

## Before each beat sheet

Read 2 notes in [[Shots]] whose pattern or medium matches this video, and write the one move borrowed from each in the beat sheet (a move, never a look).
