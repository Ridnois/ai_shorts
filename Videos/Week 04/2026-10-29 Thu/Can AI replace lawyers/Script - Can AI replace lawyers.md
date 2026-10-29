---
type: script
updated: 2026-10-29
series: How AI works
words: 168
---

# Script: Can AI replace lawyers

Status: [[Can AI replace lawyers - Status]] · rules: [[Format]] §3 · idea: [[Can AI replace lawyers]]

## Research (29 Oct 2026)

1. Damien Charlotin, *AI Hallucination Cases* database, read 29 Oct 2026: "2231 cases identified so far", "Last updated: 28 October 2026"; it tracks court or tribunal decisions on hallucinated content, not every fake citation. (captured)
2. Free Law Project, M. Lissner, 16 Apr 2024, *Combat Hallucinations and Look Up Citations with our New API*: "a guardrail for those that are using AI to generate legal content. Built on our database of nearly ten million citations". (captured)
3. Magesh, Surani, Dahl, Suzgun, Manning, Ho (Stanford, Yale), *Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools*, arXiv 30 May 2024, J. Empirical Legal Studies 22 (2025): Lexis+ AI and Westlaw AI-Assisted Research / Ask Practical Law AI "each hallucinate between 17% and 33% of the time" (tool versions tested in 2024; vendors dispute the method and report later releases). (captured)
4. SRA news release, 6 May 2025: Garfield.Law Ltd, the first purely AI-based firm authorised in England and Wales, guides businesses "through the small claims court process"; "The system will not be able to propose relevant case law, which is a high-risk area for large language model machine learning"; "not autonomous", steps only with client approval; "named regulated solicitors will still ultimately be accountable". (captured)
5. The example citation is the invented case in *Mata v. Avianca* (S.D.N.Y., 2023): "Varghese v. China Southern Airlines, 925 F.3d 1339 (11th Cir. 2019)"; shown once, as a pattern, not as the story.

**Not verified:** how often current (2026) versions of Lexis and Westlaw tools err; the narrator says "tested" in the past tense and the screen says 2024. "Legal orientation" (the user's term) is spoken as "guide you through a legal problem".

## Package

- **Promise:** why AI invents court cases, and what makes an AI legal guide safe to use.
- **Titles:** **Can AI Replace Lawyers? Why AI Invents Court Cases** ← · Why AI Makes Up Legal Citations (and the Fix) · The First AI Law Firm Isn't Allowed to Cite Case Law
- **Frame 0:** AI INVENTED LAW / 2,231 COURT CASES over the real database. **Thumbnail:** the citation card stamped red, AI INVENTS COURT CASES.
- **Hooks:** number ← "Courts have now caught AI inventing law in over two thousand two hundred cases." · contradiction "The first AI law firm isn't allowed to cite case law." · question-free fact "A citation is a pattern, so AI can write a perfect fake one."

## Scenes

| # | Beat | Voice (exact text as read) | Words | Viewer sees happen | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | hook | Courts have now caught AI inventing law in over two thousand two hundred cases. | 14 | the real database rows; 2,231 lands | Charlotin |
| 2 | stake | That's one researcher's count, updated this week. So can an AI agent guide you through a legal problem? | 18 | the count boxed, UPDATED 28 OCT 2026; Hairline `loop` (an agent: plan, act, check) | Charlotin |
| 3 | mechanism | A legal citation is a pattern: two names, a volume, a reporter, a page, a year. A model writes the likely next word, so it can build a perfect citation for a case that doesn't exist. | 37 | the citation built part by part on its word; Hairline `riffle` picks the next card; NO SUCH CASE | Mata v. Avianca (example) |
| 4 | fix | So fix one: the model never cites from memory. Free Law Project built a free tool that looks every citation up in millions of real ones. | 26 | Anatomy `citator`: the card goes in, drawers scan, the match found, green lamp; the real Free Law Project post | Free Law Project |
| 5 | turn (55 %) | But a lookup isn't enough. Stanford tested Lexis and Westlaw's AI tools, which search real cases first. They still made things up seventeen to thirty-three percent of the time. | 29 | red lamp, red stamp; the real paper, 17–33 % boxed | Stanford |
| 6 | payoff | So Garfield, England's first approved AI law firm, isn't allowed to propose case law at all. It guides small claims, and a named solicitor answers for it. | 28 | the real SRA release; the case-law line boxed; the solicitor line boxed; green ground | SRA |
| 7 | loop | So an agent can guide you, as long as every citation is checked. Otherwise, you join the list. | 16 | the green-stamped card; the database rows return; comment prompt | |

Words: 168 (51.4 s take). Turn at 55 %. Loop: "...you join the list. Courts have now caught AI inventing law..." Cut test: dropped the sanction amounts (a second story) and the "good law" check (a citator also checks whether a case was overruled; no room to show it).
