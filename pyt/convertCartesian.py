'''

Create a function that converts two lists of x- and y- coordinates into a list of (x, y) coordinates.

'''


def convert_cartesian(x, y):
    return [[i, j] for i, j in zip(x, y)]