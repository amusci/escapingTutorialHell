"""

Create a function that takes three integer arguments (a, b, c)

and returns the amount of integers which are of equal value.

"""


def equal(a, b, c):
    if a == b == c:
        return 3
    elif a == b or b == c or a == c:
        return 2
    else:
        return 0