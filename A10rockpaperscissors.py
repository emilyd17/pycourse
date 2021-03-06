#-------------------------------------------------------------------------------------------
# Name:         Emily Dayanghirang
# Date:         03-29-2020
# Reference:    page # 329 problem # 12
# Title:        Rock, Paper, Scissors Game
# Inputs:       String input of 'rock','paper',or 'scissors'
# Process:      Uses the randint function from the random library and a decision structure
#               to determine the computer's choice of rock, paper, or scissors.
#               It also uses a decision structure and a repition structure in
#               determining the winner of the game and in playing the game again
#               when a certain condition is met, respectively.
# Outputs:      (1) The computer's choice of rock, paper, or scissors
#               (2) Decision of who won the game by teling the user he/she won or lost
#-------------------------------------------------------------------------------------------

import random

def main():
    # Initialize boolean variable
    play = True

    # Introduction
    print('The Game of Rock, Paper, Scissors: User Vs. The Machine\n')

    # Keep iterating(playing the game) until False
    while play:
        # Assign random integer in the range of 1 through 3 to number variable
        number = random.randint(1,3)

        # Determine computer's choice of rock, paper, or scissors
        if number == 1:
            compchoice = 'rock'
        elif number == 2:
            compchoice = 'paper'
        else:
            compchoice = 'scissors'

        # Inform user that the computer has already chosen
        print('The computer has determined its choice of rock, paper, or scissors...\n')

        # Prompt user to enter his/her choice of rock, paper, or scissors
        userchoice = input('Enter your choice of rock, paper, or scissors: ')

        # Display computer's choice
        print('The computer\'s choice is ',compchoice,'.',sep='')

        # Display line break
        print()

        # Assign the returned boolean value
        # From determinewinner function to play variable
        play = determinewinner(compchoice,userchoice)
        print()

# Function that determines the winner
# Also determies whether the game is a tie or not
def determinewinner(comp,user):
    # Using case-insensitive string comparisons
    # Return True if the game is a tie
    # Return False if the game is not a tie
    if comp.lower() == 'rock' and user.lower() == 'rock':
        print('Tie. Play again.\n')
        return True
    elif comp.lower() == 'rock' and user.lower() == 'paper':
        print('You won!')
        return False
    elif comp.lower() == 'rock' and user.lower() == 'scissors':
        print('You lost!')
        return False
    elif comp.lower() == 'paper' and user.lower() == 'rock':
        print('You lost!')
        return False
    elif comp.lower() == 'paper' and user.lower() == 'paper':
        print('Tie. Play again.\n')
        return True
    elif comp.lower() == 'paper' and user.lower() == 'scissors':
        print('You won!')
        return False
    elif comp.lower() == 'scissors' and user.lower() == 'rock':
        print('You won!')
        return False
    elif comp.lower() == 'scissors' and user.lower() == 'paper':
        print('You lost!')
        return False
    elif comp.lower() == 'scissors' and user.lower() == 'scissors':
        print('Tie. Play again.\n')
        return True
    else:
        print('Error. Play again.\n')
        return True

main()
    
