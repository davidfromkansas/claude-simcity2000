# Claudeville 4 · Attempt 6 post-mortem

**Result: failed, but the best Claudeville 4 city.** Peak **120,770** people (Apr 2049); **118,410** at Jan 2050.
Goal: 200,000 by Jan 2050.

| Date | People | Loans | Notes |
|---|---|---|---|
| Jun 2006 | 18,320 | 7 | 4,000 ahead of attempt 5; airport one row in from the edge (still only 12 of 24 tiles developed) |
| Dec 2008 | 25,600 | 9 | Ahead of every earlier attempt |
| Jul 2015 | 39,690 | 12 | Crossed the river: bridge, west district, fourth neighbour link (west edge) |
| Dec 2018 | 51,410 | 15 | West bank filling |
| Feb 2026 | 75,760 | 18 | Beat attempt 4's 74,150 peak |
| Nov 2036 | 100,180 | 23 | First Claudeville 4 city past 100,000 |
| Jul 2043 | ~112,000 | 27 | **Map full**: the last empty land would not fill |
| Apr 2049 | 120,770 | 27 | Peak (demand at maximum in the last years) |

## What worked
- **The loan rule.** Loans only for districts that fill, guard never overridden. 27 loans for ~4,400 people each
  (attempts 4-5: ~2,700-2,800). The 2050 cash projection stayed positive; income nearly covered the bonds.
- **Fire.** No great fire in 50 years. Three small fires burned out on open land. No tree parks, plants spread out,
  each with a station, ~20 stations.
- **Shoreline pumps.** Pumps on true shore tiles gave several times the water of inland pump columns (5% -> 30% spare
  with 14 shore pumps in 2039).

## Control failures vs strategy failures

### Control failures
1. **A refused plan went unnoticed for 5 years** (the seaport factory block, Dec 2007 - Jul 2013): I read only the last
   lines of the build output. *Fixed:* `seq.sh` ends with "SEQ NOT CLEAN" naming any plan not "BUILD: checked".
2. **Autocal left two stray bridges near the west map edge** (2018, 2041). Bulldozing a bridge by click failed, so both
   were joined to the road network instead. *To fix:* calibrate near the west edge from a known tile, not a test road.
3. **Inland pump columns** (x41, x49) gave little water; I only found out when spare water fell to 5%.
   *To fix:* a pump check in `audit.py` that counts shore pumps and warns about inland ones.

### Strategy failures
1. **Not enough density.** At the end: 3,085 dense home tiles held 118,000 people (~38 a tile). Homes were 21% of the
   land, jobs 22%, roads 17%. 200,000 needs ~5,300 home tiles at that density, or higher density (land value).
2. **Too much road.** The 7x7 grid (roads both ways every 7 tiles) used 17% of the land.
3. **The airport still only half developed** (12 of 24 tiles) in a new spot; shops were capped from ~40,000 until the
   west link (2015).
4. **The west-edge factory strips (2041) never filled**: too far by road from homes.

## What changes next time (attempt 7)
- **Plan the whole map from day one** as long strips: dense zones 6 deep on each side of roads 13 apart,
  cross streets only every ~20 tiles. No light zones at all.
- Keep: the loan rule, the fire rules, shore pumps only.
- Reach 120,000 by ~2035 so arcologies can be tested; keep 4x4 lots free.
