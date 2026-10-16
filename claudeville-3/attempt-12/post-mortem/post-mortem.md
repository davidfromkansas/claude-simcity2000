# Claudeville 3 · Attempt 12 post-mortem

**Result: missed.** Stopped in July 2015 (game year 15) at **21,120 people** (peak 21,130), with 6 loans
and -$393 cash. The fastest start of all twelve attempts until 2005 (12,030 in 2004; attempt 4: 10,920),
then flat at 20,500-21,100 from 2012. Target: 20,000 by 2010 (reached in 2012), 30,000 by 2015.

| Year | People | Home tiles built | Loans | Cash | Taxes R/C/I | Unemployed | Demand R/C/I |
|---|---|---|---|---|---|---|---|
| 2001 | 1,870 | 132 | 1 | $3,661 | 4/4/3 | 3% | max/max/+ |
| 2003 | 7,900 | 531 | 3 | $1,789 | 7/7/7 | 2% | max/+/max |
| 2004 | 12,030 | 745 | 4 | $523 | 8/8/8 | 3% | max/+/max |
| 2005 | 14,520 | 913 | 5 | $1,937 | 8/8/8 | 7% | +/-/max |
| 2007 | 16,640 | 1,080 | 6 | $6,474 | 8/8/10 | 16% | -/-/+ |
| 2009 | 18,030 | 1,154 | 6 | $2,862 | 8/6/8 | 17% | -/-/+ |
| 2012 | 20,720 | 1,198 | 6 | $568 | 8/6/8 | 12% | -/-/+ |
| 2015 | 21,120 | 1,209 | 6 | -$393 | 8/6/8 | 13% | -/-/+ |

## What happened, phase by phase

**2000-2004: the best start yet.** Attempt 11's proven plans, with the second loan (allowed in April 2002),
blocks 3-4, a second coal plant *before* the shortage, the seaport and 19 pumps in 2003, taxes to 7% at
6,000 people and 8% at 12,000. On the target curve from 2003 to 2009 - a first in any attempt.

**2005-2008: unemployment.** Water hit 2% (loan #5: pumps, zoo, district 6). Then power ran out while I had
the low-capacity stop overridden (loan #6: fourth coal plant). Unemployment climbed from 3% to 19%;
home and shop demand went negative and stayed negative to the end.

**2009-2015: out of money, out of land.** Every tile was zoned and built; shop demand sat near -1,300 with
the game's "no airport" shop cap; factory demand stayed positive but factory land was full. Property tax
($2,094) was smaller than loan payments ($2,299) plus fire stations ($300) - four finance ordinances
(+$337) halved the gap but could not close it.

## Where the money went
About **$60,700** was spent, almost exactly the six loans ($60,000): day one $15.8k, blocks 3-4 $7.6k,
power and pumps ~$16.6k, seaport + north pumps $6.0k, shops $2.2k, district 5 + west factories $10.5k,
zoo + district 6 $5.8k, factories $1.2k. That bought 21,000 people: **~$2.90 per person**. At that price
100,000 people costs ~$290,000; a city growing to 100,000 by 2050 at 8% tax earns about that much in
total, before loan interest. The plan cannot work at this cost per person.

## Control failures vs strategy failures

**Control failures:**
- **Power alarm hidden by an override.** After building pumps I ran the loop with `LOW_OK=1` to get past a
  stale water reading; it also silenced the power alarm, and power fell from 16% to 1% (53 buildings
  unpowered, unemployment 7% -> 13%). **Fixed:** the override no longer exists.
- **Started the clock with an audit FAIL** (west factory strip unpowered) for one step (5 months).
  **Fixed:** `play.sh` refuses to start while the audit fails.
- **Calibration wiped a zone tile** again ((81,84); (87,40) in attempt 11). **Fixed:** `build.py` now
  restores the zone type of any tile outside the plan that lost it (it worked later in this attempt).
- A one-tile power gap at (109,76) was caught by the audit before the clock ran.

**Strategy failures:**
1. **Cost per person too high (~$2.90).** All-light zoning, a 4x4 coal plant per ~5,000 people, pumps,
   and 6x6 cells with a road and a power line around each. Nothing in the plan aimed at people per dollar.
2. **Jobs capped twice:** shop demand negative for ten years without an airport (the audit warned from
   20,000), and factory land full while factory demand stayed positive. Unemployment 12-19% from 2007.
3. **Six loans.** Two beyond the rule, both forced by shortages that came from building homes faster
   than power and water.

## What changes next time
See `claudeville-3/reflection.md` (all twelve attempts) and the attempt 13 strategy.
