"""

Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.

"""


def mapping(letters):
    return {l:l.upper() for l in letters}