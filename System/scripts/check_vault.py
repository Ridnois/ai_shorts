#!/usr/bin/env python3
"""Coherence check for the YouTube vault. Run from the vault root:  python3 System/scripts/check_vault.py

Fails (exit 1) on:
  * broken wikilinks and embeds (a target that is neither a note nor a file in the vault or in Media/)
  * notes without front matter (type, updated)
  * System/ notes that the index (YouTube Channel.md) does not mention
  * Python scripts that do not compile
  * `[[Note]] §Heading` references whose heading does not exist (numbered §N must match "## N." in that note)
  * per-video notes over their size ceiling; index missing a video's YouTube id; Script scene 1 differing from the hook in Analytics/videos.csv
  * missing INVARIANTS: phrases that encode user feedback and must stay in the notes that carry them
  * hfkit.py or captions.py failing its self-check
When feedback adds a rule, add its invariant below in the same pass (see System/Feedback loop.md).
"""
import os
import re
import sys

ROOT = os.getcwd()
SKIP = (".git", ".obsidian", ".claude", "Media", "__pycache__")       # .claude: agent skills, not notes

INVARIANTS = [
    # (file, phrase, rule it protects): rules that must never silently disappear
    ("System/Playbook.md", "Street-lamp test", "idea gate"),
    ("System/Playbook.md", "Five candidate hooks", "the hook earns its reaction"),
    ("System/Playbook.md", "Facts bank", "idea gate"),
    ("System/Playbook.md", "named real case", "a real case carries the concept"),
    ("System/Playbook.md", "never seconds", "length is planned in words"),
    ("System/Playbook.md", "need-to-know claim", "the first 2 seconds"),
    ("System/Playbook.md", "Explain, do not narrate", "cause and effect, not story"),
    ("System/Playbook.md", "theme line", "one thread"),
    ("System/Playbook.md", "concrete payoff", "ending"),
    ("System/Playbook.md", "one continuous take", "the voice is never stitched"),
    ("System/Playbook.md", "Transitions with a cause", "no slideshow crossfades (professional standard, 27 Oct 2026)"),
    ("System/Playbook.md", "shot sizes", "the camera changes scale inside a world (27 Oct 2026)"),
    ("System/Playbook.md", "Slideshow-risk score", "pre-render check"),
    ("System/Playbook.md", "Ship discipline", "ship, fix or drop; at most two revisions (27 Oct 2026)"),
    ("System/Playbook.md", "variety", "inauthentic-content policy"),
    ("System/Playbook.md", "Loop ledger", "stacked open questions keep the viewer to the end (28 Oct 2026)"),
    ("System/Playbook.md", "Loop-back close", "the ending re-asks the hook so the Short replays (28 Oct 2026)"),
    ("System/Playbook.md", "Re-hook every 8 to 12 s", "a new question or reversal on a turn word (28 Oct 2026)"),
    ("System/Design system.md", "colx(k, n)", "elements sit on a column grid, never placed by eye"),
    ("System/Design system.md", "Every world is a canvas", "camera on one canvas (27 Oct 2026)"),
    ("System/Design system.md", "Sound kit", "effects come from the licensed kit"),
    ("System/Design system.md", "Blender", "Blender scenes reach HyperFrames as glb or alpha webm"),
    ("System/Workflow.md", "validate_palette.js", "new colours are validated, not eyeballed"),
    ("System/Workflow.md", "did you know what the video is about", "rubric asks about hook clarity"),
    ("System/Workflow.md", "listen.py", "the agent measures the sound instead of leaving it unverified (28 Oct 2026)"),
    ("System/Workflow.md", "--crf 14", "renders keep their gradients and fine lines (27 Oct 2026)"),
    ("System/Workflow.md", "Clarify first", "interactive questions before a new video"),
    ("System/Style.md", "never inside the video", "no branding inside the video"),
    ("CLAUDE.md", "hfkit.py", "one design system in code"),
]
FORBIDDEN = [
    # (file, phrase, why): rules the user removed; must not come back
    ("System/Playbook.md", "≤ 10 words", "hook quality is not measured in words (feedback, 5 Oct 2026)"),
    ("CLAUDE.md", "16 to 20 plates", "a plate count produced filler pictures (user, 9 Oct 2026)"),
    ("System/Playbook.md", "16 to 20 plates", "a plate count produced filler pictures (user, 9 Oct 2026)"),
    ("System/Audience.md", "civil engineering", "the old technology niche was replaced by AI (user, 23 Oct 2026)"),
    ("CLAUDE.md", "civil engineering", "the old technology niche was replaced by AI (user, 23 Oct 2026)"),
    ("System/Playbook.md", "Fluent Emoji", "emoji illustrations were replaced by Hairline figures (user, 27 Oct 2026)"),
    ("System/Playbook.md", "build_video.py", "the Blender builder was retired (27 Oct 2026)"),
    ("System/Workflow.md", "SOLO_PROYECTO", "the Blender builder was retired (27 Oct 2026)"),
]
CEILING = {"Script - ": 2700, "Upload - ": 2300, " - Status": 1500}

problems = []
notes, names = {}, set()
for r, d, f in os.walk(ROOT):
    d[:] = [x for x in d if x not in SKIP]
    for x in f:
        p = os.path.join(r, x)
        rel = os.path.relpath(p, ROOT)
        names.add(x)
        names.add(os.path.splitext(x)[0])
        if x.endswith(".md"):
            notes[rel] = open(p, encoding="utf-8").read()
media = set()
for r, d, f in os.walk(os.path.join(ROOT, "Media")):
    for x in f:
        media.add(x)
        media.add(os.path.splitext(x)[0])

LINK = re.compile(r"!?\[\[([^\]|#]+)((?:#[^\]|]*)?)(?:\|[^\]]*)?\]\]")
for rel, t in notes.items():
    body = re.sub(r"```.*?```", "", t, flags=re.S)           # ignore code blocks
    body = re.sub(r"`[^`]*`", "", body)                      # and inline code
    for m in LINK.finditer(body):
        tgt = m.group(1).strip()
        if (m.group(1) + m.group(2)).strip() in names:      # a note whose own name contains "#" (e.g. "Youtube idea #2")
            continue
        if tgt in names or os.path.basename(tgt) in names or tgt in media or os.path.basename(tgt) in media:
            continue
        problems.append(f"broken link in {rel}: [[{tgt}]]")
    if rel in ("CLAUDE.md",):
        continue
    fm = re.match(r"---\n(.*?)\n---\n", t, re.S)
    if not fm:
        problems.append(f"no front matter: {rel}")
    else:
        keys = {l.split(":")[0].strip() for l in fm.group(1).splitlines() if ":" in l and not l.startswith((" ", "-"))}
        need = {"type", "status"} if rel.startswith("Pipeline/Idea") else {"type", "updated"}
        miss = need - keys
        if miss:
            problems.append(f"front matter of {rel} lacks {sorted(miss)}")

index = notes.get("YouTube Channel.md", "")
for rel in notes:
    if rel.startswith("System/") and not rel.startswith("System/assets/") and os.path.splitext(os.path.basename(rel))[0] not in index:
        problems.append(f"not in the index (YouTube Channel.md): {rel}")

# the design system and the captions pass their own self-checks
import subprocess
for _script in ("hfkit.py", "captions.py"):
    _r = subprocess.run([sys.executable, os.path.join(ROOT, "System", "scripts", _script)], capture_output=True, text=True)
    if _r.returncode:
        problems.append(f"{_script} self-check failed: {(_r.stdout + _r.stderr).strip().splitlines()[-1][:120]}")

for r, d, f in os.walk(os.path.join(ROOT, "System", "scripts")):
    for x in f:
        if x.endswith(".py"):
            try:
                compile(open(os.path.join(r, x), encoding="utf-8").read(), x, "exec")      # syntax only
            except SyntaxError as e:
                problems.append(f"does not compile: {x}: {str(e)[:80]}")

for rel, phrase, why in FORBIDDEN:
    if phrase.lower() in notes.get(rel, "").lower():
        problems.append(f"{rel} contains \"{phrase}\": {why}")

# section references: [[Note]] §N or §Heading must point at a real heading
SEC = re.compile(r"\[\[([^\]|#]+)\]\] §([0-9]+|[A-Za-z][A-Za-z ]*[A-Za-z])")
by_name = {os.path.splitext(os.path.basename(r))[0]: t for r, t in notes.items()}
for rel, t in notes.items():
    if rel.startswith("Analytics/Reports/"):
        continue          # dated reports are history
    for m in SEC.finditer(t):
        tgt, ref = m.group(1).strip(), m.group(2).strip()
        body = by_name.get(tgt)
        if body is None:
            continue
        heads = re.findall(r"(?m)^#+ (.*)$", body)
        ok = any(h.startswith(ref + ".") for h in heads) if ref.isdigit() else any(ref.lower().startswith(h.lower()) or h.lower().startswith(ref.lower()) for h in heads)
        if not ok:
            problems.append(f"dead section reference in {rel}: [[{tgt}]] §{ref}")

# per-video note size ceilings (words)
for rel, t in notes.items():
    if rel.startswith("Videos/"):
        n = len(t.split())
        for key, cap in CEILING.items():
            if key in os.path.basename(rel) and n > cap:
                problems.append(f"{rel} has {n} words, ceiling {cap} (Workflow: Note size ceilings)")

# the index knows every published video; Script scene 1 equals the hook in videos.csv
import csv
norm = lambda s: re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()
with open(os.path.join(ROOT, "Analytics", "videos.csv"), encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        if row["youtube_id"] and row["youtube_id"] not in index:
            problems.append(f"YouTube Channel.md lacks the id of {row['video']} ({row['youtube_id']})")
        sc = next((t for r, t in notes.items() if os.path.basename(r) == f"Script - {row['video']}.md"), "")
        m = re.search(r"(?m)^\|\s*1\s*\|\s*([^|]+?)\s*\|", sc[sc.find("Voice (exact text)"):]) if "Voice (exact text)" in sc else None
        if m and norm(m.group(1)) != norm(row["hook"]):
            problems.append(f"hook in videos.csv differs from scene 1 of the script: {row['video']}")

for rel, phrase, why in INVARIANTS:
    t = notes.get(rel, "")
    if phrase.lower() not in t.lower():
        problems.append(f"missing in {rel}: \"{phrase}\" ({why})")

print(f"{len(notes)} notes checked, {len(INVARIANTS)} invariants.")
if problems:
    print(f"{len(problems)} problem(s):")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("OK: the vault is coherent.")
