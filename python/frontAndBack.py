# numbers_x = [10, 20, 30, 40, 10]


numbers_x = []

inp = int(input('How big do you want this list to be?: '))

for i in range(0, inp):
    x = int(input(f'What should be number in the {i} index?: '))
    numbers_x.append(x)

print(numbers_x)

if numbers_x[0] == numbers_x[-1]:
    print('yeah')