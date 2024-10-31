/*

Create a function that takes an array of values resistance that are connected in series, and calculates the total resistance of the circuit in ohms. The ohm is the standard unit of electrical resistance in the International System of Units ( SI ).

*/

function seriesResistance(arr) {

    let result = 0;

    for (let num of arr) {

        result += num;

    }
	
    if (result > 1) {

        return result + " ohms";

    } else {

        return result + " ohm";

    }

}