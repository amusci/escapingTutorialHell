'''
Write a function that transforms all letters from [a, m] to 0 and letters from [n, z] to 1 in a string.
'''


def convert_binary(string):
    ans = ''
    a_to_m = 'abcdefghijklm'
    for char in string.lower():
        if char in a_to_m:
            ans += '0'
        else:
            ans += '1'
    return ans