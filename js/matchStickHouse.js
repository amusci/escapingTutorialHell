/*

    6 match Sticks(1 house/1 step) ==>(1 * 5) + 1
    11 match Sticks(2 house/2 step)==> (2 * 5) + 1
    16 match Sticks(3 house/3 step)==> (3 * 5) + 1
    21 match Sticks(4 house/4 step)==> (4 * 5) + 1
*/

function matchHouses(step) {

    if (step === 0) {

        return 0

    } else {

        return (step * 5) + 1

    }

}