---
type: status
updated: 2026-11-03
---

# AI websites look the same: Status

**Ask once (user, 3 Nov 2026, verbatim):** angle "5 sites, 1 design (Recommended)" · real run "Claude Code headless (Recommended)". Request: *"1"* (pick 1 of the /short-idea table).

| Stage | State |
| --- | --- |
| **Idea** | Agent at work (last video How AI works). `surprising-result`. Real thing: our runs, Claude Opus 5.5 in Claude Code 2.1.318, 3 Nov 2026: five briefs, one page (5 of 5 "See how it works"); impeccable 4.8.0 on the same five prompts gives five different pages. Demand: Coding with Lewis "Every AI Startup Website Looks the Same" 458,642 (9.3x); autocomplete "ai website design". Idea note [[Why every AI website looks the same]], score 16. |
| **Pre-flight** | 1. `surprising-result`; Lewis 9.3x. 2. Field: Lewis "Every AI Startup Website Looks the Same", "The AI Model Iceberg", "3 GitHub repos with 150,000 stars…", "WTF is going on at GitHub?", "The End of Programming"; ours is the only one with a test, a reason and a measured fix. 3. Hook "Claude Code built me five websites. They're the same website."; stake "A notes app, a budget app, a fitness band…"; 0 s the five-hero grid, 3 s the notes hero full width, 6 s the budget hero. 4. Weakest beat: scene 3 (token talk after a visual hook; 16 words, chips must move fast). 5. Prediction: above median (650 engaged at 7 d against 585.5). |
| **Script** | 167 words, 7 scenes, turn at 52 %; sources checked 3 Nov 2026 ([[Script - AI websites look the same]]). |
| **Spend** | cap $2.00. Runs on the user's Claude plan (claude.ai auth), $0 billed (the CLI's notional `total_cost_usd` about $0.4 a run is not charged). |
| **Build** | blocked before the voice (3 Nov 2026, 23:40): `.env` holds only `APIFY_TOKEN` and `GEMINI_API_KEY` since 22:03, so `voice.py` stops on `KeyError: 'REPLICATE_API_TOKEN'`; the `YT_` keys are gone too. Ready: runs, 20 real crops and screenshots in `hf/assets`, `plan.json`. |
| **Review** | |

## Not verified

The bars are counts from five runs, not token odds. The skill pages were judged by eye and by computed styles, five a side. Scene 7's advice was not run.

## Feedback
