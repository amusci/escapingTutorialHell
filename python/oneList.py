'''

Programmer Pete is trying to combine two lists inside one list into one without changing the order of the list nor
the type and because he's pretty advanced he made it without blinking, but I want you to make it, too.

'''


def one_list(lst):
    ans = []
    for l in lst:
        ans.extend(l)
    return ans
