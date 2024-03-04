"""

Return the smallest number of steps it takes to convert a string entirely into uppercase or entirely into lower case,

whichever takes the fewest number of steps.

A step consists of changing one character from lower to upper case, or vice versa.

"""

def steps_to_convert(txt):
    lower = len([i for i in txt if i.islower()])
    upper = len([i for i in txt if i.isupper()])
    return min(lower,upper)