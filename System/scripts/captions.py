#!/usr/bin/env python3
"""Phrase captions (Playbook §4): group timed words into captions of 1 to 3 words.
  from captions import groups, html_caps
  groups(words)  words = [(text, start, end), ...] in seconds -> [[i, j, ...], ...] word indices per caption
  html_caps(words, colour=lambda text, start: "#FFFFFF")  -> HyperFrames divs: one per spoken word, showing its
      whole phrase with that word lit and the others dimmed, so timing stays word-exact (class "cap", id c<k>; the
      phrase sits in span c<k>i, which hfkit animates, and the lit word has class "on").
A caption breaks after MAX_WORDS, before passing MAX_CHARS, after . , ? ! : ; and across a silence over GAP s.
Run it to self-check:  python3 System/scripts/captions.py"""
import html

MAX_WORDS, MAX_CHARS, GAP, HOLD = 3, 16, 0.3, 0.55   # HOLD: longest pause (s) a caption stays on screen


def groups(words):
    out = []
    for i, (t, s, e) in enumerate(words):
        g = out[-1] if out else None
        if g and len(g) < MAX_WORDS and len(" ".join(words[k][0] for k in g + [i])) <= MAX_CHARS \
                and words[g[-1]][0][-1:] not in ".,?!:;" and s - words[g[-1]][2] <= GAP:
            g.append(i)
        else:
            out.append([i])
    return out


def size(text):                                       # 84 px, fitted so a phrase in Inter Black capitals stays inside 860 px
    return max(56, min(84, int(860 / (0.72 * max(len(text), 1)))))


def html_caps(words, colour=lambda t, s: "#FFFFFF", end=None):
    end = end if end is not None else words[-1][2] + 0.25
    divs = []
    for g in groups(words):
        texts = [words[k][0].strip(".,?!:;").upper() for k in g]   # punctuation breaks phrases, never shows
        for n, k in enumerate(g):
            s = words[k][1]
            nxt = words[k + 1][1] if k + 1 < len(words) else end
            e = round(min(nxt, words[k][2] + HOLD), 3)
            body = " ".join(f'<span{" class=\"on\"" if m == n else ""} style="color:{colour(t, s)};opacity:{1 if m == n else 0.45}">'
                            f'{html.escape(t)}</span>' for m, t in enumerate(texts))
            divs.append(f'<div id="c{k}" class="clip cap" data-start="{round(s, 3)}" data-duration="{round(e - s, 3)}" '
                        f'data-track-index="20" style="font-size:{size(" ".join(texts))}px"><span class="ci" id="c{k}i">{body}</span></div>')
    return "\n".join(divs)


if __name__ == "__main__":
    w = [("A", 0, .1), ("chatbot", .1, .5), ("never", .5, .8), ("looks", .8, 1.0), ("it", 1.0, 1.4), ("up.", 1.4, 1.6),
         ("It", 2.2, 2.3), ("guesses.", 2.3, 2.8), ("Supercalifragilistic", 2.9, 3.5)]
    g = groups(w)
    assert g == [[0, 1, 2], [3, 4, 5], [6, 7], [8]], g
    h = html_caps(w)
    assert h.count('class="clip cap"') == len(w) and h.count('class="on"') == len(w) and 'id="c8i"' in h
    assert size("SUPERCALIFRAGILISTIC") == 59 and size("IT") == 84
    assert all(len(" ".join(w[k][0] for k in x)) <= MAX_CHARS or len(x) == 1 for x in g)
    print("captions.py ok:", [" ".join(w[k][0] for k in x) for x in g])
