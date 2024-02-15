"""
Your spouse is not concerned with the loss of material possessions but rather with his/her favorite pet. Is it gone?!

Given a dictionary of the stolen items and a string in lowercase representing the name of the pet (e.g. "rambo"),

return:

    "Rambo is gone..." if the name is on the list.
    "Rambo is here!" if the name is not on the list.
"""

def find_it(items, name):
    if not items:
        return name.capitalize() + " is here!"
    else:
        for i in items:
            if i == name:
                return name.capitalize() + " is gone..."
            else:
                return name.capitalize() + " is here!"