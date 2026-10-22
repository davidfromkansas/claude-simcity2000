# Claudeville 4 · Attempt 12 strategy (from claudeville-4/reflection.md)

Goal: 200,000 by Jan 2050, same map, Medium, disasters on.

## What eleven attempts show
- Peak population is ~39 people per home tile in every attempt. Attempt 6 had the most home tiles (3,085) and the best
  peak (120,770). 200,000 needs arcologies, unlocked at 120,000.
- Attempt 11 solved money (ordinances day one, loan floor, taxes 8-9%) and fire (26 stations, dispatch every burst).

## Plan
1. **Opening**: attempt 11's order to ~2012 (the same plans, same timing; it led all attempts to 2015).
2. **Homes first on all later land**: new blocks mostly dense homes (stripplan bands like RRCR / RRIR), aiming for
   3,300+ home tiles; convert empty job tiles to homes when home demand is positive and jobs are idle.
3. **Plants, pumps and fire stations on land that cannot hold zones** (shores, corners, beside plants).
4. **Money rules from attempt 11**: ordinances day one, loan floor (3,000 -> 4,000 per loan by 120,000), taxes 8-9%,
   shop tax never above 9%, transit and fire funding never cut, no build while cash < 0.
5. **At 120,000**: open the arcology menu at once, record price/size/population, and build arcologies with the loans left.
6. Read every reused plan's header and run `bot/overlap.py` before building it.
