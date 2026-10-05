---
type: research
created: 2026-10-05
updated: 2026-10-05
status: decided, Austin (5 Oct 2026)
tags: [voice, redtail, replicate]
---

# Voice samples (new Redtail voice, 5 Oct 2026)

**Decided: Austin** (user, 5 Oct 2026: *"Austin it is"*), registered in [[Channel voice]]. Mark and Dave are archived below as text; their audio is deleted.

User: *"I want to test a new voice for te channel, show three for me on the vault"*, then *"Lets test 2 more voices similar to mark, aria and bradford doesnt make it"*. Current voice: `elevenlabs/v3` Roger ([[Channel voice]]). Brand context: science entertainment, "Science at full speed" ([[Brand options]]), so the candidates lean energetic. **The agent cannot hear audio: the descriptions below are my recollection of ElevenLabs' voice descriptions, not a judgement. The user's ear decides.**

Same text for every voice (the first four sentences of the Moon Short, 247 characters, 45 words), same settings (`elevenlabs/v3`, `language_code: en`, `speed: 0.95`, default stability and style), one take each, no tags.

> Our newborn Moon was about twenty times closer. A Mars-sized world hit young Earth. The debris gathered into the Moon, right beside us. So close that it filled the sky, many times wider than the Moon you know, and it pulled the oceans much harder.

![[voice-austin.mp3]]

| Voice | Why it was picked (from memory of ElevenLabs' descriptions) | Length (estimate) | Words per minute (estimate) | Prediction |
| --- | --- | --- | --- | --- |
| **Mark** | relaxed, conversational young American man, the "social media" register (round 1) | ≈ 14 s | ≈ 190 | [p7vynrbf…](https://replicate.com/p/p7vynrbfw5rmr0d11khsm8g474) |
| **Austin** | another young American male, relaxed and good-natured (round 2, similar to Mark) | ≈ 15 s | ≈ 179 | [45h6wyex…](https://replicate.com/p/45h6wyexd5rmw0d11kjv53gn6w) |
| **Dave** | conversational young male, British accent, casual (round 2, similar to Mark) | ≈ 17 s | ≈ 159 | [vyns3bgg…](https://replicate.com/p/vyns3bggpxrmy0d11kk8a06n18) |

Lengths come from the file size at an assumed 128 kbps, as [[Channel voice]] does: unmeasured. The channel plans ≈ 145 words per minute, so Mark and Austin may need a lower `speed` than 0.95 if one wins.

Cost: round 1 ≈ $0.075, round 2 ≈ $0.05 (`elevenlabs/v3` ≈ $0.10 per 1,000 characters; Replicate's metrics report characters, not dollars). The pick is registered in [[Channel voice]] and the pipeline now uses Austin.

## Archive (rejected)

- **Aria** (expressive, husky young woman) and **Bradford** (articulate British storyteller): rejected by the user in round 1 (*"aria and bradford doesnt make it"*); audio files deleted, not recoverable (predictions `g2cnxwx5…`, `rr8867ys…` expire).
- **Mark** (relaxed young American male, ≈ 190 words per minute at 0.95) and **Dave** (casual young British male, ≈ 159): not chosen (round 1 and 2); audio deleted.
