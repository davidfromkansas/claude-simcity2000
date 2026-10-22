# Claudeville 4 · Attempt 7 post-mortem

**Result: failed.** Peak **91,980** people (Feb 2041). The money ran out in **January 2046** (-$104,898).
Attempt 6, with the same rules, reached 120,770.

| Date | People | Loans | Notes |
|---|---|---|---|
| Jul 2006 | 18,000 | 7 | Same pace as attempt 6 |
| Nov 2008 | 23,320 | 10 | River crossed and west link built (attempt 6: 2015) |
| 2015-2017 | ~38,900 | 13-14 | Two-year stall: shops had no land |
| Nov 2019 | 44,790 | 16 | First stripplan district (26 audit FAILs, fixed) |
| 2022-2023 | 54,750-57,590 | 18-20 | Second strip district ran out of cash part-way (2 extra loans) |
| Jul 2025 | 64,000 | 21-22 | Two coal plants built as trails of stray roads near the map edges (~$5,000 lost) |
| Feb 2041 | 91,980 | 32 | Peak; bond payments $19k a year vs $9.8k income |
| Jan 2046 | 81,580 | 32 | Game over |

## Control failures (each one now has a check)
1. **The strip generator's first districts were broken**: roads cut by its own power lines, cross streets not joined,
   lines over water, line columns not joined to power (26 + 32 audit FAILs). *Fixed:* lines before roads, cross streets
   reach the road above, no lines on water, a WARN for unjoined line columns.
2. **Plans ran out of cash part-way** (2022-23), leaving roads without zones or pipes. *Fixed:* `build.py` refuses a
   plan whose missing tiles cost more than the cash on hand.
3. **Clicks near the west edge and the north-east corner landed wrong** (2025): two coal plants became trails of road
   tiles. *Fixed:* `build.py` refuses tiles within 8 of the west edge or the north corners; the harmless strays are
   listed in `run.json` known_strays.
4. A refused plan (2007 west block) was again caught only because `seq.sh` now prints SEQ NOT CLEAN.

## Strategy failures
1. **Borrowing outran growth**: 32 loans for ~92,000 people (~2,900 each; attempt 6: ~4,400). The bond rate also
   rises with the number of loans: 32 loans cost $19k a year (~$600 each).
2. **The early river crossing did not pay**: the west district filled slowly while shops were capped (2015-17 stall).
3. **Taxes swung too much** (7 -> 10 -> 7 -> 10): each cut was followed by a deficit, each raise by a stall.

## What changes next time (attempt 8)
- Replay attempt 6's build order (its loans paid best), using the fixed tools only where attempt 6 had none.
- Hard loan cap: no loan unless people per loan stays above ~4,000 (a new guard check).
- Keep taxes steady at 8-9% once the city passes 30,000.
