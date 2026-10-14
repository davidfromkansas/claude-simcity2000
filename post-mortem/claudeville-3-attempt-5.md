# Claudeville 3 · Attempt 5 post-mortem

**Result: missed.** Stopped in September 2012 (game year 12) at about **6,700 people**, with
negative cash and 2 loans. Earlier attempts had 18,000–35,000 people by this year and still missed,
so 100,000 by 2050 was out of reach.

| Year | People | Unemployed | Abandoned | Land value | Loans |
|---|---|---|---|---|---|
| 2001 | 430 | 7% | 4 | 7 | 1 |
| 2003 | 1,340 | 20% | 28 | 7 | 1 |
| 2004 | 4,560 | 4% | 19 | 6 | 1 |
| 2007 | 5,140 | 27% | 190 | 6 | 1 |
| 2009 | 5,610 | 12% | 76 | 6 | 2 |
| 2011 | 6,430 | 13% | 95 | 6 | 2 |
| 2012 | 6,740 | 14% | 108 | 6 | 2 |

## What happened, phase by phase

**2000–2002: homes had no power.** The plan put a column of parks between each power line and its
home zones. Parks don't carry power, and empty zones don't either, so no home could grow for two
years. The pumps were also one tile short of the pipe network. Both were found and fixed in
December 2001.

**2003–2004: a burst of growth.** With power and water working, the city went from 1,000 to 4,500.
Water ran out and 7 pumps were added.

**2005–2010: stuck at 5,000.** Shops and factories were abandoned faster than they were built, even
though the game showed maximum demand for factories. Fixes tried: a second power plant (loan #2),
turning the empty shop band into factories, pipes for the south factory strip. None of them moved
population past ~6,000.

**December 2010: the real cause.** The road to the neighbor city stopped one tile short of the map
edge, so the $1,000 neighbor link was never built. Without it, shops and factories have no trade.
It was built in 2010, but by then cash was gone and land value was 6.

## Top causes

1. **No neighbor link for 10 years.** *Evidence:* cash never dropped by $1,000 for the link; the
   road ended at y=1, not the map edge; demand for factories at maximum while factories were
   abandoned.
2. **Setup never checked against the save.** Parks blocking power, pumps not joined to pipes, and
   the missing link were each a one-line check that was skipped. Two years lost to power, ten to
   the link.
3. **Far too much shop land.** Two full shop bands (288 tiles) for 5,000 people; most were
   abandoned, which dragged land value down to 6.
4. **Bulldozer drags hit the wrong tiles.** One drag destroyed the fire station and two road tiles.

## What changes next time

- **Day-one checklist, verified from the save before the game runs:** neighbor link built ($1,000
  charged, road tile at the map edge), every zone touches a power line or road as planned, every
  pump touches the pipe network, pipes reach every band, power plant linked.
- **Stall rule:** if a zone type has demand but doesn't grow for 6 game months, query one empty tile
  and one abandoned tile at once (power, water, land value), and check trade links.
- **Shops sized to demand:** shop bands half the depth of home bands; add more only when shop demand
  is positive.
- **Parks never between a power line and a zone:** put them at the far end of a band or between
  two roads.
- **Bulldoze tile by tile** with a list from the save, never long drags next to buildings.
- Keep attempt 4's proven layout and wiring (it reached 30,000) and its yearly money rules.

Next: [attempt 6 strategy](../claudeville-3/attempt-6/strategy.md)
