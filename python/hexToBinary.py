'''

Create a function that will take a HEX number and returns the binary equivalent (as a string).

'''


def to_binary(num):
    return bin(num)[2:]
    


if __name__ == "__main__":
    print(to_binary(0xFF))