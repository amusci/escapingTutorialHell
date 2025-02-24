/*
Create a function that takes an array of numbers and returns the second largest number.
*/

function secondLargest(arr) {
  return arr.sort((a, b) => b - a)[1];
}

console.log(secondLargest([3, 4, 7, 1, 2]));
