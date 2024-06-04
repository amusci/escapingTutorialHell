"""

Given an unsorted list, create a function that returns the nth smallest integer

(the smallest integer is the first smallest,the second smallest integer is the second smallest, etc).

"""

def nth_smallest(lst, n):
    try:
        sorted_list = sorted(lst)
        for i in sorted_list:
            return sorted_list[n - 1]
    except IndexError:
        return None