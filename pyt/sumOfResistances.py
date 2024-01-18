def series_resistance(lst):
    sum_of_list = 0

    for i in lst:
        sum_of_list += i
    if sum_of_list <= 1:
        return str(sum_of_list) + " ohm"
    else:
        return str(sum_of_list) + " ohms"