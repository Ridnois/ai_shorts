---
type: research
created: 2026-10-04
updated: 2026-10-04
status: v1 · template for the user's feedback after a render (P7); copy it to Videos/<Topic>/Post-render feedback - <Topic>.md
tags: [research, youtube, process, feedback, template]
---

# Post-render feedback template

← [[YouTube Channel]] · [[Feedback loop]] · [[Production process]]

**How to use it:** copy everything below the line into `Videos/<Topic>/Post-render feedback - <Topic>.md` (the agent does this when a render is ready), fill what you want, leave the rest empty, and tell the agent *"feedback is in"*. Free sentences are fine; **your words are kept verbatim**. The agent then follows [[Feedback loop]]: classifies every point by layer, edits the vault everywhere it applies, adds an invariant to `check_vault.py`, and answers with a *what changed where* table, appended below as **Response**.

Scale for the ratings: **1** = redo, **2** = weak, **3** = acceptable, **4** = good, **5** = keep exactly as is. Leave blank if you did not judge it.

---

```markdown
---
type: research
created: <date>
updated: <date>
status: waiting for the user's feedback on render r<n>
tags: [research, youtube, feedback, <topic>]
---

# Post-render feedback - <Topic>

← [[YouTube Channel]] · [[<Topic> - Status]] · [[Feedback loop]]

**Render watched:** `Media/<Topic>/render/<file>.mp4` · **Watched with sound?** yes / no · **Device:** phone / desktop

## 1. Verdict

**Would you publish it as it is?** yes / yes after small fixes / no
**In one sentence, the best thing:**
**In one sentence, the worst thing:**

## 2. By layer (rating 1 to 5, then your words)

| Layer | Rating | What you saw or heard, and what you want instead |
| --- | --- | --- |
| **Hook** (first 3 s: plain words, a claim you need to hear, does it stop you?) | | |
| **Idea and content** (is it surprising, clear, scientifically right?) | | |
| **Script and pace** (one theme you can say in a sentence? lost in facts? compact enough?) | | |
| **Illustrations and photos** (useful, faithful, one per idea?) | | |
| **Text boxes, callouts, highlight** (readable, specific, in the right place?) | | |
| **Captions** (on the spoken word? readable on every image?) | | |
| **Channel assets** (name, avatar, banner; the video itself carries no branding) | | |
| **Voice** (timbre, speed, intonation, mispronounced words) | | |
| **Sound design** (thump, whooshes, ticks, pings, drone: too loud, missing, annoying?) | | |
| **Editing** (cuts, cross-fades, how long an image stays, transitions) | | |
| **Ending** (does it leave an idea? does it loop?) | | |

## 3. Moments (use the time in the video)

| Time (s) | What happens | What is wrong or great | What to do |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |

## 4. Checks only you can do (the agent cannot hear or watch the video)

- [ ] The voice sounds natural and the pace feels right
- [ ] Each caption word lands on the spoken word
- [ ] The sound design is at a comfortable level (adjust `sfx_gain`, `bed_gain`)
- [ ] Transitions and the speed of image changes look right in motion
- [ ] The facts you know are correct; list any doubt here:

## 5. After publishing (fill 48 hours and 7 days later; see [[Channel strategy]] §6)

| Metric | 48 h | 7 days |
| --- | --- | --- |
| Views / **engaged views** | | |
| Share who stay past the first seconds (Studio: viewed vs swiped away, if shown) | | |
| Average percentage viewed | | |
| Subscribers gained | | |
| Comments worth reading (paste the best two) | | |

## 6. Process and anything else

Rules you want changed, things the agent should always or never do, ideas for the channel:

## 7. Keep and change (for the agent to turn into rules)

**Keep exactly:**
**Change from now on:**
```
