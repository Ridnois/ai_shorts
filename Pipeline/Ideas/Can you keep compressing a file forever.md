---
type: video-idea
status: idea
format: short
publish: 
estimated_budget_usd: 
approved_budget_usd: 
actual_cost_usd: 
video: 
hook_type: contradiction
error: 
created: 2026-10-06
updated: 2026-10-06
tags: [youtube, pipeline, computer-science, suggestion]
---

# Can you keep compressing a file forever

← [[Pipeline]] · [[YouTube Channel]] · [[Audience]] · [[Niche map]]

**Topic family:** computing. **Y:** make a file smaller (free up space). **X:** compression removes patterns and a file with no pattern left cannot shrink; counting says no method can shrink every file.

**Demand (youtube_search, 6 Oct 2026): good.** "Can You Just Keep Compressing a File?" (Topest) 299k views, 534x its channel median; "Every File Compression System Explained" 92k, 112x; Shorts on "how does a zip work" mostly under 5k, so the Short format is open.

**Original synthesis, already run (Python zlib at level 9, 6 Oct 2026):** an 18,737-byte text file compressed to 8,540 bytes, then compressing the result again made it **bigger by 11 bytes every pass** (8,551, 8,562, ...); 18,737 random bytes became 18,753. A number on screen and a test the viewer can repeat with a zip file.

**Package draft.** Promise: *you cannot zip a zip forever, and the reason is a counting rule, not a software limit.* Titles: *Why Zipping a Zip File Makes It Bigger* · *Can You Compress a File Forever? (I Tried)* · *The One Rule Every Compression Program Obeys*. Thumbnail: a stack of folders shrinking then one growing, kicker COMPUTING, lines **ZIP IT AGAIN** / **IT GETS BIGGER**, chips 18,737 BYTES / 8,540 BYTES / +11 EACH TIME.

**Hook candidates:** contradiction "Compress a file twice and it gets bigger." · surprising number "I compressed a file six times: the first pass saved half, every pass after added eleven bytes." · stakes "No compression program can shrink every file, and mathematics proves it." · question-as-claim "A zip file is already full: there is nothing left to take out." · consequence "Photos, music and video are small because someone decided what you will not notice is missing."

**Facts to verify at P1:** the counting (pigeonhole) argument (there are 2^n files of n bits and fewer shorter ones); Shannon entropy, 1948; lossless against lossy; why a second pass adds a few bytes (headers); where JPEG and MP3 throw data away. Sources to read: Shannon 1948 paper abstract, the DEFLATE RFC 1951 (header overhead), a university lecture note on the counting argument.

**Risks:** keep it a Short: one rule (patterns), one test (zip a zip), one number; leave Huffman details out.
