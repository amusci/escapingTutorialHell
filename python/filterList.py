def filter_list(lst):
    ans = [] # initalize answer list

    for i in lst: # iterate through the list
        if isinstance(i, int): # if i is an integer
            ans.append(i) #  append to the final list
    return ans #return ans