---
name: short-qa
description: Audit a Next Token Short before the user sees it - one qa.py run (kit, build warnings, lint, layout, frames, pace and composition, sound, both masters), one read of every frame, and a slideshow-risk score against the Picture bar. Use before calling any render ready, when the user reports a visual or quality fault, or when asked to review or score a video.
---

# /short-qa: catch it before the user does

The bar: `System/Picture.md` §Bar and §Pace. The command: `System/Build.md` §Checks. You cannot watch or hear the video: you read frames and numbers, and you say so.

## 1. Run the checks

- Before the render: `python3 System/scripts/qa.py "Media/…/<Video>"`.
- After the mix: `python3 System/scripts/qa.py "Media/…/<Video>" --render <mixed mp4>`.
- Every FAIL is fixed; every WARN is fixed or explained in one line in Status.

## 2. Read the frames once

Read the contact sheet `qa.py` names (every event and 0.45 s after it). On each frame, first describe it in one sentence (what is on screen, what is the hero), then ask:
- Is the hero 70 to 90 % of the width? Is any third of the frame empty for 2 s or more?
- Is text cropped, overlapping a picture, under 44 px, or in the right strip or the bottom interface zone?
- Does the frame show the verb the voice says at that moment? Is frame 0 the end state?
- Does the spine return, and is the current part marked?
- Mid-move frames: half-arrived words, collisions, a ghost of the last world.
- Mute test: read the sheet alone, top to bottom; does it tell the story without the voice?

A fault seen once is searched for on every frame; a fault class seen twice becomes a check, per [[Data]] §Feedback loop.

## 3. Score (write it in Status; any 2 in one row, or 5 or more in total, means rework before review)

| Risk (0 good, 1 some, 2 bad) | Look for |
| --- | --- |
| Frame 0 | no claim text or no picture at 0 s; not the end state or the event; unreadable at 170 px |
| Empty frame | a third of the frame empty for 2 s or more |
| Slideshow | the same layout on 4 tiles in a row; one shot size throughout; no spine |
| Text doing the picture's job | a card or line where a picture should act |
| No real thing | a named product never shown as itself; no real run or model output |
| Static | `pace.py` FAIL, or a composition held over 5 s |
| Same as last video | the same main figure or composition as the previous Short |

## Report

Five lines: the `qa.py` table result (rows passed, each FAIL), the score total and its worst row, the `LISTEN` line, both `MASTER` lines, and what remains unverified (voice quality, effect levels, whether the motion means something).
