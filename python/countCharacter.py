def count_characters(lst):
    count = 0

    for i in lst:
        for j in i:
            count += 1

    return count