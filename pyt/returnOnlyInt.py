def filter_list(l):
    lst = []

    for i in l:
        if isinstance(i, (int, float)):
            lst.append(i)

    return lst