# Claudeville 4 · Attempt 11 post-mortem

**Result: failed (alive at the deadline).** **104,690** people at the Jan 2050 check (Dec 2049), peak **106,750** (Jun 2048);
goal 200,000. Cash about -$55,000 with 29 loans - the first city since attempt 6 to reach 2050 without money trouble.

| Date | People | Loans | Notes |
|---|---|---|---|
| Dec 2005 | 18,350 | 8 | Attempt 10's opening, 2 years ahead of it |
| Dec 2009 | 36,380 | 12 | River crossed (attempt 10: 2016) |
| Dec 2011 | 48,740 | 14 | Fastest city of all 11 attempts to here |
| Jul 2017 | 68,030 | 18 | Land nearly full |
| Dec 2022 | 77,830 | 20 | Growth ~1,000 a year; budget below zero |
| Feb 2033 | 97,140 | 26 | Alien ship: firefighters on every burst, ~160 tiles burned, road y69 rebuilt |
| Jun 2036 | 100,150 | 27 | Past 100,000 |
| Jun 2048 | 106,750 | 29 | Peak |
| Dec 2049 | 104,690 | 29 | Deadline (cash -$54,649) |

## Control failures (each now has a fix or a rule)
1. **A build cut off by the 30-minute background limit (Feb 2001)** left the game running unpaused. Rule: long sequences run
   with a longer limit; check `sc paused` after every killed job.
2. **A reused shore-pump plan put 5 pumps on the empty west bank (Jul 2009)** - I did not read its header. *Fixed:* audit
   `pending_pumps` (WARN until the district exists); rule: read a reused plan's header for what it depends on.
3. **A build with --cash-ok while cash was negative looped 30 minutes (Dec 2022)** and left a stray sign. *Fixed:* build.py
   refuses every build while cash is below zero.
4. **Reused plans assumed attempt-10 neighbours** (power lines from plants not built here, roads ending at old streets):
   powerfix/roadjoin/pipe joins were needed after almost every plan. *Tool:* `/tmp/sc/overlap.py`-style check of planned tiles
   against the current map before building (to become `bot/overlap.py`).

## Strategy failures
1. **Too few home tiles.** Peak population is ~39 people per home tile in every attempt (6: 3,085 tiles -> 120,770;
   11: 2,706 -> 106,750). Attempt 11 spent late land on shops/factories (demand-led), 26 fire stations, zoos and plants.
2. **Shop tax cap raised to 11% (2024)**: the controller went to 11% and shop demand fell from +1,373 to -860 for two years
   (research note: shops turn negative above ~9%).
3. **Land filled at ~70,000 by 2017**; the last 35,000 people came from 30 years of small fill-ins.

## What worked
- Fastest start of all attempts (49k by 2011, 63k by 2015), river crossed in 2009.
- Money rules: ordinances from day one, loan floor, taxes 8-9%: cash never below -$60k, 29 loans, alive at 2050.
- Fire rules: 26 stations; the 2033 alien ship burned ~160 tiles (attempt 9's burned ~4,000).

## Next (attempt 12)
- Attempt 11's opening to ~2015, then **home tiles first**: every new block mostly dense homes (target 3,300+ home tiles),
  jobs only as demand needs, plants/stations on unbuildable edges. Aim: 120,000 by ~2040, then open the arcology menu.
