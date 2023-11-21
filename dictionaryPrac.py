# DICTIONARY DAT

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}


def twoListsOneMeat(l1, l2):
    # combines two lists into one meat
    meat = dict(zip(l1, l2))
    print(meat)


def twoMeatOneMeat(d1, d2):
    # combines two meat to one meat
    oneMeat = {**d1, **d2}
    print(oneMeat)


def describeOneMeat():
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

    # understand how to locate the nested key
    # sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
    # sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
    # sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}

    print(sampleDict['class']['student']['marks']['history'])


def diffKeysSameValues(l1, d1):
    out = dict.fromkeys(l1, d1)
    print(out)


if __name__ == "__main__":
    diffKeysSameValues(employees, defaults)
