'''

Create a function that takes any non-negative number as an argument and returns it with its digits in descending order.

Descending order is when you sort from highest to lowest.

'''


def sort_descending(num):
    sorted_numbers = sorted(str(num))
    reversed_sorted = sorted_numbers[::-1]
    return ''.join(reversed_sorted)