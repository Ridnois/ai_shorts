---
type: status
updated: 2026-10-31
---

# Rust checks AI code: Status

**Ask once (user, 31 Oct 2026, verbatim):** angle "Compiler = AI's checker (Recommended)" · medium "Recorded run + Anatomy + captures (Recommended)" · after the runs found no compiler errors: "Tell the real result (Recommended)". Request: *"new short: Why Rust is the most choosen language to code with AI"*. The premise was corrected before the question round: GitHub Octoverse (28 Oct 2025) puts TypeScript, not Rust, at #1.

| Stage | State |
| --- | --- |
| **Idea** | Agent at work (last video How AI works). Real thing: 24 recorded Claude Code runs (Claude Haiku 5.5, 31 Oct 2026, `Media/…/run/`): 12 Rust, 0 compiler errors; 12 Python, 0 failed hidden tests. Mündler-Sasahara et al., *Generative Compilation*, arXiv 2607.13921 v2 (16 Jul 2026), Table 1: Claude Opus 4.8 C-to-Rust translations 51.8 % non-compiling, 7.5 % with compiler feedback. GitHub Octoverse 2025. Claim: on small code the model is right without the checker; on real codebases the compiler is what catches it; types are why AI pushed TypeScript to #1. Demand: `youtube_search.py` 31 Oct 2026: 민둥이 "Claude Code·Codex가 돌아가는 언어, Rust가 뜨는 이유" 128,444 (25.7x), AI Frontier "AI Is Rewriting the World's C Code Into Rust" 1,528 (30.9x), Seb Moska "Rust vs Python for AI" 1,764 (18.4x). Hooks in [[Script - Rust checks AI code]]. |
| **Script** | |
| **Spend** | take `kjacdgea55rmt0d1j298e2c5pm` (1,016 chars, about $0.025); WhisperX `na6fnmh66nrnc0d1j29r2rcnkg` (about $0.005). Cap $0.50. Runs: 24 agent runs + 3 pilot calls on the user's Claude plan. |
| **Build** | |
| **Review** | |
| **Publish** | |
| **Numbers** | |

## Not verified

## Feedback
