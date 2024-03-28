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


def decay(m, n):
    ans = m
    for i in range(n):
        ans /= 2

    return ans


def halflife_calculator(mass, hlife, n):
    mass_decay = decay(mass, n)
    return [round(mass_decay, 3), round(hlife * n, 3)]


if __name__ == "__main__":
    print(halflife_calculator(1000, 5730, 2))