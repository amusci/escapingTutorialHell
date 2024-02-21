"""

Create a function that takes a number num and returns its length.

"""

def number_length(num):
    count = 0
    for n in str(num):
        count += 1

    return count