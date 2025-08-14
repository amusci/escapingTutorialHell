# https://leetcode.com/problems/palindrome-number/solutions/?envType=problem-list-v2&envId=nbx51cxj

def palindromeToString(num):

    return str(num) == str(num) [::-1]

def palindromeNoString(x):

    if x < 0: # negatives can't be palindromes
        return False

    rev = 0 
    num = x # copy x

    while num != 0: 
        
        rev = rev * 10 + num % 10 # num % 10 is the last digit.
                                  # rev * 10 shifts existing digits to the left
        num = num // 10 # remove the last digit in num

    return rev == x # compare and return 