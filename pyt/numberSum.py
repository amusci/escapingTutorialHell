"""

Write a function that replaces all vowels in a string with a specified vowel.

"""


def numbers_sum(lst):
    ans = 0
    for i in lst:
        if isinstance(i, int) and not isinstance(i, bool):  # True is 1 so we must avoid that
            ans += i
    return ans