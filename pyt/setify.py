"""

Create a function that sorts a list and removes all duplicate items from it.

"""


def setify(lst):
    lst.sort()
    ans = []
    seen = set()
    for i in lst:
        if i not in seen:
            ans.append(i)
            seen.add(i)

    return ans