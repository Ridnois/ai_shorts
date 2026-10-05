---
type: research
created: 2026-10-03
updated: 2026-10-04
status: v4 · expressive variant to A/B test (Superconductors feedback, 4 Oct 2026); v3 English voice chosen by Claude, pending the user's ear at P5
tags: [research, youtube, voice, replicate]
---

# Channel voice

← [[YouTube Channel]] · [[Guidelines for new scripts]] · [[Narration guide]]

## Current (English, from 5 Oct 2026): Austin

- **Voice: `Austin`** (user, 5 Oct 2026: *"Austin it is"*, after testing Mark, Austin and Dave; Aria and Bradford rejected; the test is in [[Voice samples]]). Model `elevenlabs/v3`, `language_code: en`, with `previous_text` and `next_text` for intonation. ≈ $0.10 per 1,000 characters. **Replaces `Roger`.**
- **Speed:** the user set **`speed` 1.0 ("pace 1") for the first Austin video** ([[Battery and lithium - Status]]). In the test at 0.95 Austin ran ≈ 179 words per minute (estimated from file size, unmeasured), well above the 145 planned for Roger: **measure Austin on the first complete script** and write the planning pace here.
- **Why this model:** the user chose it over `minimax/speech-2.8-turbo` and `qwen3-tts` ("Elevenlabs is better", lemon-cake Short); English is its strongest language.
- **Why Austin:** brand fit. The channel is now **Redtail, science entertainment** ([[Brand options]]), and the user wanted a relaxed, conversational young American male voice in the register of Mark. I cannot hear it: the user chose by ear.
- **Previous voice (retired 5 Oct 2026): `Roger`**, relaxed resonant male voice, used for the first English videos (Helium, Twisted carbon, Magnetar, Superconductors, Moon, Asteroid mining); their Status notes still say Roger as a record.
- **Pace with Roger (measured on the first English video, 3 Oct 2026; Austin not yet measured):** 175 words in ≈ 72.9 s of voice (estimated from file sizes at 128 kbps) = **≈ 144 words per minute with pauses**; per scene it ran from 121 to 179. Plan with **≈ 145 words per minute** ([[Helium - why it cannot be made - Status]]).
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

| Battery and lithium (200 words, **English**) | `elevenlabs/v3`, **`Austin`**, `en`, 1.0 (user) | to measure | first Austin video ([[Battery and lithium - Status]]) |

## Open

- Timbre and naturalness are for the user to judge alone: the audio is not heard during production.
- The English voice was generated on 3 Oct 2026 and is **awaiting the user's judgement** (P7 of the first English video).
