# Reflection for Claudeville 4 (200,000 by Jan 2050)

Updated before every new attempt (process rule), weighing ALL earlier attempts equally. It starts from the
19 Claudeville 3 attempts on the same map (full detail in `claudeville-3/reflection.md` and the post-mortems).

## What Claudeville 3 established (attempts 1-19)
1. **Money is not the ceiling; land and the game's caps are.** Attempts 2, 4 and 6 died of debt only because they
   stopped borrowing or stopped building. Attempt 19 carried 33 loans; the game never refused one, and negative
   cash only blocked building until the next loan.
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
