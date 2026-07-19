// @ts-check
export function canExecuteFastAttack(knight) {
  return !knight;
}

export function canSpy(knight, archer, prisoner) {
  return knight || archer || prisoner;
}

export function canSignalPrisoner(archer, prisoner) {
  return !archer && prisoner;
}

export function canFreePrisoner(
  knight,
  archer,
  prisoner,
  dog,
) {
  return !archer && (dog || (prisoner && !knight));
}