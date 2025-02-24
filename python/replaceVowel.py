'''

Create a function that takes a string and replaces the vowels with another character.

    a = 1
    e = 2
    i = 3
    o = 4
    u = 5

'''

def replace_vowel(word):
    ans = ""
    rules = {

        "a" : "1",
        "e" : "2",
        "i" : "3",
        "o" : "4",
        "u" : "5"

    }

    for i in word:
        if i in rules:
            ans += rules[i]
        else:
            ans += i
    return ans



if __name__ == "__main__":
    print(replace_vowel("khandbari"))