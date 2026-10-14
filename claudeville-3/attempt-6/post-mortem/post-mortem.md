# Claudeville 3 · Attempt 6 post-mortem

**Result: missed.** Stopped in March 2013 (game year 13) at about **11,500 people** (peak 11,620),
$1,464 in debt with 3 loans and demand falling. 100,000 by 2050 was out of reach.

| Year | People | Cash | Loans | Unemployed |
|---|---|---|---|---|
| 2001 | 800 | $4,833 | 1 | 4% |
| 2003 | 4,250 | $2,738 | 1 | 5% |
| 2005 | 6,020 | $3,064 | 2 | 7% |
| 2007 | 8,250 | $1,262 | 2 | 5% |
| 2009 | 8,920 | $5,998 | 3 | 5% |
| 2011 | 11,230 | −$427 | 3 | 3% |
| 2013 | 11,520 | −$1,464 | 3 | 5% |

## What happened, phase by phase

**2000–2003: a clean start.** Attempt 4's first block, built from a script and checked from the save
before the game ran: trade link, pumps on the pipes, power reaching every zone. 4,250 people by 2003,
with every check passing at every step.

**2004–2009: borrowing for land.** The land filled up twice; loans #2 and #3 paid for the two halves
of block 2 and a third power plant. Population grew to 9,950, but every year ended with less money.

**2010–2013: the money ran out.** At 11,500 people, property tax brought in **$1,042 a year** while
the three loans cost **$1,599 a year**. Raising home tax to 12% cut demand, and with no cash
nothing more could be built.

## Control failures vs strategy failures

**Control failures (the agent could not carry out its own plan):** small, and caught by the new checks.
- A plan put the fire station on a pond the agent had not noticed; the build runner reported it and it
  was moved. `build.py` now refuses plans that put zones or buildings on water.
- The camera calibration left one rubble tile; it now clears its own rubble.
- No setup mistake from attempt 5 happened again: the audit passed at every step.

**Strategy failures (the real cause):**
1. **Loans cannot pay for themselves.** Each $10,000 loan costs about $530 a year. A block it pays for
   brings ~2,000–3,000 people, worth only ~$200–300 a year in tax (about $0.09 per person per year
   at this land value). Every loan made the city poorer. Attempt 4 failed the same way.
2. **Too much shop land, every attempt.** Shop demand was negative almost all game, so shop bands sat
   half empty or abandoned. Experienced players advise homes ≈ shops + factories, with few shops early.
3. **Pumps placed inland** gave little water, so water ran short at almost every check.

## What changes next time
- **No loans** (or one at most, only on day one). Build only from cash; grow block by block as
  income allows.
- **Zone to demand:** add a zone type only while its demand is positive; homes first, factories
  second, shops only when shop demand is positive.
- **Pumps beside water** (river and lakes), fewer and better placed.
- Keep every controller check (audit, build runner, stall alarm).

Sources for the money advice: [SimCity 2000 Advice: Making Money](https://patcoston.com/co/strat3.aspx).

Next: [attempt 7 strategy](../../attempt-7/strategy.md)
