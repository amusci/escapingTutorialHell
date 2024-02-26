"""

Create a function that takes in two lists and returns True if the second list follows the first list by one element, and False otherwise.

In other words, determine if the second list is the first list shifted to the right by 1.

"""


def simon_says(lst1, lst2):
    count = 0
    n = len(lst1)
    for i in range(n - 1):
        print(lst1[i], lst2[i + 1])
        if lst1[i] == lst2[i + 1]:
            count += 1
    if count == n - 1:
        return True
    else:
        return False