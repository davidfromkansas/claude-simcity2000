# SimCity 2000 official manual: notes for Claudeville 3

Source: the Maxis *SimCity 2000 User Manual* by Michael Bremer (full text read cover to cover from
[archive.org](https://archive.org/details/SimCity.2000-Manual); raw text in `manual/manual.txt`).
Page numbers are the manual's. "Research" means our earlier report (`README.md`).

## Chapters read
Introduction (p.1-4) · Tutorial 1 Basics (p.10-24) · Tutorial 2 Landscape (p.25-32) · Tutorial 3
Advanced (p.33-44) · Reference: basics, menus, City window and toolbar (p.46-77) · Map window (p.78-81)
· Budget window (p.81-89) · Ordinances (p.89-92) · Population, Industries, Graphs, Neighbors windows
(p.92-96) · Inside the Simulation (p.97-118) · Strategies and disasters (p.119-124) · Gallery (p.125-135)
· Appendix (p.136-138).

## The manual's own strategy (p.119-120) - the most important page
- **Stay small at first and go easy on infrastructure. Keep costs down; get out of the red and into the
  black as soon as possible. Show patience and build a good reserve of funds.**
- **Modular approach:** design one small, compact neighborhood with all zones, transport and services
  that runs efficiently, *or better at a profit*, then copy it, sharing costly items (schools, plants).
- To grow population as large as possible: zone densely, keep crime under control, read the papers.
- Avoid large densely concentrated areas: density brings pollution and crime.
- Keep police well funded; high crime destroys land value and tax income. Fire funding can be trimmed.
- Keep land values high for property taxes; also zone some low-cost housing.
- **Zone balance: residential tiles ≈ commercial + industrial tiles. Small city: more industrial than
  commercial; equal at ~100,000; above that more commercial.** Add zones the demand bars ask for.
- Replace power plants every 50 years; big plants are cheaper per MW only if the city needs the power.

## Growth rules
- A city needs only: homes, jobs (factories), shops, power plant, power lines, roads (p.8).
- **Industry is the lifeblood of a small city**: too few customers inside, so it sells to the external
  market and brings in cash and people (p.101). Commerce is mostly internal and slow in a small city;
  it catches up with industry around 100,000 (p.100).
- **Commercial zones develop better and faster near the city centre** (p.101).
- Seaports or their lack help/hinder heavy industry (steel, mining, automotive); so do highways and rail
  (p.102). Rail is "a big boost to heavy industry" (p.107). Airport: big boost to commerce from 20,000 (p.101).
- **Marinas, zoos and stadiums are a big boost for residential growth** (p.111). (Confirms research.)
- **Sims build only within 3 tiles of a road (or other transport): the largest area that fully develops
  is a 6x6 square surrounded by road** (p.105).
- If nobody moves in: zones unpowered, or homes and factories too far apart - "Sims hate to commute
  very far" (p.18).
- External demand grows with time; Medium = stable national economy (p.97).
- Trip generation (p.107-108): every building tries a trip to both other zone types within a time
  limit; highways, rail and subways go up to 3x farther; a failed trip makes it decline. Mass transit
  is taken 50/50; depots near busy intersections and lines through different zone types. Rails need
  at least two depots, buses at least two depots on roads.
- Ports: start small, leave room to expand; add before the Sims ask if C/I growth slows (p.109).

## Power and water
- **Power does not pass through empty zones, roads or rails without lines**; it passes building to
  building into adjacent zones once built (p.102, p.134). (Confirms our attempt-5 lesson.)
- **Every power-line tile consumes power: too many lines waste power** (p.102).
- ~1 MW per 3 occupied tiles (p.103). Coal 200 MW $4,000 (worst polluter); oil 220 MW $6,600 (half
  coal's pollution); gas 50 MW $2,000; nuclear 500 MW $15,000; microwave 2020, 1,600 MW $28,000.
  Plants collapse after 50 years.
- **Water: needed before population can grow dense** (p.4, 62, 110). **A pump right next to fresh
  water (lake/river) gives about 3x a well on dry land** (p.110; p.62 says 2x). Pumps need power.
  Water towers ($250) store water for dry months; treatment plant ($500) recycles.

## Money
- Property tax 0-20%, main income; separate R/C/I rates in the tax books (p.82).
- **Ordinances** (tutorial city example): 1% income tax +$360, 1% sales tax +$196, parking fines +$180,
  legalized gambling +$98 a year; downsides: income tax discourages residents, sales tax and parking
  fines slightly hinder commerce, gambling adds crime (p.43, 89-90). City Beautification raises land value.
  Energy Conservation lets plants power up to 15% more buildings after a few years.
- **Bonds**: $10,000 each; interest = prime + 1% + a rating premium; paid yearly; repay oldest first;
  "once you're flush with cash, pay them off" (p.83-84). Loan rating AAA-F from city value.
- Running costs: police $100/yr, fire $100, hospital $75, school $25, college $100; roads $1/10 tiles,
  rails $1/5, highways $1/section, subways/bridges/tunnels $2/5 tiles (p.85-88).
- Build costs (p.59-70): bulldoze $1/tile; trees $3/click; water $100/tile; power line $2/tile ($10 over
  water); pipe $3; pump $100; tower $250; road $10/tile; highway $100/section; onramp $25; bus depot $250;
  rail $25/tile; rail depot $500; subway $100/tile; station $250; light zones $5/tile, dense $10/tile;
  seaport $150/tile, airport $250/tile; police/fire/hospital $500, prison $3,000; school $250, college
  $1,000, library $500; small park $20, big park $150, zoo $3,000, stadium $5,000, marina $1,000.
- **Roads, depots, stations and city buildings de-zone land they are placed on: leave gaps for them
  instead of zoning over them, to save zoning money** (p.100).

## Land value
Raised by: trees and forests, water (lakes, rivers), small parks (≈ trees), big parks (2x), all
education buildings, police stations (radius), fire stations, City Beautification, homeless shelters.
Lowered by: crime, pollution (cars first, then industry, then some plants), industrial areas (p.101,
109-115).

## Services
- Schools serve ~15,000 people each; colleges ~50,000; hospitals 25,000. No schools: children get 20% of
  parents' EQ. High EQ attracts high-tech industry; low EQ raises unemployment and riots (p.114-115).
- Police lower crime and raise land value near the station; jails fill as crime rises, then a prison
  helps (p.115).
- Riots: heat, high crime, unemployment, long blackouts (p.122). After any disaster, rubble must be
  bulldozed before zones rebuild (p.121).

## Rewards and milestones (p.112)
2,000 mayor's house · 10,000 city hall · 30,000 statue · 60,000 military base offer · 120,000 arcologies
(Plymouth from 2000). No shortcut to 100,000.

## What this changes for attempt 9 (vs. research and attempts 1-8)
1. **Profit first, then copy.** Every attempt built bigger than income could carry. The manual's
   order is the reverse: a small module that runs at a profit, then repeat it.
2. **Industry-led start.** Small cities live on industry selling outside; rail link and seaport lift it.
   Shops only near the centre and only as demand asks.
3. **Light zoning to start, dense later.** Dense pays only with water and land value; early on it cost
   us double for slower growth (attempt 8).
4. **Fewer power lines.** Every line tile uses power; power flows through built buildings, so one line
   per zone band is enough.
5. **Pumps only on the riverbank** (2-3x output).
6. **Money tools:** parking fines and sales tax are larger than gambling; 1% income tax is the largest
   but slows home growth (use only when demand for homes is strong).
