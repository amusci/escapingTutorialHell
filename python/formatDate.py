"""

Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

"""


def format_date(date):
    slash_split = date.split("/")
    return "{}{}{}".format(slash_split[2],slash_split[1],slash_split[0])