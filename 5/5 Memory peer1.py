# implementation of card game - Memory

import simplegui
import random
CARD_WIDTH = 50
CARD_NUM = 16

# helper function to initialize globals
def new_game():
    global decks, exposed, state, turns
    decks = range(CARD_NUM // 2) * 2
    random.shuffle(decks)
    exposed = [False] * CARD_NUM
    state = 0
    turns = 0
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, last_flip_idx1, last_flip_idx2, turns
    idx = pos[0] // CARD_WIDTH
    if not exposed[idx]:
        exposed[idx] = True
        if state == 0:
            state = 1
            last_flip_idx1 = idx
        elif state == 1:
            last_flip_idx2 = idx
            state = 2
            turns += 1          
        else:
            if decks[last_flip_idx1] != decks[last_flip_idx2]:
                exposed[last_flip_idx1] = exposed[last_flip_idx2] = False
            last_flip_idx1 = idx
            state = 1
                      
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global decks, exposed
    text_pos = [10, 70]
    for num in decks:
        canvas.draw_text(str(num), text_pos, 60, 'Red')
        text_pos[0] += CARD_WIDTH
    
    for idx in range(CARD_NUM):
        if not exposed[idx]:
            canvas.draw_polygon(([CARD_WIDTH * idx, 0], [CARD_WIDTH * idx, 100],
                                 [CARD_WIDTH * (idx + 1), 100],[CARD_WIDTH * (idx + 1), 0]),
                                1, "Blue", "Lime")
    label.set_text('Turns = ' + str(turns))
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