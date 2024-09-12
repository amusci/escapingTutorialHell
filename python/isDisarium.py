'''

A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.

Create a function that determines whether a number is a Disarium or not.

'''

def is_disarium(n):
    digits = [int(digit) for digit in str(n)]
    hello = enumerate(digits, start=1)
    return sum(digit ** position for position, digit in hello) == n
    
    



if __name__ == "__main__":
    print(is_disarium(518))