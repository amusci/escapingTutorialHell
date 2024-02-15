"""
Create a function that takes a string and returns a string in which each character is repeated once.
"""


def double_char(txt):
    new = ""
    for i in txt:
        new += i * 2

    return new
