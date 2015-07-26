import simplegui

# initialize state
width = 200
height = 200
position = [10, 20]
radius = 2
velocity = [3,0.7]

# event handlers
#def keydown(key):
#    if key == simplegui.KEY_MAP['down']:
#        position[1] = position[1] - velocity[1]
#        position[0] = position[0] - velocity[0]
#    elif key == simplegui.KEY_MAP['up']:
#        position[1] = position[1] + velocity[1]
#        position[0] = position[0] + velocity[0]
#    
#    

def tick():
    position[0]+=velocity[0]
    position[1]+=velocity[1]
    
def draw(canvas):
    canvas.draw_circle(position, radius, 2, "red", "red")
    canvas.draw_line((50, 50), (50, 140), 2, "White")
    canvas.draw_line((50, 140), (180, 140), 2, "White")
    canvas.draw_line((180, 50), (50, 50), 2, "White")
    canvas.draw_line((180, 140), (180, 50), 2, "White")



# create frame
frame = simplegui.create_frame("Key Handling", width, height)
timer=simplegui.create_timer(300,tick)
# register event handlers
#frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

# start frame
frame.start()
timer.start()