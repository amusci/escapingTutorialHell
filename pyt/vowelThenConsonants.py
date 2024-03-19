"""

Write a function that takes a string, breaks it up and returns it with vowels first, consonants second.

For any character that's not a vowel (like special characters or spaces), treat them like consonants.

"""


def split(txt):
    vowel_string = ''
    vowel_list = 'aeiou'
    con_string = ''
    for char in txt:
        if char in vowel_list:
            vowel_string += char
        else:
            con_string += char
    return vowel_string + con_string