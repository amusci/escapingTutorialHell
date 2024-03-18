"""

Create a function that takes three integer arguments (a, b, c)

and returns the amount of integers which are of equal value.

"""


def equal(a, b, c):
    unique = set([a, b, c])
    if len(unique) == 3:
        return 0
    else:
        return 4 - len(unique)