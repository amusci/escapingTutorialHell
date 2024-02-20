"""

Given the radius of a circle and the area of a square,
return True if the circumference of the circle is greater than the square's perimeter and False if the square's perimeter
is greater than the circumference of the circle.

"""
import math

def circle_or_square(rad, area):
    circum = 2 * math.pi * rad
    perim = math.sqrt(area) * 4

    if circum > perim:
        return True
    else:
        return False