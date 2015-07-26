# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
paddle1_pos = 160
paddle2_pos = 160
paddle1_vel = 0
paddle2_vel = 0
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0,0]
acc = 7
score1 = 0
score2 = 0
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if(direction == "LEFT"):
        ball_vel[0] -= (random.randrange(120,240))
        ball_vel[1] -= (random.randrange(60,180))
        ball_vel[0] = -2
        ball_vel[1] = -2
        ball_vel[0] -= (random.randrange(1,5))
        ball_vel[1] -= (random.randrange(1,5))
        
    if(direction == "RIGHT"):
        ball_vel[0] += random.randrange(120,240)
        ball_vel[1] -= (random.randrange(60,180))
        ball_vel[0] = 2
        ball_vel[1] = -2
        ball_vel[0] += random.randrange(1,5)
        ball_vel[1] -= (random.randrange(1,5))
    #print ball_pos, ball_vel

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel, acc  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = 160
    paddle2_pos = 160
    paddle1_vel = 0
    paddle2_vel = 0
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [0,0]
    acc = 7
    score1 = 0
    score2 = 0
    spawn_ball("RIGHT")

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
            
    # draw ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    #print ball_pos
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Red", "Orange")
    
    # update paddle's vertical position, keep paddle on the screen
    
    
    # draw paddles
    if(paddle1_pos + paddle1_vel >= 0 and paddle1_pos + paddle1_vel <= HEIGHT-PAD_HEIGHT):
        paddle1_pos += paddle1_vel
    if(paddle2_pos + paddle2_vel >= 0 and paddle2_pos + paddle2_vel <= HEIGHT-PAD_HEIGHT):
        paddle2_pos += paddle2_vel
    canvas.draw_line([0,paddle1_pos], [0,paddle1_pos + PAD_HEIGHT], PAD_WIDTH, 'White')
    canvas.draw_line([WIDTH-1,paddle2_pos], [WIDTH-1,paddle2_pos + PAD_HEIGHT], PAD_WIDTH, 'White')
  
    
    # determine whether paddle and ball collide
    if(ball_pos[1] <= BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    if(ball_pos[1] >= HEIGHT - 1 - BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
        
    if(ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH)): #left gutter
        if(ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + PAD_HEIGHT):  #paddle
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] += ball_vel[0]*0.1
            ball_vel[1] += ball_vel[1]*0.1
        else:
            ball_pos = [WIDTH/2, HEIGHT/2]
            score2 += 1
            spawn_ball("RIGHT")
            
    if(ball_pos[0] >= WIDTH - 1 - PAD_WIDTH - BALL_RADIUS): #right gutter
        if(ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos + PAD_HEIGHT): #paddle
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] += ball_vel[0]*0.1
            ball_vel[1] += ball_vel[1]*0.1
        else:
            ball_pos = [WIDTH/2, HEIGHT/2]
            score1 += 1
            spawn_ball("LEFT")
    
    # draw scores
    canvas.draw_text(str(score1), [150, 50], 50, 'White')
    canvas.draw_text(str(score2), [450, 50], 50, 'White')
        
def keydown(key):
    global paddle1_vel, paddle2_vel, acc
    if(key == simplegui.KEY_MAP["w"] ):
        paddle1_vel -= acc
    if(key == simplegui.KEY_MAP["s"] ):
        paddle1_vel += acc
    if(key == simplegui.KEY_MAP["up"] ):
        paddle2_vel -= acc
    if(key == simplegui.KEY_MAP["down"] ):
        paddle2_vel += acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel, acc
    if(key == simplegui.KEY_MAP["w"] ):
        paddle1_vel += acc
    if(key == simplegui.KEY_MAP["s"] ):
        paddle1_vel -= acc
    if(key == simplegui.KEY_MAP["up"] ):
        paddle2_vel += acc
    if(key == simplegui.KEY_MAP["down"] ):
        paddle2_vel -= acc

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
btn = frame.add_button('Restart', new_game)
s1= "Left controls: W, S"
s2= "Right controls: Up, Down "
label1 = frame.add_label(s1)
label2 = frame.add_label(s2)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
