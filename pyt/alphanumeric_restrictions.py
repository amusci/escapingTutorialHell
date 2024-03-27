'''

Create a function that returns True if the given string has any of the following:

    Only letters and no numbers.
    Only numbers and no letters.

If a string has both numbers and letters, or contains characters which don't fit into any category, return False
'''

def alphanumeric_restriction(s):
    if not s:
        return False

    for char in s:
        if not char.isalnum():
            return False

    has_letters = any(char.isalpha() for char in s)
    has_numbers = any(char.isdigit() for char in s)

    if has_numbers == True and has_letters == True:
        return False
    return True