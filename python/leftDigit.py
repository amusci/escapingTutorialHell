"""

Write a function that takes a string as an argument and returns the left most integer in the string.

"""


def left_digit(num):
    nums = '1234567890'
    for i in num:
        if i in nums:
            return int(i)