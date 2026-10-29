---
type: research
created: 2026-10-26
updated: 2026-10-26
status: v1 · 139 words, 6 scenes, take v1 43.3 s; second of the short test block
tags: [research, youtube, script, ai, agents, week-04]
---

# Script · HyperFrames (Week 04, Mon 26 Oct)

← [[HyperFrames - Status]] · [[YouTube Channel]] · [[Format]] · [[Growth]]

User (26 Oct 2026): *"New short: explain hyperframes to web and youtube short"*. Series: **Agent at work**. Real case ([[Growth]] *Case sources*, real runs): this channel's own Shorts, written by Claude Code as HyperFrames pages.

**Y:** make a video without a video editor. **X:** a video can be a web page that a hidden browser photographs frame by frame. **Theme line:** *a page you can film.* **Running example:** the *RAG explained* r2 page: its real code lines and its real frames.

## 0. Facts bank (**read** = opened 26 Oct 2026)

| # | Fact | Source |
| --- | --- | --- |
| 1 | Tagline "Write HTML. Render video. Built for agents." | github.com/heygen-com/hyperframes README (**read**) |
| 2 | Made by HeyGen, "used in production at HeyGen" | README (**read**) |
| 3 | Apache 2.0, "no per-render fees or commercial-use thresholds" | README (**read**) |
| 4 | A video is an HTML file with `data-start`, `data-duration`, `data-track-index` | README (**read**); our `index.html` |
| 5 | Animation by seekable timelines (GSAP on `window.__timelines`; also CSS, Lottie, Three.js, Anime.js, WAAPI) | README (**read**) |
| 6 | Headless Chrome (Puppeteer) seeks each frame; FFmpeg encodes | README (**read**) |
| 7 | "The same input produces the same video" (CI, regression tests) | README (**read**) |
| 8 | Agent-first: non-interactive CLI, no build step, skills for Claude Code, Cursor, Gemini CLI, Codex | README (**read**); yuv.ai review |
| 9 | Claude Code plugin: `claude plugin install hyperframes@hyperframes` | README (**read**) |
| 10 | Commands `init`, `preview`, `render`, `add`, `skills update`; Node 22+ and FFmpeg | README (**read**) |
| 11 | Open-sourced about 10 Mar 2026; about 73k stars on 26 Oct 2026 | landscape.jimmysong.io (date); README page (stars) |
| 12 | Not HeyGen's avatar product | themenonlab review |
| 13 | Our renders: 1080×1920 at 30 fps, about 3 min for a 43 s Short on this laptop | our Status notes |
| 14 | Our pages are written by Claude Code (Claude Opus 5.5), Oct 2026 | this vault |
| 15 | The page can be previewed live in a browser | README (**read**) |

On screen: 1 to 3, 4, 6, 7, 13, 14.

## 1. Idea gate

**Scores:** surprise 4 · scale 3 · depth 4 · evidence 5 · showable 5 · plain 4. **Street-lamp:** pass (the README says what; seek-per-frame on a real Short shows how). **Against:** (1) "a dev tool" → Y is a video with no editor; (2) "an ad for HeyGen" → open source, no fee, our own run; (3) "too technical" → three steps, one picture each. **Demand:** not run (token).
**Five hooks:** contradiction "This Short is a web page." (**used**) · question "Can an AI agent make a video without a video editor?" · fact "This video was filmed by a browser nobody could see." · number "Thirty photos a second of one web page." · stakes "Your next explainer might not need an editor."

## 2. Package

- **Promise:** how a web page becomes a YouTube Short, shown on this channel's own Short.
- **Titles:** *HyperFrames Explained: This Short Is a Web Page* (recommended) · *How AI Agents Make Videos Without an Editor* · *HTML to Video: How HyperFrames Works*.
- **Thumbnail:** the phone with a real frame, peeling to code; words "THIS IS HTML".

## 3. Script: 139 words, 6 scenes (take v1, rate 1.1: 43.3 s)

| Sc | Question | Voice (exact text) | Visual beat |
| --- | --- | --- | --- |
| 1 | (hook) | This Short is a web page. An AI agent wrote it in HTML, and a free tool called HyperFrames turned it into video. Here is how. | a real frame of *RAG explained* in a phone; globe on "web page"; agent (hammer and wrench); clapper on "HyperFrames" |
| 2 | what does the agent write? | The agent writes one page: the words, the pictures, and a timeline that says when each one moves. | the page's real code; words, pictures, stopwatch; timing lines light on "moves" |
| 3 | how does it become video? | HyperFrames opens that page in a hidden browser. It jumps to frame one and takes a picture. Then frame two. Thirty times a second. (beat 0.3) | hidden browser; counter "frame 1, 2 … 30"; camera flash; real frames fill a film strip |
| 4 | why jump? | Because it jumps instead of playing, the same page always gives the same video. Then an encoder joins them into one video file. | render 1 and render 2 identical, check; film frames to clapper, "one video file" |
| 5 | so what? | That matters because agents already write web pages well. So one agent can make your explainer, or your ad, with no video editor. | agent, web pages, three real Shorts; explainer, ad, editor crossed out |
| 6 | close | So here is the point. If an agent can build it as a web page, it can film it. What would you make? Tell me. | build it, then film it; conclusion card; margin note |

**Honesty:** "free" means open source, no per-render fee (README); the code lines are real but shortened with "…"; "thirty times a second" is our render setting, not a fixed property of the tool.

## 4. Not verified

The open-source date (third-party); how the voice sounds. P7 is the user's.
