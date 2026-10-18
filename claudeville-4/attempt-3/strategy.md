# Claudeville 4 · Attempt 3 strategy (from claudeville-4/reflection.md)

Goal: 200,000 by Jan 2050, same map, Medium, disasters on.

Attempts 1 and 2 grew as fast as any earlier city, but both ran out of money. Their loans cost more each year than the city paid in tax.
Attempt 2 also stalled from 2029 because shops, factories and homes hit caps that were never lifted.
This attempt keeps attempt 2's build order and fire cover, and changes money and caps.

## Plan
1. **Build order:** attempt 2's sequence. Day one, then:
   - the north district;
   - the seaport and east job strip;
   - district 5;
   - the river crossing by ~2008;
   - the west districts;
   - the south and south-west districts;
   - the north-west.

   Run `audit.py` after every build; it now FAILs disconnected roads.
2. **Loans:** a hard budget.
   - Take a new loan only while the last January's property tax and ordinances cover bond payments plus ~$1k.
   - Allow at most 1 extra loan a year while the city is under 20,000 people (the start needs money).
   - Repay the oldest bond when cash exceeds ~$15k.
3. **Taxes:** homes 9%, shops 8%, factories 8% from about 2,000 people. The controller goes up to 11 / 10 / 10 while demand is strong.
   Never cut below 7%, never raise into a stall.
4. **Fire cover:** about one station per 8,000 people, via `firegrid.py SPACING --avoid <next plans>`.
   Use spacing 18 instead of 14, plus a station beside each power-plant cluster.
5. **Caps ahead of demand:**
   - **Airport:** the isolated airport, enlarged to ~40 tiles by 40,000 people.
   - **Factory trade:** a seaport or rail link per ~10,000 factory workers. The audit's trade-capacity WARN is the trigger.
   - **Recreation:** ahead of every ~15,000 people.
6. **Watch the south-east district's road link.** In attempt 2 it was never joined to the rest of the city.
