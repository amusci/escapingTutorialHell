# takes the set list, finds the items in the list that are less than 5


set_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
less_than = 5

for i in set_list:
    if i < less_than:
        new_list.append(i)

print(new_list)
