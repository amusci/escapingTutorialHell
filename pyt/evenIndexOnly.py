inp = input('What is the string you would like to chop up?: ')

print(f"The original string is:{inp}")

for i, c in enumerate(inp):
    if i%2 == 0:

        print(f"Index {i}: {c}")



