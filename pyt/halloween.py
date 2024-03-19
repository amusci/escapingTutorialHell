"""

Create a function that takes date in the format yyyy/mm/dd as an input


and returns "Bonfire toffee" if the date is October 31, else return "toffee".

"""


def halloween(dt):
    split = dt.split("/")
    if split[1] == '10' and split[2] == '31':
        return "Bonfire toffee"
    else:
        return "toffee"