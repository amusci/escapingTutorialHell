# DICTIONARY DAT

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


def twoListsOneMeat(l1, l2):
    meat = dict(zip(l1, l2))
    print(meat)


if __name__ == "__main__":
    twoListsOneMeat(keys, values)
