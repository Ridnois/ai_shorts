#!/usr/bin/env python3
"""Early signals: what AI people talk about this week, and whether the watchlist has explained it yet (stdlib, no keys).
  python3 System/scripts/signals.py [--days 7]   -> Research/Signals.md (GENERATED) and Research/signals.csv
Sources: Hacker News (Algolia API), Reddit top of the week (RSS; score = 10 x reverse rank, Reddit gives none), Hugging Face daily papers, GitHub trending.
A source that fails is reported and skipped. `explained by` lists watchlist videos (Research/radar.csv) whose title
shares the item's key term: an empty cell on a rising term is the "new term at its spike" pattern (Strategy.md §Hooks)."""
import argparse, csv, datetime as dt, html, json, os, re, sys, time, urllib.parse, urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MD = os.path.join(ROOT, "Research", "Signals.md")
CSV = os.path.join(ROOT, "Research", "signals.csv")
RADAR = os.path.join(ROOT, "Research", "radar.csv")
UA = {"User-Agent": "NextTokenResearch/1.0 (research script; contact via YouTube @yournexttoken)"}
AI = re.compile(r"\b(ai|llm|llms|gpt|chatgpt|claude|gemini|openai|anthropic|deepmind|agent|agents|model|models|"
                r"transformer|diffusion|token|inference|nvidia|gpu|mcp|copilot|cursor|codex|grok|llama|qwen|deepseek|mistral)\b", re.I)
STOP = set("the a an and or of to in on for with from by is are was be this that how why what when who your you our we "
           "new now just its it as at into over vs via can will not no more most than about after before show hn ask "
           "using use used make made best first one two three open source free".split())
NOW = dt.datetime.now(dt.timezone.utc)


def fetch(url, as_json=True):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        b = r.read().decode("utf-8", "replace")
    return json.loads(b) if as_json else b


def hn(days):
    since = int((NOW - dt.timedelta(days=days)).timestamp()); out = []
    for q in ("AI", "LLM", "agent", "Claude", "OpenAI", "GPT", "Gemini"):
        u = "https://hn.algolia.com/api/v1/search?" + urllib.parse.urlencode(
            {"query": q, "tags": "story", "numericFilters": f"created_at_i>{since},points>100", "hitsPerPage": 50})
        for h in fetch(u)["hits"]:
            out.append(dict(source="HN", title=h["title"], score=h.get("points", 0), comments=h.get("num_comments", 0),
                            url=f"https://news.ycombinator.com/item?id={h['objectID']}"))
    return out


def reddit(days):
    """The JSON API answers 403 to scripts (3 Nov 2026); the RSS feed works but carries no score: rank = position."""
    t = "week" if days <= 7 else "month"; out = []
    for n, sub in enumerate(("LocalLLaMA", "singularity", "ChatGPT", "ClaudeAI", "artificial")):
        if n: time.sleep(3)  # Reddit answers 429 to back-to-back feeds
        try: feed = fetch(f"https://www.reddit.com/r/{sub}/top/.rss?t={t}&limit=25", as_json=False)
        except Exception as e:
            print(f"r/{sub}: {e}"); continue
        entries = re.findall(r"<entry>(.*?)</entry>", feed, re.S)
        for k, e in enumerate(entries):
            title = html.unescape(re.search(r"<title>(.*?)</title>", e, re.S).group(1))
            link = re.search(r'<link href="([^"]+)"', e)
            out.append(dict(source=f"r/{sub}", title=title, score=max(25 - k, 1) * 10, comments=0,
                            url=link.group(1) if link else ""))
    return out


def hf(days):
    out = []
    for k in range(min(days, 7)):
        day = (NOW - dt.timedelta(days=k)).strftime("%Y-%m-%d")
        try: d = fetch(f"https://huggingface.co/api/daily_papers?date={day}")
        except Exception: continue
        for p in d:
            pp = p.get("paper", {})
            out.append(dict(source="HF papers", title=pp.get("title", p.get("title", "")), score=pp.get("upvotes", 0),
                            comments=p.get("numComments", 0), url=f"https://huggingface.co/papers/{pp.get('id', '')}"))
    return out


def github(days):
    since = "weekly" if days <= 7 else "monthly"
    page = fetch(f"https://github.com/trending?since={since}", as_json=False); out = []
    for art in re.findall(r'<article class="Box-row">(.*?)</article>', page, re.S):
        m = re.search(r'<h2[^>]*>\s*<a[^>]*href="/([^"]+)"', art, re.S)
        if not m: continue
        desc = re.search(r'<p class="col-9[^"]*">(.*?)</p>', art, re.S)
        stars = re.search(r'([\d,]+)\s+stars? this', art)
        text = html.unescape(re.sub(r"<[^>]+>|\s+", " ", desc.group(1)).strip()) if desc else ""
        out.append(dict(source="GitHub", title=f"{m.group(1)}: {text}"[:160], score=int(stars.group(1).replace(",", "")) if stars else 0,
                        comments=0, url="https://github.com/" + m.group(1)))
    return out


def terms(title):
    """Key terms: acronyms, capitalised names and model ids; lower-case common words are dropped."""
    ws = re.findall(r"[A-Za-z][\w.\-+]*\d[\w.\-]*|[A-Z]{2,}[\w\-]*|[A-Z][a-z]+(?:[A-Z][a-z]+)+|[A-Z][a-z]{3,}", title)
    return [w for w in dict.fromkeys(ws) if w.lower() not in STOP and len(w) > 2]


def main():
    p = argparse.ArgumentParser(); p.add_argument("--days", type=int, default=7); p.add_argument("--top", type=int, default=40)
    a = p.parse_args()
    items, notes = [], []
    for name, fn in (("Hacker News", hn), ("Reddit", reddit), ("Hugging Face papers", hf), ("GitHub trending", github)):
        try:
            got = fn(a.days); items += got; notes.append(f"{name}: {len(got)}")
        except Exception as e:
            notes.append(f"{name}: FAILED ({type(e).__name__}: {str(e)[:60]})")
    seen, uniq = set(), []
    for it in sorted(items, key=lambda x: -x["score"]):
        k = it["url"]
        if k in seen: continue
        seen.add(k)
        if it["source"] not in ("HF papers", "r/LocalLLaMA", "r/ClaudeAI") and not AI.search(it["title"]):
            continue  # off-topic for an AI channel
        uniq.append(it)
    radar = list(csv.DictReader(open(RADAR, encoding="utf-8"))) if os.path.exists(RADAR) else []
    rt = {}
    for r in radar: rt[r["video_id"]] = r
    for it in uniq:
        ts = terms(it["title"]); it["terms"] = ", ".join(ts[:4]); hits = []
        for t in ts[:4]:
            rx = re.compile(r"\b" + re.escape(t) + r"\b", re.I)
            hits += [f"{r['handle']} ({float(r['ratio']):.1f}x)" if r["ratio"] else r["handle"]
                     for r in rt.values() if rx.search(r["title"])]
        it["explained"] = ", ".join(dict.fromkeys(hits[:3]))
    stamp = NOW.strftime("%Y-%m-%dT%H:%MZ")
    new = not os.path.exists(CSV)
    with open(CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["pulled_at", "source", "title", "score", "comments", "terms", "explained", "url"])
        if new: w.writeheader()
        for it in uniq: w.writerow(dict(pulled_at=stamp, **{k: it[k] for k in ("source", "title", "score", "comments", "terms", "explained", "url")}))
    L = ["---", "type: research", f"updated: {NOW:%Y-%m-%d}",
         "status: GENERATED by System/scripts/signals.py; do not edit by hand", "---", "",
         "# Signals: what AI people talk about this week", "",
         "← [[Strategy]] §Ideas · [[Radar]] · [[Channels]]", "",
         f"Pulled {stamp}, last {a.days} days. Sources: " + " · ".join(notes) + ".",
         "**Unexplained** = no watchlist video shares the key term yet: a candidate for the new-term pattern. "
         "A signal is a lead, never demand: demand is still 2 or more outliers in [[Radar]] or an autocompleting question.", ""]
    for head, cond in (("Unexplained", lambda i: not i["explained"]), ("Already explained on the watchlist", lambda i: i["explained"])):
        g = [i for i in uniq if cond(i) and i["terms"]][: a.top]
        L += [f"## {head} ({len(g)})", "", "| score | source | item | key terms | explained by |", "| --- | --- | --- | --- | --- |"]
        for i in g:
            L.append(f"| {i['score']:,} | {i['source']} | [{i['title'].replace('|', '/')[:110]}]({i['url']}) | {i['terms']} | {i['explained']} |")
        L.append("")
    open(MD, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("SIGNALS " + " · ".join(notes) + f" -> {len(uniq)} items -> {os.path.relpath(MD, ROOT)}")


if __name__ == "__main__":
    main()
