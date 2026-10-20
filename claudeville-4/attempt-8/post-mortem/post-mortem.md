# Claudeville 4 · Attempt 8 post-mortem

**Result: failed.** Peak **92,500** people (Feb 2038). A great fire in Nov 2038 took the city to ~38,000; the money ran
out in **January 2046** (-$105,463).

| Date | People | Loans | Notes |
|---|---|---|---|
| Jul 2003 | 12,380 | 5 | About a year ahead of attempt 6 |
| Jul 2008 | 29,350 | 10 | Ahead of attempt 6 (25,600) |
| Jul 2017 | 51,110 | 16 | Ahead of attempt 6 (45,480) |
| Feb 2021 | 64,670 | 18 | Ahead of attempt 6 (57,580) |
| 2022-2024 | 66,090 → 61,650 | 18 | Recession: unemployment 16%; tax cut |
| Feb 2038 | 92,500 | 27 | Peak (attempt 6: ~105,000) |
| Nov 2038 | 92,250 → 37,940 | 30 | **Alien-ship fire → great fire** (~4,800 rubble tiles) |
| Jan 2046 | 24,680 | 30 | Game over |

## Control failures (each now has a fix)
1. **The great fire: I ran the game unwatched at Cheetah for ~10 minutes during the disaster.** A ~24-tile fire by the
   seaport homes spread across the west bank, the south-west and the north district.
   *Fixed:* `disaster.sh` runs 10-second bursts centred on the disaster and stops when the fire grows; CLAUDE.md rule.
2. **firebreak.py misread rooftops and the alien ship as flames** (290-tile plan for a 24-tile fire). Not used; a tight
   ring was cut by hand. *Rule:* ring only the real cluster.
3. **Container restarts (3) and a worker restart**: a hand-typed load opened a blank map and a build saved over the
   attempt (restored from the Feb 2003 yearly save); load.sh's scratch check read a stale file and deleted the save.
   *Fixed:* load.sh (verified load, scratch file removed first, attempt file must exist), build.py refuses any city
   but "Claudeville 3"; bond count read from the save's bond rate after a restart.
4. **A misread of the save after the first restart cost one extra early loan.**

## Strategy
- Until 2038 the replay of attempt 6 with the loan floor worked: ahead of attempt 6 for 20 years, ~3,400 people per loan.
- The 2022-24 recession (unemployment 16%) cost ~4 years; taxes had drifted to 9-10%.

## Next (attempt 9)
- Same plan as attempt 8 (it was the best start), plus disaster.sh for every disaster and taxes held at 8%.
