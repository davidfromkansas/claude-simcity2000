# Claudeville 3 · Attempt 16 post-mortem

**Result: missed.** Stopped in February 2014 at **24,870 people** (the peak), with 9 loans and a
~$2,000-a-year deficit. Best city since attempt 4 at the same date; it passed attempt 15's 18,000 wall.

| Year | People | Home tiles built | Loans | Unemployed |
|---|---|---|---|---|
| 2003 | 7,990 | 386 | 3 | 3% |
| 2005 | 13,730 | 675 | 5 | 5% |
| 2008 | 18,020 | 997 | 7 | 14-20% |
| 2010 | 22,030 | 1,161 | 8 | 16% |
| 2014 | 24,870 | 1,326 | 9 | 15% |

## What happened
The trip research held up: wherever factory cells sat next to homes they filled (factory land went from
116 empty tiles to 29 in 18 months, twice), and the one batch I zoned factory-next-to-factory was caught by
the trip check at 36% success and fixed before the clock ran. The airport (2011) opened shop demand at once.
But the city never had enough jobs for its dense homes (unemployment 14-20% from 2008), and every new block,
plant and pump batch needed a loan. By 2014 nine loans (~$3,600 a year) outweighed tax (~$2,300 with homes
at 4%), cash was below zero and shop and factory land were both full at maximum demand.

## Control failures vs strategy failures

**Control failures:**
- **The second coal plant did not fit the cash** (dense zoning costs $10/tile) and I started the clock
  anyway, gated only on the audit; power ran short within seven months. **Fixed:** play now starts only
  after every plan reports "BUILD: checked" (this gate then held twice: district 5, the factory rows).
- **Cash ran out mid-build** (Jul 2013): the pump batch went in partly and one pump was left without a pipe
  (audit FAIL). Two plain check steps ran to January with that harmless FAIL in place - a deliberate,
  logged exception.
- Plans copied from attempt 14 assumed a road (y90) that this attempt never built; the trip check caught it.

**Strategy failures:**
1. **Too few jobs for dense homes.** Homes sat 300-480 tiles empty while unemployment ran at 15%+.
   Total tiles per person ended the same as the light attempts (~10 people per zoned tile of any kind).
2. **Money.** ~$85,000 (nine loans plus tax) for 24,870 people: ~$3.40 per person. Home tax stayed at 4%
   the whole game (the controller only lowers it while home demand is negative).
3. **No police at all** (removed from the plans since attempt 11) and land value averaging 21 - too low
   for dense homes to grow beyond 1x1 buildings (2x2 needs land value 96).

## What changes next time
See `claudeville-3/reflection.md` (all sixteen attempts) and the attempt 17 strategy.
