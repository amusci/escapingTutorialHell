'''

Steve and Maurice have racing snails.

They each have three, a slow s, medium m and fast f one. Although Steve's
snails are all a bit stronger than Maurice's, Maurice has a trick up his sleeve. His plan is:

    Round 1: [s, f] Sacrifice his slowest snail against Steve's fastest.
    Round 2: [m, s] Use his middle snail against Steve's slowest.
    Round 3: [f, m] Use his fastest snail against Steve's middle.

Create a function that determines whether Maurice's plan will work by outputting True if Maurice wins 2/3 games.

The function inputs:

    List 1: [s, m, f] for Maurice.
    List 2: [s, m, f] for Steve.

'''


def maurice_wins(m_snails, s_snails):
    rounds = [
        (m_snails[0], s_snails[-1]),
        (m_snails[1], s_snails[0]),
        (m_snails[-1], s_snails[1])
    ]

    count = sum(m > s for m, s in rounds)

    return count >= 2