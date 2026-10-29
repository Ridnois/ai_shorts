---
type: process
created: 2026-10-26
updated: 2026-10-26
status: v2 · rendered r2 (illustrated; r1 kept); waiting for the user (P7)
tags: [status, week-04]
---

# RAG explained · Status

← [[Script - RAG explained]] · [[YouTube Channel]] · [[Production]]

**Delegation (user, 26 Oct 2026):** *"Forget about the upload for now, build a new short, this one about rag explained to newbies"*. P1 to P7, cap **$0.06** (base about $0.05: one take $0.02, one retake $0.02, whisper $0.01). The user's "forget about the upload" overrides [[Production]] *Ship before you build* for this video. First video of the short test block and the first with phrase captions ([[Format]] (old Playbook §2), §4).

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research · 2 Script · 3 Visual plan | done (agent) | delegated 26 Oct 2026 | How it works · hook type: stakes (a real case) · theme line *remembering vs reading* · 138 words, 6 scenes · named real case: Moffatt v. Air Canada (§1 item 9) · street-lamp: pass (headlines tell the case, not how the fix works) · demand check: not run (`youtube_search.py` token, HTTP 400) |
| 4 Prompts, stock, budget | approved by delegation | 26 Oct 2026 | no stock, no generated media; all plates drawn in HyperFrames |
| 6 Generation | done | within the cap | Take v1 `pnm6egvpmdrmt0d1f94anwk1j8` (838 characters): 41.8 s, whisper `8wj3eep4wsrmt0d1f94bbqfy0r` heard all 138 words, silences 0.20 to 0.67 s, none inside a clause. Spend about **$0.03** |
| 7 Edit | done, **waiting for the user (P7)** | | `Media/Week 04/2026-10-26 Mon/RAG explained/render/rg-43s-9x16-r1.mp4` (43.1 s, HyperFrames 0.8.200, 2D). `System/scripts/check3d.mjs`: OVERLAPS 0, no WARN (four layout passes before render: stamp, beam, answers out of the caption band, "remembering" past x 950). `hyperframes check` passed. Mix −14.1 LUFS, true peak −1.8 dBTP. Final mp4 sheet looked at (`render/_sheet.jpg`). **Slideshow-risk score 3, pass:** repetition 0, decoration 0, weak motion 1 (the prompt holds about 3 s), text doing the picture's job 1 (chat and prompt are text by nature), no real thing on screen 1 (all drawn), unchanged world 0 |
| 7b Edit r2 (illustrations) | done, **waiting for the user (P7)** | | User on r1 (26 Oct 2026): *"Last render is 100% text, think on a way to improve illustration inside shorts and rerender"* (rule: [[Format]] (old Playbook §3) *Illustrate, do not typeset*, [[Look]] Illustrations). Same take and timing. Hook opens on a real photo of an Air Canada 787-9 (Commons, Adam Moreira, CC BY-SA 4.0) drifting, the chat drawn in a phone, scales and flying money on the verdict; Fluent Emoji 3D objects (MIT) for question, documents, magnifier, page, six pictured policy pages, memory, open book, paperclip source, warning. `render/rg-43s-9x16-r2.mp4` (43.1 s); `check3d.mjs` OVERLAPS 0, no WARN (now counts `.art` for fill); overflow of the scene-4 phone found on snapshots and fixed (the checker does not see overflow inside a box). Mix −14.1 LUFS, true peak −1.8 dBTP. Final mp4 sheet looked at (`render/_sheet_r2.jpg`). **Slideshow-risk score 1:** weak motion 1, all else 0. Spend unchanged (**$0.03**) |
| 8 Publish · 9 Measure | not now (user) | | |

*Schematics:* the chat, the policy pages, the retrieved paragraph and the prompt are drawn; the policy paragraph is a paraphrase of the page the tribunal cited, marked "paraphrased" on screen. No claim is made about how Air Canada's chatbot was built.

*Not verified:* the voice (whether "RAG" is said as a word); phrase-caption timing and the 45 % dimmed words in motion (first video with them); pace. Seen risks: each cut has a 0.4 s near-empty cross-fade; the chat anchor returns as an answer bubble, not the full chat window.
