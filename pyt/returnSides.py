'''

Given the shortest side of a 30° by 60° by 90° triangle, find out the other two sides.


Return the longest side and medium-length side in that order.

'''
import math


def returnsides(length):
    return length * 2, round(length * math.sqrt(3), 2)