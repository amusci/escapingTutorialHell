"""

Create a function that replaces all the vowels in a string with a specified character.

"""


def replace_vowels(txt, ch):
    vowels = set('aeiouAEIOU') # include caps
    ans = "" # empty string
    for char in txt: # go thru each character in the txt
        if char in vowels: # if a char is in the vowels set
            ans += ch # add ch where the vowel is supposed to be
        else:
            ans += char # add the character to new
    return ans