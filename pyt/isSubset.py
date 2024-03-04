"""

Create a function that returns True if the first list is a subset of the second. Return False otherwise.

"""


def is_subset(lst1, lst2):
    for n in lst1:
        if n not in lst2:
            return False
    return True