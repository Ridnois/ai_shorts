---
type: script
updated: 2026-10-28
series: Agent at work
words: 120
---

# Script: Improve AI Shorts (give the agent ears, eyes and a clock)

Status: [[Improve AI Shorts - Status]] · rules: [[Format]] · build: [[Look]]

## Idea (P1)

- **Y:** make AI-made Shorts that feel checked by a person. **X:** an agent only improves what it can measure, and it is blind to sound and frames unless a tool turns them into numbers. **Series:** Agent at work. **Theme line:** an agent improves only what it can measure.
- **Real case:** this vault's agent could not hear its renders (Playbook §7 listed the sound as *not verified*); `listen.py` (28 Oct 2026) closes that. Mechanism only, no channel history.
- **Hook (contradiction):** "An AI agent can make a video, but it cannot hear it."
- **Street-lamp:** no headline answers "what lets an agent check a video it cannot watch" (pass). **Argue against:** (1) tool tours bore: one running measurement, not a list; (2) viewers may not use agents: the close asks about checking any AI output; (3) abstract: real terminal output on screen.
- **Demand check:** not run (no `.env`, no YouTube token on this machine).

## Facts bank (28 Oct 2026; vault facts first-party)

1. HyperFrames renders HTML by seeking a paused GSAP timeline frame by frame (30 fps). 2. `hyperframes snapshot --at <t,…>` saves real frames for the agent to look at. 3. `incredibly-fast-whisper` gives a start and end per word. 4. `hfkit` cues each effect on a heard word. 5. `check3d.mjs` samples every 0.25 s for overlaps. 6. `mix_audio.py` masters to −14 LUFS, true peak −1 dBTP (YouTube's reference). 7. `loudnorm` measures integrated loudness, true peak and range (EBU R128). 8. `silencedetect` lists every gap with start and length. 9. `listen.py` adds pass or fail on those numbers (exit code 1). 10. The Playbook allows pauses of 0.3 to 0.9 s. 11. The agent cannot watch video or hear audio (CLAUDE.md). 12. earshot (Leonxlnx/earshot, MIT, CPU-only) describes sound as tags and measurements; source: its README and a 16 Oct 2026 write-up; claims self-reported. 13. earshot loads two open models, CLAP (Apache-2.0) and AST (BSD-3-Clause), about 1.1 GB. 14. Each earshot CLI call loads models in roughly 20 to 40 s (README). 15. Feedback becomes an edit of the owning rule, guarded by `check_vault.py`.

## Package

- **Promise:** see the three checks that let an AI agent judge a Short it cannot watch or hear.
- **Titles:** **How an AI Agent Checks a Video It Can't Hear** ← · Give Your AI Agent Ears, Eyes and a Clock · How to Make Better AI Shorts (Tools That Matter)
- **Thumbnail:** a real waveform with one silence lit rose; words **IT CAN'T HEAR** (3).
- **Opening map:** scene 1 = promise; scene 2 = proof (the listen run) and plan (ears, eyes, clock).

## Scenes

| # | Question it answers | Voice (exact text) | Words | Visual beat (real) | Camera · transition |
| --- | --- | --- | --- | --- | --- |
| 1 | (hook) | An AI agent can make a video, but it cannot hear it. So it ships the sound blind. | 17 | a real waveform, one gap lit rose | wide, push into the gap |
| 2 | what fixes blind sound? | Fix one: give it ears. A script measures the finished file: loudness, every silence, any clipping. It prints pass or fail. | 22 | real `listen.py` output of this render | close on the LUFS line · whip |
| 3 | and the picture? | Fix two: give it eyes. Snapshots of real frames show the agent what the viewer sees, before anyone presses render. | 20 | real snapshot contact sheet sliding | medium · cut |
| 4 | how do both line up in time? | Fix three: give it the clock. Whisper stamps every word, so each picture lands on the word that names it. | 20 | real `words.json` lines; one word lights, its tween fires | close · dip |
| 5 | what does it do with a fail? | Now a number fails. The agent edits the rule that caused it, not one video, so the next video improves too. | 21 | a rose number turning mint; the rule line in the note | medium · blur |
| 6 | so what? | So a better Short starts with a better check. Which would you add first: ears, eyes, or the clock? | 20 | comment prompt, 3 chips | wide |

Words: 120. Not verified: how the take sounds; on-screen numbers come from the real `listen.py` run at build.
