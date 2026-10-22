# Claudeville 4 · Attempt 2 strategy (from claudeville-4/reflection.md)

Goal: 200,000 by Jan 2050, same map, Medium, disasters on.

Attempt 1's fast start reached 45,530 by 2011 and was ahead of every earlier attempt. Then fire and debt broke it:
two airport fires forced two full rebuilds, and the loans ran into the game's limits (50 bonds; game over near -$100,000).
This attempt keeps the start and changes how fire and debt are handled.

## Plan
1. **The same fast start** as attempt 1: `a20-day1`, then the east-bank sequence. Cross the river by ~2006.
   Use checkerboard districts and run `trips.py` before each build.
2. **Fire stations in every district plan.** Place one every ~14 tiles; the audit WARNs below one per ~6,000 people, and `play.sh` stops on it.
   Keep fire funding at 100%.
3. **No airport until shops are really capped.** That means shop demand stays negative while jobs are short, and only after ~25,000 people.
   Then build it on bare land 10+ tiles from any district, with its own fire station. Skip `c4-stadium-airport`'s airport;
   the stadium goes elsewhere.
4. **Loan budget: about 30 in total, at most 2-3 a year.** Take a loan only for land, power, water or recreation that adds people.
   Never take one for repairs that a cheaper fix covers.
   - If cash falls below -$50,000, `play.sh` stops. Then raise taxes and cut costs; never cut taxes.
5. **Taxes:** the controller ceilings are homes 11%, shops 9% and factories 8%, with a floor of 6% while in debt.
6. **Recreation ahead of every ~15,000 people**, plus pumps and coal plants two years ahead of the alarms, as before.
7. **After a fire:** dispatch the firefighters and drop new fire stations at the front at once. Bulldozed breaks were jumped in attempt 1.
   Rebuild with `rebuild.py`.
8. **Arcologies at 120,000** if the money allows.
