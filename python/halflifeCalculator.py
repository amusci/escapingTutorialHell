'''

A half life is the amount of time for half of a radioactive substance to decay.

    After 1 half life, 50% of a substance will be left.
    After 2 half lives, 25% of a substance will be left.
    After 3 half lives, 12.5% of a substance will be left, etc...

Create a function which calculates the remaining mass and the number of years that it took for the substance to decay. You will be given:

    The mass of the substance.
    The time in years for a halflife to elapse.
    The number of half lives.

    halflife_calculator(1000, 5730, 2) ➞ [250, 11460]

# There are 2 half lives, so the mass decays from 1000 to 500, then from 500 to 250.
# Each halflife is 5730 years, and since there were 2, it took 11460 years in total.

'''


def halflife_calculator(mass, hlife, n):
    return [round(mass / n * 2, 3), hlife * n]


if __name__ == "__main__":
    print(halflife_calculator(1000, 5730, 2))