/*
Create a function that validates whether a number n is within the bounds of lower and upper. Return false if n is not an integer.
*/

function intWithinBounds(n, lower, upper) {
  return Number.isInteger(n) && n >= lower && n < upper ? true : false;
}

console.log(intWithinBounds(4.5, 3, 8));
console.log(intWithinBounds(6, 1, 6));
console.log(intWithinBounds(4.5, 3, 8));
