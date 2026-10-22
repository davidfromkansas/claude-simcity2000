# Claudeville 3 · Attempt 11 post-mortem

**Result: missed.** Stopped in February 2020 (game year 20) at **20,790 people** (the peak), with 7 loans
and -$3,721 cash. Second-best start of all attempts after 4 (attempt 10: 14,190 at its end). The target
curve called for 22,000 by 2010 and 42,000 by 2020.

| Year | People | Home tiles zoned | Cash | Loans | Taxes R/C/I | Unemployed | Demand R/C/I |
|---|---|---|---|---|---|---|---|
| 2001 | 480 | 288 | $3,662 | 1 | 4/4/4 | 3% | max/-/+ |
| 2003 | 2,970 | 683 | $2,524 | 2 | 4/4/3 | 4% | max/max/+ |
| 2005 | 8,850 | 684 | $2,806 | 3 | 4/6/6 | 3% | max/+/max |
| 2007 | 11,530 | 936 | $2,181 | 4 | 5/7/7 | 3% | max/max/max |
| 2009 | 14,390 | 1,112 | $4,302 | 5 | 5/7/7 | 4% | +/max/max |
| 2011 | 16,250 | 1,112 | -$74 | 5 | 5/7/7 | 7% | -/+/max |
| 2013 | 16,040 | 1,112 | $1,703 | 6 | 5/7/9 | 12% | -/+/max |
| 2015 | 17,340 | 1,112 | $5,464 | 7 | 5/7/9 | 10% | -/-/max |
| 2017 | 19,120 | 1,112 | $54 | 7 | 5/7/9 | 6% | -/+/max |
| 2020 | 20,790 | 1,112 | -$3,721 | 7 | 8/8/9 | 4% | +/max/max |

## What happened, phase by phase

**2000-2009: the fast start worked.** Day one built 288 home tiles (attempt 10: 108); blocks 3-4 (2003),
district 5 (2006) and district 6 with the first zoo (2008) followed as land ran out. Population reached
14,150 by 2008, close to attempt 4's pace. The game refused a second loan at founding ("credit rating"),
so day one was limited to about $20,000.

**2009-2014: stuck at 16,000.** Three things at once: water ran short for 18 months (2009-2010); the city
ran out of factory land (1,112 home tiles vs 489 factory tiles, zero empty factory tiles in 2012) so
unemployment rose and homes were abandoned; and when factory land was added, 137 tiles stayed empty
with factory demand at maximum - the industry cap. Cash went below zero.

**2014-2020: the seaport worked, the debt did not.** A seaport (loan #7, Feb 2014) let factories fill
again: 524 -> 606 built, unemployment 15% -> 4%, population 16,000 -> 20,800. A tax test in Dec 2018
(homes 5% -> 8%) showed home demand stays positive at 8% when there are jobs. But seven loans cost
about $3,000 a year against about $2,100 of tax, so cash fell every year.

## Control failures vs strategy failures

**Control failures:**
- **Ran 18 months short of water (2009-2010).** Audit printed "spare water only 0-6%" as a WARN and the
  play loop did not stop on WARN lines; 146 buildings went dry. **Fixed:** `play.sh` now stops when
  spare water or power is under 10%.
- **Camera calibration built a 3-tile bridge** on the lake (clicking a shore tile). The build guard caught
  the stray road; the bridge was bulldozed in the same step. **Fixed:** `autocal.sh` checks 24 px around
  each spot for water and stops if any new bridge tile appears.
- Plan mistakes caught by the tools within one step (no time lost): a one-tile power gap at (77,56),
  three pipe rows touching the network only diagonally, one zone tile lost during a fix.
- The pace alarm fired from 2007 on; each time I added land or noted why I ran on. It worked as
  designed, but it cannot help when the answer needs money the city does not have.

**Strategy failures:**
1. **Seaport 9 years late.** The strategy said "seaport at ~5,000"; it was skipped for lack of cash and
   built at 16,000 after three stuck years. It was the single most effective build of the attempt.
2. **Factory land fell behind.** Homes grew to 1,112 tiles while factory land stayed near 490; the ratio
   rule (factories up to ~60% of homes) was in the strategy but not checked.
3. **Taxes too low for too long.** Homes stayed at 4-5% for 18 years on the belief (from attempts 6 and
   10) that 7% kills home demand. The 2018 test showed 8% holds when jobs exist; those earlier drops were
   most likely the job shortage.
4. **Seven loans.** The debt rule was loosened twice under pressure. At 20,000 people the city cannot
   carry more than about four.

## What changes next time
See `claudeville-3/reflection.md` (all eleven attempts) and the attempt 12 strategy.
