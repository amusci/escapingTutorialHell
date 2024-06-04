c = int(input('how many columns: '))
r = int(input('how many rows: '))

for y in range(1, c + 1):  # columns
    for x in range(1, r + 1):  # row
        print(x * y, end=" ")
    print('\n\n')
