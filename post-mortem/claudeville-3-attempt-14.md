# Claudeville 3 · Attempt 14 post-mortem

**Result: missed.** Stopped in July 2013 at **23,580 people** (the peak), with 9 loans and a deficit of
about $3,000 a year. The aim was to beat attempt 2's 35,690 with attempts 2 and 4's low taxes.

| Year | People | Home tiles built | Loans | Taxes R/C/I | Unemployed |
|---|---|---|---|---|---|
| 2003 | 7,300 | 501 | 2 | 6/6/4 | 4% |
| 2005 | 12,130 | 738 | 4 | 6/6/6 | 5% |
| 2008 | 18,040 | 1,048 | 5 | 6/6/6 | 5% |
| 2010 | 20,360 | 1,202 | 7 | 6/6/6 | 5% |
| 2013 | 23,580 | 1,269 | 9 | 5/6/6 | 5% |

## What happened
The low-tax version of attempt 13 never collapsed: unemployment stayed at 4-7% the whole time (attempt 13
reached 26%), and the city grew every year. But growth after 2005 was only ~1,500 people a year, and every
step needed a loan: power (#5), district 6 (#6), the airport (#7), job land (#8, #9). The airport worked -
shop demand jumped to ~1,950 and the new shop blocks filled within a year. By 2013 nine loans cost
~$3,600 a year against ~$1,600 of property tax plus ~$390 of ordinances.

## Control failures vs strategy failures

**Control failures:** none that cost time. Two plan details were caught by the tools before the clock ran:
a road planned over the south pump lines (left out; the cells reach other roads), and a pump row that
needed a power column from a block not built in this attempt. A plan file was mangled by a bad edit and
rewritten before it was built.

**Strategy failures:**
1. **The money wall again.** ~$90,000 (nine loans plus tax) bought 23,580 people - ~$3.80 per person,
   worse than attempt 12's ~$2.90. Low taxes kept the city healthy but halved the income that pays for
   land.
2. **Light homes everywhere.** People per home tile stayed ~18-19; only district 6 was dense.
3. **Power and water bought in small, late pieces** (a gas plant, three coal plants, five pump batches),
   each time at < 10% spare.

## What changes next time
See `claudeville-3/reflection.md` (all fourteen attempts) and the attempt 15 strategy.
