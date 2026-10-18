# Attempt 12 strategy (from the reflection on attempts 1-11)

Goal: 100,000 people by Jan 2050. Same flat map, Medium, disasters on, loans allowed.
Built from [reflection.md](../reflection.md), which weighs all eleven attempts equally.

## The idea: attempt 11's start, with jobs and money fixed
Attempt 11's day one (288 home tiles) and early blocks gave the second-fastest start of all attempts.
Every stall between 11,000 and 18,000 (attempts 3, 6, 10, 11) came with rising unemployment: factory land
ran out or hit the industry cap. Attempt 11's seaport broke that cap; its tax test showed homes hold at
8% when jobs exist. Attempt 12 keeps the start and brings the seaport, factory land and higher taxes
forward by about ten years, with no more than four loans.

## Schedule (plans proven in attempt 11)
| When | Build | Loans |
|---|---|---|
| Jan 2000 | Day one (`a11-day1`): 288 home tiles, shops, factories, coal plant, 2 fire stations, 12 pumps | #1 |
| when the game allows loan #2 (~2003) | Blocks 3 + 4 (`a12-2003`): +395 home tiles, east factory strip | #2 |
| power/water < 10% | Gas plant + pumps (`a11-power1`), then coal + 19 pumps + **SEAPORT** (`a12-2004`) | #3 |
| land short (~2006) | District 5 + west factory strip + third coal plant (`a12-district5`) | #4 |
| ~12,000 | **Zoo** + district 6 (`a11-district6`) from cash | - |
| factory land short | South factory cells (`a11-factories2`), more pumps | cash |
| ~20,000 | **Airport** (shop cap warning appeared at 20,000 in attempt 11); stadium at ~25,000 | cash |
| after | new home land dense, by water and parks; a zoo/stadium every ~15,000 | cash |

## Rules
1. **Jobs set the ceiling** (3, 6, 10, 11): factory land is zoned with every home block (about 1 factory
   tile per 2 home tiles); the LAND check stops the loop when any zone type with high demand has no
   empty land; when factory demand is at max with empty factory land, build trade capacity (seaport
   first, then a second link).
2. **Taxes** (2, 4, 9, 11): 4/4/3 until ~5,000 people, then 7/7/7, then 8/8/8 at ~10,000 if home
   demand stays positive; cut a rate only if its demand is negative for a year *and* unemployment is low.
3. **Loans** (2, 4, 6, 10, 11): at most 4, all before ~2007, each buying land/plants for 5,500+ people.
   After that everything is paid from cash; repay the oldest loan when cash > $15,000.
4. **Pace, land, water, power** (5-11): `play.sh` stops on PACE behind, LAND short, spare water/power
   under 10%, audit FAIL, unpowered buildings, new rubble.
5. **Fire** (3, 9): fire station per block from day one.
6. **Unlocks** (research, 11): seaport by ~2004, zoo by ~12,000, airport ~20,000, stadium ~25,000.
7. **Control** (5-11): checked plans, audit, stall, pace and land checks, all data saved, commentary.

## Target curve (pace.json)
2001: 1,400 · 2003: 5,000 · 2005: 10,000 · 2010: 20,000 · 2015: 30,000 · 2020: 40,000 ·
2030: 60,000 · 2040: 80,000 · 2050: 100,000.
