"""

In BlackJack, cards are counted with -1, 0, 1 values:

    2, 3, 4, 5, 6 are counted as +1
    7, 8, 9 are counted as 0
    10, J, Q, K, A are counted as -1

Create a function that counts the number and returns it from the list of cards provided.

"""


def count(deck):
    count = 0
    plus_one = [2, 3, 4, 5, 6]
    negative_one = [10, 'J', 'Q', 'K', 'A']

    for card in deck:

        if card in plus_one:
            count += 1

        elif card in negative_one:
            count -= 1

    return count