# program that takes the user input and determines if the number is even or odd
# oh and makes sure it's a digit for ur dumb ass l0l0l00l

number = input('Please enter a number to determine if the number is even or odd: ')

if number.isdigit():
    if int(number) % 2 == 0:
        print(f'{number} is an even number')
    else:
        print(f'{number} is an odd number')
else:
    print('dis hoe aint a digit are you stupid? dumb 00l0l0l0l0l')


