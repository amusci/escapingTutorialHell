"""

Return the smallest number of steps it takes to convert a string entirely into uppercase or entirely into lower case,

whichever takes the fewest number of steps.

A step consists of changing one character from lower to upper case, or vice versa.

"""

def steps_to_convert(txt):
    n = len(txt)
    upper_list = []
    lower_list = []
    for i in txt:
        if i.isupper():
            upper_list.append(i)
        else:
            lower_list.append(i)

    if len(upper_list) > len(lower_list):
        return n - len(upper_list)
    else:
        return n - len(lower_list)