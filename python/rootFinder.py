"""

Create a function to find only the root value of x in any quadratic equation ax^2 + bx + c.

The function will take three arguments:

    a as the coefficient of x^2
    b as the coefficient of x
    c as the constant term

    x = (-b ± √(b^2 - 4ac)) / (2a)

"""

import math


def quadratic_equation(a, b, c):
    disc = b ** 2 - 4 * a * c
    if disc >= 0:
        root = (-b + math.sqrt(disc)) / (2 * a)
        return root
    else:
        return None