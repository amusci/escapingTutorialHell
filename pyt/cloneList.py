"""

clone list

"""


def clone(lst):
    newlst = []
    for i in lst:
        newlst.append(i)
    newlst.append(lst)
    return newlst
