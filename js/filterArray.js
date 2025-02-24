/*
Create a function that takes an array of non-negative integers and strings and return a new array without the strings.
*/

function filterArray(arr) {
  return arr.filter((x) => typeof x === "number");
}

console.log(filterArray([1, 2, "aasf", "1", "123", 123]));
