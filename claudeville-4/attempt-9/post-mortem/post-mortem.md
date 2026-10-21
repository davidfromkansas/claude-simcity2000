# Claudeville 4 · Attempt 9 post-mortem

**Result: failed.** **97,880** people at the Jan 2050 check (Feb 2050 save); goal 200,000.
Pre-fire high **94,400** (Sep 2028); after the 2028 great fire the city was rebuilt and peaked at **102,360** (Dec 2044).
46 loans. (The game kept running past the deadline and went bankrupt in Jan 2052 - after the deadline, not counted.)

| Date | People | Loans | Notes |
|---|---|---|---|
| Feb 2010 | 30,070 | 9 | Replay of attempt 8's order, on pace |
| Feb 2013 | 39,920 | 12 | River crossing (west district, west link) |
| Dec 2018 | 58,130 | 17 | ~4,000 ahead of attempt 8 |
| Aug 2020 | 60,900 | 17 | SW coal plant fire: SW district burned; rebuild landed **shifted 14 tiles** (kept as an extra district) |
| Jul 2025 | 81,280 | 22 | Ahead of every earlier attempt at this date |
| Jul 2027 | 89,990 | 24 | 6,000 ahead of pace |
| Sep 2028 | 94,400 | 25 | **Alien ship → great fire**: east bank burned |
| Oct 2028 | 48,320 | 25 | ~3,500 rubble tiles; 942 road + 663 line tiles lost |
| Jul 2032 | 76,310 | 32 | Rebuilt roads, lines, pumps, plants, zoos, stadium |
| Jul 2041 | 100,030 | 40 | Back above 100,000 |
| Dec 2044 | 102,360 | 43 | Peak before the deadline |
| Feb 2050 | 97,880 | 46 | Deadline (cash -$76,917) |

## Control failures (each now has a fix)
1. **The 2028 great fire grew while disaster.sh watched only the view around the alien ship.** 17 bursts let a fire
   elsewhere spread over the east bank. *Fixed:* disaster.sh also counts rubble on the whole map after each burst and
   stops at +25. The **Emergency → Dispatch Firefighters** tool (toolbar 68,58 → 135,81) is what finally held the front;
   use it at the first sign of fire.
2. **Calibration failures at the map edges and in fully built views** caused shifted builds three times: the 2020 SW
   rebuild (copy built 14 tiles off), the 2040 north-east shop plan (twice, ~$7k on bridges/zones in the wrong place).
   *Fixed:* autocal fails on an unverified zoom, tries both directions for its zoom check, has a power-line fallback for
   built-up views, and records its method; build.py checks every step right after placing it and stops when nothing
   landed but tiles outside the plan changed. **Still open:** the north map edge (y < ~12) - do not build there until
   autocal is fixed for views that cannot centre.
3. **My own controller change destroyed buildings:** an autocal "sweep test roads" on zoom-fail exits bulldozed with a
   wrong calibration (2 fire stations, a power-line link, road tiles). Reverted; build.py now only bulldozes outside the
   plan after a road- or line-verified calibration.
4. **play.sh had no deadline stop** and ran on to Jan 2052. *Fixed:* play.sh stops at Jan 2050.
5. **Self-matching pgrep/pkill patterns** killed my own shell twice and a wait loop ran to its time limit. Rule: never
   pgrep/pkill a pattern that appears in the same command line.

## Strategy
- The replay of attempt 8's order worked: ahead of every earlier attempt until 2028 (89,990 in Jul 2027).
- Fires decided the attempt again (attempts 5, 8, 9). Empty zones carry no power: after a big fire whole districts went
  dark and needed new links (`powerfix.py`). Roads and lines can be placed straight onto rubble (no bulldozing).
- Late loans pay for themselves in cash by 2050 (a $10k loan costs ~$450/yr); 46 loans kept the city alive to 2050.
- Recreation (stadiums/zoos) and power plants burned too; every rebuild needed one more loan.

## Next (attempt 10)
- Same opening (attempts 8-9 were the best starts) and fire defence first: a fire station per ~6,000 people from the
  start, firefighters dispatched at once in any disaster, disaster.sh with the whole-map rubble check.
- No builds at the north map edge until autocal handles views that cannot centre.
