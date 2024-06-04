"""

Write a function that takes a year and returns its corresponding century.

"""


import math

def century_from_year(year):
    return math.ceil(year / 100)
