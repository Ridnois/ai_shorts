---
type: research
created: 2026-10-03
updated: 2026-10-03
status: v3 · English voice chosen by Claude, pending the user's ear at P5
tags: [research, youtube, voice, replicate]
---

# Channel voice

← [[YouTube Channel]] · [[Guidelines for new scripts]] · [[Narration guide]]

## Current (English, from 3 Oct 2026)

- **Model:** `elevenlabs/v3`, voice **`Roger`**, `language_code: en`, `speed` 0.95, with `previous_text` and `next_text` for intonation. ≈ $0.10 per 1,000 characters.
- **Why this model:** the user chose it over `minimax/speech-2.8-turbo` and `qwen3-tts` ("Elevenlabs is better", lemon-cake Short); English is its strongest language, and it keeps the same API, parameters and price already used in the pipeline.
- **Why `Roger`:** it is the voice the user already approved in Spanish (continuity of timbre across the channel), and it is a native English voice: ElevenLabs describes it as a relaxed, resonant male voice, which suits calm explanatory narration. The wrapper on Replicate offers 26 voices (Rachel, Drew, Clyde, Paul, Aria, Domi, Dave, Roger, Fin, Sarah, James, Jane, Juniper, Arabella, Hope, Bradford, Reginald, Gaming, Austin, Kuon, Blondie, Priyanka, Alexandra, Monika, Mark, Grimblewood).
- **Alternative to test at P5 if `Roger` does not convince:** `Bradford` (articulate British storyteller). The test is one scene (≈ $0.01 per voice). **I cannot hear the difference: the user decides, and the voice is not changed afterwards.**
- **Pace (to be measured):** English is planned at ≈ 150 words per minute with pauses, the same as Spanish was; **measure with the first English script** (one full-script sample, not one sentence) and correct this figure.
- **One take per scene** with the exact script text. **Sentences are never cut** (see [[Guidelines for new scripts]] §4).
- **Acronyms and numbers:** write them as they are spoken if the model reads them badly (for example "ASML" → "A S M L"), and note the change.

## History

| Video | Voice | Pace | Result |
| --- | --- | --- | --- |
| Magnets (38 s) | `qwen3-tts`, man of almost 90, deep and calm | ≈ 118 words per minute | **Too slow** (user feedback) |
| Helium (70 s) | `qwen3-tts`, profile B: younger and brisker | 156 words per minute over the whole script | Approved |
| Brazil (60 s) | `qwen3-tts` cloned from Helium | 99 to 156 per scene | Uneven pace; the script was adapted |
| Lemon cake (80 s, Spanish) | `elevenlabs/v3`, `Roger`, `es` | ≈ 150 | "Elevenlabs is better" |
| Bike stems (63 s, Spanish) | `elevenlabs/v3`, `Roger`, `es` | ≈ 150 | See [[Bike stems - Status]] |
| Chips and lithography (≈ 93 s, Spanish) | `elevenlabs/v3`, `Roger`, `es` | ≈ 144 | See [[Chips and lithography - Status]] |

## Open

- Timbre and naturalness are for the user to judge alone: the audio is not heard during production.
- The English voice has not been tested yet; the first English video will be the test (P5).
