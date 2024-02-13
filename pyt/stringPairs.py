def string_pairs(s):
    n = len(s)  # get length of string
    pairs = []  # empty list for the pairs

    if n == 0:  # if the string is empty
        return []  # return []
    elif n % 2 == 0:  # if even
        for i in range(0, n, 2):  # iterate 0 to n, every 2
            pairs.append(s[i:i + 2])  # append the pairs (0:2) (2:4) etc
    else:
        for i in range(0, n - 1, 2):  # iterate 0 to n-1 every 2 (n-1 allows to get the even pairs
            # (this will allow the ability to add the *))
            pairs.append(s[i:i + 2])  # append the pairs (0:2) (2:4) etc
        pairs.append(s[-1] + '*')  # at the end, get the last index and then add an asterisk

    return pairs  # return
