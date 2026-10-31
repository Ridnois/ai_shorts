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
  * a key in any file git would commit, .env not ignored, or the pre-commit secret hook missing (secret_scan.py)
When feedback adds a rule, add its invariant below in the same pass (see System/Feedback loop.md).
"""
import os
import re
import sys

ROOT = os.getcwd()
SKIP = (".git", ".obsidian", ".claude", "Media", "__pycache__")       # .claude: agent skills, not notes

INVARIANTS = [
    # (file, phrase, rule it protects): rules that must never silently disappear
    ("System/Format.md", "Real thing", "a named, dated real case carries every video"),
    ("System/Format.md", "Curiosity gap", "the idea must make a stranger ask why"),
    ("System/Format.md", "130 to 170 words", "45 to 60 s length (user, 29 Oct 2026)"),
    ("System/Format.md", "three-hook rule", "visual, spoken and text hook name the same thing"),
    ("System/Format.md", "Frame 0 is the thumbnail", "the hook's picture and claim at 0 s"),
    ("System/Format.md", "The loop ending", "the last line runs into the first"),
    ("System/Format.md", "Show the verb", "pictures show what happens, never decorate"),
    ("System/Format.md", "Three shot sizes", "the camera changes scale inside a world"),
    ("System/Format.md", "Varied from the last video", "inauthentic-content policy"),
    ("System/Format.md", "at most two revisions", "ship, fix or drop"),
    ("System/Look.md", "Next Token", "the brand (user, 29 Oct 2026)"),
    ("System/Look.md", "flat paper", "the look that survives YouTube's re-encode (user, 29 Oct 2026)"),
    ("System/Look.md", "not inside the video", "no branding inside the video"),
    ("System/Look.md", "Every world is a canvas", "camera on one canvas"),
    ("System/Look.md", "Sound kit", "effects come from the licensed kit"),
    ("System/Production.md", "Ask once", "one question round before a new video"),
    ("System/Production.md", "one continuous take", "the voice is never stitched"),
    ("System/Production.md", "master.py", "every upload is the 4K master"),
    ("System/Production.md", "listen.py", "the agent measures the sound"),
    ("System/Production.md", "check3d.mjs", "layout faults are caught by a check"),
    ("System/Growth.md", "confirm the pack", "upload only after the user confirms"),
    ("System/Growth.md", "engaged views", "compare videos on the right metric"),
    ("System/Growth.md", "Inauthentic content", "the channel-wide policy risk"),
    ("CLAUDE.md", "hfkit.py", "one design system in code"),
    ("CLAUDE.md", "master.py", "never upload the raw render"),
    ("CLAUDE.md", "youtube_auth.py", "every YouTube token is checked against the Next Token channel (user, 30 Oct 2026)"),
    ("System/scripts/youtube_auth.py", "UCCZX7-YPNPntwPKI1hdv2hQ", "the Next Token channel id the scripts enforce"),
]
FORBIDDEN = [
    # (file, phrase, why): rules the user removed; must not come back
    ("CLAUDE.md", "civil engineering", "the old technology niche was replaced by AI (user, 23 Oct 2026)"),
    ("System/scripts/hfkit.py", "feTurbulence", "animated grain wrecks YouTube's re-encode (29 Oct 2026)"),
    ("System/scripts/hfkit.py", "#grain", "animated grain wrecks YouTube's re-encode (29 Oct 2026)"),
]
SKILLS = ["short", "short-idea", "short-script", "short-qa", "short-publish"]   # the vault's own skills (.claude/skills)
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
    src = notes.get(rel) if rel.endswith(".md") else (open(os.path.join(ROOT, rel), encoding="utf-8").read() if os.path.exists(os.path.join(ROOT, rel)) else "")
    if phrase.lower() in (src or "").lower():
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
                problems.append(f"{rel} has {n} words, ceiling {cap} (Production: Files)")

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

# no keys in what git would commit (the repo is public); .env ignored; pre-commit hook installed
sys.path.insert(0, os.path.join(ROOT, "System", "scripts"))
import secret_scan
problems += secret_scan.scan()

for rel, phrase, why in INVARIANTS:
    t = notes.get(rel, "") if rel.endswith(".md") else (open(os.path.join(ROOT, rel), encoding="utf-8").read() if os.path.exists(os.path.join(ROOT, rel)) else "")
    if phrase.lower() not in t.lower():
        problems.append(f"missing in {rel}: \"{phrase}\" ({why})")

for sk in SKILLS:
    f = os.path.join(ROOT, ".claude", "skills", sk, "SKILL.md")
    if not os.path.exists(f):
        problems.append(f"skill missing: .claude/skills/{sk}/SKILL.md")
    elif not re.match(r"---\nname: " + re.escape(sk) + r"\ndescription: ", open(f, encoding="utf-8").read()):
        problems.append(f"skill {sk}: front matter must start with name and description")

print(f"{len(notes)} notes checked, {len(INVARIANTS)} invariants.")
if problems:
    print(f"{len(problems)} problem(s):")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("OK: the vault is coherent.")
