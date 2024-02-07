def sum_odd_and_even(lst):
    even = []
    odd = []
    final = []

    for i in lst:
        if i % 2 == 0:
            even.append(i)
        elif i % 2 != 0:
            odd.append(i)

    final.append(sum(even))
    final.append(sum(odd))
    return final