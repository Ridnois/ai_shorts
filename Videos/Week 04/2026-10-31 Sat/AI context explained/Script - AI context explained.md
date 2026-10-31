---
type: script
updated: 2026-10-31
series: How AI works
words: 165
---

# Script: AI context explained

Status: [[AI context explained - Status]] · rules: [[Format]] §3

## Research (31 Oct 2026)

1. **Recorded runs**, 31 Oct 2026 01:41 (-03), `claude -p --model claude-opus-5-5 --effort low --tools ""` (Claude Code 2.1.314), system prompt "You are a helpful assistant. Answer in one short sentence.", in a clean folder outside the vault; log, script and JSONs in `Media/…/run/` (`README.md`, `turn.sh`). "Input tokens" = `input_tokens` + `cache_read_input_tokens` + `cache_creation_input_tokens` (all count toward the window, Anthropic docs).
2. Same session (`--resume`): "Hi, I'm Sam. My dog is called Pixel." **618** · "What should I feed a puppy?" **654** · "How often should I walk her?" **741** · "What's my dog's name?" **838** → "Your dog's name is Pixel."
3. New session, same question: **605** tokens → "I don't know your dog's name, since you haven't told me". Sam and Pixel are made up.
4. New session with a one-line `CLAUDE.md` ("The user is Sam. Sam's dog is called Pixel.") loaded: **817** tokens → "Your dog's name is Pixel." (the +212 includes Claude Code's wrapper around the file, not only the note).
5. Anthropic, *Context windows*, platform.claude.com, read 31 Oct 2026 (captured): input phase "Contains all previous conversation history plus the current user message"; "working memory"; "context rot"; Claude Opus 5.5 has a 1M-token window; claude.ai "can also manage the context window on a rolling 'first in, first out' basis".
6. OpenAI, *Conversation state*, developers.openai.com, read 31 Oct 2026 (captured): "each text generation request is independent and stateless".
7. Claude Code, *How Claude remembers your project*, code.claude.com, read 31 Oct 2026: "Each Claude Code session begins with a fresh context window"; CLAUDE.md and auto memory are "loaded at the start of every conversation".
8. Liu et al., *Lost in the Middle: How Language Models Use Long Contexts*, arXiv 2307.03172 v3 (20 Nov 2023), Stanford, UC Berkeley, Samaya AI. GPT-3.5-Turbo (0613), 20 documents (about 4K tokens): answer in position 1 **75.8 %**, position 10 **53.8 %**, position 20 **63.2 %**; closed book **56.1 %** (Table 1, Table 6, Figure 1, captured from the PDF).

**Not verified:** the ChatGPT app's own context handling (it may trim or summarize long chats); the claim rests on OpenAI's API docs and the measured Claude runs. A 2023 test on GPT-3.5; newer models were not re-tested here.

## Package

- **Promise:** how a chatbot "remembers" you, shown on a real run.
- **Titles:** **How AI Remembers: The Context Window Explained** ← · ChatGPT Doesn't Remember You (It Rereads Everything) · AI Memory Explained: Why Long Chats Get Worse
- **Frame 0:** CHATGPT DOESN'T REMEMBER YOU over the context reader mid-read. **Thumbnail:** the reader, "AI REREADS EVERYTHING".
- **Hooks:** fact ← "ChatGPT doesn't remember you. Every message, it rereads your whole chat." · number "Claude read 618 tokens to answer 9 words." · contradiction "A longer chat makes AI forget more, not less."

## Scenes

| # | Beat | Voice (as read) | Words | Viewer sees happen | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | hook | ChatGPT doesn't remember you. Every message, it rereads your whole chat. | 11 | Anatomy `context-reader`: the head sweeps every slip; OpenAI docs crop "independent and stateless" | 6 |
| 2 | stake | That chat is the context window, and I watched it grow. I told Claude Opus five point five: I'm Sam, my dog is Pixel. | 24 | the tray fills and empties; the real command and prompt; the first slip lands | 1 |
| 3 | mechanism | Claude read six hundred eighteen tokens. Next question, six hundred fifty-four. Then seven hundred forty-one. Each turn, the whole chat goes back in. | 23 | counter 618, 654, 741 as slips land and the head rereads all of them; docs crop "Contains all previous conversation history" | 2, 5 |
| 4 | mechanism 2 | So I asked my dog's name. Pixel. It didn't recall it, it read it again. A new chat, same question: it doesn't know. | 23 | real outputs; the first slip lights as the head passes it; the tray empties for the new chat | 2, 3 |
| 5 | mechanism 3 | And the memory feature? A note. One line in Claude Code's memory file, and a new chat said Pixel. The note is pasted in first. | 25 | the real memory file; the yellow note drops into the holder; the head reads it before the question | 4, 7 |
| 6 | turn (64 %) | But a longer chat isn't a better memory. Stanford gave G P T three point five twenty documents. With the answer in the middle, it scored fifty-four percent, below its score with no documents at all. | 36 | Hairline `window`; the paper's title and Figure 1, the middle ringed red, the closed-book line ringed | 8 |
| 7 | payoff, loop | So put what matters first or last, and start a new chat when it gets long, because it only knows what you send. | 23 | the middle slips fade, the first lights; the tray empties for a new chat, one slip, one sweep | 5, 8 |

Words: 165 (49.8 s take, 51.5 s video). Turn at 64 %. Loop: "...it only knows what you send. ChatGPT doesn't remember you..." Self-test: hook 11 words, names ChatGPT, "remember" in the first sentence and "context window" by 6 s; stake by 10 s (the real run); re-hooks at 12 s (numbers), 21 s (the name), 28 s (memory), 35 s (but), 42 s (54 %); no banned words. Cut test dropped a line on the 1M-token window and the claude.ai first-in-first-out note. Whisper heard "asked" as "ask"; `plan.json` `texts` carry digits as heard, `spoken` holds the text read.
