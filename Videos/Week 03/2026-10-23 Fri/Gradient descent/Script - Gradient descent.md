---
type: research
created: 2026-10-23
updated: 2026-10-23
status: v1 · P1 to P4a done by delegation
tags: [research, youtube, script, ai, week-03]
---

# Script · Gradient descent (Week 03, Fri 23 Oct)

← [[Gradient descent - Status]] · [[YouTube Channel]] · [[Format]] · [[Growth]]

User (23 Oct 2026): *"Make a new video about gradient descend"*. Series: **How it works**.

**Y:** understand what "training" an AI actually means. **X:** a model learns nothing by rules; it nudges billions of numbers a small step downhill on its error, over and over (gradient descent, Cauchy 1847). **Theme line:** *less wrong, one small step at a time.* **One question:** how does an AI learn?

## 0. Facts bank (**read** = opened or quoted from the primary source, 23 Oct 2026)

| #   | Fact                                                                                                                                                                              | Source                                                                                                     |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| 1   | Cauchy proposed the gradient method in a note of 18 Oct 1847, *Comptes Rendus* 25, pp. 536 to 538                                                                                 | Lemaréchal, "Cauchy and the gradient method", Documenta Math. 2012 (search summary); RHUL scan of the note |
| 2   | Cauchy's motive was astronomy: computing the orbit of a celestial body from equations                                                                                             | Lemaréchal 2012 (search summary)                                                                           |
| 3   | The update moves the parameters a step length times the negative gradient                                                                                                         | de Klerk lecture slides 2026; any optimization text                                                        |
| 4   | Llama 3 405B was pre-trained with AdamW, peak learning rate 8e-5, linear warm-up over 8,000 steps, cosine decay to 8e-7 over 1,200,000 steps                                      | Meta, *The Llama 3 Herd of Models*, arXiv 2407.21783, July 2024 (**read**, quoted)                         |
| 5   | Its batch grew from 4M to 8M (after about 252M tokens) to 16M tokens (after 2.87T) for stability, then efficiency                                                                 | same (**read**)                                                                                            |
| 6   | Pre-training corpus about 15.6T tokens; about 3.8e25 FLOPs                                                                                                                        | secondary summaries of the same paper (**not checked in the paper**)                                       |
| 7   | GPT-3 175B: batch 3.2M tokens, learning rate 0.6e-4, 300B tokens                                                                                                                  | Brown et al., arXiv 2005.14165, Table 2.1 (via a wiki reproduction; not used)                              |
| 8   | In high dimensions saddle points, not bad local minima, are the main obstacle for gradient methods                                                                                | Dauphin et al., NeurIPS 2014, arXiv 1406.2572 (abstract **read**; not used)                                |
| 9   | Stochastic approximation (the root of "stochastic" gradient descent): Robbins and Monro, 1951                                                                                     | textbook reference (**not opened**; not used)                                                              |
| 10  | Backpropagation computes all the gradients in one backward pass: Rumelhart, Hinton, Williams, *Nature* 1986                                                                       | textbook reference (**not opened**; not used)                                                              |
| 11  | Adam optimizer: Kingma and Ba, 2014; AdamW (decoupled weight decay): Loshchilov and Hutter, 2017                                                                                  | textbook reference (**not opened**; not used)                                                              |
| 12  | A language model's error is cross-entropy on the next token: the less probability it gave the right word, the higher the score                                                    | standard; not cited on screen                                                                              |
| 13  | Learning rate too large: the iterates overshoot and can diverge; too small: progress is slow. On f(x) = x², x ← x(1 − 2·lr), so lr above 1 diverges                               | derived (the plate draws this exact map)                                                                   |
| 14  | A model starts from random weights                                                                                                                                                | standard practice                                                                                          |
| 15  | **Derived:** Llama 3 405B's steps from fact 5 and fact 6: about 63 thousand at 4M + 330 thousand at 8M + 800 thousand at 16M = about 1.2 million, matching the schedule in fact 4 | own synthesis (rests on fact 6)                                                                            |

## 1. Idea gate

**Scores:** surprise 4 (1847 math trains today's chatbots) · scale 4 (405 billion numbers, a million steps) · depth 4 · evidence 4 · showable 5 (the landscape is a real function, the ball runs real descent) · plain 4. **Street-lamp:** pass, not borderline: the headline "AI is trained" says nothing about how; the video adds the mechanism (error as height, feel the slope, step) and the step-size trade-off. **Expert test:** the step-size trade-off and the scale of one step (every number nudged at once) are the interesting part. **Coffee test:** *"AI learns by being a little less wrong, one step downhill at a time, a trick from 1847."* **Against the idea:** (1) "3Blue1Brown already did it" → 60 s, plain, with today's scale; (2) "too mathy" → no formula in the voice; (3) "so what?" → the close asks whether that is understanding. Scores kept.
**Demand check: not run** (`youtube_search.py` returns HTTP 400 on this machine, 23 Oct 2026). Indirect: "gradient descent" is a core term in every machine-learning course. Unverified: autocomplete, comparable Shorts. **Series:** How it works, the same as the previous video (rotation rule broken at the user's request). Not compact (165 words).
**Five hooks:** surprising fact (**used**) "The idea that trains every AI chatbot dates from eighteen forty-seven." · contradiction "Nobody teaches an AI anything. It just rolls downhill." · stakes "Every answer a chatbot gives came from a billion tiny corrections." · number "Over a million small steps built one AI model." · question-free claim "AI learns by being a little less wrong, a million times." **Hook test (used):** plain (no term) · reason to care (a broken expectation: modern AI, 1847 math) · opens "what idea?", answered in scene 2 · sound-off (caption 1847 over the ball stepping downhill) · honest (the video names and shows the idea) · matches the package.

## 2. Package

- **Promise:** every AI chatbot learns with an idea from 1847, gradient descent, and you will see how it works in a minute.
- **Titles:** *How AI Actually Learns: An Idea From 1847* (recommended, 41 characters) · *Gradient Descent Explained in 60 Seconds* · *Every Chatbot Learns by Walking Downhill*.
- **Thumbnail (at P8):** the 3D landscape with the copper ball and its trail of steps into the valley; words "MATH FROM 1847". Beats neighbours (equations on whiteboards, robot heads) by showing the mechanism itself.
- **Opening map:** scene 1 promise · scene 2 proof (Cauchy, named method) and plan (theme line).

## 3. Script: 165 words, 8 scenes

| Sc | Voice text | Delivery and pause |
| --- | --- | --- |
| 1 | The idea that trains every AI chatbot dates from eighteen forty-seven. | plain, intrigued |
| 2 | Augustin Cauchy used it to work out orbits. We call it gradient descent: learning by being less wrong, one small step at a time. | warm, the theme line slower |
| 3 | Here is how. A new model is billions of random numbers. It guesses the next word, and a score says how wrong it was. | steady, explaining |
| 4 | So picture that score as a landscape: each spot is one setting of the numbers, and height is the error. | calm, visual |
| 5 | But the model cannot see the map. It feels the slope where it stands, steps a little downhill, and checks again. | quiet, step by step |
| 6 | That is why the step size matters. Too big, it jumps the valley. Too small, training never ends. | brisk, a little amused |
| 7 | Meta's biggest Llama has four hundred five billion numbers. Over a million steps nudged every one of them. | weight on the numbers |
| 8 | So here is the point: AI does not learn rules. It learns by being a little less wrong, a million times. Is that understanding? Tell me what you think. | slower on the point; `break` 0.2 after "times" |

**Honesty:** "every AI chatbot": today's chatbots are neural networks trained with gradient-based optimizers (AdamW is gradient descent with momentum and per-number step sizes; the voice says "the idea", not "the same formula"). "Over a million steps" = fact 4 (schedule) and fact 15 (derived). "Every one of them": AdamW updates all weights each step. "A score says how wrong" = cross-entropy, simplified. The landscape is a 2-number picture of a billion-number space: marked schematic. Facts used: 5 (Cauchy 1847, random start and error, slope and step, step size, Llama scale). Cut test: saddle points, Adam, backprop cut.

## 4. Beat sheet, prefix `gd` (3D = `scene3d.py`, 2D = `motion.py`)

1 3D hook: the landscape, the copper ball already stepping downhill with its trail, "1847" in 3D · 2 Cauchy lithograph (Smithsonian, public domain), move to the face, context card · 3 3D at "gradient": closer, a fresh ball steps on "step" · 4 2D at "Here": a block of random numbers, then "The cat sat on the" with the guess *moon*, the error bar fills on "score" (values illustrative) · 5 3D at "So": the landscape rises from flat on "landscape", a marker on "spot", a height line on "height" · 6 3D at "But": close on the ball, downhill arrow on "slope", steps from "steps" · 7 2D at "That": two parabolas, a real zigzag that diverges (lr 1.05) on "big", a crawl (lr 0.03) on "small" · 8 2D at "Meta's": 405 billion counter, then about 1.2 million steps counter, source line · 9 3D at "So": the ball at rest in the valley, camera pulls back, conclusion card · 10 2D at "Is": an error curve falling over steps, margin note with the question.
**Schematic:** the landscape is an invented 2-D function (two wells and a bowl) but the ball's path is real gradient descent on it; the error curve (plate 10) is illustrative.

## 5. Not verified

The 15.6T tokens (secondary); the derived step count rests on it; the GPT-3 row (wiki); Cauchy's motive (summary of Lemaréchal); demand; how the voice sounds; caption timing. P7 is the user's.
