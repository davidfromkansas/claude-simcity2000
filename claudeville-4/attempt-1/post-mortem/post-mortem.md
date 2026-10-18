# Claudeville 4 · Attempt 1 post-mortem

**Result: failed.** Peak 87,090 people (Dec 2030), against a goal of 200,000 by Jan 2050.
The city ended in **January 2031**: cash fell below about **-$100,000** and the game threw the mayor out.
It returned to the start menu, so the attempt could not be played on.

| Date | People | Notes |
|---|---|---|
| Dec 2007 | 25,450 | Ahead of Claudeville 3's winning attempt (23,030) |
| Apr 2011 | 45,530 | Plane crash at the airport: the **first great fire** burned almost the whole east bank |
| Oct 2011 | 21,300 | East bank rebuilt from the plans (loans 17-21) |
| Feb 2014 | 44,030 | Recovered; back on pace |
| Dec 2020 | 68,020 | Ahead of pace (62,750); new west-bank districts |
| Feb 2023 | 77,850 | Second plane crash at the airport: the **second great fire** burned the east bank again |
| Apr 2023 | 48,240 | Second full rebuild, now with 25 fire stations (loans 36-41) |
| Jul 2028 | 78,680 | The game refused loan 51 (**bond cap 50**) |
| Dec 2030 | 87,090 | Peak; taxes had been cut to 2% |
| Jan 2031 | - | Cash -$108,214: the mayor is thrown out, game over |

## What worked
- The fast start: 25,000 people by 2007 and 45,000 by 2011, both ahead of Claudeville 3's winner. Crossing the river in 2006 instead of 2027 worked.
- Rebuilding from saved plans: after each fire the east bank's roads, lines, pipes and plants were rebuilt from every plan this attempt had built. Population recovered from 21,300 to 44,000 within 3 years.
- The new west-bank districts (south-west 2 and 3) grew as soon as they had power and water.

## Control failures vs strategy failures

### Control failures (the agent could not carry out its own plan)
1. **Calibration edge margin.** A 6-tile edge guard in `autocal.sh` broke calibration near the east edge, so builds placed 2x2 roads where parks belonged (~$3k lost).
   *Fixed:* the guard was loosened to 2 tiles.
2. **A stray autocal test road blocked the zoo.**
   *Fixed:* autocal now checks that its test roads are gone.
3. **The builder kept clicking with no money.**
   - In 2011 the east-bank rebuild spent everything, then kept clicking with $0 for about an hour.
   - In 2023 it did the same at $8.

   *Fixed:* `build.py` stops below $100 every 10 steps and before each gap round.
4. **Rubble under a stadium.** The stadium would not go down on rubble left by the fire.
   *Fixed:* `build.py` clears rubble under plants, stations and recreation first.
5. **The stadium team dialog.** A team already used by another stadium is greyed out, so no Done button appeared and the dialog blocked the screen. That also made a coal plant in the same plan fail.
   *Fixed:* `build.py` tries each team until Done shows.
6. **The rebuild generator dropped the cross-river power line.** It skipped the whole `line 21 68 59 68` step because part of it crossed water. The east-shore end was never rebuilt, and in 2023 the west bank's north blocks sat unpowered for months.
   *Fix for attempt 2:* the generator must keep the land part of a crossing step. Also, `audit.py` should flag a power plant with no line into the grid.
7. **Pipe networks that never linked.** About 540 buildings stood dry for years in 2012-2016. The audit only checked that pumps touched pipes, not that every zone's pipes reached a pump.
   *Fix for attempt 2:* add a water-reach check to `audit.py`, like the power-reach check.
8. **I killed my own shell twice** with `pkill -f` patterns.
   *Rule:* kill by PID only.

### Strategy failures (the plan itself was wrong)
1. **Far too few fire stations.** There were 3 stations for up to 78,000 people. Both great fires spread across the whole east bank. Bulldozed firebreaks 1, 2 and even 4 tiles wide were jumped.
2. **The airport sat inside the city.** Both great fires began with plane crashes at the airport, next to dense blocks. The airport zone also regrows by itself after a fire.
3. **Loans as unlimited money.** The plan assumed loans were never refused and that negative cash only blocked building. Both were wrong:
   - The game caps bonds at **50**.
   - At about **-$100,000** cash it ends the game.

   By 2026 the 41-48 loans cost $25-28k a year against $7k of taxes.
4. **Cutting taxes to 2% once the loan cap was reached.** I reasoned that money no longer mattered. It sped up the slide from -$18k to -$108k in two and a half years and ended the city.
   Keeping taxes at 9-12% would have kept the city alive longer, though still not out of debt.
5. **Two rebuilds cost about 25 loans and about 8 years of growth.** Without the fires, the attempt was on pace for roughly 100,000 by 2030.

## What changes next time (attempt 2)
- **Fire cover from day one.** A fire station every ~14 tiles in every district, built in the same plan as the district, and kept at 100% funding.
- **Airport late and isolated.** Build no airport until shops are actually capped (~20k+ people). Then put it on bare land at least 10 tiles from any district, with its own fire station.
- **A debt budget.** Keep loans to about 25-30. Watch the yearly balance and take a loan only for something with a clear payback.
  - Never let cash fall toward -$100,000.
  - At the loan cap, raise taxes; never cut them.
- **Controller:**
  - The rebuild generator keeps the land part of crossings.
  - The audit checks water reach and plants with no line.
  - `play.sh` stops when cash falls below -$50,000.
