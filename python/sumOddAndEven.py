def sum_odd_and_even(lst):

    odd = 0
    even = 0

    for i in lst:
        if i % 2 == 0:
            even += i
        else:
            odd += i
    return [even,odd]
