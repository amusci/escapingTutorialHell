"""

Imagine a messaging device with only one button.

For the letter A, you press the button one time, for E, you press it five times, for G, it's pressed seven times, etc, etc.

Write a function that takes a string (the message) and returns the total number of times the button is pressed.

"""

def how_many_times(msg):
    alphabet_dict = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)} # make da dictionary where a =
    # 1, b = 2, etc
    string_list = list(msg)
    count = 0
    for char in string_list:
        if char in alphabet_dict:
            count += alphabet_dict[char] # add the value of the char
    return count