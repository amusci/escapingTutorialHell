'''
You are given two numbers a and b.

Create a function that returns the next number greater than a and b and divisible by b.
'''


'''
divisible_by_b(17, 8) ➞ 24

divisible_by_b(98, 3) ➞ 99

divisible_by_b(14, 11) ➞ 22
'''


def divisible_by_b(a, b):
    final_number = a
    while (final_number % b != 0):
        final_number += 1
    
    return final_number

print(divisible_by_b(14, 11))

