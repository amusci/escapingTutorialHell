"""

Create a function that takes a country's name and its area as arguments and returns

the area of the country's proportion of the total world's landmass.

"""


def area_of_country(name, area):
    world_mass = 148940000
    country_mass = area / world_mass
    return name + " is " + "{:.2%}".format(country_mass) + " of the total world's landmass"