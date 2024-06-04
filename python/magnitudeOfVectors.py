"""

You will be implementing a basic case of the map-reduce pattern in programming.

Given a vector stored as a list of integers, find the magnitude of the vector.

Use the standard distance formula for n-dimensional Cartesian coordinates.

"""

import math

def magnitude(lst):
    squared_sum = sum(i**2 for i in lst)
    return math.sqrt(squared_sum)