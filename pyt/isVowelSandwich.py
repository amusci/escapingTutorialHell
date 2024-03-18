"""

Create a function which validates whether a 3 character string is a vowel sandwich.

In order to have a valid sandwich, the string must satisfy the following rules:

    The first and last characters must be a consonant.
    The character in the middle must be a vowel.

"""


def is_vowel_sandwich(s):
    return [c in "aeiou" for c in s] == [False, True, False]