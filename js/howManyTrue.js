/* Create a function which returns the number of true values there are in an array. */

function countTrue(arr) {

    let count = 0;

    arr.forEach(element => {
        
        if (element == true) {

            count++

        }

    });

    return count;
	
}