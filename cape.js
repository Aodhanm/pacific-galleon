// =====================================================================
// CABO SAN LUCAS, in plan, for play.
//
// The real geography, simplified the way doghole simplified Fort Ross:
// the right shapes in the right places at a playable scale, not a
// survey. What is here and true in KIND:
//  - LAND'S END: the narrow granite ridge running out to the southern
//    tip of Baja California, with the arch (El Arco) and its outlying
//    rocks at the very point. Granite, not sand.
//  - THE BAY (Bahia San Lucas), east of the ridge, a curve of sand
//    beach sheltered from the north-west. This is where a ship lies
//    hidden waiting: Cavendish's squadron watered and waited about
//    this cape in 1587, Rogers' in 1709.
//  - THE PACIFIC COAST running away west-north-west, cliffy, with
//    rocks close under the shore.
//  - DEEP WATER CLOSE TO: a submarine canyon heads almost at the
//    beach here, so the bank is steep and a galleon can pass close.
// ⚠ Exact outline and distances are INVENTED at plausible scale.
// ⛔ CORRECTED 2026-10-07: there is NO Anson plan of this bay. Anson was
// never at Cape San Lucas; the harbour plan in his Voyage (1748) is
// plate 31, Chequetan, on the Mexican mainland, and Cabo San Lucas
// appears nowhere in his printed plate list. See SOURCES-WORKING.md.
// The period authorities for this anchorage are WRITTEN, not drawn:
//  - Cavendish's own log, 1587: anchored in 12 fathoms, and "a
//    Southeast winde is the woorst" (Hakluyt XI).
//  - Shelvocke, 1726: anchor on the bank on the NORTHERN side in 16 to
//    8 fathoms, keep off the southern side where the bank "shelves away
//    very fast" into very deep water; he rode in 13 fathoms, half a
//    mile offshore, open to the sea from E by N to SE by S.
// Those three soundings are what the depth field should be built on.
// ⚠⚠ WHICH BAY IS STILL OPEN: Pretty puts it "within the said cape" and
// gives it a "faire fresh river"; Shelvocke puts it 2 leagues NE of the
// cape; modern Bahia San Lucas has no river. Do not redraw until that
// is settled.
//
// UNITS: yards. x east, y south. Origin = the tip of Land's End.
// =====================================================================

export const YD_PER_NM = 2027;
export const KN = YD_PER_NM / 3600;

// ---------------------------------------------------------------- land
// One polygon, coast drawn west to east, closed inland to the north.
export const LAND = [
  [-5200, -2600], [-5200, -1250],
  [-4300, -1150], [-3400, -1050], [-2600, -980], [-1900, -880],
  [-1300, -820], [-800, -760], [-430, -690],
  [-260, -620],                      // the west (Solmar) beach head
  [-190, -470], [-150, -330], [-115, -195], [-70, -75],
  [0, 0],                            // LAND'S END, the tip
  [85, -65], [125, -185], [155, -320], [205, -430],
  [330, -500],                       // round into the bay
  [560, -545], [860, -605],          // the Medano sand, curving away NE
  [1150, -665], [1420, -745], [1650, -835],
  [2000, -905], [2700, -965], [3600, -1025], [4600, -1105],
  [5200, -1165], [5200, -2600],
];

// the stretch of the outline that is SAND, for drawing: [start, end]
// indexes into LAND. West beach and the bay beach.
export const SAND_RUNS = [[8, 9], [18, 24]];
// the stretch that is the GRANITE ridge of Land's End
export const GRANITE_RUN = [9, 18];

// ------------------------------------------------------------ features
// The arch and its outliers off the tip, and rocks under the cliffs.
export const ROCKS = [
  { x: 25,  y: 70,  r: 22, high: 60, arch: true,  name: "the arch" },
  { x: 95,  y: 125, r: 14, high: 25, name: "the outer rock" },
  { x: -55, y: 95,  r: 12, high: 15, name: "the friars" },
  { x: -35, y: 160, r: 9,  awash: true, name: "the wash rock" },
  { x: 160, y: 40,  r: 10, awash: true, name: "the wash rock" },
  // close under the Pacific cliffs, as they are
  { x: -700,  y: -660, r: 14, awash: true,  name: "rocks under the cliffs" },
  { x: -1450, y: -720, r: 16, high: 12, name: "rocks under the cliffs" },
  { x: -2250, y: -850, r: 13, awash: true,  name: "rocks under the cliffs" },
  { x: -3100, y: -930, r: 15, high: 10, name: "rocks under the cliffs" },
  // off the east shore
  { x: 2400, y: -860, r: 12, awash: true, name: "the inshore rock" },
];

// ------------------------------------------------------------- THE VIGIA
// ⭐ The lookout hill, and it is a REAL place with a REAL name: the
// summit of the ridge between the Pacific beach and San Lucas Bay is
// marked Vigia on the charts, which is simply Spanish for "lookout"
// (Findlay has it at 527 ft, the Hydrographic Office at 627; they
// disagree). Anson, 1748, writing from captured Spanish instructions:
// "there is besides care taken at Cape St. Lucas to look out for any
// ship of the enemy, which might be cruising there to intercept her",
// the shore people signal her with fires, and her captain sends his
// launch in for "intelligence whether or no there are enemies on the
// coast" before he will commit. If he is told there are, he does not
// come on. That is the whole mechanic, and it was waiting in the source.
// See GAME.md.
// Placed on the ridge close above the tip rather than far inland, so
// that the player's run out round the point actually passes under it
// and the fires are something you SEE go up, not a number on a bar.
export const VIGIA = { x: 55, y: -210, high: 527 };

// Are you tucked under the land, or showing yourself to his water? The
// bay east of the ridge is the hiding place. Everything south and west
// of the point is in his view.
export function inShelter(x, y) {
  return x > 180 && y < -180;
}

// where you lie in wait, inside the bay under the lee of the ridge
export const AMBUSH = { x: 620, y: -330, hdg: 195 };

// the galleon's track: down the Pacific coast offshore, round the
// cape, away east for the mainland crossing to Acapulco
export const LANE = [
  { x: -4800, y: 150 }, { x: -3200, y: 260 }, { x: -1800, y: 360 },
  { x: -700, y: 450 }, { x: 150, y: 520 }, { x: 1200, y: 640 },
  { x: 2800, y: 800 }, { x: 5200, y: 1000 },
];
export const ESCAPE_X = 4400;        // past this she is gone for Acapulco

// ------------------------------------------------------- geometry help
function segDist(px, py, ax, ay, bx, by) {
  const dx = bx - ax, dy = by - ay;
  const L2 = dx*dx + dy*dy || 1;
  let t = ((px-ax)*dx + (py-ay)*dy) / L2;
  t = Math.max(0, Math.min(1, t));
  return Math.hypot(px - (ax + t*dx), py - (ay + t*dy));
}
export function distToShore(x, y) {
  let m = 1e9;
  for (let i = 0; i < LAND.length; i++) {
    const a = LAND[i], b = LAND[(i+1) % LAND.length];
    m = Math.min(m, segDist(x, y, a[0], a[1], b[0], b[1]));
  }
  return m;
}
export function onLand(x, y) {
  let inside = false;
  for (let i = 0, j = LAND.length - 1; i < LAND.length; j = i++) {
    const [xi, yi] = LAND[i], [xj, yj] = LAND[j];
    if ((yi > y) !== (yj > y) &&
        x < (xj - xi) * (y - yi) / (yj - yi) + xi) inside = !inside;
  }
  return inside;
}

// depth: the bank is steep here (the canyon), so it deepens fast off
// the beach, faster still off the granite. Rocks carry their own
// shallows. Computed analytically here, then baked into a grid below so
// the live game only ever does a cheap lookup.
function depthRaw(x, y) {
  if (onLand(x, y)) return -4;
  let ft = Math.min(260, distToShore(x, y) * .5);
  for (const r of ROCKS) {
    const d = Math.hypot(x - r.x, y - r.y);
    if (d < r.r * 3) ft = Math.min(ft, (d - r.r) * .9);
  }
  return ft;
}

// ---- the depth grid, built once at load. depthAt() is then an O(1)
// bilinear lookup, so recolouring the water as the camera moves costs
// almost nothing (the old per-call coastline scan was the main lag).
const G = { x0: -6200, y0: -3000, x1: 6200, y1: 1600, cell: 36 };
G.nx = Math.ceil((G.x1 - G.x0) / G.cell) + 1;
G.ny = Math.ceil((G.y1 - G.y0) / G.cell) + 1;
const grid = new Float32Array(G.nx * G.ny);
(function buildDepth(){
  for (let j = 0; j < G.ny; j++)
    for (let i = 0; i < G.nx; i++)
      grid[j*G.nx + i] = depthRaw(G.x0 + i*G.cell, G.y0 + j*G.cell);
})();
export function depthAt(x, y) {
  const fx = (x - G.x0) / G.cell, fy = (y - G.y0) / G.cell;
  if (fx < 0 || fy < 0 || fx >= G.nx-1 || fy >= G.ny-1) return 260;  // open sea
  const i = fx|0, j = fy|0, tx = fx-i, ty = fy-j;
  const a = grid[j*G.nx+i], b = grid[j*G.nx+i+1];
  const c = grid[(j+1)*G.nx+i], d = grid[(j+1)*G.nx+i+1];
  return (a*(1-tx)+b*tx)*(1-ty) + (c*(1-tx)+d*tx)*ty;
}

// the ridge gives the bay its lee in the north-west wind, which is
// exactly why it is the anchorage. Deep in the bay your sails go soft;
// work her out to the point before you need full way.
export function windShadow(x, y, windFromDeg) {
  const r = windFromDeg * Math.PI / 180;
  const ux = -Math.sin(r), uy = Math.cos(r);       // downwind
  let shade = 0;
  for (let i = GRANITE_RUN[0]; i <= GRANITE_RUN[1]; i++) {
    const a = LAND[i];
    const dx = x - a[0], dy = y - a[1];
    const along = dx * ux + dy * uy;
    if (along < 0 || along > 420) continue;
    const across = Math.abs(dx * uy - dy * ux);
    if (across > 160) continue;
    shade = Math.max(shade, (1 - along / 420) * (1 - across / 160));
  }
  return Math.min(.55, shade);
}

// ------------------------------------------------------------ weather
// The winter pattern that brought the galleon: a fresh norther to
// north-wester running down the outer coast, the set going south-east
// along it, a long NW swell astern of her. Rates playable; directions
// are the documented pattern (VERIFY seasonal detail, PLAN.md).
export function makeWeather() {
  return {
    t: 0,
    windFrom: 305 + Math.random() * 30,
    windKn: 11 + Math.random() * 8,
    setDeg: 125 + Math.random() * 20,
    setKn: .4 + Math.random() * .5,
    swell: .12 + Math.random() * .08,
    swellDir: 315,
    swellRate: .5,
    curX: 0, curY: 0,
  };
}
export function weatherStep(env, dt) {
  env.t += dt;
  const breathe = Math.sin(env.t * .017) * 9 + Math.sin(env.t * .041) * 4;
  env.windNow = env.windFrom + breathe;
  env.windKnNow = env.windKn * (.88 + .12 * Math.sin(env.t * .03 + 2));
  const dir = env.setDeg * Math.PI / 180;
  const mag = env.setKn * KN;
  env.curX = Math.sin(dir) * mag;
  env.curY = -Math.cos(dir) * mag;
}

// an irregular outline per rock, doghole's
export function rockShape(seed, r, n = 9) {
  let s = (seed || 1) >>> 0;
  const rnd = () => (s = (s*1664525 + 1013904223) >>> 0) / 4294967296;
  const pts = [];
  for (let i = 0; i < n; i++) {
    const a = i / n * Math.PI * 2;
    const rr = r * (.62 + rnd() * .66);
    pts.push([Math.cos(a)*rr, Math.sin(a)*rr*.82]);
  }
  return pts;
}
