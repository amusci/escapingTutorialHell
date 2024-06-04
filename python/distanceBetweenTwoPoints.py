"""

In this challenge, you have to find the distance between two points placed on a Cartesian plane.

Knowing the coordinates of both the points, you have to apply the Pythagorean theorem to find the distance between them.

Given two dictionaries a and b being the two points coordinates (x and y),

implement a function that returns the distance between the points, rounded to the nearest thousandth.
"""

def get_distance(a, b):
    return round(math.sqrt((a['x'] - b['x']) ** 2 + (a['y'] - b['y']) ** 2), 3)