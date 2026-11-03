---
type: script
updated: 2026-11-03
series: How AI works
words: 163
---

# Script: AI attention explained

Status: [[AI attention explained - Status]] · rules: [[Story]] §Beats

## Research (3 Nov 2026)

1. **Recorded run**, 3 Nov 2026, `bert-base-uncased` (Devlin et al., Google, arXiv 1810.04805, 2018) with transformers 5.22.1 and torch 2.15.0 (CPU), eager attention, in `Media/…/run/` (`dump.py`, `attention.json`). Sentences: "The trophy doesn't fit in the suitcase because it is too big." and the same ending "too small." (a Winograd-style pair, Levesque et al. 2012).
2. Attention from the token "it", averaged over all 12 layers x 12 heads (144): `[SEP]` end marker **23.1 %** (big) / 22.7 % (small); trophy **6.0 %** / **6.1 %**; suitcase **4.3 %** / 4.4 %. Each head's row sums to 1 (softmax).
3. Trophy-minus-suitcase gap per head, big vs small: median |change| **0.0016** (0.16 points), max 0.061 (layer 4, head 10); the preferred noun flips in **7 of 144** heads, each by a small margin.
4. Vaswani et al., *Attention Is All You Need*, arXiv 1706.03762 (12 Jun 2017): a network "based solely on attention mechanisms".
5. Jain and Wallace, *Attention is not Explanation*, NAACL 2019, arXiv 1902.10186 (26 Feb 2019): different attention distributions can yield the same predictions.

**Not verified:** BERT is a bidirectional encoder; chatbots such as ChatGPT use a decoder that looks only backward, with the same attention math. No ChatGPT weights are public. One sentence pair and one small model; the finding is about this probe, not all models. Whether BERT resolves "it" correctly was not tested.

## Package

- **Titles:** **How AI Attention Works (And Why It Isn't an Explanation)** ← · How ChatGPT Knows What "It" Means · Attention Explained on a Real Model
- **Frame 0:** TO READ "IT", CHECK EVERY WORD over the sentence with lines from "it" to each word.
- **Hooks:** fact ← "To read the word it, ChatGPT pays attention to every other word." · number "A word-less end marker got 23 % of the attention." · contradiction "Change one word and AI's attention barely moves."

## Scenes

| # | Beat | Voice (as read) | Words | Viewer sees happen | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | hook | To read the word it, ChatGPT pays attention to every other word. | 12 | the sentence; "it" lights, lines reach every word | 4 |
| 2 | stake | Take this sentence: the trophy doesn't fit in the suitcase because it is too big. Which one is it? | 19 | trophy and suitcase swell as the question lands | 1 |
| 3 | mechanism | I ran Google's BERT on it. Every word scores every other word, and the scores add to a hundred percent. Averaged over its hundred forty-four heads, it gave twenty-three percent to the end marker, six to trophy, four to suitcase. | 40 | recorded weights: bars from "it" fill; 144 head dots; the 23 % bar on the end marker | 1, 2 |
| 4 | mechanism 2 | Then each word becomes a blend of the others, mixed by those scores. | 13 | "it" fills with trophy and suitcase colour in those proportions | 2 |
| 5 | turn (about 60 %) | Now change one word: big becomes small. For you, the answer flips to the suitcase. But the scores barely move. Trophy was six percent, then six percent again. The typical head's trophy-suitcase gap moved under two tenths of a point. | 39 | big becomes small; the human answer flips to suitcase; the 144 dots barely shift | 1, 3 |
| 6 | turn 2 | So attention shows where a model looked, not why it answered. A twenty nineteen paper found different scores can give the same answer. | 23 | Jain and Wallace title crop; two different bars, one answer | 5 |
| 7 | payoff, loop | So treat it as a clue, never a reason. Looking at every word is not understanding them. | 17 | the lines fade to one lit word | 5 |

Words 163 (49.0 s take, 50.3 s video). Loop: "...not understanding them. To read the word it, ChatGPT..." Self-test: hook 12 words, names ChatGPT, "attention" in the first sentence; re-hooks at 6 s (question), 14 s (23 %), 30 s (change one word), 38 s (but); no banned openers. Stake is thin (the question carries it); QA to judge.
