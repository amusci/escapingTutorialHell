'''

Create a function that takes a list of numbers and returns the sum of the two lowest positive numbers.

'''

def sum_two_smallest_nums(lst):

    lst = sorted([num for num in lst if num >= 0])
    return lst[0] + lst[1]