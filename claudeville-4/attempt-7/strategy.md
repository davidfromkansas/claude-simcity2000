# Claudeville 4 · Attempt 7 strategy (from claudeville-4/reflection.md)

Goal: 200,000 by Jan 2050, same map, Medium, disasters on.

## What six attempts show
- Attempt 6 solved fire and money (no great fire, budget near balance) and reached 120,770, but **the map was full
  by 2043**. It zoned only 44% of the land; roads took 17%.
- 200,000 needs ~70% of the land zoned dense (at ~38 people per home tile).

## Plan
1. **Keep attempt 6's rules exactly**: loans only for districts that fill (guard never overridden), no tree parks,
   power plants spread out each with a station, shore pumps only (the audit now warns about inland pumps),
   taxes 7-10 by demand.
2. **Same opening as attempt 6** to ~2009 (it was ahead of every attempt).
3. **All new districts as dense strips**: two 6-deep zone bands on each side of a road (13-tile pitch: zone 6, road,
   zone 6), cross streets every ~20 tiles, lines through the middle of each band. No light zones. Homes and jobs in
   alternating bands so trips succeed.
4. **Cross the river ~2010** (attempt 6: 2015) and start the south-west bank ~2015 (attempt 6: 2021).
5. **Fill every leftover lot**: run `spots.py 6` every few years and zone what fits.
6. Arcologies if the city reaches 120,000 early enough; keep a few 4x4 lots free from ~2035.

## Note after testing stripplan.py (Oct 2026)
The 7x7 grid already zones ~73% of a district; strips zone ~70%. Attempt 6's 44% came from unused pockets, lake
margins, pump columns and service lots, not from the road pattern. So the gains must come from **filling every
pocket** (spots.py each few years, stripplan.py for any open area) and **higher density per home tile** (land value:
police coverage - attempt 6 had about one police station - and coal plants away from homes).
