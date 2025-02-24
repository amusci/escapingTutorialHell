/*

Given a string, reverse all the words which have odd length. The even length words are not changed.

*/

function reverseOdd(str) {
  const arrayOfWords = str.split(" ");

  for (let i = 0; i < arrayOfWords.length; i++) {
    if (arrayOfWords[i].length % 2 != 0) {
      arrayOfWords[i] = arrayOfWords[i].split("").reverse().join("");
    }
  }

  return arrayOfWords.join(" ");
}
