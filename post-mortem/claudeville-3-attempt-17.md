# Claudeville 3 · Attempt 17 post-mortem

**Result: missed.** Stopped in November 2013 at 28,320 people (**peak 29,090**, Feb 2013), with 11 loans.
The best city since attempt 2 (35,690 in 2011) and the fastest of all seventeen attempts through 2010.

| Year | People | Loans | Unemployed |
|---|---|---|---|
| 2002 | 6,600 | 3 | 1% |
| 2004 | 16,230 | 5 | 5% |
| 2006 | 21,830 | 7 | 9% |
| 2008 | 24,640 | 9 | 11% |
| 2010 | 26,530 | 10 | 11% |
| 2013 | 29,090 (peak) | 10 | 9-12% |

## What happened
Attempt 16's plan with more job land, police and a 6% home-tax floor: 16,230 people by 2004 and 21,830 by
2006, far ahead of every other attempt. Every new district was mixed (factories next to homes; district 7 a
checkerboard) and the trip check caught two layout mistakes before the clock ran (a factory row next to
factories in attempt 16's plans; a dead-end road in the west strip, 0% trips). The airport (2006) and a
stadium (2011) went in before their caps. After 2006 growth slowed to ~1,000 a year: each new block needed a
loan, eleven loans left a ~$2,000-a-year deficit, and from 2012 factory land stopped filling (~60 empty
tiles at maximum demand, ~9,300 factory workers).

## Control failures vs strategy failures

**Control failures:** none that cost game time. The checks did their job: a road on water refused by the
preflight, a police station planned on a lot that had grown a house (moved), cash running out mid-plan
(clock held until finished), a dead-end road caught by the trip check. One plan step (the north rezone)
reported "problems" that were only lots already built - harmless.

**Strategy failures:**
1. **Money.** ~$110,000 (eleven loans plus tax) for 29,000 people: ~$3.80 per person. Homes taxed 6%,
   no finance ordinances this time (attempts 12-14 showed +$300-400 a year from them).
2. **Late growth limited by job land and its cost** - every factory cell has to sit next to homes, so new
   land always comes as a whole mixed district with roads, lines and pipes.
3. **The late factory stall is not explained** (trip success 67%, ~9,300 workers vs ~20,000 of trade
   capacity by the spec's numbers).

## What changes next time
See `claudeville-3/reflection.md` (all seventeen attempts) and the attempt 18 strategy.
