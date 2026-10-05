---
type: process
updated: 2026-10-05
status: v2 · short procedure
---

# Feedback loop

The vault is the single source of knowledge: feedback is finished only when the vault says it and agrees with itself.

1. **Record** the user's words verbatim (in the video's Status note under *Feedback*, or a dated line for process feedback). Words stay as evidence.
2. **Classify** each point and **edit the one rule that owns it**: idea, script, visuals, text, voice, sound, edit → [[Playbook]]; stages, cost, models, files → [[Workflow]]; look and brand → [[Style]]; upload, policy, metrics → [[Publish]]; agent behaviour → `CLAUDE.md`. Also change what implements it (`build_video.py`, `plan.json`, `pipeline.py` prompts).
3. **The newest explicit feedback wins:** edit or delete the older rule in the same pass; never leave both. If two instructions truly conflict, ask.
4. **Delete what it replaces** (git keeps history; no archives, no "supersedes" tables).
5. **Add an invariant** to `System/scripts/check_vault.py` (a phrase that must stay in the owning note, or a builder guard), run `python3 System/scripts/check_vault.py` until it passes.
6. **Answer** with a short table of what changed where, and what remains unverified.
7. **Update memory** with a one-line pointer to the note that now holds the lesson.

Data feedback (retention, shares) goes through [[Publish]] §Analytics loop, then to the owning rule here.
