# Claudeville 3 · Attempt 4 post-mortem

**Result: missed.** Stopped in November 2021 (game year 21) at about **30,000 people** (peak 30,860).
The city had ten $10,000 loans costing **$3,800 a year** against **$2,627 of tax income**, a negative
bank balance, and weak demand for homes and shops. 100,000 by 2050 was out of reach.

| Year | People | Cash | Loans | Unemployed | Land value | Pollution |
|---|---|---|---|---|---|---|
| 2001 | 900 | $4,502 | 1 | 3% | 6 | 1 |
| 2004 | 10,920 | $787 | 3 | 3% | 14 | 6 |
| 2008 | 16,070 | $260 | 4 | 3% | 16 | 9 |
| 2011 | 21,670 | $2,511 | 6 | 1% | 21 | 12 |
| 2014 | 24,870 | $7,761 | 8 | 3% | 24 | 14 |
| 2017 | 28,750 | $3,101 | 9 | 5% | 27 | 16 |
| 2021 | 30,150 | −$863 | 10 | 5% | 28 | 16 |

## What went right
- **Power and water never failed.** Un-zoned power columns linked at both ends, wired pump fields
  and a pipe main kept every building powered all game (0 unpowered buildings at every check).
- **No disaster damage.** Five fire stations, a volunteer fire department; no fire spread.
- **Steady early growth:** 10,900 by 2004, close to attempt 2's pace.
- **A seaport works.** It turned factory demand from 0 to the maximum within two years.

## What went wrong, phase by phase

**2004–2013: money always short.** Every new block needed a loan. Each loan added about $350–400
a year in payments but brought only ~3,000 new people (~$300 a year in tax). Taxes were raised to
cover payments (homes up to 12%), which cut demand.

**2013–2016: land full, homes thin.** Homes averaged only ~22 people per tile (all low-density).
Dense housing grew on test lots and in a new north district, but land value stayed low (≈25) because
homes sit next to factories and coal plants, so dense towers stayed rare.

**2016–2021: demand ran out.** Demand for homes, shops and factories fell to zero or below around
28,000 people. A second neighbor link and a seaport revived factory demand, but there was no money
left to build roads for the new factory land, and loan payments passed 140% of tax income.

## Top causes

1. **Low-value city = low tax income.** Property tax depends on land value. Factories and six coal
   plants next to homes kept land value around 20–28 and pollution rising all game. *Evidence:* tax
   income only ~$2,600 a year at 30,000 people.
2. **Borrowing for growth that didn't pay back.** Ten loans, each costing more per year than the tax
   from the people it added. *Evidence:* payments $3,800 vs taxes $2,627 in 2021.
3. **Low density.** ~22 people per home tile. 100,000 people at that density needs about 4× the
   land available east of the river.
4. **Seaport (trade) came too late.** Factory demand had been stuck near zero for years before it.

## What changes next time
- **Build for land value from day one:** keep factories in a separate district downwind, away from
  homes, with shops in between; parks along home bands; homes next to the river and lakes.
- **Cleaner power:** fewer, larger plants placed far from homes (gas or nuclear later), not six coal
  plants on the riverside.
- **Dense homes and shops from the start** wherever land value allows; schools and hospitals early.
- **Seaport early** (when factories need trade), stadium/airport when demand stalls.
- **Loans:** at most 4–5, only for things that clearly pay back; keep tax at 7–9% on homes.
- Keep attempt 4's wiring rules and fire coverage.

Next: [attempt 5 strategy](../claudeville-3/attempt-5/strategy.md)
