# Reflection on attempts 1-15 (all weighted equally)

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
| 11 | 2,770 | 10,330 | 16,270 | 17,830 | 20,790 (2020) | 7 | 4-8% | 599 | 1,010 | 19 |
| 12 | 3,190 | 14,520 | 18,900 | 21,120 | 21,130 (2015) | 6 | 4-8% | 913 | 1,169 | 17 |
| 13 | 3,430 | 14,520 | 17,370 | - | 20,070 (2008) | 7 | 4-6% (factories to 12%) | 873 | 1,177 | 17 |
| 14 | 3,610 | 12,130 | 20,360 | - | 23,580 (2013) | 9 | 5-6% | 738 | 1,202 | 19 |
| 15 | 4,330 | 13,240 | 17,750 | - | 18,260 (2011) | 6 | 4-7% | 568 (dense) | 827 (dense) | 27 |

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
11. **Attempt 11 (20,790):** attempt 10's layout built up front (288 home tiles on day one, 683 by 2003)
   gave the second-fastest start (10,330 by 2005). Then stuck at 16,000 for five years: water short
   18 months, factory land ran out (1,112 home vs 489 factory tiles), then the industry cap held 137
   factory tiles empty. The **seaport** (2014) broke it: factories filled, unemployment 15% -> 4%. A tax
   test showed home demand stays positive at **8%** when jobs exist. Seven loans (~$3,000 a year) still
   outgrew all tax (~$2,100). *Lesson: seaport early, factory land in step with homes, taxes ~8% once
   the city works, and no more than ~4 loans.*
12. **Attempt 12 (21,130):** attempt 11's plans with the seaport, second plant and 7-8% taxes brought
   forward: the fastest start of all (12,030 by 2004, on the target curve 2003-2009). Then water and
   power shortages forced loans #5 and #6, unemployment rose to 12-19% (shop demand negative for ten
   years: one road link, no airport), and the city sat at ~21,000 from 2012 with land full and cash
   below zero. It spent ~$60,700 - the six loans - for 21,000 people: **~$2.90 per person**, which
   cannot reach 100,000 on the tax a growing city earns. *Lesson: the money model is the problem now:
   income per person (tax rate) and cost per person (density, layout) both have to move.*
13. **Attempt 13 (20,070):** attempt 12's start plus an east road link and a tax controller: 17,790 by
   2006, the best year 6 of all. The controller pushed factory tax to 12% while factory demand read
   maximum; factory demand then went negative, unemployment rose to 26% and the city shrank to 16,650.
   South rail + road links made no visible difference. Shops ended 30-45% abandoned (the 170-tile east
   shop block was too much); homes next to the coal plants about half abandoned. *Lesson: factory tax
   is a demand lever, not free money; keep shops near ~1/3 of homes; homes away from plants.*
14. **Attempt 14 (23,580):** attempt 13's start with low taxes (5-6%), the airport at ~20,000 and nine
   loans. It never collapsed (unemployment 4-7% throughout) and the airport visibly opened shop demand,
   but after 2005 it grew only ~1,500 people a year and each step needed a loan: ~$3.80 per person.
   *Lesson: low taxes buy stability, not speed; with light homes at ~18 people per tile the money runs
   out near 20,000-25,000 whatever the tax rate.*
15. **Attempt 15 (18,260):** every home zone dense: **26.8 people per home tile** (all light attempts
   17-20), the same city on ~40% less home land - and the same ~18,000 ceiling, with factory land empty at
   maximum demand even after a second seaport. *Lesson (from the research that followed): the stuck
   factory land failed the game's trip test.*

## Patterns across all fifteen

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
   homes last. *Attempt 11's test (2018) points the other way: at 8% home demand held while jobs were
   available; the earlier drops line up with job shortages (factory land full or capped), not tax.*
6. **Control is solved since attempt 6:** checked plans, audit, stall alarm, play loop that stops at alarms.
   Remaining control risk: batches that run past alarms (fixed in 9), calibration side effects (fixed).
7. **Fire is the recurring disaster:** attempt 3 (city), attempt 9 (power plant). Coverage from day one.
8. **Water always ran short** unless pumps were placed far ahead (2: 100+ pumps; 9: 19 at once fixed it).
9. **Debt only works sized to the city.** Every attempt with more loans than about 1 per 8,000 people
   (2, 4, 6, 10) ended with loan payments above property tax. Each loan is ~$400 a year; tax is ~$0.09
   per person a year at 7%.
10. **Factory land beyond the trade capacity is wasted.** Factory demand reads maximum all game (4, 9, 10)
   while factories stand abandoned; more factory land did not add jobs. A seaport or second link raises
   the cap. Attempt 11 confirmed it: after the seaport, factories went 524 -> 606 and unemployment
   15% -> 4%. A rail link alone was not enough.
11. **Every stall at 11,000-18,000 (3, 6, 10, 11) came with rising unemployment.** Homes empty when jobs
   run out (no factory land, or the industry cap), and home demand turns negative. Jobs, not taxes or
   home land, set the ceiling in that range. Attempt 12 adds the shop side: shop demand negative for ten
   years with a single road link and no airport.
12. **Every attempt costs ~$2.50-3.00 per person and earns ~$0.10 per person per year at 7-8%.** With
   loans at ~$400 a year each, no attempt has been able to fund growth past ~21,000 except 2 and 4,
   which borrowed 10 times and then failed on debt. Rates were left low while demand bars sat at
   maximum for years (9, 11, 12) - money left on the table.
13. **Low taxes went furthest.** The two biggest cities (2: 35,690; 4: 30,860) ran homes at 4-5% and
   factories at 3-4% while growing. Every attempt that pushed rates to 7%+ before ~20,000 (6, 9, 10, 11,
   12, 13) topped out between 7,800 and 21,000. Attempt 13 shows it directly: factory tax 9 -> 12 and
   factory demand fell from maximum to negative within two years. Attempt 11's 8% home test held for
   one year only. The debt that killed 2 and 4 came later, at 30,000+.
14. **People per home tile never moved.** Every attempt with light homes sat at 17-20 people per tile
   (2, 3, 4, 6, 9-14); the dense-only attempts 7 and 8 reached 26-31 but on tiny cities. Since roads,
   power lines, pipes and plants are paid per tile, density is the one lever on cost per person that no
   big attempt has used. Attempt 15 used it: 27 people per tile.
15. **The ~20,000 ceiling of attempts 10-15 was the trip test, not caps, taxes or money alone.** An empty
   zone only grows after a random road trip of ~33 tiles reaches a destination zone (factories need homes)
   or the map edge. `trips.py` on the stalled saves of 11, 13, 14 and 15: stuck factory land 22-33% trip
   success, home/shop land 65-100%. Every stuck area was a factory-only district (the west strip by the
   river, the south factory rows) - zoned there because it was empty land, and abandoned factories and
   rising unemployment followed. Attempts 2 and 4, the biggest cities, used thin mixed bands (attempt 1's
   lesson). The industry cap (10,000 workers per crane or link) was never reached.

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

## What this means for attempt 12
Keep attempt 11's start (it works). Fix what stopped it, in order of cost: the seaport in the first
years (~$3,200, location proven), factory land zoned with every home block (LAND check now stops the
loop), taxes up to ~8% once the city has ~5,000 people and jobs, at most 4 loans, the zoo by ~12,000.
See `attempt-12/strategy.md`.

## What this means for attempt 13
Keep attempt 12's start (best ever). Change the money model: a tax controller raises each zone's rate
while its demand is at maximum (up to 12%) and lowers it when demand turns negative; power and water are
built at 30% spare from cash, not at 10% from loans; a second road link on the east edge lifts the shop
cap; district 6 is zoned dense to test people per tile (cost per person). See `attempt-13/strategy.md`.

## What this means for attempt 14
Go back to the low-tax growth of attempts 2 and 4 on top of attempt 13's start (the best first six
years): taxes 4-5% everywhere until ~30,000 (controller capped at 6%), loans as needed for land and
plants (2 and 4 used ten), shops held near a third of home tiles, an airport at ~20,000 and a stadium at
~25,000, and the first target simply to beat 35,690. Debt gets handled at 30,000+ by raising homes
first. See `attempt-14/strategy.md`.

## What this means for attempt 15
Same proven layout and start, but **every home zone dense** from day one, so the same roads, lines, pipes
and plants house more people. Taxes moderate (6%, factories <= 7%), the airport at ~20,000, police for
land value. Success test: people per home tile above 25 by 2008. See `attempt-15/strategy.md`.

## What this means for attempt 16
Keep attempt 15's start and dense homes; **never zone factory-only land**: every factory cell sits next to
home cells (mixed district grids), checked with `trips.py` after each build and at every step (the loop
stops on weak trips). With factories filling, jobs keep pace with dense homes. See `attempt-16/strategy.md`.
