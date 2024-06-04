"""

Create a function that counts the number of times a particular letter shows up in the word search.

"""

def letter_counter(lst, letter):
    count = 0

    for i in lst:
        count += i.count(letter)
    return count