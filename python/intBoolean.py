"""

Create a function which returns a list of booleans, from a given number.

Iterating through the number one digit at a time, append True if the digit is 1 and False if it is 0.

"""

def integer_boolean(n):
    return [i == '1' for i in n]