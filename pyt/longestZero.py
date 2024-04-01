
'''

Write a function that returns the longest sequence of consecutive zeroes in a binary string.

'''


def longest_zero(s):
    longest = 0
    answer = longest

    for i in s:
        if i == "0":
            longest += 1
        else:
            answer = max(longest, answer)
            longest = 0
    return "0" * max(longest,answer)
