---
type: script
updated: 2026-10-31
series: Agent at work
words: 163
---

# Script: Rust checks AI code

Status: [[Rust checks AI code - Status]] · rules: [[Format]] §3

## Research (31 Oct 2026)

r2 (user: "explain why is it choosen over typescript and explain how rust works. with a note about why AI chooses it"):

0. **OpenAI, "Codex CLI is Going Native"**, GitHub discussion #1174, fouad-openai, 30 May 2025 (read and captured 31 Oct 2026): Codex CLI moves from TypeScript to Rust. Reasons as written: "Zero-dependency Install — currently Node v22+ is required"; "Native Security Bindings — … we already ship a Rust for linux sandboxing"; "Optimized Performance — no runtime garbage collection, resulting in lower memory consumption"; "Extensible Protocol". InfoQ (4 Jun 2025) and heise report the same.
00. **Rust's rules, shown with real rustc 1.94.1 errors** on two examples I wrote (`Media/…/run/rustc/`): `moved.rs` → `error[E0382]: borrow of moved value: a`; `borrow.rs` → `error[E0502]: cannot borrow v as mutable because it is also borrowed as immutable`.

r1 research, kept:

1. **Premise check:** the request said Rust is "the most chosen language to code with AI". Not supported: GitHub Octoverse (28 Oct 2025, updated 28 Feb 2026, read 31 Oct 2026, captured): "TypeScript overtook both Python and JavaScript in August 2025 to become the most used language on GitHub", 2,636,006 monthly contributors (+66.6 %); "Type systems reduce ambiguity and catch LLM errors before production."
2. **Recorded runs**, 31 Oct 2026 02:50 to 03:03 (-03): Claude Code 2.1.314, `claude -p --model claude-haiku-5-5 --effort low`, file tools plus only `cargo build`/`cargo run` or `python3`, a fresh copy of a small shop crate (`Media/…/run/sandbox-shop`) or `shop.py` each run; `agent.sh`, `grade.py`, `grade_t.py`, `README.md`, one `.jsonl` stream per run.
3. Task 1 ("add restock_low and report(), without copying the names"): Rust 9 of 9 built on the first `cargo build` (0 compiler errors, `std::mem::take`, hidden tests pass, e.g. `Finished … in 0.17s`); Python 9 of 9 pass.
4. Task 2 (4 threads x 50,000 sells on one shared store): Rust 3 of 3 built first try with `Arc<Mutex<Store>>`, `bread left: 0` in 5 runs each; Python 3.14.4: 2 of 3 added a lock, the third did not and still printed 0 in 5 runs.
5. Mündler-Sasahara, Venev, Song, Vechev, He, *Generative Compilation: On-the-Fly Compiler Feedback as AI Generates Code*, arXiv 2607.13921 v2 (16 Jul 2026), ETH Zurich, INSAIT, UC Berkeley. Table 1, Translation (C to Rust, repository level, from CRUST-Bench): Claude Opus 4.8 compiler errors 51.8 % without feedback (LLM), 7.5 % with post-generation compiler feedback (PC), 2.6 % with their method (GC). Across models: 65.9 % → 20.7 % → 13.1 % (§7.2).

**Not verified:** a handful of small tasks on one model (Haiku 5.5): an illustration, not a benchmark; a bigger repository-level task was not run. The paper's "half" is 51.8 % on C-to-Rust translation, one of two datasets (UpdatedAPI: 51.7 %). "Refuses any code it can't prove safe" is the plain-words version of safe Rust's ownership and borrow rules (`unsafe` blocks opt out).

## Package (r2)

- **Promise:** why OpenAI chose Rust over TypeScript for Codex, how Rust's rules work, and why AI agents like them.
- **Titles:** **Why OpenAI Rewrote Codex in Rust: How Rust Works** ← · Rust vs TypeScript: Why AI Tools Switch to Rust · How Rust Works in 60 Seconds (and Why AI Likes It)
- **Frame 0:** CODEX: TYPESCRIPT → RUST over OpenAI's post title and the ownership figure. **Thumbnail:** the ownership figure, "RUST OVER TYPESCRIPT?".
- **Hooks:** fact ← "OpenAI rewrote its Codex coding agent from TypeScript into Rust." · question-free contrast "TypeScript is GitHub's number one language. OpenAI dropped it." · mechanism "Rust frees memory with no garbage collector."

## Scenes (r2)

| # | Beat | Voice (as read) | Words | Viewer sees happen | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | hook | OpenAI rewrote its Codex coding agent from TypeScript into Rust. | 10 | OpenAI's post title; Anatomy `ownership` | 0 |
| 2 | stake | TypeScript is GitHub's most used language, so why switch? OpenAI listed three reasons: no Node to install, native sandboxing, and no garbage collector. | 23 | Octoverse crop; the three reasons cropped from OpenAI's post, one per word; the crate is freed | 0, 1 |
| 3 | mechanism | That last one is how Rust works. Every value has exactly one owner. When the owner is done, the memory is freed. No collector runs in the background. | 28 | `ownership`: the crate and its one blue key; the hatch opens, the crate is gone | (Rust rules) |
| 4 | mechanism 2 | Hand the value to a new owner, and the old name can't touch it. Try, and the compiler stops the build before anything runs. | 24 | the key arcs to post b; post a lights red; the real E0382 error | 00 |
| 5 | mechanism 3 | Borrowing has one rule: many readers, or one writer, never both. That's why two threads can't corrupt the same data. | 20 | three lenses light; the stamp lowers and the lenses go dark; the real E0502 error; NO DATA RACES | 00 |
| 6 | turn (64 %), the AI note | But the reason AI agents like it: the compiler checks every line the model writes. In a July twenty twenty-six paper, half of Claude Opus four point eight's Rust translations didn't compile. Fed the compiler's errors: seven and a half percent. | 41 | `compile-gate` rejects a part; the paper's title and Table 1 row, 51.8 % red, 7.5 % green; reject, return, pass | 5 |
| 7 | payoff, loop | So TypeScript is easier to write. Rust is harder to get wrong. That's the trade OpenAI made. | 17 | TYPESCRIPT: EASY TO WRITE / RUST: HARD TO GET WRONG; readers, writer, the key moves | 0 |

Words: 163 (54.2 s take, 56.1 s video). Turn at 64 %. Loop: "...That's the trade OpenAI made. OpenAI rewrote its Codex coding agent..." Self-test: hook 10 words, names OpenAI, Codex, TypeScript and Rust; stake by 10 s (TypeScript is #1, why switch); re-hooks at 14 s (how Rust works), 22 s (move), 29 s (borrowing), 36 s (but, AI); no banned words. Whisper heard "build" as "bill" in r2's take; the words file says "build". "Many readers or one writer" is the plain-words version of the borrow rules; safe Rust prevents data races, not every concurrency bug. The r1 runs (24 agent runs, 0 compiler errors) are not in r2.
