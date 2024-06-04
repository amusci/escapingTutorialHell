"""

Create a function that takes date in the format yyyy/mm/dd as an input


and returns "Bonfire toffee" if the date is October 31, else return "toffee".

"""


def halloween(dt):
    return 'Bonfire toffee' if dt.endswith('10/31') else 'toffee'