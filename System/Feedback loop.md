---
type: process
updated: 2026-10-28
status: v4 · 28 Oct 2026: a recurring fault becomes an automatic check; v3 · 27 Oct 2026: edit the rule, never append a quote; one change per gap; feedback applies forward
---

# Feedback loop

The vault is the single source of knowledge: feedback is finished only when the vault says it and agrees with itself.

1. **Record** the user's words verbatim in the video's Status note under *Feedback* (they are the evidence; the rule never repeats them, git keeps the history).
2. **Find the gap:** what the video did that the user did not want, in one line. One gap, one change.
3. **Edit the one rule that owns it**, as a principle plus its test: idea, script, visuals, voice, sound, ship → [[Playbook]]; look, layout, camera, motion, sound kit → [[Design system]] and `hfkit.py` together; brand and words → [[Style]]; stages, cost, commands → [[Workflow]]; before the click → [[Audience]]; upload, policy, metrics → [[Publish]]; agent behaviour → `CLAUDE.md`.
4. **The newest explicit feedback wins:** edit or delete the older rule in the same pass, never leave both. If two instructions truly conflict, ask.
5. **Delete what it replaces** (no archives, no "supersedes" tables). A rule that only restates another is deleted.
6. **Apply forward:** the next video follows the new rule; renders already waiting ship unless the feedback names a defect in them ([[Playbook]] §8).
7. **Add an invariant** to `System/scripts/check_vault.py` only for a rule that must never silently disappear; run it until it passes.
8. **A fault that comes back is a missing check, not a missing glance:** when the user reports the same class of fault twice (layout, clipping, overlap), the fix is an automatic check in `check3d.mjs` or an `hfkit` warning plus a structural rule in [[Design system]], then the whole video is re-audited, not only the frames the user sent.
9. **Answer** with a short table of what changed where, and what remains unverified.

Data feedback (retention, shares) goes through [[Publish]] §Analytics loop, then here.
