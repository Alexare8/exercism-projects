// @ts-check


export function dayRate(ratePerHour) {
  return 8 * ratePerHour;
}

export function daysInBudget(budget, ratePerHour) {
  return Math.floor(budget / dayRate(ratePerHour));
}

export function priceWithMonthlyDiscount(ratePerHour, numDays, discount) {
  const daysPerMonth = 22;
  var dayPay = dayRate(ratePerHour);
  return Math.ceil(Math.floor(numDays / daysPerMonth) * dayPay * daysPerMonth * (1 - discount) + numDays % daysPerMonth * dayPay);
}
