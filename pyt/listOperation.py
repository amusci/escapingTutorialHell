"""

Create a function that takes three parameters where:

    x is the start of the range (inclusive).
    y is the end of the range (inclusive).
    n is the divisor to be checked against.

Return an ordered list with numbers in the range that are divisible by the third parameter n.

Return an empty list if there are no numbers that are divisible by n.

"""


def list_operation(x, y, n):
    return [i for i in range(x, y + 1) if not i % n]
