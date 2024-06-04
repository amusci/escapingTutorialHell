def marathon_distance(d):
    ans = 0
    for i in d:
        ans += abs(i)

    if ans == 25:
        return True
    else:
        return False