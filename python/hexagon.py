'''

Given the side length x find the area of a hexagon.

'''

import math

def area_of_hexagon(x):
    if x > 0:
        return round((3 * math.sqrt(3) * x ** 2) / 2, 1)

	


if __name__ == "__main__":
    print(area_of_hexagon(1.1))