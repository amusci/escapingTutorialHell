def is_triplet(n1, n2, n3):
    a1 = max(n1, n2, n3)
    a2 = min(n1, n2, n3)
    a3 = (n1 + n2 + n3) - a1 - a2

    if (a2 ** 2) + (a3 ** 2) != a1 ** 2:
        return False
    else :
        return True