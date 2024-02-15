

def find_even_nums(num):
    vals = [n for n in range(1, num + 1) if n % 2 == 0] # make sure it's n for n to start
    return vals