# Attempt 6 strategy (from the attempt 1–5 post-mortems)

Goal: 100,000 people by Jan 2050. Same flat map, Medium, disasters on, loans allowed.

## Main idea: attempt 4's proven start, checked properly
Attempt 4 had the fastest healthy start (10,900 people by 2004) and never lost power or water.
Attempt 5 lost ten years to setup mistakes that a check of the save would have caught. So:

1. **Rebuild attempt 4's first block exactly** (same script): homes y21–26, shops y28–33,
   factories y35–40, shops/factories y42–47, homes y49–54, power columns linked at both ends,
   wired pumps joined to a pipe main, fire station.
2. **Day-one checklist, from the save, before the game runs:**
   - neighbor road link built: a road tile on the map edge and $1,000 gone from the cash;
   - every pump touches the pipe network; pipe rows reach every band;
   - the power plant touches a power line that reaches every power column;
   - no park, empty tile or line gap between a zone and its power.
3. **Stall rule:** if a zone type has demand but doesn't grow for 6 game months, query an empty
   and an abandoned tile right away (power, water, land value) and recheck the trade link.

## Growing past 30,000 (where attempt 4 stopped)
- **Second district north of block 1, by the lakes (y2–18):** homes and shops only, parks at the
  ends of bands (never between a power line and a zone). This is the high-land-value district.
- **Factories go south** (y57 and below), with a shop band between them and any homes.
- **Seaport when factory demand stalls; stadium when home demand stalls;** second neighbor link.
- **Shops sized to demand:** add shop land only when shop demand is positive.
- Schools and a hospital from 10,000 people; police per two blocks; fire station per block.

## Money
- Separate taxes from day one: homes 7%, shops 5%, factories 4%. Legal gambling and parking fines on.
- At most 6 loans, only for blocks or plants. Keep $3,000+ in reserve after year 5.

## Tools
- Bulldoze tile by tile from a list made from the save, never long drags next to buildings.
