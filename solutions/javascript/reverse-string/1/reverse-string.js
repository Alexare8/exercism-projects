export const reverseString = (inputString) => {
  var reversed = '';
  for (let i in inputString) {
    reversed = inputString[i] + reversed;
  };
  return reversed;
};
