# Claudeville 4 · Attempt 11 strategy (from claudeville-4/reflection.md)

Goal: 200,000 by Jan 2050, same map, Medium, disasters on.

## What ten attempts show
- Fire is solved (attempt 10: one fire, out in two bursts). Debt ended 5 of 10 cities; only low-debt attempt 6
  (27 loans, 120,770) stayed healthy. The land holds ~110-120k; 200,000 needs arcologies (unlock at 120,000).

## Plan
1. **Opening**: attempt 10's build order (its plans, in the same order) - the fastest to 100,000.
2. **Money from day one**: ordinances enacted in Jan 2000 (`bot/ordinances.sh`); loans through loan.sh with a
   **4,000 people-per-loan floor from 30,000 people** (run.json `loan_floor`); target <= 30 loans at 120,000.
3. **Taxes**: controller 7-9%. Never raise taxes while demand is negative or unemployment is rising.
4. **Budget**: transit and fire funding stay at 100%.
5. **Fire rules** unchanged: stations per ~6,000 people, every disaster -> pause, dispatch firefighters, watched
   bursts with disaster.sh, rebuild onto rubble, powerfix.
6. **At 120,000**: open the arcology tool at once, record price/size/population, then save cash and build them.
7. Journal every January during play (attempt 10 missed it).
