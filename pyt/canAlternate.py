"""

You will be implementing a basic case of the map-reduce pattern in programming.

Given a vector stored as a list of integers, find the magnitude of the vector.

Use the standard distance formula for n-dimensional Cartesian coordinates.

"""


def can_alternate(s):
    zero_count = s.count('0')
    one_count = s.count('1')
    if abs(zero_count - one_count) >=2:
        return False
    else:
        return True