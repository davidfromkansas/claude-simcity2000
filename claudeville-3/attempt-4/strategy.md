# Attempt 4 strategy (from the attempt 1–3 post-mortems)

Goal: 100,000 people by Jan 2050. Same flat map, Medium, disasters on, loans allowed.

## Combine what worked
- **Attempt 2's speed:** thin alternating bands (homes / shops / factories / shops / homes), a whole
  block built at once, the next block started before the current one is full.
- **Attempt 3's wiring:** un-zoned power columns next to every cross street, linked at both ends;
  pump fields as alternating rows of pumps and power lines; a north–south pipe main; check the save
  every January for unpowered or dry buildings (`bot/pmap.py`).
- **Separate taxes from day one:** homes 7–10%, shops 5–6%, factories 4–5% (set in the property-tax
  book). Factories react strongly to tax.

## New: survive disasters
- One fire station and one police station per block (about 30×35 tiles), built with the block.
- Cash reserve of at least $5,000 after year 5. Loans only for building that pays back (new blocks,
  plants); stop at about 6.
- If a fire starts: pause, dispatch firefighters to the front, bulldoze a firebreak if it spreads.

## Order of work
1. Day one: $10,000 bond, block 1 with power columns linked, coal plant, wired pumps, pipe main,
   neighbor link, fire station.
2. Every January: health check (power, water, unemployment, demand, newspaper, traffic, cash).
3. Each new block: roads, power columns + link, zones (jobs next to homes), pipes, fire + police.
4. From about 20,000 people: second neighbor link, schools/hospitals, rail if roads jam.
