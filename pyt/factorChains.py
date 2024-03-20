'''

A factor chain is a list where each previous element is a factor of the next consecutive element.

The following is a factor chain:

[3, 6, 12, 36]

# 3 is a factor of 6
# 6 is a factor of 12
# 12 is a factor of 36

Create a function that determines whether or not a list is a factor chain.

'''


def factor_chain(lst):
    count = 0
    length = len(lst)

    for i in range(length - 1):
        if lst[i + 1] % lst[i] == 0:
            count += 1

    if count == length - 1: # -1 because it only loops length - 1 times if true
        return True
    else:
        return False


if __name__ == "__main__":
    print(factor_chain([1, 2, 4, 8, 16, 32]))