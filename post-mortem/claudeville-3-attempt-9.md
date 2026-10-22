# Claudeville 3 · Attempt 9 post-mortem

**Result: missed.** Stopped in February 2022 (game year 22) at **7,410 people** (peak 7,830), with 3
loans and $6,143. The target curve (from the official manual's method) called for 18,000 by 2010 and
40,000 by 2020.

| Year | People | Cash | Loans | Taxes R/C/I | Unemployed |
|---|---|---|---|---|---|
| 2002 | 910 | $8,699 | 1 | 7/7/7 | 13% |
| 2004 | 2,360 | $6,127 | 1 | 7/7/7 | 15% |
| 2007 | 4,060 | $3,600 | 1 | 5/5/4 | 6% |
| 2010 | 5,810 | $5,142 | 2 | 5/5/4 | 7% |
| 2013 | 7,680 | $1,491 | 2 | 5/5/4 | 5% |
| 2017 | 7,680 | $1,167 | 2 | 8/8/7 | 7% |
| 2019 | 6,090 | $1,705 | 3 | 10/10/9 | 27% |
| 2022 | 7,410 | $6,143 | 3 | 8/10/9 | 11% |

## What happened, phase by phase

**2000–2004: the manual's start.** One compact module (light zoning, road + rail links, coal plant,
riverbank pumps) built from a checked plan. Growth was as slow as attempts 7 and 8: 2,360 by 2004.

**2004–2012: lower taxes and more land.** Taxes cut to 5/5/4 (attempt 2's fast start began at 4%), and
land was added each time it filled: factory squares, an east factory strip, south and east homes. Loan
#2 paid for a second coal plant; 19 riverbank pumps fixed water. Population 7,700 by 2012.

**2012–2017: stuck with every demand bar at maximum.** Land was full and cash under $1,500. Taxes went
to 8% then 10% and demand stayed at maximum, but the extra income only covered loan interest.

**2017–2019: the power plant burned down.** The second coal plant was destroyed (rubble), almost
certainly by fire; the city had no fire station. 180 buildings lost power; population fell to 6,100;
loan #3 rebuilt the plant and added a fire station.

## Control failures vs strategy failures

**Control failures:**
- **The play loop kept running for 18 game months after the plant burned down.** Steps were run in
  batches of 6-8 without stopping on alarms. Fixed: `bot/play.sh` stops at the first alarm (buildings
  without power, new rubble, audit FAIL, game not paused).
- **Camera calibration put a test road on the lake** (a 3-tile bridge). The build guard caught and
  removed it; `autocal.sh` now skips screen spots that show water.

**Strategy failures:**
1. **Money could not buy land as fast as demand wanted it.** All three demand bars sat at maximum from
   2011 to 2017 while the land was full. Each module cost $1,000-2,000 and added ~2,000 people (~$130 a
   year in tax at 5%).
2. **7% tax for the first 4 years** throttled the start (the manual and guides: 0-6% grows fast).
3. **No fire station for 17 years** with disasters on; the strategy listed police and unlocks but not fire.
4. **No unlocks built** (marina, stadium, seaport, airport) because there was never spare cash.

## What changes next time
See `claudeville-3/reflection.md`, which now reflects on all attempts equally before each new strategy.

Next: [attempt 10 strategy](../claudeville-3/attempt-10/strategy.md)
