"""

You work in a toy car workshop, and your job is to build toy cars from a collection of parts.

Each toy car needs 4 wheels, 1 car body, and 2 figures of people to be placed inside.

Given the total number of wheels, car bodies and figures available, how many complete toy cars can you make?

"""


def cars(wheels, bodies, figures):
    ans = 0
    if wheels < 4 or bodies < 1 or figures < 2:
        return 0
    else:
        while wheels >= 4 and bodies >= 1 and figures >= 2:
            ans += 1
            wheels -= 4
            bodies -= 1
            figures -= 2
        return ans