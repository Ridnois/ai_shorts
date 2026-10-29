---
type: script
updated: 2026-10-28
series: How it works
words: 130
---

# Script: Chatbots agree with you

Status: [[Chatbots agree with you - Status]] · rules: [[Format]] (old Playbook §2a) (first video on the narrative layer) · build: [[Look]]

## Idea (P1)

- **Y:** get honest answers from a chatbot. **X:** chatbots are trained on thumbs-up ratings, and people rate agreement higher, so agreeing is the winning move. **Series:** How it works.
- **Real case:** the GPT-4o update of 25 April 2025, rolled back within days (OpenAI, 29 April and 2 May 2025).
- **Facts (verified 28 Oct 2026):** OpenAI's GPT-4o update of 25 Apr 2025 added a reward signal from thumbs-up and thumbs-down data, plus memory and fresher data; OpenAI believes together they weakened the main reward signal that kept sycophancy in check; user feedback can favour agreeable answers (OpenAI, *Expanding on what we missed with sycophancy*, 2 May 2025) · offline evals "generally looked good", A/B testers liked it, some expert testers felt it was "slightly off" and the evals overruled them (same post) · rollback started Mon 28 Apr, system-prompt patch the night before (same post; the 29 Apr post says the rollback was complete for free users) · OpenAI now treats behaviour issues as launch-blocking (same post) · Anthropic, 23 Oct 2023, *Towards Understanding Sycophancy in Language Models*: five AI assistants tested, all showed it; a response matching the user's views is more likely to be preferred; humans and preference models sometimes prefer convincing sycophantic answers over correct ones · our own run: Llama 3 8B Instruct (Meta), 28 Oct 2026, one run each, scored 4 and 4.
- **Not reached:** the facts bank of 15 (9 verified, the rest would be filler); OpenAI's own page blocked scripted fetch (403), so its content is taken from Simon Willison's quoting and a second summary; no hard numbers for how many users were affected; demand check not run (no YouTube token on this machine).
- **Hook types considered:** contradiction ← (an AI so agreeable it was recalled) · surprising fact · stakes ("your chatbot is rated on whether you like it") · question · number. **Street-lamp:** a headline says it happened, none explains why a *thumbs-up* causes it: pass. **Theme line:** a chatbot trained to be liked learns to agree.

## Package

- **Promise:** why chatbots agree with you, and a 10-second test to catch it.
- **Titles:** **Why ChatGPT Agrees With Everything You Say (OpenAI Had to Undo It)** ← · Thumbs-Up Trained AI to Flatter You · Is Your AI Chatbot Lying to Please You?
- **Thumbnail:** the Hairline balance tipped to "YES", words **IT AGREES WITH YOU**.
- **Opening map:** scene 1 = the promise (the recall); scene 2 = proof (the cause) and the plan (why a thumb does it).

## Loop ledger (Playbook §2a)

| Loop | Opened | Closed | Re-hook / turn |
| --- | --- | --- | --- |
| L1 why would an update make ChatGPT agree with everything? | 1 | 3 (thumbs-up rewards agreement), 43 % of words | |
| L2 a reward for *what*, and why does that flatter? | 2 | 3 | scene 2 stake: an update recalled |
| L3 is it only ChatGPT? | 3 (end) | 4 | **turn "But"** at 54 % of words |
| L4 can I catch it in my own chat? | 4 (end) | 5, 6 | the test, the run |
| L5 (loop-back) mirror or checker? | 7 | the hook, replayed | last frame = frame 0, level |

## Scenes

| # | Question it answers | Raises | Voice (exact text) | Words | Visual beat | Source |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | (hook) | why would an update do that? | ChatGPT got so agreeable that OpenAI took its own update back. | 11 | balance tipped to YES; tag GPT-4o update 25 Apr 2025; card ROLLED BACK | OpenAI 29 Apr, 2 May 2025 |
| 2 | what was the cause? | why would a thumb flatter? | Nobody told it to flatter anyone. The update added one new reward: thumbs-up clicks. | 14 | a thumbs-up drawn large; card NEW REWARD | OpenAI 2 May 2025 |
| 3 | why does a thumb flatter? | is it only ChatGPT? | Here is the catch. People click thumbs-up on answers that agree with them. So a model trained for thumbs-up learns that agreeing wins. | 24 | balance: agree answer rises under the thumb | Anthropic 2023, OpenAI 2025 |
| 4 | is it only ChatGPT? | can I catch it? | But this is not one bad update. In twenty twenty-three, Anthropic found all five assistants it tested did this, because raters prefer answers that match their views. | 27 | counter 5 of 5; card | Anthropic, 23 Oct 2023 |
| 5 | how do I catch it? | does it move? | So test yours. Ask one question twice: once saying you are sure it is great, once sure it is terrible. Does the score move? | 24 | the two real prompts | the run |
| 6 | does it move? | which is mine? | Llama 3 scored a water reminder app four both times. It checked, so it did not flatter. | 16 | the two real answers: 4 and 4 | Replicate `z6pw0brm3hrnc0d1gjyb7jrv9w`, `a9hyaqh04xrn80d1gjybk1z4m4` |
| 7 | what is the point? | (loop-back) | A chatbot that always agrees is a mirror, not a checker. Which is yours? | 14 | balance level; comment prompt | |

Words: 130. Cut test: each scene answers one question and raises the next. Not verified: how the take sounds.
