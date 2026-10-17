# Claudeville 4 · Attempt 1 strategy (from claudeville-4/reflection.md)

Goal: 200,000 by Jan 2050 on the Claudeville 3 map. Claudeville 3's winner (attempt 19) reached 107,460 but lost
~13 years on east-bank plateaus before crossing the river. This attempt replays its proven pieces faster and fills
the whole map, then adds arcologies.

## Plan
1. **Years 0-10: attempt 19's east-bank sequence, compressed.** Day one `a20-day1` (dense homes + parks), loan #2
   as soon as the game allows, then the same blocks in order (`a20-2003`, coal + north pumps, district 5, north,
   seaport + dense east jobs with homes across the road and NO edge tiles, zoo before 10,000, stadium/airport by
   20,000). Take a loan whenever a build is waiting on money (33 loans never got refused).
2. **Cross the river by ~2006-2010**, as soon as the east side shows the first land shortage: causeway on y69 +
   raised wires on y68 (build.py --allow-water picks the cheapest option), then the west grid (attempt 19's
   west, west2, far-west strips, west shops, south-west bands, west-bank checkerboard, north-west) in that order.
3. **Recreation ahead of every ~15,000 people** (zoos, stadiums, marinas; big parks as extras), airport ~20,000,
   second seaport ~30,000.
4. **Pumps and coal plants two years ahead** of the water/power alarms (pump rows on both banks and the lakes).
5. **Arcologies at 120,000** (target ~2040): research the tool, cost and size the moment they unlock (game help /
   a copy of the save - never the live attempt), keep a few 4x4 lots free near the centre for them.
6. Taxes by the controller: homes up to 10%, shops up to 9%, factories up to 8%; floor 5%.
7. All Claudeville 3 checks stay on (trips, land, audit, edge guard, road reach, park clash, pause confirmation).
