"""An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 typically using all the original letters exactly once."""


def isAnagram(s, t):
    if len(s) != len(t):  # if the lengths of the strings dont match
        return False  # return false

    countS, countT = {}, {}  # creating the hashmaps

    for i in range(len(s)):  # iterate the length of the string
        countS[s[i]] = 1 + countS.get(s[i], 0)  # increment the count of each character in string s
        countT[t[i]] = 1 + countT.get(t[i], 0)  # increment the count of each character in string t

    for c in countS: # iterate through countS
        if countS[c] != countT.get(c, 0): # if the character amount in countS != countT
            return False # they arent anagrams

    return True # if it passes all those checks, it must be an anagram


if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))
