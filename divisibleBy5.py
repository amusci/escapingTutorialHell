l = [10, 20, 33, 46, 55,65,75,32321,100]
n =[]
d = []

for i in l:
    if i % 5 == 0:
        d.append(i)
    else:
        n.append(i)

print(d)