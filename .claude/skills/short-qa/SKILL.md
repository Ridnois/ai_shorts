---
name: short-qa
description: Audit a Next Token Short before the user sees it - lint, layout check, a frame audit of every beat, a slideshow-risk and quality score against the Format bar, sound numbers and the encode of the YouTube and TikTok masters. Use before calling any render ready, when the user reports a visual or quality fault, or when asked to review or score a video.
---

# /short-qa: catch it before the user does

The bar: `System/Format.md` §4. Commands: `System/Production.md` §Checks. Work in the video's `Media/…/<Topic>/hf/`. You cannot watch or hear the video: you read frames and numbers, and you say so.

## 1. Page checks (before render)

- `python3 System/scripts/beats.py "Media/…/<Video>"`: no `WARN` left unexplained (frame 0, transitions, callouts, card and chip fit).
- `HYPERFRAMES_NO_TELEMETRY=1 npx --yes hyperframes@0.8.209 check --json`: no errors.
- `node ../../../../../System/scripts/check3d.mjs index.html` (or the absolute path): `OVERLAPS 0`, no `CLIPPED`, `OVERFLOW`, `TEXT OVER PICTURE`.

## 2. Frame audit (every beat, not a sample)

`npx --yes hyperframes@0.8.209 snapshot . --at "$(cat ../render/_beats.txt)"` and read every contact sheet. On each frame ask:
- Is the hero 70 to 90 % of the width? Is any third of the frame empty for 2 s or more?
- Is text cropped, overlapping a picture, under 44 px, or in the right strip or the bottom interface zone?
- Does the frame show the verb the voice says at that moment?
A fault seen once is searched for on every frame; a fault class seen twice becomes a check (`hfkit` warning or `check3d`), per [[Feedback loop]].

## 3. Score (write it in Status; any 2 points in one row, or 5 or more in total, means rework before review)

| Risk (0 good, 1 some, 2 bad) | Look for |
| --- | --- |
| Frame 0 | no claim text or no picture at 0 s; unreadable at 170 px |
| Empty frame | a third of the frame empty for 2 s or more |
| Slideshow | the same layout on 4 tiles in a row; one shot size throughout |
| Text doing the picture's job | a card or line where a picture should act |
| No real thing | a named product never shown as itself |
| Static | nothing moves for over 3 s; fewer than one event per 2 s |
| Same as last video | the same main figure or composition as the previous Short |

## 4. Sound and encode (after render and mix)

- `python3 System/scripts/pace.py <render mp4>`: `PACE PASS` (no still picture over 3 s, none over 1.5 s in the first 3 s); each WARN or FAIL names its world: give that beat an event.
- `python3 System/scripts/listen.py <mixed mp4>`: `LISTEN PASS` (−14 LUFS ±1, true peak −1 dBTP or lower, no silence over 0.9 s, no clipping).
- `python3 System/scripts/master.py <mixed mp4>`, then `--probe` each master: YouTube `h264 2160x3840 … bt709/tv`, about 30 to 60 Mb/s; TikTok `1080x1920`, about 6 to 15 Mb/s.
- A full-frame contact sheet of the YouTube master at 1/2 s (`ffmpeg -i <yt.mp4> -vf "fps=1/2,scale=270:-1,tile=8x4" -frames:v 1 ../render/_sheet.jpg`): look for banding, blocky dark areas, soft text.

## Report

Five lines: checks passed or failed (with counts), the score table total and its worst row, `LISTEN` line, both `MASTER` lines, and what remains unverified (voice quality, effect levels, pace in motion).
