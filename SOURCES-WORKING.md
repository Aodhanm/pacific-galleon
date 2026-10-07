# PACIFIC GALLEON: sources working file

Scratch ledger for the sources pass begun 2026-10-07. Verified findings land here
first; `GAME.md` is assembled from it. Nothing goes into GAME.md that is not in
here with a locator and a retrieval proof.

Verdicts: CONFIRMED · PARTLY · REFUTED · UNVERIFIED (a null is a finding, not a gap).

---

## Texts fetched and proved

| Source | Copy used | How the retrieval was proved |
|---|---|---|
| Walter, Richard [and Benjamin Robins], *A Voyage Round the World in the Years MDCCXL, I, II, III, IV* (London, 1748) | IA `gri_33125011256381` (Getty Research Institute, 1748 first edn, 546 images) AND Project Gutenberg ebook 47130 | IA copy's title page reads "In the Years MDCCXL, I, II, III, IV" with imprint "Mdccxlviii"; Gutenberg header carries the same title. The two texts agree word for word on every passage quoted below, so the quotations are not OCR artefacts. |
| Rogers, Woodes, *A Cruising Voyage Round the World* (London, 1712) | IA `10467991bsb` (Bayerische Staatsbibliothek) | Title page transcribes as "By Captain WOODES ROGERS" with the 1712 London imprint of A. Bell and B. Lintot. ⚠ OCR on this copy is POOR. Nothing is quoted from it below as verbatim; a cleaner copy is needed before any Rogers wording ships. |

---

## CONFIRMED, and stronger than the game's version

### The cape is the ambush station, and a period source says so outright
Anson's compilers, writing from captured Spanish papers, on Cape San Lucas:

> "this being a station where she is constantly expected, and where she has been
> often waited for and fought with, though generally with little success"

Walter, *Voyage Round the World* (1748), ch. on the Manila ship (Gutenberg 47130,
line 8828; 1748 edn p. 244).

**Game impact:** this is the premise of the entire game in one period sentence, and
it belongs on the brief card. Note the sting in the tail: "generally with little
success". The game should not pretend this was easy.

### The refreshments, and why she closes the land at all

> "there are refreshments, as fruits, wine, water, etc., constantly kept in
> readiness for her"

Same passage. The Jesuit mission "lies just within Cape St. Lucas".

**Game impact:** confirms the watering/refreshment premise the whole ambush rests on.

### Usual arrival at Acapulco

> "The most usual time of the arrival of the galeon at Acapulco is towards the
> middle of January"

**Game impact:** dates the scenario. The game is silent on season; it need not be.

---

## CORRECTED: the game's track is wrong in an interesting way

The game's brief says the galleon "is coming down the outer coast". Anson says she
deliberately did NOT:

> "they steer to the southward without endeavouring to approach the coast, till they
> have run into a lower latitude, for as there are many islands, and some shoals
> adjacent to California, the extreme caution of the Spanish navigators renders them
> very apprehensive of being engaged with the land. However, when they draw near its
> southern extremity, they venture to hale in, both for the sake of making Cape St.
> Lucas to ascertain their reckoning"

She crossed the Pacific "in the latitude of 40 or 45 degrees", found the floating
plant the Spaniards called *Porra*, corrected her longitude by it "without ever
coming within sight of land", and only closed the coast at the very bottom of Baja.

**Game impact:** this makes the game BETTER, not worse. The reason the ambush
happens at this cape and nowhere else is that the cape is the one place on five
thousand miles of ocean where she is obliged to come within reach of the land.
The brief should say that. "Coming down the outer coast" throws the point away.

---

## DOCUMENTED MECHANIC THE GAME DOES NOT MODEL: the shore watch

> "there is besides care taken at Cape St. Lucas to look out for any ship of the
> enemy, which might be cruising there to intercept her"

> "the captain of the galeon is ordered to fall in with the land to the northward of
> Cape St. Lucas, where the inhabitants are directed, on sight of the vessel, to make
> the proper signals with fires. On discovering these fires, the captain is to send
> his launch on shore with twenty men well armed, who are to carry with them the
> letters from the convents at Manila to the California missionaries, and are to
> bring back the refreshments which will be prepared for the ship, and likewise
> intelligence whether or no there are enemies on the coast. If the captain finds,
> from the account which is sent him, that he has nothing to fear, he is directed to
> proceed for Cape St. Lucas"

**Game impact:** the ambush phase currently has no teeth. The HUD tells you to "lie
quiet" and nothing whatever happens if you do not. Here is the documented basis for
making it matter: there is a shore lookout, it signals her with fires, she sends a
launch in for intelligence before she commits, and if she is told there are enemies
on the coast she does not come on. Being seen should cost you the prize. This is a
better mechanic than any the plan invented, and it is in a period source.

---

## REFUTED: one of our own notes is wrong

`cape.js` says, in its header: "pull the period charts (Anson's 1742 plan of the bay
exists) and redraw from them."

**There is no Anson plan of Cabo San Lucas.** Both sides checked:

1. Anson's squadron was never at Cabo San Lucas. In 1742 it was in the South Sea;
   the Centurion's Mexican station was off Acapulco, and she careened at Chequetan
   (Zihuatanejo) on the mainland.
2. The 1748 edition's own "Directions to the Bookbinder, for placing the
   Copper-Plates" lists all 31 plates. There is no Cabo San Lucas among them. The
   harbour plan is plate 31, "A plan of the harbour of Chequetan", and the text
   confirms it: "A plan of the harbour itself is represented in the annexed plate"
   (1748 edn, Chequetan chapter). Plate 27 is "The form of cruising off Acapulco".

The period authority for the anchorage at Cabo San Lucas is **Woodes Rogers**, who
lay there in 1709 and calls it **Port Segura** ("at Anchor in Port Segura on
California", repeatedly, in his journal headings). ⚠ Rogers' title page promises
"Maps of all the Coast, from the best Manuscript Draughts", which is coastal charts,
NOT a harbour plan. Whether any period plan of this bay exists is still OPEN: check
Shelvocke (1726), who also lay at Puerto Seguro, and the Spanish derroteros.

**Action:** correct the `cape.js` header comment. It currently sends a future reader
to a chart that does not exist.

---

## OPEN / still to resolve

- A period plan of Cabo San Lucas bay: does one exist at all? (Shelvocke 1726, Spanish
  derroteros, 19th-c. US Hydrographic Office charts as the fallback authority.)
- Clean text of Rogers 1712 for verbatim quotation. The IA Bavarian copy's OCR is not
  fit to quote from.

---

## Rogers 1709: two finds that change the ambush phase

Copy used for these: IA `cruisingvoyagero00roge_0`, the 1928 reprint of the 1712
text, whose OCR is far better than the Bavarian copy of the original. ⚠ Still OCR:
it mangles "Manila" to "Alanda" and "Marquiss" to "Jflarquiss", so WORDING BELOW
MUST BE CHECKED AGAINST A PAGE IMAGE before it is quoted in the game.

### Rogers names the harbour after Cavendish
On 21 December 1709 the Duke made "the best of our Way into the Harbour call'd by
Sir Tho. Cavendish Port Segura". (Rogers, *Cruising Voyage*, journal entry 21 Dec.
1709.)

**Game impact:** this is the period source for the brief's claim that the English
"lay for her twice in life" at this cape. Rogers himself makes the link, and he
makes it by the place-name. ⚠ Note what is and is not established: Rogers ATTRIBUTES
the name to Cavendish. That Cavendish in fact gave it is Rogers' claim at 122 years'
remove and is NOT independently verified here.

### The English kept a shore lookout too
Laid up refitting and out of the chase, "He placed two men on an adjoining hill-top
to signal as soon as the Spanish ship was sighted". (Manwaring's editorial
introduction to the 1928 edition, summarising the journal; the journal entries
themselves are at the same date, late Dec. 1709.)

**Game impact:** pair this with the Spanish shore watch in Anson and the ambush
phase writes itself. Both sides had eyes ashore. The game currently has neither.

### The council chose this cape deliberately
The majority of the council thought "Cape St. Lucas the properest Place to lie for
the Manila Ship bound for Acapulco", over Rogers' own proposal to split the squadron
between two stations for "2 Chances for the Prize". (Committee minute, Tres Marias,
Oct. 1709.)

**Game impact:** confirms the cape was chosen on purpose as THE station, and gives
the Rogers level its historical shape: he wanted to split and was overruled.

---

## THE PILOT FOR THE BAY: Shelvocke 1726

George Shelvocke, *A Voyage Round the World by the Way of the Great South Sea*
(London, 1726), lay at the same anchorage in 1721 and printed a sailing description
of it. IA copy `avoyageroundwor00schegoog`; retrieval proved by the title page,
"By Capt. George Shelvocke, Commander of...". ⚠ Google scan, OCR is poor: every
wording below needs checking against a page image before it is quoted in the game.
This is the Cabo San Lucas equivalent of what Davidson's *Coast Pilot* gave doghole.

What Shelvocke gives us, in substance:

| In the game | What Shelvocke says |
|---|---|
| The bay lies east of the Land's End ridge | Puerto Seguro "is about 2 leagues to the North eastward of Cape St. Lucas, which is the Southermost land of California, and is almost right under the tropick of Cancer" ⚠ see the problem below |
| `cape.js`: "DEEP WATER CLOSE TO: a submarine canyon heads almost at the beach here, so the bank is steep" | CONFIRMED by a 1726 pilot: anchor on "a bank of land on the Northern side as you go in, on which you may anchor from 16 to 8 fathoms", but "take care that you do not fall too near the Southern side, where there is very deep water; for the bank shelves away very fast from the Northern shore" |
| Depth field and the anchorage | he rode in 13 fathom, not above half a mile from the shore, moorings laid SE and NW with a good scope of cable |
| The bay is sheltered from the west, open to the east and south-east | he "lay open to the sea from the E. by N. to the S. E. by S."; during his stay the wind held "from the S.S.W. to the W. by N. which render'd it a commodious harbour" |
| The shore the player sees | from the SE round to the W "it is rocky and mountainous"; from the W to N by W "is low, cover'd with bare trees"; from N by W to NNE "there are three different high mountains of the same appearance and bigness with one another" |

**Second independent source for the Cavendish attribution:** Shelvocke, like Rogers,
calls it "Puerto Seguro, so call'd by Sir Thomas Cavendish". Two English captains,
1709 and 1721, independently name Cavendish as the author of the name. That is
good evidence for the game's "the English lay for her twice in life", though still
not proof that Cavendish himself gave the name.

### ⚠ A PROBLEM THE GAME MUST RESOLVE
Shelvocke puts Puerto Seguro **about two leagues (roughly six miles) north-east of
Cape St. Lucas**. `cape.js` puts the ambush bay **immediately east of Land's End**,
which is modern Bahia San Lucas, at the cape itself. Those may not be the same water.
Either Shelvocke's distance is a loose estimate or the game has the wrong bay.

Do NOT resolve this by inference. It needs either a period chart or a modern
hydrographic chart read against Shelvocke's bearings. Flagged, not answered.

### Does a period plan of this bay exist?
Still OPEN, and now leaning NO for the English sources: Anson's plate list has none
(see above), Rogers promises only coastal "Maps ... from the best Manuscript
Draughts", and Shelvocke's text gives a written description precisely BECAUSE he had
no chart to point at. If nothing turns up in the Spanish derroteros, the honest
fallback is a 19th-century US Hydrographic Office chart or the Mexican west-coast
sailing directions, cited as such, with the period descriptions laid over it.

---

# CAVENDISH AND THE SANTA ANA: the core level, checked against the eyewitness

Source: Francis Pretty, "The admirable and prosperous voyage of the Worshipfull
M. Thomas Candish", in Hakluyt, *The Principal Navigations* (MacLehose edn, 1904),
vol. XI, pp. 323-327. IA copy `principalnavigat11hakluoft`; retrieval proved by the
volume's own title page ("THOMAS CAVENDISH ... RICHARD HAKLUYT") and by the running
heads "CANDISH'S CIRCUMNAVIGATION A.D. 1587". OCR is good but spaced; wording below
is reproduced as the scan has it.

## ⛔ REFUTED: the mechanic the whole level is built on has no source

PLAN.md: "the *Santa Ana* ... had her great guns struck below for cargo: she cannot
batter you, but she is full of men."

**Pretty never says this.** He does not mention her armament at all. What he describes
is her people fighting off the boarders with hand weapons and stones:

> "stood close under their fights, with lances, javelings, rapiers, & targets, & an
> innumerable sort of great stones, which they threw overboord upon our heads and
> into our ship so fast and being so many of them, that they put us off the shippe
> againe, with the losse of 2 of our men which were slaine, & with the hurting of 4 or 5"

So the EFFECT the game models is right: in this action she never fires a great gun,
and she is beaten by gunnery and defended by men. The REASON the plan gives for it
is not in the eyewitness. This is the trap exactly: the cheap reading was also the
one we wanted.

**What to do:** keep the mechanic, change the justification. Say what the source
says, which is that her defence was close fights, hand weapons and stones. Do not
assert the guns were struck below unless a source for it turns up.

## ⛔ REFUTED: "she repelled Cavendish's boarders twice"

PLAN.md says twice. Pretty describes **one** repulsed boarding, then two further
gunnery encounters. His own marginal notes number them "The second encounter" and
"The third encounter", and both are gunfire:

> "we new trimmed our sailes, and fitted every man his furniture, and gave them a
> fresh encounter with our great ordinance and also with our small shot"

Boarded once, thrown back once, then pounded twice more. The level should teach
"soften her before you board", which is still the right lesson, but the number is one.

## ✅ CONFIRMED, with figures the game can use

| Game needs | Pretty says |
|---|---|
| How long the fight ran | she struck "within 5 or 6 houres fight" |
| How long the chase ran | "we gave them chase some 3 or 4 houres, standing with our best advantage and working for the winde" |
| Her tonnage | "called the S. Anna, & thought to be 700 tunnes in burthen", and she was "Admiral of the south sea", the king of Spain's own ship |
| How she struck | "being in hazard of sinking by reason of the great shot which were made, wherof some were under water", she "set out a flagge of truce and parled for mercy" |
| Your boarding party is TINY | "being not past 50 or 60 men at the uttermost in our ship" |
| The treasure | "an hundreth and 22 thousand pezos of golde", plus "silkes, sattens, damasks, with muske", victuals, conserves and wines. A marginal note prices a pezo at 8s. |
| Prisoners put ashore | "the whole company of the Spaniardes, both of men and women to the number of 190 persons were set on shore", given victuals, their own sails for tents, and planks to build a bark |
| ⭐ THE LOOT LESSON, exactly | on 19 November he "caused the kings shippe to be set on fire, which having to the quantitie of 500 tunnes of goods in her we saw burnt unto the water" |

**That last line is the game's capacity mechanic in a period source.** He burned her
with five hundred tons of cargo still in her because he could not carry it. The win
card should quote it.

⚠ **C-7 is NOT settled.** Pretty, an English eyewitness, says she burned to the
water. There is a well-known Spanish counter-tradition that she was salvaged and got
to Acapulco. That is a question for the Spanish side of the record and is NOT
resolved here. Do not state either version as fact in the game yet.

## ✅ CONFIRMED: the ambush phase is real, and it is three weeks long

> "The 14 of October we fell with the cape of S. Lucar ... wee watered in the river
> and lay off and on from the saide cape of S. Lucar untill the fourth of November"

He raised the cape on 14 October and lay off and on until 4 November. The game's
"wait" phase lasts seconds. The real thing was **three weeks**, and he watered in
the river while he waited, which is the same reason the galleon came in.

The sighting itself, at 7 to 8 in the morning, from the maintop, by the trumpeter:

> "espied a sayle bearing in from the sea with the cape"

She came in **from seaward toward the cape**, which is the geometry the game draws.

## ⚠ THE WIND IS PROBABLY WRONG

The game blows **NW 17 kn**. Two independent period observers at this anchorage say
otherwise:

- Pretty, Oct-Nov 1587: "had the windes hanging still Westerly"; and when Cavendish
  sailed on 19 November the wind "was come about to East northeast".
- Shelvocke, 1721: during his stay the wind held "from the S.S.W. to the W. by N."

Neither is north-west. Both are westerly or south of it. ⚠ This does NOT yet prove
the game wrong: these are two spot observations in one season each, and NW is the
general prevailing along outer Baja. But it needs a pilot or sailing directions
before the game asserts a wind, because the wind direction is the chase.

## ⭐ A PERIOD DESCRIPTION OF LAND'S END, and it is the game's own drawing

> "the cape of S. Lucar, which is on the West side of the point of California ...
> which cape is very like the Needles at the isle of Wight"

The Needles are a file of sharp chalk stacks running out from the Isle of Wight into
the sea. That is precisely what `cape.js` draws: a narrow ridge running out to the
point with outlying rocks at the end. An Elizabethan eyewitness reaching for the
nearest English comparison gives us the shape of the headland for free.

## ⛔⛔ REFUTED: Cavendish did not name the harbour

Rogers (1709) and Shelvocke (1726) both call it "Puerto Seguro, so call'd by Sir
Thomas Cavendish". **Cavendish's own expedition says the name is Spanish and was
already there.** Twice:

> "within the said cape is a great bay called by the Spaniards Aguada Segura"
> "wee went into an harbour which is called by the Spaniards, Aguada Segura, or
> Puerto Seguro"

The eyewitness of 1587 beats two English captains repeating a tradition 122 and 134
years later. Supersede the note I wrote above under Rogers.

## ⚠⚠ WHICH BAY? An unresolved toponym problem

This needs flagging hard, because the vault has been burned by exactly this before
(see the Bodega/Tomales case, 2026-09-25).

- Pretty puts the bay **at the cape**: "within the said cape is a great bay".
- Shelvocke puts Puerto Seguro **about 2 leagues (roughly 6 miles) north-east** of
  Cape St. Lucas.
- Pretty's bay has **"a faire fresh river"** falling into it, which they watered from,
  and around which "many Indians use to keepe".

Modern Bahia San Lucas, immediately east of Land's End, where `cape.js` puts the
ambush, **has no river**. The nearest permanent watercourse is the Rio San Jose, at
San Jose del Cabo, roughly twenty miles up the coast to the north-east.

So the three pieces of evidence do not sit together, and the game may be drawing the
wrong bay. **Do NOT resolve this by inference.** It needs a chart read against
Shelvocke's bearings and Pretty's river. Until it is resolved, the game should not
claim the anchorage is Bahia San Lucas.

## ✅ Latitude, as a period control
Pretty puts the headland "in 23 degrees and two thirds to the Northward", i.e.
23 deg 40 min N. Cabo San Lucas is in fact about 22 deg 53 min N, so he is some
47 minutes high. Worth knowing before trusting any period position on this coast.

## Also recovered, not currently in the game
- The *Content*, Cavendish's consort, was left astern at the road, "which was not as
  yet come out of the road ... we lost her companie and never saw her after." The
  second English ship simply vanished. The game has no consort for the player.
- Among the prisoners Cavendish kept were "two yong lads borne in Japon" and "3
  boyes borne in the isles of Manilla".
- On leaving he "gave them a piece of ordinance and set sayle joyfully homewardes".

---

## ⭐ CAVENDISH'S OWN SAILING LOG: a second document in the same volume

Hakluyt vol. XI also prints Cavendish's navigational discourse, with a table of the
depths his ships anchored in. Same IA copy, pp. 369 and 380 or thereabouts.

The dated log of the ambush, from the navigator's side rather than the narrator's:

> "The 14 day of October we had sight of the Cape of California."
> "The 15 day of October we lay off the Cape of S. Lucas, and the 4 day of November
> we tooke the great and rich ship called Santa Anna, comming from the Philippinas:
> and the 5 day of November we put into the port of S. Lucas, where we put all the
> people on shore, and burnt the Santa Anna: and we ankered in 12 fadoms water."
> "The 19 day of November we departed from the port of S. Lucas."

And from the anchorage table:

> "You may anker in the port of S. Lucas on the Cape of California in 12 fadoms
> water: and a Southeast winde is the woorst."

### Two things the game can use immediately

1. **The depth is settled.** Twelve fathoms where they lay, which agrees with
   Shelvocke's "I rode [in] 13 fathom" and sits inside his 8-to-16-fathom bank. The
   depth field in `cape.js` is currently invented; here are three period soundings
   to anchor it on.

2. **⭐ THE HAZARD IS A SOUTH-EAST WIND.** Cavendish: "a Southeast winde is the
   woorst." Shelvocke, independently, 134 years later: he "lay open to the sea from
   the E. by N. to the S. E. by S." Two sources, same answer. The ambush berth is
   snug in anything westerly and a trap in anything from the south-east.

   The game has no weather hazard in the wait phase at all. This is the documented
   one, and it is the Fort Ross lee in reverse: in doghole the bluff gave you shelter
   and the game modelled it; here the bay gives you shelter from exactly three
   quarters of the compass and from the fourth it will put you on the beach.

### It also bears on the which-bay problem
Cavendish's log calls the anchorage "the port of S. Lucas **on the Cape of
California**", which pulls toward the cape itself and against Shelvocke's "2 leagues
to the North eastward". Set against that, Pretty's "faire fresh river" still has no
modern counterpart at the cape. ⚠ Recorded, still NOT resolved. The river is the
piece that does not fit, and it should be chased before the map is redrawn.

---

## ✅ WHICH BAY: RESOLVED, and the game has it right

Found in the vault's own holdings, not online: William Shaler, *Journal of a Voyage
between China and the North-Western Coast of America* (1808), describing the coast
from his own trading voyages. Vault copy:
`~/vault/07 Files/Raw/books/shaler-journal-voyage-between-china-northwestern-coast-1808.txt`.
⚠ Double-column OCR, and the passage appears twice, the second time garbled; the
clean reading is the first.

> "Directly round Cape San Lucas there is a very commodious anchorage, called Puerto
> Segura, where there is very good water. The mission of San Josef is but a short
> distance from this place, but no considerable supplies could be expected there.
> There is safe anchorage directly opposite to the mission, where water is still
> more abundant."

This answers both halves of the problem at once:

1. **Puerto Segura is AT the cape**, "directly round Cape San Lucas". That is where
   `cape.js` puts the ambush bay. Pretty's "within the said cape" and Cavendish's own
   log, "the port of S. Lucas on the Cape of California", agree. Shelvocke's "about
   2 leagues to the North eastward" is the outlier and reads as a loose estimate.
2. **There is water at the cape**, "very good water", which is what Pretty's "faire
   fresh river" was. Shaler also tells us why the question looked confusing: there
   are TWO watering anchorages on this stretch, Puerto Segura at the cape, and a
   separate road off the mission of San Jose a short distance up the coast, where
   water is "still more abundant". The Rio San Jose is the second of those, not the
   first.

**Verdict: three independent navigators (1587, 1587, 1804) put the anchorage at the
cape with fresh water, against one loose distance from Shelvocke (1726). The game's
geography stands.** ⚠ Shaler is writing 217 years after Cavendish, so he confirms
the place, not Cavendish's river specifically.

### Null result, recorded
The vault's map collection (`07 Files/Map Collection`, indexed at
`02 Source Material/historical-map-collection.md`) holds **no chart of Cabo San
Lucas**. The only Baja sheet is the 1823 *Carta esferica de los territorios de la
alta y baja Californias*, at far too small a scale for a harbour. Searched by
filename and by index text. If a harbour plan is wanted it must be acquired.
