"""

Create a function that takes a string and returns True or False, depending on whether the characters are in order or not.

"""

def is_in_order(txt):
    sorted_txt = sorted(txt)
    sorted_string = "".join(sorted_txt)
    if sorted_string == txt:
        return True
    else:
        return False