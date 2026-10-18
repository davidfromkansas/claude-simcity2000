# SimCity 2000 (1993): RCI demand, demand caps and what blocks zone growth

Primary sources used (full text read from archive.org OCR):
- MANUAL = Maxis, *SimCity 2000 User Manual* (1993) — https://archive.org/details/sc2000_manual
- PPP = Dargahi & Bremer, *SimCity 2000: Power, Politics, and Planning*, Revised Ed. (Prima). Chapter 16, "Inside the SimCity 2000 Model", was written with Maxis's designers and is the closest thing to official internals — https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised
- S&S = *SimCity 2000 Strategies and Secrets*, Special Edition (Sybex) — https://archive.org/details/SimCity_2000_Strategies_Secrets_SE
- Save-file reverse engineering: dfloer, SC2k-docs — https://github.com/dfloer/SC2k-docs/blob/master/sc2%20file%20spec.md
- Community FAQs (lower trust, marked where used).

Note: two well-known search results (somacon "SimCity 3000 FAQ" with "stadium raises cap by 125,000", "27,000 Sims") are for **SimCity 3000** and do NOT apply here. Micropolis/SimCity Classic cap rules (stadium/airport/seaport) also differ from SC2000.

## 1. How RCI demand is computed and capped

### Takeaway
Residential demand follows jobs (C+I), commercial demand follows population, and industrial demand follows the external national economy (set by difficulty) minus industry tax. On top of that are three caps: residential is capped at about **15,000 people** until you build stadiums/zoos/marinas; commerce is capped by trade capacity (airport or **road** connections to neighbours); industry is capped by trade capacity (seaport, **highway or rail** connections off the map). A negative C or I bar often means a missing cap-breaker, not too many zones.

### Cited Findings
- "Residential demand is driven by the presence of commerce and industry, because you need someplace for the workers to live." "Commercial demand is driven by the overall population size." "Industrial demand is driven by the external national model... because you need to sell the bulk of your industrial goods to consumers outside your city." "In general, the residential demand will equal the sum of the industrial and commercial demands." — [PPP ch.16 p.398](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- "Initially there is an industry-to-commerce ratio of 3:1. As the city grows and the population nears 100,000, the ratio approaches 1:1. Beyond that, commercial demand continues to grow and outstrips industry." — [PPP p.398](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- "No matter the demand, there are three major limits on city growth: no growth without power; no growth without transportation; growth is severely limited unless there is a water system." — [PPP p.398](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- **Residential cap:** "Residential growth hits a cap at a population of about 15,000. At this point, you need some entertainment centers, such as stadiums and zoos and marinas, before the residential population will break through that cap. Up to a point, the more you build, the more population you can get." — [PPP p.399](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Stadium/zoo/marina location does not matter: "As with zoos, the location of the stadium does not matter. Stadiums give a big boost to the growth of residential" zones; "it is the presence of a stadium, marina, or zoo, not where it is located." — [PPP ch.?, recreation section](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised). Manual: "Marinas, zoos and stadiums are a big boost for residential growth." Stadium costs $3,000 per stadium; marina $1,000. — [MANUAL p.110 & tool reference](https://archive.org/details/sc2000_manual)
- **Commerce cap:** "The commerce cap is broken by the presence of airports or roads off the edge of the city to reach your neighbors... If you don't have enough commercial transportation, the Sims will let you know, and you'll have to either enlarge your airport or add roads to your neighbors." — [PPP p.399](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- **Industry cap:** "The industry cap is broken by the presence of seaports, highways, or rail connections off the edge of the city... The amount of industrial trade capacity required is based on the amount of industry in your city—the more industry, the more capacity you need. When you don't have enough, the Sims will raise a stink (by sending out an Industry Needs a Seaport message)... This message can flash by quickly and be easily missed, so if you notice your industry lagging behind the other two zones and unemployment rising, add more industrial carrying capacity. If you don't have a river or coastline, a seaport is useless." — [PPP p.399](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Equivalence: "the cost of running a road, rail, or highway off the edge of the city is roughly equivalent to an airport or seaport of equal carrying capacity." Spreading connections over several edges makes no difference to *your* capacity, but "If they are well-connected, they [neighbours] will grow faster, and their growth will feed back into the national model, which will grow faster and create more industrial demand for your city." — [PPP p.399-400](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Contradiction on duplicates: the same book's tool chapter says "It does not help commerce in your city to build multiple road connections to the same neighboring city off the same edge of the map. You will, however, need to build a highway or railroad connection to allow your industry to trade." Status messages: "Commerce demands a connection" → build a **road** connection; "Industry demands a connection" → build a **highway (or rail)** connection, "not a road connection". — [PPP ch.2, pp.~60-70](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Connection cost: "$1,000 for a road or highway, or $1,500 for a rail line." "You cannot build a subway connection to your neighbors. If you build an airport or seaport... this does not preclude the need for road or rail connections." — [S&S pp.167-168](https://archive.org/details/SimCity_2000_Strategies_Secrets_SE); subways "can't make connections to neighboring cities (and therefore don't affect industrial carrying capacity)" — [PPP p.402](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Airport timing: "Airports provide a big boost to your city's commerce once your city reaches a population of at least 20,000." Airport $250/tile, seaport $150/tile; ports must be powered; seaports must be on a river or ocean. "If you notice your commercial or industrial zones' growth rate slowing down, you may want to add ports before your Sims ask for them." — [MANUAL pp.101,108-109 & Ports tool](https://archive.org/details/sc2000_manual)
- Demand bar is a rough gauge: "if the Demand Indicator shows a negative demand for commerce and industry, it may be caused by the lack of an airport or seaport and not have anything to do with whether or not you have a surplus of industrial and commercial zones... you should have R = C + I" (zone populations, Graphs window). — [PPP p.37 footnote 17](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Lag: "Depending on the size of your city, the indicator can take up to a few minutes to respond to your changes, so be patient." — [MANUAL, Demand Indicator](https://archive.org/details/sc2000_manual); "Don't try to follow its results with knee-jerk reactions, because there is some time delay." — [PPP p.113](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Difficulty: Medium starts with $10,000; "In medium games, the national economy is stable" (easy = boom, hard = recession); "The easier the game, the more demand for the products that your city's industries can produce." — [MANUAL p.~96](https://archive.org/details/sc2000_manual)
- Industrial model: industry mix driven by "external demand for industries, tax rates, current ratios of existing industries"; "If you've got a zillion automobile plants, you might satiate the national demand." — [PPP p.413](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Commerce role: "Commerce remains a much less important aspect of a city until it reaches a population of about 100,000, where income from commerce catches up with industry." "Commercial zones develop better and faster near the city center." — [MANUAL pp.100-101](https://archive.org/details/sc2000_manual)
- Taxes: default 7%, range 0-20%, per-zone rates settable. "Sims reach the limit of their tolerance at about 9%." Very low tax brings "transient and unstable" Sims "with exceptional crime rates". — [S&S p.129](https://archive.org/details/SimCity_2000_Strategies_Secrets_SE). Community: "If your tax rate is around 9% or over, you should see depressed demand rates"; 7-8% gives better growth — [Zen and the Art of SC2000](https://ibiblio.org/GameBytes/issue18/misc/zen.html). Forum (unverified): "the RCI demand bars take into account the tax rates, although it will take at least a few months after you change a tax rate" — [GOG forum](https://www.gog.com/forum/simcity_series/sim_city_2000_rci_demands)
- Ordinances affecting demand: 1% Sales Tax "may also inhibit local commerce"; 1% Income Tax "may discourage residential growth"; Parking Fines "hinder commercial growth a little"; Business Advertising "can bring new industry"; City Beautification "increases residential desirability"; Nuclear Free Zone small + residential, small − industry; Annual Carnival boosts local commerce. — [MANUAL pp.89-91](https://archive.org/details/sc2000_manual)
- Save file: RCI demand stored at MISC 0x0718-0x0720 as "Signed 32b int from -2000 to +2000. First R, second C, third I"; 0x1024 "Connection Tiles... count of tiles that are connected to neighbours"; 0x1028 "Sports Teams: count of active sports teams from stadiums"; 0x06D8 neighbour data (index, population, value, fame). — [dfloer SC2k-docs](https://github.com/dfloer/SC2k-docs/blob/master/sc2%20file%20spec.md)
- Unemployment: "A healthy, vibrant economy should have an unemployment rate of less than seven percent." It "is based on the number that can't find work in your commercial zones and industrial zones." — [PPP p.~140](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)

### Inferences
- Our pattern "I demand at max while factories abandoned" fits the model: I demand reflects external market, but individual factories still die if their trips fail, they lack power/water, or the industry trade cap (no highway/rail connection or seaport) is hit. A **road** link only lifts the *commerce* cap; on a landlocked flat map, industry needs a **highway or rail** connection to the edge ($1,000 / $1,500).
- "C negative most of the game" is expected in a small city (I:C 3:1 early) and also signals the commerce cap (needs road link / airport after 20k).
- For 100,000 people, a stadium/zoo/marina is mandatory well before 15,000 residents; several more will probably be needed ("the more you build, the more population you can get"). Cheap check: MISC 0x1028 sports team count.
- Read MISC 0x0718 directly instead of the screenshot bars; watch for the flashed "Industry needs..."/"Commerce demands a connection" status messages.

### Gaps
- Exact demand formula and numeric trade-capacity per connection/port tile not published; no reverse-engineered code found.
- Size of the residential cap increment per stadium/zoo/marina unknown ("up to a point").

## 2. Recommended R:C:I land ratios by city size

### Takeaway
Residential tiles ≈ commercial + industrial tiles at all sizes. C:I goes from ~1:3 (small city) to 1:1 at ~100,000, then commerce > industry.

### Cited Findings
- "You need a good balance of the three basic zones, with the number of tiles zoned residential approximately equal to the total tiles zoned commercial and industrial. In a small city, you'll need more industrial than commercial. You'll need equal numbers of each at a population of about 100,000. Above that, lean more towards commercial." — [MANUAL p.119](https://archive.org/details/sc2000_manual)
- Same rule, "Residential zone tiles = Commercial zone tiles + Industrial zone tiles"; Table 2-20 gives I:C by population (first row "20,000 and less"; rest of table illegible in OCR). — [PPP p.113](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Community table (1996, garbled bracket labels as published): R:C:I = 4:1:3 (small, ~<10,000), 4:2:2 (10,000-60,000), 4:3:1 (>60,000); "R = C + I". — [somacon SC2000 tips](https://www.somacon.com/p606.php) (note: the page literally prints "Over 10,000 → 4:1:3" and "Under 60,000 → 4:3:1", evidently a typo; also its 4:3:1 at 60k conflicts with the manual's 1:1 at 100k).

### Inferences
- For a 100k target: early 4:1:3, around 50-100k move toward 2:1:1.

### Gaps
- Exact Table 2-20 values not legible.

## 3. Development speed and what blocks development

### Takeaway
A zone tile develops only if: powered (power reaches it through lines or powered buildings — never through empty zone), within 3 tiles (orthogonal) of road/rail station/subway station, and its trips to both other zone types succeed within 100 "steps" (~33 road tiles). Water is needed for density; land value, pollution, and crime decide what grows. No published per-month development rate exists.

### Cited Findings
- Road distance: "Sims won't build buildings that are more than three tiles from a road (or other transportation system), so... the largest area that will fully develop is a 6 x 6 square surrounded by road." — [MANUAL p.105](https://archive.org/details/sc2000_manual). "within 3 tiles (not counting diagonals)" — [Iconbar SC2000 FAQ](https://www.iconbar.com/Sim_City_2000_FAQ/news1022.html)
- **Trip generation algorithm** (PPP pp.400-401): starts at a zoned tile, heads in one direction looking for road, subway station or rail station ("but not tracks without a station"); "If it doesn't find it in three tiles or less, it will go back... If after trying four directions it still can't find what it's looking for, the trip is a failure." Trips from each building must reach **both** other zone types (R→C, R→I, C→R, C→I, I→R, I→C). "If the trip is successful within the limits, the building has the opportunity to develop. If the trip is not successful, the building will stagnate or decay." — [PPP](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- **Trip limit numbers:** "The actual time and distance limits of a trip amount to 100 steps... Cars on roads take three steps per tile. Cars on highways take one step per tile. Buses on roads take two steps per tile. Buses on highways take one step per tile. Rails and subways take one step per tile. There is also a four-step trip charge to use a station." → ~33 road tiles, ~50 by bus, ~96 by rail/subway/highway. — [PPP p.401](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised); manual: highways/rail/subway let trips go "up to three times as far" — [MANUAL pp.106-107](https://archive.org/details/sc2000_manual)
- "Trips prefer to follow the non-diagonal roads." Trips only transfer between modes "if their access points are adjacent." A trip succeeds if it reaches the zone type "whether or not the zone is developed." — [PPP p.401](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- **Map edge counts as all zone types**: "the model assumes that all types of zones are accessible just beyond the edges of the city. If you run roads, highways, or rails off the edge, any nearby zone will have successful trips to neighboring cities." — [PPP p.403](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- "One of the main things that keep cities from developing is that the different zones are too far away from each other and the simulated trips fail. You have to mix your three zone types." — [PPP p.403](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Traffic: ≤44 cars/min "no traffic", 44-88 light, above heavy; trips "try to avoid heavy traffic areas". — [MANUAL pp.106-107](https://archive.org/details/sc2000_manual)
- **Power:** "All zones need power to develop." "Power isn't transferred through adjacent zones or through roads or rails that divide zones without power lines." — [MANUAL p.102](https://archive.org/details/sc2000_manual). "It will not travel through an undeveloped area of a zone. Placing lots of power lines throughout an undeveloped zone... will help it grow faster." When available power reaches zero, remaining buildings "will be unpowered and decay." Power lines have no upkeep. — [PPP p.407-408](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised). Manual: ~1 MW per 3 occupied tiles. Energy Conservation ordinance: up to 15% more buildings per plant. — [MANUAL pp.91,103](https://archive.org/details/sc2000_manual)
- **Water:** "You can build a city without any water system at all, but the population won't grow very dense." — [MANUAL p.110](https://archive.org/details/sc2000_manual); "Growth is severely limited unless there is a water system." — [PPP p.398](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised). Forum (unverified): "Lack of water can also cause black/abandoned buildings even with high demand... once the water supply is restored then the buildings will be rebuilt." — [GOG forum](https://www.gog.com/forum/simcity_series/sim_city_2000_rci_demands)
- **Building sizes:** light zones only 1x1; dense zones grow 1x1 → 2x2 (two densities) → 3x3 "if all the other conditions are met". — [PPP p.398](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised). Community: 3x3 needs "at least 3 roads on one side and 1 road on another side", high land value, positive demand, other zones within ~10-15 tiles; densities ≈10 people/tile small, 20/tile low 2x2 (80/bldg), 30/tile high 2x2 (120/bldg), 40/tile 3x3 (360/bldg) — [somacon](https://www.somacon.com/p606.php) (unverified). "3x3 buildings need the zone to sit next to an intersection" and mass transit alone gives slower growth with no 3x3 — [Iconbar FAQ](https://www.iconbar.com/Sim_City_2000_FAQ/news1022.html) (unverified). Rail/subway: "Sims will develop within 3 squares of rail or subway too, but growth will be much slower" — [Zen](https://ibiblio.org/GameBytes/issue18/misc/zen.html)
- Known bug: model "prevents high land values from being associated with low-density zones, and low land values from being associated with high-density zones." — [PPP p.113 fn](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- **Land value** rises with proximity to city center (more so in bigger cities), trees/water/parks, hills; falls with pollution and crime. Small park ≈ trees; big park = 2× small park. — [PPP p.403-404](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised); [MANUAL p.110](https://archive.org/details/sc2000_manual)
- **Pollution**: from cars (largest), industry, power plants, ports, military; residential and commercial zones produce none. Pollution lowers land value → raises crime. — [PPP p.404](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised); [MANUAL p.111](https://archive.org/details/sc2000_manual)
- **Crime**: "breeds and spreads in areas of low land value and high population density"; police max radius "about 14 tiles", five bands; must be powered; prison holds 10,000, releases 25%/yr. "High crime destroys land value, chasing out some of your population." — [PPP pp.404-407](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised); [MANUAL p.119](https://archive.org/details/sc2000_manual)

### Inferences
- With 3 steps per road tile and a 100-step budget, any home farther than ~30 road tiles from both a shop zone and a factory zone (or the map edge on a connected road/highway) fails trips. Mixed thin bands, as in our CLAUDE.md, are correct; a road off the map edge near each district makes trips succeed for all three types.
- Residential at max but no growth once land fills: likely the 15,000 residential cap (no stadium/zoo/marina), the commerce/industry trade caps, or simply no more zoned land; also water shortage blocks density.

### Gaps
- No source gives tiles-per-month growth rates. The manual only says demand "can take up to a few minutes" of real time to respond.
- Exact water rule (whether unwatered zones are capped at some building size) not stated numerically in primary sources.

## 4. Abandonment: causes and reversal

### Takeaway
Buildings are abandoned when Sims "found something not to their liking": failed trips, no power (brownouts), no water, high crime, negative demand, overzoning. Abandonment is temporary if demand stays up and the cause is fixed; Sims rebuild over abandoned buildings and rubble, except disaster rubble which must be bulldozed.

### Cited Findings
- "buildings appear, sometimes disappear, and then are replaced by dark, abandoned buildings... the Sims have moved in, found something not to their liking, and moved out... provide access to jobs, transportation, power, water, convenient shopping, good education, police and fire protection, and recreational facilities." — [PPP ch.1](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Brownouts: if not fixed "Sims will move out in droves and that area will become abandoned." Crime: Sims "will simply move away from the troubled area... leaving large residential areas abandoned." — [S&S](https://archive.org/details/SimCity_2000_Strategies_Secrets_SE)
- Failed trips: "the building will stagnate or decay." — [PPP p.400](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- "When the bar drops down into the negative side the zones are downsized or abandoned." "The abandoned buildings are a temporary problem if the demand indicator stays up." Over-zoning commercial in small cities causes abandonment. — [Zen](https://ibiblio.org/GameBytes/issue18/misc/zen.html)
- "Sims build over abandoned buildings and rubble, so bulldozing is optional"; abandoned buildings lower property values. — [Iconbar FAQ](https://www.iconbar.com/Sim_City_2000_FAQ/news1022.html). But after a disaster "you must manually bulldoze the rubble in Demolish/Clear mode before the zone will begin to rebuild." — [MANUAL p.121](https://archive.org/details/sc2000_manual)
- Abandoned buildings still transmit power (forum, unverified) — [GOG forum](https://www.gog.com/forum/simcity_series/sim_city_2000_rci_demands)

### Inferences
- Abandoned factories with I demand at max → check trip success (C and R within ~33 road tiles), industrial trade cap (highway/rail link), power/water, and pollution-driven land value.

### Gaps
- No numeric timing for abandonment/recovery.

## 5. Mass transit and highways

### Takeaway
Highways, rail, subway cost 1 step/tile vs 3 for road, so they triple trip reach; buses (2 steps/tile on roads) are used about twice as often as rail. Transit only helps if it links different zone types; failed transit trips are not retried.

### Cited Findings
- "If it bumps into mass transit, there is a 50/50 chance it will take it." "If a failed trip involves mass transit, then the next time that same building is checked, it won't even try that same type of mass transit." "A bad mass transit system is worse than none at all." Put depots near busy intersections; lines must pass through different zone types. — [MANUAL pp.107-108](https://archive.org/details/sc2000_manual)
- Bus depot max effect radius "about 10 tiles"; "about twice as many Sims will take a bus as will take subways or rails"; rail/subway need ≥2 stations, "A rail-only series of trips from one zone to the two destination zones requires three stations." — [PPP p.402](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Highways carry twice a road; need on-ramps and roads; "Sims will commute farther on a highway... up to three times as far." Availability ±10 yrs: subway 1910, bus 1920, highway 1930. Rail is "a big boost to heavy industry". — [MANUAL pp.106-107](https://archive.org/details/sc2000_manual)
- Costs (FAQ): rail $25/tile, rail depot $500, subway $100/tile, subway station $250, bus depot $250 ($25/yr). — [Iconbar FAQ](https://www.iconbar.com/Sim_City_2000_FAQ/news1022.html)

### Inferences
- In 2000+ all transit is available. A highway ring with on-ramps plus a highway off the map edge would both triple trip reach and lift the industry cap.

### Gaps
- None major.

## 6. Education and health

### Takeaway
EQ mainly sets which industries come (high-tech boosted above EQ 100, aerospace/electronics boosted above 130, curtailed below 80); low EQ raises unemployment and riot risk. Hospitals raise LE which makes schools more effective.

### Cited Findings
- Immigrants arrive with EQ ~85 and LE 59-65. Newborn EQ = working-age average ÷ 5; schools add 35 points in each of ages 5-10 and 10-15; college multiplies by 1.5. School capacity 1,500 students ≈ 15,000 population; college 5,000 students ≈ 50,000 population; libraries serve 20,000, museums 40,000. — [PPP pp.410-412](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- "high-tech industries will grow slowly even with a low EQ, but they receive a growth boost if your city's average EQ for working-age Sims is above 100... You can maintain this level with colleges for about half the population." Aerospace/electronics: boost at 100 and again >130, "curtailment if your EQ is below 80." "In spite of what the manual says, hospitals do not help the petrochemical industry." — [PPP p.414](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- With no schools, children get "about 20% of their parents' EQ"; "A city with a low EQ has a higher likelihood of both unemployment and rioting." — [MANUAL p.114](https://archive.org/details/sc2000_manual)
- Hospital serves 25,000; without hospitals LE declines to ~35; enough funded hospitals → 85. — [MANUAL p.116](https://archive.org/details/sc2000_manual). Short lives raise the child share, making schools less effective. — [PPP p.412](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Educational buildings raise land value and need no road access. — [Iconbar FAQ](https://www.iconbar.com/Sim_City_2000_FAQ/news1022.html); [MANUAL p.115](https://archive.org/details/sc2000_manual)
- Community: schools/hospitals at ~25% funding can keep an "A" grade early — [Zen](https://ibiblio.org/GameBytes/issue18/misc/zen.html) (unverified).

### Inferences
- For 100k: ~7 schools, 2 colleges, 4 hospitals at full coverage; EQ is not a direct growth cap but steers industry type and pollution.

### Gaps
- No source says EQ/LE directly enters the RCI demand formula.

## 7. Disasters (Medium) and protection

### Takeaway
On Medium disasters are random but less frequent than Hard ("the harder the game, the more likely"). Fire is the worst: stop fires first. Riots come from heat, crime, unemployment and long blackouts.

### Cited Findings
- "The propensity for disaster. The harder the game, the more likely is it that your city will be host to a disaster." — [MANUAL p.~96](https://archive.org/details/sc2000_manual)
- Fires likelier in hot dry weather and without fire coverage; fire stations raise land value. Riots: "heat, high crime and unemployment... or a long blackout." Floods only hit sea-level tiles; raise terrain one level as dikes. Earthquakes/tornadoes cannot be prevented. Rubble must be bulldozed before rebuild. — [MANUAL pp.120-123](https://archive.org/details/sc2000_manual)
- "Fires in SimCity 2000 are really mean... fires had to be allowed to spread very fast." Firebreaks: bulldoze (rubble burns), De-zone mode removes rubble in zones. Refusing the military base at 60,000 → "in one disaster out of four, Captain Hero will appear". Earthquake/monster: "no particular conditions, no warning." Too many clustered arcologies → chemical spill. — [PPP ch.12 pp.282-290](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- With disasters ON, power plants that reach 50 years collapse and must be rebuilt (with No Disasters they auto-rebuild). — [MANUAL p.103](https://archive.org/details/sc2000_manual)
- Max 33 emergency units dispatchable. — [Iconbar FAQ](https://www.iconbar.com/Sim_City_2000_FAQ/news1022.html)

### Inferences
- Plant built in 2000 collapses around 2050, at the end of our window: not an issue before Jan 2050 unless the plant was older.
- Keep fire stations spread, keep cash for rebuild, keep unemployment <7% and crime low to limit riots.

### Gaps
- No numeric disaster probabilities per difficulty found.
