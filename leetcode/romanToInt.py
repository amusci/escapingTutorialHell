# https://leetcode.com/problems/roman-to-integer/description/

def romanToInt(s):

    numerals = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    
    total = 0

    for i in range(len(s)): # iterate through string
        print(total)

        current_val = numerals[s[i]] 

        next_val =  numerals[s[i+1]] if i + 1 < len(s) else 0 # bounds check

        total += -current_val if current_val < next_val else +current_val # IV (1 < 5) -1 + 5
    
    return total