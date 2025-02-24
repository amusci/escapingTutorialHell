'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


'''

def bruteForceTwoSum(nums, target):
    for i in range(len(nums)): # start pointer i at the first index
        for j in range(i + 1, len(nums)): # start pointer j at the i + 1 index to scan each element to the right, stop at the length of the list
            if nums[i] + nums[j] == target: # if the two numbers = the target
                return [i,j] # return the pair of indicies 
            

def twoSum(nums, target):
    hashMap = {} # value : index
    for i,n in enumerate(nums): # i will be index, n will be the value
        diff = target - n # calculate the difference between the target and the current value
        if diff in hashMap: # if the diff is in the Hash Map
            return [hashMap[diff], i] # return the pair of indicies
        hashMap[n] = i # value : index




if __name__ == "__main__":


    #print(bruteForceTwoSum([2,3,11,4], 7))
    print(twoSum([2,3,11,4], 7))


