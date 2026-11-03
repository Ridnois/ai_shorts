---
name: short
description: Make one Next Token YouTube Short / TikTok end to end in this vault - ask once, pick and test the idea, write the script, voice it, build it with HyperFrames + hfkit in the paper look, audit it, master it for YouTube and TikTok, build the publish pack, and stop for the user's verdict. Use whenever the user asks for a new video, a short, "make one about X", or names an idea note from Pipeline/Ideas.
---

# /short: one video, end to end

The rules live in the vault; this skill is the order of work. Read `CLAUDE.md`, `System/Strategy.md`, `System/Story.md`, `System/Picture.md` (whole) and `Analytics/Report.md` first, and `System/Build.md` before building.

## 0. Before anything

- If two or more renders wait for a verdict (Status notes in `review`), ask the user to ship, fix or drop them first.
- Check the last video's series and main picture (`YouTube Channel.md`): this one must differ.
- Read `Research/Radar.md` and `Research/Signals.md` (regenerate them if older than 7 days: `radar.py pull && radar.py report`, `signals.py`).

## 1. Ask once

One `AskUserQuestion` round (1 to 4 questions, your recommendation first, as options):
- **Angle and series:** 2 or 3 concrete claims, each with its real thing, its hook pattern and its radar evidence.
- **Medium of the mechanism** ([[Picture]] §Medium): primitive, figure, capture, Manim, with the one real run or model output.
- Anything truly unclear (the length is fixed at 45 to 60 s).

Write the answers verbatim as the first line of the Status note.

## 2. Idea, script and pre-flight (no spend)

- Run the `/short-idea` tests and score only as far as needed ([[Strategy]] §The idea passes).
- Write the script with `/short-script`: the Script note `Videos/Week NN/<YYYY-MM-DD Day>/<Topic>/Script - <Topic>.md` holds the package, the voice table, sources with dates, the beat sheet (with its medium per beat, the spine and 2 moves borrowed from `Research/Shots/`), and the **pre-flight card** ([[Data]]) in Status.
- Create `Media/…/<Topic>/plan.json` (`prefix`, `texts` = one string per scene, `scenes`, `voice` rate 1.1).

## 3. Spend (cap $2.00, written in Status)

`voice.py --dry` → `voice.py` → `word_timings.py`. Check the take: the words match, no silence over 0.9 s. A generated still or clip ([[Build]] §Budget) only for a metaphor or establishing beat, its model id checked first; log every prediction id in Status at once.

## 4. Build

- `beats.py "Media/…/<Topic>" --new`, then turn the beat sheet into `hf/beats.json`: per world its `items` and `do`. ML primitives for mechanisms (`primitives-example.json`), `capture.py` for real pages, `manim.py` for exact maths, figures for machines. No hand-written `build.py`.
- Per beat: one hero at 70 to 90 % of the width; frame 0 on the end state; the spine returning; motion every 2 s, a new composition every 5 s, a scene change every 8 to 12 s ([[Picture]] §Pace); `v.payoff` once.
- Search `hyperframes-registry` before hand-writing an effect; read `.claude/skills/hyperframes/references/motion.md` before a new kind of scene.

## 5. Check, render, master

`qa.py "Media/…/<Topic>"` before the render; read the contact sheet once, every frame. Render (`--crf 14`, background), `mix_audio.py`, then `qa.py "Media/…/<Topic>" --render <mixed mp4>` (pace, sound, both masters). Thumbnail: `v.thumb(...)`. Publish pack: `upload/publish.json` with `series`, `hook_pattern`, `medium`, then `publish.py --dry-run` (`/short-publish` §1).

## 6. Stop for review

Set the idea note to `review`, update Status and the `YouTube Channel.md` row, run `check_vault.py`. Report in 10 lines or fewer: the render and masters (paths, duration), the `qa.py` table result, the pre-flight prediction, the pack path, the spend, and **what you could not check** (sound, whether the motion means something). Ask: ship, fix or drop.
