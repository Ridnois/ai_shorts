---
type: research
created: 2026-10-03
updated: 2026-10-04
status: v4 · expressive variant to A/B test (Superconductors feedback, 4 Oct 2026); v3 English voice chosen by Claude, pending the user's ear at P5
tags: [research, youtube, voice, replicate]
---

# Channel voice

← [[YouTube Channel]] · [[Guidelines for new scripts]] · [[Narration guide]]

## Current (English, from 3 Oct 2026)

- **Model:** `elevenlabs/v3`, voice **`Roger`**, `language_code: en`, `speed` 0.95, with `previous_text` and `next_text` for intonation. ≈ $0.10 per 1,000 characters.
- **Why this model:** the user chose it over `minimax/speech-2.8-turbo` and `qwen3-tts` ("Elevenlabs is better", lemon-cake Short); English is its strongest language, and it keeps the same API, parameters and price already used in the pipeline.
- **Why `Roger`:** it is the voice the user already approved in Spanish (continuity of timbre across the channel), and it is a native English voice: ElevenLabs describes it as a relaxed, resonant male voice, which suits calm explanatory narration. The wrapper on Replicate offers 26 voices (Rachel, Drew, Clyde, Paul, Aria, Domi, Dave, Roger, Fin, Sarah, James, Jane, Juniper, Arabella, Hope, Bradford, Reginald, Gaming, Austin, Kuon, Blondie, Priyanka, Alexandra, Monika, Mark, Grimblewood).
- **Alternative to test at P5 if `Roger` does not convince:** `Bradford` (articulate British storyteller). The test is one scene (≈ $0.01 per voice). **I cannot hear the difference: the user decides, and the voice is not changed afterwards.**
- **Pace (measured on the first English video, 3 Oct 2026):** 175 words in ≈ 72.9 s of voice (estimated from file sizes at 128 kbps) = **≈ 144 words per minute with pauses**; per scene it ran from 121 to 179. Plan with **≈ 145 words per minute** ([[Helium - why it cannot be made - Status]]).
- **Expressiveness (Superconductors feedback, 4 Oct 2026: voice 3 of 5, *"needs improvement, rhythm could be more controlled and passionate"*, and *"the pace could improve"*).** Hypotheses, **not heard by the agent**; the user's ear decides:
  1. **Controlled rhythm comes from the script:** sentences of 6 to 14 words with real full stops, a comma only where a breath belongs, a delivery note per scene (calm, rising, amused, grave) in the script table ([[Guidelines for new scripts]] §1.12). The ElevenLabs v3 `stability` default is 0.5.
  2. **Passion variant to test:** `stability` 0.35 and `style` 0.35 (both schema inputs of `elevenlabs/v3`, defaults 0.5 and 0), with one audio tag at the start of a scene where the delivery note asks for it (for example `[curious]` or `[serious]`; v3 reads bracketed tags as direction). Tags go in the voice prompt only, **never in the caption text** (`plan.json` `texts` stays plain).
  3. **P5 A/B test, ≈ $0.02:** scene 1 twice, default and passion variant; the user picks; the winner becomes the default parameters here and this bullet is updated. Until then the defaults above stand.
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
| Helium - why it cannot be made (≈ 76 s, **English**) | `elevenlabs/v3`, `Roger`, `en`, 0.95 | ≈ 144 | First English video; awaiting the user's ear at P7 ([[Helium - why it cannot be made - Status]]) |

## Open

- Timbre and naturalness are for the user to judge alone: the audio is not heard during production.
- The English voice was generated on 3 Oct 2026 and is **awaiting the user's judgement** (P7 of the first English video).
