'''

Create a function that will return an integer number corresponding to the amount of digits in the given integer num.
DO NOT USE STRINGS

'''


def num_of_digits(num):

    if num == 0:
        return 1
    count = 0
    while abs(num) >= 1:
        count += 1
        num /= 10
    return count