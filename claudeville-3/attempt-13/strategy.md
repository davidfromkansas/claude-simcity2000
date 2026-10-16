# Attempt 13 strategy (from the reflection on attempts 1-12)

Goal: 100,000 people by Jan 2050. Same flat map, Medium, disasters on, loans allowed.
Built from [reflection.md](../reflection.md), which weighs all twelve attempts equally.

## The idea: attempt 12's start, with a new money model
Attempt 12 had the best start of all twelve attempts and stalled at ~21,000 for the same reason as
2, 4, 6, 10 and 11: each person costs ~$2.90 to house and pays ~$0.10 a year in tax, and the loans that
pay for the start cost more than the city earns. Attempt 13 keeps the start and moves both sides of
that equation: income per person (taxes follow demand, up to 12%) and cost per person (dense homes,
jobs uncapped so homes stay full).

## Schedule (plans proven in attempts 11-12)
| When | Build | Loans |
|---|---|---|
| Jan 2000 | `a11-day1` | #1 |
| loan #2 allowed (~2002) | `a12-2003` (blocks 3+4) + `a12-power1` (coal #2 + pumps) | #2 |
| ~6,000 / shop land short | `a12-2003b` (seaport + 19 pumps) + `a10-block5` (east shops) + `a13-link2` (east road link) | #3 |
| ~10,000 / land short | `a12-district5` (district 5, west factories, coal #3) | #4 |
| spare < 30% | pumps (`a11-pumps4`, `a11-pumps5`), coal #4 (`a12-power2`) - from cash | - |
| ~13,000 | zoo + district 6 **dense** (`a13-district6-dense`) - from cash, loan #5 only if not | (#5) |
| land short | `a11-factories2`; new districts south (dense homes) | cash |
| ~20,000 | airport if shop demand stays negative; stadium ~25,000 | cash |

## Rules
1. **Taxes follow demand** (9, 11, 12): `taxctl.py` runs every step - a zone's rate goes up 1 while its
   demand is >= 1,800 (max 12%), down 1 after two checks at <= -300 (min 5%), from 3,000 people.
   Start 4/4/3.
2. **Capacity ahead** (2, 9, 11, 12): build power and water when spare drops under 30%, paid from cash;
   the loop still stops hard under 10%.
3. **Jobs uncapped** (3, 6, 10, 11, 12): seaport by ~6,000, second road link with the east shops,
   factory land with every home block (LAND check at demand >= 1,000), airport when shop demand stays
   negative past ~20,000.
4. **Loans** (2, 4, 6, 10, 11, 12): four for the start; a fifth only for the zoo before 15,000. None
   after; repay the oldest when cash > $15,000.
5. **Density** (7, 8, 12): district 6 dense as a test; if it fills at 25+ people per tile, all new home
   land is dense.
6. **Fire, control** (3, 5-12): fire stations per block; checked plans, audit, stall, pace, land and
   capacity stops, all data saved, commentary logged.

## Target curve (pace.json)
2001: 1,400 · 2003: 5,000 · 2005: 12,000 · 2010: 22,000 · 2015: 32,000 · 2020: 42,000 ·
2030: 62,000 · 2040: 82,000 · 2050: 100,000.
