def XO(txt):
    countX = 0  # initalize x count
    countO = 0  # initalize o count

    for i in txt.lower():  # for each character in txt
        if i == 'x':  # if char == x
            countX += 1  # add 1 to the counter
        elif i == 'o':  # if char  == o
            countO += 1  # add 1 to the counter

    if countX == countO:  # if the counters equal each other
        return True  # the x and o must be the same

    else:
        return False
