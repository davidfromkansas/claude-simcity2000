# Claudeville 3 · Attempt 13 post-mortem

**Result: missed.** Stopped in July 2011 at **16,650 people** (peak 20,070 in Feb 2008), with 7 loans.
The best city of all attempts at year 6 (17,790 in Dec 2006), then a collapse: unemployment 5% -> 26%,
abandoned buildings 70 -> 587.

| Year | People | Home tiles built | Loans | Taxes R/C/I | Unemployed | Demand R/C/I |
|---|---|---|---|---|---|---|
| 2002 | 3,430 | 273 | 2 | 4/4/3 | 5% | max/+/+ |
| 2004 | 10,730 | 656 | 3 | 6/6/5 | 3% | +/+/max |
| 2006 | 17,790 | 1,071 | 5 | 6/5/9 | 5% | +/-/max |
| 2008 (Feb) | 20,070 | 1,130 | 6 | 6/5/12 | 7% | -/-/max |
| 2009 | 18,320 | 1,166 | 7 | 5/5/12 | 19% | -/-/+ |
| 2011 | 16,650 | 1,179 | 7 | 5/5/10 | 26% | -/-/- |

## What happened
**2000-2006:** attempt 12's plans plus a second neighbour road link (east edge) and a tax controller.
17,790 people by the end of 2006, ahead of the target curve every year.

**2007-2011:** the tax controller kept raising factory tax while factory demand read maximum: 9% -> 12%
by Nov 2007. Factory demand then fell from 2,000 to -945, factories emptied, unemployment reached 26%,
and homes followed. A rail link and a road link off the south edge (loan #7, July 2008) made no visible
difference. Shops were 30-45% abandoned in every district; homes next to the power plants 43-58%.

## Control failures vs strategy failures

**Control failures:**
- **The game ran six months (Jan -> Jul 2002) while a loan dialog was open** and I was reading it. No harm
  this time, but the city ran unchecked. **Fixed:** `bot/loan.sh` issues a loan in one call, re-pauses,
  and checks the loan count from the save.
- **A build was cut off by a command time limit** (district 5, ~$6,600 spent of ~$10,500); re-running
  the plan finished it. Long builds now run in the background with a long time limit.
- **Plans copied from earlier attempts assumed power lines that did not exist here** (east shops, south
  pumps). The audit caught both before the clock ran; no time lost.

**Strategy failures:**
1. **The tax controller pushed factory tax to 12%.** Factory demand at maximum was the trade cap, not
   spare willingness to pay; the higher rate turned it negative and took the jobs with it.
2. **Too many shops.** The east shop block (170 tiles) answered a short "shop land" alarm; shops ended
   30-45% abandoned everywhere.
3. **Homes next to coal plants** (west side) were half abandoned.
4. **Seven loans** - the debt rule was broken again (#5 power, #6 power + zoo, #7 the links test).

## What changes next time
See `claudeville-3/reflection.md` (all thirteen attempts) and the attempt 14 strategy.
