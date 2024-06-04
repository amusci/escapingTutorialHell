"""

Given an integer, return "odd" if the sum of all odd digits is greater than the sum of all even digits.

Return "even" if the sum of even digits is greater than the sum of odd digits, and "equal" if both sums are the same.

"""




def odds_vs_evens(num):
    odd = 0
    even = 0
    for i in str(num):
        if int(i) % 2 == 0:
            even += int(i)
        else:
            odd += int(i)
    if even > odd:
        return 'even'
    elif odd > even:
        return 'odd'
    else:
        return 'equal'