'''
Create a function that takes a list containing nested lists as an argument. Each sublist has 2 elements. The first element is the numerator and the second element is the denominator. Return the sum of the fractions rounded to the nearest whole number.

'''

'''
sum_fractions([[18, 13], [4, 5]]) ➞ 2

sum_fractions([[36, 4], [22, 60]]) ➞ 9

sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]) ➞ 11
'''


def sum_fractions(lst):
    total = 0
    for i in lst:
        total += i[0] / i[1]

    return round(total)





print(sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]))

