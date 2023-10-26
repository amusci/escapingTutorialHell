"""Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)"""

s = input("Please input a string to check if it's a palindrome or not: ")

if s == s[::-1]:
    print(f'{s} is a palindrome.')
else:
    print('are you dumb')

