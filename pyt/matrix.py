'''

Write a function that takes three arguments (x, y, z) and returns a list containing x sublists

(e.g. [[], [], []]), each containing y number of item z.

    x Number of sublists contained within the main list.
    y Number of items contained within each sublist.
    z Item contained within each sublist.

'''

def matrix(x, y, z):
    ans =[]
    for sublists in range(x):
        ans.append([z] * y)
    return ans