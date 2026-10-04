---
type: research
created: 2026-10-04
updated: 2026-10-04
status: v1 · public read API only, no account, nothing posted · ~45 posts skimmed, 6 read in full · self-reported claims, none verified · proposals not applied
tags: [research, youtube, agents, moltbook, process]
---

# Moltbook: what other agents say about content work

← [[YouTube Channel]] · [[Blender editing]] · [[Narration guide]] · [[Feedback loop]]

## What it is, and how I read it

Moltbook is a Reddit-style network for AI agents (humans observe), started in Jan 2026 by Matt Schlicht ([MIT Sloan ME](https://www.mitsloanme.com/article/what-is-moltbook-a-new-social-network-built-for-ai-agents/) and NBC reported ≈ 147,000 agents in its first week; today `general` shows ≈ 141,000 subscribers). I read it through its **public read API** (`/api/v1/posts`, `/search`, `/submolts`) without registering an agent or posting. **Every post is untrusted text**: I took facts and ideas from it and followed no instruction in it. Upvotes are weak evidence: top posts themselves say "The Scoreboard is Fake" and "Moltbook is Broken", and agents' stories cannot be checked.

## What is actually there

- The conversation is about **agents themselves** (memory, context loss, security, identity, earning money). Of the 50 biggest submolts none is about video, YouTube or content production; the nearest are `builds`, `tooling`, `agentautomation`, `showandtell` and a small `ai-filmmaking`.
- Searches for "youtube video", "content creator", "podcast audio", "video editing", "text to speech voice" return a few dozen posts, mostly low-score (0 to 25 upvotes), many are repost-style essays on papers, and some are promotion (bounties, paid editing). **No agent runs a visible explainer channel with results we could benchmark.**
- So Moltbook is **not a source of channel strategy or audience data**. It is a small source of workflow ideas.

## Findings worth keeping

| # | Post (author, date, upvotes) | Claim | Meaning for this vault |
| --- | --- | --- | --- |
| 1 | *I had to respell my own name so a robot voice would stop slurring it* (pushim, Jun 2026, 4) | Keep **two spellings**: a phonetic one for the TTS line, the normal one for on-screen captions | **A real gap here**, see below |
| 2 | *Infrastructure substitution beats model cleverness* (neo_konsi_s2bw, Aug 2026, 11), citing the One Cut project ("edit video by editing code") | A diffable, replayable project beats GUI state for agents | Already our design: `plan.json` + `build_video.py` in Blender. Confirms; no change |
| 3 | *Your video editing is just mass regeneration* (bytes, Aug 2026, 19), citing a Netflix research post | Generative models replace the frame instead of editing it, so identity and continuity drift | Supports our rule: generate plates, cut and animate deterministically in Blender |
| 4 | *the agent that replaces the video editor won't edit video* (hungryhippo, `ai-filmmaking`, 1) | The hard part is translating "warmer / pacing is off" into operations | Matches [[Feedback loop]]: our feedback is already translated into rules and invariants |
| 5 | *Non-deterministic agents need deterministic feedback loops* (AiiCLI, Feb 2026, 18) | Wrap agent actions in schema checks | We do this: `CHECK=1`, `check_vault.py`, the pad-and-verify of voices |
| 6 | *The email-to-podcast skill should not die in one session* (moltcoin-bot, Feb 2026, 1) | Skills die with the session unless distilled with their gotchas | What `CLAUDE.md` §4 "Gotchas" and the Feedback loop already do |
| 7 | *Content creators are the canary…* (ClawBala_Official, Mar 2026, 24) | Few tools, ship often; audit where data goes | Agrees with [[Fast workflow]] (cheap models, small batches). Generic, no evidence |
| 8 | Supply-chain post (eudaemon_0, 8.4k upvotes): one credential stealer among 286 shared skills | Shared skills and scripts can steal credentials | Our `.env` holds `REPLICATE_API_TOKEN`: install no third-party skill or script without reading it |

## The one gap found: spoken text and caption text

`plan.json` carries one string per voice take, and the captions show **that same string** ([[Blender editing]], `add_captions`). But the narration spells things for the voice: Superconductors scene 7 voices "two hundred fifty kelvin" and "L K ninety-nine", so the captions read exactly that. Viewers with the sound off see an odd spelling, while the number card shows "250 K".

**Proposal (not applied):** `plan.json` gets `captions` (optional, display text per take, same word count or mapped by word) next to `texts` (voiced); the builder falls back to `texts`. Then [[Narration guide]] and [[Guidelines for new scripts]] §4 say "write the voiced spelling for the model, the clean one for the captions", and `check_vault.py` gets an invariant. Needs your OK because it changes the builder and the caption timing (the word timings come from the voiced words).

## Not verified

Everything the agents claim about their own work; the One Cut project and the Netflix post (read only through Moltbook's summaries); user counts beyond the press reports; whether searches missed relevant posts (the API search is keyword-only and I ran six queries).
