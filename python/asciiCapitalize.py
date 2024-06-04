"""
Create a function that takes a string as input and capitalizes a letter if its ASCII code is even and returns its lower case version if its ASCII code is odd.

"""


def ascii_capitalize(txt):
    ans = ''
    for i in txt:
        if ord(i) % 2 != 0:
            ans += i.lower()
        else:
            ans += i.upper()
    return ans