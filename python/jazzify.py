def jazzify(lst):
    last_char = '7'
    empty_lst = []

    if not lst:
        return lst
    else:

        for i in lst:
            if not i.endswith(last_char):
                empty_lst.append(i + "7")
            if i.endswith(last_char):
                empty_lst.append(i)

        return empty_lst