"""

Create a function that takes a string and returns True or False, depending on whether the characters are in order or not.

"""

def is_in_order(txt):
    n = len(txt)
    count = 0
    in_order = sorted(txt)
    for i in range(n):
        if txt[i] == in_order[i]:
            count += 1
    if count == n:
        return True
    else:
        return False