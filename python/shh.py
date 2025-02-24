'''

Write a function that removes all capital letters from a sentence except the first letter, puts quotation marks around the sentence and adds ", whispered Edabit." at the end.

'''

def shhh(txt):

    if len(txt) <= 2:
        return '"", whispered Edabit'
    else:
        return '"' + txt[0].upper() + txt[1:].lower() + '"' + ', whispered Edabit.'



if __name__ == "__main__":
    print(shhh(""))