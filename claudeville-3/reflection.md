# Reflection on attempts 1-9 (all weighted equally)

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

## Patterns across all nine

1. **Population follows home land zoned early (~20 people per home tile).** The three fast attempts had
   565-650 home tiles by 2005; every other attempt had under 370 and never passed 12,000.
2. **Fast attempts borrowed early (4-6 loans by 2006) and taxed low at the start (4-5%).** Cautious
   attempts (0-3 loans, 7% tax) stalled small. Borrowing is necessary; *what failed was never raising
   income to carry it.*
3. **Every fast attempt died of something other than growth:** traffic + wiring + debt (2), fire (3),
   land value + debt (4). Each is preventable with known fixes.
4. **No attempt ever built the unlocks** (stadium/zoo/marina, seaport, airport) - and 2 and 4 both
   stalled near 30,000, the research's ~15,000-resident home cap (displayed population counts more).
5. **Demand at maximum is a signal to raise taxes**, not only to build (attempt 9: max demand held at 10%).
   Attempts 2 and 4 kept taxes at 5-8% while carrying 7-10 loans.
6. **Control is solved since attempt 6:** checked plans, audit, stall alarm, play loop that stops at alarms.
   Remaining control risk: batches that run past alarms (fixed in 9), calibration side effects (fixed).
7. **Fire is the recurring disaster:** attempt 3 (city), attempt 9 (power plant). Coverage from day one.
8. **Water always ran short** unless pumps were placed far ahead (2: 100+ pumps; 9: 19 at once fixed it).

## What this means for attempt 10
Combine attempt 4's fast start (big early zoning, low tax, early loans) with attempt 9's tax lesson,
attempt 3's fire lesson, attempt 2's water/wiring/traffic lessons, the research unlocks before ~25,000,
and the control tools from 6-9. See `attempt-10/strategy.md`.
