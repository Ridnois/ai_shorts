---
type: research
created: 2026-10-26
updated: 2026-10-26
status: v1 · 138 words, 6 scenes, take v1 41.8 s; first of the short test block, first with phrase captions
tags: [research, youtube, script, ai, rag, week-04]
---

# Script · RAG explained (Week 04, Mon 26 Oct)

← [[RAG explained - Status]] · [[YouTube Channel]] · [[Playbook]] · [[Audience]]

User (26 Oct 2026): *"build a new short, this one about rag explained to newbies"*. Series: **How it works**. Named real case (§1 item 9): **Moffatt v. Air Canada**.

**Y:** know why some chatbots can be trusted with facts and others make things up. **X:** a plain chatbot answers from what it absorbed in training; RAG makes it look up the real document first and answer from it. **Theme line:** *remembering vs reading.* **Running example:** the funeral-discount question to the airline's chat.

## 0. Facts bank (**read** = opened 26 Oct 2026; others from search excerpts)

| # | Fact | Source |
| --- | --- | --- |
| 1 | Moffatt v. Air Canada, 2024 BCCRT 149, decided 14 Feb 2024 by tribunal member Christopher Rivers | Manatt (**read**); CRT decision page (403) |
| 2 | Nov 2022: Jake Moffatt asked Air Canada's chatbot about bereavement fares after his grandmother died | Manatt (**read**) |
| 3 | The chatbot said he could claim the bereavement fare after travel, within 90 days of the ticket's issue | Manatt (**read**); Loyalty Lobby |
| 4 | The airline's policy did not allow bereavement claims after travel | Loyalty Lobby; Fox Business |
| 5 | Air Canada argued the chatbot was a separate legal entity; the tribunal rejected it: the airline answers for all information on its site | DailyHive; Manatt |
| 6 | Ordered: CA$650.88 (fare difference) + CA$36.14 interest + CA$125 fees, about CA$812 | Loyalty Lobby; Fox Business |
| 7 | RAG = retrieval-augmented generation; Lewis et al., arXiv 22 May 2020, NeurIPS 2020 | arxiv.org/abs/2005.11401; NeurIPS proceedings |
| 8 | The paper pairs a model's "parametric memory" with a "non-parametric memory": a vector index of Wikipedia searched by a neural retriever | paper abstract |
| 9 | Stanford RegLab and HAI (May 2024): Lexis+ AI, Westlaw AI-Assisted Research and Ask Practical Law AI hallucinated on 17 to 33 % of 200+ legal queries | reglab.stanford.edu; hai.stanford.edu (HAI gives Westlaw over 34 %) |
| 10 | LexisNexis disputed the Stanford figures (its own data shows a much lower rate) | Law360; HAI |
| 11 | RAG pipelines split documents into chunks, embed them as vectors and fetch the nearest chunks to the question | general description of the method (no figure) |
| 12 | The fetched text is placed in the prompt with the question; the model answers from it and can cite it | Lewis et al.; general method |
| 13 | A retrieval miss (the wrong chunk) gives a fluent answer grounded in the wrong text | Stanford RegLab study (failure analysis) |
| 14 | Since 31 Mar 2025 a Shorts view counts every play or replay | [[Playbook]] §0 research (shortimize) |
| 15 | Company help-desk bots and "chat with your PDF" tools are the most common RAG products | general (no figure) |

Used on screen: 1, 3, 4, 6, 7, 9. Not claimed: how Air Canada's chatbot was built.

## 1. Idea gate

**Scores:** surprise 4 · scale 4 · depth 4 · evidence 4 · showable 5 · plain 5. **Street-lamp:** pass: headlines tell the case or define the acronym; few show the retrieval step on one question. **Against:** (1) "RAG is for developers" → the question is one any traveller asks; (2) "old news" → the case is the hook, the mechanism is current; (3) "so RAG fixes it?" → the catch scene and the Stanford card. **Demand check:** not run (`youtube_search.py` token, HTTP 400); "what is RAG" is a common beginner query (unmeasured).
**Five hooks:** stakes "Air Canada's chatbot invented a refund rule, and a tribunal made the airline pay." (**used**) · question "Why do some chatbots cite their sources?" · contradiction "The smartest chatbot still can't read your company's rules, unless it uses RAG." · fact "Most company chatbots don't answer from memory. They search first." · number "CA$812: the price of a chatbot that guessed."

## 2. Package

- **Promise:** what RAG is, shown on the question that cost Air Canada a tribunal case.
- **Titles:** *RAG Explained: Why Chatbots Look Things Up* (recommended) · *Air Canada's Chatbot Made Up a Rule. RAG Is the Fix.* · *What Is RAG? AI Explained for Beginners*.
- **Thumbnail:** the chat bubble "Yes, within 90 days" stamped in rose; words "IT GUESSED". Beats neighbours: a real case, not a diagram.

## 3. Script: 138 words, 6 scenes (take v1, rate 1.1: 41.8 s)

| Sc | Question it answers | Voice (exact text) | Visual beat |
| --- | --- | --- | --- |
| 1 | (hook) | Air Canada's chatbot invented a refund rule, and a tribunal made the airline pay. The usual fix has a name: RAG. Here is how it works. | the chat with the wrong answer on frame 1; the stamp "airline pays CA$812" on "tribunal"; RAG tile on its word |
| 2 | what is it? | RAG means the bot looks up the real document first. Then it answers from what it just read. | bot, line to the document, line to "answers from it"; card Lewis 2020 |
| 3 | how does it look up? | Say a passenger asks: can I get the funeral discount after I fly? A search finds the matching paragraph in the airline's policy. | six policy pages, a scan beam, "Bereavement fares" lights mint, its paragraph lifts out |
| 4 | then what? | That paragraph is pasted into the prompt, above the question. So the model is not guessing from memory. It is reading, and it can point to the page. (beat 0.3) | the prompt fills: paragraph above question; the right answer with "source: policy page" |
| 5 | the catch | The catch: it is only as good as what it finds. The wrong page gives a confident wrong answer. | the beam lights "Refunds" in rose; a wrong answer with a citation; card Stanford 2024 |
| 6 | so what? | So here is the point. RAG turns a chatbot from remembering into reading. Would you trust a bot that shows its source? Tell me. | "remembering" struck, "reading" in mint; conclusion card, margin note |

**Honesty:** the chat lines are paraphrased and marked; the policy paragraph is a paraphrase of the reported policy; the "Refunds page" mistake is illustrative.

## 4. Not verified

The decision text itself (CRT and CanLII returned 403); the chatbot's exact words; demand. How the voice sounds. P7 is the user's.
