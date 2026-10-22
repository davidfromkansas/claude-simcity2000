# Attempt 11 strategy (from the reflection on attempts 1-10)

Goal: 100,000 people by Jan 2050. Same flat map, Medium, disasters on, loans allowed.
Built from [reflection.md](../reflection.md), which weighs all ten attempts equally.

## The idea: attempt 4's land, on day one, with debt sized to the city
The fast attempts (2, 3, 4) had ~600 home tiles by 2005 and borrowed early; the slow ones (5-10) did
not, and never passed 12,000 by 2010. Attempt 10 had the right idea but built a third of the land on
day one and the rest 1-2 years late. Attempt 11 builds attempt 10's whole audited layout up front.

## Schedule
| When | Build | Loans |
|---|---|---|
| Jan 2000 | Blocks 1-3 of attempt 10 at once (road + rail links, 2 coal plants on the river strip, ~330 home tiles, shops, factories, 31 riverbank pumps, 2 fire stations, police) | #1 and #2 |
| when blocks 1-3 are ~70% built (target 2001-2002) | Block 4 (south district, 264 home tiles) | #3 |
| ~5,000 people | **Seaport** on the river (factory cap; attempts 4, 9, 10 had factory demand stuck at max) | cash |
| ~10,000 | **Zoo**; third coal plant; more riverbank pumps | cash or #4 |
| ~15,000 | **Stadium**; east block (shops + homes) | cash or #5 |
| ~20,000 | **Airport**; second road link on another edge | |
| from ~15,000 | new home land **dense** next to water and parks | |

## Rules
1. **Pace** (10): `pace.json` holds the target curve; `play.sh` stops when the city is under 70% of it,
   and the answer is always land (or the cause the stall check finds), not waiting.
2. **Land ahead of demand** (2, 3, 4 vs 5-10): keep 100+ empty home tiles; never let cash sit above
   $5,000 while home demand is at maximum and land is short.
3. **Debt sized to the city** (2, 4, 6, 10): at most 2 loans until 8,000 people, then at most
   1 + population / 8,000. Repay the oldest when cash > $15,000.
   *Changed Dec 2006:* the game refused a second loan at founding, and the cap blocked land the city
   needed. New rule: a loan is taken only to buy land (with power and water) for 5,500+ people
   (~250 home tiles + jobs), the payback point from the research.
4. **Taxes** (2, 4, 6, 9, 10): start 4/4/4. Raise shops and factories first when their demand is at
   maximum; raise homes last and only while home demand stays at maximum; cut any rate whose demand
   has been below zero for a year.
5. **Ratio** (10, research): factory tiles at most ~60% of home tiles; when factory demand is at maximum
   but >10% of factories are abandoned, build trade capacity (seaport, link), not factory land.
6. **Fire, power, water, wiring** (2, 3, 9): fire station per block from day one; plants on the river
   strip; riverbank pumps in wired rows; add plants/pumps at < 30% spare.
7. **Jobs next to homes** (1): the attempt 10 bands (every home within ~15 road tiles of jobs).
8. **Control** (5-10): checked plans, audit, stall alarm, pace check, play loop that stops at alarms,
   all agreed data saved, commentary logged.

## Target curve (pace.json)
2001: 2,000 · 2003: 7,000 · 2005: 12,000 · 2010: 22,000 · 2015: 32,000 · 2020: 42,000 ·
2030: 62,000 · 2040: 82,000 · 2050: 100,000. Zoned home tiles: 330 on day one, 600 by 2002,
800 by 2005, 1,300 by 2010, then dense.
