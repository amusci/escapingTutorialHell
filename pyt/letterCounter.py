"""

Create a function that counts the number of times a particular letter shows up in the word search.

"""

def letter_counter(lst, letter):
    count = 0

    for i in lst:
        for j in range(0,6):
            if i[j] == letter:
                count+=1
    return count