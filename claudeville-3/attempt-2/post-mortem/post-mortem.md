# Claudeville 3 · Attempt 2 post-mortem

**Result: missed.** Stopped in January 2017 (game year 17 of 50). The city peaked at **35,690 people
in January 2011**, well ahead of the straight-line pace at the time. It then shrank to about 29,000
with 30% unemployment, more than 1,200 empty buildings, ten $10,000 loans and a negative bank balance.

| Year | People | Cash | Loans | Unemployed | Abandoned |
|---|---|---|---|---|---|
| 2001 | 1,650 | $6,600 | 1 | 7% | 6 |
| 2002 | 5,140 | $4,535 | 1 | 0% | 5 |
| 2005 | 10,670 | $2,969 | 3 | 11% | 137 |
| 2007 | 19,020 | $7,921 | 5 | 3% | 74 |
| 2009 | 28,920 | $5,824 | 7 | 6% | 216 |
| 2011 | 35,690 | $3,160 | 7 | 4% | 166 |
| 2013 | 31,720 | $7,539 | 9 | 18% | 709 |
| 2016 | 28,560 | $6,014 | 10 | 33% | 1,331 |
| 2017 | 29,940 | −$1,762 | 10 | 30% | 1,208 |

## What happened, phase by phase

**2000–2007: the compact layout worked.** Thin bands of homes, shops and factories next to each
other, with cross streets every 10 tiles, fixed attempt 1's long-commute problem. The city grew
30–40% a year: 1,650 people after one year (attempt 1 had 20), 10,000 by 2005, 19,000 by 2007.

**2002–2008: power and water kept breaking.** The coal plants ran out twice; when power ran short,
the water pumps lost power and water dropped to zero. Most pumps had no power at all for years:
pumps don't pass power to each other, and some power-line junctions didn't connect. Fixing the
junctions took water from 47% to 99% of buildings in 2008.

**2008–2011: wiring the south.** Power lines drawn across zoned land get replaced by buildings when
they grow, and power did not flow from those buildings back into the lines further on. Whole
districts went dark. Extra plants placed inside those districts brought power back.

**2011–2016: decline.** Home demand turned negative first, then shop and factory demand. Factory
land was 100% built, so new factory land was zoned, then police, fire stations and a hospital were
added. Unemployment kept rising (4% → 33%). The traffic map showed every north–south street jammed
and the newspaper said "Traffic Toxic". Commutes on a road-only grid this size were failing.

**2016–2017: out of money.** Ten loans cost about $4,000 a year, roughly all of the tax income.
Clearing a column of buildings for a new north–south road used the last $6,000, and the demolition
cut power and water again. The bank balance went negative.

## Top causes

1. **Traffic with roads only.** One-lane streets carried a 35,000-person city with no rail, subway or
   bus. *Evidence:* traffic map saturated on every north–south street; "Traffic Toxic"; jobs vanished
   while factories and shops emptied at the same time, the same signature as attempt 1's long commutes.
2. **Fragile power wiring.** Lines over zones get absorbed by buildings; pumps don't conduct; some
   junctions don't connect; distant districts brown out. *Evidence:* 37 of 132 pumps powered in 2008;
   southeast district unpowered from 2011 to the end.
3. **Debt trap.** Ten bonds in 16 years. Payments rose to match all tax income, leaving nothing for
   transit or services when the city needed them. *Evidence:* budget net about +$50 in 2012 at 8% tax.
4. **Services far too late.** No police, fire, school or hospital until 2011–2015.
   *Evidence:* "Citizens Request Protection"; life expectancy 59, education 80.
5. **Tool bugs cost time and money.** The bulldozer button was left on "De-zone", so the helper that
   removes test roads silently failed, leaving dozens of stray road tiles that blocked buildings.

## What changes next time

- **Keep the compact band layout** (it is the reason for the fast start).
- **Plan for traffic from day one:** streets both ways every 6–7 tiles, and reserve a rail corridor
  through the middle of each block. Build rail with stations (or a subway) before 20,000 people.
- **Power done properly:** dedicated un-zoned power-line columns that buildings can't absorb; pump
  fields built as alternating rows of pumps and power lines; a plant in every district; check the
  power map from the save every January (`bot/pmap.py`) and fix any dark area in the same year.
- **At most 5 loans.** Raise tax to 7–8% once demand is strong; spend on transit and services
  before more zoning.
- **Services on schedule:** fire + police by 5,000 people, school + hospital by 10,000, one more of
  each per 10,000.
- **Tooling:** always pick "Demolish" from the bulldozer menu; check every helper's result in the save.

Next: [attempt 3 strategy](../../attempt-3/strategy.md)
