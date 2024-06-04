def color_invert(rgb):
    inverted_list = []

    for i in rgb:
        inverted = abs(i - 255)
        inverted_list.append(inverted)


    return tuple(inverted_list)