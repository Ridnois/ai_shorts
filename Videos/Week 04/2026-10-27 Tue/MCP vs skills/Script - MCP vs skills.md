---
type: research
created: 2026-10-27
updated: 2026-10-27
status: v3 · refocused on Agent Skills (user, 27 Oct 2026); 117 words, 6 scenes, take v3 34.5 s
tags: [research, youtube, script, ai, agents, week-04]
---

# Script · AI agent skills explained (Week 04, Tue 27 Oct; folder name MCP vs skills)

← [[MCP vs skills - Status]] · [[YouTube Channel]] · [[Format]] · [[Growth]]

User (27 Oct 2026): *"New short: explain the diference between an mcp and skill …"*, then on r3: *"Refocus the video. ai agent skills explained. make it more dynamic. more engaging"*. Series: **How it works**. Real case: Anthropic's `slack-gif-creator` skill (anthropics/skills), shown with its real folder, header and rules.

**Y:** teach your agent a new job. **X:** a skill is a folder the agent reads in two steps: only the short description at the start, the whole file when a task matches it. **Theme line:** *a manual your agent opens only when the job shows up.* **Running example:** the `slack-gif-creator` skill and a request for a birthday GIF.

## 0. Facts bank (**read** = opened 27 Oct 2026)

| # | Fact | Source |
| --- | --- | --- |
| 1 | MCP announced 25 Nov 2024: "an open standard … secure, two-way connections" between data sources and AI tools; servers and clients | anthropic.com/news/model-context-protocol (**read**) |
| 2 | First servers: Google Drive, Slack, GitHub, Git, Postgres, Puppeteer | same (**read**) |
| 3 | 9 Dec 2025: MCP donated to the Agentic AI Foundation (Linux Foundation); over 10,000 active public servers, 97M+ monthly SDK downloads; used by ChatGPT, Cursor, Gemini, Copilot, VS Code | anthropic.com/news/donating-the-model-context-protocol… (**read**) |
| 4 | Agent Skills announced 16 Oct 2025: "a folder containing instructions, scripts, and resources" loaded when a task calls for them | claude.com/blog/skills (**read**) |
| 5 | Progressive disclosure: at startup only `name` and `description` of every skill enter the system prompt; full `SKILL.md` when relevant; more files only as needed | anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (**read**) |
| 6 | Bundled context is "effectively unbounded" | same (**read**) |
| 7 | Agent Skills is an open standard (agentskills.io), three stages: discovery, activation, execution | agentskills.io (**read**) |
| 8 | Skills in Claude apps (Pro, Max, Team, Enterprise), Claude Code (`~/.claude/skills`, plugins), API (`/v1/skills`) | claude.com/blog/skills (**read**) |
| 9 | anthropics/skills holds 19 example skills (algorithmic-art, slack-gif-creator, skill-creator, mcp-builder, docx, pdf …); 184k stars | GitHub API and README (**read**) |
| 10 | `slack-gif-creator`: description 36 words, `SKILL.md` 1,103 words plus a `core/` code folder; Slack emoji GIF 128×128, message GIF 480×480 | raw SKILL.md (**read**) |
| 11 | BlenderMCP: "control Blender 3D with any LLM"; runs Python in a live session, imports Poly Haven and Sketchfab assets; 32.5k stars; example prompt "a low poly scene in a dungeon, with a dragon guarding a pot of gold" | github.com/ahujasid/blender-mcp (**read**) |
| 12 | GhidraMCP lets LLMs "autonomously reverse engineer applications": decompile, rename methods, list imports and exports; 11.6k stars | github.com/LaurieWired/GhidraMCP (**read**) |
| 13 | `caveman` skill (Julius Brussee): "Terse caveman voice: answer first, fluff gone, every technical fact kept"; 628-word SKILL.md | ~/.claude plugin files, github.com/JuliusBrussee/caveman |
| 14 | This session: `claude mcp list` shows 4 connected servers (Claude Docs, Google Drive, Google Calendar, Gmail) | our run, 27 Oct 2026 |
| 15 | Anthropic's own `mcp-builder` is a skill that teaches the agent to build MCP servers | anthropics/skills (**read**) |

On screen (v3): 4, 5, 7, 9, 10. **Original synthesis:** 100 skills with a 36-word description take 3,600 words, about the room of three full `slack-gif-creator` files (3 x 1,103 = 3,309).

## 1. Idea gate

**Scores:** surprise 4 · scale 4 · depth 4 · evidence 5 · showable 4 · plain 5. **Street-lamp:** pass (the announcement says skills load "when needed"; the video shows the two-step read on a real file and measures what 100 skills cost). **Against:** (1) "Claude-only" → open standard (agentskills.io); (2) "jargon" → a folder and a text file; (3) "so what" → teach your own agent a job. **Demand:** autocomplete "claude skills", "agent skills", "mcp vs claude skills" (27 Oct 2026); outliers not checked (token HTTP 400).
**Five hooks:** fact "Claude can learn a new job from one text file." (**used**) · question "How does Claude learn a job it was never trained for?" · number "A hundred skills take the room of three." · contradiction "Your agent has a manual it does not read." · stakes "Your agent can do your team's job your way, from one file."
**History:** r1 and r2 (a list, "hands vs know-how") were "a plain comparison table"; r3 (MCP vs skill as a story) was refocused by the user on skills alone and asked to be more dynamic. Rules edited: [[Format]] (old Playbook §2) *A comparison is a story*, §3 event every 1.5 to 2 s and one scale change per world.

## 2. Package

- **Promise:** how an AI agent learns a new job from a skill, shown on a real one.
- **Titles:** *AI Agent Skills Explained: How Claude Learns a New Job* (recommended) · *What Are Claude Skills? One File, One New Job* · *Agent Skills: The Manual Your AI Reads on Demand*.
- **Thumbnail:** a scroll flying into the agent, "+1 JOB".
- **Opening map:** scene 1 = promise; scene 2 = definition (folder); scenes 3 to 5 = proof on the real skill.

## 3. Script: 117 words, 6 scenes (take v3, rate 1.1: 34.5 s)

| Sc | Question | Voice (exact text) | Pause | Visual beat (scale change) |
| --- | --- | --- | --- | --- |
| 1 | (hook) | Claude can learn a new job from one text file. It's called a skill, and here is how it works. | natural | Claude settles; a text file flies into it (shrinks into the agent); "+1 job"; card |
| 2 | what is it? | A skill is a folder. Inside, one text file of instructions, and sometimes a few scripts. | natural | folder grows, then the camera zooms into it; instructions, scripts; real folder tree lights |
| 3 | how does it read it? | Take Anthropic's Slack GIF skill. The top of its file is a short description, thirty-six words. That's all Claude reads at the start. | natural | the real header builds; description lit; counter 0 to 36; the rest fades in dim, "read later" |
| 4 | why does it matter? | So a hundred skills like it take about the room of three full ones. | 0.2 s beat | 100 scrolls pop in; the grid collapses beside 3 full files; card 100 x 36 = 3,600 |
| 5 | when does it read the rest? | Now ask for a birthday GIF. The description matches, so Claude opens the whole file: one hundred twenty-eight pixels, under three seconds, forty-eight colors. | natural | ask, cake, check "description matches"; the rules panel springs open; each rule lights on its number; GIF frame 128 x 128 |
| 6 | close | That's a skill: a manual your agent opens only when the job shows up. What job would you teach yours? | natural | agent and its manual (anchor returns); mint card; comment prompt |

**Honesty:** no recorded run (running the skill's downloaded code was blocked by the auto-mode classifier, 27 Oct 2026); the rules shown are the file's real text; "a hundred skills like it" assumes descriptions of about 36 words.

## 4. Not verified

How the voice says "Claude" and the numbers; outlier demand. P7 is the user's.
