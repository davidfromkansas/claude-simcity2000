# Claudeville 4 · Attempt 3 post-mortem

**Result: failed.** Peak **81,950** people (Nov 2033), against a goal of 200,000 by Jan 2050.
The game ended in **January 2038** at -$106,226 cash, when the mayor was thrown out.

| Date | People | Loans | Notes |
|---|---|---|---|
| Dec 2003 | 9,490 | 3 | Slightly ahead of attempt 2 |
| Jul 2008 | 18,670 | 9 | River crossed |
| Nov 2012 | 30,720 | 11 | The first loan rule (deficit cap ~$2.5k) refused every loan from ~25,000 people. It was replaced by a projection of cash to 2050 |
| Nov 2016 | 40,560 | 14 | West district 2, west 3 and east 2 left with road gaps (see control failures) |
| Nov 2017 | 46,180 | 15 | The south-east district joined to the road network at once |
| Nov 2021 | 62,680 | 21 | 12% jobless, shop demand negative; the airport found never to have developed |
| Feb 2023 | 66,840 → 56,900 | 23 | Fire in the coal-plant cluster by the seaport burned ~1,300 tiles |
| Nov 2024 | 71,200 | 27 | The loan guard refused further loans |
| Nov 2033 | 81,950 | 27 | Peak; shop demand ~-1,300 for 12 years |
| Jan 2038 | - | 27 | Game over |

## What worked
- **The new audit checks.** Road network, water reach and isolated plants caught every gap within one step. That includes the south-east district that attempt 2 left cut off for 30 years.
- **The loan guard** (projection to 2050) kept the city alive until 2038 on 27 loans. Attempt 2 lasted to 2039 on 30.

## Control failures vs strategy failures

### Control failures
1. **A bug in my own fix.**
   - The stray-road cleanup added to `build.py` treated new road/line crossings as strays and bulldozed them. It left road gaps in west2, w3 and east2 (2012-2014).
   - *Fixed:* any tile covered by a road step is kept.
2. **Builds placed 2-4 rows off** near the west bank's north-west, where the view could not centre and autocal calibrated 20+ tiles away.
   *Fixed:* autocal now warns (`AUTOCAL STRAY calibration tile ... tiles from the requested centre`). Placements there must still be checked tile by tile.
3. **The west shops were built before west district 2**, the district they depend on.
   *Rule:* replayed sequences keep their original order. `seq.sh` lists the order once.
4. **Autocal test roads on planned lots** blocked the zoo and cut a power line.
   *Fixed:* `build.py` clears stray roads inside a big building's lot and re-places a line that a stray road replaced.
5. **The first loan rule was set too tight.** It froze the city at 25,000 until it was replaced. That is a design error in a control tool, so it is listed here.

### Strategy failures
1. **The airport never developed**, in this attempt, in attempt 2, or in Claudeville 3's winner. Only attempt 1's airports did.
   - Shops therefore stayed capped from ~14,000 shop workers. Road links cover ~2,000 each, so three links covered ~6,000.
   - Cutting the shop tax to 1% did not move shop demand above -1,100, so the cap is hard.
   - Attempt 1's airports had a power line along a whole side, and the first was zoned while shop demand was positive. The airports in attempts 2-3 had a line touching one corner tile.
2. **The coal-plant cluster by the seaport** (4 plants side by side) burned and took ~1,300 tiles with it, despite stations nearby.
3. **Money.**
   - With shops capped, the city could not grow past ~80,000. Its ~$8.6k of tax could not carry 27 loans (~$15k a year), even with the guard.
   - Raising the home tax helped little while all demand was negative.

## What changes next time (attempt 4)
See `claudeville-4/attempt-4/strategy.md`:
- an airport at ~12-15,000 people, with a power line along a full side, checked yearly and moved if still empty after 2 years;
- road links on all four edges;
- spread-out coal plants, each with a fire station;
- higher home taxes while home demand is at its maximum.
