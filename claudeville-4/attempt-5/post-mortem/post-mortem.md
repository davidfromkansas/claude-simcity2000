# Claudeville 4 · Attempt 5 post-mortem

**Result: failed.** Peak **50,120** people (Jul 2039), against a goal of 200,000 by Jan 2050.
The city survived to the 2050 deadline (cash about -$75,000), but it never grew past 50,000.

| Date | People | Loans | Notes |
|---|---|---|---|
| Jul 2004 | 12,250 | 5 | Airport in the empty north-east corner, line through it. Only half of it ever developed. |
| 2006-2010 | ~15,000 | 7 | **Stalled for three years** with all demand negative and unemployment up to 20%. I ran on with the alarms overridden. |
| Feb 2011 | 17,180 | 8 | Road links to the east and south edges, second seaport |
| Jul 2012 | 20,390 | 9 | Taxes cut to 7/6/6: unemployment 20% → 6% within a year |
| Feb 2015 | 25,360 | 11 | All demand positive again; factory block, south-east district |
| Feb 2019 | 37,130 | 14 | Cheap south bands (no bridge), lake pumps |
| Feb 2023 | 41,900 | 15 | Bonds $7,700 a year vs $5,200 income. No more loans. |
| Jan 2036 | 48,990 | 15 | Plane crash: small fire (33 tiles) |
| Jul 2039 | 50,120 | 15 | Peak. Demand at maximum but no cash to zone land. |
| Jun 2048 | 49,600 | 15 | Alien-ship disaster with fires; cash too low to bulldoze firebreaks |

## What worked
- **No great fire for the first time in Claudeville 4.** No tree parks, spread-out coal plants each with a station,
  airport far from homes. Two disasters (2036 plane crash, 2048 aliens) did only local damage.
- The tax cut in 2012 ended a 5-year jobs stall within a year.

## Control failures vs strategy failures

### Control failures
1. **I overrode the trips and pace alarms for 12 steps at once (2007-2010).** The city sat stalled at ~15,000 for
   three years and I did nothing. *Rule:* an override covers 1-2 steps only, then look again.
2. **The run-out script mistook a disaster for game over.** The calendar freezes during a disaster (plane crash 2036,
   aliens 2048); the script stopped with "date stuck". That was safe, but slow. *Fix to make:* when the date is stuck,
   check for the red disaster arrow and say "DISASTER" instead.
3. **The 2002 plan ran before its loan.** The coal plant was half-built until loan #3. Small, but the plan said "loan #3".

### Strategy failures
1. **Money, again, and now measured.** Bond payments were ~$513 per loan per year. At 8-9% tax a person pays ~$0.11 a
   year, so **each loan needs ~4,800 more people just to pay its own interest.** Attempt 5's 15 loans bought ~2,800
   people each. Every Claudeville 4 attempt has died of this sum.
2. **The north-east airport only half developed** (12 of 24 tiles; its top row is the map edge). Shops stayed capped
   from ~40,000.
3. **Taxes too high early.** 8% with demand negative from 2006; 6-7% from 2012 fixed it.

## What changes next time (attempt 6)
- **Loans only when the plan shows 5,000+ new people for it** (a district that fills, not a coal plant ahead of need).
  Power, water and services come from cash.
- **Taxes low (6-7%) while demand is negative; raise only at demand ≥ 1,500.**
- Keep the fire rules that worked: no tree parks, spread plants, airport away from homes but **not on the map edge**
  (full 6x4 interior, line through it).
- Never override an alarm for more than 2 steps.
