"""

Create a function that returns the sum of all even elements in a 2D matrix.

"""


def sum_of_evens(lst):
    even_sum = 0
    for row in lst:
        for element in row:
            if element % 2 == 0:
                even_sum += element

    return even_sum