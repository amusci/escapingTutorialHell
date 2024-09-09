'''

Write a program that takes a temperature input in celsius and converts it to Fahrenheit and Kelvin. Return the converted temperature values in a list.

The formula to calculate the temperature in Fahrenheit from Celsius is:

F = C*9/5 +32

The formula to calculate the temperature in Kelvin from Celsius is:

K = C + 273.15

'''


def temp_conversion(celsius):

    kelvin = round(celsius + 273.15,2)
    fahrenheit = round(celsius * 9/5 + 32,2)
    if kelvin < 0:
        return "Invalid"
    else:
        return [fahrenheit,kelvin]




if __name__ == "__main__":
    print(temp_conversion(100))