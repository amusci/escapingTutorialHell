'''Write a function that takes a string and calculates the number of letters and digits within it.

Return the result in a dictionary.'''


def count_all(txt):
    return {"LETTERS": sum (c.isalpha() for c in txt),
    "DIGITS": sum(c.isdigit() for c in txt)}