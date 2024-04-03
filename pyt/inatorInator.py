'''

Create a function that takes a single word string and does the following:

    Concatenates inator to the end if the word ends with a consonant, otherwise, concatenate -inator instead.

    Adds the word length of the original word to the end, supplied with "000".

The examples should make this clear.

'''


def inator_inator(inv):
    n = str(len(inv))
    if inv[-1] in 'aeiouAEIOU':
        inv += '-inator'
    else:
        inv += 'inator'

    return inv + " " + n + '000'