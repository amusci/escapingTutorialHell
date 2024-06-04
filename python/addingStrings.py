"""

Create a function that takes two number strings and returns their sum as a string.

"""


def add(n1, n2):
    if n1 and n2:
        wee = int(n1) + int(n2)
        return '{}'.format(wee)
    else:
        return "Invalid Operation"