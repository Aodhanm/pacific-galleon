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
import { KN, depthAt, windShadow } from "./sea.js";

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
export const CLASSES = {
  goldenhind: {
    name: "Golden Hind", captain: "Drake", year: 1579,
    len: 25, beam: 6.8, masts: 3, castles: .5,
    sail: 1.55, kFwd: .057, kLat: 1.05, rud: .118, yawDamp: .95,
    mass0: 1.0, loadK: 1.05, draft0: 6, cap: 30,
    polar: { irons: 55, beam: .82, bestA: 135, best: 1, run: .86 },
    hull: "#10161e", trim: "#2a2118",
  },
  desire: {
    name: "Desire", captain: "Cavendish", year: 1587,
    len: 26, beam: 7.2, masts: 3, castles: .6,
    sail: 1.52, kFwd: .058, kLat: 1.05, rud: .105, yawDamp: .95,
    mass0: 1.1, loadK: 1.05, draft0: 6.5, cap: 36,
    polar: { irons: 56, beam: .8, bestA: 136, best: 1, run: .87 },
    hull: "#111820", trim: "#2a2118",
  },
  duke: {
    name: "Duke", captain: "Woodes Rogers", year: 1709,
    len: 32, beam: 8.8, masts: 3, castles: .45,
    sail: 1.62, kFwd: .066, kLat: 1.1, rud: .085, yawDamp: 1.0,
    mass0: 1.6, loadK: .9, draft0: 8, cap: 50,
    polar: { irons: 58, beam: .78, bestA: 138, best: 1, run: .88 },
    hull: "#121a22", trim: "#2a2118",
  },
  centurion: {
    name: "Centurion", captain: "Anson", year: 1743,
    len: 46, beam: 12.6, masts: 3, castles: .4,
    sail: 1.78, kFwd: .079, kLat: 1.2, rud: .06, yawDamp: 1.15,
    mass0: 2.4, loadK: .75, draft0: 10.5, cap: 70,
    polar: { irons: 60, beam: .76, bestA: 140, best: 1, run: .9 },
    hull: "#131b23", trim: "#2a2118",
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
    hull: "#201712", trim: "#3a2c1d",
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
    cargo: 0, damage: 0,
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

  // wind (sea.js breathes it; fall back to the base if it has not)
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
// Same flat-vector language as doghole, seen from above. What tells a
// square-rigger from the schooner at a glance is the YARDS: dark lines
// crossing each mast, braced round toward the wind, with the pale sail
// bellied away downwind of them. What tells a galleon from an English
// private ship is the CASTLES: the high block of her sterncastle and
// the smaller one forward, where the race-built English hull is flush
// and lean.
export function drawShip(ctx, T, s, t, C) {
  const c = s.cls;
  const L = c.len, B = c.beam;
  ctx.save();
  ctx.translate(T.X(s.x), T.Y(s.y));
  ctx.rotate(s.hdg);
  const S = T.S;

  // water working round her, exactly doghole's: dark torn water astern,
  // a bright lip of foam at the stem
  const sp = Math.min(1, s.speedKn / 6);
  if (sp > .05) {
    const wob2 = Math.sin(t * 2.3 + 1.1) * .5;
    ctx.globalAlpha = .18 + sp * .3;
    ctx.fillStyle = "#0c161d";
    ctx.beginPath();
    ctx.ellipse(S(wob2), S(L * .58 + sp * 4), S(B * .34 + sp), S(L * .1 + sp * 5),
                0, 0, Math.PI * 2);
    ctx.fill();
    ctx.globalAlpha = .30 + sp * .45;
    ctx.strokeStyle = "#e8f4fb";
    ctx.lineWidth = Math.max(1, S(.55));
    for (const side of [-1, 1]) {
      ctx.beginPath();
      ctx.moveTo(S(side * B * .06), S(-L * .49));
      ctx.quadraticCurveTo(S(side * (B * .5 + sp * 1.6)), S(-L * .3),
                           S(side * (B * .56 + sp * 2)), S(-L * .08));
      ctx.stroke();
    }
    ctx.fillStyle = "#dff0fa";
    for (let i = 0; i < 7; i++) {
      const sx2 = Math.sin(t * 2.2 + i * 1.9) * B * .5;
      const sy2 = L * .52 + ((i * 2.3 + t * 9) % 12);
      ctx.globalAlpha = (.5 - (sy2 - L * .52) / 24) * (.3 + sp * .6);
      if (ctx.globalAlpha <= 0) continue;
      ctx.fillRect(S(sx2), S(sy2), Math.max(1, S(.7)), Math.max(1, S(.7)));
    }
    ctx.globalAlpha = 1;
  }

  // the hull. A galleon is fuller forward and pinched at the stern; the
  // English hull keeps doghole's leaner line.
  const full = c.castles >= 1 ? 1 : 0;        // 1 = galleon proportions
  const hull = (inset, col) => {
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
    ctx.fillStyle = col; ctx.fill();
  };
  hull(0, c.hull);
  hull(.9, full ? "#2b2017" : "#1b242e");

  // the castles. Drawn as raised blocks with a shadowed edge, the way
  // doghole raises a roof: the lighter top face is what reads as height.
  if (c.castles > 0) {
    const k = c.castles;
    // sterncastle, the big one, stepped in two
    ctx.fillStyle = full ? "#3a2b1e" : "#28333e";
    ctx.fillRect(S(-B * .33), S(L * .18), S(B * .66), S(L * .3 * k));
    ctx.fillStyle = full ? "#4a3826" : "#32404c";
    ctx.fillRect(S(-B * .26), S(L * .28), S(B * .52), S(L * .2 * k));
    ctx.strokeStyle = "rgba(10,14,19,.7)";
    ctx.lineWidth = Math.max(1, S(.5));
    ctx.strokeRect(S(-B * .33), S(L * .18), S(B * .66), S(L * .3 * k));
    // a gilded taffrail on the galleon, the one warm line on her
    if (full) {
      ctx.strokeStyle = "rgba(242,166,60,.8)";
      ctx.lineWidth = Math.max(1, S(.6));
      ctx.beginPath();
      ctx.moveTo(S(-B * .26), S(L * .485));
      ctx.lineTo(S(B * .26), S(L * .485));
      ctx.stroke();
    }
    // forecastle
    ctx.fillStyle = full ? "#3a2b1e" : "#28333e";
    ctx.fillRect(S(-B * .24), S(-L * .44), S(B * .48), S(L * .14 * k));
    ctx.strokeStyle = "rgba(10,14,19,.7)";
    ctx.strokeRect(S(-B * .24), S(-L * .44), S(B * .48), S(L * .14 * k));
  }

  // treasure aboard, stowed abaft the mainmast where the deckload reads
  if (c.cap && s.cargo > .5) {
    const rows = Math.max(1, Math.round(s.cargo / c.cap * 5));
    for (let i = 0; i < rows; i++) {
      ctx.fillStyle = i % 2 ? "#c8781f" : "#f2a63c";
      ctx.fillRect(S(-B * .2), S(-L * .02 + i * L * .035), S(B * .4), S(L * .028));
    }
  }

  // bowsprit, steeved up and out over the stem
  ctx.strokeStyle = c.trim; ctx.lineWidth = Math.max(1, S(.9));
  ctx.beginPath();
  ctx.moveTo(0, S(-L * .5)); ctx.lineTo(0, S(-L * .5 - L * .26));
  ctx.stroke();

  // the wheel or whipstaff aft, and a man at it
  ctx.strokeStyle = "#3a2c1d"; ctx.lineWidth = Math.max(1, S(.7));
  ctx.beginPath(); ctx.arc(0, S(L * .44), S(1.2), 0, Math.PI * 2); ctx.stroke();
  ctx.fillStyle = "#0a0e14";
  ctx.beginPath(); ctx.arc(S(-B * .28), S(L * .1), S(.55), 0, Math.PI * 2); ctx.fill();
  ctx.beginPath(); ctx.arc(S(B * .26), S(-L * .2), S(.55), 0, Math.PI * 2); ctx.fill();

  // rudder
  ctx.strokeStyle = "#1b242c"; ctx.lineWidth = Math.max(1, S(1.1));
  ctx.beginPath();
  ctx.moveTo(0, S(L * .5)); ctx.lineTo(S(s.helm * 2.2), S(L * .5 + 3));
  ctx.stroke();

  // ------------------------------------------------------------ the rig
  // Three masts. Fore and main carry square canvas on braced yards; the
  // mizzen carries a lateen, boomed out to leeward like the schooner's
  // main, which is what these rigs actually wore aft.
  const set = s.canvas;
  const drawing = Math.min(1, (s.driveNow || 0) / .55);
  const awaDeg = Math.abs(s.awa) * 180 / Math.PI;
  const sgn = s.awa > 0 ? -1 : 1;              // sails belly to leeward
  // the yards brace round toward the wind: square before the wind, hard
  // round when she is close-hauled
  const brace = Math.min(55, Math.max(0, (180 - awaDeg) * .5)) * sgn * Math.PI / 180;

  const MASTS = [
    { my: -L * .28, yard: B * 1.5, name: "fore" },
    { my:  L * .02, yard: B * 1.8, name: "main" },
  ];
  ctx.fillStyle = c.trim;
  for (const m of MASTS.concat([{ my: L * .3 }])) {
    ctx.beginPath(); ctx.arc(0, S(m.my), S(1.0), 0, Math.PI * 2); ctx.fill();
  }

  if (set > .04) {
    for (const m of MASTS) {
      const hw = m.yard / 2;
      const yx = Math.cos(brace) * hw, yy = Math.sin(brace) * hw;
      // the course, and a shorter topsail yard just above it: two yards
      // is what says "ship" from overhead
      for (const [f, dy] of [[1, 0], [.68, -L * .035]]) {
        ctx.strokeStyle = c.trim;
        ctx.lineWidth = Math.max(1, S(f === 1 ? 1.0 : .7));
        ctx.beginPath();
        ctx.moveTo(S(-yx * f), S(m.my + dy - yy * f));
        ctx.lineTo(S(yx * f), S(m.my + dy + yy * f));
        ctx.stroke();
      }
      // the sail: a BAND of canvas hung from the yard, its foot blown
      // away downwind. A lens from tip to tip reads as a fin; a
      // trapezoid with a curved foot reads as square canvas.
      const bell = B * (.35 + .35 * drawing) * set;
      const dwx = -Math.sin(s.awa), dwy = Math.cos(s.awa);   // downwind
      const fx2 = .78;                       // the foot is a little narrower
      ctx.globalAlpha = .18 + .42 * set * (.35 + .65 * drawing);
      ctx.fillStyle = "#8d97a2";
      ctx.beginPath();
      ctx.moveTo(S(-yx), S(m.my - yy));
      ctx.lineTo(S(yx), S(m.my + yy));
      ctx.lineTo(S(yx * fx2 + dwx * bell), S(m.my + yy * fx2 + dwy * bell));
      ctx.quadraticCurveTo(S(dwx * bell * 1.6), S(m.my + dwy * bell * 1.6),
                           S(-yx * fx2 + dwx * bell), S(m.my - yy * fx2 + dwy * bell));
      ctx.closePath();
      ctx.fill();
      ctx.globalAlpha = 1;
    }
    // the lateen mizzen, out to leeward
    const out = B * 1.1 * (.35 + .65 * set) * sgn;
    const my = L * .3, len = L * .22;
    ctx.strokeStyle = c.trim; ctx.lineWidth = Math.max(1, S(.8));
    ctx.beginPath();
    ctx.moveTo(0, S(my)); ctx.lineTo(S(out), S(my + len));
    ctx.stroke();
    ctx.globalAlpha = .14 + .34 * set * (.35 + .65 * drawing);
    ctx.fillStyle = "#98a3ae";
    ctx.beginPath();
    ctx.moveTo(0, S(my));
    ctx.quadraticCurveTo(S(out * .6), S(my + len * .45), S(out), S(my + len));
    ctx.lineTo(0, S(my + len));
    ctx.closePath(); ctx.fill();
    ctx.globalAlpha = 1;
    // headsail on the bowsprit: a spritsail, square and small
    const bx = Math.cos(brace) * B * .5, by = Math.sin(brace) * B * .5;
    const sy0 = -L * .5 - L * .16;
    ctx.strokeStyle = c.trim; ctx.lineWidth = Math.max(1, S(.6));
    ctx.beginPath();
    ctx.moveTo(S(-bx), S(sy0 - by)); ctx.lineTo(S(bx), S(sy0 + by));
    ctx.stroke();
    const sbell = B * .3 * set;
    const sdx = -Math.sin(s.awa) * sbell, sdy = Math.cos(s.awa) * sbell;
    ctx.globalAlpha = .14 + .3 * set * drawing;
    ctx.fillStyle = "#98a3ae";
    ctx.beginPath();
    ctx.moveTo(S(-bx), S(sy0 - by));
    ctx.lineTo(S(bx), S(sy0 + by));
    ctx.lineTo(S(bx * .75 + sdx), S(sy0 + by * .75 + sdy));
    ctx.lineTo(S(-bx * .75 + sdx), S(sy0 - by * .75 + sdy));
    ctx.closePath(); ctx.fill();
    ctx.globalAlpha = 1;
  }
  ctx.restore();
}
