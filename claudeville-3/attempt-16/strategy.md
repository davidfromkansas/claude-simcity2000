# Attempt 16 strategy (from the reflection on attempts 1-15)

Goal: 100,000 people by Jan 2050. Same flat map, Medium, disasters on, loans allowed.
Built from [reflection.md](../reflection.md), which weighs all fifteen attempts equally, and the trip research.

## The idea: dense homes, and factories only where trips succeed
Attempts 10-15 all stopped at 18,000-24,000 with factory land empty at maximum demand. The game's growth
code explains it: an empty zone grows only after a random road trip (~33 road tiles) reaches a destination
zone - homes, for a factory - or the map edge. On our stalled saves the stuck factory land had 22-33% trip
success; it was always in factory-only districts. Attempt 16 keeps attempt 15's start (dense homes, 27 people
per tile) and puts every factory cell next to homes.

## Schedule
| When | Build | Loans |
|---|---|---|
| Jan 2000 | `a15-day1` (dense) | #1 |
| loan #2 allowed | `a15-2003` (dense blocks 3+4) + `a12-power1` | #2 |
| ~5,000 | `a12-2003b` (seaport + pumps), `a15-east`, `a13-link2` | #3 |
| ~10,000 | `a16-district5` (mixed cells, dense, gas), pumps | #4 |
| ~13,000 | `a14-zoo`, `a14-district6` (dense), coal | #5 |
| ~20,000 | airport; further districts as mixed grids south and east | #6+ |

## Rules
1. **No factory-only land** (1, 2, 4 vs 10-15): factory cells only inside mixed grids, each next to a
   home cell; run `trips.py` after every zoning build; the play loop stops on "TRIPS: weak".
2. **Dense homes** (15): 27 people per tile; cuts roads/lines/pipes per person.
3. **Taxes 5-7%** (controller ceiling 7%).
4. **Capacity ahead**: plants and pumps at 30% spare; loop stops under 10%.
5. **Unlocks**: seaport early, zoo before 15,000, airport ~20,000, stadium ~25,000.
6. **Loans** for land and capacity only; at most 8 before 30,000.
7. **Control**: checked plans in the background, `loan.sh`, audit/stall/pace/land/capacity/trip stops,
   built-plan list in run.json, all data saved, commentary logged.
