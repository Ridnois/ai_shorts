---
type: video-idea
status: review
series: How AI works
hook_pattern: name-it
medium: primitive
score: 16
publish: 
video: "[[Jev explained - Status]]"
created: 2026-11-05
updated: 2026-11-05
tags: [youtube, pipeline]
---

# Jev answers with odds, not words

← [[Pipeline]] · [[Strategy]] §The idea passes

**Claim:** Jev, TypeSafe AI's model, never writes a word: you give it typed questions and it hands back probabilities your code can act on, plus a confidence that says when to call a human.

**Real thing:** TypeSafe AI, Jev, limited early access 15 Sep 2026 with a US$40 M seed led by DCVC (Wikipedia "Jev (AI model)", read 5 Nov 2026). Docs (docs.typesafe.ai, read 5 Nov 2026): Choice, Score, Noul, Box questions; the quickstart's raw response from `jev-1.13.0` on a support ticket (technical 1.0, frustration score 0.67 with confidence 0.5, urgent 0.99). Case study on typesafe.ai: Jack & Jill cut candidate screening costs 88 % (vendor claim).

**Y · X:** to know which AI to use for a yes/no decision in software · a chatbot generates text one token at a time and has no built-in "I'm not sure"; Jev scores a fixed answer set in one pass and its spread is the uncertainty.

**Hook pattern:** `name-it`: a new term at its spike.

**Demand:** [[Radar]] 3 Nov 2026: IBM Technology "What Is Jev? The AI Model That Doesn't Generate Text" 1,266,965 views, 29.9x; Two Minute Papers "Yes, Jev Is Insane, But There's A Catch" 292,685, 2.3x; IBM "The Problem with Jev: Can You Trust AI Decisions?" 130,195, 3.1x.

**Own fit:** `name-it` 195 engaged (n=1) and How AI works 631 (n=7), both below our median: lead with the real output, not the concept.

**Score:** demand 5 (one at 29.9x) · own fit 1 · showable 5 (the `probs` primitive with Jev's real numbers shows the whole mechanism) · real thing 5 (named, dated, a number) = **16**.
