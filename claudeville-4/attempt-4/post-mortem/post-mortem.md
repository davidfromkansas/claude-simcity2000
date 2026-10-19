# Claudeville 4 · Attempt 4 post-mortem

**Result: failed.** Peak **74,150** people (Jan 2024), against a goal of 200,000 by Jan 2050.
The game ended in **January 2038** at -$102,377 cash, when the mayor was thrown out.

| Date | People | Loans | Notes |
|---|---|---|---|
| Feb 2007 | 14,760 | 7 | **The airport developed within ~7 months** (power line through it); shop demand +1,936 |
| Feb 2010 | 26,640 | 11 | River crossed; on pace |
| Jul 2013 | 41,480 | 13 | Slightly ahead of attempt 2 |
| Feb 2017 | 57,210 | 17 | Higher taxes (10/9/9) let the loan guard allow more loans |
| Sep-Nov 2017 | 59,820 → 30,380 | 20-25 | **Great fire** (probably a plane crash near the south airport): ~3,900 tiles |
| Jun 2020 | 50,030 | 25 | Recovered |
| Jan 2024 | 74,150 | 27 | Peak |
| May 2024 | 73,400 → 69,080 | 27 | A smaller fire (~300 tiles) |
| Jul-Sep 2035 | 70,960 → 24,020 | 28 | **A great fire burned most of the city while it ran unattended** |
| Jan 2038 | - | 28 | Game over |

## What worked
- **The airport.** A power line run through the zone made it develop within months. This is the fix found in the lab test.
- The early build order and the audit checks. Gaps were found at once.

## Control failures vs strategy failures

### Control failures
1. **Autocal stray roads kept landing on power lines** after builds, cutting them. Fixing them by hand cut more lines (twice).
   *Fixed:* `build.py` ends every build with a sweep. Lone new road tiles are bulldozed and any line under them is re-placed. It caught one on its first run.
2. **Two rebuild processes ran at once** (2017). I started a second while the first was still going.
   *Rule:* check `ps` for `build.py` before starting another.
3. **The run-out script ignored fires and misread its stop date.**
   - It ran on through the 2035 fire unattended.
   - Its deadline check matched population figures like "20880" as a year.

   *Fixed:* the date check now reads only the date. *To do:* it must stop on new rubble like `play.sh` does.
4. **The firefighter dispatch did not work as I expected.** Only 2-3 units ever appeared. Clicks did not move them to a second fire.

### Strategy failures
1. **Fire, three times.**
   - The 2017 fire (~3,900 tiles) cost ~30,000 people and 6 loans of rebuilding.
   - The 2035 fire finished the city.
   - The fuel was there: a 2x2 tree park in every home cell, and rubble left in burned and abandoned blocks. Research says both burn.
   - The airport sat only 5 rows from the south districts.
2. **Money.** After the 2017 rebuild the city never got back above a deficit of ~$5k a year.
3. **The city stalled near 70,000 from 2023** with all demand negative, even with a working airport. Factory demand fell to ~-800.

## What changes next time (attempt 5)
- **Fire first:**
  - No tree parks in home cells; land value comes second to survival.
  - Bulldoze rubble promptly; it is fuel.
  - Airport ≥15 tiles from any district, with the line through it.
  - Coal plants spread out, each with a station.
- **On any new rubble:** pause, find the fire, and clear a firebreak 2+ tiles wide down to bare land. That means bulldozing twice, removing rubble and roads too, while the fire is small. This needs cash, so keep ~$5k in hand from 20,000 people.
- **The run-out script stops on new rubble.**
