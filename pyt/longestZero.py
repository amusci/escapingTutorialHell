
'''

Write a function that returns the longest sequence of consecutive zeroes in a binary string.

'''


def longest_zero(s):
    lenny = len(s)
    ans = ''
    max_ans = ''

    for i in range(lenny):
        if s[i] == '0':
            ans += s[i]
        else:
            if len(ans) > len(max_ans):
                max_ans = ans
            ans = ''

    if len(ans) > len(max_ans):
        max_ans = ans

    return max_ans