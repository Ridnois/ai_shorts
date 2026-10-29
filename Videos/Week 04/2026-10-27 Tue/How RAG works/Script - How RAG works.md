---
type: research
created: 2026-10-27
updated: 2026-10-27
status: v1 · 130 words, 7 scenes, take v1 38.9 s; first with Hairline figures
tags: [research, youtube, script, ai, rag, week-04]
---

# Script · How RAG works (Week 04, Tue 27 Oct)

← [[How RAG works - Status]] · [[YouTube Channel]] · [[Format]] · [[Growth]]

User (27 Oct 2026): *"generate a new short: how rag works"*; angle chosen in the clarifying round: **deeper mechanism**, one level below [[Script - RAG explained]] (that one: remembering vs reading). Series **How it works**. Named real case (§1 item 9): **Magesh et al., Stanford RegLab and HAI**, "Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools".

**Y:** know when an AI that "looks things up" can still be wrong. **X:** RAG fetches the passages nearest the question on a map of meaning, and nearest is not the same as right. **Theme line:** *nearest is not always right.* **Running example:** the benchmark query "moral wrong doctrine" (doctrine-test-177), which Lexis+ AI answered from a source on moral turpitude.

## 0. Facts bank (**read** = opened 27 Oct 2026)

| # | Fact | Source |
| --- | --- | --- |
| 1 | Preprint 23 May 2024 (HAI news), arXiv 30 May 2024 (adds Westlaw); peer-reviewed in J. Empirical Legal Studies 22 (2025) 216 to 242 | hai.stanford.edu (**read**); arXiv 2405.20362 (**read**); search excerpt (JELS) |
| 2 | Authors Magesh, Surani, Dahl, Suzgun, Manning, Ho | arXiv (**read**) |
| 3 | 202 preregistered legal queries, four categories | paper text (**read**) |
| 4 | Lexis+ AI and Ask Practical Law AI gave misleading or false answers on over 1 in 6 queries; Westlaw AI-Assisted Research on one third | paper §results (**read**) |
| 5 | Accurate answers: Lexis+ AI 65 %, Westlaw 41 %, Practical Law 19 % | paper (**read**) |
| 6 | The tools hallucinate less than GPT-4, which the paper also tested | paper (**read**) |
| 7 | LexisNexis 2023: "hallucination-free" linked legal citations; 2024: "100% hallucination-free linked legal citations" | paper intro and §2 (**read**, the 2023 line shot from arxiv.org/html) |
| 8 | Thomson Reuters 2023: "We avoid [hallucinations] by relying on the trusted content within Westlaw" | paper (**read**) |
| 9 | Naive retrieval: asked to define the "moral wrong doctrine", Lexis+ AI relies on a source defining moral turpitude, "seemingly similar but actually unrelated" | paper §naive retrieval (**read**, shot) |
| 10 | Another miss: Practical Law fetched motion-to-dismiss sources from bankruptcy and patent cases for a plane-crash negligence question | paper (**read**) |
| 11 | The paper's RAG diagram: the query is embedded, the retriever returns documents, the model writes from them; any step can add error | paper Fig. 3 (**read**) |
| 12 | One error traced to embedding similarity between "Judge Luther A. Wilgarten" and "judge" or "William Luther" | paper footnote (**read**) |
| 13 | RAG named by Lewis et al., arXiv 22 May 2020, NeurIPS 2020: a model plus "a dense vector index of Wikipedia" | arXiv 2005.11401 (**read**) |
| 14 | That index: the Dec 2018 Wikipedia cut into disjoint 100-word chunks, 21 million, one embedding each, FAISS search, top 5 or 10 fetched | paper §3 (**read**) |
| 15 | Over 25 federal judges had standing orders on AI use by May 2024 | HAI (**read**) |
| 16 | Legal answers are often contested and retrieved sources can be overruled or from the wrong court | paper §3.2 (**read**) |

Used on screen: 1, 4, 7, 9, 13, 14. Not claimed: how Lexis+ AI builds its index (not public).

## 1. Idea gate

**Scores:** surprise 4 · scale 4 · depth 5 · evidence 5 · showable 4 · plain 4. **Street-lamp:** pass: headlines give the 1-in-6 figure; none shows *why* a lookup tool misses (nearest on a map of meaning ≠ right), which this video shows on the study's own query. **Expert test:** the retrieval-miss mechanism is what the paper calls the interesting failure. **Against:** (1) "RAG again?" → a deeper mechanism, a new case; (2) "lawyers only" → anyone using chat-with-PDF tools hits the same miss; (3) "so RAG is useless?" → the paper finds it beats GPT-4, said in the description. **Demand check:** not run (token HTTP 400); "how does RAG work" is a common query (unmeasured).
**Five hooks:** stakes "Lawyers pay for AI that promises no made-up citations. Stanford caught it wrong one time in six." (**used**) · number "1 in 6 answers wrong, from AI that looks things up first." · question "If an AI looks up the answer, how can it still be wrong?" · contradiction "The AI read the right library and still picked the wrong page." · fact "Legal AI confused 'moral wrong' with 'moral turpitude'."

## 2. Package

- **Promise:** how RAG finds its sources, and why the nearest one can be wrong, on the query Stanford caught.
- **Titles:** *How RAG Works (and Why Legal AI Still Got It Wrong)* (recommended) · *RAG Explained: The Map That Picks the Wrong Page* · *AI That Looks Things Up Was Wrong 1 Time in 6*.
- **Thumbnail:** the riffle tray with one card pulled in rose; words "WRONG CARD". Beats neighbours: a real study and one picture, not a pipeline diagram.
- **Opening map:** scene 1 = the promise struck by the study; scene 2 = the definition and plan.

## 3. Script: 130 words, 7 scenes (take v1, rate 1.1: 38.9 s)

| Sc | Question it answers | Voice (exact text) | Visual beat (Hairline = HL) |
| --- | --- | --- | --- |
| 1 | (hook) | Lawyers pay for AI that promises no made-up citations. Stanford caught it wrong one time in six. It runs on RAG, and here is how it works. | scales + the real "hallucination-free" line on frame 1; HAI headline on "Stanford"; strike on "wrong"; card 17 % / 33 %; books "RAG" |
| 2 | what is RAG? | RAG means the AI looks things up first, then answers from what it found. | magnifier, answer balloon, page; card Lewis 2020 |
| 3 | looks up in what? | First, the library is cut into short passages, like cards. Each card gets a spot on a map of meaning. | HL riffle: the pointer runs the cards, one stands; card 21 million chunks; riffle shrinks, HL terrain grows (scale change) |
| 4 | how is one found? | Say a lawyer asks about the moral wrong doctrine. The question lands on the map, and the nearest cards rise. | the question drops onto the terrain; pillars rise round it on "nearest" |
| 5 | then what? | Those cards are pasted above the question, so the model answers from them. | HL stack: frames lift above the lit question layer; answer balloon |
| 6 | the catch (beat 0.2) | The catch: nearest is not always right. Lexis pulled a card on moral turpitude. Close words, different law. | the anchor returns: riffle pulls a rose card; "found: moral turpitude"; the paper's own passage |
| 7 | so what? | So RAG is only as good as the card it finds. Would you check its sources? Tell me. | riffle, the card in mint; comment prompt "Check its sources?" always · sometimes · never |
