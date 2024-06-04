"""

Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.

"""


def missing_numBF(lst):
    FIXED_AMOUNT = 55
    total = sum(lst)
    return FIXED_AMOUNT - total
