"""

Given two integers a and b, return how many times a can be halved while still being greater than b.

"""


def halve_count(a, b):
    n = a / 2
    if n > b:
        return 1 + halve_count(n, b)
    else:
        return 0
