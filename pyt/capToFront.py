'''Create a function that moves all capital letters to the front of a word.'''


def cap_to_front(s):
    ans = ""
    for i in s:
        if i.isupper():
            ans += i
    for j in s:
        if j.islower():
            ans += j
    return ans