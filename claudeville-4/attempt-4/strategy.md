# Claudeville 4 · Attempt 4 strategy (from claudeville-4/reflection.md)

Goal: 200,000 by Jan 2050, same map, Medium, disasters on.

## What the first three attempts show
- **Shops capped every city near 75-97,000**, with shop demand negative for 10-20 years.
  - A road link to a neighbour covers ~2,000 shop workers; a developed airport covers ~10,000.
  - **Only attempt 1's airports ever developed.** Its 2008 airport sat inside the city, with power touching it and the stadium beside it. Its 2026 airport had a power line along its whole west side.
  - In attempts 2 and 3 the airport zone stayed empty for 11-28 years. Its line touched only one corner tile. Attempt 3's second airport was zoned while shop demand was already negative.
- **Money:** loans outran tax in all three (game over at -$100,000: attempt 1 in 2031, attempt 2 in 2039; attempt 3 is heading the same way).
- **Fires:** three great fires in three attempts (two at the airport, one in the coal cluster by the seaport). Each forced a ~$25-45k rebuild.

## Plan
1. **Airport early and wired properly.**
   - Zone it at ~12-15,000 people, while shop demand is positive.
   - Run a power line along one full side and a road along another.
   - Give it its own fire station. Put it at the city's edge, not in the middle and not on far bare land.
   - Check every year that it develops. If it is still empty after 2 years, move it.
2. **Road links on all four edges** by ~20,000 people (~$1,000 each; +2,000 shop workers each).
3. **Taxes:** homes at 10-11% while home demand is at its maximum (2000-2012 in every attempt). Shops and factories at 8%. Never cut below 7%.
4. **Loans:** the 2050 projection guard (`loan.sh`).
5. **Coal plants spread out, not in one cluster**, each with a fire station beside it. The 2023 fire started in a cluster of 4 coal plants.
6. **Build order:** attempt 3's sequence, with the dependencies kept in order (west2 before the west shops). `seq.sh` runs it; check `audit.py` after each step.
