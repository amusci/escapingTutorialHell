"""

Create a function that returns the number of palindrome numbers in a specified range (inclusive).

For example, between 8 and 34, there are 5 palindromes: 8, 9, 11, 22 and 33.

Between 1550 and 1552 there is exactly one palindrome: 1551.

"""


def count_palindromes(num1, num2):
    count = 0
    for i in range(num1, num2 + 1):
        if str(i) == str(i)[::-1]:
            count += 1
    return count