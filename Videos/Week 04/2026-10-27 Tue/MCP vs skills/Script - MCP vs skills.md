---
type: research
created: 2026-10-27
updated: 2026-10-27
status: v2 · story rewrite (user, 27 Oct 2026: "just a plain comparison table"); 131 words, 5 scenes, take v2 38.9 s; not the compact slot (a narrative video, Playbook §2)
tags: [research, youtube, script, ai, agents, week-04]
---

# Script · MCP vs skills (Week 04, Tue 27 Oct)

← [[MCP vs skills - Status]] · [[YouTube Channel]] · [[Playbook]] · [[Audience]]

User (27 Oct 2026): *"New short: explain the diference between an mcp and skill and mention some examples. interesting less known usages, be creative"*. Series: **How it works** (the last video was Agent at work). Real case ([[Audience]] *Case sources*, real runs): this channel's own Claude Code session on 27 Oct 2026 (Claude Opus 5.5): four MCP servers connected and the `caveman` skill active.

**Y:** know which one to add when you want your agent to do more. **X:** an MCP adds an ability from outside (a server the agent calls); a skill adds know-how the agent reads only when the task needs it. **Theme line (the message):** *when your agent gets stuck, ask: can't reach it, or doesn't know how?* **Running example:** you ask Claude to post a birthday GIF in your team's Slack (illustrative scenario); it stops at Slack (reach: the Slack MCP, one of the first servers), then the GIF may break Slack's size rules (know-how: the real `slack-gif-creator` skill).

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

On screen: 1, 4, 5, 10 (the derived number), 11, 12, 13, 14. **Original synthesis:** a skill costs its description until used: 36 words carried vs 1,103 read on demand for `slack-gif-creator`, about 30 times less.

## 1. Idea gate

**Scores:** surprise 4 · scale 4 · depth 4 · evidence 5 · showable 4 · plain 5. **Street-lamp:** pass (docs define each alone; the video adds the diagnostic question and the measured one-line loading). **Against:** (1) "jargon" → one everyday task, two failures; (2) "a feature list" → a story with a message; (3) "Claude ad" → both are open standards (ChatGPT, Cursor, Gemini use MCP). **Demand:** autocomplete "mcp vs skills", "mcp vs claude skills", "mcp vs agent skill" (27 Oct 2026); outliers not checked (token HTTP 400).
**Five hooks:** stakes "Your AI agent gets stuck for two reasons. MCP and skills each fix one." (**used**) · question "Why can't Claude post in your Slack?" · contradiction "Claude knows Slack. It just can't touch it." · number "This skill costs Claude 36 words until it needs 1,103." · fact "Your agent can't fail at Slack until it can reach Slack."
**r1 and r2 (85 words, a list: hands vs know-how plus Blender, Ghidra, Slack GIFs, caveman) were rejected by the user:** a table of examples teaches no one; the rule is now [[Playbook]] §2 *A comparison is a story*. Blender, Ghidra and caveman moved to the pinned comment.

## 2. Package

- **Promise:** why your agent gets stuck, and which of the two fixes it needs.
- **Titles:** *MCP vs Skills: Why Your AI Agent Gets Stuck* (recommended) · *MCP or Skill? The One Question to Ask* · *Claude Can't Post in Slack: MCP vs Skills Explained*.
- **Thumbnail:** the stuck agent with a stop sign, plug and scroll below; "STUCK? 2 FIXES".
- **Opening map:** scene 1 = promise (two reasons, two fixes); scene 2 = the task (plan); scenes 3 and 4 = proof on that task.

## 3. Script: 131 words, 5 scenes (take v2, rate 1.1: 38.9 s)

| Sc | Question | Voice (exact text) | Pause | Visual beat |
| --- | --- | --- | --- | --- |
| 1 | (hook) | Your AI agent gets stuck for two reasons. MCP and skills each fix one. Here is how to tell which. | natural | agent settles; stop sign on "stuck"; plug on "MCP", scroll on "skills"; card |
| 2 | stuck how? | Say you ask Claude to post a birthday GIF in your team's Slack. It writes a nice message, then stops. | natural | Claude; cake, GIF, Slack in order; the message; stop sign on Slack |
| 3 | why stop? | Reason one: it can't reach Slack. An MCP is a plug between the agent and an app. Plug in Slack, and it can post. | natural | agent, brick wall, Slack; the unposted message; the wall becomes the plug; real `claude mcp list`; check on "post" |
| 4 | and then? | Reason two: it doesn't know Slack's rules, so the GIF may come out the wrong size. A skill is a folder of instructions. The agent keeps one line in mind, and reads the rest only when a GIF comes up. | 0.2 s beat before the close | GIF, ruler, Slack's real rule (128x128, under 3 s); folder, scroll; real `slack-gif-creator` header, description lit, counter 36 to 1,103 as the rest appears |
| 5 | so what do I do? | So when your agent gets stuck, ask: can't reach it, or doesn't know how? Reach needs an MCP. Know-how needs a skill. What is your agent missing? | natural | agent; plug "can't reach it?" then "add an MCP"; scroll "doesn't know how?" then "add a skill"; mint card; comment prompt |

**Honesty:** the birthday task is an illustrative scenario, not a recorded run; "may come out the wrong size" is hedged (the skill exists because Slack has these rules); the MCP list is our real session, which has no Slack plugged in.

## 4. Not verified

How the voice says "MCP" and "Ghidra"; outlier demand (token). P7 is the user's.
