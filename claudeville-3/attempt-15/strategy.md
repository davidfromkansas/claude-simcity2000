# Attempt 15 strategy (from the reflection on attempts 1-14)

Goal: 100,000 people by Jan 2050. Same flat map, Medium, disasters on, loans allowed.
Built from [reflection.md](../reflection.md), which weighs all fourteen attempts equally.

## The idea: the same city, dense
Fourteen attempts agree on two numbers: ~$0.10 of tax per person per year, and ~$3 of building cost per
person with light homes at 17-20 people per tile. Every attempt hit the money wall between 7,800 and
35,700. Roads, power lines, pipes and plants are paid per tile, so the only lever on cost per person that
no big attempt has pulled is **density**: attempts 7 and 8 reached 26-31 people per dense tile. Attempt
15 builds the proven layout (attempts 11-14) with every home zone dense.

## Schedule (dense versions of the proven plans)
| When | Build | Loans |
|---|---|---|
| Jan 2000 | `a15-day1` | #1 |
| loan #2 allowed | `a15-2003` + `a12-power1` | #2 |
| ~5,000 | `a12-2003b` (seaport + pumps), `a15-east`, `a13-link2` | #3 |
| ~10,000 | `a15-district5` (+ gas), pumps | #4 |
| ~13,000 | `a14-zoo`, `a14-district6`, coal | #5 |
| ~20,000 | airport, job land, power, pumps | #6-8 |

## Rules
1. **Dense homes everywhere** (7, 8, 14). Success test: >25 people per home tile by 2008; if dense
   fills too slowly (empty dense tiles pile up while home demand is positive), switch new land back
   to light.
2. **Taxes** (2, 4, 11, 13, 14): homes and shops 6%, factories <= 7% (controller ceiling 7).
3. **Capacity ahead**: plants and pumps at 30% spare; loop stops under 10%.
4. **Jobs**: seaport early, airport at ~20,000, shops ~1/3 of home tiles.
5. **Loans**: for land and capacity; stop at 8 and switch to raising homes if the deficit passes
   $2,000/yr.
6. **Control**: checked plans in the background, `loan.sh`, audit/stall/pace/land/capacity stops,
   all data saved, commentary logged.
