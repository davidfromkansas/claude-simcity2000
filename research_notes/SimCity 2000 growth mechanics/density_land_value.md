# SimCity 2000 (1993 DOS/Win/Mac) — residential density and land value

Scope: SimCity 2000 classic only. Anything from SimCity (1989)/Micropolis, the SNES port, or SimCity 3000/4 is marked as such.
Source quality: no published, reverse-engineered land-value or building-population formula for SC2K turned up. The
dfloer/SC2k-docs simulation spec has nothing on it. The best sources are (1) the original Maxis manual by Michael Bremer.
Its English text on archive.org is lending-restricted (HTTP 401), but the official Italian translation is fully readable.
(2) Fan pages from 1995-96. Quotes from the Italian manual are translated by me; the original Italian is given where the
wording matters.

Key URLs
- Italian manual (official translation of Bremer's SC2K user manual, Maxis 1993, C.T.O. edition May 1994), full text: https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt (item: https://archive.org/details/manualzilla-id-6163847)
- English manual (restricted, not readable): https://archive.org/details/simcity2000ultim00brem
- 1996 fan page "Simcity 2000 Tips and Tricks": http://www.somacon.com/p606.php
- Michael Weburg zoning guide (patcoston.com, created 1995): https://patcoston.com/co/handzone.aspx
- dfloer SC2k-docs file spec: https://raw.githubusercontent.com/dfloer/SC2k-docs/master/sc2%20file%20spec.md ; simulation spec: https://raw.githubusercontent.com/dfloer/SC2k-docs/master/simulation%20spec.md

## Q1. People per residential building/tile, building sizes, largest buildings

### Takeaway
SC2K residential buildings come in 1x1, 2x2 and 3x3 sizes. The only numeric per-building figures found come from one 1996
fan page: 1x1 = 10 people/tile, 2x2 = 20 or 30/tile (80 or 120 per building), 3x3 = 40/tile (360 per building). No
primary source (manual, decompilation) confirms these numbers. Treat them as unverified folklore that fits other sources.
The largest "residential" structures are arcologies (30,000-65,000 each), which unlock only at 120,000 population, so they
cannot help reach 100,000.

### Cited Findings
- Building sizes and per-tile counts (fan page, "This page is from 1996!"): "the zoned buildings come in 3 sizes: 1X1(small), 2X2(medium), 3X3(large). Small buildings contain 10 people per tile. Medium buildings have two distinctions. Low density contain 20 people per tile. (80 people per building) High density contain 30 people per tile. (120 people per building) Large buildings contain 40 people per tile. (360 people per building)" — [somacon 1996 tips](http://www.somacon.com/p606.php)
- Same page: "To attain the highest density, you will want to promote the construction of the large buildings." — [somacon](http://www.somacon.com/p606.php)
- ludo.guide (modern guide; its source is not stated): Light Residential "can support a maximum of 10 Sims" per acre (acre = tile) and "exclusively supports single-acre homes", and "Depending on the land value, this zoning can result in tracts of lower-class homes or expansive acres of mansions." — [ludo.guide light residential](https://www.ludo.guide/guide/simcity-2000/light-residential)
- ludo.guide: Dense Residential is "approximately 40 Sims per acre", $10/tile. It develops from "small single-acre homes" to "larger apartments and tenement buildings" to "very large condos and apartments". "2x2 churches" appear inside the zones and add no population. — [ludo.guide dense residential](https://www.ludo.guide/guide/simcity-2000/dense-residential)
- Residential building IDs in the save (XBLD), from the reverse-engineered file spec (it gives no population numbers):
  - 1x1: 0x70-0x73 Lower-class homes, 0x74-0x77 Middle-class homes, 0x78-0x7B Luxury Homes.
  - 2x2: 0x8C Cheap apartments, 0x8D-0x8E Apartments, 0x8F-0x90 Nice Apartments, 0x91-0x93 Condominium.
  - 3x3: 0xAE-0xAF Large apartment building, 0xB0-0xB1 Condominium (Large Condominiums).
  — [dfloer sc2 file spec](https://raw.githubusercontent.com/dfloer/SC2k-docs/master/sc2%20file%20spec.md)
- Zone types (fan description): "Low density: only single-family homes. High density: homes plus high-rise apartments and condominiums." — [patcoston objdef](https://patcoston.com/co/objdef.aspx)
- Zone cost (manual, IT): "Costo: Area Residenziale 5 per tassello, Area alta densità 10 per tassello" (light $5/tile, dense $10/tile). — [Italian manual](https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt)
- The manual says residential zones "Comprendono sia case di lusso che i bassifondi" (they contain both luxury homes and slums). — [Italian manual](https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt)
- Arcologies (fan figures): Plymouth Arco $100,000, up to 55,000. Forest Arco $120,000, up to 30,000. DARCO $150,000, up to 45,000. Launch Arco $200,000, 65,000. — [patcoston objdef](https://patcoston.com/co/objdef.aspx). Giant Bomb gives Launch Arco 60,000 instead (conflict). — [Giant Bomb](https://www.giantbomb.com/games/3030-13760/)
- Manual: arcologies arrive "quando arrivate ai 120.000 abitanti" (at 120,000 inhabitants), designed in 2000/2050/2100/2150. They also "stimolano anche la crescita delle zone residenziali, commerciali ed industriali confinanti" (stimulate growth of adjacent R/C/I zones). — [Italian manual](https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt)
- Churches: the sim builds one every 2,500 sims, replacing an existing 2x2 residential building. An earlier note in the same spec says every 5,000 without arcos (the spec contradicts itself). — [dfloer simulation spec](https://raw.githubusercontent.com/dfloer/SC2k-docs/master/simulation%20spec.md)
- Save fields useful for checking: MISC 0x0074 "Residential population" ("Unknown exactly"), 0x05F8 Residential Tile Count, 0x102C Normal Population (non-arco). XPOP is a 32x32 overlay (population density map). — [dfloer sc2 file spec](https://raw.githubusercontent.com/dfloer/SC2k-docs/master/sc2%20file%20spec.md)

### Inferences
- Planning arithmetic, using the unverified fan numbers: 100,000 residents needs about 2,500 residential tiles if every tile
  held a 3x3 building at 40/tile, about 3,300 tiles at 30/tile (dense 2x2), or 10,000 tiles of 1x1 at 10/tile. A light-zone
  city basically cannot reach 100k on a normal map. The dense-zone mix that is realistic in practice (part 1x1, part 2x2,
  part 3x3) suggests budgeting about 4,000-5,000 dense residential tiles.
- The project can check the per-building numbers itself: compare MISC Normal Population / Residential population against
  counts of XBLD building IDs 0x70-0x7B, 0x8C-0x93 and 0xAE-0xB1 across several saves (a least-squares fit gives people per
  building type). This would replace the folklore numbers with measured ones.
- Total population shown by SC2K also counts commercial/industrial workers in some displays. Treat any per-building figures
  with that caution (unverified).

### Gaps
- No primary or decompiled source gives exact population per building ID, or whether the lower/middle/luxury variants of the
  same size hold different numbers of people.
- Prima's "SimCity 2000: Power, Politics, and Planning" (Dargahi & Bremer) was not found as readable full text. A patcoston
  review says it only makes "blanket statements about limitations on the growth of unwatered areas" ([patcoston PPP review](https://patcoston.com/co/ppp.aspx)).

## Q2. What makes dense zones build bigger/taller buildings? Do light zones reach high population?

### Takeaway
Bigger buildings need, in order of importance as the sources describe it: (1) high enough land value, (2) positive demand
for the zone type, (3) road access, with large 3x3 lots apparently needing road on more than one side, (4) jobs and other
zone types within about 10-15 tiles, and (5) water, since the manual says unwatered cities have limited density. Time spent
next to amenities also matters. Light zones stay 1x1 (max about 10/tile), so they can never be high-population.

### Cited Findings
- "A 3X3 zone must have at least 3 roads on one side and 1 road on another side to develop into a large building. It also must have a high enough land value and the demand indicator should be in the +. A big park will often coax a zone into becoming a large building. Also, the zone must have access to other zone types within about 10-15 tiles." — [somacon 1996](http://www.somacon.com/p606.php) (fan claim, unverified)
- "What will happen if you build your entire city of 6X6 zones is that most of the zones will not develop into large buildings because land values will be too low. So, you should put lots of big parks or areas with trees or water to raise land values." Recommends "A grid of 6X6 square zones with roads in between", giving "9 medium buildings or 4 large buildings with no wasted space." — [somacon 1996](http://www.somacon.com/p606.php)
- Weburg: "Land value is the biggest influence on how dense a zone will grow, and whether or not the zone is at an intersection." "The demand for a given zone will greatly influence whether or a zone will become dense." "the amount of time a zone is exposed to these things will have a big effect on whether or not it'll grow dense." Method: "the best way to have a 3x3 zone develope is to simply plot a 3x3 zone, surround it by trees, and wait until it grows. Once it has become a 3x3 zone, plot another 3x3 zone next to it." — [patcoston handzone (Weburg, 1995)](https://patcoston.com/co/handzone.aspx)
- Land value sets the building class: Light residential gives "lower-class homes or expansive acres of mansions" depending on land value, and land value "dictates the type of housing that will develop." — [ludo.guide](https://www.ludo.guide/guide/simcity-2000/light-residential)
- Manual (IT): a city "può esistere anche senza un sistema idrico, ma la densità demografica sarà limitata" (can exist without water, but population density will be limited). Also: "Potete anche costruire una città senza sistema idrico, ma la popolazione non crescerà molto" (without water the population will not grow much). — [Italian manual](https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt)
- Road distance: zones develop only with a road within 3 tiles; rail or subway within 3 also works, but "growth will be much slower." — [Zen and the Art of SimCity 2000](https://ibiblio.org/GameBytes/issue18/misc/zen.html). Same "road within three tiles" rule: [somacon](http://www.somacon.com/p606.php)
- Light vs dense: "Light zoning means you have fewer people over the same land"; converting light to dense saves roads, pipes and power lines. — [Zen](https://ibiblio.org/GameBytes/issue18/misc/zen.html). "use dense for more population but more pollution or light for less of both." — [patcoston advice](https://patcoston.com/co/advice.aspx)
- Manual: "Più è alta la densità della popolazione di un'area, più inquinamento e criminalità avete in essa" (the higher an area's density, the more pollution and crime it has). — [Italian manual](https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt)
- Demand and taxes: tax "around 9% or over" depresses demand, while "7%- 8% will give you better growth demands"; when a demand bar goes below zero, zones are "downsized or abandoned." — [Zen](https://ibiblio.org/GameBytes/issue18/misc/zen.html)
- Zone balance: the manual says the residential tile total should be roughly equal to the commercial total plus the industrial total, with more industry than commerce in a small city. — [Italian manual](https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt). Fan ratios: R:C:I = 4:1:3 below 10,000 people and 4:2:2 for 10,000-60,000; "R = C + I". — [somacon](http://www.somacon.com/p606.php)
- Recreation demand: residential recreation demand starts after 10,000 population. Each recreation tile adds 1,000 to the demand cap; marinas add 9,000, big parks 3,000, zoos and stadiums 16,000 each. — [dfloer simulation spec](https://raw.githubusercontent.com/dfloer/SC2k-docs/master/simulation%20spec.md)
- Manual: marinas, zoos and stadiums "danno un forte impulso alla crescita residenziale" (give a strong push to residential growth). — [Italian manual](https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt)
- Ordinances: City Beautification +1% residential demand; Income Tax ordinance -1% residential demand. — [dfloer simulation spec](https://raw.githubusercontent.com/dfloer/SC2k-docs/master/simulation%20spec.md)

### Inferences
- For a 100k plan: zone dense residential only. Use 6x6 blocks (two 3x3 lots per side) or thin bands 3 deep, so every 3x3
  lot fronts a road. Put parks and trees inside or next to each block. Keep R demand positive (taxes at or below 7-8%). Pipe
  every block. Keep jobs within about 10-15 tiles. This matches the project's own lesson about thin alternating bands.
- "3 roads on one side and 1 on another" probably means a 3x3 lot needs road along a full side plus one more road touch.
  Corner lots (roads on two sides) are the safest. Weburg's "whether or not the zone is at an intersection" supports
  favouring corners. Unverified.

### Gaps
- No exact land-value thresholds (XVAL numbers) for lower, middle or upper class, or for 2x2 versus 3x3, were found.
- No source quantifies how long a zone must sit next to amenities, or how many sim cycles an upgrade takes.

## Q3. Land value: inputs, weights, ranges, speed of change

### Takeaway
The manual lists these as raising land value: trees and forests, water (lakes, rivers, ocean), parks (big parks count about
twice as much as small ones, and small ones about the same as trees), all cultural buildings, police stations (within a
radius), fire stations, City Beautification / Clean-up, and, marginally, homeless shelters. Lowering it: crime, pollution,
and industry. Fans add sloped land, schools, and how long the zone has been exposed. No numeric weights for SC2K were found.
XVAL is a 64x64 map (one cell per 2x2 tiles).

### Cited Findings
- Trees: "Gli alberi aggiungono valore alla terra" (trees add land value). Trees and forests "aumentano il valore delle proprietà" (raise property value) but are flammable and can spread fires. — [Italian manual](https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt)
- Water: "L'acqua aggiunge valore alla terra e ha anche un valore ricreativo" (water adds land value). Lakes, rivers and oceans "aumentano il valore del terreno" (raise land value). — [Italian manual](https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt)
- Parks: "I giardinetti aumentano il valore del terreno più o meno come gli alberi e i grandi parchi circa del doppio" (small parks raise land value about as much as trees, and big parks about double). Recreation facilities "aumentano il valore del terreno e promuovono la crescita delle zone residenziali" (raise land value and promote residential growth). — [Italian manual](https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt)
- Culture: "Tutte le strutture culturali aumentano il valore del terreno locale" (all cultural buildings raise local land value) and need their annual funding. — [Italian manual](https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt)
- Police: stations "fanno diminuire il tasso di criminalità e aumentano il valore del terreno per un certo raggio intorno ad ogni stazione" (lower crime and raise land value within a radius around each station). Fire stations also "aumenta il valore del terreno" (raise land value). — [Italian manual](https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt)
- Crime: "Un tasso di criminalità alto abbassa il valore del terreno, facendo scappare parte della vostra popolazione" (high crime lowers land value and drives away population). — [Italian manual](https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt)
- Industry: industrial zones "hanno una spiccata tendenza verso un basso valore del terreno e un'alta criminalità" (have a marked tendency toward low land value and high crime). — [Italian manual](https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt)
- Ordinances: City Beautification (Abbellimento) "rende più appetibile la zona residenziale e fa aumentare il valore del terreno" (makes residential more attractive and raises land value). The SNES manual phrases this as "City Clean-up increases residential desirability and land value." Homeless shelters give a "marginally increasing land value". — [Italian manual](https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt); SNES port manual (wording may differ from PC): [archive.org sim-city-2000-usa](https://archive.org/download/sim-city-2000-usa/SimCity%202000%20(USA)_djvu.txt)
- Manual advice: keep land value high to keep property-tax money coming in, and build some lower-value areas because "non tutti i vostri SimCittadini possono permettersi case di lusso" (not everyone can afford luxury homes). — [Italian manual](https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt)
- Fan list of raisers: "the proximity to sloped land, water, parks, educational zones, trees, and low crime and pollution". A zone "will benefit by being next to forest or water", but "as soon as that forest or water is destroyed, the zone looses all benefit from it." — [patcoston handzone (Weburg)](https://patcoston.com/co/handzone.aspx)
- Coastline housing gets "better land values out of the deal." — [Zen](https://ibiblio.org/GameBytes/issue18/misc/zen.html)
- Data layout: XTRF, XPLT, XVAL and XCRM are 64x64 overlays ("Total # is 4096 = 64x64"), so each XVAL cell covers 2x2 tiles. XVAL holds "Land Value, simulation shows these values using human friendly 1 indexed." MISC 0x0028 Land Value = "Sum of all the values in XVAL." — [dfloer sc2 file spec](https://raw.githubusercontent.com/dfloer/SC2k-docs/master/sc2%20file%20spec.md)
- Graphs: 1 land-value graph point = 3,200 value points (rounded up). City value "seems to be land value / 2". The bond window shows city value x 1000. Land value apparently does NOT affect tax revenue, although that was reportedly intended. — [dfloer simulation spec](https://raw.githubusercontent.com/dfloer/SC2k-docs/master/simulation%20spec.md). This conflicts with the manual's advice to keep land value high for property taxes ([Italian manual](https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt)).
- OTHER GAME (SimCity 1989 / Micropolis, NOT SC2K), shown only as a possible ancestor model: "Water, park and tree tiles all increase land value", each credits its 4x4 block 15 points, and the sum is stored in one byte that can wrap above 255. The downtown bonus runs from +64 at the centre to -64 at the far corners. Pollution reduces land value, and low land value drives crime. — [jeffquast.com "a perfect simcity"](http://www.jeffquast.com/post/a-perfect-simcity)

### Inferences
- XVAL (0-255 per 2x2 cell) is the right number to watch per block. Map residential XVAL against which building IDs appear
  (lower/middle/luxury, 2x2/3x3) to find the in-game thresholds by experiment.
- On a flat map with no water (this project's map), slopes and coast are not available. The levers left are trees (cheap to
  place), small and big parks, police and fire coverage, schools, libraries and museums, City Beautification, and keeping
  industry and its pollution away from homes.
- A downtown or centre-distance term like SimCity 1989's may exist in SC2K. That is unverified: no SC2K source mentions it.

### Gaps
- No SC2K weights, radii, decay or update rate for land value were found. The manual gives only qualitative effects, plus the
  "big park ≈ 2x small park ≈ 2x trees" ratio.
- How fast XVAL responds after placing parks or trees: no source. Weburg only says exposure time matters.

## Q4. How much does water (pipes) matter for dense growth?

### Takeaway
A lot, according to the manual and fans. Without water the population "will not grow much" and density is limited. Fan tip:
"Water is not necessary, but if you want a dense population it is essential." One contemporary review notes net rumours that
the water model does little, but the official text clearly ties water to density.

### Cited Findings
- Manual: "Una città può esistere anche senza un sistema idrico, ma la densità demografica sarà limitata" (density will be limited). "Potete anche costruire una città senza sistema idrico, ma la popolazione non crescerà molto" (population won't grow much). Sims lay the pipes inside buildings; the player only has to link buildings to the system with mains. — [Italian manual](https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt)
- "Water is not nescessary, but if you want a dense population it is essential." — [patcoston advice](https://patcoston.com/co/advice.aspx)
- "Zones need power and water, or they won't develop" (paraphrase of the Zen guide). During shortages the city's outer edges lose water first. — [Zen](https://ibiblio.org/GameBytes/issue18/misc/zen.html)
- Prima guide review: the book makes only "blanket statements about limitations on the growth of unwatered areas". Net rumours said the water model might do little beyond showing "Water Shortage Reported". — [patcoston PPP review](https://patcoston.com/co/ppp.aspx)
- Pump output: in the manual, a pump next to fresh water gives "circa il triplo" (about triple) a well. Desalination gives double a river pump. A coastal pump is the same as a well. Another manual section says double. Zen also says twice. — [Italian manual](https://archive.org/download/manualzilla-id-6163847/6163847_djvu.txt); [Zen](https://ibiblio.org/GameBytes/issue18/misc/zen.html). Reverse-engineered pump formula: "sea level * 5 + fresh water tiles * 10 + precipitation / 2", with each unit = 720 gallons; one treatment plant per 2,000 tiles. — [dfloer simulation spec](https://raw.githubusercontent.com/dfloer/SC2k-docs/master/simulation%20spec.md)

### Inferences
- Treat water as required for 2x2 and 3x3 residential. Pipe every dense block before or when zoning it, and keep spare
  water capacity well above zero (this project's own lesson: water_pct = spare %).

### Gaps
- No source quantifies the cap on unwatered dense zones (e.g. max building size or stage without water).
