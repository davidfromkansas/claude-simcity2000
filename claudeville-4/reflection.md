# Reflection for Claudeville 4 (200,000 by Jan 2050)

Updated before every new attempt (process rule), weighing ALL earlier attempts equally. It starts from the
19 Claudeville 3 attempts on the same map (full detail in `claudeville-3/reflection.md` and the post-mortems).

## What Claudeville 3 established (attempts 1-19)
1. **Money was not the ceiling at 100,000; land and the game's caps were.** Attempts 2, 4 and 6 died of debt only
   because they stopped borrowing. Attempt 19 carried 33 loans. **But Claudeville 4 attempt 1 found the limits:**
   the game refuses bond #51, and at about -$100,000 cash it throws the mayor out and ends the game.
2. **Trips decide whether land grows.** Factory-only districts stalled attempts 10-15 near 20,000. Checkerboard
   districts (homes next to shops/factories) plus `trips.py` before each build fixed it (attempt 16 on).
3. **Caps:** homes stall without zoos/stadiums/marina ahead of each ~15,000 people (attempt 2's 35,690 ceiling and
   attempt 19's dip at ~85,000); factories need a seaport/rail; shops need an airport after ~20,000.
4. **Dense homes + a park in every home cell** gave the fastest start of all attempts (attempt 19: 8,010 by 2002)
   and ~35 people per home tile. Towers (land value 192) stayed rare: homes sat at land value 70-80, police and
   City Beautification moved them only a few points.
5. **The east bank holds ~51,000.** Attempt 19 sat on that plateau 2014-2027 until it crossed the river with a $275
   causeway and $110 raised wires; growth jumped to ~5,000 a year and the west half carried it past 100,000.
6. **Dense jobs** fill within months; factory tax above ~8% and shop tax above ~9% turn their demand negative.
7. **Water and power** run short every ~2 years in a growing city: riverbank/lake pump rows and coal plants
   next to each other are cheap, reliable fixes.
8. **Control failures cost real money and time** (edge tiles = $1,000 neighbour deals, lost pauses, parks on lines,
   zones out of road reach). All now have checks in `build.py`, `autocal.sh` and `sc`.

## The gap to 200,000
Attempt 19 used most of the map at ~35 people per home tile and peaked at 107,460. Doubling that needs:
- **Every buildable tile in use from early on** (both banks by ~2006, a whole-map 6x6 grid, no wasted strips).
- **More people per tile**: towers need land value 192 - waterfront + big parks + police + low pollution cells.
- **Arcologies** (unlock at 120,000 people per the manual): each Plymouth arcology houses tens of thousands on a
  4x4 lot. Not yet tested on this map - research first.
- **Recreation far ahead** of the cap (~13 zoo/stadium-equivalents for 200,000).
- **Time:** reaching 120,000 by ~2040 leaves ten years for arcologies.

## Claudeville 4 attempt 1 (peak 87,090 - mayor thrown out Jan 2031)
- The fast start worked: 25,450 by 2007, 45,530 by Apr 2011 (both ahead of attempt 19), river crossed in 2006.
- **Two plane crashes at the airport (Apr 2011, Feb 2023) each burned the whole east bank.** 3 fire stations for up
  to 78,000 people; bulldozed firebreaks 1, 2 and 4 tiles wide were all jumped. Each rebuild cost ~$40-45k and
  3-5 years of growth. The airport zone regrows by itself after a fire.
- **Debt became fatal**: 41-48 loans cost $25-28k a year against $7k of taxes; bond cap 50 hit in 2028; cutting
  taxes to 2% after that sped the slide to -$108k and the game ended in Jan 2031.
- Controller lessons: cash guard in build.py (stops under $100), rubble cleared under big buildings, stadium team
  dialog, water-reach and isolated-plant FAILs in audit.py, fire-cover WARN and a -$50,000 debt stop in play.sh,
  rebuild.py keeps the land parts of river crossings.

## What all attempts now say about 200,000
- Fast start + early river crossing + checkerboard districts (proven).
- **Fire cover is part of every district** (a station every ~14 tiles); the airport comes late, on bare land far
  from districts, with its own station - or not at all if shops are not capped.
- **A debt budget**: loans are finite (50) and so is debt (-$100,000). Every loan must add people that pay for
  it; at ~$600 a year per loan, 30 loans need ~150,000 people at 9-10% tax to break even. Keep taxes as high as
  demand allows (homes 10-12%), never cut them to "help growth" once in debt.

## Claudeville 4 attempt 2 (peak 97,090 - mayor thrown out Jan 2039)
- Fire cover (28 stations from `firegrid.py`) and an isolated airport worked: no great fire in 39 years.
- 30 loans for 97,000 people (attempt 1: 48 for 87,000), but bond payments (~$15k/yr) still outran property tax
  ($7-9k/yr). Growth stalled near 95,000 from 2029 with shop demand ~-1,500 (smallest airport), factories past
  their trade capacity, 8-22% jobless.
- Raising taxes on the stalled city (to 10-11%) lost 15,000 people in two years; income fell anyway.
- The road-network check written after the attempt found the whole south-east district (116 road tiles) cut off
  from the city for the entire game.

## What all four Claudeville 4 lessons add up to (before attempt 3)
- **Tax depends on population x rate only** (research: tax ~ rate x population / 75; land value does not count).
  At 8-9% a person pays ~$0.11-0.12 a year. 200,000 people pay ~$23k; 100,000 pay ~$12k.
- **So loans must stay well under what the city can carry**: each $10k loan costs ~$500 a year for ever. 20 loans
  (~$10k/yr) is about what a 100,000 city carries. Repay bonds whenever cash allows (bond window).
- **Service upkeep counts**: 28 fire stations cost $2.8k a year - a fifth of the tax. One station per ~8,000
  people is enough with an isolated airport.
- **The caps decide the stall**: a bigger airport (shops), a seaport or rail link per ~10,000 factory workers
  (factories), recreation ahead of each ~15,000 (homes). Lift them before demand turns negative, not after.
- **Every road must join the network** (now checked).

## Claudeville 4 attempt 3 (peak 81,950 - game over Jan 2038)
- The road-network / water-reach / isolated-plant audits caught every gap at once (south-east district joined in 2016).
- The loan guard (cash projected to 2050 > -$80k) held loans at 27; the city still ran ~$8k a year short and ended in 2038.
- **The airport never developed - in attempts 2-3 or Claudeville 3's winner; only attempt 1's did.** Shops stayed capped
  from ~14,000 shop workers (3 road links ~6,000); a 1% shop tax did not lift shop demand above -1,100.
  Attempt 1's airports had a power line along a whole side (one was zoned while shop demand was positive).
- A fire in the 4-plant coal cluster by the seaport burned ~1,300 tiles (2023).

## Before attempt 4
- The airport is the key unknown. Wire it like attempt 1's (line along a full side), zone it early, check it every
  year and move it if empty after 2 years.
- Road links on all four edges early. Spread coal plants out, each with a fire station.
- **Lab test (Oct 2026, copy of attempt 3's 2012 save): the empty airport developed once a power line ran THROUGH it.**
  The airports in attempts 2-3 had a line touching one corner tile; empty zones do not carry power. This one wiring
  detail capped shops in every city since attempt 1.

## Claudeville 4 attempt 4 (peak 74,150 - game over Jan 2038)
- **The airport fix worked**: a power line through the zone and it developed within ~7 months (2007). Shop demand rose at once.
- **Fire is now the main killer**: great fires in 2017 (~3,900 tiles, -30,000 people, 6 loans to rebuild) and 2035
  (most of the city, while the run-out script ran unattended). A 2024 fire burned ~300 tiles.
- Fuel was everywhere: a 2x2 tree park in every home cell and rubble left in burned or abandoned blocks. The airport
  sat only 5 rows from homes.
- Even with shops working, the city stalled near 70,000 from 2023 with all demand negative and a ~$5k yearly deficit.

## Across all four attempts (before attempt 5)
- Three of four cities were wrecked by great fires (attempts 1, 3, 4). Attempt 2, with no great fire, got furthest (97,090).
  **Surviving fires is worth more than any growth trick.**
- All four ran out of money in 2031-2039. Each fire rebuild cost loans that never paid back.
- Every city stalled at 70-97k with all demand negative. Fixing fires and money first; then the stall.
- Plan for attempt 5: no tree parks, clear rubble at once, airport far from homes, coal plants spread out each with a
  station, keep ~$5k for firebreaks from 20,000 people, and every run (play or run-out) stops on new rubble.
