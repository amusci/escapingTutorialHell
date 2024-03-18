"""

Write a function that replaces all vowels in a string with a specified vowel.

"""


def vow_replace(word, vowel):

    vowels = 'aeiou'
    ans = ''
    for char in word:
        if char in vowels:
            ans += vowel
        else:
            ans += char
    return ans
