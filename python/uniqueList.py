'''

In each input list, every number repeats at least once, except for two. Write a function that returns the two unique numbers.

'''

def return_unique(lst):
    ans = []
    for i in lst:
        
        if lst.count(i) == 1:
            print(i)
            ans.append(i)
        
    return ans