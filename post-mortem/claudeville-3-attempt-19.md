# Claudeville 3 · Attempt 19 post-mortem

**Result: GOAL REACHED.** The city passed **100,000 people in mid-2045** (102,140 in July 2045). It peaked at
**107,460 in December 2047** and was still above the goal at the deadline: 105,990 in July 2049 and 103,330 in
July 2050. My check steps grew long late in the game and skipped January 2050 itself; the two readings either
side put it at about 104,000-105,000. It ended with 33 loans and about -$28,000 cash.

| Year | People | Loans | What changed |
|---|---|---|---|
| 2002 | 8,010 | 4 | fastest start of all attempts (dense homes + parks) |
| 2006 | 21,110 | 6 | seaport, dense east job strip |
| 2010 | 29,590 | 9 | stadium, airport, lake pumps |
| 2015 | 35,710 | 11 | plateau; six police stations |
| 2017-20 | 36,410 -> 43,190 | 13 | south-east checkerboard, second seaport, zoo #2 |
| 2025 | ~51,000 | 16 | plateau again: no land left on the east side |
| 2028 | 51,550 | 17 | **first district west of the river** (causeway + raised wires) |
| 2033 | 64,500 | 21 | west districts filling: ~5,000 people a year |
| 2040 | 83,210 | 27 | recreation cap; 15 big parks, home tax 8% |
| 2045 | 102,140 | 33 | **100,000** |
| 2047 | 107,460 | 33 | peak |

## What worked
1. **Dense homes with a park inside every home cell** (attempt 19's land-value idea). Homes averaged ~35 people
   per tile; about half the home land grew 2x2 buildings and a few hundred tiles grew towers. Towers (land value 192)
   stayed out of reach almost everywhere: mean home land value 73-79.
2. **Land, more than anything.** Every stall from 2014 on was "no empty land of the type in demand". The east side
   topped out near 51,000; crossing the river to the empty west half (a $275 causeway and $110 raised wires,
   2027) roughly doubled the buildable land and growth went from ~1,000 to ~5,000 a year.
3. **Checkerboard districts** (homes next to jobs in every direction) and the trip check before every build:
   every new district reached 80-100% trip success after at most one cheap rezone.
4. **Recreation for the home cap**: 3 zoos, 2 stadiums, a marina and 19 big parks.
5. **Dense jobs** (untried before 19): dense factory and shop cells filled within months.
6. **Loans as a growth engine.** 33 loans. The game never refused one, and negative cash had no effect beyond
   blocking builds until the next loan. Every loan paid for land or capacity that grew the city.

## Control failures vs strategy failures

**Control failures** (each fixed in the controller):
- **Half-scale first build** (the zoom-in had not taken; Jan 2000, no game time lost). Fixed: `autocal.sh` measures
  the scale with a second tile; `begin_attempt.sh` deletes an old save first (an "Overwrite?" prompt threw off
  every click).
- **Parks planned on top of lines/police stations** (twice). Fixed: `build.py` refuses parks on planned lines,
  roads or buildings.
- **Four neighbour deals ($3,900)** from roads and a line placed on the map edge, and **two more ($2,000)** from
  calibration test roads that landed on the edge. Fixed: `build.py` refuses edge tiles; `autocal.sh` keeps test
  roads (including the zoom-check road) 6+ tiles from the edge.
- **The game ran a year unwatched** (Jan 2037 -> Feb 2038): the pause click was lost during the slow year-end
  processing of a big city. Fixed: `sc run` confirms the pause and retries.
- **Power gaps the audit caught before the clock ran** (line gaps at road crossings, empty zone tiles between a
  line and a crossing, the airport not passing power, a big park that would not bulldoze cutting a line). No
  game time lost; one (the west-bank district, 2042) only showed up as a stall because the audit counts
  adjacency through planned zones. Lesson: route lines on their own tiles all the way.
- **Zone rows with no road within 3 tiles** (Dec 2044 top strip). Fixed: `build.py` refuses them.
- **A stale 7% tax floor** from 2006 pushed factory tax back up in 2028-29. Fixed by hand; floors are now per attempt.

**Strategy failures** (what cost time):
1. **Staying east of the river until 2027.** The west half was free land all along; ~12 years of plateau (2014-27)
   were spent squeezing the east side.
2. **Police for land value** (2015) halved crime but raised home land value only 73 -> 79.
3. **Factory tax at 10% and shop tax at 10%** each turned that demand negative (as in attempt 13).
4. **Debt**: by 2032 loan payments (~$10,000/yr) exceeded taxes (~$6,000). It never stopped growth here, but a
   game that refused loans would have.

## What changes next time
The goal is met. If a faster or debt-free run is wanted: cross the river by ~2010, build checkerboard districts
on both banks from the start, and use recreation (zoos, stadiums, big parks) ahead of each ~15,000 of people.
