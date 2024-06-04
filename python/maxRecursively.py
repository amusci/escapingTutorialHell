'''
Create a function that finds the highest integer in the list using recursion.

'''

'''
EXAMPLES:

find_highest([-1, 3, 5, 6, 99, 12, 2]) ➞ 99

find_highest([0, 12, 4, 87]) ➞ 87

find_highest([8]) ➞ 8
'''


def find_highest(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        #print(lst[1:])
        m = find_highest(lst[1:])
        print(m)
        if m > lst[0]:
            return m
        else:
            return lst[0]



