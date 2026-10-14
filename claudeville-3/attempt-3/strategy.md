# Attempt 3 strategy (from the attempt 1 and 2 post-mortems)

Goal: 100,000 people by Jan 2050. Same flat map, Medium, disasters on, loans allowed.

## Keep (it worked in attempt 2)
- Thin alternating bands so every home is next to jobs: HOMES, SHOPS, FACTORIES, SHOPS, HOMES, repeated.
- A $10,000 bond on day one, the whole first block built at once, tax 4% while small.
- Neighbor link on day one.

## Change
1. **Power that can't break.** Each block gets dedicated power-line columns right next to its cross
   streets, on land that is never zoned (buildings swallow lines drawn over zones). Every district gets
   its own coal plant at its edge. Every January: `bot/pmap.py` power map from the save; fix any dark
   area that year.
2. **Pumps wired correctly.** Pump fields are built as alternating rows: pumps, power line, pumps,
   power line. Check that every pump is powered.
3. **Traffic.** Cross streets every 8 tiles (not 10) and streets every 7 rows. From about 15,000 people,
   build rail with stations through the middle of each block (or subway if money allows), before any jam.
4. **Services on schedule.** Fire + police at 5,000 people; school + hospital at 10,000; one more of
   each per 10,000 people, spread across districts.
5. **Money.** At most 5 loans in total. Tax 7% from year 5, 8% if demand stays strong. Transit and
   services come before more zoning when cash is short.
6. **Check the game's own signals** every January: water and power spare capacity graphs, newspaper
   headline, demand bars, traffic map, unpowered and dry buildings.

## Layout (east of the river, x=76-126)
```
x=76 avenue | 77 power | 78-83 zones | 84 street | 85 power | 86-91 zones | 92 street | ...
streets every 7 rows (y=20, 27, 34, ...), bands of 6 rows between them
```
