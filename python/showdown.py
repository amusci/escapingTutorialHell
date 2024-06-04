"""

Wild Roger is participating in a Western Showdown,

meaning he has to draw (pull out and shoot) his gun faster than his opponent in a gun standoff.

Given two strings,p1 and p2, return which person drew their gun the fastest.

If both are drawn at the same time, return "tie".

"""

def showdown(p1, p2):
    shot1, shot2 = p1.index('B'), p2.index('B')
    return 'p1' if shot1 < shot2 else 'p2' if shot2 < shot1 else 'tie'