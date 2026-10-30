---
type: script
updated: 2026-10-29
series: Agent at work
words: 167
---

# Script: Effort level explained

Status: [[Effort level explained - Status]] · rules: [[Format]] §3 · idea: [[Effort level explained]]

## Research (29 Oct 2026)

1. **Recorded runs**, 29 Oct 2026 21:00 to 21:42 (-03), `claude -p --model claude-opus-5-5 --effort <level> --tools ""` (Claude Code 2.1.312, print mode, JSON output); log and checker in `Media/…/run/` (`README.md`, `ask.sh`, `show.py`, one JSON per run).
2. Easy: "What is 17 times 24?" low → 408, **3** output tokens, 2.2 s; max → 408, **45** output tokens (42 thinking), 3.1 s.
3. Seating puzzle (six people, eight clues, unique answer checked by brute force): low → Eli, **543** tokens, 6.1 s; max → Eli, **1,377** tokens, 13.5 s (2.5x).
4. Hard: "How many primes below 2000 have a digit sum that is also prime?" (answer 156, checked in Python). Low, three tries: a written tool call with no number; "I'd rather not guess a number"; **156 with 3,189 tokens**, 27.3 s. Max, one try: **156 with 22,780 tokens**, 175.7 s (2 min 56 s). 22,780 / 3,189 = 7.1.
5. Low also got 14 of 14 other single questions right (counts, arithmetic, a modular power, a clock puzzle), 59 to 456 tokens each.
6. Anthropic, *Effort*, platform.claude.com, read 29 Oct 2026 (captured): "Control how many tokens Claude uses"; levels max, xhigh, high, medium, low; "The default on Claude Opus 5.5 and Claude Haiku 5.5" is medium; "Effort is a behavioral signal, not a strict token budget."

**Not verified:** a handful of runs, one max try on the hard question: an illustration, not a benchmark. The tool-call endings come from Claude Code's system prompt with tools off; through the bare API, low might fail differently or not at all. xhigh and high were not run.

## Package

- **Promise:** whether a higher effort level buys a better answer, shown on real runs.
- **Titles:** **Claude Effort Level Explained: Is Higher Better?** ← · Low vs Max Effort in Claude Code (I Tested It) · Why Max Effort Isn't Smarter: Claude Opus 5.5 Test
- **Frame 0:** MAX EFFORT / 7× THE TOKENS over the meter at max (a full token stack, a green card). **Thumbnail:** the meter, "MAX = 7× TOKENS".
- **Hooks:** number ← "Max effort cost Claude seven times the tokens for the same answer." · contradiction "Turning Claude up to max didn't make it smarter." · fact "Claude's low effort answered in three tokens."

## Scenes

| # | Beat | Voice (as read) | Words | Viewer sees happen | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | hook | Max effort cost Claude seven times the tokens for the same answer. | 12 | Anatomy `effort-meter` at max: full stack, green card; push to the stack | runs |
| 2 | stake | Effort level is a dial in Claude Code: low, medium, high, x high, max. Turn it up, and it should get smarter. So I tested it on Claude Opus five point five. | 32 | real docs table, each level marked as said; the real command | docs, runs |
| 3 | mechanism | The dial doesn't swap the model. It tells Claude how many tokens to spend, mostly on thinking before it answers. | 20 | the docs line "how many tokens"; the knob turns, tokens stack, the card comes out | docs |
| 4 | mechanism 2 | Seventeen times twenty-four. Low answered in three tokens. Max used forty-five. Both said four hundred eight. A seating puzzle: max spent two and a half times the tokens. Same name. | 30 | real run rows land one by one; SAME ANSWER, 2.5× | runs |
| 5 | turn (56 %) | But hard questions show the real trade. How many primes below two thousand have a prime digit sum? At low, two of three tries stopped with no number. | 28 | the question; the meter at low: two tiles, the card comes out red; the two real failed tries | runs |
| 6 | turn 2 | Max got it, one hundred fifty-six, after three minutes and twenty-three thousand tokens. Low's one good try took three thousand. | 20 | knob to max, the stack climbs while the counter runs to 22,780; LOW'S GOOD TRY 3,189; 7× | runs |
| 7 | payoff, loop | So higher isn't smarter, it's longer. Opus five point five defaults to medium. Start there, and turn it up only when the answer stops short. | 25 | docs table, the medium row marked; START ON MEDIUM; the meter at medium; comment prompt | docs |

Words: 167 (52.6 s take). Turn at 56 %. Loop: "...only when the answer stops short. Max effort cost Claude seven times the tokens..." Self-test: hook 12 words, names Claude and says "effort"; stake by 10 s (the assumption, with the dial); re-hooks at 9 s (smarter?), 20 s (numbers), 30 s (but), 39 s (156); no banned words; cut test dropped "and the API" and a line on xhigh's use case. In `plan.json`, `texts` carry digits as whisper heard them; `spoken` holds the text read.
