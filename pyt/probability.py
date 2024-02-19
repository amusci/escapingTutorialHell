"""

Given a list of numbers and a value n,
write a function that returns the probability of choosing a number greater than or equal to n from the list.
The probability should be expressed as a percentage, rounded to one decimal place.

"""

def probability(lst, n):
    total_possible = len(lst)
    new_list = []

    for i in lst:
        if i >= n:
            new_list.append(i)

    print(new_list)

    return round(100 * (len(new_list) / total_possible),1)