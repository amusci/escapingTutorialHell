/*
Given a number, return an array containing the two halves of the number. If the number is odd, make the rightmost number higher.
*/

const numberSplit = (n) =>
  n % 2 == 0 ? [n / 2, n / 2] : [Math.floor(n / 2), Math.ceil(n / 2)];

console.log(numberSplit(-11));
