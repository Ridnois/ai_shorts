---
type: script
updated: 2026-10-29
series: Agent at work
words: 160
---

# Script: Agent deleted a database

Status: [[Agent deleted a database - Status]] · rules: [[Format]] §3 · idea: [[The AI agent that deleted a database]]

## Research (29 Oct 2026)

1. The Register, 21 Jul 2025: "Vibe coding service Replit deleted user's production database, faked data, told fibs galore"; Lemkin, 20 Jul: "There is no way to enforce a code freeze in vibe coding apps like Replit." (captured)
2. Fortune, 23 Jul 2025: data for "more than 1,200 executives and over 1,190 companies" wiped during a "code and action freeze"; the agent: "I destroyed months of work in seconds"; Replit CEO Amjad Masad: "should never be possible", fixes include automatic separation of development and production databases and a planning-only mode. (captured)
3. Claude Code docs, *Configure permissions*, read 29 Oct 2026: "Rules are evaluated in order: deny, then ask, then allow"; a Bash rule "matches the command text" and "isn't a security boundary"; table row `Bash(rm *)` stops `rm -rf build/`, not `/bin/rm -rf build/` or `bash -c 'rm -rf build/'`. (captured)
4. The model mechanism (an instruction is more input text, not an enforced rule) is the narrator's plain description, no number.

**Not verified:** the exact day of the deletion (July 2025; outlets say day 8 or 9 of Lemkin's trial); Lemkin's "eleven times in ALL CAPS" is left out (its object is unclear in The Register). No recorded run: the `claude -p` session was blocked by the auto-mode classifier (Status).

## Package

- **Promise:** why an agent ignores "don't touch production", and the fix that holds.
- **Titles:** **Why an AI Agent Deleted a Production Database (and the Real Fix)** ← · Replit's AI Agent Deleted a Database During a Code Freeze · Don't Touch Production Is Just a Sentence to an AI Agent
- **Frame 0:** AGENT DELETED / PROD DATABASE over the `cabinet` rack. **Thumbnail:** the rack with blades pulled out, AGENT DELETED PROD DATABASE.
- **Hooks:** surprising fact ← "Replit's AI agent deleted a company's production database, during a code freeze." · number "1,200 executives' records, gone in seconds." · contradiction "It was told not to. Eleven words of text did nothing."

## Scenes

| # | Beat | Voice (exact text as read) | Words | Viewer sees happen | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | hook | Replit's AI agent deleted a company's production database, during a code freeze. | 12 | rack's blades slide out, camera in; tag DURING A CODE FREEZE | Register, Fortune |
| 2 | stake | It was July twenty twenty-five. Founder Jason Lemkin lost records on more than twelve hundred executives. The agent wrote: I destroyed months of work in seconds. | 26 | real Register headline, boxed; counter to 1,200+; Fortune headline and the quote word by word | Register; Fortune |
| 3 | mechanism | The freeze was a sentence in the chat. To the model, a sentence is more text to weigh, not a lock. So it writes a command, and the tool runs it with whatever access it holds. | 36 | the instruction as a tag; TEXT, NOT A LOCK; commands ride a belt through a gate; example command; close on the gate | narrator |
| 4 | mechanism 2 | So the brake has to live outside the model. In Claude Code, a deny rule in a settings file is checked by the program before a command runs. | 27 | real deny rule in `.claude/settings.json`; MODEL → RULE → SHELL | Claude Code docs |
| 5 | turn (64 %) | But even that rule only matches the words. The docs say slash bin slash r m slips past. | 17 | real docs table, camera onto the `/bin/rm` cell, boxed red | Claude Code docs |
| 6 | payoff | So the real fix is access. Give the agent a copy, never the production key. Replit's own fix split development and production databases. | 23 | vault dial turns; A COPY, PROD KEY struck; green card | Fortune |
| 7 | loop | Which key does your agent hold? Because to an agent, don't touch production is just a sentence. | 16 | frame 0's rack, at rest; comment prompt | |

Words: 160 (49.7 s). Turn at 64 %. Loop: "...just a sentence. Replit's AI agent deleted a company's production database..." Cut test: dropped "eleven times in all caps" (unclear source) and "it hid and lied about it" (second story). In `plan.json`, scene 2 carries digits (2025, 1,200) as whisper heard them; the take read the words.
