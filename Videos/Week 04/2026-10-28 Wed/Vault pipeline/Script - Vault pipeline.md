---
type: script
updated: 2026-10-28
series: How it works
words: 134
---

# Script: Vault pipeline (how this vault makes Shorts)

Status: [[Vault pipeline - Status]] · rules: [[Playbook]] · build: [[Design system]]

## Idea (P1, r3)

- **Y:** know how an AI agent turns text into a finished video. **X:** the video is a web page whose timeline is keyed to the voice's word timestamps, filmed by a browser frame by frame. **Series:** How it works (mechanism only: no channel history, [[Playbook]] §2 *Mechanism, not history*).
- **Running example:** the word "page", followed from the take (whisper 18.86 s) to its cue (19.342 s), its tween and its frame.
- **Facts (first-party, 28 Oct 2026):** HyperFrames renders HTML by seeking a paused GSAP timeline frame by frame at 30 fps; this render is 1,399 frames; one Inworld TTS-2 take; whisper word timings; `check3d.mjs` samples every 0.25 s for overlaps; `mix_audio.py` masters to −14 LUFS (YouTube's reference loudness).

## Package

- **Promise:** see how one spoken word becomes a frame of an AI-made Short.
- **Titles:** **How an AI Agent Turns Text Into a Video, Frame by Frame** ← · This Short Was a Web Page First · How AI Video Pipelines Actually Work
- **Thumbnail:** the `format` file snapped square; words **THE VIDEO IS CODE** (4).

## Scenes (r3)

| # | Question it answers | Voice (exact text) | Words | Hero | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | (hook) | Every frame of this Short was a web page first. An AI agent built it, and a browser filmed it. | 20 | real `index.html` lines and "1 page, 1399 frames"; then real frames sliding | index.html |
| 2 | where does the agent start? | The agent starts from notes, plain text rules for script, look and sound, and writes the script in words. | 19 | the real notes listing; then `plan.json` | System/, plan.json |
| 3 | how do the words get a voice and a time? | A voice model reads it in one take. Then Whisper stamps every word with the moment it is spoken. | 19 | this take's waveform; then raw whisper timings | words.json |
| 4 | how does a time become a picture? | Follow one word: page. Its timestamp becomes a cue, and a timeline on the web page draws its picture right then. | 21 | "page" lands at 19.342 s; then the 3 real lines that put it there | words.json, build.py, index.html |
| 5 | how does the page become a video? | A headless browser steps through that timeline thirty times a second, and saves every step as a frame. | 18 | real consecutive frames; the count to 1,399 | render |
| 6 | is it checked? | Before anyone watches, scripts check that nothing overlaps and the sound hits YouTube's loudness. | 14 | real terminal output (r2) | check3d, mix_audio |
| 7 | so what? | So the whole video is code. Change one note, and every next video changes. Would you build videos this way? Tell me. | 22 | the `format` file snaps square; the comment prompt | |

Words: 133. Not verified: how the take sounds.
