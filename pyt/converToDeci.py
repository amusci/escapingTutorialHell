"""

Create a function to convert a list of percentages to their decimal equivalents.

"""
def convert_to_decimal(perc):
    ans = []
    for i in perc:
        ans.append(float(i.strip('%'))/100)
    return ans