'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Easy
Topics
Companies
Hint

Given an integer x, return true if x is a
palindrome
, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

    -231 <= x <= 231 - 1

'''

def isPalindromeWithString(x):
    return str(x) == str(x)[::-1] # We can just turn the integer input to a string and then compare it to the revered string

def isPalindromeWithoutString(x):
    if x < 0 : return False

    divider = 1

    while x >= 10  * divider:
        divider *= 10
    
    while x:
        rightDigit = x % 10
        leftDigit = x // divider

        if leftDigit != rightDigit: return False

        x = (x % divider) // 10

        divider = divider / 100

    return True




if __name__ == "__main__":

    #print(isPalindromeWithString(121))
    print(isPalindromeWithoutString(121))


