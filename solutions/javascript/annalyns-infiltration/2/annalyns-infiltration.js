// @ts-check
export function canExecuteFastAttack(kAwake) {
  return !kAwake;
}
export function canSpy(kAwake, aAwake, pAwake) {
  return kAwake || aAwake || pAwake;
}
export function canSignalPrisoner(aAwake, pAwake) {
  return !aAwake && pAwake;
}
export function canFreePrisoner(
  kAwake,
  aAwake,
  pAwake,
  dPresent,
) {
  return !aAwake && (dPresent || (pAwake && !kAwake));
}