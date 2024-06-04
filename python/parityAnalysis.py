def parity_analysis(num):
    num_string = str(num)
    sum = 0
    for i in num_string:
        sum += int(i)
    print(sum % 2)
    print(num % 2)
    if num % 2 == 0 and sum % 2 == 0:
        return True
    elif num % 2 != 0 and sum % 2 != 0:
        return True

    else:
        return False