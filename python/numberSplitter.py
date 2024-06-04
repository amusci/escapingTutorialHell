def number_split(n):
    if n % 2 == 0:
        return [n / 2, n / 2]
    if n % 2 == 1 and n > 0:
        return [int(n / 2), int(n / 2) + 1]

    if n % 2 == 1 and n < 0:
        return [int(n / 2) - 1, int(n / 2)]