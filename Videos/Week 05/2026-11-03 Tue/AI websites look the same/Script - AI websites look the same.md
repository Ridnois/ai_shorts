---
type: script
updated: 2026-11-03
---

# Script: AI websites look the same

← [[AI websites look the same - Status]] · [[Story]] · [[Picture]] §Medium · idea [[Why every AI website looks the same]]

**Promise:** you will see five real pages Claude Code built from five different briefs, why they come out as one page, and the one change that made five different ones.
**Pattern:** `surprising-result` · **Series:** Agent at work · **Main medium:** capture (our recorded runs and their real screenshots).

## Package

| | |
| --- | --- |
| Title | Why Every AI Website Looks the Same |
| Alternatives | Claude Code Built Me 5 Websites. They're the Same One · Why AI Websites All Say "See How It Works" |
| Frame-0 text | 5 APPS, 1 WEBSITE |
| Thumbnail | the five real bare heroes in a grid, every "See how it works" boxed · "SAME WEBSITE" |
| Field (nearest [[Radar]] outliers) | "Every AI Startup Website Looks the Same" (HRaGvoRa-IU, 458 k, 9.3x); "The AI Model Iceberg" (34.6x); "3 GitHub repos with 150,000 stars that put you ahead…" (6.2x, early); "WTF is going on at GitHub?" (8.6x). Ours names the thing and adds what the others do not: a real five-run test, the reason (likeliest token) and a fix measured on the same five prompts |

## Voice (exact text, r2)

| Scene | Beat | Voice | Words | Viewer sees happen | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | Hook | Claude Code built this website from one prompt. Before a design skill, and after. | 14 | the bare notes page full width, BEFORE; the skill page lands on "after", AFTER | runs |
| 2 | Proof | A budget app, before and after. A fitness band, before and after. All five apps, one prompt each. | 18 | budget and fitness pages full width, before then after; the bare grid, then the five skill pages land over it tile by tile | runs |
| 3 | Stake | Without the skill, all five came out as one page. Same off-white background, same headline on the left, same second button: See how it works. | 25 | the bare grid, a zoom on one headline, every button boxed; the five real button crops stack, 5 OF 5 | runs |
| 4 | Mechanism | Here's why. A model writes one token at a time, and takes a likely next one. | 16 | `tokens` chips "See · how · it · works" | mechanism |
| 5 | Mechanism | The likeliest page is off-white. The likeliest button says, See how it works. With no direction, you get the average. | 20 | `probs` bars ("our 5 runs, not odds"), the real button; the grid boxed, THE AVERAGE | run counts |
| 6 | Turn | And the average moves. The old tell was a purple gradient. Now it's a serif headline with one orange word in italics. | 22 | README crop "Purple-to-blue gradients."; three real headlines | README, runs |
| 7 | Conclusion | The skill gives Claude a direction: fonts, colours, and a list of things never to do. Somebody's taste, written down. | 20 | the GitHub repo and stars; chips fonts, colours, never do this; the skill grid | README, SKILL.md |
| 8 | Payoff | Tools make a page cheap. Taste decides which page. Without it, Claude Code builds the same page. | 17 | the bare grid; the skill pages land over it (payoff on "which"); the frame-0 page, THE SAME PAGE | – |

152 words. Order (user, 4 Nov 2026): before and after first, then the explanation, then tools and taste.

## Sources (checked 3 Nov 2026)

- **Our runs** (`Media/…/AI websites look the same/run/`, 3 Nov 2026, about 23:20 local): Claude Code 2.1.318, model `claude-opus-5-5` (Claude Opus 5.5, from each run's `modelUsage`), `claude -p` with Write only, one prompt per product: "Build a landing page for {a note-taking app · a project management tool · a personal finance app · a fitness tracker · a recipe app}. Write it as one file, index.html, with inline CSS. No questions, just build it." Measured in headless Chrome at 1280×800: page background off-white in 5 of 5 (`rgb(244–251, 240–250, 228–247)`); headline left with a product picture right in 5 of 5; a small label above the headline in 5 of 5; a secondary button with the exact text "See how it works" in 5 of 5; one coloured word in the headline in 4 of 5, italic serif orange in 3 of 5 (Margin "before", Tack "Monday.", Mise "whatever's"). A collision overwrote two of the first runs; finance and recipe were rerun in their own folders, the note app kept its first output.
- **Skill runs** (same five prompts with `/impeccable` prefixed, plus "make your own product assumptions"; tools Write, Read, Edit, Glob, Grep, Skill, no Bash, so impeccable's scripts never ran): impeccable 4.8.0, commit `9fadc41` (2 Nov 2026), copied into `.claude/skills/`. Backgrounds navy, yellow, royal blue (twice), brick; display fonts Archivo, Anybody, Barlow Condensed, Big Shoulders Display; 0 of 5 "See how it works".
- **impeccable README** (github.com/pbakaus/impeccable, read 3 Nov 2026): "Inter for everything. Purple-to-blue gradients. … Ask an agent for a page with no other guidance and these show up again and again, across models and projects." And: "Without Impeccable, it builds the tasteful default: cream page, thin serif, italic accent, pill buttons." 101.6k stars (sidebar), 102k (button), Apache-2.0. Recorded under fair comment; credit in the description.
- **Mechanism:** a language model generates one token at a time from a probability over the next token; Claude Code samples from it. The bars in scene 4 are **counts from our five runs**, not model probabilities (Claude exposes no token odds); the screen says so.

- **impeccable SKILL.md** (4.8.0): routes new pages through `new-work.md` and `craft-floor.md`, which "carries the quality floor, the absolute bans"; scene 7's "fonts, colours, and a list of things never to do" summarises that.

*Not verified:* "the old tell was a purple gradient" rests on the README's list, not on our own older runs. Advice in scene 7 (name a font, a colour, a site) was not run; it follows the README's "The brief wins" rule. Five runs per arm is a small sample; the skill pages share traits of their own (saturated grounds, condensed display type).

## Beat sheet (r2; spine: the 2-2-1 grid of the five pages)

Borrowed: **a spine the video returns to** ([[Coding with Lewis - The AI Model Iceberg]]): the grid returns in scenes 2, 3, 5, 7 and 8. **The contradiction is one frame** ([[3Blue1Brown - The medical test paradox]]): the skill pages land over the bare ones in the same grid (scenes 2 and 8; the user's favourite moment of r1, 0:43 to 0:47).

Transitions: push, dip, whip, cut, blur, push, cut. Builder: `hf/gen_beats.py` writes `hf/beats.json`.
