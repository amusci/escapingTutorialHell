# DICTIONARY DAT

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}


def twoListsOneMeat(l1, l2):
    # combines two lists into one meat
    meat = dict(zip(l1, l2))
    print(meat)


def twoMeatOneMeat(d1, d2):
    # combines two meat to one meat
    oneMeat = {**d1, **d2}
    print(oneMeat)

#def describeOneMeat(meat)


if __name__ == "__main__":
    twoMeatOneMeat(dict1, dict2)
