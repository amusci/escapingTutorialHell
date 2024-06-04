"""

Create a function that takes a list of items,

removes all duplicate items and returns a new list in the same sequential order as the old list (minus duplicates).

"""




def remove_dups(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)

    return seen