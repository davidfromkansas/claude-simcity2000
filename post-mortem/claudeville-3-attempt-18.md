# Claudeville 3 · Attempt 18 post-mortem

**Result: missed.** Stopped in November 2016 at 27,920 people (**peak 28,920**, Feb 2015), with 9 loans and
-$3,876 cash. Attempt 17's plan replayed with finance ordinances (from 2006) and a 7% home-tax floor.

| Year | People | Loans |
|---|---|---|
| 2004 | 11,100 | 4 |
| 2006 | 19,790 | 7 |
| 2010 | 24,020 | 8 |
| 2015 | 28,920 (peak) | 9 |

## What happened
The replay ran slower in the first years (loan #2 came seven months later than in attempt 17: the shop/factory
land alarm fired later), then tracked attempt 17 closely and reached the same plateau: ~29,000, unemployment
11-14%, home demand around -1,100 with 200-300 empty dense home tiles, factory demand at maximum with 30-70
empty factory tiles that filled slowly. Ordinances cut the yearly deficit from ~$2,000 to ~$1,200; raising homes
to 7% in 2014 did not change growth either way.

## Control failures vs strategy failures

**Control failures:**
- **I forgot to raise the home-tax floor at ~15,000** as the strategy said; it was raised in 2014. Logged.
- **The second seaport (strategy item 3) was never built.** Both slips were in steps that had no automatic
  trigger. **Fix:** strategy items tied to a population now go into `pace.json` as reminders that the pace
  check prints when the population passes them.
- District 5's fire station and police station were planned on lots that grew buildings before the plan
  ran (both caught by the build check).

**Strategy failures:**
1. **The ~29,000 plateau is reproducible** (17: 29,090; 18: 28,920) - the plan, not luck, sets it.
2. **Homes outrun jobs with dense zoning** (unemployment 11-14% for ten years) while new job land arrives in
   expensive whole districts.

## What changes next time
See `claudeville-3/reflection.md` and the attempt 19 strategy.
