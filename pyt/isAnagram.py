"""

Create a function that takes two strings and returns either True or False depending on whether they're anagrams or not.

"""

def is_anagram(s1, s2):
    return sorted(s1.upper())==sorted(s2.upper())