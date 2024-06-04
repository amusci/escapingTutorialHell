"""

Write a function that removes any non-letters from a string, returning a well-known film title.

"""


def letters_only(txt):
    ans = []
    for i in txt:
        if i.isalpha():
            ans.append(i)
    return ''.join(ans)