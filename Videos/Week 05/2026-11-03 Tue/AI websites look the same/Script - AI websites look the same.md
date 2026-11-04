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

## Voice (exact text)

| Scene | Beat | Voice | Words | Viewer sees happen | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | Hook | Claude Code built me five websites. They're the same website. | 10 | the five real bare heroes tile in; "5 APPS, 1 WEBSITE" | run, bare |
| 2 | Stake | A notes app, a budget app, a fitness band. Same off-white page, same headline on the left, same second button: See how it works. Ship one, and your product looks like everyone else's. | 33 | each named hero takes the frame; the five real "See how it works" button crops stack; tag "Claude Opus 5.5 · 3 Nov 2026" | run, bare |
| 3 | Mechanism | Here's why. A model writes one token at a time, and takes a likely next one. | 16 | `tokens` chips "See · how · it · works" arrive one at a time | mechanism |
| 4 | Mechanism | The likeliest page is off-white. The likeliest button says, See how it works. Ask with no direction, and you get the average, five times out of five. | 27 | `probs` bars, labelled "share of our 5 runs", fill; the spine grid returns with every button boxed | run counts |
| 5 | Turn | But the average moves. The old tell was a purple gradient. The new one is a serif headline with one orange word in italics. The look changed. The sameness didn't. | 30 | dip; impeccable README crop "Purple-to-blue gradients" marked; three real headline crops, the orange word marked | README, run |
| 6 | Payoff | So give it a direction it can't average. I installed Impeccable, a design skill with a hundred thousand GitHub stars, and ran the same five prompts. Five different sites. | 29 | the GitHub header, "102k" boxed; the five skill heroes replace the bare grid tile by tile; payoff hit on "different" | run, skill |
| 7 | Close | No skill? Name a font, a colour and a site you love. Skip that, and Claude Code builds you the same website. | 22 | three chips FONT, COLOUR, A SITE YOU LOVE; back to the frame-0 bare grid | README "the brief wins" |

167 words. Turn at about 52 % of the words (scene 5).

## Sources (checked 3 Nov 2026)

- **Our runs** (`Media/…/AI websites look the same/run/`, 3 Nov 2026, about 23:20 local): Claude Code 2.1.318, model `claude-opus-5-5` (Claude Opus 5.5, from each run's `modelUsage`), `claude -p` with Write only, one prompt per product: "Build a landing page for {a note-taking app · a project management tool · a personal finance app · a fitness tracker · a recipe app}. Write it as one file, index.html, with inline CSS. No questions, just build it." Measured in headless Chrome at 1280×800: page background off-white in 5 of 5 (`rgb(244–251, 240–250, 228–247)`); headline left with a product picture right in 5 of 5; a small label above the headline in 5 of 5; a secondary button with the exact text "See how it works" in 5 of 5; one coloured word in the headline in 4 of 5, italic serif orange in 3 of 5 (Margin "before", Tack "Monday.", Mise "whatever's"). A collision overwrote two of the first runs; finance and recipe were rerun in their own folders, the note app kept its first output.
- **Skill runs** (same five prompts with `/impeccable` prefixed, plus "make your own product assumptions"; tools Write, Read, Edit, Glob, Grep, Skill, no Bash, so impeccable's scripts never ran): impeccable 4.8.0, commit `9fadc41` (2 Nov 2026), copied into `.claude/skills/`. Backgrounds navy, yellow, royal blue (twice), brick; display fonts Archivo, Anybody, Barlow Condensed, Big Shoulders Display; 0 of 5 "See how it works".
- **impeccable README** (github.com/pbakaus/impeccable, read 3 Nov 2026): "Inter for everything. Purple-to-blue gradients. … Ask an agent for a page with no other guidance and these show up again and again, across models and projects." And: "Without Impeccable, it builds the tasteful default: cream page, thin serif, italic accent, pill buttons." 101.6k stars (sidebar), 102k (button), Apache-2.0. Recorded under fair comment; credit in the description.
- **Mechanism:** a language model generates one token at a time from a probability over the next token; Claude Code samples from it. The bars in scene 4 are **counts from our five runs**, not model probabilities (Claude exposes no token odds); the screen says so.

*Not verified:* "the old tell was a purple gradient" rests on the README's list, not on our own older runs. Advice in scene 7 (name a font, a colour, a site) was not run; it follows the README's "The brief wins" rule. Five runs per arm is a small sample; the skill pages share traits of their own (saturated grounds, condensed display type).

## Beat sheet (spine: the 2×3 grid of the five bare heroes; moves borrowed from [[Shots]])

Borrowed: **a spine the video returns to** ([[Coding with Lewis - The AI Model Iceberg]]): the bare grid is whole at 0 s and returns in scenes 4 and 7 with a new mark each time. **The contradiction is one frame** ([[3Blue1Brown - The medical test paradox]]): in scene 6 the skill heroes replace the bare ones tile by tile in the same grid.

| Cue | Imp. | Medium | Picture event | Camera | Trans. | Text | Sound |
| --- | --- | --- | --- | --- | --- | --- | --- |
| frame 0 | 3 | capture | bare grid, all five | wide | – | 5 APPS, 1 WEBSITE | hit |
| notes / budget / band | 1 | capture | named hero full width | medium | push | – | whoosh |
| See how it works | 3 | capture | five button crops stack (sheet) | close | – | 5 / 5 | pops |
| token | 2 | primitive | tokens chips | medium | whip | ONE TOKEN AT A TIME | pops |
| likeliest | 2 | primitive | probs fill: off-white 1.0, label 1.0, button 1.0, coloured word 0.8 | wide | cut | SHARE OF OUR 5 RUNS | – |
| average | 2 | capture | grid returns, buttons boxed | wide | – | THE AVERAGE | click |
| purple | 3 | capture | README crop marked | close | dip | – | – |
| orange | 2 | capture | three headline crops, word marked | medium | – | – | click |
| stars | 2 | capture | GitHub header, 102k boxed | close | blur | – | click |
| different | 3 | capture | skill grid replaces bare grid | wide | – | 5 DIFFERENT SITES | payoff |
| font | 1 | primitive | three chips | medium | cut | – | pops |
| same website | 2 | capture | bare grid returns | wide | – | – | – |
