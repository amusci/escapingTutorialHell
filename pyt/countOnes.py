"""

Count the amount of ones in the binary representation of an integer. For example, since 12 is 1100 in binary,

the return value should be 2.

"""


def count_ones(num):
    return bin(num).count('1')