def calculator(num1, operator, num2):
    res = 0
    if operator == "/":
        if num2 == 0:
            return "Can't divide by 0!"
        else:
            res = num1 / num2
    elif operator == "+":
        res = num1 + num2
    elif operator == "-":
        res = num1 - num2
    elif operator == "*":
        res = num1 * num2

    return res