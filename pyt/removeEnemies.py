"""

Remove enemies from the list of people, even if the enemy shows up twice.

"""


def remove_enemies(names, enemies):
    ans = []
    for enemy in names:
        if enemy not in enemies:
            ans.append(enemy)
    return ans