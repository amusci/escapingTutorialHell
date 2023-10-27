"""

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very
first exercise)

Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""

import random

count = 0
ran_num = 0
user = None

while user != ran_num:
    user = int(input('input a number between 1 - 9: '))
    ran_num = random.randint(0,10)
    if user == ran_num:
        print('YOU GUESSED IT OMG')
    elif user > ran_num:
        print('The inputted number is higher than the number you are trying to guess.')
    elif user < ran_num:
        print('The inputted number is less than the number you are trying to guess.')


