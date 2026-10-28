---
type: script
updated: 2026-10-28
series: Agent at work
words: 126
---

# Script: Vault pipeline (how this vault makes Shorts)

Status: [[Vault pipeline - Status]] · rules: [[Playbook]] · build: [[Design system]]

## Idea (P1)

- **Y:** make videos (or any repeated work) with an AI agent without re-explaining your taste every time. **X:** the agent reads rules kept as notes before every run, and a correction edits the note, not the output.
- **Series:** Agent at work (the previous video, How RAG works, was How it works). **Figure set:** `slow`, `format` + real captures (variety guard: none used by How RAG works).
- **Real case:** this channel, as of 27 Oct 2026: 14 videos rendered (24 renders), 0 uploaded; 111 KB of rules rewritten to 66 KB (−40 %) and the look moved into `hfkit.py`.
- **Score:** surprise 4 · scale 3 · depth 4 · evidence 5 (all first-party) · showable 5 · plain 4. **Against it:** "a channel about itself" (answered: the habit transfers to any agent work) · "no numbers anyone cares about" (answered: 14 made, 0 shipped is a stake every maker knows) · "inside baseball tools" (answered: tools named on screen only, the voice says what they do).
- **Street-lamp:** no headline says how an agent keeps a style across videos: pass. **Expert test:** "feedback edits the rule, not the render" is the interesting part. **Coffee test:** "My agent makes videos from a folder of rules; when it gets something wrong I fix the rule."
- **Demand check:** not run: `youtube_search.py` needs the expired token (HTTP 400). The bridge: Y ("AI agent makes YouTube Shorts") is a common search; to be verified at P8.
- **Hooks:** (contradiction) "An AI agent made this Short from a folder of notes. No long prompt." ← chosen · (number) "Fourteen videos made, zero uploaded. Then the agent fixed its own rules." · (stakes) "Your agent forgets your taste every time. Mine reads it first." · (question, rejected as opener) "What if your agent kept your notes?" · (fact) "Every frame of this video was a web page first."

## Facts bank (first-party unless named; checked 27 to 28 Oct 2026)

1. 14 videos rendered in 24 renders, 0 uploaded (`Media/`, [[YouTube Channel]]). 2. How RAG works took 5 renders. 3. Rules were 111,038 bytes in 9 notes; now 66,196 (−40.4 %). 4. 26 verbatim user corrections became rules (Status notes). 5. The vault has 285 git commits since 3 Oct 2026 (Obsidian auto-commit). 6. Voice: Inworld TTS-2, voice Dennis, one take, $0.025 per 1,000 characters ([[Workflow]]). 7. Word timings: whisper on Replicate, about $0.01. 8. A typical Short costs about $0.05. 9. HyperFrames renders HTML by seeking a paused timeline frame by frame (HyperFrames skill, 0.8.209). 10. `check3d.mjs` samples the page every 0.25 s for overlaps. 11. Mix to −14 LUFS: How RAG works r5 measured −14.04 LUFS, true peak −2.35 dBTP. 12. That render was 1.66 Mbps; v3 renders at CRF 14. 13. 33 packaged Hairline figures (MIT). 14. Baseline: 39.7 % viewed vs swiped away on the old niche (YouTube, 9 Oct 2026). 15. Shorts views count any start since 31 Mar 2025.

## Package

- **Promise:** you see the whole path an AI agent takes from notes to a finished Short, and the one habit that keeps it on style.
- **Titles:** **How an AI Agent Makes YouTube Shorts From Notes** ← · I Let an AI Agent Run My Shorts Channel · The Agent Workflow That Fixed My AI Videos
- **Thumbnail:** the `format` figure with its lines snapped square in mint; words **FIX THE NOTE** (3). Beats neighbours (screen recordings of prompts) by naming the habit, not the tool.
- **Opening map:** scene 1 = promise (an agent, notes, no long prompt); scene 2 = proof (14 made, 0 uploaded) and plan (the rail).

## Scenes

| # | Question it answers | Voice (exact text) | Words | Delivery · pause | Visual beat | Camera | Text on screen | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | (hook) | An AI agent made this Short from a folder of notes. No long prompt. Here is how it works. | 19 | calm, a small smile | the real `System/` listing (notes and sizes) beside a phone holding a real frame; a "long prompt" tag struck on "No" | close on the listing, pull back to wide on "Short" | rail: notes · script · voice · page · checks | `ls -l System` |
| 2 | what notes? | The notes are its rules for writing, look and sound. But they grew into a mess. Fourteen videos made, zero uploaded. | 21 | a dry turn on "But" | three note tags light on their words; counters run to 14 and stay at 0 (rose); a strip of real frames slides | medium on the counters | card: AS OF 27 OCT 2026 | Media, index |
| 3 | so what changed? | So the agent rewrote them, forty percent shorter, and turned the look into code. | 14 | brisk | two bars: 111 KB shrinks to 66 KB (mint); the real `hfkit.py` lines | push to the code | 111 KB to 66 KB | `wc -c` |
| 4 | how does a video run? | Each video runs one path: a script in words, then one voice take, no cuts. | 15 | even | crates on a belt pass a gate (`slow`): script, then the real waveform of this take | medium on the belt | callouts: script, one take | plan.json, take |
| 5 | how do words become frames? | Every word gets a time. Each one cues a web page, filmed frame by frame. | 14 | even | the real `words.json` lines; a strip of real rendered frames | close on one word's time, then wide | callout: cue | words.json |
| 6 | is it checked? | Before a human sees it, checks run: overlaps, empty screens, loudness. | 11 | precise | real terminal output: `OVERLAPS 0`, `MIX … -14.0 LUFS` | close on each line | | check3d, mix_audio |
| 7 | what do I copy? | Here is the part to copy. When your agent gets it wrong, do not fix the video. Fix the note. Would you let an agent run your channel? Tell me. | 32 | beat 0.2 before "Fix the note" | the `format` file snaps square in mint (payoff riser and hit on "note"); comment prompt | wide | ask: Agent run your channel? · yes · with checks · never | |

Theme line: **fix the note, not the video.** Words: 126 (short test block). Not verified: demand for the search phrase; how the take sounds.
