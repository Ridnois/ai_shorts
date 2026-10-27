---
type: research
created: 2026-10-27
updated: 2026-10-27
status: v1 · 85 words, 4 scenes; third of the short test block, so the compact slot (60 to 85)
tags: [research, youtube, script, ai, agents, week-04]
---

# Script · MCP vs skills (Week 04, Tue 27 Oct)

← [[MCP vs skills - Status]] · [[YouTube Channel]] · [[Playbook]] · [[Audience]]

User (27 Oct 2026): *"New short: explain the diference between an mcp and skill and mention some examples. interesting less known usages, be creative"*. Series: **How it works** (the last video was Agent at work). Real case ([[Audience]] *Case sources*, real runs): this channel's own Claude Code session on 27 Oct 2026 (Claude Opus 5.5): four MCP servers connected and the `caveman` skill active.

**Y:** know which one to add when you want your agent to do more. **X:** an MCP adds an ability from outside (a server the agent calls); a skill adds know-how the agent reads only when the task needs it. **Theme line:** *hands vs know-how.* **Running example:** none single by request (the user asked for several examples); the session itself is the anchor that returns at the close.

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
| 10 | `slack-gif-creator`: description 37 words, `SKILL.md` 1,103 words plus a `core/` code folder; Slack emoji GIF 128×128, message GIF 480×480 | raw SKILL.md (**read**) |
| 11 | BlenderMCP: "control Blender 3D with any LLM"; runs Python in a live session, imports Poly Haven and Sketchfab assets; 32.5k stars; example prompt "a low poly scene in a dungeon, with a dragon guarding a pot of gold" | github.com/ahujasid/blender-mcp (**read**) |
| 12 | GhidraMCP lets LLMs "autonomously reverse engineer applications": decompile, rename methods, list imports and exports; 11.6k stars | github.com/LaurieWired/GhidraMCP (**read**) |
| 13 | `caveman` skill (Julius Brussee): "Terse caveman voice: answer first, fluff gone, every technical fact kept"; 628-word SKILL.md | ~/.claude plugin files, github.com/JuliusBrussee/caveman |
| 14 | This session: `claude mcp list` shows 4 connected servers (Claude Docs, Google Drive, Google Calendar, Gmail) | our run, 27 Oct 2026 |
| 15 | Anthropic's own `mcp-builder` is a skill that teaches the agent to build MCP servers | anthropics/skills (**read**) |

On screen: 1, 4, 5, 10 (the derived number), 11, 12, 13, 14. **Original synthesis:** a skill costs its description until used: 37 words carried vs 1,103 read on demand for `slack-gif-creator`, about 30 times less.

## 1. Idea gate

**Scores:** surprise 4 · scale 4 · depth 4 · evidence 5 · showable 4 · plain 4. **Street-lamp:** pass (docs define each one alone; the side-by-side rule "new app vs new habit" and the description-only loading with a measured ratio are the video's addition). **Against:** (1) "jargon for developers" → hands vs know-how, plain picture each; (2) "seen this comparison" → named weird examples (Blender, Ghidra, Slack GIFs, caveman); (3) "Claude ad" → both are open standards used by ChatGPT, Cursor, Gemini. **Demand:** YouTube autocomplete for "mcp vs skill" gives "mcp vs skills", "mcp vs claude skills", "mcp vs agent skill" (27 Oct 2026); outlier views not checked (YouTube token HTTP 400).
**Five hooks:** contradiction "MCP and skills upgrade an AI agent. An MCP gives it hands. A skill gives it know-how." (**used**) · question "Should your AI agent get an MCP or a skill?" · fact "Claude can run Blender. That is not a skill." · number "This skill costs Claude 37 words until it needs 1,100." · stakes "Add the wrong one and your agent gets slower, not smarter."

## 2. Package

- **Promise:** the one difference between MCP and skills, with real examples you did not know.
- **Titles:** *MCP vs Skills: Hands vs Know-How for AI Agents* (recommended) · *MCP vs Agent Skills, Explained in 30 Seconds* · *The Difference Between MCP and Claude Skills*.
- **Thumbnail:** a plug and a scroll facing each other, "HANDS vs KNOW-HOW". Beats neighbours (talking heads, logo grids) by showing the split as two objects.
- **Opening map:** scene 1 = promise (hands vs know-how); scene 2 = proof (real MCP servers) and plan (MCP, then skill).

## 3. Script: 85 words, 4 scenes

| Sc | Question | Voice (exact text) | Pause | Visual beat |
| --- | --- | --- | --- | --- |
| 1 | (hook) | MCP and skills upgrade an AI agent. An MCP gives it hands. A skill gives it know-how. | natural | agent (hammer and wrench) settles; plug + "hands" on "hands"; scroll + "know-how" on "know-how" |
| 2 | what is an MCP? | An MCP plugs the agent into an app. Blender MCP lets Claude build 3D scenes. Ghidra MCP lets it take programs apart. | natural | real `claude mcp list` lines light; plug into an app; dragon on gold ("Blender, 32k stars"); magnifier on a gear ("Ghidra, 11.6k stars") |
| 3 | and a skill? | A skill is a folder of instructions. The agent reads only its short description, until a task needs the rest. One makes Slack GIFs. Mine makes Claude talk like a caveman. | 0.2 s beat before the close | folder; real `slack-gif-creator` header, description lit, body dim; counter 37 vs 1,103 words; GIF tile; moai + real caveman description |
| 4 | which do I add? | So: new app, add an MCP. New habit, add a skill. Which would you build? | natural | plug "new app", scroll "new habit"; card "Hands vs know-how"; comment prompt, chips "an MCP", "a skill", "both" |

**Honesty:** "hands" and "know-how" are a plain metaphor (an MCP can also serve data and prompts; a skill can bundle scripts); star counts read 27 Oct 2026; "mine" means this channel's own Claude Code setup.

## 4. Not verified

How the voice says "MCP" and "Ghidra"; outlier demand (token). P7 is the user's.
