"""

Write a function that takes a string, breaks it up and returns it with vowels first, consonants second.

For any character that's not a vowel (like special characters or spaces), treat them like consonants.

"""

def split(txt):
    vowel = ''.join(ch for ch in txt if ch in 'aeiou')
    con = ''.join(ch for ch in txt if ch not in 'aeiou')

    return vowel + con