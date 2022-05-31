import random
import os
import time
def clr():
    os.system('clear')


def game():
    inputs = {
        'r': 'ROCK',
        'p': 'PAPER',
        's': 'scissors'
    }
    validInputs = ['r', 'p', 's']
    while True:
        print('----------------------------------')
        print('''Rock Paper scissors game.
    "R" for "rock", 
    "P" for "paper", 
    "S" for "scissors".
    ''')
        userInput = input('Chose from above either R, P or S: ')
        userInput = userInput.lower()
        computer = random.choice(validInputs)
        if userInput in validInputs:
            if userInput == 'r' and computer == 's' or userInput == 'p' and computer == 'r' or userInput == 's' and computer == 'p':
                print(f'Player ({inputs[userInput]}) : CPU ({inputs[computer]})')
                print('Player won')
                time.sleep(3)
                break
            elif userInput == 's' and computer == 'r' or userInput == 'r' and computer == 'p'or userInput == 'p' and computer == 's':
                print(f'Player ({inputs[userInput]}) : CPU ({inputs[computer]})')
                print('Computer Won')  
                time.sleep(3)
                break
            elif userInput == computer:
                clr()
                print(f'Player ({inputs[userInput]}) : CPU ({inputs[computer]})')
                print('TIE')
                print('')
        else:
            clr()
            print('')
            print('----------------------------')
            print('ENTER A CORRECT VALUE')
            print('')


game()

