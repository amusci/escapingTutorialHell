"""

Create a function that takes an integer and returns a list from 1 to the given number, where:

    If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the number).
    If the number cannot be divided evenly by 4, simply return the number.



"""

def amplify(num):
    lst = []
    for i in range(1,num+1):
        if i % 4 == 0:
            lst.append(i*10)
        else:
            lst.append(i)

    return lst