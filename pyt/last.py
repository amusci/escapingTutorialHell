"""

Write a function that retrieves the last n elements from a list.

"""


def last(a, n):
    if n > len(a):
        return "invalid"
    elif n == 0:
        return []
    else:
        return a[-n:]


if __name__ == "__main__":
    print(last([1, 2, 3, 4, 5], 3))
