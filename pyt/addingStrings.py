"""

Create a function that takes two number strings and returns their sum as a string.

"""


def add(n1, n2):
    if n1 is None or n1 is "" or n2 is None or n2 is "":
        return "Invalid Operation"
    else:
        wee = int(n1) + int(n2)
        return '{}'.format(wee)