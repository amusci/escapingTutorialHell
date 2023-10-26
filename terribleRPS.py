# RPS
# NEED TO GO BACK AND MAKE IT BETTER IM BRAINDEAD RN SORRY

import random

rps = ['R', 'P', 'S']

user = input('Rock, Paper, or Scissors?: ')

com = random.choice(rps)

if user.lower() == 'rock':
    if com == 'R':
        print('computer chose ROCK. It results in a DRAW')
    elif com == 'P':
        print('computer chose PAPER. It results in a LOSS')
    else:
        print('computer chose Scissors. It results in a WIN')

elif user.lower() == 'paper':
    if com == 'R':
        print('computer chose ROCK. It results in a WIN')
    elif com == 'P':
        print('computer chose PAPER. It results in a DRAW')
    else:
        print('computer chose Scissors. It results in a LOSS')

elif user.lower() == 'scissors':
    if com == 'R':
        print('computer chose ROCK. It results in a WIN')
    elif com == 'P':
        print('computer chose PAPER. It results in a WIN')
    else:
        print('computer chose Scissors. It results in a DRAW')
