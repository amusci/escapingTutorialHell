def index_of_caps(word):
    ans = []

    for i, char in enumerate(word): # keep track of the iteration
        if char.isupper(): # if char is uppercase
            ans.append(i) # append the iteration (which would be the index

    return ans