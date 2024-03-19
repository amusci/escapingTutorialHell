"""

Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list.

If Bob is not in the list, return -1.

"""




def find_bob(names):
    for index,name in enumerate(names):
        if name == 'Bob':
            return index
    return -1