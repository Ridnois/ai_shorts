---
type: script
updated: 2026-10-31
series: Agent at work
words: 167
---

# Script: Rust checks AI code

Status: [[Rust checks AI code - Status]] · rules: [[Format]] §3

## Research (31 Oct 2026)

1. **Premise check:** the request said Rust is "the most chosen language to code with AI". Not supported: GitHub Octoverse (28 Oct 2025, updated 28 Feb 2026, read 31 Oct 2026, captured): "TypeScript overtook both Python and JavaScript in August 2025 to become the most used language on GitHub", 2,636,006 monthly contributors (+66.6 %); "Type systems reduce ambiguity and catch LLM errors before production."
2. **Recorded runs**, 31 Oct 2026 02:50 to 03:03 (-03): Claude Code 2.1.314, `claude -p --model claude-haiku-5-5 --effort low`, file tools plus only `cargo build`/`cargo run` or `python3`, a fresh copy of a small shop crate (`Media/…/run/sandbox-shop`) or `shop.py` each run; `agent.sh`, `grade.py`, `grade_t.py`, `README.md`, one `.jsonl` stream per run.
3. Task 1 ("add restock_low and report(), without copying the names"): Rust 9 of 9 built on the first `cargo build` (0 compiler errors, `std::mem::take`, hidden tests pass, e.g. `Finished … in 0.17s`); Python 9 of 9 pass.
4. Task 2 (4 threads x 50,000 sells on one shared store): Rust 3 of 3 built first try with `Arc<Mutex<Store>>`, `bread left: 0` in 5 runs each; Python 3.14.4: 2 of 3 added a lock, the third did not and still printed 0 in 5 runs.
5. Mündler-Sasahara, Venev, Song, Vechev, He, *Generative Compilation: On-the-Fly Compiler Feedback as AI Generates Code*, arXiv 2607.13921 v2 (16 Jul 2026), ETH Zurich, INSAIT, UC Berkeley. Table 1, Translation (C to Rust, repository level, from CRUST-Bench): Claude Opus 4.8 compiler errors 51.8 % without feedback (LLM), 7.5 % with post-generation compiler feedback (PC), 2.6 % with their method (GC). Across models: 65.9 % → 20.7 % → 13.1 % (§7.2).

**Not verified:** a handful of small tasks on one model (Haiku 5.5): an illustration, not a benchmark; a bigger repository-level task was not run. The paper's "half" is 51.8 % on C-to-Rust translation, one of two datasets (UpdatedAPI: 51.7 %). "Refuses any code it can't prove safe" is the plain-words version of safe Rust's ownership and borrow rules (`unsafe` blocks opt out).

## Package

- **Promise:** whether Rust is really the AI-coding language, shown on real agent runs.
- **Titles:** **Is Rust the Best Language for AI Coding? I Tested Claude** ← · I Tried to Make Claude Write Broken Rust · Why AI Writes Better Code in Typed Languages
- **Frame 0:** 12 TRIES. 0 ERRORS. over the compile gate passing a part. **Thumbnail:** the gate, "AI NEVER BROKE RUST".
- **Hooks:** result ← "I gave Claude twelve chances to write broken Rust. It never did." · number "Half of Claude's Rust didn't compile." · contradiction "Rust isn't the language AI made number one."

## Scenes

| # | Beat | Voice (as read) | Words | Viewer sees happen | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | hook | I gave Claude twelve chances to write broken Rust. It never did. | 12 | Anatomy `compile-gate`: the part is inspected, passes green into the tray | 2 to 4 |
| 2 | stake | Rust's compiler refuses any code it can't prove safe. That's why people call it the best language for AI coding. So I tested it. | 24 | the gate rejects a part (red lamp, kicked to the return chute); the question; 12 runs a language | 5 |
| 3 | mechanism | Claude Haiku five point five. A small shop app. One new feature. Cargo built it on the first try, nine times out of nine. | 24 | the real command, the code Claude wrote (`std::mem::take`), the real `cargo build` output; parts pass | 2, 3 |
| 4 | mechanism 2 | Then the hard case: four threads selling from one shared store. Rust won't share it unguarded, and Claude added a lock every time. | 23 | Claude's real `Arc<Mutex>` code, the lock row lit; `bread left: 0`; LOCK: 3 OF 3 | 4 |
| 5 | turn (50 %) | But those are small programs. On real codebases, a July twenty twenty-six paper found half of Claude Opus four point eight's Rust translations didn't compile. With the compiler's errors fed back: seven and a half percent. | 36 | a reject on the gate; the paper's title and Table 1 row, 51.8 % ringed red, 7.5 % green; reject, return, pass | 5 |
| 6 | turn 2 | And the language AI pushed to number one on GitHub isn't Rust. It's TypeScript, for the same reason: types catch the model's mistakes. | 23 | Octoverse captures; "catch LLM errors"; the gate checks a part | 1 |
| 7 | payoff, loop | So code with AI in a typed language, and make the agent run the checker. Small code, it won't need it. Big code, it will. | 25 | the part passes the gate; BIG CODE NEEDS IT; a new part rides in | 1, 5 |

Words: 167 (52.4 s take, 54.3 s video). Turn at 50 %. Loop: "...Big code, it will. I gave Claude twelve chances to write broken Rust..." Self-test: hook 12 words, names Claude and Rust; stake by 10 s (the claim tested); re-hooks at 12 s (the run), 20 s (hard case), 27 s (but), 38 s (TypeScript); no banned words. Cut test dropped a Python sentence (Python also passed every test) and the 13.1 % average.
