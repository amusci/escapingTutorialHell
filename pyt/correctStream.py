"""

You're in the midst of creating a typing game.

Create a function that takes in two lists: the list of user-typed words,

and the list of correctly-typed words and outputs a list containing 1s (correctly-typed words) and -1s

(incorrectly-typed words).

"""


def correct_stream(user, correct):
    ans = []
    for x,y in zip(user,correct):
        if x == y:
            ans.append(1)
        else:
            ans.append(-1)
    return ans
