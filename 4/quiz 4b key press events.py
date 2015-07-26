import simplegui

# initialize state
width = 20
height = 20
position = [1, 2]
radius = 2
acc=[0.2,0.2]
velocity = [0.3,0.7]
x = 5
# event handlers
def keydown(key):
    global x
    x = x * 2
def keyup(key):
    global x
    x -= 3
    print x
    
# create frame
frame = simplegui.create_frame("Key Handling", width, height)
#timer=simplegui.create_timer(170000,tick)
# register event handlers
#frame.set_keydown_handler(keydown)
#frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
frame.start()
#timer.start()