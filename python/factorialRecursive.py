"""
Write a function that calculates the factorial of a number recursively.
"""


def factorial(n):

    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)