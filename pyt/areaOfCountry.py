"""

Create a function that takes a country's name and its area as arguments and returns

the area of the country's proportion of the total world's landmass.

"""


def area_of_country(name, area):

    return name + " is " + "{:>2%}".format(area / 148940000) + "of the total world's landmass"
