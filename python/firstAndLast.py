"""

Write a function that returns the lexicographically first and lexicographically last rearrangements of a lowercase string.

Output the results in the following manner:

"""

def first_and_last(s):
    sorted_s = ''.join(sorted(s))
    return [sorted_s, sorted_s[::-1]]