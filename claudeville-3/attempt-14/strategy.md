# Attempt 14 strategy (from the reflection on attempts 1-13)

Goal: 100,000 people by Jan 2050. Same flat map, Medium, disasters on, loans allowed.
Built from [reflection.md](../reflection.md), which weighs all thirteen attempts equally.

## The idea: attempt 13's start, attempts 2 and 4's low taxes
The two biggest cities (2: 35,690; 4: 30,860) grew on 4-5% taxes and borrowed as they went. Every attempt
that raised rates to 7%+ before ~20,000 stopped between 7,800 and 21,000; attempt 13 watched factory
demand turn negative as its factory tax climbed to 12%. Attempt 14 keeps attempt 13's first six years
(best ever) and the low taxes, and aims first at beating 35,690.

## Schedule
| When | Build | Loans |
|---|---|---|
| Jan 2000 | `a11-day1` | #1 |
| loan #2 allowed | `a12-2003` + `a12-power1` | #2 |
| ~5,000 / land short | `a12-2003b` (seaport + pumps), `a14-east` (east block: half shops, half homes), `a13-link2` | #3 |
| ~10,000 | `a12-district5` (+ coal or gas), pumps | #4 |
| ~13,000 | zoo + dense district 6, coal | #5 |
| ~20,000 | **airport**; new home districts south (dense) | #6-7 |
| ~25,000 | **stadium**; more land, plants, pumps | #8-10 |
| ~30,000+ | raise homes first, 1 point a year while demand stays positive | - |

## Rules
1. **Taxes low** (2, 4 vs 6, 9-13): homes 4-5%, shops 4-5%, factories 3-5% until ~30,000. The tax
   controller runs with a 6% ceiling (it may lower rates, and raise to 6 at most).
2. **Shops ~1/3 of home tiles** (13): the LAND alarm for shops is answered with small blocks.
3. **Homes away from the coal plants** (13): new home land south and east; factories next to plants.
4. **Loans for land and plants** (2, 4): borrow when demand is high and land or capacity is short; up to
   10 before 30,000.
5. **Capacity ahead**: power and water built at 30% spare; the loop stops under 10%.
6. **Unlocks**: seaport ~5,000, zoo ~13,000, airport ~20,000, stadium ~25,000.
7. **Control**: checked plans run in the background with long time limits; loans via `loan.sh`; audit,
   stall, pace, land and capacity stops; all data saved; commentary logged.
