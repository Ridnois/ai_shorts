---
type: research
created: 2026-10-05
updated: 2026-10-05
status: v1 · assessment of the vault as knowledge source and process guide; proposals only, no rule changed yet
tags: [analysis, vault, process, week-01]
---

# Vault assessment · 5 Oct 2026

← [[YouTube Channel]] · [[Playbook]] · [[Workflow]] · [[Publish]] · [[Feedback loop]] · [[2026-10-05 First numbers]]

Read: `CLAUDE.md`, the five System notes, the index, Pipeline, Report, the three Week 01 videos (Status, Script, Upload), the scripts' headers and `check_vault.py` (passes: 22 notes, 38 invariants). Not read line by line: `build_video.py` (686 lines), the Upload notes beyond their structure. Not checked: any rendered video (the agent cannot watch or hear).

## 1. Verdict

**As a knowledge source: strong.** One rule per note, a clear read order, feedback converted into edits, an invariant check that keeps rules from silently disappearing. An agent starting cold can produce a compliant video.

**As a process guide: strong at compliance, weak at quality and learning.** The vault is excellent at saying *what a valid Short looks like* and almost silent on *what makes one good*. Every gate is a checklist the agent grades itself on; none is anchored to an outside signal. With 2 videos, 55 views and no retention data, the vault is currently an unfalsified theory of what works.

## 2. What works (keep)

| Strength | Why it matters |
| --- | --- |
| Read order and token discipline in `CLAUDE.md` / [[Workflow]] | A cold agent reaches the right rules in four reads |
| Hard rules with a *why* (no media before P4, budget cap ×1.2) | Prevents the costly failures (spend, regenerate) |
| Words, not seconds, as the length unit | Measurable before any money is spent |
| Hook rule (plain, ≤ 10 words, first 3 s) and cut test | Specific and testable |
| Honest "not verified" section in every Status | Keeps P7 with the user and stops false claims |
| Feedback loop + `check_vault.py` invariants | The vault cannot drift back to a rule the user removed |
| Policy section in [[Publish]] (inauthentic content, disclosure) | Protects monetization, the channel's biggest structural risk |

## 3. Problems found

### 3.1 Rules are broken by the vault's own videos (the gate does not gate)

| Rule | What happened |
| --- | --- |
| Scene 1 ≤ 10 words | `videos.csv` hook for Copper is **12 words** ("One AI server rack can hold over two miles of copper cable"); the script note says the chosen hook was 10 words ("One AI rack holds over two miles…"). The published and the planned text differ, and nothing detects it |
| Length 130 to 190 words | Battery is **200** (user override, recorded; fine) but 72 s is already above the 60 s target; no rule says what a justified exception costs |
| Street-lamp test must pass | All three videos record the test as **"borderline"** and proceed. The gate has no fail state: "borderline" is accepted every time, so it is decoration |
| "Keep notes short" (`CLAUDE.md`) | Script notes are **2.4 to 3.1 k words** each, Upload up to 2.8 k, Battery Status 1.7 k, against a Playbook of 1.9 k. Per-video notes are larger than the rulebook they follow |
| Idea scores | "Agent's guess" in every scoring table; the same author scores and approves, so scores of 4 on everything cluster and do not discriminate |

### 3.2 Stale or inconsistent text (the vault says it must agree with itself)

- **Dead section references:** `[[Publish]] §3`, `§5`, `§6` appear 11 times (Report, First numbers, Pipeline text) but [[Publish]] now has unnumbered sections. Also `[[Playbook]] §4/§5/§7` are the only valid ones. `check_vault.py` checks links, not section anchors.
- **Duplicate links** in every Status header (`[[Playbook]] · [[Playbook]]`, `[[Workflow]] · [[Workflow]]`, same in Pipeline): leftover of the consolidation find-and-replace.
- **Index states are out of date:** [[YouTube Channel]] says Copper and EV are "uploaded private" and Battery "upload package ready", but [[2026-10-05 First numbers]] shows Battery and Copper **public** with live view counts. The index is the entry point and is wrong.
- **`check_vault.py` header** points to `System/Process/Feedback loop.md` (path no longer exists).
- **Pipeline.md** describes a runner flow (statuses, `.base` table, a service in `~/Documents/youtube-pipeline`) that none of the three videos used: all were built interactively under delegation. It says "Sonnet-class model" in [[Workflow]] but the runner contract and the real flow have diverged; it also quotes "rule 0.9", a number that no longer exists. Two Ideas exist; neither has moved. Either the runner is the process or it is dead weight.
- **`Media/Legacy`** exists locally though the vault says Legacy was deleted; `CLAUDE.md` lists no such folder.
- Different media folder names (`Battery-lithium`, `Copper-AI`, `EV-battery`) than the video titles, which makes lookups by title fail.

### 3.3 Knowledge gaps (the vault cannot tell the agent how to be *good*)

1. **No examples of a great script.** The Playbook gives structure and word budgets per scene but not one model script, nor one before/after of a weak vs strong scene 1. Rules without a reference sample get satisfied minimally.
2. **No quality rubric that is not a checklist.** Everything is pass/fail. Nothing ranks the three finished videos against each other, so the agent cannot learn which of its own outputs was best.
3. **Retention knowledge is a guess.** Benchmarks (≈ 80 % held at 3 s, ≈ 70 % average viewed) are labelled as guesses, correctly, but the hook, pace (≈ 187 wpm speaking), plate rhythm (3 to 4 s) and sound design rules are all unvalidated. They are presented in imperative voice as if tested.
4. **No competitive reference.** Nothing records what the strongest science Shorts in this niche do (hook patterns, length, pacing, visual style). The idea gate is internal (facts, scores) and has no outside check of demand.
5. **No topic-demand step.** Ideas are scored on "surprise, scale, depth, evidence, showable, plain" (all supply-side). Nothing asks whether people search for or share this subject; the three Week 01 videos are all materials/battery topics chosen by the agent, which is a narrow cluster for a "science entertainment" brand.
6. **Series and recurrence are absent.** The CSV has a `series` column, always empty; no rule about recurring formats or a second video that builds on the first. Viewers subscribe to a promise, not to a topic list.
7. **Audio is the weakest-specified quality lever.** Voice settings are tuned by rules, but the agent cannot hear it, the user hears it only at P7, and no rubric records what the user liked ("perfect" is the only data point). Sound design is synthetic with fixed levels and no listening-based feedback loop.
8. **Thumbnail and title rules are thin** (title ≤ 100 chars, keyword first). For Shorts the feed ignores the thumbnail, so this is acceptable, but the title/description are the only searchable text and carry little method.

### 3.4 Process friction

- **Eight stages, five gates, one approval each,** but all three videos ran under delegation ("upload it to youtube", "follow the steps until the render"). The gates exist for a workflow the user does not actually run. Delegation is the norm; the vault documents it as the exception.
- **Stage 5 (test) was skipped** ("folded into 6") in all three. A stage skipped every time is not a stage.
- **Cost model has unconfirmed prices** (`gpt-image-2` ≈ $0.10 in the budget table, $0.25 assumed in EV Status, "unmeasured" for background removal). The cap rests on guesses until the Replicate dashboard is read once.
- **Same author, same model, same session writes the idea, scores it, writes the script and checks it.** No independent check except the user at P7. Self-review confirms itself.
- **Token cost:** every task reads ≈ 6.4 k words of rules plus ≈ 3 to 8 k of per-video notes before writing. The Playbook is 1.9 k words and dense; that is acceptable, but per-video notes should not be re-read by later videos.

## 4. What I conclude about video quality

1. **The videos are probably over-specified in structure and under-specified in taste.** Word counts, plate counts, caption positions and sound levels are fixed to the decibel; the thing that makes a Short worth watching (a voice with a point of view, a surprise that lands, a visual that surprises too) is left to "calm, precise, dry".
2. **16 to 21 plates in 60 s is a lot of content for stock photos.** Several Status notes admit weak images (a motorcycle battery line used for a car, an old Leaf pack, four reused photos, a small `contain` photo). Rhythm is satisfied by quantity, relevance by compromise. The usefulness test is applied to plates the agent already chose.
3. **Hooks are plain and honest but not yet proven to stop a scroll.** "Your battery runs on a metal that floats" and "Electric car batteries lose about two percent a year" are accurate and clear; the second is a number without a reason to care, which the Playbook itself says is not a hook.
4. **Facts are well sourced.** This is the channel's real asset and differentiator against template AI content.
5. **There is no way yet to tell whether any change helped.** One change per video is the rule; with 55 views in total, that rule cannot yet be tested.

## 5. Proposals, ranked by expected gain

| # | Change | Owning note | Cost |
| --- | --- | --- | --- |
| 1 | **Add a reference sample:** one finished script (best of the three) annotated line by line (why scene 1 works, where the bridge is, the payoff), plus one weak-to-strong scene-1 rewrite. Link from the Playbook | [[Playbook]] | one note, ≈ 400 words |
| 2 | **Give the street-lamp and expert tests a fail state:** "borderline = go back to step 1, or write the one-sentence reason it passes and get the user's yes". Add scores from a second pass that argues against the idea, not the guess of the author | [[Playbook]] §1 | 3 lines |
| 3 | **Fix hook length checking:** the builder or `check_vault.py` counts words of scene 1 from the Script and from `videos.csv` and fails above 10 | `check_vault.py` | ≈ 15 lines |
| 4 | **Make delegation the default process:** collapse the stage table to the real flow (A text → B build → render → user P7 → publish), drop stage 5 unless a new technique is tried, keep the budget cap | [[Workflow]] | rewrite one table |
| 5 | **Cap per-video notes:** Script ≤ 900 words (scenes table, hooks, scores, nothing else), research bank in the Status only if ≥ 15 facts; delete scoring tables of rejected threads after P3 | [[Playbook]], [[Workflow]] | edits; trim the three existing notes |
| 6 | **Add a demand check at P1:** one line per candidate on whether the subject is searched or shared (autocomplete, trends, 3 comparable Shorts and their views). Ranks ideas by outside evidence | [[Playbook]] §1 | one web step per idea |
| 7 | **Diversify topics deliberately:** a rule that two consecutive videos may not share a topic family (all three are batteries or materials), and use `series` for a recurring format once there are ≥ 5 videos | [[Playbook]] §1, [[Pipeline]] | 2 lines |
| 8 | **Replace "synthetic confidence" with labelled hypotheses:** mark rules with `[H]` (a hypothesis, untested) vs `[T]` (tested on channel data); the 10-video review (already in [[Publish]]) flips them | [[Playbook]] | tagging |
| 9 | **User listening rubric at P7:** three questions the user answers in a line (voice natural? pace OK? sound mix OK?) and the answer is written to Status; becomes the only audio evidence | [[Workflow]] | 3 lines |
| 10 | **Confirm prices once:** read the Replicate dashboard, replace "≈ / assumed" with measured numbers in [[Workflow]] | [[Workflow]] | 5 minutes |
| 11 | **Hygiene pass:** repair `§` references (use heading names), remove duplicate links, update the index state (Battery and Copper public), fix the `check_vault.py` header path, decide Pipeline runner (keep or delete the note), rename media folders to the video title, delete `Media/Legacy` | several | ≈ 20 min |
| 12 | **Add checks to `check_vault.py`:** heading-anchor validity for `[[Note]] §…`, index state vs `videos.csv`, hook ≤ 10 words, per-video note size | `check_vault.py` | ≈ 40 lines |

**Do first:** 11 (cheap, makes the vault trustworthy), 3 and 2 (turn two rules into gates), 1 (biggest quality lever). 6 and 7 once there are 5 videos of data. Do not touch visuals or sound rules until retention data exists.

## 6. What this assessment could not establish

- Whether any rule improves retention: there are no viewed, retention or share numbers (the Analytics API returned nothing at 1 to 2 hours).
- How the videos look and sound: the agent read notes and build logs, not the mp4s.
- Whether the Pipeline runner still works (`~/Documents/youtube-pipeline/pipeline.py` exists; not run).
- The Upload notes' content quality beyond structure.
