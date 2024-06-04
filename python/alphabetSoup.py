"""

Create a function that takes a string and returns a string with its letters in alphabetical order.

"""


def alphabet_soup(txt):
    sort = sorted(txt)
    ans = []
    for i in sort:
        ans.append(i)
    return ''.join(ans)