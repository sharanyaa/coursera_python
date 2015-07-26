# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

secret_number = 0
range = 100
max_guesses = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, count
    # remove this when you add your code 
    if(range == 100):
        max_guesses = 7
    else:
        max_guesses = 10
    count = max_guesses    
    print "New Game with Range: 0 - ",range
    secret_number = random.randrange(0,range)
    # print range,"  ",secret_number
    pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range, max_guesses
    range = 100
    new_game()
    # remove this when you add your code    
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range, max_guesses
    range = 1000
    new_game()
    pass
    
def input_guess(guess):
    # main game logic goes here	
    global count
    print "Number of remaining guesses : " , count
    count -= 1
    if (count != -1):
        my_guess = int(guess)
        print "Guess was ", my_guess
        # remove this when you add your code
        if (secret_number < my_guess):
            print "Lower"
        elif (secret_number > my_guess):
            print "Higher"
        else:
            print "Correct. You Win."
            print
            new_game()
    else:
        print "Out of guesses. You Lose. My guess was ", secret_number
        print
        new_game()
    pass

    
# create frame
frame = simplegui.create_frame("Guess The Number", 200, 200)
input = frame.add_input("My Guess: " , input_guess, 50)
btn1 = frame.add_button("Range: 0 - 100", range100)
btn2 = frame.add_button ("Range: 0 - 1000", range1000)
# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
