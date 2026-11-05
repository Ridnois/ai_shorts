---
type: script
updated: 2026-11-05
---

# Script: Jev explained

← [[Jev explained - Status]] · [[Story]] · [[Picture]] §Medium · idea [[Jev answers with odds, not words]]

**Promise:** you will see what Jev returns instead of text, why that helps software, where its "I'm not sure" comes from, and what it is used for.
**Pattern:** `name-it` · **Series:** How AI works · **Main medium:** primitive (`probs` bars with Jev's real numbers from TypeSafe's docs), plus docs phrase crops and the real JSON response in a labelled panel.

## Package

| | |
| --- | --- |
| Title | What Is Jev? The AI That Never Writes a Word |
| Alternatives | Jev Explained: AI That Answers With Odds · Why Jev Doesn't Generate Text |
| Frame-0 text | NEVER WRITES A WORD |
| Thumbnail | Jev's real ticket answer as bars (technical 100 %) · "NEVER WRITES A WORD" |
| Field ([[Radar]], 3 Nov 2026) | IBM "What Is Jev? The AI Model That Doesn't Generate Text" (29.9x); Two Minute Papers "Yes, Jev Is Insane, But There's A Catch" (2.3x); IBM "The Problem with Jev: Can You Trust AI Decisions?" (3.1x); bycloud "What Is Yann LeCun Cooking? JEPA Explained Simply" (2.4x); IBM "New frontier AI models, TypeSafe's Jev AI…" (0.7x). Ours is the 50-second version that shows the real answer and the confidence turn; the IBM one is 15 min |

## Voice (exact text)

| Scene | Beat | Voice | Words | Viewer sees happen | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | Hook | Jev is the AI that never writes a single word back. | 11 | Jev's ticket answer as bars, "technical" lights; tag TYPESAFE JEV · 15 SEP 2026 | Wikipedia, docs |
| 2 | Stake | Ask ChatGPT to sort a support ticket, and it writes a paragraph your code has to guess at. Jev hands back numbers. | 22 | a recreated chatbot paragraph types in and is struck; Jev's `"choice"` and `"noul"` lines land | docs |
| 3 | Mechanism 1 | Take one ticket: our A P I is failing, and we can't process orders. You don't ask Jev for a reply. You ask three typed questions: which team, how angry, how urgent. | 30 | the docs' example ticket; chips CHOICE: TEAM? · SCORE: ANGRY? · NOUL: URGENT? light in turn | docs quickstart |
| 4 | Mechanism 2 | A chatbot builds its answer one token at a time. Jev scores every option in one pass. Technical team, one hundred percent. Urgent, ninety-nine. | 24 | token chips arrive one by one; below, all three bars fill at once; then the urgent bars, 99 % | docs (jev-1.13.0) |
| 5 | Turn | But the useful part is when it's unsure. On anger, it split: sixty-seven percent frustrated, thirty-three calm. So its confidence drops to one half, and your code can hand that one to a person. | 34 | frustration bars 67/33; the real JSON (`"confidence": 0.5` marked); crops "is a useful signal", "Route to a human" | docs quickstart, confidence |
| 6 | Use cases | That's what it's built for: routing tickets, screening job applicants, flagging refunds. One hiring startup says it cut screening costs by eighty-eight percent. | 23 | three job chips; cost bars 100 % → 12 %; tag TYPESAFE CASE STUDY | docs, typesafe.ai |
| 7 | Payoff | So let the chatbot write, and let Jev decide, because a decision doesn't need words. | 15 | back to the frame-0 bars, "LET JEV DECIDE" | – |

159 words. Turn at 55 % (scene 5). The last line reads into the first ("…doesn't need words. Jev is the AI that never writes a single word back").

## Sources (checked 5 Nov 2026)

- **Wikipedia, "Jev (AI model)"** (read 5 Nov 2026): TypeSafe AI (San Francisco, founded 2024); limited early access 15 Sep 2026 with a US$40 M seed led by DCVC; discriminative model returning typed values with probabilities; question types noul, choice, score; confidence for choice is (p_max − 1/n)/(1 − 1/n); speed and cost figures are self-reported.
- **docs.typesafe.ai** (read and cropped 5 Nov 2026): System One page, "returns typed decisions and probabilities rather than generated text"; quickstart example ticket ("Our API integration started returning 500 errors on every request…") and its raw response from `jev-1.13.0`: department technical 1.0 (billing 0, sales 0), frustration score 0.67 with probabilities 0: 0.33, 1: 0.67 and confidence 0.5, is_urgent noul 0.99 ("These are example results; values can change between Jev releases"). Confidence page: "'I don't know' is a useful signal", "Route to a human"; the docs' own use cases: ticket routing, refund requests.
- **typesafe.ai** (read 5 Nov 2026): case study "How Jack & Jill Cut Candidate Screening Costs By 88% With Jev" (vendor claim, not independently checked).

*Not verified:* the 88 % (TypeSafe's own case study); whether Jev is accurate on any ticket outside the docs' example (we made no API call: no key). The JSON on screen is the docs' published response, not our run. "Jack & Jill" is described in the voice as "one hiring startup" from the case-study summary.

## Beat sheet (spine: the department bars)

Borrowed: **frame 0 = the whole system plus the number** ([[ByteByteGo - 1 trillion messages]]): Jev's full answer as bars at 0 s. **The contradiction is one frame** ([[3Blue1Brown - The medical test paradox]]): token chips arriving one by one above bars that fill at once (scene 4).

Transitions: push, whip, cut, dip (the turn), blur, cut. Importance 3: scene 4 (one pass) and scene 5 (confidence). Acted-out word: "split" (the bars split 67/33). Sound: kit defaults plus the first default music bed (`mix_audio.py`). Builder: `hf/beats.json`.

## Self-test

159 words ✓ · hook 11 words, `name-it`, "Jev" + "AI" spoken in sentence 1 ✓ · sentences 2–3 carry no date, name or institution (the date is a tag on screen) ✓ · one running example (the docs' ticket) ✓ · turn at 55 % ✓ · loop ending ✓ · no banned words ✓ · cut test: dropped a "zero hallucinations" line (vendor claim, can't show it) and a price line (40–400x, self-reported).
