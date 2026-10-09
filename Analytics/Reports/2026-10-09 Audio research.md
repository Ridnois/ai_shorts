---
type: research
created: 2026-10-09
updated: 2026-10-09
status: v1 · evidence behind the audio redesign of 9 Oct 2026; rules live in [[Playbook]] §5 and [[Workflow]]; channel data has not tested them yet
tags: [research, audio, voice, music, loudness]
---

# Audio research · 9 Oct 2026

← [[Playbook]] §5 (the rules) · [[Workflow]] (tools, budget) · [[2026-10-09 Visual research]] · [[YouTube Channel]]

**Trigger** (user, 9 Oct 2026, on [[Phone charging slows - Status]] r2): *"voice and audio feels broken now, i want you to redesign that segment of the process, also lets use pixabay ... make your research about audio and engagement before starting"*; on the voice: *"lets skip the test and go for a higher tier model"*, then chose Inworld TTS-2 over Eleven v4 (own key, $6 a month) and Gemini TTS.

## 1. What was broken (measured on Phone charging r2; the voice track was identical in r1)

| Fault | Measure | Cause |
| --- | --- | --- |
| Captions and cuts early | up to 0.94 s ("Tell"); "It", "That", "So", "The", "Should" 0.3 to 0.8 s | whisper starts a word at the beginning of the silence before it |
| A pause inside a clause | 0.35 s in "Should … phones", absent from the raw take | the pause cutter treated soft consonants as silence (10 % of peak) and cut there |
| Prosody resets | 5 separate takes | text context (`previous_text`) does not carry the audio of the take before |
| Too quiet | −20.8 LUFS master; takes drifting 1.6 LU | no loudness stage; YouTube plays at −14 and never turns quiet uploads up |
| Dead air | pauses are digital silence (−90 dBFS) under a 110 Hz sine bed | phones cannot reproduce a pure sub-200 Hz sine |
| Sounds on words | ticks, pings, clicks fired on the word a plate or label landed on | the builder tied effects to every visual event |

## 2. Evidence

| Finding | Source |
| --- | --- |
| Modern neural TTS learns as well as a human voice; human-likeness raises liking with no uncanny dip | Craig & Schroeder 2017, 2019; Chiou et al. 2020; Kühne et al. 2020 |
| Recognition best near 170 wpm for dense content; 150 felt slow | Rodero 2016, *Media Psychology* |
| Background music under narration cut retention and transfer (d ≈ 0.5 to 1.0, a bland synthesized loop); meta-analyses: about zero overall, costs when music competes with words | Moreno & Mayer 2000; Kämpfe et al. 2011 |
| Narration ≥ 10 LU over music for intelligibility; broadcast guideline 16 to 23 LU; ducking 6 to 12 dB | Torcoli et al. 2019, *JAES*; practitioner guides |
| Separately generated chunks show "abrupt changes in prosody" | ElevenLabs docs (request stitching) |
| Poor audio makes the speaker seem less intelligent and the research less important | Newman & Schwarz 2018 |
| A sound synchronised with a visual change speeds its detection | Van der Burg et al. 2008 |
| YouTube normalises to −14 LUFS, down only; Stable volume on by default | productionadvice.co.uk; YouTube Help 14106294 |

Voice market (Artificial Analysis Speech Arena, read 9 Oct 2026, short clips): Eleven v4 1326, Inworld Realtime TTS-2 1257, Gemini 3.1 Flash TTS 1210, Eleven v3 1177, Eleven turbo-v2.5 1099. Inworld TTS-2 on Replicate: $0.025 per 1,000 characters, ≤ 2,000 characters, `<break>` tags, bracketed natural-language direction, 48 kHz WAV, no timestamps.

Music sources: Pixabay's API serves images and video only; `/api/audio/` answered **403** with the channel's key (9 Oct 2026), and its terms forbid scraping, so Pixabay music is chosen and downloaded by hand, **shield-free tracks only** (a shield marks Content ID registration). Others: Mixkit (manual), YouTube Audio Library (CC BY tracks if cross-posted), Incompetech (CC BY), ccMixter (CC BY, keyless API). AI music on Replicate (not adopted; the rules ban ML-generated sound): `google/lyria-2` about $0.06 per 30 s with a commercial-use badge, `elevenlabs/music` about $0.46 per 55 s.

## 3. Test: Phone charging r3 (same script and pictures; about $0.05: two takes and one timing call)

One Inworld take (voice Dennis, rate 0.95, one break), 37.9 s; pauses 0.34 to 0.64 s and one deliberate beat of 0.86 s. Inworld **adds a break to its own pause** (a 0.7 s break gave 1.24 s of digital silence on the first try, discarded). Whisper heard all 112 script words (the bracketed direction was not read aloud). After onset snapping, "Tell" lands at 39.81 s where it is heard. Mix: −14.0 LUFS, true peak −2.8 dBTP, range 3.0 LU, mix-to-picture lag 20 ms (an `adelay` bug that put the voice 0.44 s early was found and fixed). Music path tested on a stand-in signal: ducking 9.2 dB under speech, music 20 LU under the voice. **Not verified:** how any of it sounds; P7 is the user's.

## 4. Open

Music tracks (Pixabay by hand, or approve ccMixter or AI music); an A/B of "voice only" against "voice + music" on swipe-away and average percentage viewed ([[Publish]] §Analytics loop).
