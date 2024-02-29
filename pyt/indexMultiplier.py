"""

Return the sum of all items in a list, where each item is multiplied by its index (zero-based).

For empty lists, return 0.

"""


def index_multiplier(lst):
    n = len(lst)
    ans = 0
    for x,y in enumerate(lst):
        ans += x * y
    return ans