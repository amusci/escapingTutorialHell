inp = int(input('What is your first number?: '))
inp2 = int(input('What is your second number?: '))

ans = inp * inp2

if ans <= 1000:
    print(ans)
else:
    ans2 = inp + inp2
    print(ans2)