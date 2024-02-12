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
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            print(nums[i], nums[j])
            if nums[i] == nums[j]:
                return True
    return False
