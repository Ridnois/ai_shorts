---
type: video-idea
status: idea
format: short
publish: 
estimated_budget_usd: 
approved_budget_usd: 
actual_cost_usd: 
video: 
hook_type: surprising fact
error: 
created: 2026-10-06
updated: 2026-10-06
tags: [youtube, pipeline, computer-science, suggestion]
---

# Why Google Maps does not check every road

← [[Pipeline]] · [[YouTube Channel]] · [[Audience]] · [[Niche map]]

**Topic family:** software and algorithms. **Y:** get there faster; trust the route. **X:** a route planner cannot check every road on a continent per request; it uses precomputed shortcuts (highways first), which is why an answer takes milliseconds.

**Demand (youtube_search, 6 Oct 2026): very strong ceiling.** "The algorithm Behind Google Maps: Dijkstra And A-star" (Brainy Byte) 51M views, 1,218x its channel median; a Wi-Fi explainer from the same channel 2.1M; copies of the topic from tiny channels at 1 to 13k, so the audience is proven and the mechanism people actually need is missing from them.

**Differentiator (the street-lamp answer):** the famous headline is "Dijkstra and A-star"; the video adds that plain Dijkstra on a whole country is too slow, and route planners use hierarchy and precomputation (contraction hierarchies and related methods in the research literature). **Honesty rule:** say "route planners use", never "Google Maps uses" unless a source states it.

**Package draft.** Promise: *your phone finds the fastest route in a blink because it ignores almost every road.* Titles: *How Google Maps Finds Your Route in Milliseconds* · *Route Planners Don't Check Every Road (Here's the Trick)* · *The Shortcut Behind Every Navigation App*. Thumbnail: a road-network map with one thin highlighted path through a faded mesh, kicker ALGORITHMS, lines **IGNORES MOST ROADS** / **FINDS YOUR ROUTE**, chips named at P3.

**Hook candidates:** surprising fact "Your phone plans a route across a country without looking at most of its roads." · stakes "A navigation app that checked every road would take minutes, not a blink." · contradiction "The fastest route is found by throwing almost every road away." · surprising number "A country has tens of millions of road segments, and an answer arrives in milliseconds." (get the figures) · question-as-claim "It is not the shortest path: it is the cheapest in time."

**Facts to verify at P1 (none read):** Dijkstra 1956, A-star 1968; size of a national road graph (OpenStreetMap or a paper); contraction hierarchies (Geisberger et al., 2008) and the survey "Route Planning in Transportation Networks" (Bast et al.); query times in the papers; what Google has published. Visual: a mesh of roads with the search frontier expanding, then the same query with highways only.

**Risks:** do not claim Google's internals; the topic is crowded by the 51M video, so the package must lead with the shortcut, not with "algorithm".
