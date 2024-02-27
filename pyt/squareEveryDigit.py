"""

Create a function that squares every digit of a number.

"""


def square_digits(n):
    ans = ''
    for i in str(n):
        ans += str(int(i) ** 2)
    return int(ans)