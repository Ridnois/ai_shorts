---
type: script
updated: 2026-10-30
series: What's coming
words: 170
---

# Script: ETH is false

Status: [[ETH is false - Status]] · rules: [[Format]] §3 · idea: [[ETH is false]]

## Research (30 Oct 2026)

1. **The paper:** OpenAI, *The Exponential Time Hypothesis is False*, 67 pages, "Date: 17 October 2026, revised 25 October 2026"; folder dated 25 Oct 2026; author "OpenAI"; github.com/openai/math, commit 26 Oct 2026 20:35 UTC. Read in full for the claim: Theorem 1.1, a deterministic algorithm that counts the satisfying assignments of any k-CNF in (n+m)^O(1) · 2^O(n log log n / √log n) time and polynomial space; abstract: "Our algorithm refutes the Exponential Time Hypothesis (ETH)". It also claims to refute SETH, Gap-ETH, NSETH and #ETH (§1.1.1 to 1.1.2). (captured)
2. **Its own limit:** "our result does not imply that general NP problems admit subexponential time algorithms" (p. 2). No implementation or experiment in the paper; the bound hides constants (O_k(1), o(1)). (captured)
3. **Who wrote it:** README: "produced by an unnamed internal OpenAI model"; about three hours of ChatGPT Pro thinking per result; 721 manuscripts; "~42% top-line results formalized"; "Some of the unformalized results could have issues." (captured)
4. **Lean:** `lean/formalization.yaml` lists `OAI.Algorithms.SubexponentialSAT.SqrtLogSpace.exact_count_and_sat` in `OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean`: a machine counts SAT solutions within `runtimeBound` time and polynomial space (read 30 Oct 2026).
5. **ETH:** Impagliazzo and Paturi, *On the Complexity of k-SAT*, JCSS 62(2), 2001, as cited by the paper [IP01] (captured). Best known 3-SAT bound cited in the paper: randomized O*(1.307031578^n), Jiang and Cai preprint 2026 [JC26].
6. **Review:** XenoSpectrum (27 Oct 2026) reports an open letter in which Impagliazzo, Paturi and Ryan Williams lead the verification and write "Our involvement should not be taken as a guarantee that this claim is correct"; other outlets (Kingy, AICoder, 26 to 27 Oct 2026) report the same group and an OpenAI-funded conference.
7. 2^100 = 1,267,650,600,228,229,401,496,703,205,376 (Python).

**Not verified:** the open letter itself (seen only through press; one outlet quotes it); whether the Lean statement matches ETH (the reviewers' question); any mathematical step of the proof (not checked here).

## Package

- **Promise:** what the Exponential Time Hypothesis is, what OpenAI's paper claims, and why it is not proven yet.
- **Titles:** **The Exponential Time Hypothesis Is False? OpenAI's Claim Explained** ← · An AI Says a Law of Computing Is Wrong · ETH Explained: OpenAI's 67-Page Claim, Under Review
- **Frame 0:** AN OPENAI MODEL SAYS: over the paper's real title, IS FALSE boxed. **Thumbnail:** the title sheet, "ETH IS FALSE?".
- **Hooks:** claim ← "An OpenAI model says the Exponential Time Hypothesis is false." · number "A hundred switches: a million trillion trillion settings." · contradiction "The people checking this proof made the rule it breaks."

## Scenes

| # | Beat | Voice (as read) | Words | Viewer sees happen | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | hook | An OpenAI model says the Exponential Time Hypothesis is false. | 10 | the paper's title, IS FALSE boxed | paper |
| 2 | stake | That's a decades-old bet that whole fields of computer science lean on. It's about one puzzle. | 16 | Anatomy `switchboard` arrives, lamps flash | paper §1.1.3 |
| 3 | mechanism | A row of switches, and rules like: switch three on, or switch seven off. Find a setting where every rule holds. | 21 | switches 4 to 8 appear; 3 flips on, lamp 1 green; the search flips switches until all three lamps are green | |
| 4 | mechanism 2 | Every new switch doubles the settings. A hundred switches: a million trillion trillion. Tricks slow it down, but it still explodes. | 21 | Hairline `doubling`: columns double, counter 2 to 512; 2^100 in full; BEST TRICK ×1.307 | Python, paper [JC26] |
| 5 | the bet | In 2001, Impagliazzo and Paturi bet it always will. That bet is the Exponential Time Hypothesis. | 16 | the paper's own [IP01] reference, phrase by phrase | paper |
| 6 | claim | OpenAI's sixty-seven page paper claims a method whose cost grows slower than any steady doubling, once the puzzle is big enough. | 21 | the abstract's "refutes the Exponential Time Hypothesis (ETH)"; the front row (claim) stays low; SHAPE ONLY | paper |
| 7 | turn (62 %) | But hard problems don't become easy. The cost still explodes, just slower, and the paper says it doesn't carry over to every hard problem. | 24 | the claim row still climbs; the paper's "does not imply" lines | paper p. 2 |
| 8 | turn 2 | It isn't confirmed yet, even with a machine-checked proof. Impagliazzo and Paturi are checking it now, and wrote their involvement is no guarantee it's correct. | 25 | README "unnamed internal OpenAI model"; the Lean statement; the names; "NO GUARANTEE" | README, Lean, press |
| 9 | payoff, loop | So don't share it as proven or wrong. Until they finish, the headline is only this: | 16 | PROVEN and WRONG struck, UNDER REVIEW; the title returns | |

Words: 170 (56.5 s take). Turn at 62 %. Loop: "...the headline is only this: An OpenAI model says the Exponential Time Hypothesis is false." For a viewer new to the problem: the puzzle is shown before any term, ETH is named only after the doubling is seen, and "subexponential" is said as "grows slower than any steady doubling". Cut test dropped "and the paper reports no run on a real computer" (kept in the caveats) and the 25-year figure (ETH dates to 1999 or 2001 by venue). In `plan.json`, `texts` carry digits as whisper heard them; `spoken` holds the text read.
