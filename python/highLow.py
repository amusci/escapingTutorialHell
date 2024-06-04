'''

Create a function that accepts a string of space separated integers and returns the highest and lowest integers (as a string).
Examples

high_low("1 2 3 4 5") ➞ "5 1"

high_low("1 2 -3 4 5") ➞ "5 -3"

high_low("1 9 3 4 -5") ➞ "9 -5"

high_low("13") ➞ "13 13"

'''


def high_low(txt):
    ans = []

    nums = txt.split()

    for num in nums:
        ans.append(int(num))
    return "{} {}".format(max(ans), min(ans))