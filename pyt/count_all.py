'''Write a function that takes a string and calculates the number of letters and digits within it.

Return the result in a dictionary.'''


def count_all(str):
    ans = {"LETTERS": 0, "DIGITS": 0}
    for i in str:
        if i.isalpha():
            ans["LETTERS"] += 1
        elif i.isdigit():
            ans["DIGITS"] += 1
    return ans