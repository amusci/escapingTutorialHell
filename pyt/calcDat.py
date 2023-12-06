# Create a Python function that accepts three parameters. The first parameter should be an integer,  the second
# parameter should be a mathematical operator:+, -, /, or, and the third parameter should also be an integer.


def calcDat(a, op, b):
    if op == '+':
        c = a + b
    elif op == '-':
        if a > b:
            c = a - b
        elif a == b:
            c = 0
        else:
            c = b - a
    elif op == '*':
        c = a * b

    print(c)


if __name__ == "__main__":
    a = int(input('Please input the first integer: '))
    b = int(input('Please input the second integer: '))
    op = input('Please input the operation: ')
    calcDat(a, op, b)
