// =====================================================================
// PACIFIC GALLEON: the ships.
//
// The physics is doghole's vessel.js, kept whole: a rudder only bites
// with way on, you cannot sail into the wind, the current sets you and
// you cannot feel it, and cargo makes her slow. What changes is the RIG.
// These are square-riggers, so each class carries its own POLAR: an
// English race-built private ship will not lie closer than about five
// points, and a Manila galleon not closer than about six and a half,
// and both are happiest with the wind on the quarter. That one table is
// the chase: the galleon runs in her best point of sail, and you must
// be faster, or cut the corner.
//
// Numbers are TUNED FOR PLAY, exactly as doghole's are: true knots in
// the HUD, time compressed, handier than life. Tonnages and the
// relative characters (small and weatherly, big and ponderous) follow
// the record; VERIFY the ship particulars before any sources table
// ships (see PLAN.md).
// =====================================================================
import { KN, depthAt, windShadow } from "./cape.js";

export const norm = a => {
  while (a > Math.PI) a -= Math.PI * 2;
  while (a < -Math.PI) a += Math.PI * 2;
  return a;
};
export const degOf = r => ((r * 180 / Math.PI) % 360 + 360) % 360;

// ------------------------------------------------------------ classes
// len/beam in yards. sail/kFwd set the top speed, rud the handiness,
// mass0 the ponderousness, cap the treasure she can stow (in chests).
// polar: irons = closest she will lie (degrees off the wind), then the
// curve's anchors at the beam, her best point, and dead run.
// Colours are daylight wood: wale = the hull sides you see around the
// deck, deck = the planking, castle = the raised works. flag picks her
// colours: St George's cross for the English, the Cross of Burgundy
// for Spain, which is what Spanish ships wore at sea in all four eras.
export const CLASSES = {
  goldenhind: {
    // a little Tudor galleon: short, beamy, a tall carrack-like
    // sterncastle, green-and-white painted topsides
    name: "Golden Hind", captain: "Drake", year: 1579,
    len: 24, beam: 8.2, masts: 3, castles: .78, decks: 1,
    sail: 1.55, kFwd: .057, kLat: 1.05, rud: .118, yawDamp: .95,
    mass0: 1.0, loadK: 1.05, draft0: 6, cap: 30,
    polar: { irons: 55, beam: .82, bestA: 135, best: 1, run: .86 },
    wale: "#3c6b3e", deck: "#caa972", castle: "#2f6b45", castleHi: "#3f8056",
    paint: "#e8e2d0", accent: "#d9a441", flag: "english",
  },
  desire: {
    // an Elizabethan race-built ship: leaner than the Hind, a medium
    // castle, dark red and gold
    name: "Desire", captain: "Cavendish", year: 1587,
    len: 28, beam: 7.6, masts: 3, castles: .55, decks: 1,
    sail: 1.52, kFwd: .058, kLat: 1.05, rud: .105, yawDamp: .95,
    mass0: 1.1, loadK: 1.05, draft0: 6.5, cap: 36,
    polar: { irons: 56, beam: .8, bestA: 136, best: 1, run: .87 },
    wale: "#4a2420", deck: "#b89158", castle: "#6e2a28", castleHi: "#8a3733",
    paint: "#d9a441", accent: "#d9a441", flag: "english",
  },
  duke: {
    // a Queen Anne frigate-privateer: long, lean, low and flush, a black
    // wale on a buff hull
    name: "Duke", captain: "Woodes Rogers", year: 1709,
    len: 34, beam: 8.4, masts: 3, castles: .34, decks: 1,
    sail: 1.62, kFwd: .066, kLat: 1.1, rud: .085, yawDamp: 1.0,
    mass0: 1.6, loadK: .9, draft0: 8, cap: 50,
    polar: { irons: 58, beam: .78, bestA: 138, best: 1, run: .88 },
    wale: "#201811", deck: "#c6a573", castle: "#5a4428", castleHi: "#6e5533",
    paint: "#2a2018", accent: "#b98f3a", flag: "english",
  },
  centurion: {
    // a 60-gun fourth-rate man-of-war: long, broad and high-sided, TWO
    // gun decks, the blue-and-yellow of the Georgian navy
    name: "Centurion", captain: "Anson", year: 1743,
    len: 48, beam: 12.6, masts: 3, castles: .5, decks: 2,
    sail: 1.78, kFwd: .079, kLat: 1.2, rud: .06, yawDamp: 1.15,
    mass0: 2.4, loadK: .75, draft0: 10.5, cap: 70,
    polar: { irons: 60, beam: .76, bestA: 140, best: 1, run: .9 },
    wale: "#1b2740", deck: "#a98f63", castle: "#243a63", castleHi: "#31508a",
    paint: "#e3c24a", accent: "#e3c24a", flag: "english",
  },
  // the prize. The variants (unarmed and fat, the normal prize, the one
  // you do not touch) come later as overrides on this base; see the
  // spawn table in PLAN.md.
  galleon: {
    name: "the galleon", captain: null, year: 0,
    len: 40, beam: 12.4, masts: 3, castles: 1,
    // She is slower than any of you: six months at sea, grass on her
    // bottom, a hold full of silk and silver and a crew on short water.
    // The chase has to be winnable from dead astern, because the wind
    // runs down the coast and so does she.
    sail: 1.5, kFwd: .095, kLat: 1.15, rud: .05, yawDamp: 1.2,
    mass0: 2.6, loadK: .4, draft0: 11, cap: 0,
    polar: { irons: 70, beam: .62, bestA: 150, best: 1, run: .95 },
    wale: "#54371d", deck: "#c6a26c", castle: "#9c582c", castleHi: "#b26a36",
    accent: "#e3b54a", flag: "burgundy",
  },
};

export function makeShip(clsKey, x, y, hdgDeg) {
  const cls = CLASSES[clsKey];
  return {
    cls, clsKey,
    x, y,
    hdg: hdgDeg * Math.PI / 180,     // 0 = north, clockwise
    vx: 0, vy: 0, omega: 0,
    helm: 0, canvas: .5,
    cargo: 0, damage: 0, rigDamage: 0, struck: false,
    // kept for the grapple, which is doghole's warp code with a moving
    // target; unused until the boarding phase goes in
    warp: null, lines: 0, moored: false,
    heel: 0, surge: 0,
    underKeel: 0, draftFt: 0, speedKn: 0, throughKn: 0, driveNow: 0,
    inIrons: false, becalmed: false, awa: 0,
  };
}

// the square-rig polar: zero inside the irons angle, then a straight
// run between the anchors. Nothing fancier survives contact with play.
function polarAt(p, a) {
  if (a < p.irons) return 0;
  const pts = [[p.irons, .3], [90, p.beam], [p.bestA, p.best], [180, p.run]];
  for (let i = 0; i < pts.length - 1; i++) {
    const [a0, c0] = pts[i], [a1, c1] = pts[i + 1];
    if (a <= a1) return c0 + (c1 - c0) * (a - a0) / Math.max(1, a1 - a0);
  }
  return p.run;
}

// ------------------------------------------------------------- physics
export function step(s, env, dt) {
  const c = s.cls;
  const load = c.cap ? s.cargo / c.cap : 0;
  const mass = c.mass0 * (1 + load * c.loadK);
  const draft = c.draft0 + 3 * load;

  const fx = Math.sin(s.hdg), fy = -Math.cos(s.hdg);   // ahead
  const sx = Math.cos(s.hdg), sy = Math.sin(s.hdg);    // to starboard

  // water-relative velocity: you drift with the set and cannot feel it
  const wx = s.vx - env.curX, wy = s.vy - env.curY;
  const fwd = wx * fx + wy * fy;
  const lat = wx * sx + wy * sy;

  // wind (cape.js breathes it; fall back to the base if it has not)
  const windFrom = env.windNow ?? env.windFrom;
  const windKn = env.windKnNow ?? env.windKn;
  const shade = windShadow(s.x, s.y, windFrom);
  const wind = windKn * (1 - shade);
  const awa = norm(s.hdg - windFrom * Math.PI / 180);
  const a = Math.abs(awa) * 180 / Math.PI;
  const curve = polarAt(c.polar, a);
  // rig damage comes off the top: a ship with her rigging cut up cannot
  // carry her canvas. s.damage is HULL; s.rigDamage is the chase-ender.
  const rigFactor = 1 - .7 * Math.min(1, s.rigDamage || 0);
  const drive = c.sail * s.canvas * curve * (wind / 14) * rigFactor;

  let ax = 0, ay = 0;
  ax += drive * fx; ay += drive * fy;
  const lee = drive * .30 * Math.sin(awa) * -1;        // leeway
  ax += lee * sx; ay += lee * sy;

  const dF = -c.kFwd * fwd * Math.abs(fwd);
  const dL = -c.kLat * lat * Math.abs(lat);
  ax += dF * fx + dL * sx;
  ay += dF * fy + dL * sy;

  // the NW swell, astern of the track
  const sw = env.swellDir * Math.PI / 180;
  const surge = Math.sin(env.t * env.swellRate + s.x * .001) * env.swell;
  s.surge = surge;
  ax += -Math.sin(sw) * surge * .4;
  ay += Math.cos(sw) * surge * .4;

  // the grapple: doghole's warp, with the target allowed to move
  if (s.warp && s.lines > 0) {
    const k = s.lines;
    ax += (s.warp.x - s.x) * .0062 * k;
    ay += (s.warp.y - s.y) * .0062 * k;
    ax -= s.vx * .34 * k;  ay -= s.vy * .34 * k;
  }

  s.vx += ax / mass * dt;  s.vy += ay / mass * dt;

  // helm: no way through the water, no steering
  const speed = Math.hypot(wx, wy);
  const bite = .22 + .78 * Math.min(1, speed / (2.0 * KN));
  let tq = c.rud * s.helm * bite * (fwd < 0 ? -1 : 1);
  // weather helm: she wants to round up, hardest with the wind abeam
  // and not at all running square, which is how a ship actually gripes
  tq -= Math.sin(awa) * drive * .02;
  tq -= s.omega * c.yawDamp;
  if (s.warp && s.lines > 0) {
    tq += norm(s.warp.hdg - s.hdg) * .034 * s.lines - s.omega * .42 * s.lines;
  }
  s.omega += tq / mass * dt;
  s.hdg = norm(s.hdg + s.omega * dt);

  s.x += (s.vx + env.curX) * dt;
  s.y += (s.vy + env.curY) * dt;

  s.heel += (Math.abs(lee) * 2.4 + surge * .3 - s.heel) * dt * 2;

  const ft = depthAt(s.x, s.y);
  s.underKeel = ft - draft;
  s.draftFt = draft;
  s.speedKn = Math.hypot(s.vx, s.vy) / KN;
  s.throughKn = speed / KN;
  s.driveNow = drive;
  s.awa = awa;
  s.inIrons = curve === 0 && s.canvas > .05;
  s.becalmed = shade > .45;
  return s;
}

// ------------------------------------------------------------ drawing
// Daylight, from overhead: wooden decks you can read the planks on,
// cream canvas with real weight, her shadow on the water, and her
// colours streaming downwind. What tells a square-rigger from the
// schooner is the YARDS; what tells the galleon from an Englishman is
// the CASTLES, the ochre paint, the gilding, and the Cross of Burgundy.
export function drawShip(ctx, T, s, t, C) {
  const c = s.cls;
  const L = c.len, B = c.beam;
  const S = T.S;
  const full = c.castles >= 1 ? 1 : 0;          // 1 = galleon proportions
  const set = s.canvas;
  const drawing = Math.min(1, (s.driveNow || 0) / .55);
  const awaDeg = Math.abs(s.awa) * 180 / Math.PI;
  // awa > 0 means the wind is on her PORT side, so leeward is to
  // starboard: the canvas bellies and the lateen booms out that way
  const sgn = s.awa > 0 ? 1 : -1;
  const dwx = Math.sin(s.awa), dwy = Math.cos(s.awa);    // downwind, body frame
  const brace = Math.min(55, Math.max(0, (180 - awaDeg) * .5)) * sgn * Math.PI / 180;

  const hullPath = (inset) => {
    const b = B / 2 - inset, l = L / 2 - inset;
    ctx.beginPath();
    ctx.moveTo(0, S(-l - 2.2));
    ctx.bezierCurveTo(S(b * (.85 + .1 * full)), S(-l * .5),
                      S(b), S(0), S(b * (.9 - .14 * full)), S(l * .62));
    ctx.lineTo(S(b * (.72 - .2 * full)), S(l));
    ctx.lineTo(S(-b * (.72 - .2 * full)), S(l));
    ctx.lineTo(S(-b * (.9 - .14 * full)), S(l * .62));
    ctx.bezierCurveTo(S(-b), S(0),
                      S(-b * (.85 + .1 * full)), S(-l * .5), 0, S(-l - 2.2));
    ctx.closePath();
  };

  // ---- her shadow on the water, cast a little to the north-east,
  //      which puts the sun high in the south-west where it belongs
  ctx.save();
  ctx.translate(T.X(s.x) + S(1.7), T.Y(s.y) - S(1.1));
  ctx.rotate(s.hdg);
  hullPath(-.6);
  ctx.fillStyle = "rgba(10,30,40,.28)";
  ctx.fill();
  ctx.restore();

  ctx.save();
  ctx.translate(T.X(s.x), T.Y(s.y));
  ctx.rotate(s.hdg);

  // ---- water working round her
  const sp = Math.min(1, s.speedKn / 6);
  if (sp > .05) {
    const wob2 = Math.sin(t * 2.3 + 1.1) * .5;
    ctx.globalAlpha = .07 + sp * .11;
    ctx.fillStyle = "#eefafb";                   // churned water, pale by day
    ctx.beginPath();
    ctx.ellipse(S(wob2), S(L * .6 + sp * 3), S(B * .26 + sp * .7), S(L * .09 + sp * 4),
                0, 0, Math.PI * 2);
    ctx.fill();
    ctx.globalAlpha = .35 + sp * .5;
    ctx.strokeStyle = "#ffffff";
    ctx.lineWidth = Math.max(1, S(.55));
    for (const side of [-1, 1]) {
      ctx.beginPath();
      ctx.moveTo(S(side * B * .06), S(-L * .49));
      ctx.quadraticCurveTo(S(side * (B * .5 + sp * 1.6)), S(-L * .3),
                           S(side * (B * .56 + sp * 2)), S(-L * .08));
      ctx.stroke();
    }
    ctx.globalAlpha = 1;
  }

  // ---- the hull: wale, a painted sheer strake (her own colours), the
  //      bulwark, then the planked deck
  hullPath(0);  ctx.fillStyle = c.wale;  ctx.fill();
  if (c.paint){ hullPath(.45); ctx.fillStyle = c.paint; ctx.fill(); }
  hullPath(.9); ctx.fillStyle = full ? "#6b4526" : "#5d4224"; ctx.fill();
  hullPath(1.1); ctx.fillStyle = c.deck; ctx.fill();

  // deck planks, running fore and aft, clipped to the deck
  ctx.save();
  hullPath(1.1); ctx.clip();
  ctx.strokeStyle = "rgba(74,51,25,.4)";
  ctx.lineWidth = Math.max(.5, S(.16));
  for (let px = -B/2 + 1.4; px < B/2 - 1.0; px += .95) {
    ctx.beginPath();
    ctx.moveTo(S(px), S(-L * .52)); ctx.lineTo(S(px), S(L * .52));
    ctx.stroke();
  }
  // main hatch and fore hatch, dark gratings
  ctx.fillStyle = "rgba(40,26,13,.85)";
  ctx.fillRect(S(-B * .17), S(-L * .07), S(B * .34), S(L * .13));
  ctx.fillRect(S(-B * .12), S(-L * .33), S(B * .24), S(L * .08));
  ctx.strokeStyle = "rgba(160,130,86,.5)";
  ctx.strokeRect(S(-B * .17), S(-L * .07), S(B * .34), S(L * .13));
  ctx.restore();

  // guns run out along the rails, little black muzzles. A two-decker
  // (the Centurion) shows a second, inner row.
  const nG = Math.max(2, Math.floor(L / 8));
  const decks = c.decks || 1;
  ctx.fillStyle = "#1c1612";
  for (let g = 0; g < nG; g++) {
    const gy = -L * .26 + (g + .5) * (L * .5 / nG);
    for (const side of [-1, 1]) {
      for (let d = 0; d < decks; d++) {
        const off = B/2 - .9 - d * 1.6;
        ctx.fillRect(S(side * off - .35), S(gy), Math.max(1, S(1.3)) * (side<0?-1:1), Math.max(1, S(.65)));
      }
    }
  }

  // ---- the castles, raised and lit from the south-west
  if (c.castles > 0) {
    const k = c.castles;
    const block = (x, y, w, h, base, hi) => {
      ctx.fillStyle = "rgba(20,12,6,.4)";                 // its shadow
      ctx.fillRect(S(x) + S(.5), S(y) + S(.5), S(w), S(h));
      ctx.fillStyle = base;
      ctx.fillRect(S(x), S(y), S(w), S(h));
      ctx.fillStyle = hi;                                  // the lit face
      ctx.fillRect(S(x), S(y), S(w * .45), S(h));
      ctx.strokeStyle = "rgba(25,15,8,.75)";
      ctx.lineWidth = Math.max(.6, S(.2));
      ctx.strokeRect(S(x), S(y), S(w), S(h));
    };
    // sterncastle, stepped: the half deck, then the poop above it
    block(-B * .34, L * .17, B * .68, L * .3 * k, c.castle, c.castleHi);
    block(-B * .26, L * .3,  B * .52, L * .18 * k, c.castleHi, full ? "#c07b40" : c.castleHi);
    // forecastle
    block(-B * .25, -L * .45, B * .5, L * .14 * k, c.castle, c.castleHi);
    // the galleon's gilded taffrail and her two stern lanterns
    if (full) {
      ctx.strokeStyle = c.accent; ctx.lineWidth = Math.max(1, S(.5));
      ctx.beginPath();
      ctx.moveTo(S(-B * .25), S(L * .485)); ctx.lineTo(S(B * .25), S(L * .485));
      ctx.stroke();
      ctx.fillStyle = c.accent;
      for (const lx of [-B * .16, B * .16]) {
        ctx.beginPath(); ctx.arc(S(lx), S(L * .5), Math.max(1, S(.5)), 0, Math.PI * 2); ctx.fill();
      }
    }
  }

  // treasure aboard, stowed abaft the mainmast
  if (c.cap && s.cargo > .5) {
    const rows = Math.max(1, Math.round(s.cargo / c.cap * 5));
    for (let i = 0; i < rows; i++) {
      ctx.fillStyle = i % 2 ? "#c8781f" : "#f2a63c";
      ctx.fillRect(S(-B * .2), S(-L * .02 + i * L * .035), S(B * .4), S(L * .028));
    }
  }

  // bowsprit, steeved out over the stem; the galleon gets her beakhead
  ctx.strokeStyle = "#4a3319"; ctx.lineWidth = Math.max(1, S(.9));
  ctx.beginPath();
  ctx.moveTo(0, S(-L * .5)); ctx.lineTo(0, S(-L * .5 - L * .26));
  ctx.stroke();
  if (full) {
    ctx.fillStyle = c.castle;
    ctx.beginPath();
    ctx.moveTo(S(-B * .09), S(-L * .5 - 1));
    ctx.lineTo(S(B * .09), S(-L * .5 - 1));
    ctx.lineTo(0, S(-L * .5 - L * .13));
    ctx.closePath(); ctx.fill();
  }

  // men on deck, for scale
  ctx.fillStyle = "#2a1c10";
  ctx.beginPath(); ctx.arc(S(-B * .28), S(L * .1), S(.5), 0, Math.PI * 2); ctx.fill();
  ctx.beginPath(); ctx.arc(S(B * .26), S(-L * .2), S(.5), 0, Math.PI * 2); ctx.fill();
  ctx.beginPath(); ctx.arc(0, S(L * .42), S(.5), 0, Math.PI * 2); ctx.fill();

  // rudder
  ctx.strokeStyle = "#2a1d10"; ctx.lineWidth = Math.max(1, S(1.1));
  ctx.beginPath();
  ctx.moveTo(0, S(L * .5)); ctx.lineTo(S(s.helm * 2.2), S(L * .5 + 3));
  ctx.stroke();

  // ---- the rig. Fore and main carry a course and a topsail on braced
  //      yards; the mizzen a lateen; a spritsail under the bowsprit.
  const MASTS = [
    { my: -L * .28, yard: B * 1.55 },
    { my:  L * .02, yard: B * 1.85 },
  ];
  ctx.fillStyle = "#3a2a16";
  for (const m of MASTS.concat([{ my: L * .3 }])) {
    ctx.beginPath(); ctx.arc(0, S(m.my), S(.9), 0, Math.PI * 2); ctx.fill();
  }

  // one band of canvas hung from a braced yard. Cream, with weight: a
  // lit face toward the sun, a shaded foot, a seam down the middle.
  const band = (mx, my, halfW, bell, footW) => {
    const yx = Math.cos(brace) * halfW, yy = Math.sin(brace) * halfW;
    const ax = -yx, ay = my - yy, bx = yx, by = my + yy;
    const afx = -yx * footW + dwx * bell, afy = my - yy * footW + dwy * bell;
    const bfx = yx * footW + dwx * bell,  bfy = my + yy * footW + dwy * bell;
    ctx.globalAlpha = .5 + .45 * set * (.4 + .6 * drawing);
    ctx.fillStyle = "#f1e7cf";
    ctx.beginPath();
    ctx.moveTo(S(ax), S(ay));
    ctx.lineTo(S(bx), S(by));
    ctx.lineTo(S(bfx), S(bfy));
    ctx.quadraticCurveTo(S(dwx * bell * 1.55 + mx), S(my + dwy * bell * 1.55),
                         S(afx), S(afy));
    ctx.closePath();
    ctx.fill();
    // the shaded foot of the cloth
    ctx.globalAlpha *= .5;
    ctx.strokeStyle = "#a89878";
    ctx.lineWidth = Math.max(.8, S(.45));
    ctx.beginPath();
    ctx.moveTo(S(bfx), S(bfy));
    ctx.quadraticCurveTo(S(dwx * bell * 1.55 + mx), S(my + dwy * bell * 1.55),
                         S(afx), S(afy));
    ctx.stroke();
    // the centre seam
    ctx.beginPath();
    ctx.moveTo(S(mx), S(my));
    ctx.quadraticCurveTo(S(mx + dwx * bell * .7), S(my + dwy * bell * .7),
                         S(mx + dwx * bell * 1.1), S(my + dwy * bell * 1.1));
    ctx.stroke();
    ctx.globalAlpha = 1;
    // the yard, dark and solid over the canvas head
    ctx.strokeStyle = "#2e2110";
    ctx.lineWidth = Math.max(1, S(.6));
    ctx.beginPath();
    ctx.moveTo(S(ax), S(ay)); ctx.lineTo(S(bx), S(by));
    ctx.stroke();
  };

  if (set > .04) {
    for (const m of MASTS) {
      // topsail first (it sits forward of the course from overhead),
      // then the course over it
      band(0, m.my - L * .045, m.yard * .33, B * (.26 + .22 * drawing) * set, .72);
      band(0, m.my,            m.yard * .5,  B * (.4 + .34 * drawing) * set, .78);
    }
    // the lateen mizzen, out to leeward
    const out = B * 1.05 * (.35 + .65 * set) * sgn;
    const my = L * .3, len = L * .22;
    ctx.strokeStyle = "#2e2110"; ctx.lineWidth = Math.max(1, S(.6));
    ctx.beginPath();
    ctx.moveTo(0, S(my)); ctx.lineTo(S(out), S(my + len));
    ctx.stroke();
    ctx.globalAlpha = .45 + .4 * set * (.4 + .6 * drawing);
    ctx.fillStyle = "#ece2c8";
    ctx.beginPath();
    ctx.moveTo(0, S(my));
    ctx.quadraticCurveTo(S(out * .6), S(my + len * .45), S(out), S(my + len));
    ctx.lineTo(0, S(my + len));
    ctx.closePath(); ctx.fill();
    ctx.globalAlpha = 1;
    // the spritsail under the bowsprit
    band(0, -L * .5 - L * .16, B * .4, B * .26 * set, .75);
  }

  // ---- her colours, off the ensign staff right aft. On striking, the
  //      national ensign is HAULED DOWN (it shrinks in to the staff) and
  //      a white flag of surrender is run up in its place.
  {
    const fl0 = Math.max(3, L * .14), fw = fl0 * .52;
    const wave = Math.sin(t * 5 + s.x * .01) * .12;
    const a = Math.atan2(dwy, dwx) + wave;
    const low = s.struck ? Math.min(1, (t - (s.struckAt ?? t)) / 1.3) : 0;
    const flag = (fl, type) => {
      if (fl < .4) return;
      ctx.save();
      ctx.translate(0, S(L * .46)); ctx.rotate(a); ctx.translate(S(1.0), 0);
      if (type === "burgundy"){
        ctx.fillStyle = "#efe6d2"; ctx.fillRect(0, S(-fw/2), S(fl), S(fw));
        ctx.strokeStyle = "#b3362a"; ctx.lineWidth = Math.max(1, S(.4));
        ctx.beginPath();
        ctx.moveTo(S(fl*.1), S(-fw*.34)); ctx.lineTo(S(fl*.9), S(fw*.34));
        ctx.moveTo(S(fl*.1), S(fw*.34));  ctx.lineTo(S(fl*.9), S(-fw*.34)); ctx.stroke();
      } else if (type === "george"){
        ctx.fillStyle = "#f4f0e6"; ctx.fillRect(0, S(-fw/2), S(fl), S(fw));
        ctx.strokeStyle = "#c03a2a"; ctx.lineWidth = Math.max(1, S(.45));
        ctx.beginPath();
        ctx.moveTo(0, 0); ctx.lineTo(S(fl), 0);
        ctx.moveTo(S(fl*.38), S(-fw/2)); ctx.lineTo(S(fl*.38), S(fw/2)); ctx.stroke();
      } else {                                      // a plain white flag
        ctx.fillStyle = "#fbfbf6"; ctx.fillRect(0, S(-fw/2), S(fl), S(fw));
      }
      ctx.strokeStyle = "rgba(30,20,10,.5)"; ctx.lineWidth = Math.max(.6, S(.2));
      ctx.strokeRect(0, S(-fw/2), S(fl), S(fw));
      ctx.restore();
    };
    if (!s.struck){
      flag(fl0, c.flag === "burgundy" ? "burgundy" : "george");
    } else {
      // the national colours coming down, the white going up
      flag(fl0 * (1 - low), c.flag === "burgundy" ? "burgundy" : "george");
      flag(fl0 * Math.max(0, (low - .35) / .65), "white");
      // the struck ensign bundled at the staff foot
      if (low > .6){
        ctx.fillStyle = c.flag === "burgundy" ? "#b3362a" : "#c03a2a";
        ctx.beginPath(); ctx.arc(0, S(L * .48), Math.max(1.4, S(.8)), 0, Math.PI*2); ctx.fill();
      }
    }
  }

  ctx.restore();
}
