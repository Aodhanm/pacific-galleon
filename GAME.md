# PACIFIC GALLEON

    python3 serve_nocache.py                          # port 8914
    open http://127.0.0.1:8914/index.html             # title
    open http://127.0.0.1:8914/captains.html          # choose your captain
    open http://127.0.0.1:8914/play.html?ship=desire  # straight into the ambush

The English raiders of the Pacific, 1579 to 1743, and the richest prize on earth.
You lie in wait at Cabo San Lucas, sight the Manila galleon coming down on the
cape, run her down, batter her until she strikes, lay her aboard, take what your
hold will carry, and get clear before her consort comes down on you.

Files: `index.html` (title) · `captains.html` (the four captains) · `play.html`
(loop, HUD, gunnery, cards) · `ships.js` (classes, square-rig physics, drawing) ·
`cape.js` (the place) · `PLAN.md` (design) · `SOURCES-WORKING.md` (the research
ledger, with locators) · `sources-raw-verification-2026-10-07.json` (59 claims
checked against fetched sources, with 37 recorded null results).

---

## ⭐ The rule

**The fun is number one. The story is number two.** Aodhan's ruling, 2026-10-07.

Every ship always fires back. A prize that cannot shoot is not a fight. Where the
record and the fun disagree, the fun wins and the departure is flagged below, the
way doghole flags its invented entrance buoys. The research is a source of
material, not a constraint on design, and it has earned its keep: the best things
in this document are mechanics lifted straight out of period sources.

---

## The place is sourced

Three navigators describe this anchorage and they agree with each other and with
the modern pilots. Cabo San Lucas is the one place on five thousand miles of ocean
where the galleon had to come within reach of the land.

| In the game | The source |
|---|---|
| Why the ambush is HERE at all | Anson, 1748, from captured Spanish instructions: the cape is "a station where she is constantly expected, and where she has been often waited for and fought with, though generally with little success" |
| She comes in from seaward onto the cape | Pretty, 1587: the lookout "espied a sayle bearing in from the sea with the cape" |
| She closes the land only at the cape | Anson: they "steer to the southward without endeavouring to approach the coast, till they have run into a lower latitude"; only "when they draw near its southern extremity, they venture to hale in" |
| The anchorage, and its depth | Cavendish's own log, 1587: "You may anker in the port of S. Lucas on the Cape of California in 12 fadoms water" |
| ⭐ The hazard: a south-easter | the same sentence: "and a Southeast winde is the woorst." Shelvocke, 1726, independently: he "lay open to the sea from the E. by N. to the S. E. by S." The 1886 and 1893 pilots say the same thing three hundred years later |
| The steep bank and the deep water close in | Shelvocke: anchor on the bank on the northern side "from 16 to 8 fathoms", but keep off the southern side "where there is very deep water; for the bank shelves away very fast". That is the Cabo San Lucas submarine canyon, and `cape.js` already draws it |
| Land's End as a file of rocks | Pretty: the cape "is very like the Needles at the isle of Wight" |
| The bay is at the cape, and it has water | Shaler, 1808: "Directly round Cape San Lucas there is a very commodious anchorage, called Puerto Segura, where there is very good water" |
| Fresh water and refreshments waiting for her | Anson: "there are refreshments, as fruits, wine, water, etc., constantly kept in readiness for her" |
| Three weeks of lying in wait | Pretty: raised the cape 14 October, "lay off and on from the saide cape of S. Lucar untill the fourth of November" |

**The name.** Rogers (1709) and Shelvocke (1726) both call it "Puerto Seguro, so
call'd by Sir Thomas Cavendish". Cavendish's own narrative refutes them: it is
"called by the Spaniards, Aguada Segura, or Puerto Seguro". The Spanish name was
already there in 1587.

---

## The fight is tuned, and the tuning is measured

All gunnery numbers live in one `GUN` block at the top of `play.html`. Run
`__dev.duel()` in the console to measure any change: it fights the duel headless
and reports how long she took to strike and what it cost you.

Before 2026-10-07 the duel lasted **12.6 seconds** and cost the player 5% of her
hull, because she struck after 9 hits while needing 20 to kill you. She now takes
about 23. Measured at 110 yards, firing the instant your guns are loaded:

| Ship | Hull | Duel | You end at |
|---|---|---|---|
| Golden Hind | 1.0 | 72.5s | 82% dead |
| Desire | 1.4 | 66.5s | 59% |
| Duke | 1.9 | 66.6s | 28% |
| Centurion | 2.4 | 30.4s | 6% |

⚠ Those are the EASIEST possible numbers: the harness lays you perfectly abeam and
never misses a reload. Real sailing is worse.

**The Hull stat used to be a lie.** `captains.html` has always advertised Hull 2 /
3 / 4 / 5 and the simulation ignored it: every ship bilged at the same hard-coded
1.5. Each class now carries its own `hull` and the stat screen tells the truth.

A period sanity check on the gunnery, from Anson's carpenter's survey of the
Covadonga: 341 round shot expended, about 141 through her hull and masts, and the
Centurion took 20 to 30 herself. A 41 percent hit rate at close range over eighty
minutes, and twelve hits given for every one taken.

---

## ⭐ Three Spaniards, not one

Built 2026-10-07. Until now every run drew the same galleon with a random name
painted on her. Now she is one of three real ships, drawn at random, and they
differ in kind rather than in numbers. You cannot tell which until you close
her: at over 1250 yards she is just "a sail", inside that you get her trim, and
inside 560 yards you read her name and her character.

| | Santa Ana, 1587 | Encarnacion, 1709 | Covadonga, 1743 |
|---|---|---|---|
| what she is | the fat one | the clean prize | she means to take YOU |
| guns a side | 4 | 6 | 8 |
| her reload | 13 to 17s | 9 to 12s | 8 to 11s |
| punishment she takes | **1.55x** | 0.80x | 1.15x |
| chests in her | **190** | 105 | 125 |

Measured with `__dev.duel(110)`, six to eight runs a cell. Win rate, length of
the duel, and how much of your hull it costs:

Re-measured 2026-10-07 after Drake's ship was made survivable (see below):

| | Santa Ana | Encarnacion | Covadonga |
|---|---|---|---|
| **Golden Hind** 1579 | 8/8 · 103s · 28% | 8/8 · 54s · 49% | 6/8 · 81s · 71% |
| **Desire** 1587 | 6/6 · 77s · 16% | 6/6 · 44s · 33% | 6/6 · 55s · 55% |
| **Duke** 1709 | 6/6 · 85s · 15% | 6/6 · 37s · 32% | 6/6 · 61s · 57% |
| **Centurion** 1743 | 6/6 · 60s · 11% | 6/6 · 25s · 15% | 6/6 · 39s · 35% |

### Drake's ship was too hard, and the fix is not a stouter hull
It lost to the Covadonga **six times out of six** and cost 80% of its hull
against the Encarnacion. Raising its hull would have made the captain screen
lie again, since the Golden Hind is advertised at Hull 2 of 5.

Instead every class now carries a **`targetK`**: how big a mark she makes. A
Spanish gun crew hits a 24-yard Tudor galleon far less often than a 48-yard
two-decker, so the small ship survives by being small, not by pretending to be
stout. Golden Hind .60, Desire .74, Duke .88, Centurion 1.0.

And **`lootK`**: Drake's people were the best boarders in the game, which
PLAN.md always said and nothing implemented. The chests come over his rail at
1.5x, which shortens his time alongside and so buys him a longer head start on
the Begona.

⭐ **The loot lesson lands hardest on the Santa Ana**: you fill your 36 chests
and leave **154** in her. That is Cavendish's "500 tunnes of goods in her", in
the mechanics.

⚠ A bug this found, worth remembering: rig damage was capped at 1.0 while the
Santa Ana's strike threshold is 0.75 x 1.55 = **1.16**. She was literally
unbeatable and won eight duels out of eight before the cap was raised. Any
future `rig` above 1.33 would have done the same thing silently.

Force one for testing with `__dev.setPrize("covadonga")`.

---

## ⭐ The ambush: the watch on the Vigia

Built 2026-10-07. Before this the wait phase had no teeth at all: the HUD told
you to lie quiet and nothing whatever happened if you did not.

The mechanic is not invented. The hill above the anchorage is really called
*Vigia*, which is Spanish for lookout, and it is marked that way on the charts
(Findlay puts it at 527 ft, the Hydrographic Office at 627; they disagree).
Anson, 1748, printing the galleon captain's standing orders out of captured
Spanish papers:

> "there is besides care taken at Cape St. Lucas to look out for any ship of the
> enemy, which might be cruising there to intercept her"

and the captain is to send his launch ashore with twenty armed men to bring back
"intelligence whether or no there are enemies on the coast". Only if he has
nothing to fear is he "directed to proceed for Cape St. Lucas".

⭐ **ONLY ROGERS 1709 AND ANSON 1743 FACE HIM.** Aodhan's call, 2026-10-07, and
it fits the record better than having the watch always on: Schurz has the
viceroy ordering the cape's signal-and-refreshment system only **after 1734**,
when Montero's galleon came in to Bahia San Bernabe with one day's water left.
So there is nobody on the hill in Drake's day or Cavendish's, and the ambush
orders say so. The hill is not drawn as a manned post, and no meter appears.

This also gives the four captains a real era ramp, which the game did not have
before: the early captains have the weakest ships and an empty shore, and the
late ones have the best ships and a shore that is watching them.

**How it plays.** It is your CANVAS he sees, not your hull, and he only sees you
in open water. The bay east of the ridge is dead ground. Fill the bar and the
signal fires go up, she never closes the land at all, and you have thrown away
the only advantage you ever had.

| What you do | What it costs |
|---|---|
| Lie in the bay, any canvas | he never sees you, but the cape blankets your wind |
| Short sail out to the point | safe (bar peaks about 0.35), and you are doing **4.1 kn** when she commits |
| Half sail | bar peaks about 0.67, **5.9 kn** |
| Full sail | bar peaks about **0.82**, and you are doing **7.8 kn** |
| Dawdle in his water under full sail | spotted in **12 seconds** |

That trade is the ambush: speed at the moment she commits, bought with the risk
of being seen. Measure any change with `__dev.vigiaTest(canvas, inOpen)`.

⚠ Two bugs this introduced and which are fixed: a warned galleon never comes
within sighting distance, so the phase machine used to strand the player in the
ambush forever; and she steers wide of her waypoints when warned, so testing the
UNSHIFTED mark left her circling a point she was deliberately avoiding and she
never ran out to the escape line.

---

## ⭐ The second Spaniard: you are not meant to beat her

Built 2026-10-07. The Begona used to be a slightly bigger galleon you could
batter down like any other. She is now the thing Rogers actually met.

The lesson of this ship is not "she has more guns". It is a **penetration
failure**. Rogers put about five hundred six-pound shot into her hull for two
dead men in her tops and a shot-away mizzen yard, and diagnosed it himself:
Manila-built timber "will not splinter", her sides "much stronger than we build
in Europe". His people stopped loading bar and partridge because "the Ship's
Sides were too thick to receive any Damage by it".

So **sixteen percent** of your shot's effect gets through her, and the game says
so out loud: "Your shot will not go through her sides." Measured, fighting her
with the Desire: four broadsides in, her rig is at **0.051 of the 0.75** needed
to make her strike, and she has killed you nearly three times over.

**The escape is a race, and the stake is your greed.** The real variable is not
speed, it is your head start, and the head start is bought with loot time.
Measured at a fixed NW 15 kn, casting off with:

| Chests taken (of 36) | She is astern by | Chase lasts |
|---|---|---|
| 12 | 721 yd | 29s |
| 24 | 454 yd | 68s |
| 36, a full hold | 235 yd | 88s |

Every chest is distance. That is Cavendish's five hundred tons as a mechanic.

⚠ A bug of my own this exposed: `kFwd` in the physics is quadratic **drag**,
not speed, so terminal speed goes as the square root of `sail/kFwd`. Every
`speedK` I wrote was therefore **inverted**, and the Santa Ana, flagged as the
slow fat one, was the fastest of the three. Corrected with `kFwdForSpeed()`,
which divides by k squared. The three prizes now make 6.23, 7.19 and 6.76 knots
in the order the table says they should.

---

## ⚠ Declared departures

Flagged, not hidden. Each is a deliberate choice for play.

1. **⚠⚠ THE PRIZES ARE ARMED AND THE REAL ONES WERE NOT.** This is the big one.
   Both famous prizes were unarmed, and both say so from their own side under
   oath. The Santa Ana: her master Tomas de Alzola and Antonio de Sierra declared
   "la nao no llevaba artillería ni otras armas", and her sailors fought with the
   pump irons and the ballast stones. Drake's prize, the Nuestra Senora de la
   Concepcion: her master San Juan de Anton swore he "did not carry artillery or
   arms" and so "could not make any resistance". In this game every Spaniard
   shoots, because a turkey shoot is not a game. ⚠ The Fernandez Duro citation
   for the Alzola declaration has not been checked against the volume directly;
   it came through this project's verification pass, not from our own copy.

2. **Four captains, one cape.** Only TWO of the four were ever at Cabo San Lucas:
   Cavendish in 1587 and Rogers in 1709. Drake took a Peru silver ship off Cape
   San Francisco, on the Ecuadorian coast, about 150 leagues from Panama, and she
   was not a Manila galleon at all. Anson took the Covadonga off Cape Espiritu
   Santo in the Philippines. The brief card's "where the English lay for her
   twice in life" is exactly right, and two of the four ships you can sail are in
   the wrong ocean.

3. **One repulse became the lesson, not two.** PLAN.md used to say the Santa Ana
   threw Cavendish's boarders back twice. Pretty describes ONE boarding, repulsed
   once, at a cost of 2 English dead and 4 or 5 hurt, then two further GUNNERY
   encounters. His own marginal notes number them. The game keeps the lesson
   (soften her before you board) with the true count.

4. **The wind.** The game blows NW. Two period observers at this anchorage say
   otherwise: Pretty had "the windes hanging still Westerly" through the whole
   1587 ambush, and Shelvocke in 1721 had SSW to W by N. NW is the general
   prevailing along outer Baja and it is what makes the chase work, so it stays.

5. **Five points is wrong.** The brief says "a square rig will not lie within
   about five points of the wind". Falconer gives six points for square-riggers
   and says five is the figure for sloops and small craft. The ships in
   `ships.js` lie at 55 to 60 degrees, which is handier than life. Kept, because
   a game where you cannot tack is not a game. The relative ranking, galleon
   worst, is correct.

6. ~~**The flags are wrong for two of the four ships.**~~ ✅ **FIXED
   2026-10-07.** `ships.js` used to draw St George's cross for all four English
   ships, which is 36 years out of date for Rogers's Duke and 72 for Anson's
   Centurion. Now:
   - **george** for Drake 1579 and Cavendish 1587, which was always right.
   - **redensign** for Rogers 1709 and Anson 1743: a red field with the
     pre-1801 union in the canton. A privateer's flags were fixed by the
     Proclamation of July 1694, and the union went into the ensigns in 1707.
   - **a broad pendant** at the Centurion's main masthead, long and narrow with
     the union at the hoist. Anson was a commodore and it is the single most
     characteristic flag his ship wore. No other ship in the game flies one.

   ⚠ Note the title screen `index.html` had this RIGHT all along, with its own
   `texRedEnsign` and `paintUnion`. It was the in-game ships that were out of
   step, so this is consistency rather than a new claim.

   ⚠ Still unverified, and no longer asserted in the code comments: whether the
   Cross of Burgundy is "what Spanish ships wore at sea in all four eras". The
   game flies it as a reasonable period choice, not as a documented fact.

7. **Time is compressed**, as in doghole. The knots in the HUD are true knots.
   The real chase ran "some 3 or 4 houres" and the real fight five or six.

8. **The bay outline, soundings and distances are invented** at plausible scale,
   hung on the three period soundings above. ⛔ Corrected 2026-10-07: `cape.js`
   used to say "Anson's 1742 plan of the bay exists". It does not. Anson was
   never at this cape, and his 1748 edition's own binder's list of all 31 plates
   gives the harbour plan as Chequetan, on the Mexican mainland.

---

## The numbers the game can use

All from Pretty, in Hakluyt vol. XI, unless noted.

| | |
|---|---|
| The Santa Ana | "thought to be 700 tunnes in burthen", and the king of Spain's own ship, "Admiral of the south sea" |
| The chase | "some 3 or 4 houres, standing with our best advantage and working for the winde" |
| The fight | she struck "within 5 or 6 houres fight" |
| Why she struck | "being in hazard of sinking by reason of the great shot which were made, wherof some were under water" |
| Your boarding party | "not past 50 or 60 men at the uttermost in our ship" |
| The treasure | "an hundreth and 22 thousand pezos of golde", plus silks, satins, damasks, musk, wines |
| Prisoners | 190 men and women set ashore, given victuals, their own sails for tents, and planks to build a bark |
| ⭐ The loot lesson | he burned her with "500 tunnes of goods in her" still aboard, because he could not carry it |
| Rogers' prize | the Encarnacion, 20 guns, 193 men |
| The one you do not touch | the Begona, 900 tons, able to carry 60 guns, about 40 mounted plus 40 patereroes, over 450 men |
| The Covadonga, measured | Anson had her surveyed: 124 ft on the gun deck, 38 ft 2 in broad. The Centurion was 144 ft 1 in. ⚠ Walter's famous line that the galleon was "much larger than the Centurion" is not supported by Anson's own carpenter |

---

## Material not used yet

The research turned up more good mechanics than the design doc invented. Banked
here rather than lost.

- **⭐⭐⭐ THE BREAD TIMER.** Rogers' wait ended not because of an enemy but because
  of biscuit. On 20 December 1709 he worked out in his journal that he had 70
  days' bread, needed 9 to refit and 50 to Guam, and the council voted to abandon
  the station. "At signing this in the Committee we all looked very melancholy
  and dispirited." The galleon appeared the next morning. A victualling meter
  that forces you to give up one beat before she comes is better drama than a
  countdown.
- **⭐⭐ THE BEGONA CANNOT BE HURT BY YOUR SHOT, not merely high HP.** Rogers put
  500 six-pound shot into her for two dead men and a shot-away mizzen yard.
  Manila-built timber "will not splinter", her sides "much stronger than we build
  in Europe", and the English stopped loading bar and partridge because "the
  Ship's Sides were too thick to receive any Damage by it". The walk-away level
  should teach a penetration failure, not a big health bar.
- **⭐⭐ COMMANDER DEGRADATION.** Rogers was shot through the jaw on day one and
  gave his orders in writing; on day three a splinter took out part of his heel
  and he finished the action on his back on the quarterdeck. Better than a health
  bar.
- **⭐⭐ DRAKE FOUGHT WITH LONGBOWS.** Anton's deposition describes "many arrows"
  into her side and "about forty archers" going up the shrouds from the pinnace.
  Archers, not musketeers. Nothing models Elizabethan sea-archery.
- **⭐⭐ FALSE COLOURS, AND THE ASYMMETRY IS FREE.** Rogers decoyed his galleon
  under a FRENCH ensign, France being Spain's ally in that war, and "fired a Gun,
  (which the Stranger answer'd)". Meanwhile Spain's own Ordenanzas of 1748 make
  fighting under false colours a dismissal offence. The privateer may bluff; the
  Spaniard legally may not.
- **THE FAILURE STATE IS A SIGNED MINUTE.** Rogers' committee voted in writing to
  give up the Begona, undersigned by Rogers, Courtney, William Dampier and five
  others. A level that ends with your own officers voting to quit beats a stern
  chase.
- **THE LOOT SCREEN IS THE DANGER.** On 8 November 1587, dividing the treasure,
  "many of the company fell into a mutinie against our Generall, especially those
  which were in the Content". The Content was left astern four days later and
  never seen again.
- **FIRE AS A WEAPON.** A fire-ball from the Begona's top blew up a chest of arms
  on the Duke's quarterdeck; stink-pots set the Marquis alight and she "stunk
  several Days intolerably". The Covadonga's netting mats caught fire and blazed
  "half as high as the mizen-top", and Anson feared not for the enemy but for the
  money.
- **ANSON'S MARKSMANSHIP SCHOOL.** His crew were taught only the fastest way to
  load, then "constantly trained to fire at a mark, which was usually hung at the
  yard-arm", with "some little reward given to the most expert". Walter makes it
  the explicit cause of the casualty ratio. A training-investment mechanic with a
  documented payoff.
- **SHE CAUGHT HER WATER IN THE RAIN.** Jars hung in the shrouds and mats rigged
  sloping along the gunwale, draining through a split bamboo. It never failed.
  Kills the "crew on short water" trope the galleon comment in `ships.js` uses.
- **THE FRAILES LOOKED LIKE FRIGATES.** Cabrera Bueno, 1734: three white rocks
  "que parecen Fragatas a la Vela", which fooled the ship San Geronimo in 1699. A
  false-contact mechanic with a date and a ship's name on it.
- **SPAIN REMEMBERED 1587 AS DRAKE.** Torquemada attributes the whole raid to "el
  corsario Francisco Draque". A ready-made fog-of-war beat.
- **THE DATES DISAGREE BY TEN DAYS AND BOTH ARE RIGHT.** Pretty dates the capture
  4 November 1587; the Spanish declarations say they raised the cape on the 14th.
  That is the Julian/Gregorian gap exactly. Two archives, two calendars, one day.

---

## Open, and honest about it

- The wind at the cape needs a pilot before the game asserts one. See departure 4.
- The Fernandez Duro citation for the Santa Ana's armament has not been checked
  against the volume itself.
- Whether any period PLAN of this bay exists is unresolved. Anson has none,
  Rogers promises only coastal charts, and Shelvocke wrote a description because
  he had no chart to point at. The vault holds no chart of Cabo San Lucas.
- The verification pass recorded **37 null results** alongside its 59 claims.
  They are in `sources-raw-verification-2026-10-07.json` and they are findings,
  not gaps.
