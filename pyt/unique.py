"""

Create a function that takes a list of numbers and returns the number that's unique.

"""


def unique(lst):
    def unique(lst):
        for num in lst:
            if lst.count(num) == 1:
                return num
