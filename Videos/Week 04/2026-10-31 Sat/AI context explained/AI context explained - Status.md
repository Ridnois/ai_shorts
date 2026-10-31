---
type: status
updated: 2026-10-31
---

# AI context explained: Status

**Ask once (user, 31 Oct 2026, verbatim):** angle "It rereads everything (Recommended)" · medium "Use all the tools available plus recorded run". Request: *"new short: AI context explained, how AI remembers"*.

| Stage | State |
| --- | --- |
| **Idea** | How AI works (last video What's coming). Real thing: Claude Opus 5.5 (`claude-opus-5-5`) via `claude -p` (Claude Code 2.1.314), 31 Oct 2026, 6 recorded runs (`Media/…/run/`); Anthropic context-window docs; Liu et al., *Lost in the Middle* (arXiv 2307.03172 v3). Claim: a chatbot has no memory of you; each turn the whole chat is sent again (618, 654, 741, 838 input tokens); "memory" is a note pasted in first; and a longer chat is not a better memory (54 % with the answer in the middle, under 56 % closed book). Demand: `youtube_search.py` 31 Oct 2026: Claude "Context Management in Claude Code" 448,724 (7.0x), Analytics Vidhya "What is the Context Window in LLMs?" 7,605 (15.1x), Casey Fiesler 11,208 (3.3x). Hooks in [[Script - AI context explained]]. |
| **Script** | 165 words, 7 scenes, turn at 64 %; Anthropic context-window docs, OpenAI conversation-state docs, Claude Code memory docs and the Liu et al. PDF read and captured 31 Oct 2026. |
| **Spend** | take `zys70dmza9rmr0d1j12v5b0ser` (985 chars, about $0.025); incredibly-fast-whisper `w66jy1rassrmy0d1j13bgd815g` canceled in `starting`; WhisperX `g2kvpvrfadrne0d1j15t24mvxr` (about $0.005). Total about $0.03, cap $0.50. Runs: 6 `claude -p` turns on the user's Claude plan. |
| **Build** | Anatomy `context-reader` (new: `msgs`, `scan`, `read`, `note`, `lit`, `mid`) in w1 to w5 and w7; real run as terminal panels (prompt, real outputs, the memory file) in w2, w4, w5; counter 618, 654, 741; phrase crops of OpenAI and Anthropic docs (w1, w3), Liu et al. title, affiliation and Figure 1 from the PDF (w6); Hairline `window` (w6). Transitions push, whip, cut, blur, dip (1 cut of 6); shot sizes wide, medium (zooms on tray and note), close (first slip). Lint 0 errors; `check3d` OVERLAPS 0 (one interface-strip note on the w3 whip entrance, one frame, accepted); frame audit 4 rounds plus the render sheet. Render `ctx-52s-9x16-r1.mp4` 51.5 s; `MIX` −14.0 LUFS, −1.4 dBTP; `LISTEN` PASS; `PACE` PASS; masters `-yt` 2160x3840 12.8 Mb/s, `-tt` 1080x1920; thumbnail; pack `upload/ctx-publish-pack.md`. |
| **Review** | review: ship, fix or drop (asked 31 Oct 2026) |
| **Publish** | |
| **Numbers** | |

## Not verified

The ChatGPT app's own context handling was not measured (it may trim or summarize long chats); the hook rests on OpenAI's API docs and the measured Claude runs. The memory run's +212 tokens include Claude Code's wrapper around the file. Lost in the Middle is a 2023 test on GPT-3.5-Turbo. Two capture phrases on the Claude Code memory page were not found by the headless browser (the quote is in the Script note from the fetched page, not captured). Quality score against [[Format]] §4 (0 good, 2 bad): frame 0 0 (claim + reader mid-read), empty frame 1 (the lower stage under the figure stays plain paper in w3 to w5), slideshow 0, text doing the picture's job 0, no real thing 0 (real runs, docs, paper figure), static 0 (`PACE` PASS), same as last video 0 (new figure, new series); total 1. Not checked: how the voice and effects sound, the pace in motion.

## Feedback
