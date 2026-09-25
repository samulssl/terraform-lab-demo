// Punto de ruptura del plan gratuito (alternativa B).
// Uso: node estimar-costos.mjs --despliegues-mes 30 [--free-builds 500]
const args = Object.fromEntries(
  process.argv.slice(2).flatMap((a, i, arr) => {
    if (!a.startsWith("--")) return [];
    const key = a.slice(2);
    const val = arr[i + 1]?.startsWith("--") || arr[i + 1] === undefined ? "true" : arr[i + 1];
    return [[key, val]];
  })
);
const depMes = Number(args["despliegues-mes"] ?? 30);
const freeBuilds = Number(args["free-builds"] ?? 500);
console.log("A Lab (Docker+nginx): $0/mes. Sin ruptura de precio.");
console.log(`B gratuito: despliegues=${depMes}/mes builds_incluidos=${freeBuilds} cabe=${depMes <= freeBuilds ? "SI" : "NO"}`);
console.log(`RUPTURA_FREE: a x${(freeBuilds / depMes).toFixed(1)} (~${Math.floor(freeBuilds)} despliegues/mes). Luego plan pago o espaciar despliegues.`);
