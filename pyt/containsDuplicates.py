def contains_duplicateSet(nums):
    seen = set() # create a set (NO DUPLICATES)
    for num in nums: # iterate through the list of numbers
        print(seen)
        if num in seen: # if the num is in seen
            return True # return true
        seen.add(num) # ties to the for loop, adding numbers to the set

    return False # return false if no duplicates