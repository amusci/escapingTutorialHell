def solve_for_exp(a, b):
    count = 0

    while b != a:
        b = b / a
        count += 1
    return count + 1