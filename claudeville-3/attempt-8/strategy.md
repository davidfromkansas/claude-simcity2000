# Attempt 8 strategy (built on the research, not guesses)

Goal: 100,000 people by Jan 2050. Same flat map, Medium, disasters on, loans allowed.
Based on [the research report](../research/README.md) and lab tests on our own map.

## What we now know
- **The game caps growth until you build "unlocks".** Homes stall around 15,000 residents until there
  is a stadium, zoo or marina, and more of them lift it further. Factories need a **rail or highway
  link off the map edge** or a **seaport** (a road link does not count). Shops need road links and,
  from about 20,000 people, an **airport**. We never built any of these in attempts 1–7.
- **Lab tests on our map:**
  - rail link $1,500;
  - seaport $150 per tile, and it builds on our river;
  - marina $1,000, placed across the riverbank;
  - stadium $5,000 (4×4); zoo $3,000 (4×4).
- **Tax income is fixed by the game** at about 1.29 × population × tax rate, roughly $0.10 per person
  per year at 7%. A loan pays for itself only if it adds about 5,500+ people.
- **Density decides how much land 100,000 people need.**
  - Dense homes hold 30–40 people per tile; light homes about 10–18.
  - That means about 3,300 dense home tiles, against ~5,600 light ones.
  - Dense homes need water, land value (trees, parks, the river, no nearby factories) and corner road access.
- **Trips:** every building must reach the other two zone types within about 33 road tiles, or it decays.

## Milestone plan (build each unlock BEFORE the city reaches it)

| When | Build | Approx. cost |
|---|---|---|
| Day one | Road link + **rail link**, coal plant, dense homes, factories, small shop strip, riverside pumps | ~$11,000 (one loan) |
| ~3,000 people | Fire station; seaport on the river if factory demand stalls | $500 / $3,000 |
| ~10,000 | First **marina** (cheapest unlock) and a **stadium or zoo**; second road link on another edge | $1,000 + $3,000–5,000 |
| ~15,000 | Seaport if not built; schools; second power plant | $3,000+ |
| ~20,000 | **Airport**; another marina or zoo | ~$5,000 |
| every +15,000 | One more stadium, zoo or marina; power and water ahead of need | $1,000–5,000 |
| 2020+ | Microwave plant ($28,000, 1,600 MW) when coal plants age or power runs short | |

Target curve: 15,000 by 2010, 35,000 by 2020, 60,000 by 2030, 85,000 by 2040, 100,000 by 2050.

## Rules
1. **Loans: one on day one, then only for a named unlock or a block that will add 5,500+ people.**
   At most 3 at a time. Repay the oldest when cash passes $15,000.
2. **Taxes 7%** (6% for a zone whose demand needs help; never above 9%; factories ≤ 7%).
   Turn on the money ordinances from about 30,000 people.
3. **Dense zoning only** for homes and shops. Homes ≈ shops + factories; early on ~3 factory tiles per shop tile.
4. **Compact districts:** every home within ~30 road tiles of shops and factories; rail through the
   city when traffic or trips fail.
5. **Land value:** homes along the river, trees and small parks inside home blocks (never between a
   power line and a zone), factories downwind at the far side with shops between.
6. **Water and power ahead of need:** pumps beside the river; ~1 MW per 3 tiles.
7. **Measure early:** people per dense tile, land value and demand after each unlock. Record each in the
   journal so the numbers become our own.
8. **Controller:** every build is a checked `build.py` plan; `step.sh` runs the audit (now with
   demand-cap warnings) and the stall alarm every 3–4 game months.
