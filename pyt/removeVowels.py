"""
Create a function that takes a string and returns a new string with all vowels removed.

"""


def remove_vowels(txt):
    vowels = 'aeiouAEIOU'
    result = ''
    length = len(txt)
    for i in range(0,length):
        if txt[i] not in vowels:
            result += txt[i]

    return result