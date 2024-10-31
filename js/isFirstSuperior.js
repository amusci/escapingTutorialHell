/*

You will be given two extremely similar arrays, but exactly one of the items in an array will be valued slightly higher than its counterpart (which means that evaluating the value > the other value will return true).

Create a function that returns whether the first array is slightly superior to that of the second.
*/

function isFirstSuperior(arr1, arr2) {

    for (let i = 0; i < arr1.length; i++) {

        if (arr1[i] > arr2[i]) {

            return true;

        } else if (arr1[i] < arr2[i]) {


            return false;
        }

    }

    return false;
	
}