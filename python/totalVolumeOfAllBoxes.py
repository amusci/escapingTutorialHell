"""

Given a list of boxes, create a function that returns the total volume of all those boxes combined together.

A box is represented by a list with three elements: length, width and height.

For instance, total_volume([2, 3, 2], [6, 6, 7], [1, 2, 1])
my
should return 266 since (2 x 3 x 2) + (6 x 6 x 7) + (1 x 2 x 1) = 12 + 252 + 2 = 266.

"""

def total_volume(*boxes):
    ans = 0
    for i in boxes:
        ans += (i[0]*i[1]*i[2])
    return ans