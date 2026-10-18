# Plan: Claude Plays SimCity 2000

## Goal

Start a new city and:

1. Reach **5,000 residents** within **30 game years**.
2. Then keep a **positive annual budget for 3 years in a row**, with **no bonds** (no borrowing).

## How it works (big picture)

```
 ┌───────────────┐   screenshot   ┌──────────────┐
 │ SimCity 2000  │ ─────────────► │   Claude     │
 │ (DOSBox, in a │                │ (looks at the│
 │ virtual screen│ ◄───────────── │ screen, picks│
 └───────────────┘ mouse / keys   │ next move)   │
        │                         └──────────────┘
        │ save file                      ▲
        ▼                                │ exact numbers
 ┌───────────────┐                       │
 │ Save reader   │ ──────────────────────┘
 │ (population,  │
 │ money, bonds) │
 └───────────────┘
```

- The game runs in **DOSBox** on a hidden virtual screen.
- Claude **sees** the game through screenshots and **plays** by sending mouse clicks and key presses.
- Every in-game year we **save the game** and read the save file to get exact numbers (population, cash, bonds, year). Screens can be misread; the save file can't.

## Steps

### 1. Get the game running
- Download the DOS version from the archive.org link.
- Install DOSBox, a virtual screen (Xvfb), and a tool to send clicks/keys (xdotool).
- Start the game, confirm it loads, and take a screenshot.
- Note: you should own a copy of the game; archive.org hosts it as "abandonware".

### 2. Build the "hands and eyes"
A small Python program that can:
- `screenshot()` – grab the game screen.
- `click(x, y)`, `drag(from, to)`, `press(key)` – control the game.
- `pause()` / `set_speed()` – stop time while Claude thinks.

### 3. Build the "scorekeeper"
- Read the `.SC2` save file (its format is publicly documented).
- Pull out: **year, population, cash, number of bonds, yearly income vs. expenses**.
- Write a log row every year (`progress.csv`) so we can track the goal.

### 4. Connect Claude (uses your Claude subscription, no API key)
- **Claude Code itself plays the game** in this session — no separate API key or API billing.
- Small helper commands do the work: `./sc snap` (save a screenshot), `./sc click x y`, `./sc key F`, `./sc stats` (read the save file).
- Claude runs a helper, opens the screenshot to look at it, decides, and runs the next helper. Repeat.
- `/loop` keeps Claude playing turn after turn without you typing "continue".
- Claude keeps a `city-notes.md` file (what's built where, current strategy, last good save) so it can pick up where it left off if the chat gets long or a new session starts.

### 5. Play the game (strategy Claude follows)

**Setup**
- New city, **Easy** difficulty ($20,000 start), **disasters off**, flat land near water.

**Years 1–5: Get started cheap**
- One **coal power plant** (cheapest).
- Small grid of **roads** (no rails/highways – too costly).
- **Light** residential, commercial, and industrial zones, about 2 : 1 : 1.
- Keep industry away from homes.

**Years 5–15: Grow to 5,000**
- Watch the **R/C/I demand bars** and zone what's in demand.
- Add a **police station** and **fire station** only once crime/fires appear.
- Add **water pumps** and pipes when growth slows.
- Keep taxes around **7–8%**.

**After 5,000: Keep the budget positive**
- **Never** issue bonds.
- Cut spending on things not needed yet (e.g., lower road/transit funding a bit, skip expensive buildings).
- Raise taxes slightly (up to ~9%) if income < expenses.
- Check the budget every January; need **3 positive years in a row**.

### 6. Safety rules for the bot
- Auto-save every game year (so we can recover from mistakes).
- Never click "issue bond" – block it in code.
- If cash drops below a safe level, stop building and focus on budget.
- If stuck for too long, reload the last good save.

### 7. Report results
- A final summary: the year 5,000 was reached, the 3 positive budget years, and a chart of population and cash over time.
- Save screenshots of key moments.

## Success check (automatic)

| Check | Pass when |
|---|---|
| Population | ≥ 5,000 before game year 30 |
| Budget | 3 consecutive years with income > expenses |
| No borrowing | Bond count stays at 0 the whole game |

## Risks

- **Misreading the screen** → fixed by using the save file for numbers.
- **Mis-clicks** (small icons, old 640×480 screen) → map exact menu positions once and reuse them.
- **Subscription usage limits** → each screenshot uses some of your plan. To save usage: shrink screenshots, use save-file numbers instead of screenshots when possible, and let years run at fast speed when nothing needs doing. If you hit your limit, the game is saved and Claude continues later from `city-notes.md`.

## Suggested order of work

1. Game running in DOSBox + screenshots ✅ first milestone
2. Click/key control
3. Save-file reader
4. Claude loop
5. Full playthrough + report
