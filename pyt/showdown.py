"""

Wild Roger is participating in a Western Showdown,

meaning he has to draw (pull out and shoot) his gun faster than his opponent in a gun standoff.

Given two strings,p1 and p2, return which person drew their gun the fastest.

If both are drawn at the same time, return "tie".

"""

def showdown(p1, p2):
    bet = " "
    bang = "B", "a", "n", "g", "!"

    p1_count = 0
    p2_count = 0
    for i in p1:
        if i in bet:
            p1_count += 1
        elif i in bang:
            break

    for j in p2:
        if j in bet:
            p2_count += 1
        elif j in bang:
            break

    print(p1_count, p2_count)
    if p1_count < p2_count:
        return "p1"
    elif p2_count < p1_count:
        return "p2"
    else:
        return "tie"