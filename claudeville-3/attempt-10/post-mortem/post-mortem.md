# Claudeville 3 · Attempt 10 post-mortem

**Result: missed.** Stopped in February 2018 (game year 18) at **14,190 people** (the peak), with 5 loans
and $1,530. The strategy's target curve called for 12,000 by 2005, 22,000 by 2010 and 40,000 by 2020.
The city was at 3,160 in 2005 and 11,220 in 2010, and loan payments ($2,000 a year) had grown bigger than
property tax ($1,391 a year).

| Year | People | Home tiles built | Empty home tiles | Cash | Loans | Taxes R/C/I | Demand R/C/I |
|---|---|---|---|---|---|---|---|
| 2001 | 180 | 9 | 99 | $8,472 | 1 | 5/4/4 | max/min/max |
| 2003 | 1,660 | 100 | 179 | $8,260 | 2 | 5/4/4 | max/max/0 |
| 2005 | 3,160 | 200 | 211 | $10,620 | 3 | 5/4/4 | max/0/max |
| 2008 | 7,680 | 444 | 231 | $2,399 | 3 | 5/4/4 | max/max/max |
| 2010 | 11,220 | 657 | 18 | $445 | 3 | 7/6/6 | max/max/max |
| 2012 | 11,520 | 673 | 2 | $1,459 | 4 | 7/6/6 | 0/max/max |
| 2014 | 12,050 | 706 | 71 | $7,135 | 5 | 7/8/8 | 0/max/max |
| 2016 | 12,620 | 765 | 12 | $3,550 | 5 | 7/7/8 | 0/min/max |
| 2018 | 14,190 | 777 | 0 | $1,530 | 5 | 7/7/8 | 0/min/max |

## What happened, phase by phase

**2000-2005: a slow start, not attempt 4's.** The strategy was "copy attempt 4's fast start" (attempt 4 had
647 home tiles built and 12,970 people by 2005). Attempt 10's three block plans zoned only about 410 home
tiles by 2005, and only 200 of them were built. In the first year only 9 home tiles grew (attempt 4: 151).
Cash sat at $8,000-10,600 the whole time while home demand was at maximum.

**2005-2010: steady growth, then the land ran out.** Growth was good (about 1,500 people a year) while there
was empty land. By 2010 the empty home tiles were down to 18 and cash was under $500. Taxes went from
5/4/4 to 7/6/6 to carry 4 loans.

**2010-2018: home demand fell to zero.** After the tax rise and with no land, home demand slid from
maximum to about zero and stayed there, even after new land was added. Loan #5 (Dec 2012) paid for an
east block of 170 shop tiles and 102 home tiles; it filled in 18 months but only added about 2,000 people.
A south factory block (2015) filled with factories, but about 1 in 8 buildings in the city stood abandoned,
unemployment reached 14%, and factory demand stayed at maximum all along (the sign of the industry cap
and failed trips, not of missing land). No zoo, stadium, seaport or airport was ever affordable.

## Control failures vs strategy failures

**Control failures (the agent did not carry out its own plan):**
- **The block plans did not match the strategy's own pace.** The strategy said ~650 home tiles by 2005;
  the plans built ~410 and nothing compared the city to the target until this post-mortem. That is a
  checking gap, so it is counted here. The block dates slipped too: block 2 was planned for Jan 2002 and
  built Dec 2002; block 3 was planned for Jan 2003 and built Dec 2004. **Fixed:** `bot/pace.py` reads the attempt's `pace.json`
  (population and zoned home tiles by year) and prints a PACE line in every step; `play.sh` stops when
  the city is under 70% of the target. Run on attempt 10's own saves, it flags "behind" from Feb 2001.
- **Two wiring mistakes in plans, both caught by the tools within one step:** the east factory strip's
  power column touched only empty zones (2009, fixed with two crossings), and one power crossing was
  planned on a road junction instead of next to it (2015, fixed in the same step). No time was lost.

**Strategy failures:**
1. **Too little land in the first five years.** The day-one block had ~108 home tiles; attempt 4 had over
   150 built within a year. With cash idle at $8,000-10,000 there was no reason not to zone more.
2. **Loans did not pay back.** Five loans cost $2,000 a year. Loans #4 and #5 each added about 2,500
   people (~$230 a year of tax), far below the ~5,500 people a loan needs to pay for itself.
3. **Taxes rose before the city was big.** Raising homes to 7% at 11,000 people (2010) coincided with home
   demand falling from maximum to zero for the rest of the game.
4. **Too many factories for the trade capacity.** By 2018: 777 home, 297 shop and 551 factory tiles.
   Factory demand sat at maximum while factories were abandoned, so more factory land did not help.
5. **No unlocks** (zoo, stadium, seaport, airport): there was never cash once the loans were paid.

## What changes next time
See the updated `claudeville-3/reflection.md` (all ten attempts) and the attempt 11 strategy.
