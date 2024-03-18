"""

You will be implementing a basic case of the map-reduce pattern in programming.

Given a vector stored as a list of integers, find the magnitude of the vector.

Use the standard distance formula for n-dimensional Cartesian coordinates.

"""

def can_alternate(s):
    return s.count("0") - s.count("1") in [-1, 0, 1]