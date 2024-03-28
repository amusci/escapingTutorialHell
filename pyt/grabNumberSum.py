import re

'''

Given a string including a bunch of characters and numbers, return the sum of all the numbers in the string.

Note that multiple digits next to each other are counted as a whole number rather than separate digits.

'''


def grab_number_sum(s):
    total = 0
    nums = re.findall(r'\d+', s)
    for i in nums:
        total += int(i)
    return total