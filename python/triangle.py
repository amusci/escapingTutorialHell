"""

This Triangular Number Sequence is generated from a pattern of dots that form a triangle. The first 5 numbers of the sequence, or dots, are:

1, 3, 6, 10, 15

This means that the first triangle has just one dot, the second one has three dots, the third one has 6 dots and so on.

Write a function that returns the number of dots when given its corresponding triangle number of the sequence.

"""


def triangle(n):
    ans = 0
    if n == 1:
        return 1
    else:
        for i in range(n + 1):
            ans += i # 1 + 2 + 3 + 4 + 5 + ... + n + (n+1)

    return round(ans)