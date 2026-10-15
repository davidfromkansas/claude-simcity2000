# Money in SimCity 2000 (classic, 1993): taxes, bonds, ordinances, expenses, construction costs

Primary sources used (all full text on archive.org):
- Official manual (DOS/Mac): https://archive.org/details/SimCity.2000-Manual (full text: https://archive.org/download/SimCity.2000-Manual/SimCity.2000-Manual_djvu.txt). Below it is called "Manual".
- Nick Dargahi, *SimCity 2000: Power, Politics, and Planning* (Prima, revised ed.): https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised. Below it is called "Dargahi". Ch. 4 "Managing Your Money", Ch. 9 "The City Council and Ordinances".
- *SimCity 2000 Strategies & Secrets, Special Edition* (Sybex): https://archive.org/details/SimCity_2000_Strategies_Secrets_SE. Below it is called "S&S".
- In-game help strings (Windows/SE), copied in the sc2kfix project: https://github.com/araxestroy/sc2kfix/blob/main/modules/sc2k_help.cpp. Below it is called "In-game help".
- Save-file spec: https://github.com/dfloer/SC2k-docs/blob/master/sc2%20file%20spec.md

The OCR is imperfect. Numbers quoted below were checked in the OCR text. Places where the OCR is garbled are flagged.

---

## 1. How property tax is computed (R/C/I)

### Takeaway
Property tax is driven by **population × tax rate**, with land value acting through population (and as a multiplier in the official description). The community rule of thumb is **annual tax ≈ 1.29 × Σ(rate × zone population)**, or ≈ 1.29 × total population × average rate. Your observed ~$0.09-0.10 per resident per year at 6-7% is exactly what this formula predicts. It is normal, not a bug.

### Cited Findings
- Dargahi: "The tax is based on land value and population, as shown in the formula below: Property Tax = Land Value x Tax Rate x Population x Scaling Factor, where Population consists of residential, commercial, and industrial zone populations, and Land Value represents the average land value. The Scaling Factor remains constant." — [Dargahi Ch.4](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Dargahi: "Thanks to SimCity 2000 veteran Kevin Endo, who discovered this simple relationship, you can approximate the tax revenue you earn by applying the following formula: **Property Tax = Total City Population x Tax Rate x 1.29**". A footnote says it "works fine in cities without arcologies, but it gives you less-than-accurate results when you have large arcology populations." — [Dargahi Ch.4](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- S&S: "Instead of making a simple calculation based on the value of each building in your city as you might expect, the program calculates property tax based on population. When you maintain high land values, you actually are maintaining higher populations, which increases the amount of property tax collected… **Tax collected = 1.29 x {[T(residential) x P(residential)] + [T(commercial) x P(commercial)] + [T(industrial) x P(industrial)]}** where T is tax rate and P is population." — [S&S](https://archive.org/details/SimCity_2000_Strategies_Secrets_SE)
- Manual: "Property taxes are your main source of cash… The minimum tax is 0%, the maximum is 20%. Any taxes you set here will be equally applied to all zones. You can independently set the tax rates for residential, commercial and industrial zones in the Property Taxes Books." If you set the three rates separately, the Budget window shows "the average of the three rates." — [Manual p.82-83](https://archive.org/details/SimCity.2000-Manual)
- The Manual's sample Property Taxes book shows a city earning about **$148-150/month residential, $81-83 commercial, $118-120 industrial, for $4,202 for the year** (the rate column is OCR-garbled as "595", probably 5% or 7%; the city's population is not given). — [Manual p.83](https://archive.org/details/SimCity.2000-Manual)
- The industry window also has **per-industry tax rates** (11 industry types: steel/mining, textiles, petrochemical, food, construction, automotive, aerospace, finance, media, electronics, tourism) that you set by dragging bars. "This is the property tax for industry as set in the Budget window." — [Manual p.92-93](https://archive.org/details/SimCity.2000-Manual); per-industry rates are saved in the file (`pIndividualIndTaxRate`) — [sc2kfix save_vanilla.cpp](https://github.com/araxestroy/sc2kfix/blob/main/modules/save_vanilla.cpp)
- Taxes accrue monthly but reach your funds only at year's end: "Tax revenues are not available to you till the following January, even though they are collected on a month-by-month basis." — [Dargahi Ch.4](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised). In-game help: "Estimated and accrued funds are not added into current funds until the year's end." — [In-game help](https://github.com/araxestroy/sc2kfix/blob/main/modules/sc2k_help.cpp)
- Save layout: the res/com/ind tax blocks hold "current population (possibly), current rate, …, then population and rate pairs for January through December" (offsets 0x077C / 0x07E8 / 0x0854). So the game stores a population figure next to each zone's monthly rate, which fits a population-based tax. — [dfloer SC2k-docs](https://github.com/dfloer/SC2k-docs/blob/master/sc2%20file%20spec.md)
- Land value: S&S gives an example: "You'll get greater income taxing land that is worth $150,000 at 7% (you'd get $10,500) than … land that is worth $75,000 at 10% (you'd get $7,500)". This illustrates the idea and is not the real formula (it contradicts S&S's own population formula). — [S&S](https://archive.org/details/SimCity_2000_Strategies_Secrets_SE)
- Dargahi on density: "Tax revenue is based on a combination of population and land values." The choice between light and dense zones trades higher land value (light) against higher population (dense). — [Dargahi Ch.2](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)

### Inferences
- **Units check against our own data.** The 1.29 factor only works with the rate as a fraction (7% = 0.07) and the result in $ per year:
  - 11,500 people × average rate (9+5+5)/3 = 6.33% × 1.29 = **≈ $939/yr**. Observed: $1,042.
  - 2,530 × 0.07 × 1.29 = **≈ $228/yr**. Observed: $245.
  - Both are within ~10%. Our ~$0.09-0.10 per resident per year is **normal**.
- **Projections** (formula only; real results vary with land value):
  - 10,000 people: about $900/yr at 7%, about $1,160 at 9%.
  - 50,000 people: about $4,500/yr at 7%.
  - 100,000 people: about **$9,000/yr at 7%**, about $11,600 at 9%.
- The per-zone version weights each rate by that zone's population. Since residents are usually the largest P, **the residential rate moves income the most**. A 9% R rate with 5% C/I earns more than a flat 6.3% if residential population is the bigger share.
- Income per resident is fixed by the rate, so the only real levers are **(a) more population** and **(b) a higher rate**. Land value helps mainly by allowing denser, larger buildings (more people per tile).
- Money is tight at every size: a 100k city earns only around $9-12k/yr. So power plants ($2-15k) and bond interest weigh heavily even late in the game.

### Gaps
- The exact land-value term and the "Scaling Factor" in the official formula were not found. No decompiled source for the tax routine was found (sc2kfix hooks the budget UI only).
- I could not confirm whether "P(commercial)/P(industrial)" means the jobs counts shown in-game.

---

## 2. Example tax incomes at 10k / 50k / 100k

### Takeaway
No published Budget-window screenshots at those sizes were found. The best numbers come from the 1.29 formula, which matches our own two measurements.

### Cited Findings
- Formula: Property Tax ≈ population × rate × 1.29 — [Dargahi](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised); [S&S](https://archive.org/details/SimCity_2000_Strategies_Secrets_SE)
- The Manual's sample city: $4,202/yr property tax (population not stated) — [Manual p.83](https://archive.org/details/SimCity.2000-Manual)
- Dargahi (ordinances chapter): parking fines are only worth it "if you really need a quick couple hundred bucks", which shows how small amounts are in this economy. — [Dargahi Ch.9](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Will Wright/Fred Haslam (S&S foreword): "To my chagrin, I found that you could actually use a bond to generate rapid growth that would offset the bond expense." — [S&S foreword](https://archive.org/details/SimCity_2000_Strategies_Secrets_SE)

### Inferences
- Expected property tax (formula):
  - 10k: ≈ $900 at 7%, ≈ $1,160 at 9%
  - 50k: ≈ $4,500 at 7%, ≈ $5,800 at 9%
  - 100k: ≈ $9,000 at 7%, ≈ $11,600 at 9%
- Add finance ordinances (section 4), roughly +$1 per 30-75 residents. At 100k that could add a few thousand $/yr.

### Gaps
- No verified real-game Budget screenshots at 50k or 100k were found.

---

## 3. Tax rates vs demand (neutral rate, collapse point)

### Takeaway
**7% is the game's "average"/neutral rate.** 0-6% speeds growth, 7-9% gives slow growth with stable revenue, and above 9% the city declines. One test found the long-run revenue peak at about 9%. On Normal/Medium, industry tax should stay at or below 7%.

### Cited Findings
- In-game help: "The minimum tax is 0% and the maximum is 20%. **A tax rate of 7% is average.** Low taxes attract citizens and businesses. High taxes will drive them out, but earn you more." Also: "Sometimes a lower rate can bring in more funds because the city grows larger." — [In-game help](https://github.com/araxestroy/sc2kfix/blob/main/modules/sc2k_help.cpp)
- Dargahi Table 4-1: "**0-6**: Fast growth in all zones, diminished tax revenues; **7-9**: Slow but gradual growth, tax revenues stable; [10-20, OCR garbled]: All zones decline, population decreases, initially high tax revenues decrease rapidly." The text adds: "Tax rates above nine percent are suicidal… Lowering taxes below six percent encourages growth." — [Dargahi Ch.4](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- S&S: "Sims reach the limit of their tolerance at about 9%"; "the safety zone for property taxation seems to be between 6% and 9%"; "(The safe range for taxation is 6%-8%.)"; and "The fastest way to kill off your city is to raise taxes to 20% and cut city services." — [S&S](https://archive.org/details/SimCity_2000_Strategies_Secrets_SE)
- An experiment (SC2000 under Wine) stepped rates over 0-20% in 3% steps with 5.5-year runs: "**9% appears to be the approximate maxima**" of average revenue; at 15% revenue "drops steeply." — [danbscott Laffer curve](https://danbscott.ghost.io/sim-citys-laffer-curve/)
- Ludo guide: "taxes can rise to about 9% without major consequences" when zone ratios are balanced. On Normal difficulty keep **industrial taxes ≤7%**; on Hard, as low as 4%. Lowering a zone's tax helps most where that zone's demand is low. — [ludo.guide budget](https://www.ludo.guide/guide/simcity-2000/budget)
- Old player tips: "Keep taxes around 7 or 8%" (Greg Kelly); "Keep your tax rate at 7-8%" (Jerry Moore) — [patcoston STRAT3](https://patcoston.com/co/strat3.aspx)
- S&S: setting electronics' industry tax to 4% in the late 20th century "is a big boon to urban growth." — [S&S](https://archive.org/details/SimCity_2000_Strategies_Secrets_SE)
- Difficulty: Medium = $10,000 start and "the national economy is stable"; Easy = boom, Hard = recession. "The easier the game, the more demand for the products that your city's industries can produce." — [Manual p.~97](https://archive.org/details/SimCity.2000-Manual)

### Inferences
- For a growth race to 100k: keep R and C around 6-7% while demand needs help, and I at ≤7% (lower it if industrial demand is the bottleneck). Raise R toward 8-9% only when R demand is clearly maxed.
- Dropping one zone from 7% to 5% costs only about 0.02 × P × 1.29 per year (for example, 5,000 workers → about $130/yr). That is cheap if it unlocks growth.

### Gaps
- No exact demand-response curve per 1% was found. Table 4-1's third row is OCR-garbled (likely "10-20").

---

## 4. Ordinances: income/cost and side effects

### Takeaway
There are four money-raising ordinances: **1% Income Tax** (~$1 per 75 residents/yr, the biggest), **Legalized Gambling** (~$1 per 38 commercial Sims, but adds crime), **1% Sales Tax** (~$1 per 75 commercial Sims) and **Parking Fines** (~$1 per 150 residents). Each slightly hurts demand (income tax → residential; sales tax and parking fines → commercial). Costs of the other programs scale with population.

### Cited Findings (Dargahi Ch.9 "approximate… close enough for planning purposes": [Dargahi](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised))

Income ordinances:

| Ordinance | Income per year | Effect on growth |
|---|---|---|
| 1% Sales Tax | +$1 per 75 commercial Sims | "Slight negative effect on commerce" |
| 1% Income Tax | +$1 per 75 residential Sims | "Moderate negative effect on residential growth"; "biggest money maker of all the ordinances" |
| Legalized Gambling | +$1 per 38 commercial Sims | "Increases crime"; "the police funding and the loss to land value-based taxes cost more than the gambling brings in" |
| Parking Fines | +$1 per 150 residential Sims | "Very slight negative effect on commerce"; "Unless you really need a quick couple hundred bucks, don't bother" |

Cost ordinances:

| Ordinance | Cost per year |
|---|---|
| Pro-Reading | −$1 per 450 residential |
| Anti-Drug | −$1 per 850 total |
| CPR Training | −$1 per 1,000 total |
| Neighborhood Watch | −$1 per 230 residential |
| Volunteer Fire Dept | −$1 per 230 residential |
| Public Smoking Ban | −$1 per 500 commercial |
| Free Clinics | −$1 per 150 residential |
| Junior Sports | −$1 per 300 residential |
| Tourist Advertising | −$1 per 75 commercial |
| Business Advertising | −$1 per 75 industrial |
| City Beautification | −$1 per 300 residential ("Increases residential growth and land value") |
| Annual Carnival | −$1 per 230 commercial ("very approximate"; wait until 10k+ pop) |
| Energy Conservation | −$1 per 75 total. Claims +15% power capacity; James Alton's tests found "two to three percent." |
| Homeless Shelters | −$1 per 150 residential |
| Pollution Controls | −$1 per 75 industrial |
| Nuclear Free Zone | Free. Small residential plus, small industry minus; blocks building or replacing nuclear plants. |

- Manual tutorial city (population not stated): Sales Tax 196, Income Tax 360, Legalized Gambling 98, Parking Fines 180, Volunteer Fire −120, Free Clinics −130, Pro-Reading −60 (OCR; "$/yr" implied). — [Manual tutorial p.42](https://archive.org/details/SimCity.2000-Manual)
- Manual: "1% Sales Tax will add cash … but may also inhibit local commerce. 1% Income Tax … may discourage residential growth, and even cause some tax-haters to move away. Legalized Gambling … brings with it an increase in crime. Parking Fines are a small, steady source of the green, but tend to hinder commercial growth a little." Costs "will vary with the size and development of your city." — [Manual p.89-91](https://archive.org/details/SimCity.2000-Manual)
- In-game help adds that gambling "will increase your tourist trade and act as an incentive to commerce", and that Parking Fines "encourage city residents to use mass transit… [but] make people think twice before moving to your city." — [In-game help](https://github.com/araxestroy/sc2kfix/blob/main/modules/sc2k_help.cpp)
- The City Council may enact programs on its own if the city is doing well. — [Manual p.83](https://archive.org/details/SimCity.2000-Manual). Dargahi says choosing No Disasters stops them doing so. — [Dargahi Ch.9](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Ludo guide (opinion): Parking Fines, City Beautification and Annual Carnival are "cost-effective" relative to their RCI effect. — [ludo.guide](https://www.ludo.guide/guide/simcity-2000/budget)

### Inferences
- At 100k people (say ~60k residents and ~20k commercial Sims):
  - Income Tax ≈ $800/yr
  - Sales Tax ≈ $270
  - Gambling ≈ $530
  - Parking ≈ $400
  - Together that is ≈ +20% on top of ~$9k property tax.
- At 10k people, all four together are only ~$250/yr. Early on they are worth less than the growth they cost.

### Gaps
- What counts as the "commercial/residential population" in these per-capita figures is not defined. No exact code formulas were found.

---

## 5. Bonds

### Takeaway
Bonds come in fixed **$10,000** units at **prime ("Fed"/bank) rate + 1% + a premium for credit rating**. Each extra bond lowers your rating and raises the next rate. Interest accrues monthly and is paid each January. There is no maturity date. Repayment is oldest-first and costs the full $10,000. You can hold **one bond per $4M of city value, up to 50 bonds ($500k)**. Negative funds block all building, and **−$100,000 ends the game**.

### Cited Findings
- Manual: "All bonds are issued for $10,000. The interest you pay on outstanding bonds is prime rate plus 1%, plus an additional percentage based on your city's current value and loan rating." "Loan ratings range from AAA to F. Your rating is based on your city value. The higher your rating, the more bonds you can issue and the lower the interest rate you pay on them." "If your loan rating or city value is too low, you won't be allowed to issue any more bonds." "Bonds are always repaid from the oldest to the newest. During the life of the bond, interest accrues monthly, and is paid out at the end of each year." The Manual's example: one $10,000 bond at 4.0% = −$33/−$34 per month (≈$400/yr); Show Bonds shows "BankRate 3%, NextBond 4%, City Value $84,500,000, Loan Rating AAA". — [Manual p.83-85](https://archive.org/details/SimCity.2000-Manual)
- In-game help: "The rate on these bonds is based on the prime rate plus a percentage based on your city value. **The best rate is prime+1%.** Given that the prime rate changes from year to year, it is possible to have an outstanding bond with a rate that is lower than the current prime." "The 'Fed Rate'… is influenced by both GNP and Nat'l Pop. You cannot control this." — [In-game help](https://github.com/araxestroy/sc2kfix/blob/main/modules/sc2k_help.cpp)
- Dargahi:
  - "you usually end up paying one to two percent above this rate."
  - On ratings: "your credit rating starts out at a very high AAA… take out a $10,000 bond at five percent… now your credit rating has fallen a notch to AA. Taking out a second bond… the interest rate now being offered is six percent… dropped to an A rating… eventually… F. At this point… you cannot take out any more loans."
  - On limits: "You are able to issue an additional $10,000 bond for **each $4,000,000 of city value up to a maximum of 50 bonds, or $500,000**… If you try issuing bonds before building any city at all, then you will be allowed to issue only one bond." For example, "a coal power plant that is worth $40,000,000 [lets you] issue up to 10 bonds."
  - City Value counts "infrastructure and buildings, but not the value of buildings… built by the Sims in the [RCI] zones."

  — [Dargahi Ch.4](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Dargahi on deficits: "If you don't have enough money to pay the interest in January, then this interest will be added to your deficit… With a negative balance in your treasury, you cannot build or do anything except take out more bonds or raise taxes… **If you allow your deficit to pass the −$100,000 mark, you will be kicked out of office**… the game will end." "Unlike in the real world, bonds never mature… you need never repay a bond." Advice: "If you have a small city… stay away from bonds — they will eat you alive." But "For medium-to-large cities that have a positive cash flow, taking out bonds can be useful." — [Dargahi Ch.4](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Save file: up to 50 bond entries. Rates are stored ×10,000 (4% = 40,000). "National Trend … affects interest rates." — [dfloer SC2k-docs](https://github.com/dfloer/SC2k-docs/blob/master/sc2%20file%20spec.md)
- Hard difficulty starts "$10,000 in debt, with a bond issue to pay back." — [Manual](https://archive.org/details/SimCity.2000-Manual)
- Refinancing: if federal rates drop, issue a new low-rate bond to repay an older high-rate one. — [ludo.guide](https://www.ludo.guide/guide/simcity-2000/budget)
- S&S: "You should only consider issuing a bond to finance a part of your city that will generate tax revenue in the future… As a rule of thumb, we discourage issuing bonds." — [S&S](https://archive.org/details/SimCity_2000_Strategies_Secrets_SE)

### Inferences
- Your $400-530/yr per $10k bond means 4-5.3% rates, which is consistent with prime ~3% + 1% + rating premium. This is normal.
- **Payback test:** a $10k bond pays for itself in interest terms only if it adds at least $500/yr of income. At ~$0.09 per resident per year (7%), that is **≥5,500 extra residents**, or about $830/yr more if repaid within ~12 years. Bonds make sense only when $10k unlocks growth that money is the bottleneck for, such as power plants, water, or the neighbor link.
- Taking 3-4 bonds at once quickly pushes rates up (5% → 6% → …) and the rating down.
- Repaying a bond costs $10,000 cash. At a 100k city's ~$9-12k/yr gross, repaying more than one bond per year is hard.

### Gaps
- The exact rating thresholds and premium per notch are not documented. The "fund" bond rate (25%) is fixed.

---

## 6. Expense lines: services, funding cuts, transit

### Takeaway
Service upkeep is tiny in absolute dollars. At 100% funding:

| Item | Upkeep per year |
|---|---|
| Police station | $100 |
| Fire station | $100 |
| Hospital | $50 or $75 (sources conflict) |
| School | $25 |
| College | $100 |
| Roads | $1 per 10 tiles |
| Rail | $1 per 5 tiles |
| Highway | $1 per 4-tile section |
| Subway, bridges, tunnels | $2 per 5 tiles |

Funding scales cost linearly and reduces effectiveness.

### Cited Findings
- Manual:
  - "Complete funding for a police station is $100 per year." The example book shows 21 stations at −$175/month = −$2,100/yr.
  - "A fully funded fire station costs $100 per year."
  - "Complete funding for a hospital is $75 per year."
  - "Complete funding for a school costs $25 per year, and a college costs $100 per year."
  - Transit: "Roads $1 per 10 tiles; Rails $1 per 5 tiles; Highways $1 per section (4 tiles); Subways $2 per 5 tiles; Bridges $2 per 5 tiles; Tunnels $2 per 5 tiles."

  — [Manual p.85-88](https://archive.org/details/SimCity.2000-Manual)
- **Conflict on hospitals:** in-game help says "Hospitals cost $50 for one full year of operation"; S&S also says $50. The Manual says $75, but the Manual's own example book (5 hospitals, $500/yr) implies $100. — [In-game help](https://github.com/araxestroy/sc2kfix/blob/main/modules/sc2k_help.cpp); [S&S](https://archive.org/details/SimCity_2000_Strategies_Secrets_SE)
- In-game help: "100% funding means you are paying full price and receiving full service. The up and down arrows adjust the funding by +/-5%." "Less than full funding has a detrimental effect… Fire and police service smaller areas, hospitals help fewer people, transit cutbacks allow roads to decay, and education cutbacks result in a lowered EQ." "With less than 100% funding, the police will be less efficient, but the annual cost will decrease accordingly." — [In-game help](https://github.com/araxestroy/sc2kfix/blob/main/modules/sc2k_help.cpp)
- Libraries and museums have no budget line. "The Education budget affects only schools and colleges." — [S&S](https://archive.org/details/SimCity_2000_Strategies_Secrets_SE)
- Dargahi: bus stations count under roads, power lines over water under bridges, subway stations under subways, train depots under rail. He also reports **a bug: "you can let your transportation infrastructure fall into disrepair without any affect on population levels"** (DOS/Mac 1.0-1.1 era; unverified for other versions). — [Dargahi Ch.4](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- With No Disasters on, fire funding can go to 0%. — [S&S](https://archive.org/details/SimCity_2000_Strategies_Secrets_SE); [ludo.guide](https://www.ludo.guide/guide/simcity-2000/budget). The ludo guide also says to fund transit at 100% except the subway.
- Manual strategy: "If you need to skimp on city services, go ahead, but keep your police well-funded… If the arrests are equal to the crimes, you can try lowering the funding." — [Manual p.118-119](https://archive.org/details/SimCity.2000-Manual)
- Ports have no upkeep: "There are no maintenance costs for ports." — [Dargahi Ch.2](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Player anecdotes (unverified): "Drop funding on everything to 15% except transportation" (Jerry Moore); a claim that police cost "10,800" in one city (Greg Kelly; contradicts $100/station unless ~108 stations). — [patcoston STRAT3](https://patcoston.com/co/strat3.aspx)

### Inferences
- A 100k city with, for example, 15 police stations, 10 fire stations, 15 schools, 3 colleges, 4 hospitals and 2,000 road tiles costs about $1.5k + $1.0k + $375 + $300 + $200-300 + $200 ≈ **$3.6k/yr**, against roughly $9-12k of tax.
- The big money sinks are construction and power-plant replacement, not upkeep.

### Gaps
- No exact formula for coverage radius versus funding was found.

---

## 7. Other income sources

### Takeaway
Classic SC2000 has **no neighbor deals** (selling power or water is a SimCity 3000 feature) and **no direct income from seaports or airports**. These only raise demand caps and growth. Arcologies unlock at 120,000 people, past our target. Property tax plus the four finance ordinances are effectively the only income.

### Cited Findings
- The Manual's budget lines are only: Property Taxes, City Ordinances, Bond Payments, Police, Fire, Health & Welfare, Education, Transit Authority. There are no neighbor deals or port revenue. — [Manual p.82-88](https://archive.org/details/SimCity.2000-Manual); [In-game help: "eight budget commisioners"](https://github.com/araxestroy/sc2kfix/blob/main/modules/sc2k_help.cpp)
- Neighbor connections cost money and boost demand:
  - Road link costs $1,000 and helps commerce only ("effects… seem very weak").
  - Highway link costs $1,500.
  - Rail link costs $1,500 and helps industry.
  - Seaport (worth it from ~10,000 pop) boosts industry; airport (from ~15,000 pop) boosts commerce.
  - "Commerce is heavily favored only when your city has grown past a population of 100,000."

  — [Dargahi Ch.2](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Stadiums and marinas "give a big boost to the growth of residential zones." — [Dargahi Ch.2](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)
- Arcologies: "Arcologies at a population of 120,000." — [Manual p.112](https://archive.org/details/SimCity.2000-Manual). Costs and populations: Plymouth (2000) $100,000, 55,000 people; Forest (2050) $120,000, 30,000; Darco (2100) $150,000, 45,000; Launch (2150) $200,000, 65,000. — [S&S ch.14](https://archive.org/details/SimCity_2000_Strategies_Secrets_SE)
- Military base offered at 60,000 people. — [Manual p.112](https://archive.org/details/SimCity.2000-Manual)
- Cheats (noted only, NOT to be used): DOS "fund" gives "a $10,000 bond at 25 percent interest". The "Double-Fund Trick" (two fund bonds, issue one, repay the first two in a brand-new city) created negative interest worth "$1,548,199 per year" in DOS; it was fixed in Windows. — [Dargahi Ch.10](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised); [patcoston CHEATDOS](https://patcoston.com/co/CHEATDOS.aspx)
- Folklore (UNVERIFIED, likely wrong): S&S claims taxes are "collected retroactively for the entire year in December", so raising to 20% in December and back to 7% in January gives extra income. This conflicts with the monthly per-rate rows in the Property Tax book (Manual/Dargahi show the rate and amount per month). — [S&S](https://archive.org/details/SimCity_2000_Strategies_Secrets_SE)

### Inferences
- For the 100k goal, "more income" comes only from more taxed population, rates up to ~9%, and finance ordinances. Every neighbor link, port or stadium is a demand investment, not revenue.

### Gaps
- None found for SC2000 port income. I am confident none exists, based on the budget-line list.

---

## 8. Construction costs (Manual reference section)

### Cited Findings ([Manual Reference p.~60-75 and p.103-104](https://archive.org/details/SimCity.2000-Manual))

Terrain and clearing:

| Item | Cost |
|---|---|
| Bulldoze/clear | $1 per tile |
| Raise/lower/level terrain | $25 per tile per altitude change |
| De-zone | $1 per tile |
| Trees | $3 per click |
| Water | $100 per tile |

Zones:

| Zone | Light | Dense |
|---|---|---|
| Residential | $5 per tile | $10 per tile |
| Commercial | $5 per tile | $10 per tile |
| Industrial | $5 per tile | $10 per tile |

Transport:

| Item | Cost |
|---|---|
| Road | $10 per tile |
| Highway | $100 per 4-tile section |
| Onramp | $25 per tile |
| Tunnel | $150 per tile |
| Rail | $25 per tile |
| Rail depot | $250 |
| Subway | $100 per tile |
| Subway station | $500 (OCR) |
| Bus depot | $250 (OCR) |
| Subway-to-rail junction | $250 |
| Seaport | $150 per tile |
| Airport | $250 per tile |

Power and water:

| Item | Cost |
|---|---|
| Power line | $2 per tile (land), $10 per tile (water) |
| Water pipe | $3 per tile |
| Water pump | $100 |
| Water tower | $250 |
| Treatment plant | $500 |
| Desalination plant | $1,000 |

Power plants ("years are +/- 10"):

| Type | Available | MW | Cost | $/MW |
|---|---|---|---|---|
| Coal | 1900 | 200 | $4,000 | $20 |
| Hydro | 1900 | 20 | $400 | $20 |
| Oil | 1900 | 220 | $6,600 | $30 |
| Gas | 1950 | 50 | $2,000 | $40 |
| Nuclear | 1955 | 500 | $15,000 | $30 |
| Wind | 1980 | 4 | $100 | $25 |
| Solar | 1990 | 50 | $1,300 | $26 |
| Microwave | 2020 | 1,600 | $28,000 | $17.5 |
| Fusion | 2050 | 2,500 | $40,000 | $16 |

- "Developed areas require on the average **one Mw for three occupied tiles**."
- "All power plants have a 50-year life span." With No Disasters they are auto-rebuilt; otherwise they collapse.

Services and recreation:

| Item | Cost |
|---|---|
| School | $250 |
| College | $1,000 |
| Library | $500 |
| Museum | not legible in OCR |
| Police station | $500 |
| Fire station | $500 |
| Hospital | $500 |
| Prison | $3,000 |
| Small park | $20 |
| Big park | $150 |
| Zoo | $3,000 |
| Stadium | $5,000 |
| Marina | $1,000 |

Neighbor links: road $1,000; highway $1,500; rail $1,500. — [Dargahi Ch.2](https://archive.org/details/SimCity_2000_Power_Politics_and_Planning_Revised)

### Inferences
- Gas is the most expensive power per MW ($40). A coal plant gives 4× the MW of gas for 2× the price. From ~2020, microwave ($17.5/MW) is the cheapest.
- At 1 MW per 3 tiles, 100k people on light zones needs thousands of tiles and therefore several hundred MW. That means **$8-20k of plants**, which is 1-2 years of a 100k city's whole tax take, and plants must be replaced at the 50-year mark.

### Gaps
- Museum, subway station and bus depot costs are partly illegible in the OCR. Check them with the in-game tool info panel.
