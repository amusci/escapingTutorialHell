def is_curzon(num):
    first_part = 2 ** num + 1
    second_part = 2 * num + 1

    if num >= 0:
        if first_part % second_part == 0:
            return True

    return False