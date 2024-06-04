"""

Write a function that replaces all vowels in a string with a specified vowel.

"""


def vow_replace(word, vowel):

    vowels = 'aeiou'
    for char in word:
        if char in vowels:
            word = word.replace(char, vowel)
    return word
