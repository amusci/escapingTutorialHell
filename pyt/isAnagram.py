"""

Create a function that takes two strings and returns either True or False depending on whether they're anagrams or not.

"""

def is_anagram(s1, s2):
    clean_s1 = s1.lower()
    clean_s2 = s2.lower()

    s_1 = list(clean_s1)
    s_2 = list(clean_s2)
    print(s_1,s_2)
    s_1.sort()
    s_2.sort()
    if s_1 == s_2:
        return True

    return False