def find_odd(lst):
    for i in range(0, len(lst)):
        count = 0
        for j in range (0, len(lst)):
            if lst[i] == lst[j]:
                count += 1

        if count % 2 != 0:
            return lst[i]