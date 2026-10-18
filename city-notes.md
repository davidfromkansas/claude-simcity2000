# City notes

## Attempt 1 (abandoned)
Hilly map. 7 game years with zero growth: power links broken and power lines placed between zones and road.

## Attempt 2 (current) — refounded Jan 2000
- Flat map made with the map editor. Easy, $20,000, disasters off.
- Build area: big flat plain along the north edge of the map, x 47-115, y 0-24.
- Jan 2001: population 290, cash $16.1k. Residential and industry demand positive, commercial negative.
- Next: keep zoning residential as demand allows; add water pump when growth slows; extend road grid south (y=18) and west.
- Jan 2006: pop dipped to 1,200 with 35% unemployment. Added coal plant (200 MW), water pump + pipes, second road y=19 with industry rows y16-18 and y20, connector road x=80 y12-19.
- Jan 2009: pop 2,110, unemployment 13%. Added road y=3 and residential rows y4-6 (x70-99).
- Jan 2010: pop 2,390, cash $10.5k, no bonds. R and I demand high, C slightly negative. Power coverage 64% (watch it).
- SE corner (x>=91, y>=13) is raised ground; tile.py now corrects for altitude.
- 2013-2024: stalled ~3,200-3,400. Causes found: (1) only 15/390 buildings had water -> added riverside pumps (26 total now);
  (2) main roads at max traffic -> converted power-line rows y=7 and y=15 into roads; (3) south industry badly connected -> connector roads x=74, x=80.
- Neighbor connection: road x=75 to north edge (Villa). Police station x81-83 y16-18.
- Tax: 7% -> 5% (2025) -> 3% (2029). Dense residential rows 0-2 (north) and 16-18 (east of x=80).
- Jan 2030: pop 4,410 -> MISSED the 5,000-by-2030 goal. Jan 2031: 4,610, cash $7.0k, no bonds.

## Attempt 2 (Claudeville II) — BOTH GOALS MET
- Same map as attempt 1, west plain. Coal plant + 10 pumps + road grid + neighbor link + 5% tax on day one.
- Yearly health check (water %, power %, abandoned, jammed roads) caught every problem within 1 year:
  2001 pipe gap; 2003 too much industry -> north housing district; 2005 jobs short -> east factory strip;
  2008 strip unpowered across road; 2010 long commutes -> east lake road; 2013 jobs short -> rezone abandoned homes to industry.
- Jan 2015: 5,970 people (goal 1, 15 years in). 2015/2016/2017 cash +$353/+$362/+$372 (goal 2). Bonds: 0 all game.
