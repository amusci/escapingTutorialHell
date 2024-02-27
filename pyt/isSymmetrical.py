"""

Create a function that takes a number as an argument and returns True or False
depending on whether the number is symmetrical or not.

A number is symmetrical when it is the same as its reverse.

"""


def is_symmetrical(num):
    n = len(str(num))
    if n == 1:
        return True
    else:
        if str(num)[::-1] == str(num):
            return True
    return False
