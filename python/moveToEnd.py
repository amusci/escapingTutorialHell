"""
Write a function that moves all elements of one type to the end of the list.


What I learned: iterate over  acopy of the list if you're going to manipulating the data in the list

lst[:]
"""


def move_to_end(lst, el):
    end = []
    for i in lst[:]:  # Iterate over a copy of lst
        if i == el:
            lst.remove(i)
            end.append(i)
    lst.extend(end)
    return lst