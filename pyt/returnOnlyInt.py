def filter_list(l):
    lst = []

    for i in l:
        if isinstance(i, (int, float)):
            lst.append(i)

    return lst

def return_only_integer(lst):
    return [i for i in lst if type(i)==int]