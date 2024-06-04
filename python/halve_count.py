"""

Given two integers a and b, return how many times a can be halved while still being greater than b.

"""


def halve_count(a, b):
    n = 0

    while a / 2 > b:
        n += 1
        a /= 2

    return n