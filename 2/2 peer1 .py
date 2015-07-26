import simplegui
import random
import math

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
range = 100
guesses = 7

# helper function to start and restart the game
def num_guesses():
    global range, guesses
    guesses = int(math.ceil(math.log(( range + 1 ), 2)))
    return guesses

def new_game():
    # initialize global variables used in your code here
    global secret_number, range
    secret_number = random.randrange(0,range)
    num_guesses()
    print "Let's play a game where I think of a number 0 through " + str(range) + ","
    print "and you have to guess the number. You only have " + str(guesses) + " guesses."
    print "I'll tell you if your next guess should be higher or lower"
    print ""

    # define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range
    range = 100
    new_game()    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range
    range = 1000
    new_game()    
   
def input_guess(guess):
    global secret_number, guesses
    x = int(guess)
    print "Guess was ", x
    guesses = guesses - 1
    if x == secret_number:
        print "Correct"
        print ""
        new_game()
    elif guesses < 1:
        print "Nope, and you're all out of guesses. Loser."
        print""
        new_game()
    elif x < secret_number:
        print "Higher."
        print str(guesses) + " guesses left."
        print ""
    elif x > secret_number:
        print "Lower."
        print str(guesses) + " guesses left."
        print ""
    else:
        print "I'm not sure what happened here"

    
# create frame
f = simplegui.create_frame("frame",200,200)


# register event handlers for control elements and start frame
f.add_input("input guess",input_guess,100)
f.add_button("range100",range100,100)
f.add_button("range1000",range1000,100)


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
