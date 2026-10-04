# PACIFIC GALLEON — design plan (v1, 2026-10-03)

Status: **OPEN-WATER SCAFFOLD BUILT AND VERIFIED 2026-10-03** (build
order steps 1-3 partial): square-rig physics with per-class polars,
four player classes + the galleon base, top-down square-rig drawing,
the chase loop (lie in wait, sail on the horizon, pursuit, laid-aboard
card) all working in `play.html`. Verified in-browser: galleon makes
7-8 kn terminal, player ~9, stern-chase closure ~1.7 kn, win card
fires at 45 yd. Next = the Cabo shore (`cape.js`), then chain shot and
the gun phase. Decisions locked with Aodhan 2026-10-03:
**four captains · era levels · manual broadsides · Acapulco finale.**

The engine is DOGHOLE (`~/doghole/`), reused heavily by agreement. Copy,
never modify, the doghole repo. Same look: top-down flat vector, hard
edges, canvas 2D, ES modules, no dependencies.

---

## The premise

The English raiders of the Pacific, 1579–1743, and the richest prize on
earth: the Manila galleon. The heart of the game is Cabo San Lucas, where
the galleon's track down the Baja coast pinches against the land. You lie
in wait, sight her, chase her down using the wind, batter her with
broadsides until she strikes, grapple and board, take as much treasure as
your ship can carry, and get away before the second Spaniard comes down
on you.

**The galleon comes from the NORTH-WEST, running south-east.** She made
landfall high on the California coast and ran down Baja with the NW wind
and the current astern, bound round the cape for Acapulco. So she arrives
with the weather gauge, in her best point of sail, and the ambusher's
problem is real: be faster, or cut the corner at the cape.

## The four captains, four era levels

One scripted scenario per captain, oldest first. Each is built from a
documented action; each teaches one layer of the full loop.

### 1 · DRAKE, *Golden Hind*, 1579 — "The Cacafuego" (tutorial)
Not a Manila galleon and not at Cabo (off South America): the level that
teaches chase and boarding with nothing shooting back. Drake overhauled
the treasure ship over days and took her almost without a fight; the
accounts say he disguised his speed (trailing drags astern) so she never
ran. Mechanic: approach under false colours; the prize does not flee
until you show your hand. One broadside, grapple, board, done.
- Ship: smallest, fastest, points highest, weakest broadside, best
  boarders (loot ticks fastest).

### 2 · CAVENDISH, *Desire*, 1587 — "The Santa Ana" (the classic ambush)
The real Cabo San Lucas action and the core level: wait at the cape,
sight, chase, battle, board, loot, burn her, get out. The *Santa Ana*
was huge and rich and — I believe, VERIFY against the accounts before
this goes in a sourcing table — had her great guns struck below for
cargo: she cannot batter you, but she is full of men. She repelled
Cavendish's boarders twice; he stood off and pounded her for hours until
she struck. So: board too early and you are thrown back with crew
losses; soften her first.
- Ship: the balanced one. Special: the second grapple attempt is
  cheaper (he kept coming).
- The loot lesson: Cavendish could not carry a fraction of what she
  held. Treasure chosen > capacity is left burning on the water.

### 3 · ROGERS, *Duke*, 1709 — "Two Galleons" (the greed level)
The documented two-prize season, and the level the whole detection
mechanic comes from. Take the *Encarnación* (mid-size, ~20 guns, strikes
after a sharp fight) — and from the moment your guns speak, the clock
runs: the *Begoña*, ~900 tons and 40+ guns, is coming down the coast.
She fought off Rogers' entire squadron in life. Engage her and you will
very likely be beaten off with damage; the level is about knowing when
to leave. Echo of doghole's Iversen's: a situation you are meant to
abandon.
- Ship: heavy broadside, slow, toughest hull. Special: the *Dutchess*,
  an AI consort you can signal to engage or stand off (documented; she
  was there).

### 4 · ANSON, *Centurion*, 1743 — "The Covadonga" (the gun duel)
The last and the only pure artillery fight: the *Covadonga* fought back
properly for an hour and a half. Anson's real enemy was scurvy, so the
Centurion is the attrition ship: overwhelming broadside, slowest hull,
and a crew that shrinks on a timer — every minute of the cruise costs
gun crews, so reloads get slower the longer you dither. Find her fast,
kill her quick.
- Setting: open ocean (historically off the Philippines; the game can
  keep it abstract blue water, no cape).

### 5 · FINALE — "The Mouth of the Lion" (⚠ INVENTED, flagged)
Aodhan's fort bombardment, put where a fort really stood: Acapulco,
Fort San Diego (built 1617). A cutting-out raid: slip into the outer
bay, grapple the outbound galleon at her anchor, and bring her out past
the guns. Shore guns are the hazard the player cannot fight, only
position against: hug the wrong side and you are under the battery's
arc. No English captain ever did this — it is the game's one declared
departure, flagged in-game the way doghole flags its entrance buoys.
Unlocked by finishing the four eras; playable with any captain.

## The galleon spawn table (for replay / freeplay later)

The three real prizes ARE the variation Aodhan asked for:
| archetype | model | guns | speed | treasure |
|---|---|---|---|---|
| the fat one | *Santa Ana* 1587 | struck below (musketry + boarders only) | slow | immense |
| the normal prize | *Encarnación* 1709 | ~20 | middling | good |
| the one you don't touch | *Begoña* 1709 | 40+ | fair | you'll never see it |
| the fighter | *Covadonga* 1743 | ~30, fights hard | middling | good |

Freeplay mode (post-v1): random draw from this table, sighted at range —
reading WHICH she is before you commit is the skill.

## What ports from doghole (assessed from the code, 2026-10-03)

| doghole | here | change |
|---|---|---|
| `vessel.js` physics: wind polar, rudder-bites-with-way, leeway, in-irons, current, cargo→mass/draft | all ships, player + AI | per-ship constants table; SQUARE-RIG POLAR (in irons under ~65–70°, best point = quarter/run, worse close-hauled than the schooner) |
| warp/lines code (`v.warp`, `v.lines`, spring + head-swing) | THE GRAPPLE | target is a moving ship; lines part under too much strain |
| cargo slows her (`cargo/CAPACITY`) | treasure weight | identical; loot vs escape speed is already coded |
| `gate.js` polyline lanes + traffic + spotting + contacts minimap | galleon track, Begoña, Acapulco patrol | galleon lane = the coastal track NW→SE round the cape |
| fog visibility pools (`destination-out` mask) | sighting/haze: a sail is a smudge before she is a hull | lighter use; Cabo is not a fog coast |
| phase state machine (cove's 4 phases) | WAIT → SIGHT → CHASE → BATTLE → BOARD → ESCAPE | new phases, same scaffold |
| weather/wind-shift system, HUD, audio engine (synth + clips), wreck sequence, title screen style, `serve_nocache.py`, dev hooks | wholesale | reskin |
| land rendering approach (cove.js) | `cape.js`: Land's End granite, the arch, the beach, desert scrub palette | new geometry + palette, same technique |

## Genuinely new systems

1. **Gunnery, manual broadsides.** Port/starboard fire keys, per-side
   reload timers, broadside arcs. Shot types: ROUND (hull → flooding,
   striking), CHAIN (rig → her speed drops; how you end a chase),
   GRAPE (crew → softens boarding defense). Accuracy falls with range
   and your own heel. All sailing skill feeds gunnery: crossing her
   stern, holding the arc, keeping your guns loaded for the moment.
2. **Damage model**, both sides: rig (speed/turning), hull (flooding →
   she settles → strikes), crew (boarding strength). She strikes her
   colours when beaten; sinking her loses the treasure.
3. **Galleon AI**: runs downwind when sighted, yaws to fire her own
   broadside if armed, turns toward her consort/the fort when one
   exists.
4. **Boarding phase**: grappled, loot ticks up chest by chest, boarders
   can be repelled if her crew is unsoftened; the Begoña clock runs the
   whole time.
5. **Square-rig top-down art**: yards braced round the mast, galleon
   with high sterncastle and tubby beam; English race-built hulls lean.
   New `drawVessel` variants, same flat-vector language.
6. **Captain select screen** (title: four portraits/ships, era dates).

## Sourcing discipline

Same rule as doghole: a sources table in GAME.md mapping every modelled
fact to its authority, departures flagged ⚠. Before build, VERIFY (do
not trust this plan's memory): Santa Ana's guns struck below; tonnages
and gun counts for all four flagships and four prizes; the Begoña
action's course of events; Cabo San Lucas bay geography and the
galleons' watering practice; Fort San Diego's armament. Primary leads:
Pretty's account of Cavendish's voyage (Hakluyt), Rogers' own *A
Cruising Voyage Round the World* (1712), Walter/Robins' *Anson's Voyage*
(1748), Schurz *The Manila Galleon* (1939). Rogers and the Anson account
are on IA; check the vault bibliography DB first.

## Music (built 2026-10-03)

Three cues, rendered through the passion-organ storm-organ synth
(`tools/render_organ.py`, a parameterized fork of
`~/passion-organ/scripts/render_midi.py`):
- **Rule, Britannia!** (Arne, 1740) at 80 bpm: the title theme
  (`theme-britannia.m4a`).
- **The British Grenadiers** (traditional): the victory cue
  (`grenadiers.m4a`).
- **Marcha Real / Marcha Granadera** (anonymous, in print by 1761) at
  58 bpm, HOLD 1.5, SWELL .6: slow and in the old style; rises when
  the galleon is sighted (`marcha-real.m4a`).

Licensing is CLEAN by construction: the compositions are public
domain, and the shipped MIDI arrangements are our own
(`tools/make_tunes.py` extracts only the melody line from reference
encodings downloaded from mfiles.co.uk and flutetunes.com, then writes
its own harmony and bass; no third-party encoding ships). ⚠ Aodhan
should AUDITION all three: the melody lines came from the references,
but the harmonization is algorithmic (I-ii-IV-V-vi by melody fit) and
a wrong chord is possible. ⚠ Anachronism, flagged: the Marcha
Granadera postdates Drake and Cavendish by nearly two centuries; it is
game music, not a period claim.

## Build order

1. Repo scaffold: copy doghole's `play.html`/`vessel.js`/`serve_nocache.py`
   skeleton, strip cove specifics. Get a ship sailing on open water.
2. Square-rig polar + per-ship tables; square-rig drawing.
3. `cape.js`: Cabo terrain, the galleon lane, sighting.
4. Chase + chain-shot (disable), galleon AI.
5. Manual broadsides + damage model (level 4's duel becomes testable).
6. Grapple (port warp code) + boarding + loot weight.
7. Begoña clock + escape phase (level 3 complete).
8. Levels 1, 2 scripting; captain select; level 5 last.
9. Audio pass (synth cannon, splinter, grapple; theme TBD — not the
   doghole Bach, this game needs its own cue).
10. Title screen, GAME.md sources table, publish (own repo + a fourth
    cabinet on the arcade, later).
