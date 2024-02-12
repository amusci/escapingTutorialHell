def contains_duplicateSet(nums):
    seen = set()  # create a set (NO DUPLICATES)
    for num in nums:  # iterate through the list of numbers
        print(seen)
        if num in seen:  # if the num is in seen
            return True  # return true
        seen.add(num)  # ties to the for loop, adding numbers to the set

    return False  # return false if no duplicates


def contains_duplicatesSort(nums):
    nums.sort()  # sort the list
    for i in range(1, len(nums)):  # interate through the list
        if nums[i] == nums[i - 1]:  # if index 2 == index 1
            return True  # return true if dups
    return False  # return false if no dups


def contains_duplicatesBF(nums):
    n = len(nums) # n is the length of the list
    for i in range(n - 1): # iterate through list
        for j in range(i + 1, n): # use second pointer
            if nums[i] == nums[j]: # compare two pointers
                return True # return true
    return False # return false


def contains_duplicatesHM(nums):
    seen = {}  # create a hashmap
    for num in nums:  # iterate through list
        if num in seen and seen[num] >= 1:  # if num is in hasmap and the keys >= 1
            return True  # return true, this would mean there are duplicates
        seen[num] = seen.get(num, 0) + 1  # increase count in the map
    return False  # return false since no dups

