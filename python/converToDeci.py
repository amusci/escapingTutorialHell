"""

Create a function to convert a list of percentages to their decimal equivalents.

"""
def convert_to_decimal(perc):
    return [float(i.strip('%')) / 100 for i in perc]