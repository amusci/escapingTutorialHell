/* Create a function that takes an array of numbers and return "Boom!" if the digit 7 appears in the array. Otherwise, return "there is no 7 in the array". */

function sevenBoom(arr) {
  const stringfy = arr.toString();

  if (stringfy.includes(7)) {
    return "Boom!";
  } else {
    return "there is no 7 in the array";
  }
}

console.log(sevenBoom([2, 55, 60, 97, 86]));
