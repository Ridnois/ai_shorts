---
type: script
updated: 2026-11-04
---

# Script: AI fails tax jobs

← [[AI fails tax jobs - Status]] · [[Story]] · [[Picture]] §Medium · idea [[AI agents fail 9 in 10 tax jobs]]

**Promise:** you will see how AI agents score on real tax work, where they slip, and why catching the trap is not the same as passing the job.
**Pattern:** `surprising-result` · **Series:** What's coming · **Main medium:** capture (Surge's page as marked crops, our recorded Claude Code runs).

## Package

| | |
| --- | --- |
| Title | Can AI Do Your Taxes? Claude Passed 1 in 10 Real Tax Jobs |
| Alternatives | AI Agents Fail 9 in 10 Real Tax Jobs · I Rebuilt the Tax Traps That Beat AI |
| Frame-0 text | 1 IN 10 TAX JOBS |
| Thumbnail | the three pass bars against the 95 % line · "1 IN 10" |
| Field (nearest outliers, `youtube_search.py "can ai do my taxes"`, 4 Nov 2026) | "Claude AI Did My Tax Prep In 5 Minutes" (183.7x); "Using AI to file your taxes? Expert warns against it" (103.1x); "ChatGPT for Bookkeeping and Taxes: What It Can't Know" (14.9x); "My Thoughts on Using AI to Do Your Taxes" (9.0x); "I Used An AI Tool To Do My Taxes – Here's Where Experts Say I Went Wrong" (3.4x). Ours gives the measured score, the two named traps and our own rerun; none of them has a number |

## Voice (exact text)

| Scene | Beat | Voice | Words | Viewer sees happen | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | Hook | Claude passed about one real tax job in ten. | 9 | three pass bars (10.8, 9.6, 9.2 %) with the 95 % bar far right; "1 IN 10" | Surge |
| 2 | Stake | Not quiz questions: fifty real jobs, each a folder of client records, up to a hundred and twenty three files. Nine in ten miss the bar. | 26 | file chips pile into a folder; the real crop "as many as 123"; the bars return | Surge |
| 3 | Case 1 | Here's where they slip. A client asks which closing date is better for her condo. One agent compared both dates, five times, and never noticed her tax break runs out in August twenty twenty-seven. | 34 | a timeline: moved out Aug 2024 · Oct 2026 · Jan 2027 · Aug 2027 cliff in red; crop "Astra never identified the deadline." | Surge |
| 4 | Case 2 | Claude caught that one. Its miss was a couple splitting up: all five times, it assumed they were never married, though their records hinted at a common-law marriage. | 28 | crop "Across all five attempts," "the couple was unmarried,"; evidence chips | Surge |
| 5 | Turn | So I rebuilt both traps and ran Claude Code five times each. It caught both. Ten out of ten. | 19 | our terminal: the real lines from runs; a 10/10 counter | our runs |
| 6 | Mechanism | That's the catch. My rebuilds were one short email and thirty tiny files. A real job is every calculation, the evidence, every issue and the finished return, and it only passes at ninety-five percent of the checklist. | 37 | our 30-file folder beside the real job's 123; the four criteria chips; crop "at least 95% of the task's criteria," | our runs, Surge |
| 7 | Payoff | So let it spot the issue, and keep a human on the return. | 13 | chips AI: SPOT THE ISSUE · HUMAN: THE RETURN; back to the frame-0 bars | – |

166 words. Turn at about 52 % (scene 5).

## Sources (checked 4 Nov 2026)

- **Surge AI, "DAYJOB: Tax"** (surgehq.ai/blog/dayjob-tax, 27 Oct 2026, read and captured 4 Nov 2026): 50 environments; "1,789 workspace files, with a median of 30 per assignment and as many as 123"; "We report pass@1 at a 95% rubric threshold. An attempt passes when it satisfies at least 95% of the task's criteria, which assess calculations, supporting evidence, consequential issues, and the completed deliverable."; "Claude Sonnet 5.5 leads with a 10.8% pass rate …, followed by Claude Fable 5.1 at 9.6% and Claude Opus 5.5 at 9.2%." Condo: the client moved out in August 2024, closing October 2026 or January 2027; eligibility lapses "around the end of August 2027"; "Across five attempts, Astra never identified the deadline. Opus identified it in all five attempts." Couple: "Across all five attempts, Opus based its recommendations around the assumption that the couple was unmarried"; records suggested a possible valid marriage (Texas or Colorado). No human baseline is reported.
- **Our runs** (`Media/…/AI fails tax jobs/run/`, 4 Nov 2026): Claude Code 2.1.318, `claude-opus-5-5`, on your plan. Condo, rebuilt as one email (`prompt.txt`), no tools, 5 runs: the August 2027 limit stated in 5 of 5 (run 5: "You need to close by about **August 2027**, 3 years after you moved out."). Couple, rebuilt as one email (`couple.txt`), 5 of 5 raised Texas common-law marriage; then as a 30-file folder (`folder/`, the clues in 3 files: lease, joint account, holiday card; the email says "We never married"), Read/Glob/Grep only, 5 of 5 raised it ("the Austin records suggest Jordan and Sam may have a Texas common-law marriage"). The rebuilds are ours, from the post's descriptions, not Surge's files.

*Not verified:* the Astra model's maker and version (the post gives none). Why our rebuilds pass where the benchmark fails is our reading (size and the 95 % bar), not tested; the benchmark files are not public.

## Beat sheet (spine: the three pass bars)

Borrowed: **frame 0 = the whole system plus the number** ([[ByteByteGo - 1 trillion messages]]): the bars and "1 IN 10" at 0 s. **The contradiction is one frame** ([[3Blue1Brown - The medical test paradox]]): "10/10" in our runs next to "1 in 10" on the real jobs (scene 6).

Transitions: push, whip, cut, dip, blur, cut. Builder `hf/gen_beats.py`.
