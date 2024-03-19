"""

A museum wants to get rid of some exhibitions.

Katya, the interior architect, comes up with a plan to remove the most boring exhibitions.

She gives them a rating, and removes the one with the lowest rating.

Just as she finishes rating the exhibitions, she's called off to an important meeting.

She asks you to write a program that tells her the ratings of the items after the lowest one is removed.

"""


def remove_smallest(lst):
    if not lst:
        return []
    else:
        lst.remove(min(lst))
    return lst