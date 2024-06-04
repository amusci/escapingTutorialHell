"""

Remove enemies from the list of people, even if the enemy shows up twice.

"""


def remove_enemies(names, enemies):
    return [i for i in names if i not in enemies]