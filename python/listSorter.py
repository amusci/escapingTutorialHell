def asc_des_none(lst, s):
    if s == "Asc":
        lst.sort()
        return lst
    elif s == "Des":
        lst.sort(reverse=True)
        return lst
    else:
        return lst