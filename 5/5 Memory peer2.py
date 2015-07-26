# implementation of card game - Memory

import simplegui
import random

deck = []
exposed = []
state = 0
card1 = -1
card2 = -1
turns = 0

CARD_WIDTH = 800/16

# helper function to initialize globals
def new_game():
    global deck
    global exposed
    global state
    global card1
    global card2
    global turns
    
    #Creater randomly ordered deck
    deck = range(8)
    deck.extend(range(8))
    random.shuffle(deck)
    
    exposed = [False] * 16
    state = 0
    card1 = -1
    card2 = -1
    turns = 0


# define event handlers
def mouseclick(pos):
    global state
    global card1
    global card2
    global turns
    global exposed
    
    card_index = pos[0]//CARD_WIDTH
    
    #Process click only if card is
    #not yet exposed
    if(exposed[card_index]==False):
        #Expose the card
        exposed[card_index] = True
        
        if state == 0:
            #First Card clicked            
            card1 = card_index            
            state = 1
        elif state == 1:
            #Second Card clicked
            card2 = card_index 
            turns = turns + 1
            state = 2
        else:
            #Third Card clicked (new pair)            
            if(deck[card1] != deck[card2]):
                exposed[card1] = False
                exposed[card2] = False            
            card1 = card_index
            state = 1
        
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global CARD_WIDTH
    label.set_text("Turns = " + str(turns))
    
    #Draw cards either exposed or covered
    for card_index in range(len(deck)):        
        if(exposed[card_index]):  
            canvas.draw_text(str(deck[card_index]), [10 + (CARD_WIDTH * card_index), 60], 40, "White")
        else:
            canvas.draw_polygon([[CARD_WIDTH * card_index,0],[CARD_WIDTH * (card_index +1),0],[CARD_WIDTH * (card_index +1),100],[CARD_WIDTH * card_index,100]], 2, "Maroon", "Green")

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

