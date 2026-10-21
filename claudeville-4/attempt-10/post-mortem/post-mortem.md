# Claudeville 4 · Attempt 10 post-mortem

**Result: failed.** Peak **109,570** (Nov 2040); goal 200,000. Bankrupt at the **Jan 2048** check
(cash -$102,331, all loans used) - the game ended two years before the deadline.

| Date | People | Loans | Notes |
|---|---|---|---|
| Dec 2010 | 28,630 | 11 | Same opening as attempts 8-9 |
| Dec 2015 | 40,740 | 13 | One-year stall: no home land left on the east bank |
| Dec 2019 | 54,640 | 19 | River crossed in 2016; west and south districts |
| Dec 2022 | 70,800 | 24 | Ahead of the pace curve |
| Aug 2028 | 84,690 | 28 | Cash below zero for the first time |
| Nov 2032 | 100,470 | 35 | Past 100,000 - four years before any earlier C4 city |
| Nov 2040 | 109,570 | 41 | Peak. Cash -$39,750; finance ordinances only now enacted |
| Nov 2043 | 93,430 | 41 | Recession after taxes were raised to 10-11% |
| Nov 2047 | 103,780 | 48-50 | Cash -$82,510, no loans left |
| Jan 2048 | - | - | Cash -$102,331: game over |

## Control failures (each now has a fix or a rule)
1. **Zoo built 22 rows off (Dec 2002)**: the calibration file kept a scale from a failed zoom check. *Fixed:* autocal
   deletes cal.json on every failed zoom check.
2. **powerfix ran after a refused plan (Jun 2030)** and laid a line along a planned road row. *Rule:* never run
   powerfix/roadjoin after "SEQ NOT CLEAN".
3. **Road funding set to 0% (Feb 2046)** to save $288 a year: 89 road tiles crumbled in three months, including
   the east neighbour link, and could not be rebuilt with negative cash. *Rule:* transit funding never below 100%.
4. **The ended game went unnoticed**: after the Jan 2048 game over, `sc save` kept printing the Nov 2047 save as if it
   were current, and my budget clicks on the start menu hit Quit. *Fixed:* `sc save` now fails (exit 4) when the save
   file does not change.
5. **The year-by-year journal was not written during play.** Backfilled from the logs after the attempt.

## Strategy failures (the real cause)
1. **Too much debt for the city's tax base.** 41 loans by 2038 for ~105,000 people (~2,600 each; attempt 6 had
   ~4,400 each). Bond payments reached ~$24-31k a year against ~$10-11k of property tax, so cash fell every year
   from 2035.
2. **No finance ordinances for 40 years.** Attempt 9 enacted them at the start; attempt 10's strategy forgot them
   (~$1.8k a year lost, plus no compounding).
3. **Raised taxes on a stalled city (2041, again in 2045)** - the same mistake as Claudeville 3 attempt 2 and C4
   attempt 2: unemployment 3% -> 18%, 109,000 -> 93,000.
4. **Land was full by ~2033** and nothing new was planned for the 15 years after (no density push, no arcology plan).

## What worked
- The fastest early city in Claudeville 4: 100,000 by Nov 2032 (attempt 6: Nov 2036).
- Fire rules: the one real fire (Aug 2036, seaport coal plants) was out in two watched bursts thanks to dispatching
  firefighters at once. No great fire in 48 years for the first time since attempt 6.

## Next (attempt 11)
- Keep attempt 10's opening and fire rules up to ~2032.
- Money from day one: ordinances on in Jan 2000; a hard loan budget (no loan under ~4,000 people per loan after
  30,000 people); taxes never raised on a stalled city; transit and fire funding never cut.
- Plan the years after the land is full: density (towers) and the arcology unlock at 120,000.
