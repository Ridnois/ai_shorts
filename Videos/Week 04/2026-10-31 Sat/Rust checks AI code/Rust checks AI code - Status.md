---
type: status
updated: 2026-10-31
---

# Rust checks AI code: Status

**Ask once (user, 31 Oct 2026, verbatim):** angle "Compiler = AI's checker (Recommended)" · medium "Recorded run + Anatomy + captures (Recommended)" · after the runs found no compiler errors: "Tell the real result (Recommended)". Request: *"new short: Why Rust is the most choosen language to code with AI"*. The premise was corrected before the question round: GitHub Octoverse (28 Oct 2025) puts TypeScript, not Rust, at #1.

| Stage | State |
| --- | --- |
| **Idea** | Agent at work (last video How AI works). Real thing: 24 recorded Claude Code runs (Claude Haiku 5.5, 31 Oct 2026, `Media/…/run/`): 12 Rust, 0 compiler errors; 12 Python, 0 failed hidden tests. Mündler-Sasahara et al., *Generative Compilation*, arXiv 2607.13921 v2 (16 Jul 2026), Table 1: Claude Opus 4.8 C-to-Rust translations 51.8 % non-compiling, 7.5 % with compiler feedback. GitHub Octoverse 2025. Claim: on small code the model is right without the checker; on real codebases the compiler is what catches it; types are why AI pushed TypeScript to #1. Demand: `youtube_search.py` 31 Oct 2026: 민둥이 "Claude Code·Codex가 돌아가는 언어, Rust가 뜨는 이유" 128,444 (25.7x), AI Frontier "AI Is Rewriting the World's C Code Into Rust" 1,528 (30.9x), Seb Moska "Rust vs Python for AI" 1,764 (18.4x). Hooks in [[Script - Rust checks AI code]]. |
| **Script** | 167 words, 7 scenes, turn at 50 %; Octoverse page and the Generative Compilation PDF read and captured 31 Oct 2026. |
| **Spend** | take `kjacdgea55rmt0d1j298e2c5pm` (1,016 chars, about $0.025); WhisperX `na6fnmh66nrnc0d1j29r2rcnkg` (about $0.005). Cap $0.50. Runs: 24 agent runs + 3 pilot calls on the user's Claude plan. |
| **Build** | Anatomy `compile-gate` (new: `feed`, `check`, `ok`, `bad`, `count`, `part`) in every world; real runs as panels (the command, Claude's `std::mem::take` and `Arc<Mutex>` code, `cargo build` and `cargo run` output) in w3, w4; paper title and Table 1 row (w5), Octoverse phrase crops (w6). Transitions push, whip, cut, dip, blur (1 cut of 6); shot sizes wide, medium (figure under panels), close (Table 1 row). Lint 0 errors; `check3d` OVERLAPS 0; frame audit 5 rounds plus the render sheet. Render `rst-54s-9x16-r1.mp4` 54.3 s; `MIX` −14.1 LUFS, −1.5 dBTP; `LISTEN` PASS; `PACE` PASS (one 2.7 s still at 38.8 s); masters `-yt` 2160x3840 11.7 Mb/s, `-tt` 1080x1920; thumbnail; pack `upload/rst-publish-pack.md`. |
| **Review** | review: ship, fix or drop (asked 31 Oct 2026) |
| **Publish** | |
| **Numbers** | |

## Not verified

A handful of small tasks on one model (Haiku 5.5): an illustration, not a benchmark; no bigger repository-level task was run, so the video's evidence for the compiler catching AI errors is the paper, not my runs. The compile-gate reject in w2 is a schematic of what the compiler does, not one of my runs (none failed). Python passed every hidden test too (said in the caveats, not the voice). The "catch LLM errors" crop shows a sliver of the next letter at its right edge. Quality score against [[Format]] §4 (0 good, 2 bad): frame 0 0, empty frame 1 (w6 opens with captures only for 2.7 s), slideshow 0, text doing the picture's job 1 (w6 is captures and a display line), no real thing 0, static 0, same as last video 0 (new figure, new series); total 2. Not checked: how the voice and effects sound, the pace in motion.

## Feedback
