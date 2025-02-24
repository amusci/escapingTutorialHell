
'''

Parity bits are used as very simple checksum to ensure that binary data isn't corrupted during transit. Here's how they work:

    If a binary string has an odd number of 1s, the parity bit is a 1.
    If a binary string has an even number of 1s, the parity bit is a 0.
    The parity bit is appended to the end of the binary string.

Create a function that validates whether a binary string is valid, using parity bits.

'''

def validate_binary(b):
    zero_count = 0
    one_count = 0

    for i in b:
        print(i)
        if i == "0":
            zero_count += 1
        elif i == "1":
            one_count += 1
    if b[-1] == "0":
        
        if one_count % 2 == 0:
            return True
        else:
            return False
    elif b[-1] == "1":
        if zero_count % 2 == 0:
            return True
        else:
            return False



if __name__ == "__main__":
    print(validate_binary("10010010"))