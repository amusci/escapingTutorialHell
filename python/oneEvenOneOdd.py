'''

Given a two digit number, return True if that number contains one even and one odd digit.

'''

def one_odd_one_even(n):

    stringfy = str(n)

    digit_one = int(stringfy[0])
    digit_two = int(stringfy[1])
    

    if digit_one % 2 == 0 and digit_two % 2 == 0:
        return False
    elif digit_one % 2 != 0 and digit_two % 2 != 0:
        return False
    else:
        return True



if __name__ == "__main__":
    print(one_odd_one_even(12))
    print(one_odd_one_even(55))
