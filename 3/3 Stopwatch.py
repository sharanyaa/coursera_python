# template for "Stopwatch: The Game"

import simplegui
# define global variables
interval = 100
time = 0
win_count = 0
stop_count = 0
flag = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    
#    print time
    a1 = 0
    b1 = 0
    c1 = 0
    d1 = 0
    sec = 0
    
    d1 = time % 10
    time //= 10
    
    a1 = time // 60
    sec = time % 60
    c1 = sec % 10
    b1 = sec // 10
#    print str(a1)+"min "+str(b1)+str(c1)+"sec "+str(d1)+ "msec"
#    print str(a1) + ":" + str(b1) + str(c1) + "." + str(d1) + "\n"
#    a = str(a1)
#    d = str(d1)
#    c = str(c1)
#    b = str(b1)
#    t = a + ":" + b + c + "." + d + "\n"
#    return str(a1) + ":" + str(b1) + str(c1) + "." + str(d1) + "\n"
    return str(a1) + ":" + str(b1) + str(c1) + "." + str(d1)
    pass

def draw_counters():
    return str(win_count) + "/" + str(stop_count)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global flag
    timer.start()
    flag = True
    
def stop():
    timer.stop()
    global stop_count, win_count, flag
    # if timer is running and stopped, increment counters
    if(flag == True):
        stop_count += 1
        if((time % 10) == 0):
            win_count += 1
            
    # if timer is already stopped:        
    flag = False
        
    
def reset():
    global time, stop_count, win_count
    stop_count = 0
    win_count = 0
    time = 0
    

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1
    if(time > 5999):
        time = 0

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time),[200,250], 50, "White")
    canvas.draw_text(draw_counters(), [400,50], 40, "Blue")
    
# create frame
frame = simplegui.create_frame('Stopwatch', 500, 500)

# register event handlers
start_btn = frame.add_button("Start", start, 50)
stop_btn = frame.add_button("Stop", stop, 50)
reset_btn = frame.add_button("Reset", reset, 50)
frame.set_draw_handler(draw)
timer=simplegui.create_timer(interval,tick)

# start frame
frame.start()

# Please remember to review the grading rubric
