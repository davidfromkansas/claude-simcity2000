# Claudeville 3 · Attempt 8 post-mortem

**Result: missed.** Stopped in February 2014 (game year 14) at **7,590 people** (peak 8,230), with 2
loans, $923 in cash and a loss of about $400 a year. The target curve called for 15,000 by 2010.
Abandoned at the user's request so the official manual could be read before attempt 9.

| Year | People | Cash | Loans | Unemployed |
|---|---|---|---|---|
| 2001 | 960 | $8,530 | 1 | 8% |
| 2003 | 2,440 | $7,891 | 1 | 5% |
| 2005 | 2,210 | $6,694 | 1 | 18% |
| 2008 | 3,440 | $4,924 | 1 | 3% |
| 2010 | 5,000 | $3,142 | 1 | 2% |
| 2012 | 7,140 | $6,426 | 2 | 3% |
| 2014 | 7,590 | $923 | 2 | 10% |

## What happened, phase by phase

**2000–2003: a checked start.** Day one used one plan: road **and rail** links, coal plant, 108 dense
home tiles, factories, shops and riverside pumps. All 475 tiles were confirmed before the clock ran.

**2004–2007: jobs and water.** Unemployment reached 17–22% while factory demand sat at maximum, because
factory land was full. A jobs block and three factory blocks fixed it. Water ran out twice; the build
check stopped a pump plan that put three pumps on water.

**2008–2013: loan #2 and a stall.** A north home block took the city to 5,000 by 2010. Loan #2 paid for
a south block (dense homes, shops, factories, fire station), plus the first marina and a second power
plant. Population reached 8,230 in 2013, then stalled: water short again, jobs short, and no cash.

## Control failures vs strategy failures

**Control failures:** none reached the game. Every build printed "BUILD: checked" and every step's
audit passed. The pre-build check caught a pump plan on water before anything was spent.

**Strategy failures:**
1. **Dense-only zoning grew slowly and cost twice as much.** Dense zones cost $10 a tile against $5,
   and on low land value they filled with small buildings. Attempt 2, with cheap light zoning, had
   10,000 people by 2004; attempt 8 had 2,200.
2. **Loan #2 did not pay back.** The south block added about 2,600 people, not the 5,500 needed. Two
   loans cost $1,000 a year against $707 of property tax.
3. **Water was always behind.** Three rounds of pumps; spare water was near 0% at most checks.
4. **Jobs and homes were never in balance.** The city swung between unemployment and home shortages
   because each block was sized by cash, not by demand.

## What changes next time
Read the official SimCity 2000 manual in full and build attempt 9's strategy from it, together with
what attempts 1–8 proved.

Next: [attempt 9 strategy](../claudeville-3/attempt-9/strategy.md)
