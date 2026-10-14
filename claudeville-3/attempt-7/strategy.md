# Attempt 7 strategy (from the attempt 1–6 post-mortems)

Goal: 100,000 people by Jan 2050. Same flat map, Medium, disasters on, loans allowed.

## Main idea: a city that pays for itself
Attempts 2, 4 and 6 all died the same way: loans cost about $530 a year each, but the land they paid
for brought in only $200–300 a year in tax. So attempt 7 takes **no loans**. Everything is built from
cash, and building follows demand, never ahead of it.

## Rules
1. **No loans.** (If one is ever taken, it must be backed by a number showing it pays back within
   10 years.)
2. **Zone to demand.** Every check: add a zone type only while its demand is positive. Homes first,
   factories second, shops only while shop demand is positive. Target homes ≈ shops + factories.
3. **Dense zoning** for homes and shops: more people per tile of road. Roads are the biggest cost.
4. **Cheap growth order:** extend existing roads before starting new districts; reuse power columns.
5. **Water:** pumps right beside the river or lakes, in short wired rows.
6. **Taxes 7–8%** (homes up to 9% only while home demand stays at maximum). Gambling and parking on.
7. **Track income per person** every January (property tax ÷ population). If it is under $0.10,
   find out why (land value, pollution, abandonment) before building more.
8. Keep all controller checks: `step.sh` (audit + stall alarm), `build.py` plans checked tile by tile.

## Day one ($10,000)
- Neighbor link ($1,000), one coal plant on the river strip far from homes ($4,000).
- A small first block next to the river: dense homes, a factory band, a small shop band.
- Pumps beside the river, a pipe main, a fire station when cash allows.

## Later
- Seaport when factory demand stalls; second neighbor link; fire and police per block.
- Parks and schools as land value boosters once income allows.
