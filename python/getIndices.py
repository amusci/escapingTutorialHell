'''

Create a function that returns the indices of all occurrences of an item in the list.

'''

def get_indices(lst, el):
    ans = []
    for i, n in enumerate(lst):
        if n == el:
            ans.append(i)
    return ans


	



if __name__ == "__main__":
    print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))

