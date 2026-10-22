# Claudeville 3 · Attempt 15 post-mortem

**Result: missed.** Stopped in July 2011 at **18,260 people** (the peak), with 6 loans and -$1,638 cash.

| Year | People | Loans | Unemployed | Demand R/C/I |
|---|---|---|---|---|
| 2003 | 8,770 | 3 | 3% | -/max/max |
| 2005 | 13,240 | 4 | 7% | -/+/max |
| 2007 | 17,950 | 5 | 5% | -/+/max |
| 2009 | 17,250 | 6 | 13% | -/+/max |
| 2011 | 18,260 | 6 | 13% | -/-/max |

## What happened
The test was density: the proven layout with every home zone dense. **It worked for what it tests:
26.8 people per home tile** in 2008 (every light attempt: 17-20), so the city reached the same size on
~40% less home land. But it stopped at the same ~18,000. From 2008 factory zones sat empty with factory
demand at maximum (530 built, 59 empty for three years); a second, larger seaport (2008) changed nothing.
Home demand stayed negative because there were too few jobs (unemployment 13-14%).

## Control failures vs strategy failures

**Control failures:**
- **District 5 was never built** in this attempt, yet later plans assumed it (district 6's water came
  through it). The audit flagged the dry district and it was joined to the main directly; no lasting
  harm, but the build order should have been checked against the strategy table. **Fix:** the
  strategy's plan list is now checked off in `bot/run.json` ("built" list) by `build.py`.
- A plan put a seaport tile on water; the water preflight refused it before any money was spent.
- The play loop showed only the last stop reason; it now lists all of them.

**Strategy failures:**
1. **Jobs are the ceiling, not homes.** Dense homes produced residents faster than jobs; unemployment
   went from 3% to 16% in 2004 and again to 14% by 2010.
2. **The factory stall is still not understood.** Empty, powered, watered factory land with demand at
   maximum, after two seaports and two road links. This is the question for the research before
   attempt 16.

## What changes next time
Research first (what lets factory land develop), then the attempt 16 strategy.
