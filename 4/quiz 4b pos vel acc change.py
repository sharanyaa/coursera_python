import simplegui

# initialize state
width = 2000
height = 2000
position = [1, 2]
radius = 2
acc=[0.2,0.2]
velocity = [0.3,0.7]

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
    acc[0]+=0.1
    acc[1]+=0.1
#    position[0]+=velocity[0]
#    position[1]+=velocity[1]
    
def draw(canvas):
    velocity[0]+=acc[0]
    velocity[1]+=acc[1]
    position[0]+=velocity[0]
    position[1]+=velocity[1]
    canvas.draw_circle(position, radius, 20, "red", "red")
#    canvas.draw_line((50, 50), (50, 140), 2, "White")
#    canvas.draw_line((50, 140), (180, 140), 2, "White")
#    canvas.draw_line((180, 50), (50, 50), 2, "White")
#    canvas.draw_line((180, 140), (180, 50), 2, "White")



# create frame
frame = simplegui.create_frame("Key Handling", width, height)
timer=simplegui.create_timer(170000,tick)
# register event handlers
#frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

# start frame
frame.start()
timer.start()