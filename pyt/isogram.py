"""

An isogram is a word that has no duplicate letters.

Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".

"""

def is_isogram(txt):
    lower = txt.lower()
    for i in lower:
        if lower.count(i) > 1:
            return False

    return True
