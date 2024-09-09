'''

Write a function that inverts the keys and values of a dictionary

'''


def invert(dct):
    return {y:x for (x,y) in dct.items()}
        
        


if __name__ == "__main__":
    print(invert({ "zebra": "koala", "horse": "camel" }))