inp = int(input('What number would you like the range of?: '))
print(f'Printing current and previous number sum in a range({inp})')

for i in range(inp):
    if i == 0:
        print(f'Current number {i} Previous number {0}')
    else:

        ans = i + i-1

        print(f'Current number {i} Previous number {i - 1} SUM: {ans}')
