# implementation of card game - Memory
import math
import simplegui
import random

# helper function to initialize globals
def new_game():
    global deck, state, turn
    vals = range(8) + range(8)
    random.shuffle(vals)
    pos = range (25, 750, 50)
    deck = []
    for i in range(len(vals)):
        deck.append([vals[i], 25 + 50 * i, False])  
    # last two exposed
    card0Idx = -1
    card1Idx = -1
    # number of exposed cards
    state = 0   
    turn = 0

def dist(p, q):
    return abs(p[0] - q[0])
     
def update(i):
    global state, card0Idx, card1Idx, turn
    
    deck[i][2] = True
    if state == 0:       
        card0Idx = i
        state = 1
    elif state == 1:
        card1Idx = i
        state = 2
        turn += 1
    else:
        if deck[card0Idx][0] != deck[card1Idx][0]:
            deck[card0Idx][2] = False
            deck[card1Idx][2] = False
        card0Idx = i
        state = 1
        
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, turns
    for i in range(len(deck)):
        if abs(pos[0] - deck[i][1]) < 25:
            # if turned down
            if not deck[i][2]:
                update(i)  
     
# cards are logically 50x100 pixels in size    
def draw(canvas):   
    for i in range(len(deck)):
        if deck[i][2]:
            canvas.draw_text(str(deck[i][0]),(deck[i][1] - 10, 60), 40, "White")
    for i in range(50, 800, 50):
        canvas.draw_line([i, 0],[i, 100], 2, "Gray")   
    label.set_text("Turns = " + str(turn))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric