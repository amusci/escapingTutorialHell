'''

Create a function, that will for a given a, b, c, do the following:

    Add a to itself b times.
    Check if the result is divisible by c.

abcmath(42, 5, 10) ➞ False
# 42+42 = 84,84+84 = 168,168+168 = 336,336+336 = 672, 672+672 = 1344
# 1344 is not divisible by 10

abcmath(5, 2, 1) ➞ True

abcmath(1, 2, 3) ➞ False

'''


def abcmath(a, b, c):

    ans = a
    for _ in range(b - 1):
        ans += ans
    if ans % c == 0:
        return True
    else:
        return False