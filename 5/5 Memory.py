# implementation of card game - Memory

import simplegui
import random
cards = []
exposed = []
selected_card_index = -1
state = 0
card1 = -1
card2 = -1
turns = 0
# helper function to initialize globals
def new_game():
    global cards, exposed, state, turns, selected_card_index,card1,card2
    cards = []
    exposed = []
    selected_card_index = -1
    state = 0
    card1 = -1
    card2 = -1
    turns = 0
    label.set_text("Turns : " + str(turns))
    cards =range(8)
    cards.extend(cards)
    random.shuffle(cards)
    for i in range(0,16):
        exposed.append(False)
    # print i, exposed[i]
    #exposed[1]=False
    #print deck  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global selected_card_index, state, card1, card2, turns
      
    selected_card_index = (pos[0]//50)
    #print selected_card_index
   
    #if(exposed[selected_card_index]==False):
     #   exposed[selected_card_index]=True
    if state == 0:
        exposed[selected_card_index]=True
        card1 = selected_card_index
        state = 1
        print "card1 " + str(cards[card1]) 
    elif state == 1:
        print "\nstate " + str(state)
        if(exposed[selected_card_index]==False):
            exposed[selected_card_index]=True
            card2 = selected_card_index
            state = 2
            print "card2 " + str(cards[card2])
            turns+=1	
            label.set_text("Turns : " + str(turns))
    else:
        print "\nstate " + str(state)
        if(cards[card1]!=cards[card2]):
            exposed[card1] = False
            exposed[card2] = False   
            
            
        if(exposed[selected_card_index]==False):
            exposed[selected_card_index]=True
            card1 = selected_card_index
            print "card1 " + str(cards[card1])
            state = 1
            
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    width = 50
    height = 100
    for card_index in range(len(cards)):
        card_pos = 50 * card_index
        if(exposed[card_index]):
            canvas.draw_text(str(cards[card_index]), [card_pos,50], 25, "Blue")
        else:
              canvas.draw_polygon([(width*card_index, 0),  (width*card_index + width, 0),(width*card_index + width, height), (width*card_index, height)],
                            1, "White", "Green")

            #print card_index, exposed[card_index]
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns : " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric