---
type: research
created: 2026-10-23
updated: 2026-10-23
status: v1 · P1 to P4a done by delegation; rendered r1, waiting for the user (P7)
tags: [research, youtube, script, ai, week-03]
---

# Script · AI invented sources (Week 03, Fri 23 Oct)

← [[AI invented sources - Status]] · [[YouTube Channel]] · [[Playbook]] · [[Audience]]

User (23 Oct 2026): *"lets generate the video of the idea 'Why AI Invents Sources (and How to Catch It in 5 Seconds)'"*.

**Y:** use AI answers without citing something that does not exist. **X:** a language model predicts plausible text, it does not look sources up, and most tests reward a confident guess over "I do not know". **Theme line:** *no match, no trust.* **One question:** how do you catch an invented source fast?

## 0. Facts bank (**read** = opened 23 Oct 2026 via search or fetch; not every page opened in full)

| # | Fact | Source |
| --- | --- | --- |
| 1 | Mata v. Avianca (S.D.N.Y.), Judge P. Kevin Castel: lawyers filed a brief citing cases that did not exist, produced by ChatGPT | Wikipedia, *Mata v. Avianca, Inc.* (**read**) |
| 2 | The order of 4 May 2023 said at least six of the cited cases appeared bogus, with bogus quotes and citations | search summary of the order and press (**not opened in full**) |
| 3 | Fake cases included Varghese v. China Southern Airlines, Shaboon v. Egyptair, Martinez v. Delta Air Lines | same (**not opened in full**) |
| 4 | ChatGPT assured the lawyers the cases "indeed exist" and could be found on LexisNexis and Westlaw | Wikipedia (**read**) |
| 5 | $5,000 fine; the infobox date is 22 June 2023; the lawyers also had to write to the judges named in the fake opinions | Wikipedia (**read**); search summary |
| 6 | Damien Charlotin's database of AI hallucinations in court filings: about 1,600 examples in 35 countries by June 2026 (crowd-sourced, so not definitive); over 1,000 by March 2026 | AFP via Malay Mail, June 2026; UNC Law Library, June 2026 (**search summaries**) |
| 7 | OpenAI, "Why language models hallucinate" (Sept 2025): most evaluations reward guessing; a model guessing a birthday has a 1 in 365 chance, "I don't know" scores zero | openai.com (**search summary, post not opened in full**) |
| 8 | Walters and Wilder, *Scientific Reports*, Sept 2023: 55 % of GPT-3.5 and 18 % of GPT-4 citations were fabricated (636 citations, 42 topics); often real author names with invented titles | NCBI PMC10484980 (**search summary**); not used on screen |
| 9 | GPTZero found 100 hallucinated citations in 51 NeurIPS 2025 papers (Fortune says 53) | GPTZero, Fortune (**search summary**; commercial source); not used |

## 1. Idea gate

**Scores:** surprise 4 · scale 4 · depth 3 · evidence 4 · showable 4 · plain 5 (thread ≥ 4 on surprise, scale, plain). **Street-lamp:** pass, not borderline: the headline is "AI makes up sources"; the video adds the mechanism (predicts plausible text; tests reward guessing) and a concrete 5-second action. **Expert test:** the reward-for-guessing finding and "a citation is easy to imitate" are the interesting part. **Coffee test:** *"AI invents sources, and one quoted search catches it."* **Against the idea:** (1) "everyone knows AI hallucinates" → the video gives the fix and the why; (2) "a search is not proof" → stated as no match, no trust, not as proof of fakery (below); (3) lawyers only → the check works for any title. Scores kept.
**Demand check: not run** (`youtube_search.py` token returns HTTP 400 on this machine, 23 Oct 2026). Indirect evidence only: the Mata case was widely reported and the tracker grew from about 100 entries (2025) to about 1,600 (mid 2026). Unverified: search autocomplete and comparable Shorts. **Topic family:** software and AI (new for the channel; the last videos were grid, energy, software). Not compact (153 words).
**Five hooks:** surprising fact (**used**) "AI will invent a source, then swear it is real." · stakes "A lawyer was fined for citing cases that never existed." · contradiction "The citation looks perfect. The paper does not exist." · question-free number "One tracker lists over a thousand court filings with invented citations." · consequence "One search catches most invented sources in five seconds." **Hook test (used):** plain (10 words, no term) · reason to care (a source you may cite) · open "how, and why?" · sound-off (caption INVENT/REAL over the AI answer card) · honest (the video shows the check) · matches the package.

## 2. Package

- **Promise:** AI invents sources and swears they are real, and a quoted search of the exact title catches it in seconds.
- **Titles:** *Why AI Invents Sources (and How to Catch It in 5 Seconds)* (user's idea title, 62 characters, recommended) · *The 5-Second Check for Fake AI Citations* · *A Lawyer Cited Cases ChatGPT Invented*.
- **Thumbnail (not built; at P8):** an AI answer card with a citation and an orange NO MATCH stamp, 3 words max.
- **Opening map:** scene 1 promise and proof (Mata) · scene 2 why · scene 4 the check.

## 3. Script: 153 words heard, 5 scenes (take v1: 52.5 s, about 175 wpm)

| Sc | Voice text | Delivery and pause |
| --- | --- | --- |
| 1 | AI will invent a source, then swear it is real. In twenty twenty-three, New York lawyers filed court cases ChatGPT had invented. A judge fined them. | plain, intrigued; natural pauses |
| 2 | It happens because AI does not look sources up. It predicts the words that probably come next, and a citation is easy to imitate: names, a title, a year. And most tests reward a confident guess over an honest, I do not know. | steady, explaining |
| 3 | So this is not rare. A public tracker now lists over one thousand court filings with invented citations. | a little grave |
| 4 | Here is the five second check. Copy the exact title, put it in quotes, and search it. A real source shows up with the same authors. An invented one shows nothing, or a different paper. | brisk, clear |
| 5 | So here is the point: no match means do not trust it, however real it sounds. Should a chatbot be allowed to cite anything it cannot link? Tell me what you think. | slower on the point; `break` 0.2 before the question |

**Honesty:** "swear it is real" = fact 4 (ChatGPT assured they exist); "a judge fined them" = fact 5 (lawyers and firm); "over one thousand" is under every count in fact 6. The check is a **strong signal, not proof**: a real but paywalled, very new or differently titled source can return nothing, and a model can attach real authors to an invented title (fact 8), so the rule is "no match, do not trust", and the video says "same authors". Facts used: 5 (Mata, mechanism, incentive, tracker, check). Cut test: Walters (fact 8) and NeurIPS (fact 9) cut.

## 4. Beat sheet: 10 motion plates, prefix `ai`, no photo or footage (swap test: generic screens add nothing)

1 chat answer card with the citation, tick on "real" · 2 the filing: three fake cases stamped FAKE, a $5,000 counter · 3 "does not look up": arrow to the source, crossed out · 4 next-word bars (schematic, illustrative) then names, title, year labelled on a citation · 5 the scoring: guess 1 in 365 vs "I do not know" 0 · 6 1,000 dots fill, counter · 7 search bar with the quoted title, 5 s countdown · 8 real result (same title, authors, tick) vs invented (0 results) · 9 0 results, DO NOT TRUST IT, card "No match, no trust" · 10 AI answer with "link: none", margin note.
**Schematic:** the next-word bars (plate 4) are illustrative, marked "schematic"; "Smith v. Jones, 2019" and the real-result card are examples, not real cases.

## 5. Not verified

Court order text and the Charlotin figures (read through search summaries and Wikipedia, not the primary pages); the OpenAI post wording; search demand; how the voice sounds; caption timing; the quoted-search check against real cases (not tested on this machine). P7 is the user's.
