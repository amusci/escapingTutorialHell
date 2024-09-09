'''

Write a function that transforms a list of characters into a list of dictionaries, where:

    The keys are the characters themselves.
    The values are the ASCII codes of those characters.

'''


def to_dict(lst):
    result = []
    for i in lst:
        result.append({i: ord(i)})
    return result
    


if __name__ == "__main__":
    print(to_dict(["a", "b", "c"]))