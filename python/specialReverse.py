'''

Write a function that reverses all the words in a sentence that start with a particular letter.

'''


def special_reverse(s, c):
    ans = ''
    splitted = s.split(" ")
    for word in splitted:
        if word.startswith(c):
            word = word[::-1]
            ans += word + " "
        else:
            ans += word + " "
    return ans.rstrip()