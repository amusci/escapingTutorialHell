"""

Create a function that takes a list of numbers and returns the number that's unique.

"""


def unique(lst):
    counts = {}
    for num in lst:
        counts[num] = counts.get(num,0) + 1

    for num,count in counts.items():
        if count == 1:
            return num

    return None
