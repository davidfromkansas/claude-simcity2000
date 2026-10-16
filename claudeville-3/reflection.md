# Reflection on attempts 1-10 (all weighted equally)

Updated before every new attempt (process rule). Each attempt gets its own entry; then the patterns
that repeat across attempts; then what that means for the next strategy.

## Side by side

| # | 2002 | 2005 | 2010 | 2015 | peak (year) | loans max | home-tax range | home tiles 2005 | home tiles 2010 | people per home tile |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 170 | 640 | 3,120 | 6,070 | 9,190 (2022) | 4 | 3-7% | 62 | 236 | 13 |
| 2 | 5,140 | 10,670 | - | 32,560 | 35,690 (2011) | 10 | 4-8% | 612 | - | 18 |
| 3 | 2,090 | 10,060 | 17,350 | - | 18,410 (2011) | 6 | 4-10% | 565 | 857 | 25 |
| 4 | 2,650 | 12,970 | 21,120 | 27,100 | 30,860 (2021) | 10 | 5-12% | 647 | 1,019 | 22 |
| 5 | 940 | 4,920 | 6,370 | - | 6,740 (2011) | 2 | 6-7% | 231 | 234 | 29 |
| 6 | 3,370 | 6,930 | 10,930 | - | 11,620 (2012) | 3 | 7-12% | 363 | 537 | 21 |
| 7 | 1,480 | 2,150 | 3,850 | - | 3,850 (2009) | 0 | 7% | 67 | 130 | 31 |
| 8 | 1,750 | 2,360 | 5,480 | - | 8,230 (2013) | 2 | 7% | 97 | 193 | 26 |
| 9 | 1,760 | 3,260 | 6,360 | 7,750 | 7,830 (2016) | 3 | 5-10% | 178 | 341 | 19 |
| 10 | 890 | 3,160 | 11,220 | 13,380 | 14,190 (2018) | 5 | 5-7% | 200 | 657 | 18 |

## What each attempt teaches

1. **Attempt 1 (9,190):** homes far from jobs; commutes failed. *Lesson: every home within ~10-15 road
   tiles of shops and factories (thin alternating bands).* Also the slowest land build-out (62 home tiles
   by 2005).
2. **Attempt 2 (35,690, the best):** zoned a whole district on day one at 4% tax, a second district in
   2002, east and south districts by 2007 (612 home tiles by 2005). Then: traffic jams, pump fields
   without power (pumps don't pass power to each other), 10 loans, bankrupt 2017. *Lesson: big early
   zoning + low tax grows fast; wiring, traffic and debt must be handled before ~30,000.*
3. **Attempt 3 (18,410):** fast too (10,060 by 2005, 565 home tiles), then an earthquake and fire burned
   the city in 2011 with one fire station and no reserve. *Lesson: fire stations in every district;
   firebreaks; cash reserve.*
4. **Attempt 4 (30,860):** the fastest early growth (12,970 by 2005, 647 home tiles), steady to 30k,
   never lost power or water; stalled because land value stayed ~25 (factories and 6 coal plants next to
   homes) and 10 loans cost more than taxes. *Lesson: fast growth works; plan land value and debt service
   for the 30k+ phase.*
5. **Attempt 5 (6,740):** neighbor link missing for 10 years, homes unpowered 2 years (parks between lines
   and zones), too many shops. *Lesson (control): verify setup from the save - led to audit/build/stall.*
6. **Attempt 6 (11,620):** clean setup, cautious land (363 home tiles by 2005), loans cost more than
   taxes at 11k. *Lesson: careful but small = slow; debt at small size is the worst of both.*
7. **Attempt 7 (3,850):** no loans at all; debt-free but tiny. *Lesson: on Medium the $10,000 start cannot
   fund growth by itself; some borrowing is required.*
8. **Attempt 8 (8,230):** research plan with unlocks and dense-only zoning; dense cost 2x and filled
   slowly on low land value (97 home tiles by 2005). *Lesson: dense zoning early is a trap; unlock
   buildings need a city big enough to need them.*
9. **Attempt 9 (7,830):** the manual's "small and profitable" start; with all three demand bars at
   maximum for 6 years there was no cash for land; demand stayed at maximum even at 8-10% tax; a power
   plant burned with no fire station. *Lesson: demand saturation means taxes can rise; one fire station
   per district from day one.*
10. **Attempt 10 (14,190):** meant to copy attempt 4's fast start, but the day-one block had ~108 home
   tiles, blocks 2 and 3 came 11-23 months late, and cash sat idle at $8,000-10,000 while home demand was
   at maximum (200 home tiles built by 2005 vs attempt 4's 647). Growth was good whenever land was empty
   (~1,500 people a year). Home demand fell to zero after taxes went to 7% at 11,000 people and never
   came back; five loans ($2,000 a year) outgrew property tax ($1,391). Factory demand sat at maximum
   while 1 in 8 buildings stood abandoned; no seaport, zoo or stadium. *Lesson: the plan must be checked
   against its own pace (now `pace.py`); idle cash with demand at maximum is wasted time; size the debt to
   the population.*

## Patterns across all ten

1. **Population follows home land zoned early (~20 people per home tile).** The three fast attempts had
   565-650 home tiles by 2005; every other attempt had under 370 and never passed 12,000 by 2010.
   Attempt 10 confirms it from the other side: same layout tools, 200 home tiles by 2005, 3,160 people.
2. **Fast attempts borrowed early (4-6 loans by 2006) and taxed low at the start (4-5%).** Cautious
   attempts (0-3 loans, 7% tax) stalled small. Borrowing is necessary; *what failed was never raising
   income to carry it.*
3. **Every fast attempt died of something other than growth:** traffic + wiring + debt (2), fire (3),
   land value + debt (4). Each is preventable with known fixes.
4. **No attempt ever built the unlocks** (stadium/zoo/marina, seaport, airport) - and 2 and 4 both
   stalled near 30,000, the research's ~15,000-resident home cap (displayed population counts more).
5. **Demand at maximum is a signal to raise taxes**, not only to build (attempt 9: max demand held at 10%).
   Attempts 2 and 4 kept taxes at 5-8% while carrying 7-10 loans. But attempts 6 and 10 both saw home
   demand drop to zero once homes went to 7% at ~11,000 people: raise shop and factory rates first,
   homes last.
6. **Control is solved since attempt 6:** checked plans, audit, stall alarm, play loop that stops at alarms.
   Remaining control risk: batches that run past alarms (fixed in 9), calibration side effects (fixed).
7. **Fire is the recurring disaster:** attempt 3 (city), attempt 9 (power plant). Coverage from day one.
8. **Water always ran short** unless pumps were placed far ahead (2: 100+ pumps; 9: 19 at once fixed it).
9. **Debt only works sized to the city.** Every attempt with more loans than about 1 per 8,000 people
   (2, 4, 6, 10) ended with loan payments above property tax. Each loan is ~$400 a year; tax is ~$0.09
   per person a year at 7%.
10. **Factory land beyond the trade capacity is wasted.** Factory demand reads maximum all game (4, 9, 10)
   while factories stand abandoned; more factory land did not add jobs. A seaport or second link raises
   the cap; nobody built one.

## What this means for attempt 10
Combine attempt 4's fast start (big early zoning, low tax, early loans) with attempt 9's tax lesson,
attempt 3's fire lesson, attempt 2's water/wiring/traffic lessons, the research unlocks before ~25,000,
and the control tools from 6-9. See `attempt-10/strategy.md`.

## What this means for attempt 11
Attempt 10's idea was right but under-executed. Attempt 11 builds the land attempt 4 had - on day one,
not over five years - using attempt 10's proven, audited layout (blocks 1-3 in Jan 2000, block 4 by
2002), with a pace file the play loop enforces. Debt is capped by population, home tax rises last, and
the cheap unlocks (seaport, zoo) come before the demand stalls rather than after. See
`attempt-11/strategy.md`.
