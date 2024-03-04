"""

Given a list of scrabble tiles (as dictionaries),

create a function that outputs the maximum possible score a player can achieve by summing up the total number of points

for all the tiles in their hand. Each hand contains 7 scrabble tiles.



"""


def maximum_score(tile_hand):
    score = 0
    for i in tile_hand:
        score += i["score"]
    return score