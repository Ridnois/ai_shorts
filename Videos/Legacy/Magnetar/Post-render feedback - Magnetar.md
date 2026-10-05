---
type: research
created: 2026-10-04
updated: 2026-10-04
status: feedback recorded verbatim · applied to the vault 4 Oct 2026
tags: [research, youtube, feedback, magnetar]
---

# Post-render feedback - Magnetar

← [[YouTube Channel]] · [[Magnetar - Status]] · [[Feedback loop]]

The construction of the video is ok, illustration are too creative and uncientific. blue empty background with added text is strange, illustrations could go there.

You could also add transcriptions to the video. word by word in video transctiption so users can follow the narrative with the audio off.

You could start with a prase to start curiosity, narrative oriented too much on storytelling, this could be something you need to know after 3 seconds.

The style of the added text is good and appealing, keep improving the render guidelines to improve style. and create top tier quality youtube shorts.

## Technical assesment

in addition of modifying the vault based on the post render feedback, i want you to research youtube monetization and requirements, and design a plan to create a solid, multi platform content chanel that is recognizable and solid. i want you to learn how to create a successful youtube shorts channel.

## Response (4 Oct 2026)

| Feedback | Layer | What changed where |
| --- | --- | --- |
| Illustrations too creative and unscientific | Illustrations | New rule 2.13 *Scientific fidelity beats creativity*: [[Guidelines for new scripts]] §2, [[Illustration pipeline]] §1.6, [[Prompt - per-scene generation guide]] (textbook schematic, "no glow, no light rays", element-by-element check). Applied in [[Superconductors - Status]] (four schematics, each checked) |
| Blue empty background with text is strange; illustrations could go there | Illustrations, builder | Rule 2.14 *No bare backdrops*: [[Guidelines for new scripts]], [[Illustration pipeline]] §1.7, [[On-screen text style]]; `build_video.py` now refuses blank placeholder plates |
| Add word-by-word transcriptions | Editing, tooling | `System/scripts/word_timings.py` (whisper word times), captions in `build_video.py` (`texts` in `plan.json`, one word at a time, copper figures, caption zone), [[Blender editing]], [[On-screen text style]], [[Shorts quality bar]] §3, [[Fast workflow]] (model and budget row) |
| Start with a need-to-know phrase, less storytelling | Idea, script | Rule 0.7: [[Guidelines for new scripts]] §0, [[Narration guide]] §2 and §3 (scene 1 ≤ 10 words, explain-don't-narrate, new example), [[Idea and hook quality]] §3, runner prompt in `youtube-pipeline/pipeline.py`, `CLAUDE.md` |
| Text style is good; keep improving the render guidelines; top-tier Shorts | Style, quality | [[On-screen text style]] keeps the style as is; new [[Shorts quality bar]] (first 3 s, rhythm, captions, checklist before P7) |
| Research monetization and requirements; plan a solid multi-platform channel | Strategy | New [[Channel strategy]]: YPP thresholds and the 15 July 2025 inauthentic-content policy (fetched from YouTube Help), disclosure rules, positioning, cadence, multi-platform plan, measurement loop, open decisions |
| (process) | Guards | `check_vault.py`: 16 new invariants plus a check that the builder keeps its guards; supersession rows in [[Feedback loop]]; index and `CLAUDE.md` updated; Replicate helper retries HTTP 429 |

**Not done:** [[Magnetar - Status]] was not reworked (flagged in its note). **Not verified:** early-access YPP tier, other platforms' rules and payouts, any earnings figure ([[Channel strategy]] §8); the craft rules in [[Shorts quality bar]] are hypotheses until Analytics exist; the agent cannot hear the voice or confirm the captions land on the spoken words.
