# Attempt 10 strategy (from the reflection on attempts 1-9)

Goal: 100,000 people by Jan 2050. Same flat map, Medium, disasters on, loans allowed.
Built from [reflection.md](../reflection.md), which weighs all nine attempts equally.

## The idea: attempt 4's fast start, carried past 30,000
Every attempt that grew fast zoned ~600 home tiles by 2005, started at 4-5% tax and borrowed early
(attempts 2, 3, 4). Every cautious attempt stalled under 12,000. The fast ones then died of known,
preventable things: debt they never raised income to carry (2, 4), fire (3), traffic and wiring (2),
low land value and no unlocks near 30,000 (2, 4). Attempt 10 copies the fast start and fixes each killer.

## Schedule (attempt 4's pace)
| When | Build | Loan |
|---|---|---|
| Jan 2000 | Block 1: road + rail links, coal plant on the river strip, light homes/shops/factories bands, riverbank pumps, pipe main, **fire station** | #1 |
| Jan 2002 | Block 2 south: same bands, second coal plant, police station, more pumps, **fire station** | #2 |
| Jan 2003 | Block 3 east + a wired pump field (two pump rows with a power line between) | #3 |
| ~10,000 | **Seaport** on the riverbank; **marina** | (cash) |
| ~15,000 | **Zoo**; schools; hospital | #4 if needed |
| ~20,000 | **Airport**; second road link on another edge | |
| ~25,000 | **Stadium**; rail or a second avenue through the busiest blocks | #5 if needed |
| every +15,000 | another zoo/stadium/marina; a block of homes by the river or lakes | |

Target curve: 2005: 12,000 · 2010: 22,000 · 2020: 40,000 · 2030: 65,000 · 2040: 85,000 · 2050: 100,000.

## Rules (each from a specific attempt)
1. **Land ahead of demand** (2, 3, 4 vs 5-9): keep at least ~100 empty zoned home tiles; zone the next block
   when the current one is ~80% built. Light zoning; dense only for new home blocks by water after ~25,000.
2. **Taxes** (2, 4, 9): start homes 5%, shops 4%, factories 4%. Every January: if loan interest is over half of
   property tax, raise the rate of every zone whose demand is at maximum by 1-2 points (up to 10%); lower a
   zone's rate if its demand goes negative for a year.
3. **Loans** (2, 4, 6, 7): up to 3 in the first 3 years for blocks and plants; after that only when demand is at
   maximum and land is nearly full, at most 6 in total; repay the oldest whenever cash > $15,000.
4. **Fire** (3, 9): a fire station in every block from day one, near power plants too; volunteer fire ordinance.
5. **Power and water** (2, 4, 9): coal plants on the river strip west of the avenue, away from homes; pumps on
   the riverbank in wired rows; add both when spare capacity < 30%.
6. **Jobs next to homes** (1): thin alternating bands, every home within ~15 road tiles of shops and factories.
7. **Land value** (4, research): homes on the river and lake sides, small parks at band ends (never between a
   line and a zone), factories and plants on the far side.
8. **Unlocks before caps** (2, 4, research): seaport, marina, zoo, airport, stadium by the populations above.
9. **Control** (5-9): every build a checked plan; `play.sh` loop (stops at alarms); all agreed data saved;
   commentary logged.
