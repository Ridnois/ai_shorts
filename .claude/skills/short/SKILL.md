---
name: short
description: Make one Next Token YouTube Short / TikTok end to end in this vault - ask once, pick and test the idea, write the script, voice it, build it with HyperFrames + hfkit in the paper look, audit it, master it for YouTube and TikTok, build the publish pack, and stop for the user's verdict. Use whenever the user asks for a new video, a short, "make one about X", or names an idea note from Pipeline/Ideas.
---

# /short: one video, end to end

The rules live in the vault; this skill is the order of work. Read `CLAUDE.md`, `System/Format.md` (whole), `System/Production.md`, `Analytics/Report.md` first; `System/Look.md` before building; `System/Growth.md` §Package before the pack.

## 0. Before anything

- If two or more renders wait for a verdict (Status notes in `review`), ask the user to ship, fix or drop them first.
- Check the last video's series and main figure (`YouTube Channel.md`): this one must differ ([[Format]] §1, §4 *Varied*).

## 1. Ask once

One `AskUserQuestion` round (1 to 4 questions, your recommendation first, written as options, not open questions):
- **Angle and series** (2 to 3 concrete claims you would make, each with its real thing);
- **Visual medium** (recorded run, real captures, Anatomy figure, Hairline figure, mix);
- anything truly unclear (length is fixed: 45 to 60 s).
Write the answers verbatim as the first line of the Status note.

## 2. Idea and script (no spend)

- Run `/short-idea` logic only as far as needed: the 4 tests of [[Format]] §2, with demand evidence from `youtube_search.py` when the token works (say so when it does not).
- Write the script with `/short-script`: Script note `Videos/Week NN/<YYYY-MM-DD Day>/<Topic>/Script - <Topic>.md` with the package (title, 2 alternatives, frame-0 text, thumbnail idea), the voice text table, sources with dates, and the beat sheet.
- Create `Media/…/<Topic>/plan.json` (`prefix`, `texts` = one string per scene, `scenes`, `voice` rate 1.1).

## 3. Spend (cap $0.50 by default, written in Status)

`voice.py --dry` → `voice.py` → `word_timings.py`. Check the take: words match, no silence over 0.9 s. Log every prediction id in Status at once.

## 4. Build

- `python3 System/scripts/beats.py "Media/…/<Topic>" --new`, then turn the beat sheet into `hf/beats.json`: per world its `items` (hfkit components, `at` = x, y, w) and `do` (verbs cued on spoken words, e.g. `["reveal", "t2", "needs-0.1"]`). Format: `beats.py`'s docstring; example: `System/scripts/beats-example.json`. No hand-written `build.py`.
- Per beat: one hero filling 70 to 90 % of the width, an event every 1.5 to 2 s, the camera through wide/medium/close, 3 to 5 transition kinds, `first=` for the frame-0 hook, `v.payoff` once, `flood=` from the fix.
- Real things as themselves: screen recordings or captures in `frame`/`phone`; machines through `anatomy`; flat mechanisms through `hairline`. Read `.claude/skills/hyperframes/references/motion.md` before a new kind of scene; search `hyperframes-registry` before hand-writing an effect.
- `python3 System/scripts/beats.py "Media/…/<Topic>"` → fix every `WARN`.

## 5. Check, render, master

Run `/short-qa` steps 1 to 3 before the render (lint, `check3d`, frame audit); then render (`--crf 14`, background), `mix_audio.py`, `listen.py`, `pace.py`, `master.py`, and `/short-qa` step 4 on the mixed mp4. Thumbnail: `v.thumb(...)`. Publish pack: write `upload/publish.json` and run `publish.py --dry-run` (`/short-publish` §1).

## 6. Stop for review

Set the idea note to `review`, update Status and the `YouTube Channel.md` row, run `check_vault.py`. Report in 10 lines or fewer: the render and masters (paths, duration), the QA score, the pack path, the spend, and **what you could not check** (sound, pace in motion). Ask: ship, fix or drop.
