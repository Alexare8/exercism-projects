// @ts-check
/**
 * The fast attack is available when the knight is sleeping
 *
 * @param {boolean} knight
 *
 * @return {boolean} Whether or not you can execute a fast attack.
 */
export function canExecuteFastAttack(knight) {
  return !knight;
}

/**
 * A useful spy captures information, which they can't do if everyone's asleep.
 *
 * @param {boolean} knight
 * @param {boolean} archer
 * @param {boolean} prisoner
 *
 * @returns {boolean} Whether or not you can spy on someone.
 */
export function canSpy(knight, archer, prisoner) {
  return knight || archer || prisoner;
}

/**
 * You'll get caught by the archer if you signal while they're awake.
 *
 * @param {boolean} archer
 * @param {boolean} prisoner
 *
 * @returns {boolean} Whether or not you can send a signal to the prisoner.
 */
export function canSignalPrisoner(archer, prisoner) {
  return !archer && prisoner;
}

/**
 * The final stage in the plan: freeing Annalyn's best friend.
 *
 * @param {boolean} knight
 * @param {boolean} archer
 * @param {boolean} prisoner
 * @param {boolean} dog
 *
 * @returns {boolean} Whether or not you can free Annalyn's friend.
 */
export function canFreePrisoner(
  knight,
  archer,
  prisoner,
  dog,
) {
  return !archer && (dog || (prisoner && !knight));
}