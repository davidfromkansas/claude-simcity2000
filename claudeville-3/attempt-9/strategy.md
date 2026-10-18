# Attempt 9 strategy (from the official manual + attempts 1-8)

Goal: 100,000 people by Jan 2050. Same flat map, Medium, disasters on, loans allowed.
Based on [the manual notes](../research/manual-notes.md) and [the research report](../research/README.md).

## The idea: the manual's own method
"Stay small, go easy on infrastructure, get into the black, build a reserve. Design one compact
neighborhood that runs at a profit, then copy it." (manual p.119-120). Every earlier attempt built
ahead of income. Attempt 9 grows module by module, each one paid for and filling before the next.

## The module (copied across the map)
A block of 6x6 squares between roads (the largest area that fully develops, p.105), with
**homes ≈ shops + factories**, more factories than shops while small (p.120):
- 3 home squares (108 tiles) · 2 factory squares (72) · 1 shop square (36), shops toward the centre.
- One power line per zone column (lines use power, p.102), crossing every road it meets.
- Pumps only on the riverbank (2-3x output, p.110), joined to a pipe main.
- **Light zoning ($5/tile)** for the first modules; dense zoning only for new home squares once water is
  steady and land value has risen (near the river and parks), from about 15,000 people.

## Day one ($10,000 + one $10,000 loan)
Road link + **rail link** (industry, p.102/107), coal plant away from homes, module 1 (above), 6 riverbank
pumps, pipe main. About $10,500. Taxes 7%. Parking fines + sales tax on from day one (largest small-city
earners after income tax; they only slightly slow commerce, which matters little while small).

## Growth rules
1. **Copy a module only when** the last one is ≥80% built and the demand bars ask for it; size jobs vs
   homes by the bars (p.120).
2. **Loans:** day one, then at most one more per ~5,000 people of real growth; never more than 3
   outstanding; never if January tax income < 2x total interest. Repay the oldest when cash > $15,000.
3. **Unlocks before caps:** police station ~4,000 (land value, crime); first **marina** ~5,000 (cheap,
   boosts homes); **seaport** when factory growth slows (by ~10,000); **stadium or zoo** by ~12,000 and
   one more per +15,000; **airport** at ~20,000; schools/hospital from ~10,000.
4. **Water and power ahead of need:** add pumps when spare water < 30%; second plant when spare power
   < 30% (oil pollutes half as much as coal; microwave from 2020).
5. **Income check every January:** property tax vs interest and running costs; 1% income tax only if the
   budget is negative and home demand is at maximum.
6. Controller as before: every build is a checked `build.py` plan; `step.sh` every 3-4 game months.

## Target curve (checked every January)
2005: 8,000 · 2010: 18,000 · 2020: 40,000 · 2030: 65,000 · 2040: 85,000 · 2050: 100,000.
If a check is 30% under the curve two years running, stop and find out why before building more.
