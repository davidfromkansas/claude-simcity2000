# Claudeville 3 · Attempt 3 post-mortem

**Result: missed — destroyed by a disaster.** In May 2011 (game year 11) an earthquake started fires
that spread across the whole city. About 3,500 tiles burned, including most roads; only about 250
building tiles and two power plants were left. With six $10,000 loans and no tax base left, the
city could not be rebuilt. Peak population: **18,410** (spring 2011).

| Year | People | Cash | Loans | Unemployed | Abandoned |
|---|---|---|---|---|---|
| 2001 | 120 | $5,540 | 1 | 13% | 1 |
| 2003 | 3,190 | $4,593 | 1 | 2% | 12 |
| 2005 | 8,260 | −$109 | 2 | 2% | 21 |
| 2007 | 13,510 | $4,190 | 4 | 2% | 36 |
| 2009 | 16,430 | $270 | 4 | 4% | 76 |
| 2011 | 17,580 | −$81 | 5 | 8% | 145 |

## What happened, phase by phase

**2000–2001: wiring fixed, but a slow first year.** The new un-zoned power columns worked, but only
one of them touched the coal plant, so most zones had no power for a year (120 people by January).
Once linked, every building had power for the rest of the game: the wiring lessons from attempt 2 held.

**2002–2007: healthy but slower growth.** 1,000 → 13,500 people with 2–3% unemployment and no
power or water failures. Growth was slower than attempt 2 (19,000 by 2007) because money ran out
sooner: loan payments passed tax income in 2008.

**2008–2010: stall.** Raising the tax to 8% to cover the loans pushed factory and shop demand
negative, and the new south block's homes had no jobs nearby because its middle bands were never
zoned for lack of cash. Population barely moved (15,030 → 17,580). Separate tax rates (homes 10%,
shops 6%, factories 5%) and zoning those bands were the fix, applied in January 2011.

**May 2011: earthquake.** Fires spread from block to block. The city had one fire station, built
for 5,000 people, and no money to respond.

## Top causes

1. **Not ready for disasters.** One fire station for 18,000 people, no cash reserve, and solid
   blocks of buildings with nothing to stop fire spreading. *Evidence:* rubble 3,500 tiles, two
   power plants left.
2. **Money too tight to build ahead.** Loan payments exceeded tax income from 2008; zoning the jobs
   bands next to new homes had to wait. *Evidence:* 208 empty home tiles in the south block in 2011.
3. **One flat tax rate.** At 8% for everyone, industry demand collapsed (+1,245 → −654 in two years).
   SimCity 2000 lets you tax homes, shops and factories separately (the property-tax book).

## What changes next time

- **Fire stations everywhere:** one per block of about 30×35 tiles from the start (they are cheap,
  $500), more as density grows; police likewise. Keep the dispatch tool in mind for any fire.
- **Firebreaks:** keep the empty power-line columns and streets as breaks; add small parks or empty
  rows between dense blocks.
- **Cash reserve:** keep at least $5,000 after year 5 for emergencies.
- **Separate taxes from day one:** homes higher (they have the demand), factories and shops low.
- **Keep attempt 3's wiring** (un-zoned power columns, linked at both ends; wired pump fields;
  a north–south pipe main) and **attempt 2's speed** (build blocks ahead of demand).

Next: [attempt 4 strategy](../../attempt-4/strategy.md)
