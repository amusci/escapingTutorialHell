/*

Write a function that takes a two-digit number and determines if it's the largest of two possible digit swaps.

To illustrate:

largestSwap(27) ➞ false

largestSwap(43) ➞ true

*/

function largestSwap(num) {

    let swap = num.toString();
    swap = swap.split("").reverse().join("");

    swap = parseInt(swap, 10);
    
    return num >= swap;
	
}
