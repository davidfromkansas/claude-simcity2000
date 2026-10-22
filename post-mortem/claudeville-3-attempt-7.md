# Claudeville 3 · Attempt 7 post-mortem

**Result: missed.** Stopped in July 2010 (game year 10) at **3,850 people**, with no debt. The city was
healthy but growing far too slowly to reach 100,000 by 2050. Stopped early, at the user's choice, to
research how the game really grows before attempt 8.

| Year | People | Cash | Loans | Unemployed |
|---|---|---|---|---|
| 2001 | 1,000 | $1,824 | 0 | 1% |
| 2003 | 1,550 | $1,822 | 0 | 3% |
| 2004 | 1,450 | $1,964 | 0 | 21% |
| 2005 | 1,750 | $1,259 | 0 | 9% |
| 2007 | 2,780 | $368 | 0 | 5% |
| 2009 | 3,220 | $891 | 0 | 8% |
| 2010 | 3,850 | $1,226 | 0 | 1% |

## What happened, phase by phase

**2000–2003: a debt-free start.** Block 1 (trade link, coal plant, dense homes, factories, pumps beside
the river) used $8,000 of the $10,000. The audit caught an unlinked power column before the clock ran.
Growth was slow and stopped near 1,500 with unemployment rising to 21%.

**2004–2007: small steps from savings.** Factory blocks, two shop strips and a dense-home block were
added one at a time as cash allowed. Each was checked tile by tile. Population crept to 2,800.

**2008–2010: still crawling.** Income stayed at about $250 a year for 2,500 people. With ~$1,000 a year
to spend, the city could only add one small block every year or two.

## Control failures vs strategy failures

**Control failures:** none reached the game. The audit stopped two plans that left a power column or a
road crossing unlinked; both were fixed before the clock ran. After the session, a container restart cut
the screen recording off without its index; the video was rebuilt from the raw data, and the recorder now
writes pieces that survive a sudden stop.

**Strategy failure (the real cause):** growing only from savings is far too slow. Tax income was again
about **$0.10 per person per year**, so a city of 2,500 earns ~$250 a year, enough for one small block
every year or two. Attempts 2, 4 and 6 showed that borrowing faster sinks the budget; attempt 7 showed
that not borrowing stalls growth. Neither works with what is known so far.

## What changes next time
Before attempt 8: research how SimCity 2000 really works (how dense homes grow, what drives land value
and tax income, what caps demand, how fast zones build) from guides and the game's own numbers, test the
key ideas in a lab city, and build attempt 8's strategy only from those findings.

Next: [research](../claudeville-3/research/README.md)
