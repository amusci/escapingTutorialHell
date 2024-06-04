'''

Create a function that returns True if the given string has any of the following:

    Only letters and no numbers.
    Only numbers and no letters.

If a string has both numbers and letters, or contains characters which don't fit into any category, return False
'''

def alphanumeric_restriction(s):
    return s.isdigit() or s.isalpha()