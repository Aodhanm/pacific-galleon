// =====================================================================
// PACIFIC GALLEON: the water, for now.
//
// This is the open sea off the cape, BEFORE the land goes in. It keeps
// exactly the interface doghole's cove.js kept (depthAt, onLand,
// distToShore, windShadow), so when cape.js arrives with the real Cabo
// San Lucas shore, soundings and rocks, nothing that calls these needs
// to change. Until then: blue water, deep everywhere, no lee.
//
// UNITS: yards. x runs east, y runs south (canvas-friendly), as in
// doghole. The origin will become the tip of the cape (Land's End) when
// the coast goes in; the galleon's track runs NW to SE past it.
// =====================================================================

export const YD_PER_NM = 2027;
export const KN = YD_PER_NM / 3600;          // 1 knot in yards per second

export function depthAt(x, y) { return 300; }   // feet. Blue water.
export function onLand(x, y) { return false; }
export function distToShore(x, y) { return 1e9; }
export function windShadow(x, y, windFromDeg) { return 0; }

// ------------------------------------------------------------ weather
// The eastbound Manila galleon made the coast high up and ran DOWN Baja
// for the cape in the northern winter, with the NW wind and the
// California Current astern. So the standing weather here is a fresh
// norther to north-wester, and the set runs to the south-east along the
// coast. (Rates are playable, not hindcast; the DIRECTIONS are the
// documented pattern. VERIFY exact seasonal ranges before the sources
// table ships.)
export function makeWeather() {
  return {
    t: 0,
    windFrom: 305 + Math.random() * 30,        // NW quarter
    windKn: 11 + Math.random() * 8,
    setDeg: 135 + Math.random() * 20,          // the set runs SE, coastwise
    setKn: .4 + Math.random() * .5,
    swell: .12 + Math.random() * .08,
    swellDir: 315,                             // out of the NW, astern of her
    swellRate: .5,
    curX: 0, curY: 0,
  };
}

export function weatherStep(env, dt) {
  env.t += dt;
  // the wind breathes: slow swings of a point or so either way, never a
  // trap. The chase is decided by the polar, not by a header.
  const breathe = Math.sin(env.t * .017) * 9 + Math.sin(env.t * .041) * 4;
  env.windNow = env.windFrom + breathe;
  env.windKnNow = env.windKn * (.88 + .12 * Math.sin(env.t * .03 + 2));
  const dir = env.setDeg * Math.PI / 180;
  const mag = env.setKn * KN;
  env.curX = Math.sin(dir) * mag;
  env.curY = -Math.cos(dir) * mag;
}
