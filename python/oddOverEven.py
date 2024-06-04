'''

Given a list, return True if there are more odd numbers than even numbers, otherwise return False.

'''


def oddeven(lst):
    even = 0
    odd = 0

    for num in lst:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd > even