def shortestDistance(txt):
    xy_list = txt.split(",")
    x1 = int(xy_list[0])
    x2 = int(xy_list[2])
    y1 = int(xy_list[1])
    y2 = int(xy_list[3])

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(distance, 2)