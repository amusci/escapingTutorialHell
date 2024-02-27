"""

Create a function that returns the mean of all digits.

"""


def mean(num):
    count = 0
    n = len(str(num))
    for i in str(num):
        count += int(i)
    return count // n