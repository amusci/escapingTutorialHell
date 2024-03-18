"""

Create a function which validates whether a 3 character string is a vowel sandwich.

In order to have a valid sandwich, the string must satisfy the following rules:

    The first and last characters must be a consonant.
    The character in the middle must be a vowel.

"""


def is_vowel_sandwich(s):
    vowels = "aeiou"
    if len(s) != 3:
        return False
    elif s[1] in vowels and s[0] not in vowels and s[2] not in vowels:
        return True
    else:
        return False