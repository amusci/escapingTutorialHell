'''

to_list(), which converts a number to an integer list of its digits.
to_number(), which converts a list of integers back to its number.

'''


def to_list(num):
    ans = []
    for i in str(num):
        ans.append(int(i))
    return ans


def to_number(lst):
    ans = ''
    for num in lst:
        ans += str(num)
    return int(ans)
